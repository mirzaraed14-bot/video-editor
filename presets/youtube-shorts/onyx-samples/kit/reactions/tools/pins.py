"""pins.py: apply MEASURED boundary pins to a reaction job's final EDL (after splice RENDER=0 + polish-boundaries + cutcheck).

  PYTHONUTF8=1 python pins.py <job>            # reads <job>/work/pins.json, rewrites transcript/cuts.json, prints every change

work/pins.json: {"starts": [[old_start, new_start, why]], "ends": [[old_end, new_end, why]], "drop": [[start, end, why]]}
Each pin names its segment by the boundary it moves (within 30 ms), so a pin can never land on the wrong segment; a moved boundary
must stay inside its own gap (never past the neighbour), and a pinned segment is marked no_refine. "drop" removes whole segments (a
restart, a fragment the video replays later). The pins were measured on the 5-20 ms envelope of work/seq-a1.wav: why says what.
Re-run splice.sh AFTER this would overwrite it (splice reads /tmp): this is the last step on the EDL.
"""
import json, os, sys
job = sys.argv[1]
P = json.load(open(os.path.join(job, "work", "pins.json"), encoding="utf-8"))
cp = os.path.join(job, "transcript", "cuts.json"); c = json.load(open(cp, encoding="utf-8")); S = c["segments"]
for a, b, why in P.get("drop", []):
    k = next((i for i, s in enumerate(S) if abs(s["start"] - a) < 0.03 and abs(s["end"] - b) < 0.03), None)
    if k is None and "--rerun" in sys.argv: print(f"drop {a}-{b}: already dropped"); continue
    if k is None: raise SystemExit(f"drop: no segment {a}-{b}")
    print(f"drop seg {k} {S[k]['start']:.3f}-{S[k]['end']:.3f} '{S[k].get('transcript', '')[:50]}'  ({why})"); S.pop(k)
for key, other in (("ends", "end"), ("starts", "start")):     # ends first: a start pin may use the gap an end pin opens
    for old, new, why in P.get(key, []):
        k = min(range(len(S)), key=lambda i: abs(S[i][other] - old))
        if abs(S[k][other] - old) > 0.03 and min(abs(x[other] - new) for x in S) < 0.009:    # 2026-10-27: re-run safe (already pinned; seqmap3 snaps to 1/60)
            print(f"{key} {old} -> {new}: already pinned"); continue
        if abs(S[k][other] - old) > 0.03: raise SystemExit(f"{key}: no boundary at {old} (nearest {S[k][other]:.3f})")
        if other == "start" and k > 0 and S[k - 1]["end"] > new + 1e-4: raise SystemExit(f"start pin {new} crosses the previous end {S[k - 1]['end']}")
        if other == "end" and k + 1 < len(S) and S[k + 1]["start"] < new - 1e-4: raise SystemExit(f"end pin {new} crosses the next start {S[k + 1]['start']}")
        print(f"seg {k}: {other} {S[k][other]:.4f} -> {new}  ({why})"); S[k][other] = new; S[k]["no_refine"] = True
json.dump(c, open(cp, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
print(f"{len(S)} segments, {sum(s['end'] - s['start'] for s in S):.2f} s")
