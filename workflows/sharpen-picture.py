"""sharpen-picture.py: Affan's finishing sharpen on a YT-kit job's picture track (asked twice: Morgan 2026-10-26 "a tad bit of unsharp mask
and sharpen", Patron 2026-10-28 "a slight tinge of sharpen and unsharp mask throughout the video"), so it is now a standard step.

  python workflows/sharpen-picture.py projects/<job>      (after yt_build.py; then yt_build.py <job> <version> --skip picture,overlay)

Two luma-only unsharp passes, the unsharp MASK (7x7, 0.45) then the sharpen (3x3, 0.35), chroma untouched, on the camera + B-roll only:
the drawn cards (B shots whose src is an mg-*.mp4 card) are excluded by frame range, so their type stays clean; captions and the
overlay are composited after, so they are never sharpened. Works on the picture the next composite reads: yt/work/picture.whip60.mov
(ProRes HQ) when the spec's fps_out is 60, else yt/work/picture.whip.mp4 (x264 CRF 12). The untouched picture is kept once as *.raw.*
and every run sharpens from it, so re-running never stacks the effect.
"""
import json, os, shutil, subprocess, sys

job = os.path.abspath(sys.argv[1])
spec = json.load(open(os.path.join(job, "yt", "spec.json"), encoding="utf-8"))
fps, out_fps = spec["fps"], spec.get("fps_out", spec["fps"])
k = int(round(out_fps / fps))
w = os.path.join(job, "yt", "work")
pic = os.path.join(w, f"picture.whip{int(out_fps)}.mov" if out_fps != fps else "picture.whip.mp4")
raw = pic.replace(".whip", ".whip.raw", 1) if out_fps == fps else pic.replace(".mov", ".raw.mov")
mark = pic + ".sharpened.json"                       # the fingerprint of this script's own output
st = os.stat(pic); ours = os.path.exists(mark) and json.load(open(mark)) == [st.st_size, int(st.st_mtime)]
if not os.path.exists(raw) or not ours:              # a fresh render (not our output) becomes the raw backup
    shutil.copy2(pic, raw)
cards = [(x["f0"] * k, x["f1"] * k - 1) for x in spec["shots"] if x["kind"] == "B" and os.path.basename(x["src"]).startswith("mg-")]
keep = "+".join(f"between(n\\,{a}\\,{b})" for a, b in cards)
en = f":enable='not({keep})'" if keep else ""
vf = (f"unsharp=luma_msize_x=7:luma_msize_y=7:luma_amount=0.45:chroma_amount=0{en},"
      f"unsharp=luma_msize_x=3:luma_msize_y=3:luma_amount=0.35:chroma_amount=0{en}")
enc = (["-c:v", "prores_ks", "-profile:v", "3", "-pix_fmt", "yuv422p10le"] if pic.endswith(".mov")
       else ["-c:v", "libx264", "-crf", "12", "-preset", "medium", "-pix_fmt", "yuv420p"])
tmp = pic + ".tmp" + os.path.splitext(pic)[1]
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", raw, "-vf", vf, *enc, "-r", str(out_fps), tmp], check=True)
os.replace(tmp, pic)
st = os.stat(pic); json.dump([st.st_size, int(st.st_mtime)], open(mark, "w"))
print(f"sharpened {os.path.basename(pic)} at {out_fps} fps from {os.path.basename(raw)}; cards excluded: {cards}")
