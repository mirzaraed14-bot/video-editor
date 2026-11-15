# shots.py (ig-mj, 15 Nov 2026): minors/picture check at the CUTS of a planned window.
# usage: python -I shots.py <video> <t0> <t1> <out.jpg> [label] [scene_threshold=0.25]
# Finds every shot boundary inside [t0, t1] (ffmpeg scene score), then grabs the FIRST and LAST frame of every shot
# and tiles them with their timestamps, so no shot inside the window goes unseen (lesson: one sampled frame is not a check).
import subprocess, sys, re, os, tempfile
from PIL import Image, ImageDraw

src, t0, t1, out = sys.argv[1], float(sys.argv[2]), float(sys.argv[3]), sys.argv[4]
label = sys.argv[5] if len(sys.argv) > 5 else os.path.basename(src)
thr = float(sys.argv[6]) if len(sys.argv) > 6 else 0.25

pre = max(0.0, t0 - 2.0)
cmd = ['ffmpeg', '-hide_banner', '-nostdin', '-ss', f'{pre:.3f}', '-i', src, '-t', f'{t1 - pre + 0.1:.3f}', '-an',
       '-vf', f"select='gt(scene,{thr})',showinfo", '-f', 'null', '-']
p = subprocess.run(cmd, capture_output=True, text=True, errors='replace')
cuts = []
for m in re.finditer(r'pts_time:([0-9.]+)', p.stderr):
    t = pre + float(m.group(1))
    if t0 + 0.04 < t < t1 - 0.04:
        cuts.append(round(t, 3))
bounds = [t0] + cuts + [t1]
grabs = []
for a, b in zip(bounds[:-1], bounds[1:]):
    grabs.append(a + 0.05)
    if b - a > 0.3:
        grabs.append(b - 0.09)
tmp = tempfile.mkdtemp(prefix='shots_')
tiles = []
for i, t in enumerate(grabs):
    f = os.path.join(tmp, f'{i:03d}.png')
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', f'{t:.3f}', '-i', src, '-frames:v', '1', '-vf', 'scale=360:-2', f],
                   capture_output=True)
    if os.path.exists(f):
        tiles.append((t, Image.open(f).convert('RGB')))
if not tiles:
    print('no frames'); sys.exit(1)
w, h = tiles[0][1].size
cols = min(6, len(tiles)); rows = (len(tiles) + cols - 1) // cols
sheet = Image.new('RGB', (cols * w, rows * (h + 18) + 22), (16, 16, 16))
d = ImageDraw.Draw(sheet)
d.text((6, 4), f'{label}  {t0:.2f}-{t1:.2f}  cuts: {", ".join(f"{c:.2f}" for c in cuts) or "none"}', fill=(255, 255, 0))
for i, (t, im) in enumerate(tiles):
    x, y = (i % cols) * w, 22 + (i // cols) * (h + 18)
    sheet.paste(im.resize((w, h)), (x, y))
    d.text((x + 4, y + h + 2), f'{t:.2f}', fill=(255, 255, 255))
sheet.save(out, quality=85)
print(f'{label}: cuts {cuts} -> {len(tiles)} frames -> {out}')
