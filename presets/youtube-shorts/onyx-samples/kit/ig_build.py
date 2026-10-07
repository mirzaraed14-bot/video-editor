"""ig_build.py: build an Instagram-look sample from its spec, end to end (PLAYBOOK § 5).

  python presets/youtube-shorts/onyx-samples/kit/ig_build.py projects/<job> <version> [--preview] [--skip picture,overlay,mix]

Steps: the shared picture engine (onyx-samples-youtube/kit/yt_picture.py --dir ig: speaker crops, B-roll, splits, FIT cards,
push-ins; HARD cuts, no whips: the Instagram look cuts clean) → ig_captions.py (when "captions.chunks" is empty) →
ig_capy.py (captions placed just under the speaker's lips, per shot) → ig_overlay.py → HyperFrames render (transparent ProRes 4444) → the mix (voice + optional bed + one designed sound per graphic
entrance, from the library: Affan wanted MORE sound on this look) → composite → outputs/<job>.sample-ig.<version>.mp4.
"""
import json, os, re, shutil, subprocess, sys

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8")
    except Exception:
        pass

KIT = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(KIT, "..", "..", "..", ".."))
YTKIT = os.path.join(REPO, "presets", "youtube-shorts", "onyx-samples-youtube", "kit")
SFX = {"whoosh": ("assets/sfx/Simple Whoosh 1.wav", 0.0, -20), "pop": ("assets/sfx/Bubble Pop.wav", 0.0, -18), "tick": ("assets/sfx/Mac SFX 05.wav", 0.0, -20),
       "vibrate": ("assets/sfx/Phone Vibrate (synth).wav", 0.0, -24), "paper": ("assets/sfx/Paper 1.mp3", 0.0, -20),
       "pen": ("assets/sfx/Pencils & Markers.mp3", 0.0, -24), "notify": ("assets/sfx/UI Notification.wav", 1.03, -20)}   # the file opens with 1.03 s of silence
SFX.update(number=SFX["tick"], title=SFX["whoosh"], message=SFX["notify"], chat=SFX["notify"])   # the semantic kinds, on the old library


# The Epidemic Sound kit (assets/sfx/epidemic/MANIFEST.md; Affan 2026-10-07: "clear crisp sound effects which give off that high end
# podcast minimalistic vibe… you have Epidemic Sound at your side"). With "audio.sfx_kit": "epidemic" every cue kind maps to one of these
# files and is set by PEAK relative to the voice's own peak (dB under it), so a cue is audible by construction: the old -22 dB ticks
# under voice + bed read as "no sound effects" on a phone. A cue may carry "rel_db" (+/- a few dB) or an explicit "es" file name.
ES = {"pop": ("pop-glass", 6), "chip": ("pop-glass", 6), "card": ("pop-glass", 6), "pop-soft": ("pop-soft", 7), "tick": ("click", 0),
      "click": ("click", 0), "confirm": ("confirm", 7), "whoosh": ("whoosh-air", 6), "swoosh": ("whoosh-light", 7), "title": ("whoosh-light", 7),
      "hit": ("hit", 3), "number": ("hit", 3), "notify": ("notify", 3), "shutter": ("shutter", 8), "riser": ("riser", 8), "pen": ("click", 9),
      "paper": ("whoosh-light", 8), "vibrate": ("vibrate", 6), "message": ("message", 7), "chat": ("message", 7)}
# Where each file's sound actually starts (measured 2026-10-08, 5 ms RMS): trimmed off so the transient lands ON the cue. Without it
# pop-glass (a soft pre-tick, then the real pop at 0.595 s) and whoosh-light (silent to 0.42 s, crest 0.75 s) landed ~0.6 s after
# the card (Rich Roll QA r1). click/tick sat 8 dB under the voice and read as nothing on a phone: 0 dB now (r2: little body
# below 3.2 kHz, so a phone speaker needs the level).
ES_LEAD = {"pop-glass": 0.585, "whoosh-air": 0.14, "whoosh-light": 0.45, "vibrate": 0.34}


def peak_db(path):
    out = subprocess.run(["ffmpeg", "-hide_banner", "-i", path, "-af", "volumedetect", "-f", "null", "-"], capture_output=True, text=True).stderr
    m = [l for l in out.splitlines() if "max_volume" in l]
    return float(m[0].split("max_volume:")[1].split("dB")[0]) if m else -6.0


def fps_arg(fps):
    """HyperFrames wants NTSC rates as a fraction."""
    for num, den in ((24000, 1001), (30000, 1001), (60000, 1001)):
        if abs(fps - num / den) < 1e-6:
            return f"{num}/{den}"
    return str(int(round(fps))) if abs(fps - round(fps)) < 1e-6 else str(fps)     # "30", never "30.0" (HyperFrames rejects it)


