#!/usr/bin/env python
# /// script
# requires-python = ">=3.10"
# dependencies = ["opencv-python-headless", "numpy"]
# ///
"""Frame-by-frame nose track for the head lock (the creator's After Effects Stabilize Motion, done by script).

The creator tracks the speaker's NOSE on every frame and applies it as Anchor Point keyframes, which
holds the nose where it sat on the clip's first frame. This computes that track straight from the
source files at the SEQUENCE frame rate (60 fps), using the YuNet nose-tip landmark:
  - the speaker is the face nearest the clip's current crop centre on frame 1, then the face whose nose
    is nearest the previous frame's nose (so a second person in shot is never picked up mid-clip);
  - frames with no detection are interpolated; the track is lightly smoothed (Gaussian, sigma 1.5
    frames) because detector jitter is magnified by the clip's scale.

Input : the live V1 clip list (read_v1 output) + which clip indices to track.
Output: track.json — per clip, the nose position in SOURCE pixels for every timeline frame.

usage: python head_track.py <job_dir> <v1_live.txt> <idx,idx,...> [--fps 60]
"""
import json, os, subprocess, sys
import cv2
import numpy as np

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))   # wherever the repo lives (was hard-coded to E:)
MODEL = os.path.join(REPO, 'assets', 'models', 'face_detection_yunet_2023mar.onnx')
FPS = 60.0
DETECT_W = 1280          # detection width; coordinates are scaled back to full source pixels
SIGMA = 1.5              # smoothing, in frames
MAX_JUMP = 0.12          # a nose may not jump more than this fraction of frame width in one frame


def probe(src):
    out = subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries',
                          'stream=width,height', '-of', 'csv=p=0', src], capture_output=True, text=True).stdout
    w, h = out.strip().split(',')[:2]
    return int(w), int(h)


def frames(src, t0, dur, w, h):
    """One picture per TIMELINE frame, picked the way AE and Premiere show a clip: the source frame that
    starts at or before the frame's time. Not `-ss t0` + `fps=60`: the accurate seek drops the frame
    that straddles the in-point and the fps filter takes the NEAREST frame, so at 23.976 the track ran
    up to a source frame ahead of the picture and read the next shot's face on a clip's last frame
    (2026-09-29). Decoded with the real timestamps (-copyts) and chosen here."""
    dw = min(DETECT_W, w)
    dh = int(round(h * dw / w / 2)) * 2
    st = subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries', 'stream=start_time',
                         '-of', 'csv=p=0', src], capture_output=True, text=True).stdout.strip()
    st = float(st) if st not in ('', 'N/A') else 0.0                 # AE's source time 0 = the first frame
    a, b = t0 + st - 0.2, t0 + st + dur + 0.1
    s0 = max(0.0, a - 1.0)                                  # -t: stop reading after the clip (select alone decodes to EOF)
    cmd = ['ffmpeg', '-hide_banner', '-loglevel', 'info', '-ss', '%.4f' % s0, '-t', '%.4f' % (b - s0 + 0.5), '-copyts', '-i', src, '-an',
           '-vf', 'select=between(t\\,%.4f\\,%.4f),scale=%d:%d,showinfo' % (a, b, dw, dh),
           '-fps_mode', 'passthrough', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-']
    p = subprocess.run(cmd, capture_output=True, stdin=subprocess.DEVNULL)
    pts = [float(l.split('pts_time:')[1].split()[0]) - st for l in p.stderr.decode(errors='ignore').splitlines()
           if 'Parsed_showinfo' in l and 'pts_time:' in l]
    n = min(len(pts), len(p.stdout) // (dw * dh * 3))
    decoded = np.frombuffer(p.stdout[:n * dw * dh * 3], np.uint8).reshape(n, dh, dw, 3)
    pts = np.array(pts[:n])
    n_tl = int(round(dur * FPS))
    pick = [max(0, int(np.searchsorted(pts, t0 + k / FPS + 1e-4, side='right')) - 1) for k in range(n_tl)]
    return decoded[pick], dw / w


def smooth(v, sigma):
    r = int(3 * sigma)
    k = np.exp(-0.5 * (np.arange(-r, r + 1) / sigma) ** 2)
    k /= k.sum()
    pad = np.pad(v, r, mode='edge')
    return np.convolve(pad, k, mode='valid')


def main(job, live_path, idx_list):
    rows = [l.split('|') for l in open(live_path, encoding='utf-8').read().splitlines() if l.strip()]
    live = {int(r[0]): r for r in rows}
    out = {}
    for i in idx_list:
        r = live[i]
        start, end, src_in = float(r[1]), float(r[2]), float(r[3])
        scale, pos = float(r[6]) / 100.0, [float(x) for x in r[7].split(',')]
        src = r[10]
        W, H = probe(src)
        dur = end - start
        n_tl = int(round(dur * FPS))
        arr, k = frames(src, src_in, dur, W, H)
        det = cv2.FaceDetectorYN_create(MODEL, '', (arr.shape[2], arr.shape[1]), score_threshold=0.55)
        # the speaker: the face nearest the current crop centre
        cx_src = W / 2 + (540 - pos[0] * 1080) / scale
        nose, prev, miss = [], None, 0
        for f in range(min(n_tl, len(arr))):
            _, faces = det.detect(arr[f])
            best = None
            if faces is not None and len(faces):
                cands = [(float(x[8]) / k, float(x[9]) / k, float(x[2]) / k) for x in faces]
                if prev is None:
                    best = min(cands, key=lambda c: abs(c[0] - cx_src))
                else:
                    best = min(cands, key=lambda c: (c[0] - prev[0]) ** 2 + (c[1] - prev[1]) ** 2)
                    if abs(best[0] - prev[0]) > MAX_JUMP * W or abs(best[1] - prev[1]) > MAX_JUMP * W:
                        best = None
            if best is None:
                nose.append([np.nan, np.nan]); miss += 1
            else:
                nose.append([best[0], best[1]]); prev = best
        nose = np.array(nose, float)
        while len(nose) < n_tl:                               # decoder came up a frame short
            nose = np.vstack([nose, nose[-1:]])
        for c in (0, 1):                                     # fill gaps, then smooth
            v = nose[:, c]
            ok = ~np.isnan(v)
            if ok.sum() == 0:
                v[:] = (W if c == 0 else H) / 2
            else:
                v[~ok] = np.interp(np.flatnonzero(~ok), np.flatnonzero(ok), v[ok])
            nose[:, c] = smooth(v, SIGMA)
        drift = nose - nose[0]
        out[str(i)] = {'source': src, 'W': W, 'H': H, 'tl_start': start, 'tl_end': end, 'src_in': src_in,
                       'scale': scale * 100, 'pos': pos, 'frames': n_tl, 'missing': miss,
                       'nose': [[round(a, 2), round(b, 2)] for a, b in nose]}
        print('clip %2d  %6.2f-%6.2f  %4d frames  missed %3d  nose moves x %5.1f..%5.1f  y %5.1f..%5.1f px (source)' % (
            i, start, end, n_tl, miss, drift[:, 0].min(), drift[:, 0].max(), drift[:, 1].min(), drift[:, 1].max()))
    json.dump(out, open(os.path.join(job, 'track.json'), 'w', encoding='utf-8'))
    print('wrote', os.path.join(job, 'track.json'))


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], [int(x) for x in sys.argv[3].split(',')])
