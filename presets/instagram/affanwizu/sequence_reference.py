"""Turn the creator's Premiere sequence into a caption job: read it, rebuild it, check it.

usage: python presets/instagram/affanwizu/sequence_reference.py "Sequence 31" projects/seq31-short
       (Premiere open with the project; the CEP bridge must answer `node lanes/premiere/premiere-bridge.mjs ping`)

1. READ    the named sequence through the bridge: every V1/A1 clip (source, in point, timeline start/end, Motion).
           -> <job>/transcript/sequence.json
2. REBUILD the cut so its timeline seconds ARE the sequence's seconds (PLAYBOOK § 2, GATE A):
           - audio: one ffmpeg per A1 clip, PCM joined sample-exact in Python, every timeline gap kept as silence;
           - picture: each V1 clip encoded on its own from the main video stream, at the SEQUENCE frame rate and with
             its own Scale / Position, then joined; for `chin-line.py` and build.py's frame snap (never time anything off it).
           -> <job>/raw/<job>-cut.mp4
           The cut ENDS where the last V1/A1 clip ends: a title graphic stretched past it on V2 doesn't count
           (Seq 25: the sequence ran to 191.3 s, the cut to 43.6 s).
3. CHECK   GATE A (audio length = cut end) and print the `--dur` build.py needs.

Why one script: these steps used to be ad-hoc session scripts; a 114-clip sequence (Seq 31, 11.8 min) broke the
one-filtergraph rebuild on Windows (WinError 206, command line too long), which the per-clip audio path avoids.
"""
import json, os, subprocess, sys, wave

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
BRIDGE = os.path.join(ROOT, "lanes", "premiere", "premiere-bridge.mjs")
SR = 48000

JSX = r"""(function(){
  var NAME=__NAME__, seq=null;
  for (var i=0;i<app.project.sequences.numSequences;i++) if (app.project.sequences[i].name===NAME) seq=app.project.sequences[i];
  if (!seq) { var n=[]; for (var i=0;i<app.project.sequences.numSequences;i++) n.push(app.project.sequences[i].name); return "ERROR: no "+NAME+" | have: "+n.join(", "); }
  var o={project:app.project.name, name:seq.name, end:seq.end/254016000000, w:seq.frameSizeHorizontal, h:seq.frameSizeVertical, fps:254016000000/Number(seq.timebase), v:[], a:[]};
  function speed(c){ var r=1; try{ r=Number(c.getSpeed()); }catch(e){} try{ if (c.isSpeedReversed()) r=-r; }catch(e){} return r||1; }
  function motion(c){ var r={}; for (var i=0;i<c.components.numItems;i++){ var k=c.components[i]; if (k.displayName=="Motion"){
      for (var j=0;j<k.properties.numItems;j++){ var p=k.properties[j]; try{ r[p.displayName]=String(p.getValue()); }catch(e){} } } } return r; }
  for (var t=0;t<seq.videoTracks.numTracks;t++){ var tr=seq.videoTracks[t]; for (var i=0;i<tr.clips.numItems;i++){ var c=tr.clips[i];
     o.v.push({t:t, name:c.name, s:c.start.seconds, e:c.end.seconds, i0:c.inPoint.seconds, sp:speed(c), path:c.projectItem?c.projectItem.getMediaPath():"", m:motion(c)}); } }
  for (var t=0;t<seq.audioTracks.numTracks;t++){ var tr=seq.audioTracks[t]; for (var i=0;i<tr.clips.numItems;i++){ var c=tr.clips[i];
     o.a.push({t:t, name:c.name, s:c.start.seconds, e:c.end.seconds, i0:c.inPoint.seconds, sp:speed(c), path:c.projectItem?c.projectItem.getMediaPath():""}); } }
  return JSON.stringify(o);
})()"""


def read_sequence(name):
    script = JSX.replace("__NAME__", json.dumps(name))
    r = subprocess.run(["node", BRIDGE, "execute_extendscript", json.dumps({"script": script})],
                       capture_output=True, text=True, encoding="utf-8")
    out = r.stdout
    try:
        j = json.loads(out); d = j.get("data", j)
        d = d.get("result", d) if isinstance(d, dict) else d
        out = d if isinstance(d, str) else json.dumps(d)
    except Exception:
        pass
    if "ERROR" in out[:200] or "{" not in out:
        sys.exit(f"sequence_reference: {out.strip()[:600] or r.stderr[-600:]}")
    return json.loads(out[out.index("{"):out.rindex("}") + 1])


