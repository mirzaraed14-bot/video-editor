"""xplay.py: where does a reviewed video PLAY inside Affan's OBS recording? (batch-3 reactions, 2026-10-19)

  uv run --with numpy --with scipy python xplay.py <obs media> <sample media> [t0 t1] [--hop 0.5] [--win 1.5]

The OBS track carries the sample's own audio (desktop capture) under his voice. Every `win` s chunk of the sample (hop `hop`)
is cross-correlated (normalised, 8 kHz, FFT) against the OBS audio in [t0, t1]; a chunk whose peak stands > 6x the median
correlation is a match (obs_t, sample_t). Matches with the same offset (obs_t - sample_t, within 40 ms) and rising obs_t form a
PLAY: printed as OBS a-b = sample c-d. A pause, a seek or a restart starts a new play. Several plays of one stretch are all listed
(he restarts samples), so the caller picks the take to keep.
"""
import subprocess, sys
import numpy as np
from scipy.signal import fftconvolve

SR = 8000


def load(path, t0=None, t1=None):
    cmd = ["ffmpeg", "-v", "error"]
    if t0 is not None: cmd += ["-ss", f"{t0:.3f}"]
    if t1 is not None: cmd += ["-t", f"{t1 - (t0 or 0):.3f}"]
    cmd += ["-i", path, "-vn", "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"]
    return np.frombuffer(subprocess.run(cmd, capture_output=True, check=True).stdout, np.float32).astype(np.float64)


def main():
    a, opt, it = [], {}, iter(sys.argv[1:])
    for x in it:
        if x.startswith("--"): opt[x] = next(it)
        else: a.append(x)
    hop, win = float(opt.get("--hop", 0.5)), float(opt.get("--win", 1.5))
    obs, smp = a[0], a[1]
    t0 = float(a[2]) if len(a) > 2 else 0.0
    t1 = float(a[3]) if len(a) > 3 else None
    O = load(obs, t0, t1); S = load(smp)
    O2 = np.concatenate([[0], np.cumsum(O * O)])
    n = int(win * SR); res = []
    for st in np.arange(0, len(S) / SR - win, hop):
        c = S[int(st * SR): int(st * SR) + n]
        if np.sqrt(np.mean(c * c)) < 1e-3: continue                       # silence in the sample: no signature
        c = (c - c.mean()) / (np.linalg.norm(c - c.mean()) + 1e-12)
        x = fftconvolve(O, c[::-1], mode="valid")
        e = np.sqrt(O2[n:] - O2[:-n] + 1e-12)
        r = x / e
        k = int(np.argmax(r)); med = np.median(np.abs(r)) + 1e-9
        if r[k] / med > 6 and r[k] > 0.25:
            res.append((t0 + k / SR, st, float(r[k]), float(r[k] / med)))
    res.sort()
    plays, cur = [], []
    for m in res:
        if cur and abs((m[0] - m[1]) - (cur[-1][0] - cur[-1][1])) < 0.04 and m[0] - cur[-1][0] < 4.0:
            cur.append(m)
        else:
            if cur: plays.append(cur)
            cur = [m]
    if cur: plays.append(cur)
    for p in plays:
        off = np.median([m[0] - m[1] for m in p])
        print(f"PLAY obs {p[0][0]:8.3f}-{p[-1][0] + win:8.3f}  = sample {p[0][1]:6.2f}-{p[-1][1] + win:6.2f}  offset {off:+9.4f}  "
              f"chunks {len(p):3d}  ncc {np.median([m[2] for m in p]):.2f}")


if __name__ == "__main__":
    main()
