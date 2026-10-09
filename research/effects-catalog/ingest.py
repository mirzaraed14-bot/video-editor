"""Import frames captured in Chrome (fxcat-<code>-<kind>.json in ~/Downloads) into the catalog.

  python ingest.py <code> scan    -> work/<code>/frames/<t>.jpg + work/<code>/sheet-NN.jpg (6x5, labelled m:ss)
  python ingest.py <code> stills  -> shots/<code>-<name>.jpg (full size) and shots/<code>-<name>-strip.jpg
The JSON is moved into work/<code>/ afterwards so ~/Downloads stays clean.
"""
import base64, io, json, os, shutil, sys
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.abspath(__file__))
DL = os.path.join(os.path.expanduser('~'), 'Downloads')
FONT = 'C:/Windows/Fonts/arialbd.ttf'


def mmss(t):
    return f'{int(t // 60)}:{t % 60:05.2f}'


def label(im, text, size=20):
    d = ImageDraw.Draw(im); f = ImageFont.truetype(FONT, size)
    w = d.textlength(text, font=f); d.rectangle([0, 0, w + 12, size + 10], fill=(0, 0, 0))
    d.text((6, 4), text, font=f, fill=(255, 220, 0)); return im


def img(data_url):
    return Image.open(io.BytesIO(base64.b64decode(data_url.split(',', 1)[1]))).convert('RGB')


def main(code, kind):
    src = os.path.join(DL, f'fxcat-{code}-{kind}.json')
    work = os.path.join(ROOT, 'work', code); os.makedirs(work, exist_ok=True)
    if not os.path.exists(src):
        src = os.path.join(work, f'fxcat-{code}-{kind}.json')
    d = json.load(open(src, encoding='utf-8'))
    if kind == 'scan':
        fr = os.path.join(work, 'frames'); os.makedirs(fr, exist_ok=True)
        ims = []
        for f in d['frames']:
            im = img(f['d']); im.save(os.path.join(fr, f"{f['t']:07.2f}.jpg"), quality=88)
            ims.append((f['t'], im))
        per, cols = 30, 6
        for s in range(0, len(ims), per):
            chunk = ims[s:s + per]; w, h = 384, round(384 * chunk[0][1].height / chunk[0][1].width)
            sheet = Image.new('RGB', (cols * w, 5 * h), (20, 20, 20))
            for i, (t, im) in enumerate(chunk):
                sheet.paste(label(im.resize((w, h)), mmss(t)), ((i % cols) * w, (i // cols) * h))
            p = os.path.join(work, f'sheet-{s // per + 1:02d}.jpg'); sheet.save(p, quality=85); print(p)
        print(f'{len(ims)} frames, {ims[0][0]}..{ims[-1][0]} s')
    else:
        shots = os.path.join(ROOT, 'shots'); os.makedirs(shots, exist_ok=True)
        for s in d['shots']:
            frames = [(f['t'], img(f['d'])) for f in s['frames']]
            if len(frames) == 1:
                p = os.path.join(shots, f"{code}-{s['name']}.jpg"); frames[0][1].save(p, quality=90)
            else:
                small = [label(im.resize((640, round(640 * im.height / im.width))), mmss(t)) for t, im in frames]
                w, h = small[0].size
                out = Image.new('RGB', (w * len(small) + 8 * (len(small) - 1), h), (255, 255, 255))
                for i, im in enumerate(small):
                    out.paste(im, (i * (w + 8), 0))
                p = os.path.join(shots, f"{code}-{s['name']}-strip.jpg"); out.save(p, quality=88)
                mid = frames[len(frames) // 2][1]
                mid.save(os.path.join(shots, f"{code}-{s['name']}.jpg"), quality=90)
            print(p)
    if os.path.dirname(src) != work:
        shutil.move(src, os.path.join(work, os.path.basename(src)))


main(sys.argv[1], sys.argv[2])
