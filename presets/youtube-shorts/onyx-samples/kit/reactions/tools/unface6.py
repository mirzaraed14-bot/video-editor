"""unface6.py <plan.json> <placed plan.json>: a face-only beat of the PLACED plan that is a split in the new one goes back to the split:
its face clips get the split style again (G.FACE_SPLIT scale + position, no crop: what build_seq --style gave every face clip) and the
screen clips under them are enabled (apply.py --layout only ever switches screen clips OFF and only styles face-only beats, so it cannot
undo a beat by itself). DOM only. 2026-11-02: Drinkin' Bros r2, the verdict 58.22-62.18 became a split (REACTIONS-V2 rule 5)."""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import apply as A   # noqa: E402
plan, seq = A.load(sys.argv[1]); old = json.load(open(sys.argv[2], encoding="utf-8"))
G = A.G; si, fi = plan["screen_track"], plan["face_track"]
inb = lambda t, beats: any(f["t0"] - 1e-3 <= t < f["t1"] - 1e-3 for f in beats)
m = dict(scale=G.FACE_SPLIT["scale"], pos=G.FACE_SPLIT["pos"], crop=dict(L=0, T=0, R=0, B=0))
jobs = []
for c in seq["v"][fi]["clips"]:
    mid = (c["s"] + c["e"]) / 2
    if inb(mid, old["face"]) and not inb(mid, plan["face"]):
        jobs.append((c["s"], A.motion_js(fi, c["s"], m) + f"var x = at(s.videoTracks[{si}], {c['s']:.4f}); if (!x) return 'NOSCREEN'; x.disabled = false; return 'split ok';"))
print(f"unface6: {len(jobs)} face clip(s) back to the split")
for t, js in jobs:
    r = A.es(A.head(plan) + js + " })()"); print(f"  {t:.3f}: {r}")
    if r != "split ok": raise SystemExit(r)
