# /// script
# dependencies = ["opencv-python-headless==4.10.0.84", "pillow"]
# ///
"""Fair anchor compare for finalist A (adapted from projects/harry-potter-niche/qa_anchor_fair.py): the same face region
(detected face box x1.4) at the same tile size, RAW 9:16 crops of the downloaded Oldman HSC footage (no Topaz) vs the approved
Prince ABC panels and Bieber Oslo, plus Radcliffe HSC 2024 raw. Writes hp-films/proof/anchor_oldman.jpg.
Usage (repo root): python research/deep-research-2026-11-14/hp-films/tools/anchor_oldman.py <oldman2023.mp4> <t2023> <oldman2026.mp4> <t2026>
"""
import pathlib, subprocess, sys
import cv2
from PIL import Image, ImageDraw

HF = pathlib.Path("research/deep-research-2026-11-14/hp-films")
P = HF / "proof"; P.mkdir(parents=True, exist_ok=True)
EX = pathlib.Path("X:/Claude Projects/Exports")
RAD = pathlib.Path("E:/Bullshit Folder/Henry/Daniel Radcliffe, Jonathan Groff, _ Lindsay Mendez talk MERRILY WE ROLL ALONG I Happy Sad Confused.mp4")
casc = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
NINE16 = "crop=ih*9/16:ih:(iw-ih*9/16)/2:0,scale=1080:1920"

def grab(f, t, vf=None):
    o = P / "_fa.png"
    args = ["ffmpeg", "-nostdin", "-v", "error", "-y", "-ss", str(t), "-i", str(f), "-frames:v", "1"] + (["-vf", vf] if vf else []) + [str(o)]
    subprocess.run(args, check=True)
    return cv2.imread(str(o))

def face(img, label):
    g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    fs = casc.detectMultiScale(g, 1.1, 5, minSize=(40, 40))
    if len(fs) == 0:
        return img, label + " (no face found: full frame)"
    x, y, w, h = max(fs, key=lambda r: r[2] * r[3]); m = int(w * 0.2)
    x0, y0 = max(x - m, 0), max(y - m, 0); x1, y1 = min(x + w + m, img.shape[1]), min(y + h + m, img.shape[0])
    return img[y0:y1, x0:x1], f"{label}  face {w}px at delivery"

o23, t23, o26, t26 = sys.argv[1], float(sys.argv[2]), sys.argv[3], float(sys.argv[4])
items = [
    ("OLDMAN HSC 2023, raw 9:16", o23, t23, NINE16),
    ("OLDMAN HSC 2026, raw 9:16", o26, t26, NINE16),
    ("RADCLIFFE HSC 2024, raw 9:16", RAD, 1700.0, NINE16),
    ("APPROVED Prince ABC P7", EX / "Why Michael Jackson's Son Had To Step Outside.mov", 25.0, None),
    ("APPROVED Prince ABC P8", EX / "Why Michael Jackson's Son Had To Step Outside.mov", 32.5, None),
    ("APPROVED Bieber Oslo", EX / "Why Justin Bieber Walked Off His Own Stage.mov", 1.5, None),
]
tiles = []
for lab, f, t, vf in items:
    try:
        crop, text = face(grab(f, t, vf), lab)
    except Exception as e:
        print("skip", lab, e); continue
    im = Image.fromarray(cv2.cvtColor(crop, cv2.COLOR_BGR2RGB)).resize((480, 480))
    canvas = Image.new("RGB", (480, 500), "black"); canvas.paste(im, (0, 20))
    ImageDraw.Draw(canvas).text((4, 3), text, fill="yellow")
    tiles.append(canvas); print(text)
sheet = Image.new("RGB", (480 * 3, 500 * ((len(tiles) + 2) // 3)), "black")
for i, tl in enumerate(tiles):
    sheet.paste(tl, ((i % 3) * 480, (i // 3) * 500))
sheet.save(P / "anchor_oldman.jpg", quality=88)
print("wrote", P / "anchor_oldman.jpg")
