"""seqwords.py: map a recording's WhisperX words through a sequence's A1 clips to sequence time.

  python seqwords.py <seq-dump.json> "<Sequence N>" <job>/transcript/words.json <out.json>
Writes [{w, start, end, clip}] in sequence seconds (a word kept only if its middle lies inside a kept clip) and prints
the transcript one A1 clip per line with the clip's sequence span.
"""
import json, sys
dump, name, wpath, out = sys.argv[1:5]
seq = next(s for s in json.load(open(dump)) if s["name"] == name)
a1 = seq["a"][0]["clips"]
d = json.load(open(wpath, encoding="utf-8"))
clips = d["clips"] if isinstance(d["clips"], list) else list(d["clips"].values())
words = clips[0]["words"]
res = []
for k, c in enumerate(a1):
    dur = c["e"] - c["s"]
    for x in words:
        if "start" not in x: continue
        m = (x["start"] + x["end"]) / 2
        if c["i"] <= m < c["i"] + dur:
            res.append(dict(w=x["w"], start=round(c["s"] + x["start"] - c["i"], 3), end=round(min(c["s"] + x["end"] - c["i"], c["e"]), 3), clip=k))
json.dump(res, open(out, "w", encoding="utf-8"), indent=0, ensure_ascii=False)
for k, c in enumerate(a1):
    print(f"{k:3} [{c['s']:7.2f}-{c['e']:7.2f}] " + " ".join(x["w"] for x in res if x["clip"] == k))
