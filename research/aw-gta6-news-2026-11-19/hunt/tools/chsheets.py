import sys, json, os
from PIL import Image, ImageDraw
sel = json.load(open(sys.argv[1], encoding="utf-8")); tag = sys.argv[2]
TW = 320; COLS = 6; PER = 30
by = {}
for r in sel["rows"]: by.setdefault(r["ch"], []).append(r)
os.makedirs("sheets", exist_ok=True)
for ch, rs in by.items():
    rs.sort(key=lambda r: (r["kind"] != "match", -(r["views"] or 0)))
    for pi in range(0, len(rs), PER):
        part = rs[pi:pi + PER]
        tiles = []
        for r in part:
            p = f"thumbs/{ch}-{r['id']}.jpg"
            try: im = Image.open(p).convert("RGB")
            except Exception: im = Image.new("RGB", (TW, 180), (40, 40, 40))
            im = im.resize((TW, int(im.height * TW / im.width)))
            d = ImageDraw.Draw(im)
            d.rectangle([0, 0, TW, 24], fill=(0, 0, 0))
            t = (r["title"] or "").encode("ascii", "replace").decode()
            d.text((2, 1), f"{'M' if r['kind']=='match' else 't'} {r['views']}v {r['dur']:.0f}s {r['id'][-6:]}", fill=(255, 255, 0))
            d.text((2, 12), t[:52], fill=(255, 255, 255))
            tiles.append(im)
        th = max(t.height for t in tiles); rows = (len(tiles) + COLS - 1) // COLS
        S = Image.new("RGB", (COLS * TW, rows * th), (0, 0, 0))
        for i, t in enumerate(tiles): S.paste(t, ((i % COLS) * TW, (i // COLS) * th))
        out = f"sheets/{tag}-{ch}-{pi//PER+1}.jpg"; S.save(out, quality=80); print(out, len(tiles))
