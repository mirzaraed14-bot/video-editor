#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["opencv-python-headless", "numpy"]
# ///
"""style-zoom.py <video> <out.json> [--fps 5] — the TRUE zoom track of a talking-head edit, from the background.

A post zoom (a cut zoom, a gradual push) scales the whole frame, so the static set behind the person — the neon sign,
the monitor edge, the chair — scales with it, while a face box only tells you about the head. This matches ORB
features between consecutive samples with the centre (the person) masked out, fits a similarity transform, and keeps
its scale: ratio > 1 = the picture got bigger (a zoom in). Cumulated inside every run of matched samples it is the
zoom level over that run's start.

Writes {fps, samples: [{t, ratio, inliers}], runs: [{start, end, steps: [{t, ratio}], push_pct_per_s, level_max}],
summary: {steps_in, step_median, step_hold_median, push_pct_per_s, levels}}. A sample with < 15 inliers is a break
(a hard cut, an overlay, a frame with nothing static to match) and starts a new run.
"""
import json, subprocess, sys, statistics, math
import cv2, numpy as np

video, out = sys.argv[1], sys.argv[2]
fps = int(sys.argv[sys.argv.index('--fps') + 1]) if '--fps' in sys.argv else 5
W, H = 960, 540
orb = cv2.ORB_create(nfeatures=2000, scaleFactor=1.2, nlevels=8)
bf = cv2.BFMatcher(cv2.NORM_HAMMING)
mask = np.full((H, W), 255, np.uint8); mask[int(0.10 * H):, int(0.26 * W):int(0.74 * W)] = 0   # the person's column

p = subprocess.Popen(['ffmpeg', '-v', 'error', '-i', video, '-map', '0:v:0', '-vf', f'fps={fps},scale={W}:{H}', '-f', 'rawvideo', '-pix_fmt', 'gray', '-'],
                     stdout=subprocess.PIPE, bufsize=10 ** 8)
prev, samples, i = None, [], 0
while True:
    buf = p.stdout.read(W * H)
    if len(buf) < W * H: break
    g = np.frombuffer(buf, np.uint8).reshape(H, W)
    kp, des = orb.detectAndCompute(g, mask)
    ratio, inl = None, 0
    if prev is not None and des is not None and prev[1] is not None and len(kp) >= 20 and len(prev[0]) >= 20:
        m = bf.knnMatch(prev[1], des, k=2)
        good = [a for a, b in (x for x in m if len(x) == 2) if a.distance < 0.75 * b.distance]
        if len(good) >= 15:
            src = np.float32([prev[0][a.queryIdx].pt for a in good]); dst = np.float32([kp[a.trainIdx].pt for a in good])
            M, ok = cv2.estimateAffinePartial2D(src, dst, method=cv2.RANSAC, ransacReprojThreshold=3.0)
            if M is not None and ok is not None:
                inl = int(ok.sum())
                if inl >= 15: ratio = float(math.hypot(M[0, 0], M[0, 1]))
    samples.append(dict(t=round(i / fps, 3), ratio=round(ratio, 4) if ratio else None, inliers=inl))
    prev = (kp, des); i += 1
p.wait()

# runs of matched samples; steps and pushes inside them
runs, cur = [], None
for s in samples:
    if s['ratio'] is None or s['ratio'] < 0.5 or s['ratio'] > 2.0:
        if cur: runs.append(cur); cur = None
        continue
    if cur is None: cur = dict(start=s['t'], end=s['t'], log=[0.0], ts=[s['t']], steps=[])
    cur['log'].append(cur['log'][-1] + math.log(s['ratio'])); cur['ts'].append(s['t']); cur['end'] = s['t']
    if s['ratio'] >= 1.08 or s['ratio'] <= 1 / 1.08: cur['steps'].append(dict(t=s['t'], ratio=round(s['ratio'], 3)))
if cur: runs.append(cur)
for r in runs:
    ts, lg = np.array(r['ts']), np.array(r['log'])
    keep = np.ones(len(ts), bool)
    for st in r['steps']:
        k = int(np.argmin(np.abs(ts - st['t']))); keep[k] = False
    # the push: slope of log-scale between steps, per second, on stretches >= 1.5 s
    segs, a = [], 0
    for k in range(1, len(ts)):
        if not keep[k] or k == len(ts) - 1:
            if ts[k - 1] - ts[a] >= 1.5:
                sl, _ = np.polyfit(ts[a:k], lg[a:k], 1); segs.append(100 * (math.exp(sl) - 1))
            a = k
    r['push_pct_per_s'] = round(statistics.median(segs), 2) if segs else None
    r['level_max'] = round(float(math.exp(lg.max())), 3); r['dur'] = round(r['end'] - r['start'], 2)
    del r['log']; del r['ts']
steps_in = [st for r in runs for st in r['steps'] if st['ratio'] > 1]
holds = []
for r in runs:
    for st in r['steps']:
        if st['ratio'] <= 1: continue
        nxt = [x['t'] for x in r['steps'] if x['t'] > st['t'] and x['ratio'] < 1]
        holds.append(min([r['end']] + nxt[:1]) - st['t'])
pushes = [r['push_pct_per_s'] for r in runs if r['push_pct_per_s'] is not None and r['dur'] >= 3]
summary = dict(steps_in=len(steps_in), steps_out=sum(1 for r in runs for st in r['steps'] if st['ratio'] < 1),
               step_median=round(statistics.median([s['ratio'] for s in steps_in]), 3) if steps_in else None,
               step_hold_median=round(statistics.median(holds), 2) if holds else None,
               push_pct_per_s=round(statistics.median(pushes), 2) if pushes else None,
               level_max_median=round(statistics.median([r['level_max'] for r in runs if r['dur'] >= 3]), 3) if runs else None,
               matched_share=round(sum(1 for s in samples if s['ratio']) / max(1, len(samples)), 3))
json.dump(dict(fps=fps, samples=samples, runs=runs, summary=summary), open(out, 'w', encoding='utf-8'), indent=1)
print(json.dumps(summary))
