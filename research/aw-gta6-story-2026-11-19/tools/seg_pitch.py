# seg_pitch.py <wav> <words.json> <from_s> <to_s> <wav_offset_s> : median f0 per ASR segment (who is speaking, without listening)
import sys, json, numpy as np, librosa
wav, wj, a, b, off = sys.argv[1], sys.argv[2], float(sys.argv[3]), float(sys.argv[4]), float(sys.argv[5])
y, sr = librosa.load(wav, sr=16000, offset=a - off, duration=b - a)
segs = [s for s in json.load(open(wj, encoding='utf-8'))['segments'] if s['end'] > a and s['start'] < b]
for s in segs:
    i0, i1 = int(max(0, s['start'] - a) * sr), int(min(b - a, s['end'] - a) * sr)
    seg = y[i0:i1]
    if len(seg) < sr * 0.3: print(f"{s['start']:8.2f} short | {s['text'].strip()[:70]}"); continue
    f0, vf, _ = librosa.pyin(seg, fmin=70, fmax=400, sr=sr)
    v = f0[~np.isnan(f0)]
    rms = 20*np.log10(np.sqrt(np.mean(seg**2))+1e-9)
    m = f"{np.median(v):6.0f} Hz" if len(v) else "   n/a  "
    print(f"{s['start']:8.2f} {m} {rms:6.1f} dBFS | {s['text'].strip()[:75]}")
