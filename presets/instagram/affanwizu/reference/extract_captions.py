# /// script
# requires-python = ">=3.10"
# dependencies = ["numpy", "pillow"]
# ///
"""Pull the creator's burned-in captions out of a finished @affanwizu export, frame-exact.

usage: uv run extract_captions.py <export.mov> <out_dir> [--y0 950 --y1 1500]

Yellow (#FFD700) caption pixels are found in a horizontal band of the frame; every frame's caption
mask is compared with the previous one, and a switch is logged when the text changes. Writes
<out_dir>/<name>.segments.json (frame-exact on/off for every caption, empty stretches included) and
<name>.sheet-NN.png contact sheets (one full-res crop per caption, labelled #index and time) for
reading the text. The text itself is read off the sheets into <name>.captions.json by hand.
"""
import argparse, json, os, subprocess, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont

ap = argparse.ArgumentParser()
ap.add_argument("src"); ap.add_argument("out")
ap.add_argument("--y0", type=int, default=950); ap.add_argument("--y1", type=int, default=1500)
ap.add_argument("--switch", type=float, default=0.30, help="XOR/OR ratio that counts as a new caption")
a = ap.parse_args()
os.makedirs(a.out, exist_ok=True)
name = os.path.splitext(os.path.basename(a.src))[0]

pr = json.loads(subprocess.check_output(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
      "stream=width,height,r_frame_rate", "-of", "json", a.src]))["streams"][0]
W, H = pr["width"], pr["height"]; n, d = map(int, pr["r_frame_rate"].split("/")); fps = n / d
h = a.y1 - a.y0
p = subprocess.Popen(["ffmpeg", "-v", "error", "-i", a.src, "-vf", f"crop={W}:{h}:0:{a.y0}", "-f", "rawvideo",
                      "-pix_fmt", "rgb24", "-"], stdout=subprocess.PIPE)

def yellow(fr):
    r, g, b = (fr[..., i].astype(np.int16) for i in range(3))
    return (r > 170) & (g > 0.62 * r) & (b < 0.45 * g) & (r - b > 110)

masks, frames_keep = [], {}
i = 0
while True:
    buf = p.stdout.read(W * h * 3)
    if len(buf) < W * h * 3: break
    fr = np.frombuffer(buf, np.uint8).reshape(h, W, 3)
    m = yellow(fr)
    masks.append(np.packbits(m, axis=1))
    i += 1
p.wait()
N = len(masks)
# band = the rows whose yellow content CHANGES over time (captions), not the static neon
rows = np.stack([np.unpackbits(m, axis=1)[:, :W].sum(1) for m in masks]).astype(np.float32)   # N x h
act = np.abs(np.diff(rows, axis=0)).mean(0)
pk = act.argmax(); thr = act[pk] * 0.12
lo = pk; hi = pk
while lo > 0 and act[lo - 1] > thr: lo -= 1
while hi < h - 1 and act[hi + 1] > thr: hi += 1
lo = max(0, lo - 12); hi = min(h - 1, hi + 12)
lo, hi = int(lo), int(hi)
if (hi - lo + 1) % 2: hi = hi + 1 if hi < h - 1 else hi - 1     # yuv420: ffmpeg crops to even heights
band = (a.y0 + lo, a.y0 + hi)

def bm(k): return np.unpackbits(masks[k], axis=1)[lo:hi + 1, :W].astype(bool)
segs = []; cur = None; prev = None
for k in range(N):
    m = bm(k); cnt = int(m.sum())
    empty = cnt < 60
    if prev is None: new = True
    else:
        pe = prev.sum() < 60
        if empty and pe: new = False
        elif empty != pe: new = True
        else:
            x = np.logical_xor(m, prev).sum(); o = np.logical_or(m, prev).sum()
            new = (x / max(o, 1)) > a.switch
    if new:
        if cur: cur["f1"] = k; segs.append(cur)
        cur = {"f0": k, "empty": bool(empty)}
    prev = m
cur["f1"] = N; segs.append(cur)
# merge 1-frame flickers into their neighbour
clean = []
for s in segs:
    if clean and s["f1"] - s["f0"] <= 1 and not s["empty"]:
        clean[-1]["f1"] = s["f1"]; continue
    clean.append(s)
for j, s in enumerate(clean):
    s["i"] = j; s["t0"] = round(s["f0"] / fps, 4); s["t1"] = round(s["f1"] / fps, 4)
    s["dur"] = round(s["t1"] - s["t0"], 4)
json.dump({"src": a.src, "fps": fps, "frames": N, "band_y": band, "segments": clean},
          open(f"{a.out}/{name}.segments.json", "w"), indent=1)

# contact sheets: a full-res crop of each caption, 3 frames after it switches on
caps = [s for s in clean if not s["empty"]]
try: font = ImageFont.truetype("arial.ttf", 22)
except OSError: font = ImageFont.load_default()
crops = []
for s in caps:
    k = min(s["f0"] + 3, (s["f0"] + s["f1"]) // 2)
    t = k / fps
    need = W * (band[1] - band[0] + 1) * 3
    for back in range(0, 30, 3):                      # a seek at the very end can return nothing: step back
        out = subprocess.check_output(["ffmpeg", "-v", "error", "-ss", f"{max(0, t - back / fps):.4f}", "-i", a.src,
              "-frames:v", "1", "-vf", f"crop={W}:{band[1]-band[0]+1}:0:{band[0]}", "-f", "rawvideo", "-pix_fmt", "rgb24", "-"])
        if len(out) >= need: break
    out = out[:need]
    crops.append((s, Image.frombytes("RGB", (W, band[1] - band[0] + 1), out)))
PER = 22; LAB = 230
for sh in range(0, len(crops), PER):
    part = crops[sh:sh + PER]; ch = part[0][1].height
    img = Image.new("RGB", (W + LAB, ch * len(part)), (40, 40, 40))
    dr = ImageDraw.Draw(img)
    for r, (s, c) in enumerate(part):
        img.paste(c, (LAB, r * ch))
        dr.text((8, r * ch + ch // 2 - 12), f"#{s['i']:03d} {s['t0']:.2f}-{s['t1']:.2f}", fill=(255, 255, 255), font=font)
        dr.line([(0, r * ch), (W + LAB, r * ch)], fill=(90, 90, 90))
    img.save(f"{a.out}/{name}.sheet-{sh // PER + 1:02d}.png")
print(f"{name}: {N} frames @ {fps:g}  band y{band[0]}-{band[1]}  captions {len(caps)}  empty stretches "
      f"{sum(1 for s in clean if s['empty'])}  sheets {(len(caps) + PER - 1) // PER}")
