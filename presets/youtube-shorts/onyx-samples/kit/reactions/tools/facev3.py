"""facev3.py <job>/plan.json [--write]: v3 face framing (REACTIONS-V3 P1-P3, main's final rule 2026-11-10).
ONE scale per face PIECE (a run of consecutive face clips no full graphic covers = a plan['face'] beat: 'why'): the smallest scale in [132, 142] that puts his lips (P95 of the clip's YuNet mouth
detections, camera px -> frame y) at <= y 950 in >= 90 % of the piece's clips, the rest <= y 965 (if impossible: 142 and the clip is flagged). Per CLIP only a static x offset (the head centre)
and a static y offset (the mouth y fed to mgx6.face_motion, clamped so the piece scale is never raised: no head-size pop at a jump cut). No keys. Caption base stays the seam y1038.
Detections are cached in work/face-det.json (YuNet every 0.2 s per clip). Needs cv2: run it with the uv-cached Python 3.11 (see RECIPE-V3.md)."""
import json, os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
path = sys.argv[1]; plan = json.load(open(path, encoding="utf-8")); job = os.path.dirname(os.path.abspath(path))
seq = next(s for s in json.load(open(os.path.join(job, plan["dump"]), encoding="utf-8")) if s["name"] == plan["sequence"])
fc = seq["v"][plan["face_track"]]["clips"]; cachep = os.path.join(job, "work", "face-det.json")
cache = json.load(open(cachep)) if os.path.exists(cachep) else {}
def det(c):
    k = f"{c['s']:.3f}:{c['i']:.3f}:{c['e']:.3f}"
    if k in cache: return cache[k]
    from mouth import mouth_at
    xs, ms = [], []
    for t in np.arange(c["s"] + 0.05, c["e"] - 0.04, 0.2):
        d = mouth_at(c["p"], round(c["i"] + t - c["s"], 3))
        if d: xs.append(d[0]); ms.append(d[1])
    cache[k] = [xs, ms]; json.dump(cache, open(cachep, "w")); return cache[k]
need = lambda m: max((1653 - 950) / (1080 - m), (950 - 227) / m)          # scale that puts mouth cam-y m at frame y 950 with the 1426 px window covered
pieces = {}
for f in plan["face"]: pieces.setdefault(f.get("why", "").split(" |")[0], []).append(f)
out = []; flags = []
for why, fs in pieces.items():
    clips = [c for f in fs for c in fc if c["s"] >= f["t0"] - 0.01 and c["e"] <= f["t1"] + 0.01]; clips = sorted({c["s"]: c for c in clips}.values(), key=lambda c: c["s"])
    info = []
    for c in clips:
        xs, ms = det(c); info.append((c, float(np.median(xs)) if xs else None, float(np.percentile(ms, 95)) if ms else None))
    mps = [m for _, _, m in info if m]
    def lip_at(m, s):          # frame y of his mouth at piece scale s (mouth clamped into [723/s, 1080-703/s])
        hi, lo = 1080 - 703 / s, 723 / s; me = min(max(m, lo), hi); return 950 + (m - me) * s
    s_pick = 1.50
    for s in np.arange(1.32, 1.5001, 0.0025):
        ly = [lip_at(m, s) for m in mps]
        if np.mean([y <= 950.5 for y in ly]) >= 0.9 and max(ly) <= 965.5: s_pick = round(float(s), 4); break
    for c, x, m in info:
        hi, lo = 1080 - 703 / s_pick, 723 / s_pick
        m_eff = min(max(m if m else 560.0, lo), hi); x = x if x is not None else (out[-1]["face_x"][0] if out else 1000.0)
        ly = 950 + ((m if m else 560.0) - m_eff) * s_pick
        if ly > 965.5: flags.append(f"clip {c['s']:.3f}: lips y {ly:.0f} at the piece scale {100 * s_pick:.1f}")
        out.append(dict(t0=round(c["s"], 4), t1=round(c["e"], 4), scale=round(100 * s_pick, 2), why=why, face_x=[round(x, 1), round(m_eff, 1)], lips_y=round(ly)))
    print(f"piece '{why[:34]}': {len(info)} clips, scale {100 * s_pick:.2f}; lips y per clip: {[o['lips_y'] for o in out[-len(info):]]}")
for fl in flags: print("  !", fl)
if "--write" in sys.argv:
    plan["mouth_y"] = 950; plan["face"] = [{k: v for k, v in o.items() if k != "lips_y"} for o in out]
    json.dump(plan, open(path, "w", encoding="utf-8"), indent=1, ensure_ascii=False); print("written", path)
