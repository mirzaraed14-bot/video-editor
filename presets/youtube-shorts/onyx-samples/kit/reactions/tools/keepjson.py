"""keepjson.py <job dir> [<job>/CUT.md] [K9 K18 ...]: keep.json from the K table of CUT.md (spans.py format, rows BEFORE the '## Beats' heading).
Talk rows: each sub-span 'a-b' of the span column (OBS raw seconds) -> a word-index entry [i0, i1, "A", note] snapped to words.json.
PLAY rows: span 'PLAY <who> file a-b (= OBS x-y, ...)' -> ["t", x, y, "S", note] (the OBS window the face camera shows; the play file spans live in seqmap/plays).
Trailing K ids drop those rows (the 'drop in order' list when the placed cut runs over 3:00). The OBS clip name comes from seq.json. Writes <job>/keep.json."""
import json, os, re, sys
if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"): print(__doc__); raise SystemExit(0)
job = sys.argv[1].rstrip("/")
args = sys.argv[2:]; cut = next((a for a in args if a.endswith(".md")), os.path.join(job, "CUT.md")); OUT = {a for a in args if re.fullmatch(r"K\d+", a)}
SJ = json.load(open(os.path.join(job, "seq.json"), encoding="utf-8"))
ws = json.load(open(os.path.join(job, "transcript", "words.json"), encoding="utf-8"))["clips"][0]["words"]
keep = []; beats = False
for line in open(cut, encoding="utf-8").read().split("\n"):
    if line.startswith("## Beats"): beats = True
    m = re.match(r"^\| (K\d+) \| (.+?) \| (.+?) \| (.+?) \|$", line)
    if beats or not m: continue
    k, span, words, rule = m.groups()
    if k in OUT: continue
    if span.startswith("PLAY"):
        o = re.search(r"OBS ([\d.]+)\s*(?:-|->)\s*([\d.]+)", span)
        if not o: raise SystemExit(f"{k}: PLAY row has no '(= OBS a-b ...)' window")
        keep.append(["t", float(o.group(1)), float(o.group(2)), "S", f"{k} PLAY: {words[:60]}"]); continue
    for a, b in re.findall(r"([\d.]+)-([\d.]+)", span):
        fa, fb = float(a), float(b)
        i0 = min((i for i, w in enumerate(ws) if "start" in w), key=lambda i: abs(ws[i]["start"] - fa))
        i1 = min((i for i, w in enumerate(ws) if "end" in w), key=lambda i: abs(ws[i]["end"] - fb))
        if not (abs(ws[i0]["start"] - fa) < 0.02 and abs(ws[i1]["end"] - fb) < 0.02): print("  WARN", k, a, b, "->", ws[i0]["w"], ws[i0]["start"], ws[i1]["w"], ws[i1]["end"])
        keep.append([i0, i1, "A", f"{k}: " + " ".join(w["w"] for w in ws[i0:i1 + 1])])
json.dump(dict(clip=os.path.basename(SJ["obs"].replace("\\", "/")), gap=0.25, keep=keep), open(os.path.join(job, "keep.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
print(len(keep), "entries")
