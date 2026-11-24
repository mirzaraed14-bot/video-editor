"""dip.py <wav/media> t0 t1 [t0 t1 ...]: the quietest 5 ms point (dBFS, 10 ms RMS) inside each window: the measured cut point for a pin."""
import subprocess, sys, numpy as np
p = sys.argv[1]; a = [float(x) for x in sys.argv[2:]]
for t0, t1 in zip(a[::2], a[1::2]):
    x = np.frombuffer(subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{t0 - 0.01}", "-t", f"{t1 - t0 + 0.02}", "-i", p, "-vn", "-ac", "1", "-ar", "48000", "-f", "f32le", "-"],
                                     capture_output=True).stdout, np.float32)
    best = None
    for k in range(0, len(x) - 480, 240):
        v = x[k:k + 480]; db = 20 * np.log10(np.sqrt(np.mean(v * v)) + 1e-9); t = t0 - 0.01 + (k + 240) / 48000
        if t0 <= t <= t1 and (best is None or db < best[1]): best = (t, db)
    print(f"{t0:.3f}-{t1:.3f}: dip {best[0]:.3f} at {best[1]:.1f} dB")
