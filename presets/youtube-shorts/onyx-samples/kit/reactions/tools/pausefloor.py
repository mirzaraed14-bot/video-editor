"""pausefloor.py <job>: the 10 ms RMS (dBFS) inside his between-word gaps >= 0.12 s vs inside words, from the OBS audio, to set tight6 --th.
Prints percentiles; a good --th = the gap P75 + 3 dB, capped so it stays >= 8 dB under the word P10."""
import json, subprocess, sys, glob
import numpy as np
j = sys.argv[1]; SR = 16000
raw = glob.glob(f"{j}/raw/*.mp4")[0]
x = np.frombuffer(subprocess.run(["ffmpeg", "-v", "error", "-i", raw, "-vn", "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"], capture_output=True).stdout, np.float32).astype(float)
h = SR // 100; n = len(x) // h; e = 20 * np.log10(np.sqrt((x[:n * h].reshape(n, h) ** 2).mean(1)) + 1e-9)
W = [w for c in json.load(open(f"{j}/transcript/words.json", encoding="utf-8"))["clips"] for w in c["words"] if "start" in w]
gap, word = [], []
for a, b in zip(W, W[1:]):
    g0, g1 = a["end"] + 0.03, b["start"] - 0.03
    if g1 - g0 >= 0.10 and g1 - g0 < 1.5: gap.extend(e[int(g0 * 100):int(g1 * 100)])
for w in W: word.extend(e[int(w["start"] * 100):int(w["end"] * 100)])
gp, wp = np.percentile(gap, [25, 50, 75, 90]), np.percentile(word, [10, 50])
th = min(gp[2] + 3, wp[0] - 8)
print(f"{j.split('/')[-1]:45s} gap P25/50/75/90 {gp[0]:6.1f} {gp[1]:6.1f} {gp[2]:6.1f} {gp[3]:6.1f} | word P10/50 {wp[0]:6.1f} {wp[1]:6.1f} | suggest --th {th:.1f}")
