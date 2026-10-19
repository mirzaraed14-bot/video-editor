"""img-candidates.py: web photo candidates for overlays -> files + sources.txt + ONE numbered contact sheet (_sheet.jpg).

  python workflows/img-candidates.py OUT_DIR "tag|query|n" ["tag|query|n" ...] [--min 700]

Bing image search fetched with curl (python urllib gets region-skewed junk on this machine), full-size `murl` links downloaded with
curl, kept when the short side >= --min px. Pinterest /736x/ links are retried as /originals/. Look at the sheet once, pick, then
check the pick at full size; skip Getty / Alamy watermarks. Client Shorts recipe: presets/youtube-shorts/onyx-samples-youtube/CLIENT-SHORT-RECIPE.md
"""
import html, io, os, re, subprocess, sys, urllib.parse
from PIL import Image, ImageDraw

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"


def get(url, t=12):
    return subprocess.run(["curl", "-s", "-L", "--max-time", str(t), "-A", UA, url], capture_output=True).stdout


def main():
    a = sys.argv[1:]
    mn = 700
    if "--min" in a:
        i = a.index("--min"); mn = int(a[i + 1]); del a[i:i + 2]
    out, specs = a[0], a[1:]
    os.makedirs(out, exist_ok=True)
    tiles, seen = [], set()
    for sp in specs:
        tag, q, n = sp.split("|"); n = int(n)
        h = get("https://www.bing.com/images/search?q=" + urllib.parse.quote_plus(q) + "&first=1", 20).decode("utf-8", "ignore")
        k = 0
        for u in [html.unescape(u) for u in re.findall(r'murl&quot;:&quot;(.*?)&quot;', h)]:
            if k >= n:
                break
            if u in seen:
                continue
            seen.add(u)
            for cand in ([u.replace("/736x/", "/originals/"), u] if "pinimg.com/736x/" in u else [u]):
                try:
                    b = get(cand); im = Image.open(io.BytesIO(b)); im.load(); u = cand
                    break
                except Exception:
                    im = None
            if im is None or min(im.size) < mn:
                continue
            k += 1; name = f"{tag}{k}"; ext = (im.format or "jpg").lower().replace("jpeg", "jpg")
            open(os.path.join(out, f"{name}.{ext}"), "wb").write(b)
            open(os.path.join(out, "sources.txt"), "a", encoding="utf-8").write(f"{name}.{ext}\t{im.size[0]}x{im.size[1]}\t{u}\n")
            t = im.convert("RGB"); t.thumbnail((240, 300)); c = Image.new("RGB", (240, 322), (20, 20, 20))
            c.paste(t, ((240 - t.size[0]) // 2, 0)); ImageDraw.Draw(c).text((4, 306), f"{name} {im.size[0]}x{im.size[1]}", fill=(255, 255, 0))
            tiles.append(c)
    cols = 8; rows = max(1, (len(tiles) + cols - 1) // cols); sh = Image.new("RGB", (cols * 240, rows * 322))
    for i, t in enumerate(tiles):
        sh.paste(t, ((i % cols) * 240, (i // cols) * 322))
    sh.save(os.path.join(out, "_sheet.jpg"), quality=75); print(len(tiles), "candidates ->", os.path.join(out, "_sheet.jpg"))


if __name__ == "__main__":
    main()
