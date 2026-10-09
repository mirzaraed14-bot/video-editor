import sys, glob, os, wave
import numpy as np
def load(p):
    w = wave.open(p); sr = w.getframerate(); n = w.getnframes()
    x = np.frombuffer(w.readframes(n), np.int16).astype(np.float32) / 32768
    return x, sr
for p in sorted(glob.glob(os.path.join(sys.argv[1], '*.wav'))):
    x, sr = load(p)
    hop = int(0.02 * sr); win = int(0.08 * sr)
    n = (len(x) - win) // hop
    w = np.hanning(win)
    freqs = np.fft.rfftfreq(win, 1 / sr)
    sub = (freqs >= 25) & (freqs <= 80)
    voice = (freqs >= 300) & (freqs <= 3000)
    hi = (freqs >= 5000) & (freqs <= 10000)
    S_sub, S_voice, S_all = [], [], []
    for i in range(n):
        f = x[i*hop:i*hop+win] * w
        sp = np.abs(np.fft.rfft(f)) ** 2
        S_sub.append(sp[sub].sum()); S_voice.append(sp[voice].sum()); S_all.append(sp.sum())
    db = lambda a: 10 * np.log10(np.array(a) + 1e-12)
    sub_db, voice_db, all_db = db(S_sub), db(S_voice), db(S_all)
    t = np.arange(n) * hop / sr
    # loudness
    rms = np.array([np.sqrt(np.mean(x[i*hop:i*hop+win]**2)) for i in range(n)])
    rdb = 20*np.log10(rms+1e-9)
    floor = np.percentile(rdb, 10); med = np.median(rdb)
    # boom: sub-bass jumps >= 10 dB over the median sub level and sub dominates voice band
    subm = np.median(sub_db)
    events = []; i = 0
    while i < n:
        if sub_db[i] > subm + 14 and sub_db[i] > voice_db[i] + 3:
            j = i
            while j < n and sub_db[j] > subm + 8: j += 1
            if (j - i) * 0.02 >= 0.25: events.append((t[i], (j - i) * 0.02, sub_db[i:j].max() - subm))
            i = j
        else: i += 1
    name = os.path.basename(p)[:-4]
    print(f"{name}: dur {len(x)/sr:.2f}s  rms median {med:.1f} dBFS  10th pct {floor:.1f}  2nd pct {np.percentile(rdb,2):.1f}  peak {rdb.max():.1f}")
    print("   sub-bass hits:", ", ".join(f"{a:.2f}s({d:.1f}s,+{h:.0f}dB)" for a, d, h in events) or "none")
    # quietest 0.5 s windows (pauses) level
    k = 25
    rolling = np.convolve(rdb, np.ones(k)/k, 'valid')
    print(f"   quietest 0.5s window: {rolling.min():.1f} dBFS at {t[np.argmin(rolling)]:.2f}s; 5th pct of 0.5s windows {np.percentile(rolling,5):.1f}")