def out_fps(fps, spec):
    """The OUTPUT rate: 60 (59.94 for NTSC sources) so the caption rise tween renders smooth (Affan, 2026-10-07: "it looks like it's
    30 frames per second instead of 60"). The picture keeps its own cadence (each frame repeated); `spec.output_fps` overrides."""
    if spec.get("output_fps"):
        return float(spec["output_fps"])
    return 60000 / 1001 if abs(fps * 1001 - round(fps * 1001 / 1000) * 1000) < 1 and abs(fps - round(fps)) > 1e-6 else 60.0


def sh(cmd, cwd=None):
    print("·", " ".join(str(c) for c in cmd[:4]), "…", flush=True)
    if subprocess.run(cmd, cwd=cwd).returncode:
        sys.exit(f"ig_build: step failed: {' '.join(str(c) for c in cmd)}")


def lufs(path):
    r = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", path, "-af", "ebur128=peak=true", "-f", "null", "-"], capture_output=True, text=True).stderr
    return float(re.findall(r"I:\s+(-?[\d.]+) LUFS", r)[-1]), float(re.findall(r"Peak:\s+(-?[\d.]+) dBFS", r)[-1])


def mix(job, spec):
    a = spec["audio"]; fps = spec["fps"]; dur = spec["frames"] / fps
    w = os.path.join(job, "ig", "work")
    voice = os.path.join(w, "voice.wav")
    sh(["ffmpeg", "-v", "error", "-y", "-i", os.path.join(job, a["voice"]), "-vn", "-ac", "2", "-ar", "48000", "-t", f"{dur:.4f}", voice])
    vi, _ = lufs(voice)
    cues = json.load(open(os.path.join(w, "sfx-cues.json"), encoding="utf-8")) + a.get("sfx", [])
    inputs, fc, labels = ["-i", voice], [], ["[0:a]"]
    epidemic = a.get("sfx_kit") == "epidemic"
    vpk = peak_db(voice) if epidemic else 0.0
    pk_cache = {}
    for k, cue in enumerate(cues):
        if epidemic and (cue.get("es") or cue.get("kind") in ES):
            name, under = (cue["es"], ES.get(cue.get("kind"), ("", 7))[1]) if cue.get("es") else ES[cue["kind"]]
            f, lead = os.path.join("assets", "sfx", "epidemic", f"{name}.wav"), ES_LEAD.get(name, 0.0)
            if f not in pk_cache:
                pk_cache[f] = peak_db(os.path.join(REPO, f))
            gain = vpk - under + cue.get("rel_db", 0.0) - pk_cache[f]      # this cue's peak sits `under` dB below the voice's peak
            ms = int(round(max(0, cue["t"] - (0.06 if name.startswith("whoosh") else 0.01)) * 1000))   # a whoosh swells into its peak
            dur_s = 2.4
        else:
            f, lead, g = SFX.get(cue.get("kind"), (cue.get("file"), cue.get("lead", 0), cue.get("gain_db", -20)))
            g = a.get("sfx_gain", {}).get(cue.get("kind"), g)      # per-job level for a library sound ("audio.sfx_gain": {"whoosh": -12})
            gain = cue.get("gain_db", g)
            ms = int(round(max(0, cue["t"] - 0.05) * 1000))     # a whoosh peaks just after the motion starts
            dur_s = 1.2
        inputs += ["-i", os.path.join(REPO, f)]
        fc.append(f"[{len(inputs) // 2 - 1}:a]atrim=start={lead}:duration={dur_s},asetpts=PTS-STARTPTS,aresample=48000,aformat=channel_layouts=stereo,"
                  f"afade=t=in:d=0.005,volume={gain:.2f}dB,adelay={ms}|{ms},apad[s{k}]")
        labels.append(f"[s{k}]")
    if a.get("bed") and os.path.exists(os.path.join(job, a["bed"])):
        bed = os.path.join(w, "bed-cut.wav")
        sh(["ffmpeg", "-v", "error", "-y", "-ss", f"{a.get('bed_in', 0):.3f}", "-t", f"{dur:.4f}", "-i", os.path.join(job, a["bed"]),
            "-af", f"afade=t=out:st={dur - 1.0:.3f}:d=1.0", "-ar", "48000", "-ac", "2", bed])
        bi, _ = lufs(bed)
        inputs += ["-i", bed]
        fc.append(f"[{len(inputs) // 2 - 1}:a]aresample=48000,aformat=channel_layouts=stereo,volume={(vi - a.get('bed_under_lu', 18)) - bi:.2f}dB,apad[bed]")
        labels.append("[bed]")
    fc.append(f"{''.join(labels)}amix=inputs={len(labels)}:duration=first:normalize=0,atrim=0:{dur:.4f}[m]")
    premix = os.path.join(w, "premix.wav")
    sh(["ffmpeg", "-v", "error", "-y", *inputs, "-filter_complex", ";".join(fc), "-map", "[m]", "-ar", "48000", premix])
    ti, ttp = a.get("target_i", -13.0), a.get("target_tp", -1.5)
    out = os.path.join(w, "mix.wav"); gain = ti - lufs(premix)[0]
    for _ in range(3):
        sh(["ffmpeg", "-v", "error", "-y", "-i", premix, "-af",
            f"volume={gain:.3f}dB,aresample=192000,alimiter=limit={10 ** ((ttp - 0.3) / 20):.4f}:attack=5:release=50:level=0:latency=1,"
            f"aresample=48000,afade=t=out:st={dur - 0.010:.4f}:d=0.010", "-ar", "48000", out])
        mi, mtp = lufs(out)
        if abs(mi - ti) <= 0.15 and mtp <= ttp + 0.05:
            break
        gain += ti - mi
    print(f"mix: {len(cues)} sound cues, {mi:.1f} LUFS, true peak {mtp:.1f} dBTP")