def src_in(c):
    """The clip's real in point in its source file. On a speed-changed clip Premiere reports inPoint DIVIDED by the
    speed (ABW10 Seq 12: 0.8x clips read in=250.04 s on a 215.7 s file; the real in point is 250.04 x 0.8 = 200.03 s).
    Ignoring it pulled the wrong stretch of the take: 9 s of speech captioned out of 40 s."""
    return c["i0"] * abs(c.get("sp", 1))


def tempo(sp):
    """ffmpeg atempo chain for a speed (each stage 0.5-2.0): the voice plays at the clip's speed, pitch kept."""
    out, sp = [], abs(sp)
    while sp > 2.0: out.append("atempo=2.0"); sp /= 2.0
    while sp < 0.5: out.append("atempo=0.5"); sp /= 0.5
    if abs(sp - 1) > 1e-6: out.append(f"atempo={sp:.6f}")
    return ",".join(out)


def rebuild(d, job):
    name = os.path.basename(os.path.normpath(job))
    V = sorted([c for c in d["v"] if c["t"] == 0], key=lambda x: x["s"])
    A = sorted([c for c in d["a"] if c["t"] == 0], key=lambda x: x["s"])
    if not V or not A:
        sys.exit("sequence_reference: V1 or A1 is empty")
    if any(c.get("sp", 1) < 0 for c in V + A):
        sys.exit("sequence_reference: a V1/A1 clip is REVERSED; this rebuild doesn't do reverse playback yet")
    end = max(c["e"] for c in V + A)
    tmp = os.path.join(os.environ.get("TMP", "/tmp"), f"seqref_{name}")
    os.makedirs(tmp, exist_ok=True)
    pcm, pos = bytearray(), 0
    for a in A:
        target = round(a["s"] * SR)
        if target > pos:                                          # timeline gap -> silence
            pcm.extend(b"\0" * 4 * (target - pos)); pos = target
        n = round((a["e"] - a["s"]) * SR)
        sp, af = abs(a.get("sp", 1)), tempo(a.get("sp", 1))
        raw = subprocess.check_output(["ffmpeg", "-v", "error", "-ss", f"{src_in(a):.6f}", "-t", f"{n / SR * sp + 0.05:.6f}", "-i", a["path"],
                                       "-vn", *(["-af", af] if af else []), "-ac", "2", "-ar", str(SR), "-f", "s16le", "-"])
        if len(raw) < n * 4 * 0.98:
            sys.exit(f"sequence_reference: A1 clip at {a['s']:.2f}s returned {len(raw) / 4 / SR:.2f}s of audio for "
                     f"{n / SR:.2f}s on the timeline (in point {src_in(a):.2f}s, speed {sp}): the read in point is wrong")
        if target < pos:                                          # overlapping clips: the earlier one wins
            raw = raw[(pos - target) * 4:]; n -= pos - target
        raw = raw[:n * 4] + b"\0" * max(0, n * 4 - len(raw))
        pcm.extend(raw); pos += n
    if round(end * SR) > pos:
        pcm.extend(b"\0" * 4 * (round(end * SR) - pos))
    wav = os.path.join(tmp, "audio.wav")
    w = wave.open(wav, "wb"); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(bytes(pcm)); w.close()

    W, H = d["w"], d["h"]
    fps = round(float(d.get("fps") or 60), 3)      # the SEQUENCE frame rate: build.py snaps every caption switch to this
    #   picture's frame grid (a 10 fps picture put every switch on a 0.1 s grid: Seq 31-42)
    # Picture = one short encode PER CLIP from the main video stream only (`0:v:0`), then a stream-copy join.
    # The concat demuxer straight off the camera files gave an EMPTY picture on Seq 47: those CAM_*.MP4 carry a second
    # (MJPEG thumbnail) video stream and HEVC that the demuxer would not decode. Per clip also means per-clip framing.
    segs = []
    for k, v in enumerate(V):
        m = v["m"]
        sc = float(m.get("Scale", 100)) / 100
        px, py = (float(x) for x in m.get("Position", "0.5,0.5").split(","))
        sw, sh = map(int, subprocess.check_output(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
                                                   "stream=width,height", "-of", "csv=p=0", v["path"]]).decode().strip().split(",")[:2])
        vw, vh = round(sw * sc / 2) * 2, round(sh * sc / 2) * 2
        ox, oy = round(px * W - vw / 2), round(py * H - vh / 2)
        sp = abs(v.get("sp", 1))
        vf = (f"setpts=(PTS-STARTPTS)/{sp:.6f},scale={vw}:{vh},pad={max(W, vw + max(0, ox))}:{max(H, vh + max(0, oy))}:{max(0, ox)}:{max(0, oy)}:black,"
              f"crop={W}:{H}:{max(0, -ox)}:{max(0, -oy)},setsar=1,fps={fps}")
        seg = os.path.join(tmp, f"v{k:04d}.mp4")
        still = os.path.splitext(v["path"])[1].lower() in (".png", ".jpg", ".jpeg", ".webp", ".bmp", ".tif", ".tiff", ".psd")
        src = ["-loop", "1", "-i", v["path"]] if still else ["-ss", f"{src_in(v):.4f}", "-i", v["path"]]   # a still is ONE frame
        r = subprocess.run(["ffmpeg", "-v", "error", "-y", *src, "-t", f"{v['e'] - v['s']:.4f}",          # unless looped (Seq 12)
                            "-map", "0:v:0", "-an", "-vf", vf, "-c:v", "libx264", "-preset", "ultrafast", "-crf", "30", seg],
                           capture_output=True, text=True)
        if r.returncode: sys.exit(f"sequence_reference: picture clip {k} failed: {r.stderr[-400:]}")
        segs.append(seg)
    lst = os.path.join(tmp, "list.txt")
    with open(lst, "w", encoding="utf-8") as f:
        f.writelines(f"file '{x}'\n" for x in segs)
    framings = {(c["m"].get("Scale"), c["m"].get("Position")) for c in V}
    out = os.path.join(job, "raw", f"{name}-cut.mp4")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    r = subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-i", wav, "-map", "0:v:0", "-map", "1:a",
                        "-vf", f"tpad=stop_mode=clone:stop_duration={end:.2f}", "-t", f"{end:.4f}", "-r", f"{fps}",
                        "-c:v", "libx264", "-preset", "ultrafast", "-crf", "30", "-c:a", "aac", "-b:a", "256k", out],
                       capture_output=True, text=True)
    if r.returncode:
        sys.exit(f"sequence_reference: ffmpeg failed: {r.stderr[-800:]}")
    vstreams = subprocess.check_output(["ffprobe", "-v", "error", "-select_streams", "v", "-show_entries", "stream=index",
                                        "-of", "csv=p=0", out]).decode().split()
    if not vstreams:
        sys.exit("sequence_reference: the rebuilt cut has NO picture (chin-line and the frame snap need it)")
    got = float(subprocess.check_output(["ffprobe", "-v", "error", "-select_streams", "a:0", "-show_entries", "stream=duration",
                                         "-of", "csv=p=0", out]))
    gaps = sum(1 for a, b in zip(V, V[1:]) if b["s"] - a["e"] > 0.02)
    return out, end, got, gaps, len(V), len(framings)


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    name, job = sys.argv[1], sys.argv[2].rstrip("/\\")
    d = read_sequence(name)
    os.makedirs(os.path.join(job, "transcript"), exist_ok=True)
    json.dump(d, open(os.path.join(job, "transcript", "sequence.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    out, end, got, gaps, n, framings = rebuild(d, job)
    srcs = sorted({c["path"] for c in d["v"] if c["t"] == 0})
    print(f"{d['project']} · {d['name']}: {n} V1 clips, {gaps} timeline gap(s), {float(d.get('fps') or 0):.3f} fps, source {', '.join(srcs)}")
    if abs(d["end"] - end) > 0.05:
        print(f"  the sequence runs to {d['end']:.3f}s but the cut ends at {end:.3f}s (something on V2+ is stretched past it)")
    if framings > 1:
        print(f"  {framings} different Scale/Position values (each clip framed as in Premiere)")
    ok = abs(got - end) < 0.05
    print(f"  GATE A: audio {got:.3f}s vs cut {end:.3f}s -> {'OK' if ok else 'MISMATCH'}")
    print(f"  -> {out}\n  build.py ... --srt --dur {end:.3f}")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
