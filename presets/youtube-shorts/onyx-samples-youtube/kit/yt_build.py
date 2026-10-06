"""yt_build.py: build a whole YouTube-look sample from its spec (PLAYBOOK § 5), about 2-3 minutes end to end.

  python presets/youtube-shorts/onyx-samples-youtube/kit/yt_build.py projects/<job> <version> [--preview] [--skip picture,overlay,mix]

Runs, in order: yt_picture.py (pass 1) → workflows/whip-slide.py → yt_captions.py → yt_overlay.py → HyperFrames render
(transparent ProRes 4444) → yt_mix.py → the ffmpeg composite (in RGB so caption colours stay exact, BT.709 tagged) →
`<job>/outputs/<job>.sample-yt.<version>.mp4`. `--preview` also writes a 720p copy under 30 MB for phone review.
`--skip` reuses an earlier step's output (e.g. `--skip picture` after a caption-only change).
"""
import os, shutil, subprocess, sys   # npx is npx.cmd on Windows: resolved with shutil.which

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8")
    except Exception:
        pass

KIT = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(KIT, "..", "..", "..", ".."))


def sh(cmd, cwd=None):
    print("·", " ".join(str(c) for c in cmd[:4]), "…", flush=True)
    p = subprocess.run(cmd, cwd=cwd)
    if p.returncode:
        sys.exit(f"yt_build: step failed: {' '.join(str(c) for c in cmd)}")


def main():
    job, version = os.path.abspath(sys.argv[1]), sys.argv[2]
    skip = set()
    if "--skip" in sys.argv:
        skip = set(sys.argv[sys.argv.index("--skip") + 1].split(","))
    name = os.path.basename(job)
    import json
    spec = json.load(open(os.path.join(job, "yt", "spec.json"), encoding="utf-8"))
    fps, dur = spec["fps"], spec["frames"] / spec["fps"]
    w = os.path.join(job, "yt", "work")
    if "picture" not in skip:
        sh(["uv", "run", "-q", os.path.join(KIT, "yt_picture.py"), job, "--stills"])
        sh(["uv", "run", "-q", os.path.join(REPO, "workflows", "whip-slide.py"), os.path.join(w, "picture.mp4"), os.path.join(w, "shots.json"),
            os.path.join(w, "picture.whip.mp4")])
    if "overlay" not in skip:
        sh([sys.executable, os.path.join(KIT, "yt_captions.py"), job]) if "captions" not in skip else None
        if spec.get("faces") and not spec.get("captions", {}).get("fixed_y"):     # captions just under the lips, per shot (Affan, 2026-10-06)
            sh([shutil.which("uv") or "uv", "run", "-q", os.path.join(REPO, "presets", "youtube-shorts", "onyx-samples", "kit", "ig_capy.py"), job, "--dir", "yt"])
        sh([sys.executable, os.path.join(KIT, "yt_overlay.py"), job])
        sh([shutil.which("npx") or "npx", "--yes", "hyperframes@0.8.16", "render", ".", "--format", "mov", "--fps", str(fps), "-o", "../work/overlay.mov", "--quiet"],
           cwd=os.path.join(job, "yt", "hf-overlay"))
    if "mix" not in skip:
        sh([sys.executable, os.path.join(KIT, "yt_mix.py"), job])
    out = os.path.join(job, "outputs", f"{name}.sample-yt.{version}.mp4")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    fc = ("[0:v]scale=in_color_matrix=bt709:in_range=tv:out_range=full,format=gbrp[p];[1:v]scale=in_color_matrix=bt601:out_range=full,format=gbrap[o];"
          "[p][o]overlay=format=gbrp:shortest=1,scale=out_color_matrix=bt709:out_range=tv,format=yuv420p,"
          "setparams=color_primaries=bt709:color_trc=bt709:colorspace=bt709[v]")
    sh(["ffmpeg", "-v", "error", "-y", "-i", os.path.join(w, "picture.whip.mp4"), "-i", os.path.join(w, "overlay.mov"), "-i", os.path.join(w, "mix.wav"),
        "-filter_complex", fc, "-map", "[v]", "-map", "2:a", "-c:v", "libx264", "-crf", "16", "-preset", "slow", "-c:a", "aac", "-b:a", "320k",
        "-ar", "48000", "-movflags", "+faststart", "-t", f"{dur:.4f}", out])
    if "--preview" in sys.argv:
        sh(["ffmpeg", "-v", "error", "-y", "-i", out, "-vf", "scale=720:1280:flags=lanczos", "-c:v", "libx264", "-crf", "23", "-preset", "slow",
            "-c:a", "aac", "-b:a", "160k", "-movflags", "+faststart", out.replace(".mp4", ".preview.mp4")])
    print(f"✓ {out}")


if __name__ == "__main__":
    main()
