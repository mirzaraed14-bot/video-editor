"""leakcheck.py <job>: killed raw words that leak into a kept segment (overlap > 30 ms and > 35 % of the word): the 'title you' class of bug."""
import json, sys
job = sys.argv[1] if len(sys.argv) > 1 else "."
W = [w for w in json.load(open(f"{job}/transcript/words.json", encoding="utf-8"))["clips"][0]["words"] if "start" in w]
K = json.load(open(f"{job}/keep.json", encoding="utf-8"))["keep"]
kept = set()
for e in K:
    if e[0] != "t":
        for i in range(e[0], e[1] + 1): kept.add(i)
C = json.load(open(f"{job}/transcript/cuts.json", encoding="utf-8"))["segments"]
D = json.load(open(f"{job}/transcript/cuts.draft.json", encoding="utf-8"))["segments"]
n = 0
for s in C:
    if any(d["kind"] == "S" and d["start"] <= s["start"] + 0.01 and s["end"] <= d["end"] + 0.01 for d in D): continue
    for i, w in enumerate(W):
        if i in kept: continue
        ov = min(s["end"], w["end"]) - max(s["start"], w["start"])
        if ov > 0.03 and ov > 0.15 * (w["end"] - w["start"]):
            print(f"seg {s['start']:.3f}-{s['end']:.3f} contains killed word '{w['w']}' {w['start']:.2f}-{w['end']:.2f} ({ov * 1000:.0f} ms)"); n += 1
print(n, "leaks")
