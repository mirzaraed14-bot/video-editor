# /// script
# dependencies = ["opencv-python-headless==4.10.0.84", "pillow"]
# ///
"""1:1 anchor sheet at delivery scale. Sources: a 9:16 window centred on the detected face, scaled to 1080x1920 with LANCZOS only
(HP-EXECUTION v1.3: no Iris/Proteus on real faces). Approved exports are already 1080x1920. Each tile is a 480x480 crop around the
face at delivery scale, never resized. Usage: uv run anchor_1to1.py <out.jpg> "label|file|t|src_or_final" ..."""
import subprocess, sys, pathlib, cv2
from PIL import Image, ImageDraw
casc = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
out = pathlib.Path(sys.argv[1]); tmp = out.parent / "_a11.png"; tiles = []
def frame(f, t, vf=None):
    subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-ss", t, "-i", f, "-frames:v", "1"] + (["-vf", vf] if vf else []) + [str(tmp)], check=True)
    return cv2.imread(str(tmp))
def bigface(img):
    fs = casc.detectMultiScale(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), 1.1, 5, minSize=(60, 60))
    return max(fs, key=lambda r: r[2] * r[3]) if len(fs) else None
for spec in sys.argv[2:]:
    lab, f, t, kind = spec.split("|")
    if kind == "src":
        full = frame(f, t); fc = bigface(full)
        if fc is None: print(lab, "no face on full frame"); continue
        H, W = full.shape[:2]; cw = int(H * 9 / 16); cx = fc[0] + fc[2] // 2
        x0 = min(max(cx - cw // 2, 0), W - cw)
        img = frame(f, t, f"crop={cw}:{H}:{x0}:0,scale=1080:1920:flags=lanczos")
    else:
        img = frame(f, t)
    fc = bigface(img)
    if fc is None: print(lab, "no face at delivery"); continue
    cx, cy = fc[0] + fc[2] // 2, fc[1] + fc[3] // 2
    x0 = min(max(cx - 240, 0), img.shape[1] - 480); y0 = min(max(cy - 240, 0), img.shape[0] - 480)
    crop = img[y0:y0 + 480, x0:x0 + 480]
    c = Image.new("RGB", (480, 500), "black"); c.paste(Image.fromarray(cv2.cvtColor(crop, cv2.COLOR_BGR2RGB)), (0, 20))
    txt = f"{lab}: face {fc[2]}px at delivery, 1:1"; ImageDraw.Draw(c).text((4, 3), txt, fill="yellow"); tiles.append(c); print(txt)
sheet = Image.new("RGB", (480 * 3, 500 * ((len(tiles) + 2) // 3)), "black")
for i, tl in enumerate(tiles): sheet.paste(tl, ((i % 3) * 480, (i // 3) * 500))
sheet.save(out, quality=90); print("wrote", out)
