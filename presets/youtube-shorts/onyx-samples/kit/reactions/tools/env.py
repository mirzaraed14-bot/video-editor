"""env.py <media> <t0> <t1> [ms]: RMS envelope (dBFS) of a stretch, one line per window, for measuring cut points by hand."""
import subprocess, sys, numpy as np
p, t0, t1 = sys.argv[1], float(sys.argv[2]), float(sys.argv[3]); ms = float(sys.argv[4]) if len(sys.argv) > 4 else 10
x = np.frombuffer(subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{t0}", "-t", f"{t1 - t0}", "-i", p, "-vn", "-ac", "1", "-ar", "48000", "-f", "f32le", "-"],
                                 capture_output=True).stdout, np.float32)
n = int(48000 * ms / 1000)
for k in range(len(x) // n):
    v = x[k * n:(k + 1) * n]; db = 20 * np.log10(np.sqrt(np.mean(v * v)) + 1e-9)
    print(f"{t0 + k * ms / 1000:8.3f} {db:6.1f} " + "#" * max(0, int((db + 70) / 2)))
