# /// script
# requires-python = ">=3.10"
# dependencies = ["numpy", "pillow"]
# ///
"""analyze.py — measure a reference video's editing style (the numbers a preset is written from).

  uv run presets/youtube/fern-inspired/reference/analyze.py <video.mp4> [...]

Per video, writes reference/analysis/<id>/:
  stats.json        cuts/min, shot-length distribution, luma/saturation, palette, loudness
  sheet-NN.png      contact sheets: one frame every SAMPLE s, 6x4 grid, timestamps burned in
  cuts.txt          every detected cut time (scene score > THRESH)
Reference videos are for ANALYSIS ONLY — nothing from them ships in an edit.
"""
import json, re, subprocess, sys, os, statistics
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw

HERE = Path(__file__).resolve().parent
THRESH = 0.30
SAMPLE = 5.0


def sh(*a):
    return subprocess.run(a, capture_output=True, text=True, encoding="utf-8", errors="replace")


def duration(v):
    return float(sh("ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", v).stdout.strip())


def cuts(v):
    r = sh("ffmpeg", "-hide_banner", "-i", v, "-an", "-vf", f"scale=320:-1,select='gt(scene,{THRESH})',showinfo", "-f", "null", "-")
    return [float(m) for m in re.findall(r"pts_time:([\d.]+)", r.stderr)]


def frames(v, dur, out):
    out.mkdir(parents=True, exist_ok=True)
    tmp = out / "_f"
    tmp.mkdir(exist_ok=True)
    sh("ffmpeg", "-v", "error", "-y", "-i", v, "-vf", f"fps=1/{SAMPLE},scale=320:180", str(tmp / "f%05d.png"))
    return sorted(tmp.glob("f*.png"))


def palette(imgs, k=8):
    px = np.concatenate([np.asarray(Image.open(p).convert("RGB").resize((64, 36))).reshape(-1, 3) for p in imgs]).astype(float)
    rng = np.random.default_rng(0)
    px = px[rng.choice(len(px), min(len(px), 60000), replace=False)]
    cent = px[rng.choice(len(px), k, replace=False)]
    for _ in range(25):
        lab = np.argmin(((px[:, None, :] - cent[None]) ** 2).sum(-1), axis=1)
        cent = np.array([px[lab == i].mean(0) if (lab == i).any() else cent[i] for i in range(k)])
    share = np.bincount(lab, minlength=k) / len(lab)
    order = np.argsort(-share)
    return [{"hex": "#%02x%02x%02x" % tuple(int(c) for c in cent[i]), "share": round(float(share[i]), 3)} for i in order]


def tone(imgs):
    L, S, dark = [], [], []
    for p in imgs:
        a = np.asarray(Image.open(p).convert("RGB")).astype(float) / 255
        mx, mn = a.max(-1), a.min(-1)
        luma = 0.2126 * a[..., 0] + 0.7152 * a[..., 1] + 0.0722 * a[..., 2]
        L.append(luma.mean()); S.append(np.where(mx > 0, (mx - mn) / np.maximum(mx, 1e-6), 0).mean()); dark.append((luma < 0.15).mean())
    return {"luma_mean": round(float(np.mean(L)), 3), "luma_p10": round(float(np.percentile(L, 10)), 3), "luma_p90": round(float(np.percentile(L, 90)), 3),
            "sat_mean": round(float(np.mean(S)), 3), "dark_pixel_share": round(float(np.mean(dark)), 3)}


def loudness(v):
    r = sh("ffmpeg", "-hide_banner", "-nostats", "-i", v, "-vn", "-af", "ebur128=framelog=quiet", "-f", "null", "-")
    g = lambda pat: (lambda m: float(m.group(1)) if m else None)(re.search(pat, r.stderr))
    return {"lufs": g(r"I:\s+(-?[\d.]+) LUFS"), "lra": g(r"LRA:\s+([\d.]+) LU")}


def sheets(imgs, out, per=24):
    for n in range(0, len(imgs), per):
        page = Image.new("RGB", (6 * 320, 4 * 180), (0, 0, 0))
        for j, p in enumerate(imgs[n:n + per]):
            im = Image.open(p).convert("RGB")
            d = ImageDraw.Draw(im)
            t = (n + j) * SAMPLE
            d.rectangle((0, 0, 58, 14), fill=(0, 0, 0))
            d.text((3, 2), f"{int(t // 60)}:{int(t % 60):02d}", fill=(255, 255, 0))
            page.paste(im, ((j % 6) * 320, (j // 6) * 180))
        page.save(out / f"sheet-{n // per:02d}.png")


for v in sys.argv[1:]:
    vid = Path(v).stem
    out = HERE / "analysis" / vid
    dur = duration(v)
    c = cuts(v)
    shots = np.diff([0.0] + c + [dur])
    imgs = frames(v, dur, out)
    stats = {
        "id": vid, "duration_s": round(dur, 1), "cuts": len(c), "cuts_per_min": round(len(c) / (dur / 60), 1),
        "shot_s": {"median": round(float(np.median(shots)), 2), "mean": round(float(np.mean(shots)), 2),
                   "p10": round(float(np.percentile(shots, 10)), 2), "p90": round(float(np.percentile(shots, 90)), 2),
                   "share_over_8s": round(float((shots > 8).mean()), 3)},
        "cuts_per_min_by_quarter": [round(sum(1 for t in c if q * dur / 4 <= t < (q + 1) * dur / 4) / (dur / 4 / 60), 1) for q in range(4)],
        "tone": tone(imgs), "palette": palette(imgs), "loudness": loudness(v),
    }
    (out / "stats.json").write_text(json.dumps(stats, indent=1))
    (out / "cuts.txt").write_text("\n".join(f"{t:.2f}" for t in c))
    sheets(imgs, out)
    print(json.dumps({k: stats[k] for k in ("id", "duration_s", "cuts_per_min", "shot_s", "tone", "loudness")}))
