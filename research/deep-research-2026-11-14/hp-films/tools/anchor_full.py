# /// script
# dependencies = ["opencv-python-headless==4.10.0.84", "pillow"]
# ///
"""Face size at 9:16 delivery from a FULL 1920x1080 frame (the build head-locks its crop, so detect on the full frame).
A 9:16 crop of a 1080-high frame is scaled x1.778 to 1080x1920, so face px at delivery = face width in source x 1.778.
Usage: uv run anchor_full.py <out.jpg> <label|file|t> ...   (several frames per file allowed)"""
import subprocess, sys, pathlib, cv2
from PIL import Image, ImageDraw
casc = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
out = pathlib.Path(sys.argv[1]); tiles = []
for spec in sys.argv[2:]:
    lab, f, t = spec.split("|")
    tmp = out.parent / "_af.png"
    subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-ss", t, "-i", f, "-frames:v", "1", str(tmp)], check=True)
    img = cv2.imread(str(tmp)); g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    fs = casc.detectMultiScale(g, 1.1, 5, minSize=(60, 60))
    if len(fs) == 0:
        print(lab, "no face"); continue
    x, y, w, h = max(fs, key=lambda r: r[2] * r[3]); m = int(w * 0.2)
    crop = img[max(y - m, 0):y + h + m, max(x - m, 0):x + w + m]
    k = 1920 / img.shape[0]; dw = int(round(w * k))
    im = Image.fromarray(cv2.cvtColor(crop, cv2.COLOR_BGR2RGB)).resize((480, 480))
    c = Image.new("RGB", (480, 500), "black"); c.paste(im, (0, 20))
    txt = f"{lab}: face {w}px in source = {dw}px at 9:16 delivery"
    ImageDraw.Draw(c).text((4, 3), txt, fill="yellow"); tiles.append(c); print(txt)
sheet = Image.new("RGB", (480 * min(3, len(tiles)), 500 * ((len(tiles) + 2) // 3)), "black")
for i, tl in enumerate(tiles):
    sheet.paste(tl, ((i % 3) * 480, (i // 3) * 500))
sheet.save(out, quality=88); print("wrote", out)
