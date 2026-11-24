"""Anchor test (PITCH-CHECKLIST § 2): streamer face cams at DELIVERY scale vs the approved Prince ABC panels (P7 25.0 s, P8 32.5 s)
and Bieber Oslo. Same face region (detected face box + 20 %), same 480 px tile. Two delivery cases for the cams:
  inset  = the 16:9 stream frame scaled to 1080 wide (cam stays inside it)
  split  = the cam region alone enlarged to 1080 wide (README § 13 stacked split), used only on summit1g beat 3.
Writes frames/anchor_compare.jpg and prints the face width at delivery for each tile."""
import subprocess, pathlib, cv2, sys
from PIL import Image, ImageDraw
sys.stdout.reconfigure(encoding="utf-8")
J = pathlib.Path(__file__).resolve().parent.parent; F = J / "frames"; EX = pathlib.Path("X:/Claude Projects/Exports")
casc = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
def grab(f, t, vf=None):
    o = F / "_anc.png"
    subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-ss", str(t), "-i", str(f), "-frames:v", "1"] + (["-vf", vf] if vf else []) + [str(o)], check=True)
    return cv2.imread(str(o))
def face(img, label, roi=None):
    sub = img if roi is None else img[roi[1]:roi[3], roi[0]:roi[2]]
    g = cv2.cvtColor(sub, cv2.COLOR_BGR2GRAY); fs = casc.detectMultiScale(g, 1.1, 4, minSize=(16, 16))
    if len(fs) == 0: return None, label + " (no face found)"
    x, y, w, h = max(fs, key=lambda r: r[2] * r[3]); m = int(w * 0.2)
    if roi is not None: x += roi[0]; y += roi[1]
    x0, y0 = max(x - m, 0), max(y - m, 0); x1, y1 = min(x + w + m, img.shape[1]), min(y + h + m, img.shape[0])
    lap = cv2.Laplacian(cv2.cvtColor(img[y:y + h, x:x + w], cv2.COLOR_BGR2GRAY), cv2.CV_64F).var()
    return img[y0:y1, x0:x1], f"{label} | face {w}px | lapvar {lap:.0f}"
M = J / "media/ondisk"
# (label, file, t, vf, roi in the delivered frame where the cam is: x0,y0,x1,y1)
items = [
 ("FANUM inset (1920->1080)", M / "fanum-bigfoot.mp4", 5.0, "scale=1080:-2", (0, 200, 300, 400)),
 ("SUMMIT1G inset (2560->1080)", M / "summit-bigfootjumpscare.mp4", 34.0, "scale=1080:-2", (0, 260, 260, 420)),
 ("SUMMIT1G split: cam region x0-700 y720-1100 of 2560 -> 1080 wide", M / "summit-bigfootjumpscare.mp4", 34.0, "crop=700:380:0:720,scale=1080:-2", None),
 ("XQC inset (1920->1080)", M / "xqc-kirk-0940-1060.mp4", 96.5, "scale=1080:-2", (0, 260, 220, 420)),
 ("APPROVED Prince ABC P7", EX / "Why Michael Jackson's Son Had To Step Outside.mov", 25.0, None, None),
 ("APPROVED Prince ABC P8", EX / "Why Michael Jackson's Son Had To Step Outside.mov", 32.5, None, None),
]
tiles = []
for lab, f, t, vf, roi in items:
    img = grab(f, t, vf); c, l = face(img, lab, roi)
    if c is None: c = img if roi is None else img[roi[1]:roi[3], roi[0]:roi[2]]
    print(l, "| delivered frame", img.shape[1], "x", img.shape[0])
    im = Image.fromarray(cv2.cvtColor(c, cv2.COLOR_BGR2RGB)).resize((480, 480), Image.LANCZOS)
    d = ImageDraw.Draw(im); d.rectangle((0, 0, 480, 22), fill="black"); d.text((5, 5), l[:78], fill="yellow"); tiles.append(im)
sheet = Image.new("RGB", (1440, 960)); [sheet.paste(im, ((k % 3) * 480, (k // 3) * 480)) for k, im in enumerate(tiles)]
sheet.save(F / "anchor_compare.jpg", quality=92); (F / "_anc.png").unlink(missing_ok=True); print("ok")
