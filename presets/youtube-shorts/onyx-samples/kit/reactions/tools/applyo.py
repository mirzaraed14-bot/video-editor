"""applyo.py <plan.json> <apply.py flags...>: applyx.py (mgx6's face_motion patch) + the two things this reaction needs that apply.py has no flag for:

  push   a face piece with "push": 1.04 gets ONE eased (inOutSine) keyframed push-in across the whole beat: Scale/Position/Crop keys every 0.5 s on EVERY face clip of the
         piece (a piece spans several clips, all driven by the same beat clock), the mouth held at plan["mouth_y"] by face_motion at each key.
  full   a view with "full": true (the channel page, beat 4) fills the WINDOW (0,227,1080,1653), not the top panel: the screen clip's Motion is computed against that box and the
         face clip under it is switched OFF (the cam shows as the inset_cam overlay instead). Leak/gap checks use the window box for it.
--verify additionally reads the pushed face clips back (Scale time-varying) and that the face under a full view is disabled.
"""
import json, math, os, runpy, sys
HERE = os.path.dirname(os.path.abspath(__file__))
R3 = HERE; TOOLS = HERE
sys.path.insert(0, R3); sys.path.insert(0, TOOLS)
import mgx6   # noqa: E402,F401
import apply as A   # noqa: E402
import geom as G   # noqa: E402
import viewpatch   # noqa: E402,F401  (per-view box + crop_left_src, fix shift)

plan0 = json.load(open(sys.argv[1], encoding="utf-8"))
if plan0.get("mouth_y"): mgx6.MOUTH_Y = float(plan0["mouth_y"])
WIN = (0, 227, 1080, 1653)
sine = lambda u: -(math.cos(math.pi * min(max(u, 0.0), 1.0)) - 1) / 2
_hlp = os.path.join(os.path.dirname(os.path.abspath(sys.argv[1])), "work", "headlock.json")
HL = json.load(open(_hlp)) if os.path.exists(_hlp) else {}
_sxp = os.path.join(os.path.dirname(os.path.abspath(sys.argv[1])), "work", "splitx.json")
SX = json.load(open(_sxp)) if os.path.exists(_sxp) else {}

_orig_jobs = A.layout_jobs


def layout_jobs_o(plan, seq):
    jobs, probs = _orig_jobs(plan, seq)
    si, fi = plan["screen_track"], plan["face_track"]
    face_clips = seq["v"][fi]["clips"]; scr = seq["v"][si]["clips"]
    out = []
    for label, js in jobs:
        if label.startswith("face "):
            st = float(label.split()[1]); f = next((f for f in plan["face"] if f["t0"] - 0.01 <= st < f["t1"] - 0.01), None)
            c = next((c for c in face_clips if abs(c["s"] - st) < 0.006), None)
            if f and c and f.get("push"):
                ts = sorted({round(c["s"], 4), round(c["e"], 4)} | {round(c["s"] + 0.5 * k, 4) for k in range(1, int((c["e"] - c["s"]) / 0.5) + 1) if c["s"] + 0.5 * k < c["e"]})
                keys = []; hl = HL.get(f"{c['s']:.4f}")
                for t in ts:
                    u = (min(max(t, f["t0"]), f["t1"]) - f["t0"]) / (f["t1"] - f["t0"]); sc_t = f.get("scale", 132) * (1 + (f["push"] - 1) * sine(u)); fx_t = f.get("face_x")
                    if hl:                      # head lock (tools/headlock.py): the head on the SAME frame point and at the SAME size on both sides of every cut; along the straight line between the clip's two ends
                        w_ = (t - c["s"]) / max(c["e"] - c["s"], 1e-6); L_ = lambda a_, b_: a_ + (b_ - a_) * w_
                        fx_t = [L_(hl[0], hl[3]), L_(hl[1], hl[4])]; sc_t *= min(max(hl[6] / L_(hl[2], hl[5]), 0.96), 1.18)
                    keys.append((c["i"] + (t - c["s"]), G.face_motion(sc_t, fx_t)))
                js = A.motion_js(fi, c["s"], None, keys) + f"var x = at(s.videoTracks[{si}], {c['s']:.4f}); if (x) x.disabled = true;"
                label = f"face {c['s']:.3f} (push {f['push']}, {len(keys)} keys)"
        out.append((label, js))
    jobs = out
    # R9 P2b for the SPLIT-stage face clips: one STATIC (scale, x, y) per clip from work/splitx.json (tools/splitx.py), matched across every same-camera cut (the head keeps its size and place)
    if SX:
        sk = sorted(float(k) for k in SX)
        for c in face_clips:
            if any(f["t0"] - 0.01 <= c["s"] and c["e"] <= f["t1"] + 0.01 for f in plan["face"]): continue
            k = max((x for x in sk if x <= c["s"] + 0.006), default=None)
            if k is None: continue
            sc, px, py = SX[f"{k:.4f}"]
            m = dict(scale=sc, pos=(round(px / 1080, 6), round(py / 1920, 6)), crop=dict(L=0, R=0, T=0, B=0))
            jobs.append((f"split {c['s']:.3f} (static {sc}%)", A.motion_js(fi, c["s"], m)))
    # R9: the OBS screen (V1) shows ONLY while a graphic needs it (plan["screen_on"], default the hl-title page 28.68-37.1); everywhere else it is disabled, so a card entrance reveals a dark stage, never their page
    SO = plan.get("screen_on", [[28.6833, 37.1]])
    for c in scr:
        if any(f["t0"] - 0.01 <= c["s"] and c["e"] <= f["t1"] + 0.01 for f in plan["face"]): continue
        if any(c["s"] >= lo - 0.01 and c["e"] <= hi + 0.01 for lo, hi in SO): continue
        if any(c["s"] < hi - 0.01 and c["e"] > lo + 0.01 for lo, hi in SO): probs.append((f"screen {c['s']:.3f}", "V1 clip straddles the screen window: razor first"))
        jobs.append((f"screen off {c['s']:.3f} (stage covers)", f"var x = at(s.videoTracks[{si}], {c['s']:.4f}); if (!x) return 'NOSCREEN {c['s']:.3f}'; x.disabled = true;"))
    # full-window views
    full = [v for v in plan["views"] if v.get("full")]
    saved = G.BOX; probs2 = []
    for k, (label, js) in enumerate(jobs):
        for v in full:
            if label.startswith("view ") and f" {v['view']}" in label:
                st = float(label.split()[1]); c = next((c for c in scr if abs(c["s"] - st) < 0.006), None)
                if not c or not (v["t0"] - 0.01 <= st < v["t1"] - 0.01): continue
                G.BOX = WIN
                try:
                    m = G.view_motion(G.named(plan, v["view"])); probs2 += A.leak_problems(label + " [window]", [(c["i"], m)])
                finally: G.BOX = saved
                jobs[k] = (label + " [window]", A.motion_js(si, c["s"], m) + f"var y = at(s.videoTracks[{fi}], {c['s']:.4f}); if (y) y.disabled = true;")
                probs = [(kk, x) for kk, x in probs if not x.startswith(label)]
    return jobs, probs + probs2


