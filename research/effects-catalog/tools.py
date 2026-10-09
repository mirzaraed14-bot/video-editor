"""Effects-catalog helpers. Reference only: frames from other channels' videos, never used in an edit.

  python tools.py sheets <code> [--every 2] [--from 0] [--to 600]
      -> work/<code>/sheet-NN.jpg, 6x5 frames per sheet, each labelled with its m:ss time
  python tools.py still <code> <t>
      -> shots/<code>-<t>.jpg, one full-size frame
  python tools.py strip <code> <t0> <t1> [--n 4] [--name slug]
      -> shots/<code>-<slug>-strip.jpg, n frames evenly spaced t0..t1 side by side (shows a move), times labelled
"""
import argparse, os, subprocess, sys, tempfile, glob
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.abspath(__file__))
FONT = 'C:/Windows/Fonts/arialbd.ttf'


def src(code):
    p = os.path.join(ROOT, 'src', code + '.mp4')
    if not os.path.exists(p):
        sys.exit(f'missing {p}')
    return p


def mmss(t):
    return f'{int(t // 60)}:{t % 60:05.2f}' if t % 1 else f'{int(t // 60)}:{int(t % 60):02d}'


def frame(code, t, width=None):
    fd, out = tempfile.mkstemp(suffix='.png'); os.close(fd)
    vf = ['-vf', f'scale={width}:-2'] if width else []
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', str(t), '-i', src(code), '-frames:v', '1', *vf, out], check=True)
    im = Image.open(out).convert('RGB'); os.remove(out)
    return im


def label(im, text, size=22):
    d = ImageDraw.Draw(im)
    f = ImageFont.truetype(FONT, size)
    w = d.textlength(text, font=f)
    d.rectangle([0, 0, w + 12, size + 10], fill=(0, 0, 0))
    d.text((6, 4), text, font=f, fill=(255, 220, 0))
    return im


def sheets(a):
    out = os.path.join(ROOT, 'work', a.code); os.makedirs(out, exist_ok=True)
    tmp = tempfile.mkdtemp()
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', str(a.frm), '-to', str(a.to), '-i', src(a.code),
                    '-vf', f'fps=1/{a.every},scale=384:-2', os.path.join(tmp, 'f%05d.jpg')], check=True)
    files = sorted(glob.glob(os.path.join(tmp, 'f*.jpg')))
    per = 30
    for s in range(0, len(files), per):
        chunk = files[s:s + per]
        w, h = Image.open(chunk[0]).size
        sheet = Image.new('RGB', (6 * w, 5 * h), (20, 20, 20))
        for i, f in enumerate(chunk):
            t = a.frm + (s + i) * a.every
            sheet.paste(label(Image.open(f).convert('RGB'), mmss(t)), ((i % 6) * w, (i // 6) * h))
        p = os.path.join(out, f'sheet-{s // per + 1:02d}.jpg'); sheet.save(p, quality=85); print(p)
    for f in files: os.remove(f)
    os.rmdir(tmp)


def still(a):
    os.makedirs(os.path.join(ROOT, 'shots'), exist_ok=True)
    p = os.path.join(ROOT, 'shots', f'{a.code}-{a.name or str(a.t).replace(".", "_")}.jpg')
    frame(a.code, a.t).save(p, quality=90); print(p)


def strip(a):
    os.makedirs(os.path.join(ROOT, 'shots'), exist_ok=True)
    ts = [a.t0 + (a.t1 - a.t0) * i / max(1, a.n - 1) for i in range(a.n)]
    ims = [label(frame(a.code, t, 640), mmss(round(t, 2)), 20) for t in ts]
    w, h = ims[0].size
    out = Image.new('RGB', (w * len(ims) + 8 * (len(ims) - 1), h), (255, 255, 255))
    for i, im in enumerate(ims):
        out.paste(im, (i * (w + 8), 0))
    p = os.path.join(ROOT, 'shots', f'{a.code}-{a.name or "strip"}-strip.jpg'); out.save(p, quality=88); print(p)


ap = argparse.ArgumentParser(); sp = ap.add_subparsers(dest='cmd', required=True)
s = sp.add_parser('sheets'); s.add_argument('code'); s.add_argument('--every', type=float, default=2)
s.add_argument('--from', dest='frm', type=float, default=0); s.add_argument('--to', type=float, default=600)
s.set_defaults(fn=sheets)
s = sp.add_parser('still'); s.add_argument('code'); s.add_argument('t', type=float); s.add_argument('--name')
s.set_defaults(fn=still)
s = sp.add_parser('strip'); s.add_argument('code'); s.add_argument('t0', type=float); s.add_argument('t1', type=float)
s.add_argument('--n', type=int, default=4); s.add_argument('--name'); s.set_defaults(fn=strip)
a = ap.parse_args(); a.fn(a)
