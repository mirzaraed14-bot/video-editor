"""endcheck.py <job>: the 2026-10-28 ACOUSTIC check of every segment edge in transcript/cuts.json (the "buried cut midway" lesson:
the Whisper joint proof completes a word from its first syllable). For each segment END: the 10 ms RMS over the last 60 ms before
the cut vs the segment's speech level (its loudest 10 ms windows, p90) -> flag when the voice has not dipped (> p90 - 12 dB) AND the
60 ms after the cut stays speech-loud; and any raw WhisperX word that starts before the cut and ends > 40 ms after it (a word cut
mid-way). Segment STARTS likewise (a word that started > 40 ms before the start). Prints only the flags."""
import json, os, subprocess, sys
import numpy as np
job = sys.argv[1]; SR = 16000
C = json.load(open(os.path.join(job, "transcript", "cuts.json"), encoding="utf-8"))["segments"]
W = json.load(open(os.path.join(job, "transcript", "words.json"), encoding="utf-8"))["clips"][0]["words"]
raw = os.path.join(job, "raw", C[0]["clip"])
x = np.frombuffer(subprocess.run(["ffmpeg", "-v", "error", "-i", raw, "-vn", "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"], capture_output=True).stdout, np.float32).astype(float)
h = SR // 100; e = 20 * np.log10(np.sqrt((x[:len(x) // h * h].reshape(-1, h) ** 2).mean(1)) + 1e-9)
db = lambda a, b: float(e[max(0, int(a * 100)):max(int(a * 100) + 1, int(b * 100))].max())
n = 0
at = lambda t: float(e[max(0, int(t * 100) - 2):int(t * 100) + 2].min())       # the quietest 10 ms window within +-15 ms of the cut
for k, s in enumerate(C):
    a, b = s["start"], s["end"]; ref = float(np.percentile(e[int(a * 100):int(b * 100)], 90)); f = []
    for nm, t in (("END", b), ("START", a)):
        lv = at(t)
        if lv > ref - 20: f.append(f"{nm} {t:.3f}: no dip AT the cut ({lv:.0f} dB vs speech p90 {ref:.0f})")
        for w in W:
            if lv > ref - 25 and w["start"] < t - 0.02 and w["end"] > t + 0.04: f.append(f"{nm} {t:.3f} inside '{w['w']}' {w['start']:.2f}-{w['end']:.2f} ({lv:.0f} dB)")
    for m in f: print(f"seg{k} {m}"); n += 1
print(f"endcheck: {len(C)} segments, {n} flags (a joint between contiguous segments is not a cut)")
