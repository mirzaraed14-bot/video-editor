"""switches.py: where the SCREEN picture switches (a window change, a new page), to the frame, on the SEQUENCE timeline.

  PYTHONUTF8=1 python switches.py <job> <raw OBS file> [threshold]

Reads work/seqmap.json (seqmap.py: raw OBS time -> sequence time through transcript/cuts.json), samples the screen every 0.25 s of
sequence time (256x144 grey), keeps the steps whose mean change > threshold (default 25: a window switch, not a scroll or a playing
video), then refines each to the exact 60 fps frame (the biggest frame-to-frame change within ±0.3 s). A step that sits ON a cut
(the raw jumps there) is reported as "cut" so the plan can tell a cut-revealed switch from one inside a clip.
Writes work/switches.json [[t, change, "cut"|"clip"], ...] and prints it.
"""
import json, os, subprocess, sys
import numpy as np

job, raw = sys.argv[1], sys.argv[2]; thr = float(sys.argv[3]) if len(sys.argv) > 3 else 25.0
m = json.load(open(os.path.join(job, "work", "seqmap.json")))["map"]
END = m[-1][2] + (m[-1][1] - m[-1][0])


def s2r(t):
    for a, b, p in m:
        if p - 1e-6 <= t < p + (b - a): return a + (t - p)
    return m[-1][1] - 0.02


def frame(t):
    r = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{s2r(t):.4f}", "-i", raw, "-frames:v", "1", "-vf", "scale=256:144,format=gray",
                        "-f", "rawvideo", "-"], capture_output=True)
    return np.frombuffer(r.stdout, np.uint8).astype(np.float32)


ts = list(np.arange(0, END - 0.05, 0.25)); fr = [frame(t) for t in ts]
hits = [ts[i + 1] for i in range(len(ts) - 1) if np.abs(fr[i] - fr[i + 1]).mean() > thr]
cuts = [p for _, _, p in m]
out = []
for T in hits:
    xs = [round(T - 0.3 + k / 60, 4) for k in range(37)]; xs = [x for x in xs if 0 <= x < END]
    f = [frame(x) for x in xs]; d = [np.abs(a - b).mean() for a, b in zip(f, f[1:])]
    k = int(np.argmax(d)); t = round(round(xs[k + 1] * 60) / 60, 4)
    kind = "cut" if min(abs(t - c) for c in cuts) < 1 / 60 + 1e-4 else "clip"
    if not out or t - out[-1][0] > 0.2: out.append([t, round(float(d[k]), 1), kind])
json.dump(out, open(os.path.join(job, "work", "switches.json"), "w"), indent=0)
for x in out: print(x)
