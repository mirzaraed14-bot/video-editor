"""spans.py <job> <PLAN.md> [--fix]: check every keep span of the PLAN's cut table against words.json and predict the tightened length.
A span 'a-b' must start on a word START and end on a word END. With --fix, an end that equals a word's START (the wt.py v1 bug) is moved
to that word's END, and a start that is not a word start is snapped to the nearest word start; the PLAN is rewritten in place.
Prediction: words inside each span; internal gaps >= 0.12 s count as 0.08 s (tight6); PLAY rows count their stated seconds."""
import json, re, sys
job, plan = sys.argv[1], sys.argv[2]; fix = "--fix" in sys.argv
W = [w for c in json.load(open(f"{job}/transcript/words.json", encoding="utf-8"))["clips"] for w in c["words"] if "start" in w and "end" in w]
starts = {round(w["start"], 2): w for w in W}
txt = open(plan, encoding="utf-8").read(); out = []; _beats = False; total = 0.0; rows = []
for line in txt.split("\n"):
    if line.startswith("## Beats"): _beats = True          # kit: the beats table has the same | K | a | b | c | shape; it is not a cut table
    m = re.match(r"^\| (K\d+) \| (.+?) \| (.+?) \| (.+?) \|$", line)
    if _beats or not m: out.append(line); continue
    k, span, words, rule = m.groups()
    if "PLAY" in span:
        sec = re.search(r"≈\s*([\d.]+)\s*s|\(([\d.]+) s\)", span); 
        o = re.search(r"OBS ([\d.]+)\s*(?:-|->)\s*([\d.]+)", span)
        d = float(o.group(2)) - float(o.group(1)) if o else 0.0
        rows.append((k, d, "PLAY", rule)); total += d; out.append(line); continue
    parts = re.findall(r"([\d.]+)-([\d.]+)", span); new = span; d = 0.0
    for a, b in parts:
        fa, fb = float(a), float(b)
        wa = min(W, key=lambda w: abs(w["start"] - fa)); wb_start = starts.get(round(fb, 2))
        nb = fb
        if wb_start is not None and abs(wb_start["end"] - fb) > 0.005: nb = wb_start["end"]
        if abs(wa["start"] - fa) > 0.005: print(f"  {k}: start {fa} is not a word start (nearest {wa['start']:.2f} '{wa['w']}')")
        if nb != fb: print(f"  {k}: end {fb} = START of '{wb_start['w']}' -> END {nb:.2f}")
        if fix: new = new.replace(f"{a}-{b}", f"{wa['start']:.2f}-{nb:.2f}", 1)
        ws = [w for w in W if w["start"] >= wa["start"] - 0.005 and w["end"] <= nb + 0.005]
        seg = 0.0
        for i, w in enumerate(ws):
            seg += w["end"] - w["start"]
            if i + 1 < len(ws):
                g = ws[i + 1]["start"] - w["end"]; seg += 0.08 if g >= 0.12 else max(g, 0)
        d += seg + 0.08
    out_rule = rule.strip().upper().startswith("OUT")
    rows.append((k, d, "out " if out_rule else "TALK", rule)); total += 0 if out_rule else d
    out.append(line.replace(span, new) if fix else line)
for k, d, kind, rule in rows: print(f"{k:4s} {kind:4s} {d:6.2f}  {rule[:40]}")
print(f"PREDICTED tightened length: {total:.1f} s ({int(total//60)}:{total%60:04.1f})")
if fix: open(plan, "w", encoding="utf-8").write("\n".join(out)); print("PLAN rewritten")
