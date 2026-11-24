"""seqmap.py: a raw-recording reaction job's transcript on the SEQUENCE timeline (batch 2, built by author.py + build_seq.py).

  PYTHONUTF8=1 python seqmap.py <job> [<keep.json>]

transcript/cuts.json (frame-snapped segments, laid back to back from 0) maps raw OBS time to sequence time. A word is kept when its
START or MIDPOINT lies inside a kept segment (a word the cut only grazes is not captioned). Writes transcript/words.tight.json (the
planlib.Words input; corrections.local.json applied) and work/seqmap.json {"sample_seq": [[t0, t1, note]], "map": [[raw0, raw1, seq0]]}.
"""
import json, os, sys
job = sys.argv[1]; fps = 60
segs = json.load(open(os.path.join(job, "transcript", "cuts.json"), encoding="utf-8"))["segments"]
m, pos = [], 0.0
for s in segs:
    d = round(round((s["end"] - s["start"]) * fps) / fps, 6); m.append((s["start"], s["start"] + d, pos)); pos += d
def r2s(t, clamp=False):
    for a, b, p in m:
        if a - 1e-6 <= t < b + 1e-6: return p + (t - a)
    if not clamp: return None
    a, b, p = min(m, key=lambda x: min(abs(t - x[0]), abs(t - x[1]))); return p + (min(max(t, a), b) - a)
ws = json.load(open(os.path.join(job, "transcript", "words.json"), encoding="utf-8"))["clips"][0]["words"]
cp = os.path.join(job, "corrections.local.json")
cor = json.load(open(cp, encoding="utf-8")).get("auto", {}) if os.path.exists(cp) else {}
out = []
for w in ws:
    if r2s(w["start"]) is None and r2s((w["start"] + w["end"]) / 2) is None: continue   # kept when its START or its MIDPOINT survives
                                                                                          # (WhisperX ends run late: "captions" ended
                                                                                          # 0.3 s after the measured cut, Harbinger)
    t = w["w"]; t = cor.get(t, cor.get(t.lower(), t))
    out.append(dict(w=t, start=round(r2s(w["start"], True), 3), end=round(r2s(w["end"], True), 3), raw=w["start"]))
json.dump({"clips": [{"clip": "sequence", "words": out}]}, open(os.path.join(job, "transcript", "words.tight.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=0)
S = []
if len(sys.argv) > 2:
    for k in json.load(open(sys.argv[2], encoding="utf-8"))["keep"]:
        if k[2] == "S": S.append([round(r2s(ws[k[0]]["start"], True), 3), round(r2s(ws[k[1]]["end"], True), 3), k[3] if len(k) > 3 else ""])
json.dump({"sample_seq": S, "map": m}, open(os.path.join(job, "work", "seqmap.json"), "w"), indent=0)
print(f"{len(out)} words on the sequence ({pos:.3f} s); sample ranges {S}")
