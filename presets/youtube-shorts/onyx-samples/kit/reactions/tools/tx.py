"""tx.py <job dir> [gap=0.6] : the OBS transcript as timed lines (a new line at every pause >= gap s or sentence end), for planning."""
import json, sys
j = sys.argv[1]; gap = float(sys.argv[2]) if len(sys.argv) > 2 else 0.6
d = json.load(open(f"{j}/transcript/words.json", encoding="utf-8"))
ws = [(w["start"], w["end"], w["w"]) for c in d["clips"] for w in c["words"] if "start" in w and "end" in w]
line, t0, last = [], None, None
def flush():
    if line: print(f"{t0:7.2f}-{last:7.2f} | {' '.join(line)}")
for s, e, w in ws:
    if line and (s - last >= gap):
        flush(); line.clear()
    if not line: t0 = s
    line.append(w); last = e
    if w.endswith(('.', '?', '!')) and len(line) > 6: flush(); line.clear()
flush()
