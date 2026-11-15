# words2txt.py <words.json> [from_s] [to_s]: print the WhisperX words as timed lines (a new line at each pause > 0.6 s or every ~14 words)
import json, sys
p = sys.argv[1]; a = float(sys.argv[2]) if len(sys.argv) > 2 else 0; b = float(sys.argv[3]) if len(sys.argv) > 3 else 1e9
d = json.load(open(p, encoding="utf-8"))
words = d["words"] if isinstance(d, dict) and "words" in d else d
if isinstance(words, dict): words = list(words.values())
flat = []
def take(w):
    if isinstance(w, dict) and ("word" in w or "w" in w) and "start" in w: flat.append(w)
    elif isinstance(w, dict):
        for v in w.values(): take(v)
    elif isinstance(w, list):
        for v in w: take(v)
take(words)
line, t0, last = [], None, None
for w in flat:
    s = w.get("start"); e = w.get("end", s)
    if s is None or s < a or s > b: continue
    if line and (s - last > 0.6 or len(line) >= 14):
        print(f"[{t0:7.2f}] {' '.join(line)}"); line = []
    if not line: t0 = s
    line.append(w.get("word", w.get("w"))); last = e
if line: print(f"[{t0:7.2f}] {' '.join(line)}")
