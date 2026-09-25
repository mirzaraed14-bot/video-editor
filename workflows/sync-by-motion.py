#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["opencv-python-headless", "numpy", "scipy"]
# ///
"""sync-by-motion.py — align a voice recording to camera footage that has NO USABLE AUDIO.

`sync-dual-audio.py` needs the camera's own mic as a sync reference. On this channel the camera records a DEAD track
(C1295.MP4, 2026-09-22: flat −93 dB, no modulation — the input is not connected), so there is nothing to correlate.

What still carries the same rhythm is the PICTURE: a talking head moves while speaking and stops in the pauses. This
measures the camera's motion over time, measures the voice's loudness envelope over time, and correlates the two.

  uv run workflows/sync-by-motion.py --camera CAM.MP4 --mic OBS.MP4 [--rate 30] [--max-offset 90] [--json-out F]
      [--windows 7] [--window-len 90]

Two motion signals are measured and BOTH are reported, because they fail differently:
  mouth   frame-to-frame difference inside the mouth box (the face found once with YuNet, lower half of the box,
          widened 1.6x). Tracks speech directly; fooled by a hand passing across the face.
  frame   frame-to-frame difference over the whole picture. Tracks gestures and body; fooled by a static pause with
          idle hand movement, and by anything else in the room that moves.
The offset is taken from whichever gives the sharper peak, and the two are compared in the report: agreement within a
frame is the strongest evidence available without a waveform. Windowed correlation then checks consistency and drift.

ACCURACY. Both signals are sampled at --rate (default 30 Hz), so the raw resolution is ~33 ms, and the peak is
parabolically interpolated. Lip sync tolerates roughly ±40 ms, audio-late reading better than audio-early, so the
result is reported in frames at the camera's rate and the caller should sanity-check one word visually before the mux.
"""
import argparse, json, subprocess, sys
import numpy as np
from scipy.signal import correlate

SRA = 16000


def probe(path):
    out = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'stream=codec_type,r_frame_rate:format=duration',
                          '-of', 'json', path], capture_output=True, text=True, check=True).stdout
    d = json.loads(out); fps = None; frac = None
    for s in d.get('streams', []):
        if s.get('codec_type') == 'video' and s.get('r_frame_rate', '0/0') != '0/0':
            frac = s['r_frame_rate']; n, dd = frac.split('/'); fps = float(n) / float(dd)
    return float(d['format']['duration']), fps, frac


def face_box(video, dur, n=14):
    """The creator's face, once: median YuNet box over n frames spread through the take."""
    import cv2, os, tempfile
    model = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'assets', 'models', 'face_detection_yunet_2023mar.onnx')
    W, H = 960, 540
    det = cv2.FaceDetectorYN_create(model, '', (W, H), score_threshold=0.6)
    boxes = []
    tmp = tempfile.mkdtemp()
    for i in range(n):
        t = dur * (i + 0.5) / n
        f = os.path.join(tmp, f'{i}.png')
        subprocess.run(['ffmpeg', '-v', 'error', '-ss', str(t), '-i', video, '-frames:v', '1', '-vf', f'scale={W}:{H}', '-y', f], capture_output=True)
        img = cv2.imread(f)
        if img is None: continue
        _, dets = det.detect(img)
        if dets is None or not len(dets): continue
        x, y, w, h = max(((d[0], d[1], d[2], d[3]) for d in dets), key=lambda d: d[2] * d[3])
        boxes.append((x / W, y / H, w / W, h / H))
    if len(boxes) < 3: return None
    b = np.median(np.array(boxes), axis=0)
    x, y, w, h = b
    cx = x + w / 2; my = y + h * 0.72                      # mouth sits low in the face box
    mw, mh = w * 1.6, h * 0.75
    return dict(x=max(0.0, cx - mw / 2), y=max(0.0, my - mh / 2), w=min(mw, 1.0), h=min(mh, 1.0), face=[float(v) for v in b])


