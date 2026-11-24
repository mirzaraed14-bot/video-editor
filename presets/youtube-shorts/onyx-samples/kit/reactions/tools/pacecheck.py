"""pacecheck.py <job>: rule (a): inside his talk no word gap > 0.30 s inside a kept segment, head/tail air per segment <= 0.12 s (measured on transcript/cuts.json vs words.json + the 10 ms envelope)."""
import json, sys, numpy as np
job = sys.argv[1]; TH = float(sys.argv[2]) if len(sys.argv) > 2 else -47.1
C = json.load(open(f"{job}/transcript/cuts.json", encoding="utf-8"))["segments"]; D = json.load(open(f"{job}/transcript/cuts.draft.json", encoding="utf-8"))["segments"]
ws = [w for w in json.load(open(f"{job}/transcript/words.json", encoding="utf-8"))["clips"][0]["words"] if "start" in w]; e = np.load(f"{job}/work/env10.npy")
bad = 0
for s in C:
    if any(d["kind"] == "S" and d["start"] <= s["start"] + .01 and s["end"] <= d["end"] + .01 for d in D): continue
    i0, i1 = int(round(s["start"] * 100)), int(round(s["end"] * 100)); q = e[i0 + 5:i1 - 5] <= TH; j = 0
    while j < len(q):
        if q[j]:
            m = j
            while m < len(q) and q[m]: m += 1
            if (m - j) / 100 > 0.30: bad += 1; print(f"  quiet {(m - j) / 100:.2f} s at {s['start'] + (j + 5) / 100:.2f} (seg {s['start']:.2f})")
            j = m
        else: j += 1
    i0, i1 = int(round(s["start"] * 100)), int(round(s["end"] * 100)); l = np.where(e[i0:i1] > TH)[0]
    if len(l):
        head, tail = l[0] / 100, (i1 - i0 - l[-1] - 1) / 100
        if head > 0.12 or tail > 0.12: print(f"  air head {head:.2f} tail {tail:.2f} seg {s['start']:.2f}")
print(bad, "gaps > 0.30 s")
