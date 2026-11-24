"""stagecheck.py <mov dir | plan.json>: per stage MG: longest static run (s), longest blank run (s), content bbox (alpha>40) over the clip, fill % of panel y200-1038"""
import subprocess, sys, glob, os, numpy as np
d = sys.argv[1]; skip = ("play", "ig-card"); MAXB = float(os.environ.get("MAX_BLANK", "0.5"))
if d.endswith(".json"):                      # kit: <plan.json> -> only the graphics the plan uses (not every superseded variant in overlays/mg)
    import json; P = json.load(open(d, encoding="utf-8")); mgd = os.path.join(P.get("_dir") or os.path.dirname(os.path.abspath(d)), "overlays", "mg")
    files = [os.path.join(mgd, g["id"] + ".mov") for g in P["graphics"] if g["kind"] != "play_card" and os.path.exists(os.path.join(mgd, g["id"] + ".mov"))]
else: files = sorted(glob.glob(os.path.join(d, "*.mov")))
worst = 0.0
for f in files:
    n = os.path.basename(f)[:-4]
    if n.startswith(skip) or n in ("hook-tag",) or n.startswith("captions"): continue
    w, h = 270, 480
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", f, "-vf", f"fps=4,scale={w}:{h}", "-pix_fmt", "rgba", "-f", "rawvideo", "-"], capture_output=True).stdout
    a = np.frombuffer(raw, np.uint8).reshape(-1, h, w, 4); al = a[..., 3].astype(float)
    rgb = a[..., :3].astype(float)
    st = bl = ms = mb = 0; cur_s = cur_b = 0; bb = [w, h, 0, 0]
    for i in range(len(a)):
        m = al[i] > 40
        if m.sum() < 30: cur_b += 1
        else:
            cur_b = 0; ys, xs = np.where(m); bb = [min(bb[0], xs.min()), min(bb[1], ys.min()), max(bb[2], xs.max()), max(bb[3], ys.max())]
        mb = max(mb, cur_b)
        if i and np.abs(a[i] - a[i-1]).mean() < 0.15: cur_s += 1
        else: cur_s = 0
        ms = max(ms, cur_s)
    worst = max(worst, mb / 4)
    print(f"{n:14s} {len(a)/4:5.1f}s static<={ms/4+0.25:.2f}s blank<={mb/4:.2f}s bbox x{bb[0]*4}-{bb[2]*4} y{bb[1]*4}-{bb[3]*4}")
print(f"stagecheck: longest blank run {worst:.2f} s (limit {MAXB})"); sys.exit(0 if worst <= MAXB else 1)
