#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["opencv-python-headless", "numpy"]
# ///
"""style-probe.py — measure how a finished talking-head video is EDITED, so a style can be copied from numbers.

  uv run workflows/style-probe.py <video> <out_dir> [--fps 5] [--face-fps 5] [--min-cut 0.25]

Reads the video ONCE through ffmpeg at a low sample rate and writes to <out_dir>:
  probe.json     every sample (t, luma, motion, face box), every cut, every segment (face | overlay), every face run
                 with its gradual push (scale at start/end, %/s) and every CUT ZOOM (an instant face-size step)
  summary.md     the numbers a style doc quotes: cuts/min (whole, cold open, by minute), held-shot median, face share,
                 overlay share and run lengths, push rate, cut-zoom count/size/hold, luma
  cuts/          one 480-wide jpg per cut (the first frame after it) named by timecode, for the visual read
  segments/      one mid-frame jpg per segment
  sheet.png      contact sheet of every cut, 8 per row, timecode burned in

What "face size" means: the YuNet face box height as a fraction of frame height, on the largest face. A gradual zoom
reads as a slow monotonic growth inside one held shot; a cut zoom reads as a step of >= 10 % between two samples
with the SAME scene (no cut), on a face that did not move. Lean-ins are slower than a step and rarely exceed 8 %.

A cut is a frame whose mean absolute difference from the previous sample (on a 240x135 grey thumbnail) exceeds
max(12/255, 6x the running median): robust against the creator's hand gestures, which move part of the frame,
and against slow pushes, which move nothing between two samples 0.2 s apart.
"""
import json, os, subprocess, sys, statistics, math
from collections import Counter

import cv2, numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL = os.path.join(ROOT, 'assets', 'models', 'face_detection_yunet_2023mar.onnx')
W, H = 960, 540


def probe(video):
    r = subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries',
                        'stream=width,height,r_frame_rate:format=duration', '-of', 'json', video], capture_output=True, text=True)
    j = json.loads(r.stdout); s = j['streams'][0]; n, d = s['r_frame_rate'].split('/')
    return int(s['width']), int(s['height']), float(n) / float(d), float(j['format']['duration'])


