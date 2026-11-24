"""author3.py: author.py (reactions/tools) + TIME entries, for the batch-3 reactions (2026-10-19).

  PYTHONUTF8=1 python author3.py <job> <keep.json>

keep.json {"clip": "<raw OBS file>", "gap": 0.45, "keep": [...]} in timeline order, each entry one of
  [i0, i1, "A", note]             word-index range of transcript/words.json, split at every inter-word gap > `gap` (dead air out)
  ["t", t0, t1, "S"|"A", note]    an exact RAW time range, pinned (no_refine): a sample play measured with xplay.py (WhisperX drops
                                  most of the replayed sample's words, so its edges come from the audio match, never from words)
Why a copy and not an edit of author.py: the 3:00 cap (Affan 2026-10-19) keeps only excerpts of each sample, cut at the sample's
own sentence edges, and those edges are measured times. Writes %LOCALAPPDATA%/Temp/video-editor/<job>/cuts.json (splice.sh's input)
and transcript/cuts.draft.json (with kind + note per segment: seqmap3.py reads the kinds back).
"""
import json, os, sys
job, kp = sys.argv[1], sys.argv[2]
K = json.load(open(kp, encoding="utf-8"))
ws = json.load(open(os.path.join(job, "transcript", "words.json"), encoding="utf-8"))["clips"][0]["words"]
gap = K.get("gap", 0.45)
segs = []
for e in K["keep"]:
    if e[0] == "t":
        _, t0, t1, kind, *note = e
        txt = " ".join(w["w"] for w in ws if t0 <= (w["start"] + w["end"]) / 2 < t1)
        segs.append(dict(clip=K["clip"], start=round(t0, 3), end=round(t1, 3), transcript=txt, kind=kind, no_refine=True,
                         note=note[0] if note else ""))
        continue
    i0, i1, kind, *note = e
    runs, cur = [], [i0]
    for i in range(i0 + 1, i1 + 1):
        if kind == "A" and ws[i]["start"] - ws[i - 1]["end"] > gap:
            runs.append(cur); cur = [i]
        else:
            cur.append(i)
    runs.append(cur)
    for r in runs:
        a, b = ws[r[0]], ws[r[-1]]
        segs.append(dict(clip=K["clip"], start=round(a["start"] - 0.06, 3), end=round(b["end"] + 0.08, 3),
                         transcript=" ".join(ws[i]["w"] for i in r), kind=kind, words=[r[0], r[-1]], note=note[0] if note else ""))
for p, q in zip(segs, segs[1:]):
    if q["start"] < p["end"] and q["start"] > p["start"]:          # a split inside one range: one shared boundary in the gap
        if p.get("no_refine"): q["start"] = p["end"]
        elif q.get("no_refine"): p["end"] = q["start"]
        else:
            m = round((ws[p["words"][1]]["end"] + ws[q["words"][0]]["start"]) / 2, 3); p["end"] = q["start"] = m
tmp = os.path.join(os.path.expandvars(r"%LOCALAPPDATA%\Temp") if os.name == "nt" else "/tmp", "video-editor", os.path.basename(os.path.abspath(job)))
os.makedirs(tmp, exist_ok=True)
for f in ("cuts.refined.json", "cuts.snapped.json"):            # stale refine outputs would be replayed (rough-cut SKILL § Gotchas)
    if os.path.exists(os.path.join(tmp, f)): os.remove(os.path.join(tmp, f))
keys = ("clip", "start", "end", "transcript", "no_refine")
out = dict(segments=[{k: v for k, v in s_.items() if k in keys} for s_ in segs])
json.dump(out, open(os.path.join(tmp, "cuts.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
json.dump(dict(segments=segs), open(os.path.join(job, "transcript", "cuts.draft.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
kept = sum(s_["end"] - s_["start"] for s_ in segs)
ks = sum(s_["end"] - s_["start"] for s_ in segs if s_["kind"] == "S")
print(f"{len(segs)} segments, {kept:.1f} s kept ({ks:.1f} s of sample plays) of {ws[-1]['end']:.1f} s raw -> {tmp}/cuts.json")
