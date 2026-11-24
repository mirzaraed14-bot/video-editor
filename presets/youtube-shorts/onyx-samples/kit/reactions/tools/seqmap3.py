"""seqmap3.py: snap + map a batch-3 reaction's final EDL (after pins.py), the seqmap.py contract with the sample ranges from the kinds.

  PYTHONUTF8=1 python seqmap3.py <job>

1. snaps every boundary of transcript/cuts.json to the 1/60 s grid (round) and refuses an overlap or a non-positive segment;
2. writes transcript/words.tight.json (words on the SEQUENCE timeline, corrections.local.json applied: seqmap.py's rule, a word is
   kept when its START or MIDPOINT survives) and work/seqmap.json {"sample_seq": [[t0, t1, note]], "map": [[raw0, raw1, seq0]]}.
Sample ranges come from transcript/cuts.draft.json's kinds (author3.py), matched to the final segments by order (same count; pins.py
"drop" entries would break that and are refused here). Adjacent S segments (a graft) merge into one range.
"""
import json, os, sys
job = sys.argv[1]; fps = 60
cp = os.path.join(job, "transcript", "cuts.json"); C = json.load(open(cp, encoding="utf-8")); segs = C["segments"]
draft = json.load(open(os.path.join(job, "transcript", "cuts.draft.json"), encoding="utf-8"))["segments"]
def kind_of(s):        # the draft segment overlapping this final one most (polish can split a segment; pins.py can drop one)
    best = max(draft, key=lambda d: min(d["end"], s["end"]) - max(d["start"], s["start"]))
    if min(best["end"], s["end"]) - max(best["start"], s["start"]) > 0: return best
    # a pin may move a whole segment onto a later take (DSH 2026-10-19: 'the' 217.77-218.50 -> 219.40-219.70): the nearest draft
    # segment within 3 s gives its kind, said out loud
    gap = lambda d: max(d["start"] - s["end"], s["start"] - d["end"])
    near = min(draft, key=gap)
    if gap(near) > 3.0: raise SystemExit(f"segment {s['start']}-{s['end']} matches no draft segment")
    print(f"note: segment {s['start']}-{s['end']} takes its kind from the nearest draft segment {near['start']}-{near['end']}")
    return near
for s in segs:
    s["start"] = round(round(s["start"] * fps) / fps, 6); s["end"] = round(round(s["end"] * fps) / fps, 6)
    if s["end"] - s["start"] < 1 / fps - 1e-9: raise SystemExit(f"segment {s} under a frame")
for a, b in zip(segs, segs[1:]):
    if b["start"] < a["end"] - 1e-9 and b["start"] > a["start"]: raise SystemExit(f"overlap {a['end']} / {b['start']}")
json.dump(C, open(cp, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
m, pos = [], 0.0
for s in segs:
    d = round(round((s["end"] - s["start"]) * fps) / fps, 6); m.append((s["start"], s["start"] + d, pos)); pos += d
def r2s(t, clamp=False):
    for a, b, p in m:
        if a - 1e-6 <= t < b + 1e-6: return p + (t - a)
    if not clamp: return None
    a, b, p = min(m, key=lambda x: min(abs(t - x[0]), abs(t - x[1]))); return p + (min(max(t, a), b) - a)
ws = json.load(open(os.path.join(job, "transcript", "words.json"), encoding="utf-8"))["clips"][0]["words"]
cpth = os.path.join(job, "corrections.local.json")
cor = json.load(open(cpth, encoding="utf-8")).get("auto", {}) if os.path.exists(cpth) else {}
out = []
for w in ws:
    if r2s(w["start"]) is None and r2s((w["start"] + w["end"]) / 2) is None: continue
    t = w["w"]; t = cor.get(t, cor.get(t.lower(), t))
    out.append(dict(w=t, start=round(r2s(w["start"], True), 3), end=round(r2s(w["end"], True), 3), raw=w["start"]))
json.dump({"clips": [{"clip": "sequence", "words": out}]}, open(os.path.join(job, "transcript", "words.tight.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=0)
S = []
for (a, b, p), dr in zip(m, [kind_of(s) for s in segs]):
    if dr["kind"] != "S": continue
    if S and abs(S[-1][1] - p) < 1e-3: S[-1][1] = round(p + b - a, 4); S[-1][2] += " + " + dr.get("note", "")[:40]
    else: S.append([round(p, 4), round(p + b - a, 4), dr.get("note", "")[:80]])
json.dump({"sample_seq": S, "map": m}, open(os.path.join(job, "work", "seqmap.json"), "w", encoding="utf-8"), indent=0)
print(f"{len(segs)} segments snapped, {len(out)} words on the sequence ({pos:.3f} s); sample ranges:")
for s in S: print(f"  {s[0]:8.3f}-{s[1]:8.3f}  {s[2]}")
