"""facex6m.py <job>/plan.json [--pct 90] [--dry]: every face-only piece gets face_x = [face centre x, mouth y] (camera px; x = the median,
mouth y = the --pct percentile (default 90: his LOWEST mouth in the beat) of YuNet detections every 0.25 s inside the piece; the leather
chair left of x 820 ignored), so mgx6's patched geom.face_motion puts his MOUTH at or above plan["mouth_y"] for the whole beat, head dips
included (2026-11-02 review: a 7-sample median let the caption sit on his lips at 109 s). Prints each piece's mouth spread."""
import json, os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mouth import mouth_at   # noqa: E402
path = sys.argv[1]; A = sys.argv[2:]
PCT = float(A[A.index("--pct") + 1]) if "--pct" in A else 90.0; DRY = "--dry" in A
plan = json.load(open(path, encoding="utf-8")); job = os.path.dirname(os.path.abspath(path))
seq = next(s for s in json.load(open(os.path.join(job, plan["dump"]), encoding="utf-8")) if s["name"] == plan["sequence"])
fc = seq["v"][plan["face_track"]]["clips"]
cache = {}
MY = float(plan.get("mouth_y", 915)); WT, WB = 227.0, 1653.0          # the covered window (mgx6.face_motion)
def need(my): return 100 * max((WB - MY) / (1080 - my), (MY - WT) / my) + 0.05   # the scale that keeps the mouth at MY, window covered
groups = {}
for f in plan["face"]: groups.setdefault(f.get("why", f"{f['t0']}").split(" |")[0].strip(), []).append(f)   # RP.punch marks its pieces "<why> |"
for why, fs in groups.items():
    # ONE framing per beat (the head stays put across its pieces, the punch pieces zoom about the same mouth point): x = the median,
    # mouth y = the PCT percentile of every 0.25 s detection across the whole beat
    xs, ms = [], []
    for f in fs:
        for t in np.linspace(f["t0"] + 0.08, f["t1"] - 0.08, max(3, int((f["t1"] - f["t0"]) / 0.25) + 1)):
            c = next((c for c in fc if c["s"] <= t < c["e"]), None)
            if not c: continue
            key = round(c["i"] + t - c["s"], 2)
            if key not in cache: cache[key] = mouth_at(c["p"], key)
            d = cache[key]
            if d: xs.append(d[0]); ms.append(d[1])
    if not xs: print(f"  ! {why[:40]}: no detection"); continue
    LIP, CAP_TOP = 20.0, 1000.0              # lower-lip bottom ~ mouth (corner mean) + 20 camera px; the caption block's top ~ y 1003
    for pct in (PCT, 97.5, 100.0):           # escalate until his LOWEST mouth in the beat keeps the lips above the caption line
        fx = [round(float(np.median(xs)), 1), round(float(np.percentile(ms, pct)), 1)]
        base = max(150.0, need(fx[1]))
        worst = MY + (max(ms) - fx[1] + LIP) * base / 100
        if worst <= CAP_TOP: break
    print(f"    beat '{why[:30]}': mouth P{pct:g} {fx[1]}, base scale {base:.1f}, worst lip bottom y {worst:.0f}" + ("  !! over the caption" if worst > CAP_TOP else ""))
    for f in fs:
        old = (f.get("face_x"), f.get("scale"))
        f["plan_scale"] = f.get("plan_scale", f["scale"])
        f["face_x"] = fx; f["scale"] = round(max(need(fx[1]), base * f["plan_scale"] / 150.0), 1); f["fx"] = True
        print(f"  face {f['t0']:7.2f}-{f['t1']:7.2f}: mouth y min {min(ms):.0f} med {np.median(ms):.0f} max {max(ms):.0f} (n {len(ms)}) -> face_x {fx} scale {f['scale']} (was {old})  ({why[:36]})")
if not DRY: json.dump(plan, open(path, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
