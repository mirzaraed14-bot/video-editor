"""scan.py <dump.json> "<Sequence N>" <screen track> t0 t1: where the SCREEN picture changes (window switches, scrolls), sequence time."""
import json, os, subprocess, sys
import numpy as np
sys.path.insert(0, os.path.dirname(__file__)); import geom as G
seq = next(s for s in json.load(open(sys.argv[1])) if s["name"] == sys.argv[2]); tr = seq["v"][int(sys.argv[3])]
t0, t1 = float(sys.argv[4]), float(sys.argv[5])
prev = None; t = t0
while t < t1:
    c = G.clip_at(tr, t)
    if c:
        r = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{G.src_time(c, t):.3f}", "-i", c["p"], "-frames:v", "1", "-vf", "scale=256:144,format=gray", "-f", "rawvideo", "-"], capture_output=True)
        a = np.frombuffer(r.stdout, np.uint8).astype(np.float32)
        if prev is not None and a.size == prev.size:
            d = np.abs(a - prev).mean()
            if d > 4: print(f"{t:7.2f}  change {d:5.1f}")
        prev = a
    t += 0.2
