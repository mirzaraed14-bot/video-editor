"""thumbnail.py: a Scott Clary Short cover in the locked format (ENGINE.md): a real photo full-bleed 9:16, 2-4 words in Anton caps,
white with a black outline, exactly one word in teal #19D3C5, centred at ~66 % of the height.

  python presets/youtube-shorts/scott-clary/thumbnail.py PHOTO OUT.jpg "LINE ONE" "LINE TWO" --teal WORD [--cx 0.5] [--cy 0.5]
"""
import argparse, os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

FONT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "onyx-samples-youtube", "kit", "fonts", "Anton-Regular.ttf")
TEAL, W, H = (25, 211, 197), 1080, 1920

ap = argparse.ArgumentParser()
ap.add_argument("photo"); ap.add_argument("out"); ap.add_argument("lines", nargs="+")
ap.add_argument("--teal", required=True); ap.add_argument("--cx", type=float, default=0.5); ap.add_argument("--cy", type=float, default=0.5)
a = ap.parse_args()

im = Image.open(a.photo).convert("RGB")
k = max(W / im.width, H / im.height); im = im.resize((round(im.width * k), round(im.height * k)), Image.LANCZOS)
x0 = min(max(round(a.cx * im.width - W / 2), 0), im.width - W); y0 = min(max(round(a.cy * im.height - H / 2), 0), im.height - H)
im = im.crop((x0, y0, x0 + W, y0 + H))
shade = Image.new("L", (W, H), 0); ImageDraw.Draw(shade).rectangle((0, int(H * 0.52), W, H), fill=150)
im = Image.composite(Image.new("RGB", (W, H)), im, shade.filter(ImageFilter.GaussianBlur(160)))   # darken the lower half for the type
d = ImageDraw.Draw(im); size = 176
while size > 60:
    f = ImageFont.truetype(FONT, size)
    if max(d.textlength(l, font=f) for l in a.lines) <= 940:
        break
    size -= 8
lh = int(size * 1.08); y = int(H * 0.66) - lh * len(a.lines) // 2
for line in a.lines:
    x = (W - d.textlength(line, font=f)) / 2
    for w in line.split(" "):
        col = TEAL if w.strip(".!?,").upper() == a.teal.upper() else (255, 255, 255)
        d.text((x + 6, y + 8), w, font=f, fill=(0, 0, 0))
        d.text((x, y), w, font=f, fill=col, stroke_width=7, stroke_fill=(0, 0, 0))
        x += d.textlength(w + " ", font=f)
    y += lh
im.save(a.out, quality=92)
print(a.out, "font", size)