def frames(video, fps):
    p = subprocess.Popen(['ffmpeg', '-v', 'error', '-i', video, '-map', '0:v:0', '-vf', f'fps={fps},scale={W}:{H}', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-'],
                         stdout=subprocess.PIPE, bufsize=10 ** 8)
    n = W * H * 3
    i = 0
    while True:
        buf = p.stdout.read(n)
        if len(buf) < n: break
        yield i, np.frombuffer(buf, np.uint8).reshape(H, W, 3)
        i += 1
    p.wait()


def tc(t):
    m, s = divmod(t, 60)
    return f'{int(m)}:{s:05.2f}'


def main():
    a = sys.argv[1:]
    if len(a) < 2: sys.exit(__doc__)
    video, out = a[0], a[1]
    opt = lambda k, d: type(d)(a[a.index(k) + 1]) if k in a else d
    fps, min_cut = opt('--fps', 5), opt('--min-cut', 0.25)
    os.makedirs(os.path.join(out, 'cuts'), exist_ok=True); os.makedirs(os.path.join(out, 'segments'), exist_ok=True)
    vw, vh, vfps, dur = probe(video)
    det = cv2.FaceDetectorYN_create(MODEL, '', (W, H), score_threshold=0.6)
    samples, prev_g, diffs = [], None, []
    keep = {}   # sample index -> frame (only what the sheets need)
    for i, img in frames(video, fps):
        t = i / fps
        g = cv2.cvtColor(cv2.resize(img, (240, 135), interpolation=cv2.INTER_AREA), cv2.COLOR_BGR2GRAY).astype(np.int16)
        motion = float(np.abs(g - prev_g).mean()) if prev_g is not None else 0.0
        prev_g = g
        _, dets = det.detect(img)
        face = None
        if dets is not None and len(dets):
            x, y, bw, bh, sc = max(((d[0], d[1], d[2], d[3], d[14]) for d in dets), key=lambda d: d[2] * d[3])
            face = dict(x=round(float(x) / W, 4), y=round(float(y) / H, 4), w=round(float(bw) / W, 4), h=round(float(bh) / H, 4), score=round(float(sc), 2))
        samples.append(dict(i=i, t=round(t, 3), luma=round(float(g.mean()) / 255, 4), motion=round(motion, 2), face=face))
        diffs.append(motion)
        if i % 5 == 0 or motion > 12: keep[i] = cv2.resize(img, (480, 270), interpolation=cv2.INTER_AREA)
    # ---- cuts: a jump in frame difference well above the local running median
    med = statistics.median([d for d in diffs[1:]]) if len(diffs) > 1 else 0
    thr = max(12.0, 6 * med)
    cuts = []
    for s in samples[1:]:
        if s['motion'] > thr and (not cuts or s['t'] - cuts[-1] >= min_cut):
            cuts.append(s['t'])
    # ---- segments between cuts, classified by face presence
    bounds = [0.0] + cuts + [round(dur, 3)]
    segs = []
    for a0, b0 in zip(bounds, bounds[1:]):
        ss = [s for s in samples if a0 <= s['t'] < b0]
        if not ss: continue
        with_face = sum(1 for s in ss if s['face'])
        kind = 'face' if with_face >= 0.6 * len(ss) else 'overlay'
        mot = statistics.median([s['motion'] for s in ss[1:]]) if len(ss) > 1 else 0.0
        segs.append(dict(start=a0, end=b0, dur=round(b0 - a0, 3), kind=kind, face_share=round(with_face / len(ss), 2),
                         motion=round(mot, 2), luma=round(statistics.mean(s['luma'] for s in ss), 3)))
    # merge adjacent face segments that are the same held shot split by a false cut? no: a cut is a cut (a jump cut IS a cut).
    # ---- face runs: consecutive face segments; the push and the cut zooms inside each held shot
    runs, cur = [], None
    for sg in segs:
        if sg['kind'] == 'face':
            if cur and abs(cur['end'] - sg['start']) < 1e-6: cur['end'] = sg['end']; cur['shots'] += 1
            else:
                if cur: runs.append(cur)
                cur = dict(start=sg['start'], end=sg['end'], shots=1)
        else:
            if cur: runs.append(cur); cur = None
    if cur: runs.append(cur)
    shots, zooms = [], []
    for sg in segs:
        if sg['kind'] != 'face': continue
        ss = [s for s in samples if sg['start'] <= s['t'] < sg['end'] and s['face']]
        if len(ss) < 3: continue
        hs = [s['face']['h'] for s in ss]
        # cut zooms: a step >= 10 % of face height between two consecutive samples inside the shot
        for p, q in zip(ss, ss[1:]):
            r = q['face']['h'] / p['face']['h'] if p['face']['h'] else 1
            if r >= 1.10 or r <= 1 / 1.10:
                zooms.append(dict(t=q['t'], ratio=round(r, 3), shot_start=sg['start'], shot_end=sg['end']))
        # the push: linear fit of face height over the shot, excluding the step samples
        step_ts = {z['t'] for z in zooms if sg['start'] <= z['t'] < sg['end']}
        base = [s for s in ss if s['t'] not in step_ts]
        if len(base) >= 3:
            xs = np.array([s['t'] for s in base]); ys = np.array([s['face']['h'] for s in base])
            k, b = np.polyfit(xs, ys, 1)
            h0 = k * xs[0] + b; h1 = k * xs[-1] + b
            shots.append(dict(start=sg['start'], end=sg['end'], dur=sg['dur'], face_h0=round(float(h0), 4), face_h1=round(float(h1), 4),
                              push_pct=round(100 * (h1 / h0 - 1), 1) if h0 > 0 else None,
                              push_pct_per_s=round(100 * (h1 / h0 - 1) / max(sg['dur'], 0.2), 2) if h0 > 0 else None,
                              cut_zooms=sorted(step_ts)))
    # ---- hold after a cut zoom: until the next cut or the reverse step
    for z in zooms:
        nxt = [c for c in cuts if c > z['t']]
        rev = [w['t'] for w in zooms if w['t'] > z['t'] and w['shot_start'] == z['shot_start'] and (w['ratio'] < 1) != (z['ratio'] < 1)]
        end = min([z['shot_end']] + nxt[:1] + rev[:1])
        z['hold'] = round(end - z['t'], 2)
    # ---- numbers
    n_cuts = len(cuts)
    per_min = lambda lo, hi: 60 * sum(1 for c in cuts if lo <= c < hi) / max(1e-9, min(hi, dur) - lo)
    held = [sg['dur'] for sg in segs]
    face_t = sum(sg['dur'] for sg in segs if sg['kind'] == 'face'); ov = [sg for sg in segs if sg['kind'] == 'overlay']
    still = [sg for sg in ov if sg['motion'] < 1.0]; moving = [sg for sg in ov if sg['motion'] >= 1.0]
    lum = [s['luma'] for s in samples]
    summary = dict(video=os.path.basename(video), size=[vw, vh], fps=round(vfps, 3), duration=round(dur, 2),
                   cuts=n_cuts, cuts_per_min=round(60 * n_cuts / dur, 1), cold_open_cuts_per_min=round(per_min(0, 60), 1),
                   cuts_per_min_by_minute=[round(per_min(60 * m, 60 * (m + 1)), 1) for m in range(int(math.ceil(dur / 60)))],
                   held_median_s=round(statistics.median(held), 2) if held else None, held_max_s=round(max(held), 2) if held else None,
                   face_share=round(face_t / dur, 3), face_runs=len(runs), face_run_median_s=round(statistics.median([r['end'] - r['start'] for r in runs]), 2) if runs else None,
                   face_shot_median_s=round(statistics.median([sg['dur'] for sg in segs if sg['kind'] == 'face']), 2) if face_t else None,
                   overlay_share=round(1 - face_t / dur, 3), overlays=len(ov), overlay_median_s=round(statistics.median([o['dur'] for o in ov]), 2) if ov else None,
                   overlays_moving=len(moving), overlays_still=len(still), overlays_per_min=round(60 * len(ov) / dur, 1),
                   push_median_pct=round(statistics.median([s['push_pct'] for s in shots if s['push_pct'] is not None and s['dur'] >= 1.5]), 1) if shots else None,
                   push_median_pct_per_s=round(statistics.median([s['push_pct_per_s'] for s in shots if s['push_pct_per_s'] is not None and s['dur'] >= 1.5]), 2) if shots else None,
                   cut_zooms_in=len([z for z in zooms if z['ratio'] > 1]), cut_zooms_out=len([z for z in zooms if z['ratio'] < 1]),
                   cut_zoom_median_ratio=round(statistics.median([z['ratio'] for z in zooms if z['ratio'] > 1]), 3) if any(z['ratio'] > 1 for z in zooms) else None,
                   cut_zoom_median_hold_s=round(statistics.median([z['hold'] for z in zooms if z['ratio'] > 1]), 2) if any(z['ratio'] > 1 for z in zooms) else None,
                   luma_mean=round(statistics.mean(lum), 3), luma_dark_share=round(sum(1 for l in lum if l < 0.18) / len(lum), 3),
                   luma_bright_share=round(sum(1 for l in lum if l > 0.40) / len(lum), 3),
                   first_shot=segs[0]['kind'] if segs else None, last_shot=segs[-1]['kind'] if segs else None)
    json.dump(dict(summary=summary, cuts=cuts, segments=segs, face_runs=runs, face_shots=shots, cut_zooms=zooms, samples=samples),
              open(os.path.join(out, 'probe.json'), 'w', encoding='utf-8'), indent=1)
    # ---- pictures: every cut, every segment mid, one contact sheet
    def nearest(t):
        i = int(round(t * fps));
        for j in (i, i + 1, i - 1, i + 2, i - 2, i + 3):
            if j in keep: return keep[j]
        return None
    tiles = []
    for c in cuts:
        img = nearest(c + 1 / fps)
        if img is None: continue
        im = img.copy(); cv2.putText(im, tc(c), (8, 262), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 4); cv2.putText(im, tc(c), (8, 262), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        cv2.imwrite(os.path.join(out, 'cuts', f'{c:07.2f}.jpg'), im, [cv2.IMWRITE_JPEG_QUALITY, 82]); tiles.append(im)
    for sg in segs:
        img = nearest((sg['start'] + sg['end']) / 2)
        if img is not None: cv2.imwrite(os.path.join(out, 'segments', f"{sg['start']:07.2f}-{sg['kind']}.jpg"), img, [cv2.IMWRITE_JPEG_QUALITY, 82])
    if tiles:
        cols = 8; rows = math.ceil(len(tiles) / cols)
        sheet = np.zeros((rows * 270, cols * 480, 3), np.uint8)
        for k, im in enumerate(tiles): r, c = divmod(k, cols); sheet[r * 270:(r + 1) * 270, c * 480:(c + 1) * 480] = im
        cv2.imwrite(os.path.join(out, 'sheet.png'), sheet)
    # ---- summary.md
    L = [f"# style probe — {summary['video']}", '', f"{vw}x{vh} @ {vfps:.2f} fps · {tc(dur)} · samples at {fps}/s", '',
         f"- **cuts:** {n_cuts} = **{summary['cuts_per_min']}/min** (cold open {summary['cold_open_cuts_per_min']}/min) · by minute {summary['cuts_per_min_by_minute']}",
         f"- **held shot:** median {summary['held_median_s']} s · longest {summary['held_max_s']} s",
         f"- **face:** {100 * summary['face_share']:.0f} % of runtime in {summary['face_runs']} runs (median run {summary['face_run_median_s']} s, median face shot {summary['face_shot_median_s']} s)",
         f"- **overlays:** {summary['overlays']} = {summary['overlays_per_min']}/min, {100 * summary['overlay_share']:.0f} % of runtime, median {summary['overlay_median_s']} s · {summary['overlays_moving']} moving / {summary['overlays_still']} still",
         f"- **gradual push (face shots >= 1.5 s):** median {summary['push_median_pct']} % per shot = {summary['push_median_pct_per_s']} %/s",
         f"- **cut zooms:** {summary['cut_zooms_in']} in / {summary['cut_zooms_out']} out · median step x{summary['cut_zoom_median_ratio']} · median hold {summary['cut_zoom_median_hold_s']} s",
         f"- **luma:** mean {summary['luma_mean']} · dark {100 * summary['luma_dark_share']:.0f} % · bright {100 * summary['luma_bright_share']:.0f} %",
         f"- first shot: {summary['first_shot']} · last shot: {summary['last_shot']}", '',
         '## cut zooms (in)', '', '| t | step | hold | shot |', '|---|---|---|---|']
    L += [f"| {tc(z['t'])} | x{z['ratio']} | {z['hold']} s | {tc(z['shot_start'])}–{tc(z['shot_end'])} |" for z in zooms if z['ratio'] > 1]
    L += ['', '## overlays', '', '| t | dur | motion | luma |', '|---|---|---|---|']
    L += [f"| {tc(o['start'])} | {o['dur']} s | {'video' if o['motion'] >= 1.0 else 'still'} ({o['motion']}) | {o['luma']} |" for o in ov]
    open(os.path.join(out, 'summary.md'), 'w', encoding='utf-8').write('\n'.join(L) + '\n')
    print('\n'.join(L[:12]))


if __name__ == '__main__':
    main()
