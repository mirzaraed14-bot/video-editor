"""p2b4_solve.py <job dir> [--write]: per-clip STATIC face transform (scale %, position x/y) so the head keeps size (<= 3 %) and place (<= 15 px) across every same-camera joint (work/p2b4-det.json).
Base 65 % at (0.5, 0.7234); scale clamped +-10 % of base; the layer covers the 1080 width and its top edge stays on the seam (y 1038); the head top stays >= y 1150 (captions sit on the seam).
Writes work/facexf.json {clip index: [scale, pos_x, pos_y]} and work/p2b4-report.json."""
import json, os, sys, math
import numpy as np
from scipy.optimize import least_squares
J = next((a for a in sys.argv[1:] if not a.startswith("--")), "."); D = json.load(open(os.path.join(J, "work", "p2b4-det.json")))
n = len(D); S0, PX0, PY0 = 0.65, 540.0, 0.72343748807907 * 1920; SEAM = 1038.0
ks = [str(k) for k in range(n)]
J_ = []                                       # joints (k, k+1) with both ends detected
for k in range(n - 1):
    a, b = D[ks[k]], D[ks[k + 1]]
    if a["B"] and b["A"]: J_.append((k, a["B"], b["A"]))
def res(x):
    s, px, py = x[0::3], x[1::3], x[2::3]; r = []
    for k, B, A in J_:
        sz = 0.5 * ((math.log(B["h"] * s[k]) - math.log(A["h"] * s[k + 1])) + (math.log(B["w"] * s[k]) - math.log(A["w"] * s[k + 1])))
        dx = (px[k] + (B["cx"] - 960) * s[k]) - (px[k + 1] + (A["cx"] - 960) * s[k + 1]); dy = (py[k] + (B["cy"] - 540) * s[k]) - (py[k + 1] + (A["cy"] - 540) * s[k + 1])
        hg = lambda v, t: max(0.0, abs(v) - t); r += [hg(sz * 100, 1.5) * 2.0 + sz * 100 * 0.15, hg(dx, 6) / 3.0 + dx / 40.0, hg(dy, 6) / 3.0 + dy / 40.0]
    for k in range(n):
        r += [(s[k] - S0) / S0 * 100 / 10 * 0.03, (px[k] - PX0) / 200 * 0.01, (py[k] - PY0) / 200 * 0.01]
        over = (1920 * s[k] - 1080) / 2 - abs(px[k] - 540); r.append(min(0, over) * 50)                    # horizontal cover
        r.append(min(0, 1035.0 - (py[k] - 540 * s[k])) * 50)                                                   # fix 6: the picture's top edge reaches the seam (<= y 1035, cropped to 1038): never a black sliver
        r.append(min(0, py[k] - 540 * s[k] - (SEAM - 330 * s[k])) * 50)                                      # top edge may rise above the seam by <= 330 px of source (cropped away with Crop Top)
        for e in ("A", "B"):
            q = D[ks[k]][e]
            if q: r.append(min(0, py[k] + (q["cy"] - q["h"] / 2 - 540) * s[k] - 1150) * 5)              # head top clear of the captions
    return np.array(r)
x0 = np.array([S0, PX0, PY0] * n); lo = np.array([S0 * 0.9, 0, 0] * n); hi = np.array([S0 * 1.1, 1080, 2400] * n)
RUN = os.environ.get("RUN", "")        # "t0:t1:min_scale": clips of a run whose head moves more than the cover allows get a larger scale (same lower bound for the whole run), room to shift
if RUN:
    r0, r1, smin = [float(v) for v in RUN.split(":")]
    for k in range(n):
        if r0 <= D[ks[k]]["s"] <= r1: lo[3 * k] = max(lo[3 * k], smin); x0[3 * k] = max(x0[3 * k], smin)
sol = least_squares(res, x0, bounds=(lo, hi), max_nfev=400)
x = sol.x; s, px, py = x[0::3], x[1::3], x[2::3]
xf = {ks[k]: [round(float(s[k] * 100), 3), round(float(px[k] / 1080), 6), round(float(py[k] / 1920), 6), round(float(max(0.0, (SEAM - (py[k] - 540 * s[k])) / (1080 * s[k]) * 100)), 3)] for k in range(n)}
rep = []; bad = 0
for k, B, A in J_:
    ra = B["h"] * s[k] / (A["h"] * s[k + 1]) - 1; rw = B["w"] * s[k] / (A["w"] * s[k + 1]) - 1
    dx = (px[k] + (B["cx"] - 960) * s[k]) - (px[k + 1] + (A["cx"] - 960) * s[k + 1]); dy = (py[k] + (B["cy"] - 540) * s[k]) - (py[k + 1] + (A["cy"] - 540) * s[k + 1])
    b0 = B["h"] * S0 / (A["h"] * S0) - 1; dx0 = (B["cx"] - A["cx"]) * S0; dy0 = (B["cy"] - A["cy"]) * S0
    rep.append(dict(t=D[ks[k + 1]]["s"], size_pct=round(100 * (ra + rw) / 2, 2), dx=round(dx, 1), dy=round(dy, 1), before_size=round(100 * b0, 2), before_dx=round(dx0, 1), before_dy=round(dy0, 1)))
over = [r for r in rep if abs(r["size_pct"]) > 3 or abs(r["dx"]) > 15 or abs(r["dy"]) > 15]
print("clips", n, "joints", len(rep), "cost", round(sol.cost, 2))
print("before: max |size| %.1f %%, max |d| %.0f px; after: max |size| %.1f %%, max |d| %.0f px" % (max(abs(r["before_size"]) for r in rep), max(max(abs(r["before_dx"]), abs(r["before_dy"])) for r in rep), max(abs(r["size_pct"]) for r in rep), max(max(abs(r["dx"]), abs(r["dy"])) for r in rep)))
print("scales", round(min(s) * 100, 1), "-", round(max(s) * 100, 1), "; still over 3 % / 15 px:", len(over)); [print("  ", r) for r in over]
json.dump(rep, open(os.path.join(J, "work", "p2b4-report.json"), "w"), indent=0)
if "--write" in sys.argv: json.dump(xf, open(os.path.join(J, "work", "facexf.json"), "w"), indent=0); print("wrote work/facexf.json")
