"""est.py <job> [keep.json]: estimate the TIGHT length of a keep.json (word entries: words + 0.08 s per inner gap > 0.12; time entries as is)."""
import json, os, sys
job = sys.argv[1]; K = json.load(open(sys.argv[2] if len(sys.argv) > 2 else os.path.join(job, "keep.json"), encoding="utf-8"))
ws = json.load(open(os.path.join(job, "transcript", "words.json"), encoding="utf-8"))["clips"][0]["words"]
tot = 0; sec = {}
for e in K["keep"]:
    if e[0] == "t": d = e[2] - e[1]; txt = "[PLAY] " + e[4][:60]
    else:
        i0, i1 = e[0], e[1]; d = 0.0
        for i in range(i0, i1 + 1):
            d += ws[i]["end"] - ws[i]["start"]
            if i > i0: g = ws[i]["start"] - ws[i - 1]["end"]; d += min(g, 0.12) if g > 0 else 0
        d += 0.10; txt = " ".join(ws[i]["w"] for i in range(i0, i1 + 1))[:90]
    tot += d; s = (e[4] if e[0] == "t" else e[3]) if False else None
    print(f"{tot:7.1f} {d:5.1f}  {txt}")
print(f"TOTAL ~{tot:.1f} s")
