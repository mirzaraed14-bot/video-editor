import sys, os
from PIL import Image, ImageDraw
# usage: sheet.py out.jpg cols tilew label1=path1 label2=path2 ...
out, cols, tw = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
items = [a.split("=", 1) for a in sys.argv[4:]]
tiles = []
for lab, p in items:
    try:
        im = Image.open(p).convert("RGB")
    except Exception:
        im = Image.new("RGB", (tw, tw * 9 // 16), (40, 40, 40))
    h = int(im.height * tw / im.width)
    im = im.resize((tw, h))
    d = ImageDraw.Draw(im)
    d.rectangle([0, 0, tw, 14], fill=(0, 0, 0))
    d.text((3, 1), lab[:60], fill=(255, 255, 0))
    tiles.append(im)
th = max(t.height for t in tiles)
rows = (len(tiles) + cols - 1) // cols
S = Image.new("RGB", (cols * tw, rows * th), (0, 0, 0))
for i, t in enumerate(tiles):
    S.paste(t, ((i % cols) * tw, (i // cols) * th))
S.save(out, quality=82)
print(out, S.size)