def motion(video, rate, crop=None, size=(320, 180), rate_expr=None):
    """ONE decode, both signals: mean |frame - previous frame| over the whole picture and inside the mouth crop.

    Decoding a 7 GB 1080p60 file is the whole cost of this tool, so it happens once and the crop is taken in numpy
    (2026-09-22: two decodes for two signals doubled the run for nothing)."""
    # SAMPLE AT THE CAMERA'S EXACT RATE. Asking ffmpeg for fps=60 from a 59.94 source duplicates a frame every ~1000
    # (motion = 0 on those), and fps=30 drops unevenly: either way a slow comb rides on the signal and the windowed
    # offsets then wander monotonically — read as "drift" of −460 ppm at 30 Hz and −2512 ppm at 60 Hz for the same
    # pair (2026-09-22). With the native fraction there is no resampling and no comb.
    vf = f'fps={rate_expr or rate},scale={size[0]}:{size[1]}'
    p = subprocess.Popen(['ffmpeg', '-v', 'error', '-i', video, '-map', '0:v:0', '-vf', vf, '-f', 'rawvideo', '-pix_fmt', 'gray', '-'],
                         stdout=subprocess.PIPE, bufsize=10 ** 8)
    n = size[0] * size[1]; prev = None; whole, mouth = [], []
    if crop:
        x0, x1 = int(crop['x'] * size[0]), int(min(1.0, crop['x'] + crop['w']) * size[0])
        y0, y1 = int(crop['y'] * size[1]), int(min(1.0, crop['y'] + crop['h']) * size[1])
    while True:
        buf = p.stdout.read(n)
        if len(buf) < n: break
        g = np.frombuffer(buf, np.uint8).astype(np.float32).reshape(size[1], size[0])
        if prev is None:
            whole.append(0.0); mouth.append(0.0)
        else:
            d = np.abs(g - prev)
            whole.append(float(d.mean()))
            mouth.append(float(d[y0:y1, x0:x1].mean()) if crop else 0.0)
        prev = g
    p.wait()
    return np.array(whole), np.array(mouth)


def envelope(audio_path, rate):
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', audio_path, '-map', '0:a:0', '-f', 'f32le', '-ac', '1', '-ar', str(SRA), '-'],
                         capture_output=True).stdout
    x = np.frombuffer(raw, np.float32).astype(np.float64)
    hop = int(SRA / rate); n = len(x) // hop
    e = np.sqrt((x[:n * hop].reshape(n, hop) ** 2).mean(1) + 1e-12)
    return 20 * np.log10(e + 1e-12)


def norm(v, floor_db=None):
    v = v.astype(np.float64).copy()
    if floor_db is not None:
        v = np.clip(v, np.percentile(v, 95) - floor_db, None)
    v -= v.mean(); s = v.std()
    return v / s if s > 1e-12 else v


