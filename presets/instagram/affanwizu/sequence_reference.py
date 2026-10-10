"""Turn the creator's Premiere sequence into a caption job: read it, rebuild it, check it.

usage: python presets/instagram/affanwizu/sequence_reference.py "Sequence 31" projects/seq31-short
       (Premiere open with the project; the CEP bridge must answer `node lanes/premiere/premiere-bridge.mjs ping`)

1. READ    the named sequence through the bridge: every V1/A1 clip (source, in point, timeline start/end, Motion).
           -> <job>/transcript/sequence.json
2. REBUILD the cut so its timeline seconds ARE the sequence's seconds (PLAYBOOK § 2, GATE A):
           - audio: one ffmpeg per A1 clip, PCM joined sample-exact in Python, every timeline gap kept as silence;
           - picture: the V1 clips through the concat demuxer at the SEQUENCE frame rate with the first clip's Scale /
             Position, for `chin-line.py` and for build.py's frame snap (keyframe-approximate: never time anything off it).
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
  function motion(c){ var r={}; for (var i=0;i<c.components.numItems;i++){ var k=c.components[i]; if (k.displayName=="Motion"){
      for (var j=0;j<k.properties.numItems;j++){ var p=k.properties[j]; try{ r[p.displayName]=String(p.getValue()); }catch(e){} } } } return r; }
  for (var t=0;t<seq.videoTracks.numTracks;t++){ var tr=seq.videoTracks[t]; for (var i=0;i<tr.clips.numItems;i++){ var c=tr.clips[i];
     o.v.push({t:t, name:c.name, s:c.start.seconds, e:c.end.seconds, i0:c.inPoint.seconds, path:c.projectItem?c.projectItem.getMediaPath():"", m:motion(c)}); } }
  for (var t=0;t<seq.audioTracks.numTracks;t++){ var tr=seq.audioTracks[t]; for (var i=0;i<tr.clips.numItems;i++){ var c=tr.clips[i];
     o.a.push({t:t, name:c.name, s:c.start.seconds, e:c.end.seconds, i0:c.inPoint.seconds, path:c.projectItem?c.projectItem.getMediaPath():""}); } }
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


def rebuild(d, job):
    name = os.path.basename(os.path.normpath(job))
    V = sorted([c for c in d["v"] if c["t"] == 0], key=lambda x: x["s"])
    A = sorted([c for c in d["a"] if c["t"] == 0], key=lambda x: x["s"])
    if not V or not A:
        sys.exit("sequence_reference: V1 or A1 is empty")
    end = max(c["e"] for c in V + A)
    tmp = os.path.join(os.environ.get("TMP", "/tmp"), f"seqref_{name}")
    os.makedirs(tmp, exist_ok=True)
    pcm, pos = bytearray(), 0
    for a in A:
        target = round(a["s"] * SR)
        if target > pos:                                          # timeline gap -> silence
            pcm.extend(b"\0" * 4 * (target - pos)); pos = target
        n = round((a["e"] - a["s"]) * SR)
        raw = subprocess.check_output(["ffmpeg", "-v", "error", "-ss", f"{a['i0']:.6f}", "-i", a["path"], "-t", f"{n / SR:.6f}",
                                       "-vn", "-ac", "2", "-ar", str(SR), "-f", "s16le", "-"])
        if target < pos:                                          # overlapping clips: the earlier one wins
            raw = raw[(pos - target) * 4:]; n -= pos - target
        raw = raw[:n * 4] + b"\0" * max(0, n * 4 - len(raw))
        pcm.extend(raw); pos += n
    if round(end * SR) > pos:
        pcm.extend(b"\0" * 4 * (round(end * SR) - pos))
    wav = os.path.join(tmp, "audio.wav")
    w = wave.open(wav, "wb"); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(bytes(pcm)); w.close()

    W, H = d["w"], d["h"]
    lst = os.path.join(tmp, "list.txt")
    with open(lst, "w", encoding="utf-8") as f:
        for v in V:
            f.write(f"file '{v['path']}'\ninpoint {v['i0']:.4f}\noutpoint {v['i0'] + v['e'] - v['s']:.4f}\n")
    framings = {(c["m"].get("Scale"), c["m"].get("Position")) for c in V}
    m = V[0]["m"]
    k = float(m.get("Scale", 100)) / 100
    px, py = (float(x) for x in m.get("Position", "0.5,0.5").split(","))
    sw, sh = map(int, subprocess.check_output(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
                                               "stream=width,height", "-of", "csv=p=0", V[0]["path"]]).decode().strip().split(",")[:2])
    vw, vh = round(sw * k / 2) * 2, round(sh * k / 2) * 2
    ox, oy = round(px * W - vw / 2), round(py * H - vh / 2)
    fps = round(float(d.get("fps") or 60), 3)                     # the SEQUENCE frame rate: build.py snaps every
    #   caption switch to this picture's frame grid (a 10 fps picture put every switch on a 0.1 s grid: Seq 31-42)
    vf = (f"fps={fps},scale={vw}:{vh},pad={max(W, vw + max(0, ox))}:{max(H, vh + max(0, oy))}:{max(0, ox)}:{max(0, oy)}:black,"
          f"crop={W}:{H}:{max(0, -ox)}:{max(0, -oy)},setsar=1,tpad=stop_mode=clone:stop_duration={end:.2f}")
    out = os.path.join(job, "raw", f"{name}-cut.mp4")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    r = subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-i", wav, "-map", "0:v", "-map", "1:a",
                        "-vf", vf, "-t", f"{end:.4f}", "-c:v", "libx264", "-preset", "ultrafast", "-crf", "28",
                        "-c:a", "aac", "-b:a", "256k", out], capture_output=True, text=True)
    if r.returncode:
        sys.exit(f"sequence_reference: ffmpeg failed: {r.stderr[-800:]}")
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
        print(f"  {framings} different Scale/Position values: the picture uses the first clip's (chin-line only)")
    ok = abs(got - end) < 0.05
    print(f"  GATE A: audio {got:.3f}s vs cut {end:.3f}s -> {'OK' if ok else 'MISMATCH'}")
    print(f"  -> {out}\n  build.py ... --srt --dur {end:.3f}")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
