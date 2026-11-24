"""xplay2.py <obs> <sample> <t0> <t1> [--chunk 2.0] [--min 0.8]: where a sample PLAYS in the OBS audio, robust version of xplay.py.

Every `chunk` s of the sample is normalised-cross-correlated (8 kHz) against OBS [t0, t1]; a chunk counts when its peak ncc >= min
(xplay.py's peak/median test failed on Wellness: continuous music lifts the median). Matches are grouped into PLAYS by offset
(obs - sample within 25 ms) in sample order; each play prints obs a-b = sample c-d and its offset to 0.1 ms (refined on the play's
best chunk at 16 kHz). Several plays of one stretch are all listed (he restarts / seeks), so the caller picks and grafts.
"""
import subprocess, sys
import numpy as np
from scipy.signal import fftconvolve


def load(p, t0=None, d=None, sr=8000):
    c = ["ffmpeg", "-v", "error"] + (["-ss", f"{t0}"] if t0 is not None else []) + (["-t", f"{d}"] if d else []) + \
        ["-i", p, "-vn", "-ac", "1", "-ar", str(sr), "-f", "f32le", "-"]
    return np.frombuffer(subprocess.run(c, capture_output=True).stdout, np.float32).astype(float)


def main():
    a, opt, it = [], {}, iter(sys.argv[1:])
    for x in it:
        if x.startswith("--"): opt[x] = next(it)
        else: a.append(x)
    obs, smp, t0, t1 = a[0], a[1], float(a[2]), float(a[3])
    ch, mn, SR = float(opt.get("--chunk", 2.0)), float(opt.get("--min", 0.8)), 8000
    O = load(obs, t0, t1 - t0); S = load(smp)
    E = np.concatenate([[0], np.cumsum(O * O)]); n = int(ch * SR); e = np.sqrt(E[n:] - E[:-n] + 1e-9)
    hits = []
    for st in np.arange(0, len(S) / SR - ch, ch / 2):
        c = S[int(st * SR): int(st * SR) + n]
        if np.std(c) < 1e-3: continue
        c = (c - c.mean()) / np.linalg.norm(c - c.mean())
        r = fftconvolve(O, c[::-1], mode="valid") / e
        # every peak >= min (a stretch he played twice matches twice)
        idx = np.where(r >= mn)[0]
        if not len(idx): continue
        groups, cur = [], [idx[0]]
        for k in idx[1:]:
            if k - cur[-1] > SR // 4: groups.append(cur); cur = [k]
            else: cur.append(k)
        groups.append(cur)
        for g in groups:
            k = max(g, key=lambda q: r[q]); hits.append((t0 + k / SR - st, st, float(r[k])))
    hits.sort()
    plays, cur = [], []
    for h in hits:
        if cur and abs(h[0] - cur[-1][0]) < 0.025: cur.append(h)
        else:
            if cur: plays.append(cur)
            cur = [h]
    if cur: plays.append(cur)
    S16 = load(smp, sr=16000); O16 = load(obs, t0, t1 - t0, sr=16000)
    for p in sorted(plays, key=lambda p: min(q[0] + q[1] for q in p)):
        if len(p) < 2: continue
        off = float(np.median([q[0] for q in p])); best = max(p, key=lambda q: q[2])
        s = S16[int(best[1] * 16000): int((best[1] + ch) * 16000)]; bb = None
        for L in range(-40, 41):
            st = int((off - t0 + best[1]) * 16000) + L; o = O16[st:st + len(s)]
            if len(o) < len(s): continue
            c = np.dot(o, s) / (np.linalg.norm(o) * np.linalg.norm(s) + 1e-12)
            if bb is None or c > bb[0]: bb = (c, L)
        off += bb[1] / 16000 if bb else 0
        ss = sorted(q[1] for q in p)
        print(f"PLAY obs {off + ss[0]:8.3f}-{off + ss[-1] + ch:8.3f} = sample {ss[0]:6.2f}-{ss[-1] + ch:6.2f}  offset {off:+10.4f}  chunks {len(p):3d}  ncc {np.median([q[2] for q in p]):.2f}")


if __name__ == "__main__":
    main()
