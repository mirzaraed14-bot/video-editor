#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["numpy"]
# ///
"""style-set.py <video> <out.json> [--fps 5] — is the CREATOR'S SET on screen? Read off the frame's colour.

A face detector cannot tell the creator from a game close-up (Lucia in the GTA 6 trailer passed a size-and-centre
rule, 2026-09-21), and the frame CORNERS cannot tell a tight zoom from an overlay (a x1.5 zoom pushes the wall out of
the corners). The LED-washed wall's HUE can: it is one hue for the whole video and it stays behind the head at every
zoom. Per sample (style-probe.py's clock) this stores a 36-bin hue histogram of the saturated, non-dark pixels
(share of the WHOLE frame per bin) plus the mean saturation; style-report.py learns the set hue from the samples
that also carry a big centred face and scores every sample by how much of the frame sits within ±20° of it.
"""
import json, subprocess, sys
import numpy as np

video, out = sys.argv[1], sys.argv[2]
fps = int(sys.argv[sys.argv.index('--fps') + 1]) if '--fps' in sys.argv else 5
W, H = 240, 135
p = subprocess.Popen(['ffmpeg', '-v', 'error', '-i', video, '-map', '0:v:0', '-vf', f'fps={fps},scale={W}:{H}', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-'], stdout=subprocess.PIPE, bufsize=10 ** 8)
rows, i = [], 0
while True:
    buf = p.stdout.read(W * H * 3)
    if len(buf) < W * H * 3: break
    f = np.frombuffer(buf, np.uint8).reshape(-1, 3).astype(np.float32)
    b, g, r = f[:, 0], f[:, 1], f[:, 2]
    mx, mn = f.max(1), f.min(1); d = mx - mn + 1e-6
    sat = d / (mx + 1e-6)
    hue = np.where(mx == r, (g - b) / d % 6, np.where(mx == g, (b - r) / d + 2, (r - g) / d + 4)) * 60.0
    keep = (sat > 0.25) & (mx > 40)
    hist = np.bincount((hue[keep] // 10).astype(int) % 36, minlength=36) / len(f)
    rows.append(dict(t=round(i / fps, 3), hist=[round(float(x), 4) for x in hist], sat=round(float(sat.mean()), 3)))
    i += 1
p.wait()
json.dump(dict(fps=fps, samples=rows), open(out, 'w', encoding='utf-8'))
print(len(rows), 'samples')