def main():
    job, version = os.path.abspath(sys.argv[1]), sys.argv[2]
    skip = set(sys.argv[sys.argv.index("--skip") + 1].split(",")) if "--skip" in sys.argv else set()
    spec = json.load(open(os.path.join(job, "ig", "spec.json"), encoding="utf-8"))
    fps, dur = spec["fps"], spec["frames"] / spec["fps"]
    w = os.path.join(job, "ig", "work")
    if "picture" not in skip:
        sh(["uv", "run", "-q", os.path.join(YTKIT, "yt_picture.py"), job, "--stills", "--dir", "ig"])
    if "overlay" not in skip:
        if not spec.get("captions", {}).get("chunks"):
            sh([sys.executable, os.path.join(KIT, "ig_captions.py"), job])
        if spec.get("faces") and not spec.get("captions", {}).get("fixed_y"):     # captions just under the lips, per shot (Affan, 2026-10-06)
            sh([shutil.which("uv") or "uv", "run", "-q", os.path.join(KIT, "ig_capy.py"), job])
        sh([sys.executable, os.path.join(KIT, "ig_overlay.py"), job])
        sh([shutil.which("npx") or "npx", "--yes", "hyperframes@0.8.16", "render", ".", "--format", "mov", "--fps", fps_arg(out_fps(fps, spec)), "-o", "../work/overlay.mov", "--quiet"],
           cwd=os.path.join(job, "ig", "hf-overlay"))
    spec = json.load(open(os.path.join(job, "ig", "spec.json"), encoding="utf-8"))
    if "mix" not in skip:
        mix(job, spec)
    name = os.path.basename(job)
    out = os.path.join(job, "outputs", f"{name}.sample-ig.{version}.mp4")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    ofps = fps_arg(out_fps(fps, spec))
    fc = (f"[0:v]fps={ofps},scale=in_color_matrix=bt709:in_range=tv:out_range=full,format=gbrp[p];[1:v]fps={ofps},scale=in_color_matrix=bt601:out_range=full,format=gbrap[o];"
          "[p][o]overlay=format=gbrp:shortest=1,scale=out_color_matrix=bt709:out_range=tv,format=yuv420p,setparams=color_primaries=bt709:color_trc=bt709:colorspace=bt709[v]")
    sh(["ffmpeg", "-v", "error", "-y", "-i", os.path.join(w, "picture.mp4"), "-i", os.path.join(w, "overlay.mov"), "-i", os.path.join(w, "mix.wav"),
        "-filter_complex", fc, "-map", "[v]", "-map", "2:a", "-r", ofps, "-c:v", "libx264", "-crf", "16", "-preset", "slow", "-c:a", "aac", "-b:a", "320k",
        "-ar", "48000", "-movflags", "+faststart", "-t", f"{dur:.4f}", out])
    if "--preview" in sys.argv:
        sh(["ffmpeg", "-v", "error", "-y", "-i", out, "-vf", "scale=720:1280:flags=lanczos", "-c:v", "libx264", "-crf", "23", "-preset", "slow",
            "-c:a", "aac", "-b:a", "160k", "-movflags", "+faststart", out.replace(".mp4", ".preview.mp4")])
    print(f"✓ {out}")


if __name__ == "__main__":
    main()