A.layout_jobs = layout_jobs_o
_lp0 = A.leak_problems


def _lp_view(label, keys, tol=0.5):
    nm = label.split()[-1] if label.startswith("view ") else None
    box = plan0["views_named"].get(nm, {}).get("box") if nm else None
    if not box: return _lp0(label, keys, tol)
    saved = G.BOX; G.BOX = tuple(box)
    try: return _lp0(label, keys, tol)
    finally: G.BOX = saved


A.leak_problems = _lp_view
_orig_verify = A.verify


def verify_o(plan, seq):
    pushed = [f for f in plan["face"] if f.get("push")]
    p2 = dict(plan, face=[f for f in plan["face"] if not f.get("push")])
    ok = _orig_verify(p2, seq); bad = []
    tl = A.readback(plan); fi, si = plan["face_track"], plan["screen_track"]
    V = lambda t: [x for x in tl["v"] if x[0] == t]
    for f in pushed:
        for c in seq["v"][fi]["clips"]:
            if c["s"] >= f["t0"] - 0.01 and c["e"] <= f["t1"] + 0.01:
                x = next((x for x in V(fi) if abs(x[2] - c["s"]) < 0.005), None)
                if not x or x[5] != "kf": bad.append(f"face {c['s']}: push not keyed ({x})")
                y = next((y for y in V(si) if abs(y[2] - c["s"]) < 0.005), None)
                if y and not y[4]: bad.append(f"screen under face {c['s']} still enabled")
    for v in plan["views"]:
        if v.get("full"):
            for c in seq["v"][fi]["clips"]:
                if c["s"] >= v["t0"] - 0.01 and c["e"] <= v["t1"] + 0.01:
                    x = next((x for x in V(fi) if abs(x[2] - c["s"]) < 0.005), None)
                    if x and not x[4]: bad.append(f"face under the full view {c['s']} still enabled")
    for b in bad: print("  x", b)
    print(f"verify (push + full view): {len(bad)} problem(s)")
    return ok and not bad


A.verify = verify_o
for f in plan0["face"]:
    if isinstance(f.get("face_x"), list) and not f.get("fx"): pass
# the effective face scale: written into a sibling plan so apply.py reads the SAME numbers (applyx.py's rule)
for f in plan0["face"]:
    if isinstance(f.get("face_x"), list): f["scale"] = mgx6.face_motion(f.get("scale", 150), f["face_x"])["scale"]
eff = os.path.join(os.path.dirname(os.path.abspath(sys.argv[1])), "plan.eff.json")
json.dump(plan0, open(eff, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
sys.argv = [os.path.join(TOOLS, "apply.py"), eff] + sys.argv[2:]
src = open(os.path.join(TOOLS, "apply.py"), encoding="utf-8").read(); main = src[src.index('if __name__ == "__main__":'):]
A.__dict__["__name__"] = "__main__"
exec(compile(main, os.path.join(TOOLS, "apply.py"), "exec"), A.__dict__)
