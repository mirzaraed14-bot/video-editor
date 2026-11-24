import sys, subprocess, re
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
f = sys.argv[1]
p = subprocess.run(["ffmpeg", "-nostats", "-hide_banner", "-i", f, "-vn", "-af", "ebur128=peak=true", "-f", "null", "-"], capture_output=True, text=True, encoding="utf-8", errors="replace")
err = p.stderr
M = [(float(t), float(m)) for t, m in re.findall(r"t:\s*([\d.]+)\s+TARGET:.*?M:\s*(-?[\d.]+|-inf)", err.replace("M:-", "M: -")) if m not in ("-inf",)] if False else []
for line in err.splitlines():
    m = re.search(r"t:\s*([\d.]+)\s.*?M:\s*(-?\d+\.?\d*)\s", line)
    if m: M.append((float(m.group(1)), float(m.group(2))))
I = re.findall(r"I:\s+(-?[\d.]+) LUFS", err); LRA = re.findall(r"LRA:\s+([\d.]+) LU", err); TP = re.findall(r"Peak:\s+(-?[\d.]+) dBFS", err)
# loudest 3 s window of momentary values (mean of M in window)
best = (None, -999)
for i, (t, _) in enumerate(M):
    w = [m for tt, m in M if t <= tt < t + 3.0]
    if len(w) > 20:
        a = sum(w) / len(w)
        if a > best[1]: best = (t, a)
print(f"{f.split('/')[-1]} I={I[-1] if I else '?'} LUFS LRA={LRA[-1] if LRA else '?'} TP={TP[-1] if TP else '?'} dBFS loudest3s_start={best[0]} mean_M={best[1]:.1f}")
