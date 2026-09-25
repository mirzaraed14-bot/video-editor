#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["numpy"]
# ///
"""style-audio.py <reference_dir> — the two comedy devices in the VOICE of a finished edit, measured.

Reads <ref>/raw/*.mov|*.wav (the audio), <ref>/probe/probe.json (the hard cuts) and <ref>/transcript/words.json.
  SLOW-DOWNS  a speed change without pitch correction drops the voice's pitch by the same ratio. Frame-wise f0 by
              autocorrelation (40 ms frames, 10 ms hop, 70–400 Hz, voiced when RMS is over the floor), median-smoothed;
              a slow-down is >= 0.35 s where f0 <= 0.84 x the speaker's median f0 (a 0.75x speed reads as 0.75x pitch).
  CHOPPED WORDS  a hard cut where the audio itself breaks inside a word: RMS 30 ms before the cut is speech-level and
              the drop across the cut is >= 12 dB while a transcript word spans the cut (the "cut it midway").
Writes <ref>/audio.json and prints both lists with the words around them.
"""
import glob, json, os, subprocess, sys, statistics
import numpy as np

ref = sys.argv[1]
src = (glob.glob(os.path.join(ref, 'raw', '*.mov')) + glob.glob(os.path.join(ref, 'raw', '*.wav')) + glob.glob(os.path.join(ref, 'raw', '*.mp4')))[0]
SR = 16000
x = np.frombuffer(subprocess.run(['ffmpeg', '-v', 'error', '-i', src, '-ac', '1', '-ar', str(SR), '-f', 'f32le', '-'], capture_output=True).stdout, np.float32)
words = []
wp = os.path.join(ref, 'transcript', 'words.json')
if os.path.exists(wp):
    for c in json.load(open(wp, encoding='utf-8'))['clips']: words += c['words']
    words.sort(key=lambda w: w['start'])
cuts = json.load(open(os.path.join(ref, 'probe', 'probe.json'), encoding='utf-8'))['cuts']
tc = lambda t: f'{int(t // 60)}:{t % 60:05.2f}'
said = lambda a, b: ' '.join(w['w'] for w in words if a - 0.1 <= w['start'] <= b)

# ---- f0 track
FR, HOP = int(0.040 * SR), int(0.010 * SR)
lo, hi = int(SR / 400), int(SR / 70)
n = (len(x) - FR) // HOP
rms = np.array([float(np.sqrt(np.mean(x[i * HOP:i * HOP + FR] ** 2)) + 1e-9) for i in range(n)])
floor = np.percentile(rms, 20) * 4
f0 = np.zeros(n)
win = np.hanning(FR)
for i in range(n):
    if rms[i] < floor: continue
    fr = x[i * HOP:i * HOP + FR] * win; fr = fr - fr.mean()
    ac = np.correlate(fr, fr, 'full')[FR - 1:]
    if ac[0] <= 0: continue
    seg = ac[lo:hi]
    k = int(np.argmax(seg)) + lo
    if ac[k] / ac[0] >= 0.45: f0[i] = SR / k
voiced = f0 > 0
med = float(np.median(f0[voiced])) if voiced.any() else 0
# median smooth (5 frames) then find low runs
f = f0.copy()
for i in range(2, n - 2):
    w = [v for v in f0[i - 2:i + 3] if v > 0]
    f[i] = statistics.median(w) if len(w) >= 3 else 0
low = (f > 0) & (f <= 0.84 * med)
slow, i = [], 0
while i < n:
    if not low[i]: i += 1; continue
    j = i
    while j < n and (low[j] or (j + 3 < n and low[j + 1:j + 4].any() and f[j] == 0)): j += 1
    a, b = i * HOP / SR, j * HOP / SR
    if b - a >= 0.35:
        pf = float(np.median(f[i:j][f[i:j] > 0]))
        slow.append(dict(start=round(a, 2), end=round(b, 2), dur=round(b - a, 2), pitch_ratio=round(pf / med, 2), words=said(a, b)))
    i = j

# ---- chopped words at hard cuts
def db(a, b):
    s = x[max(0, int(a * SR)):int(b * SR)]
    return 20 * np.log10(float(np.sqrt(np.mean(s ** 2))) + 1e-9) if len(s) else -120
chopped = []
for c in cuts:
    w = next((w for w in words if w['start'] + 0.05 <= c <= w['end'] - 0.02), None)
    if not w: continue
    before, after = db(c - 0.035, c - 0.005), db(c + 0.005, c + 0.035)
    if before > -40 and before - after >= 12:
        chopped.append(dict(t=round(c, 2), word=w['w'], into=round(c - w['start'], 2), drop_db=round(before - after, 1), context=said(c - 1.5, c + 1.2)))
json.dump(dict(median_f0=round(med, 1), slowdowns=slow, chopped=chopped), open(os.path.join(ref, 'audio.json'), 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
print(f'median f0 {med:.0f} Hz · {len(slow)} pitch-drop stretches · {len(chopped)} chopped words at hard cuts')
for s in slow: print(f"  SLOW {tc(s['start'])} {s['dur']:.2f}s pitch x{s['pitch_ratio']}  «{s['words']}»")
for c in chopped: print(f"  CHOP {tc(c['t'])} '{c['word']}' {c['into']}s in, -{c['drop_db']} dB  «{c['context']}»")
