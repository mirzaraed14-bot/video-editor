#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["numpy"]
# ///
"""slowmo-scan.py <video> <out.json> — find the stretches where a finished video PLAYS SLOWER than real time.

A speed ramp / slow-mo on a 60p clip repeats frames (50 % speed = every frame shown twice): at the master's native
rate, the grey-thumbnail difference between consecutive frames drops to ~0 on every repeated frame, in a regular
pattern. This decodes the whole video at native fps (240x135 grey), marks "duplicate" frames (diff < 0.6/255), and
reports runs >= 0.4 s where the duplicate share is >= 35 % — a real slow-down, or a still. A still is then told apart
downstream by the style probe's segment kind (face vs overlay): a slowed FACE shot is the creator's comedy device.
Writes {fps, frames, runs: [{start, end, dup_share, est_speed}]} and prints the runs.
"""
import json, subprocess, sys
import numpy as np

video, out = sys.argv[1], sys.argv[2]
r = subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries', 'stream=r_frame_rate', '-of', 'csv=p=0', video], capture_output=True, text=True)
n, d = r.stdout.strip().splitlines()[0].split('/'); fps = float(n) / float(d)   # a .mov's timecode track adds a second line
W, H = 240, 135
p = subprocess.Popen(['ffmpeg', '-v', 'error', '-i', video, '-map', '0:v:0', '-vf', f'scale={W}:{H}', '-f', 'rawvideo', '-pix_fmt', 'gray', '-'], stdout=subprocess.PIPE, bufsize=10 ** 8)
prev, dups, i = None, [], 0
while True:
    buf = p.stdout.read(W * H)
    if len(buf) < W * H: break
    g = np.frombuffer(buf, np.uint8).astype(np.int16)
    dups.append(False if prev is None else bool(np.abs(g - prev).mean() < 0.6))
    prev = g; i += 1
p.wait()
dups = np.array(dups)
win = int(round(0.4 * fps)); runs = []; k = 0
share = np.convolve(dups.astype(float), np.ones(win) / win, 'same')
hot = share >= 0.35
while k < len(hot):
    if not hot[k]: k += 1; continue
    j = k
    while j < len(hot) and hot[j]: j += 1
    seg = dups[k:j]; ds = float(seg.mean())
    runs.append(dict(start=round(k / fps, 3), end=round(j / fps, 3), dur=round((j - k) / fps, 2), dup_share=round(ds, 2),
                     est_speed=round(1 - ds, 2)))   # 50 % dup ≈ half speed; 100 % ≈ a still
    k = j
runs = [x for x in runs if x['dur'] >= 0.4]
json.dump(dict(fps=fps, frames=int(len(dups)), runs=runs), open(out, 'w', encoding='utf-8'), indent=1)
print(f'{len(dups)} frames @ {fps:.2f} · {len(runs)} slowed/still runs')
for x in runs: print(f"  {x['start']:8.2f}-{x['end']:8.2f} {x['dur']:5.2f}s dup {x['dup_share']:.2f} ≈ {x['est_speed']:.2f}x")