def xcorr(a, b, max_lag):
    """lag>0 means b (mic) starts that many samples AFTER a (camera)."""
    c = correlate(a, b, mode='full')
    lags = np.arange(-len(b) + 1, len(a))
    keep = np.abs(lags) <= max_lag
    c, lags = c[keep], lags[keep]
    k = int(np.argmax(c))
    d = 0.0
    if 0 < k < len(c) - 1:
        y0, y1, y2 = c[k - 1], c[k], c[k + 1]
        den = y0 - 2 * y1 + y2
        if abs(den) > 1e-20: d = float(np.clip(0.5 * (y0 - y2) / den, -1, 1))
    prom = float(c[k]) / (float(np.std(c)) + 1e-12)
    return float(lags[k]) + d, prom, c, lags


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--camera', required=True); ap.add_argument('--mic', required=True)
    ap.add_argument('--rate', type=float, default=0.0, help='0 = the camera native rate (recommended)')
    ap.add_argument('--max-offset', type=float, default=90.0)
    ap.add_argument('--windows', type=int, default=7); ap.add_argument('--window-len', type=float, default=90.0)
    ap.add_argument('--json-out'); ap.add_argument('--signal', choices=['auto', 'mouth', 'frame'], default='auto')
    a = ap.parse_args()

    cdur, cfps, cfrac = probe(a.camera); mdur, _, _ = probe(a.mic)
    if a.rate <= 0:                       # --rate 0 = the camera's native rate, exactly
        a.rate = cfps; rate_expr = cfrac
    else:
        rate_expr = None
    print(f'camera {cdur:.2f}s @ {cfps:.3f} fps · mic {mdur:.2f}s · sampling both at {a.rate:g} Hz')
    box = face_box(a.camera, cdur)
    print(f'face box (normalised) {box["face"]}' if box else 'no face found — mouth signal unavailable')
    env = norm(envelope(a.mic, a.rate), floor_db=55.0)
    whole, mouth = motion(a.camera, a.rate, crop=box, rate_expr=rate_expr)
    sigs = {}
    if box is not None and a.signal in ('auto', 'mouth'): sigs['mouth'] = norm(mouth)
    if a.signal in ('auto', 'frame'): sigs['frame'] = norm(whole)
    ml = int(a.max_offset * a.rate)
    res = {}
    for k, v in sigs.items():
        lag, prom, _, _ = xcorr(v, env, ml)
        res[k] = dict(offset=lag / a.rate, prominence=prom)
        print(f'{k:6s}: offset {lag / a.rate:+8.3f}s  ({lag / a.rate * cfps:+9.1f} camera frames)  peak {prom:.1f}x the correlation noise')
    best = max(res, key=lambda k: res[k]['prominence'])
    off = res[best]['offset']
    if len(res) == 2:
        d = abs(res['mouth']['offset'] - res['frame']['offset'])
        print(f'the two signals agree within {d * 1000:.0f} ms ({d * cfps:.1f} camera frames)' if d < 0.2 else
              f'! the two signals DISAGREE by {d:.3f}s — trust neither without an eyeball check')
    # windowed consistency + drift, on the best signal
    v = sigs[best]; rows = []
    ov0 = max(0.0, off); ov1 = min(cdur, off + mdur)
    centres = np.linspace(ov0 + a.window_len, ov1 - a.window_len, a.windows)
    for cen in centres:
        c0 = int((cen - a.window_len / 2) * a.rate); c1 = int((cen + a.window_len / 2) * a.rate)
        m0 = int((cen - off - a.window_len / 2) * a.rate); m1 = int((cen - off + a.window_len / 2) * a.rate)
        if c0 < 0 or m0 < 0 or c1 > len(v) or m1 > len(env): continue
        lag, prom, _, _ = xcorr(v[c0:c1], env[m0:m1], int(3 * a.rate))
        rows.append((cen, off + lag / a.rate, prom))
        print(f'   window @ {cen / 60:5.2f} min  offset {off + lag / a.rate:+8.3f}s  peak {prom:5.1f}x')
    drift = None
    if len(rows) >= 3:
        good = [r for r in rows if r[2] >= 4]
        if len(good) < 3: good = rows        # a 1-point 'fit' printed +9299 ppm / 0 ms (2026-09-22)
        t = np.array([r[0] for r in good]); o = np.array([r[1] for r in good])
        k, c0 = np.polyfit(t, o, 1)
        resid = o - (k * t + c0)
        drift = dict(ppm=k * 1e6, ms_over_take=k * (t[-1] - t[0]) * 1000, scatter_ms=float(np.abs(resid).max() * 1000), offset_at_0=c0)
        print(f'\noffset {c0:+.3f}s at t=0 · drift {k * 1e6:+.0f} ppm ({k * (t[-1] - t[0]) * 1000:+.0f} ms over the take)'
              f' · scatter ±{np.abs(resid).max() * 1000:.0f} ms (±{np.abs(resid).max() * cfps:.1f} frames)')
    out = dict(camera=a.camera, mic=a.mic, camera_dur=cdur, camera_fps=cfps, mic_dur=mdur, rate=a.rate,
               signals=res, best=best, offset=off, windows=[dict(centre=r[0], offset=r[1], prominence=r[2]) for r in rows], drift=drift,
               note='offset>0: the mic starts that many seconds AFTER the camera')
    if a.json_out:
        json.dump(out, open(a.json_out, 'w', encoding='utf-8'), indent=1)
        print('wrote', a.json_out)


if __name__ == '__main__':
    main()
