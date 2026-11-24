"""claudecheck.py <job>/plan.json: EVERY sequence frame (30 fps) where his screen recording (V1) can show, checked for the Claude app.
The Claude desktop app must never show. Its left strip (sidebar + chat, the left 23 % of the OBS frame below the tab bar) is compared
with a reference (claude-ref.npy, DB OBS 25.45 s): the app scores a mean abs difference < 3, YouTube / a channel page / Films & TV /
the OBS window >= 15 (both batch-6 OBS files, 2026-11-02). Each sequence frame outside a face-only beat is mapped to its OBS frame
through work/seqmap.json; flagged runs print with what covers them (a stage / play card hides V1, a showcase does not). Exit 1 if exposed.
2026-11-02: a 1-frame Claude flash at 2.77 s slipped past a 1.5 s proof sheet (and TCO v1 shipped 7- and 12-frame flashes)."""
import json, os, subprocess, sys
import numpy as np
path = sys.argv[1]; plan = json.load(open(path, encoding="utf-8")); job = os.path.dirname(os.path.abspath(path))
import math
SM = json.load(open(os.path.join(job, "work", "seqmap.json"), encoding="utf-8"))
W, H, FPS = 128, 72, 30
raw = subprocess.run(["ffmpeg", "-v", "error", "-i", plan["obs_file"], "-vf", f"fps={FPS},scale={W}:{H}", "-pix_fmt", "gray", "-f", "rawvideo", "-"],
                     capture_output=True).stdout
fr = np.frombuffer(raw, np.uint8).reshape(-1, H, W).astype(np.float32)
REF = np.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), "claude-ref.npy"))   # the app's left strip, DB OBS 25.45 s
lum = np.abs(fr[:, 8:65, 0:30] - REF).mean(axis=(1, 2))   # mean abs difference of the left 23 % (below the tab bar) from it
LO, HI = -1.0, float(os.environ.get("CLAUDE_MAD", "8"))


def s2r(t):
    for a, b, p in SM["map"]:
        if p - 1e-6 <= t < p + (b - a): return a + (t - p)
    return None


face = [(f["t0"], f["t1"]) for f in plan["face"]]
cover = [(g["t0"] + g.get("fade_in", 0.3), g["t1"] - 0.24, g["id"]) for g in plan["graphics"]   # opaque only between its fades
         if g.get("stage") or g["kind"] in ("ba_wipe", "ba_pair")]
bad = []
n = int(plan["end"] * FPS)
for k in range(n):
    t = (k + 0.5) / FPS
    if any(a <= t < b for a, b in face): continue
    r = s2r(t)
    if r is None: continue
    i = min(len(lum) - 1, int(r * FPS))
    if LO < lum[i] < HI:
        v = next((v for v in plan["views"] if v["t0"] <= t < v["t1"]), None)               # job-local: the app is on the OBS frame (x < 1215) but every
        nv = plan["views_named"][v["view"]] if v else None                                  # non-full view crops it away: exposed only if the crop reaches it
        if v and not v.get("full"):
            sc = 0.71 * nv["z"]; xmin = max(nv["cx"] - 540 / sc, nv.get("crop_left_src", 0))
            if xmin >= 1225: continue
        bad.append((k, t, r, float(lum[i])))
runs = []
for k, t, r, l in bad:
    if runs and k == runs[-1][-1][0] + 1: runs[-1].append((k, t, r, l))
    else: runs.append([(k, t, r, l)])
print(f"{n} sequence frames, {sum(1 for k in range(n) if not any(a <= (k + .5) / FPS < b for a, b in face))} with V1 visible, Claude = left-strip MAD < {HI} from the reference; OBS MAD histogram [0-3, 3-8, 8-15, 15-30, 30+] {np.histogram(lum, bins=[0, 3, 8, 15, 30, 256])[0].tolist()}")
exposed = 0
for run in runs:
    t0, t1 = run[0][1] - 0.5 / FPS, run[-1][1] + 0.5 / FPS
    cov = [c[2] for c in cover if c[0] <= t0 + 1e-3 and t1 <= c[1] + 1e-3]
    if not cov: exposed += len(run)
    print(f"  {'covered' if cov else 'EXPOSED'} seq {t0:7.3f}-{t1:7.3f} ({len(run)} frames) OBS {run[0][2]:.2f}-{run[-1][2]:.2f} MAD {min(x[3] for x in run):.1f}"
          + (f" under {cov}" if cov else ""))
print(f"EXPOSED Claude-app frames: {exposed}")
sys.exit(1 if exposed else 0)
