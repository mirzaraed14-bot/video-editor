"""headjump.py <plan.json> [--dump <dump.json>]: the HEAD-JUMP check (main's ADD CHECK, 2026-11-09). At every V1/V2 cut INSIDE a face beat, compare his face on the LAST camera frame before the cut and the FIRST after it
(YuNet, tools6r3/mouth.py): the move of the face centre and of the mouth point in 1080-frame px (camera px x the face piece's scale at that instant, push included) and the size change (eye->chin span).
> 12 px or > 2 % size = FLAG (fix: cover it with the beat's graphic timing, or per-clip facex6m). Needs cv2: uv run --with opencv-python-headless --with numpy python tools/headjump.py plan.json"""
import json, math, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mouth import mouth_at   # noqa: E402
plan = json.load(open(sys.argv[1], encoding="utf-8")); A = sys.argv[2:]
dump = A[A.index("--dump") + 1] if "--dump" in A else os.path.join(os.path.dirname(os.path.abspath(sys.argv[1])), plan["dump"])
seq = next(s for s in json.load(open(dump, encoding="utf-8")) if s["name"] == plan["sequence"])
fc = sorted(seq["v"][plan["face_track"]]["clips"], key=lambda c: c["s"]); FR = 1 / 60
sine = lambda u: -(math.cos(math.pi * min(max(u, 0.0), 1.0)) - 1) / 2
rows, flags = [], 0
for f in plan["face"]:
    cl = [c for c in fc if c["s"] >= f["t0"] - 0.011 and c["e"] <= f["t1"] + 0.011]
    for a, b in zip(cl, cl[1:]):
        if abs(a["e"] - b["s"]) > 0.02: continue                      # not a cut (a gap or a razor at a view edge on the same source)
        if abs((a["i"] + (a["e"] - a["s"])) - b["i"]) < 0.004 and a["p"] == b["p"]: continue   # a razor inside one continuous take: no jump possible
        t = b["s"]; u = (t - f["t0"]) / (f["t1"] - f["t0"]); sc = f.get("scale", 150) * (1 + (f.get("push", 1.0) - 1) * sine(u)) / 100
        pa = mouth_at(a["p"], a["i"] + (a["e"] - a["s"]) - FR); pb = mouth_at(b["p"], b["i"] + FR * 0.5)
        if not pa or not pb: rows.append((t, None, "no detection")); continue
        dx, dm = (pb[0] - pa[0]) * sc, (pb[1] - pa[1]) * sc; sz = ((pb[3] - pb[2]) / (pa[3] - pa[2]) - 1) * 100
        bad = abs(dx) > 12 or abs(dm) > 12 or abs(sz) > 2.0; flags += bad
        rows.append((t, bad, f"face x {dx:+6.1f} px  mouth y {dm:+6.1f} px  size {sz:+5.1f} %  (scale {sc * 100:.1f})"))
for t, bad, msg in rows: print(f"  {t:8.3f}  {'FLAG' if bad else ('?' if bad is None else 'ok  ')}  {msg}")
print(f"head-jump: {len(rows)} cuts inside face beats, {flags} flagged (> 12 px or > 2 % size)")
