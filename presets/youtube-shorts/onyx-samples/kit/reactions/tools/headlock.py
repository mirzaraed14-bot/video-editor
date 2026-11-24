"""headlock.py <plan.json> [--dump <dump.json>]: per-clip HEAD LOCK for the face beats (fix shift 2026-11-09; main's ADD CHECK: a head jump > 12 px / > 2 % at a cut no graphic covers = fix 'by facex6m per clip').
For every face clip (a take between two cuts) inside a face piece: his face centre, mouth y and eye->chin span on its FIRST and LAST camera frame (YuNet, tools6r3/mouth.py) -> work/headlock.json
{clip start s: [cx0, my0, sz0, cx1, my1, sz1]} (camera px). applyo.py then keys the clip's Position/Scale (every 0.5 s with the push) along the straight line between its two ends: the head sits at the SAME frame point
(centre, plan.mouth_y) and at the SAME size on both sides of every cut; between the cut frames it moves as he really moved. Then simulates the residual jump per cut with the patched face_motion (what Premiere will show).
Needs cv2: uv run --with opencv-python-headless --with numpy python tools/headlock.py plan.json"""
import json, math, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); R3 = HERE; sys.path.insert(0, R3)
from mouth import mouth_at   # noqa: E402
import mgx6   # noqa: E402  (patches geom.face_motion)
import geom as G   # noqa: E402
plan = json.load(open(sys.argv[1], encoding="utf-8")); A = sys.argv[2:]; job = os.path.dirname(os.path.abspath(sys.argv[1]))
if plan.get("mouth_y"): mgx6.MOUTH_Y = float(plan["mouth_y"])
dump = A[A.index("--dump") + 1] if "--dump" in A else os.path.join(job, plan["dump"])
seq = next(s for s in json.load(open(dump, encoding="utf-8")) if s["name"] == plan["sequence"])
fc = sorted(seq["v"][plan["face_track"]]["clips"], key=lambda c: c["s"]); FR = 1 / 60
sine = lambda u: -(math.cos(math.pi * min(max(u, 0.0), 1.0)) - 1) / 2
RMIN, RMAX = 0.96, 1.18
out = {}; sim = []
for f in plan["face"]:
    cl = [c for c in fc if c["s"] >= f["t0"] - 0.011 and c["e"] <= f["t1"] + 0.011]
    meas = {}
    for c in cl:
        d = c["e"] - c["s"]
        a = mouth_at(c["p"], c["i"] + 0.5 * FR); b = mouth_at(c["p"], c["i"] + d - 1.5 * FR)
        meas[round(c["s"], 4)] = (a, b)
    szs = [(m[3] - m[2]) for ab in meas.values() for m in ab if m]
    ref = sorted(szs)[int(len(szs) * 0.8)]      # P80: the head is matched UP to the larger heads (a smaller head cannot be shrunk: the window must stay covered)
    fx = f.get("face_x") or [1000.0, 600.0]
    for c in cl:
        a, b = meas[round(c["s"], 4)]
        a = a or b or (fx[0], fx[1], 0, 0); b = b or a
        if len(a) == 4 and a[3] - a[2] > 0: pass
        sa = (a[3] - a[2]) or ref; sb = (b[3] - b[2]) or ref
        out[f"{c['s']:.4f}"] = [round(a[0], 1), round(a[1], 1), round(sa, 1), round(b[0], 1), round(b[1], 1), round(sb, 1), round(ref, 1)]

def frame_pt(c, side, f):
    """where his face / mouth land on the 1080 frame at a clip's first (side 0) or last (side 1) frame, and the head size in frame px, under the lock"""
    d = out[f"{c['s']:.4f}"]; t = c["s"] if side == 0 else c["e"]; u = (t - f["t0"]) / (f["t1"] - f["t0"])
    cx, my, sz = (d[0], d[1], d[2]) if side == 0 else (d[3], d[4], d[5])
    ratio = min(max(d[6] / sz, RMIN), RMAX)
    m = G.face_motion(f.get("scale", 150) * (1 + (f.get("push", 1.0) - 1) * sine(u)) * ratio, [cx, my])
    s = m["scale"] / 100; px, py = m["pos"][0] * G.W, m["pos"][1] * G.H
    return (px + (cx - 960) * s, py + (my - 540) * s, sz * s)
worst = []
for f in plan["face"]:
    cl = [c for c in fc if c["s"] >= f["t0"] - 0.011 and c["e"] <= f["t1"] + 0.011]
    for a, b in zip(cl, cl[1:]):
        if abs(a["e"] - b["s"]) > 0.02: continue
        pa, pb = frame_pt(a, 1, f), frame_pt(b, 0, f)
        dx, dy, dz = pb[0] - pa[0], pb[1] - pa[1], (pb[2] / pa[2] - 1) * 100
        sim.append((b["s"], dx, dy, dz)); worst.append(max(abs(dx), abs(dy)))
json.dump(out, open(os.path.join(job, "work", "headlock.json"), "w"), indent=0)
for t, dx, dy, dz in sim: print(f"  cut {t:8.3f}: residual face x {dx:+6.1f} px  mouth y {dy:+6.1f} px  size {dz:+5.1f} %  {'FLAG' if max(abs(dx), abs(dy)) > 12 or abs(dz) > 2 else 'ok'}")
print(f"headlock: {len(out)} clips -> work/headlock.json; {len(sim)} cuts simulated, worst residual {max(worst):.1f} px, {sum(1 for _, dx, dy, dz in sim if max(abs(dx), abs(dy)) > 12 or abs(dz) > 2)} still > 12 px / 2 %")
