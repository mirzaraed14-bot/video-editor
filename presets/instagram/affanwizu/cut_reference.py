#!/usr/bin/env python3
"""
cut_reference.py: turn a rough-cut job into a caption job for build.py (no re-transcription).

  python presets/instagram/affanwizu/cut_reference.py projects/<job> --scale 125 --x 0.5127 [--y 0.5]

Reads   projects/<job>/transcript/cuts.json          (the EDL, source seconds, frame-snapped by splice.sh)
        projects/<job>/raw/<clip>                    (the raw take the EDL cuts)
        projects/<job>/outputs/<job>.transcript.json (the kept words remapped to the cut, by splice.sh)
Writes  projects/<job>/captions/raw/<job>-framed.mp4 (the cut, framed like the Premiere sequence: 1080x1920,
                                                      source scaled --scale % and centred at --x/--y)
        projects/<job>/captions/transcript/words.json (build.py's shape)
Then:   uv run presets/instagram/affanwizu/build.py projects/<job>/captions --prep   (and the usual steps)

The framing mirrors Premiere's Motion effect (Scale %, Position as a fraction of the frame, anchor 0.5/0.5),
so the chin measured on this file is the chin in the sequence.
"""
import argparse, json, os, subprocess, sys

W, H, FPS = 1080, 1920, 60


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("job_dir")
    ap.add_argument("--scale", type=float, default=125.0, help="Premiere Motion > Scale, percent")
    ap.add_argument("--x", type=float, default=0.5, help="Premiere Motion > Position x, fraction of the frame width")
    ap.add_argument("--y", type=float, default=0.5, help="Premiere Motion > Position y, fraction of the frame height")
    a = ap.parse_args()
    job = os.path.abspath(a.job_dir); name = os.path.basename(job)
    segs = json.load(open(os.path.join(job, "transcript", "cuts.json"), encoding="utf-8"))["segments"]
    tr = json.load(open(os.path.join(job, "outputs", f"{name}.transcript.json"), encoding="utf-8"))
    cap = os.path.join(job, "captions"); os.makedirs(os.path.join(cap, "raw"), exist_ok=True)
    os.makedirs(os.path.join(cap, "transcript"), exist_ok=True)

    clips = sorted({s["clip"] for s in segs})
    src = {c: os.path.join(job, "raw", c) for c in clips}
    for c, p in src.items():
        if not os.path.exists(p):
            sys.exit(f"[cut_reference] missing raw clip {p}")
    sw, sh = map(int, subprocess.check_output(
        ["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height", "-of", "csv=p=0",
         src[clips[0]]]).decode().strip().split(","))
    k = a.scale / 100.0
    vw, vh = round(sw * k / 2) * 2, round(sh * k / 2) * 2
    ox, oy = round(a.x * W - vw / 2), round(a.y * H - vh / 2)

    inputs, fc, parts = [], [], []
    for c in clips:
        inputs += ["-i", src[c]]
    idx = {c: i for i, c in enumerate(clips)}
    for n, s in enumerate(segs):
        i = idx[s["clip"]]
        fc.append(f"[{i}:v]trim={s['start']:.6f}:{s['end']:.6f},setpts=PTS-STARTPTS,fps={FPS},scale={vw}:{vh},setsar=1[s{n}];"
                  f"color=black:s={W}x{H}:r={FPS},setsar=1[b{n}];[b{n}][s{n}]overlay={ox}:{oy}:shortest=1,format=yuv420p[v{n}];"
                  f"[{i}:a]atrim={s['start']:.6f}:{s['end']:.6f},asetpts=PTS-STARTPTS[a{n}]")
        parts.append(f"[v{n}][a{n}]")
    fc.append("".join(parts) + f"concat=n={len(segs)}:v=1:a=1[v][a]")
    out = os.path.join(cap, "raw", f"{name}-framed.mp4")
    subprocess.run(["ffmpeg", "-v", "error", "-y", *inputs, "-filter_complex", ";".join(fc), "-map", "[v]", "-map", "[a]",
                    "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-c:a", "aac", "-b:a", "256k", out], check=True)

    words = [{"w": w["text"], "start": w["start"], "end": w["end"], "prob": w.get("prob", 1.0)}
             for w in tr["words"] if w.get("type", "word") == "word"]
    json.dump({"clips": [{"clip": os.path.basename(out), "words": words}]},
              open(os.path.join(cap, "transcript", "words.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=0)
    print(f"[cut_reference] {len(segs)} segments, {len(words)} words → {out}")
    print(f"[cut_reference] framing: {sw}x{sh} at {a.scale:g}% → {vw}x{vh} at ({ox},{oy}); next: build.py {cap} --prep")


if __name__ == "__main__":
    main()
