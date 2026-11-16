"""Pre-compensate the cue PNGs for Premiere's LINEAR-LIGHT compositing, so the glow reads in Premiere the way it reads in
the browser/ffmpeg preview (and in the reference reel).

Why (Affan, 2026-11-16, ABW11 Seq 10: "too glowy, I want a subtle glow like how that guy had"): Premiere sequences
composite in linear colour by default, and a soft gold halo blended in linear light over his dark shirt comes out ~2-4x
stronger than the same alpha blended in sRGB (browser, ffmpeg, Instagram's player, where the glow was fitted). His
Premiere screenshot matched a linear-light simulation of the layer, not the sRGB preview. Check the sequence with
`seq.getSettings().compositeLinearColor` (his setting, never change it); with it off, skip this step. Fix: remap the alpha so a
linear blend over the measured background gives the sRGB look, per pixel (gold glow AND black drop shadow).
Colour stays straight; solid ink (alpha 1) is unchanged.

usage: python linfix.py <cue dir in> <cue dir out> <job dir>      measure the background from the job's cut
       python linfix.py <cue dir in> <cue dir out> --bg r,g,b     a fixed sRGB background, 0-255
then:  python assemble.py <job dir> <cue dir out> <out.mov> --alpha
"""
import glob, json, os, subprocess, sys
import numpy as np
from PIL import Image

src, dst, third = sys.argv[1:4]
os.makedirs(dst, exist_ok=True)
m = json.load(open(os.path.join(src, 'cues.json'), encoding='utf-8'))
P = m['params']; Y0, H = P['bandY'], P['bandH']
GAMMA = 2.4   # Premiere's linear mix fits a pure 2.4 power best (lanes/premiere/lab-notes.md § compositeLinearColor)
s2l = lambda x: np.power(np.clip(x, 0, 1), GAMMA)
W = np.array([0.2126, 0.7152, 0.0722])
fg = np.array([int(P['color'][i:i + 2], 16) for i in (1, 3, 5)]) / 255

if third == '--bg':
    bg = np.array([float(v) for v in sys.argv[4].split(',')]) / 255
else:
    name = os.path.basename(os.path.normpath(third)); cut = os.path.join(third, 'raw', f'{name}-cut.mp4')
    samples = []
    for c in m['cues'][::4]:
        raw = subprocess.run(['ffmpeg', '-v', 'error', '-ss', f"{c['t'] + 0.3:.3f}", '-i', cut, '-frames:v', '1',
                              '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], capture_output=True).stdout
        if len(raw) != 1080 * 1920 * 3: continue
        fr = np.frombuffer(raw, np.uint8).reshape(1920, 1080, 3)[Y0:Y0 + H]
        a = np.asarray(Image.open(os.path.join(src, os.path.basename(c['file']))))[..., 3]
        samples.append(fr[(a > 8) & (a < 150)])
    bg = np.median(np.concatenate(samples), axis=0) / 255
Yg = W @ s2l(bg)
def fix(im):
    """Per pixel (straight colour c, alpha a): the alpha whose LINEAR blend over bg has the luminance an sRGB blend shows.
    Exact for black (the drop shadow) on any background; for the gold glow it is exact on the measured background."""
    c = im[..., :3].astype(np.float64) / 255; a = im[..., 3:4].astype(np.float64) / 255
    YT = s2l(bg + a * (c - bg)) @ W; Yc = s2l(c) @ W; den = Yc - Yg
    a2 = np.where(np.abs(den) > 1e-5, (YT - Yg) / np.where(np.abs(den) > 1e-5, den, 1), a[..., 0])
    a2 = np.where(im[..., 3] == 255, 1.0, np.where(im[..., 3] == 0, 0.0, np.clip(a2, 0, 1)))
    out = im.copy(); out[..., 3] = np.round(a2 * 255).astype(np.uint8); return out
probe = np.zeros((2, 4, 4), np.uint8); probe[0, :, :3] = (np.array(fg) * 255).round(); probe[1, :, :3] = 0
probe[:, :, 3] = [51, 102, 153, 204]; pf = fix(probe)[..., 3]
print('background (sRGB 0-255):', np.round(bg * 255).astype(int).tolist(), '| gold alpha 51/102/153/204 ->', pf[0].tolist(),
      '| black ->', pf[1].tolist())
for c in m['cues']:
    im = np.asarray(Image.open(os.path.join(src, os.path.basename(c['file']))).convert('RGBA'))
    Image.fromarray(fix(im)).save(os.path.join(dst, os.path.basename(c['file'])))
m['params']['linfix'] = {'bg_srgb': np.round(bg * 255).astype(int).tolist(), 'from': os.path.abspath(src)}
json.dump(m, open(os.path.join(dst, 'cues.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('->', dst, len(m['cues']), 'cues')
