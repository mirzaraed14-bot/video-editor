"""author.py: a reaction job's ROUGH CUT from its raw OBS recording (batch 2: Affan hands over raw camera + OBS files, no rough cut).

  PYTHONUTF8=1 python author.py <job> <keep.json>

keep.json: {"clip": "<raw OBS file name>", "gap": 0.45, "keep": [[i0, i1, "A"|"S", "note"], ...]}  word-index ranges of
transcript/words.json, in timeline order. "A" = Affan talking: split at every inter-word gap > `gap` s (dead air out);
"S" = the reviewed video playing: never split (its own pauses are its timing). Writes the EDL to /tmp/video-editor/<job>/cuts.json
(the path splice.sh reads; RENDER=0 refines + frame-snaps it into transcript/cuts.json) and transcript/cuts.draft.json.
"""
import json, os, sys
job, kp = sys.argv[1], sys.argv[2]
K = json.load(open(kp, encoding="utf-8"))
ws = json.load(open(os.path.join(job, "transcript", "words.json"), encoding="utf-8"))["clips"][0]["words"]
gap = K.get("gap", 0.45)
segs = []
for i0, i1, kind, *note in K["keep"]:
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
                         transcript=" ".join(ws[i]["w"] for i in r), kind=kind, words=[r[0], r[-1]]))
for p, q in zip(segs, segs[1:]):
    if q["start"] < p["end"]:                      # a split inside one range: one shared boundary in the gap
        m = round((ws[p["words"][1]]["end"] + ws[q["words"][0]]["start"]) / 2, 3); p["end"] = q["start"] = m
tmp = os.path.join(os.path.expandvars(r"%LOCALAPPDATA%\Temp") if os.name == "nt" else "/tmp", "video-editor", os.path.basename(os.path.abspath(job)))
os.makedirs(tmp, exist_ok=True)
for f in ("cuts.refined.json", "cuts.snapped.json"):            # stale refine outputs would be replayed (rough-cut SKILL § Gotchas)
    if os.path.exists(os.path.join(tmp, f)): os.remove(os.path.join(tmp, f))
out = dict(segments=[{k: v for k, v in s_.items() if k in ("clip", "start", "end", "transcript")} for s_ in segs])
json.dump(out, open(os.path.join(tmp, "cuts.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
json.dump(dict(segments=segs), open(os.path.join(job, "transcript", "cuts.draft.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
kept = sum(s_["end"] - s_["start"] for s_ in segs)
print(f"{len(segs)} segments, {kept:.1f} s kept of {ws[-1]['end']:.1f} s raw -> {tmp}/cuts.json")
