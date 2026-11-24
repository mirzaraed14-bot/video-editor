"""sfxassign3.py <job dir> [--fam work/sfx-fam.json]: REACTIONS-V3 A5 assignment. For every graphic-entrance cue event in plan.json (the cue's event time = t + min(offset, 0.18)), pick the v3x-* sound whose
loudest K-weighted 50 ms window clears the carved bed (audio/bed-v3.wav) by >= MARGIN dB at a sample peak between -20 and -16.5 dBFS (typical -18, never above -16; A5 wants 10-14.5 dB under his -6 peaks and
>= 4 dB over the bed), with: no sound family over 20 % of the cues, no sound used more than twice, never the same sound twice in a row. Writes work/sfx-assign.json {graphic id: [name, peak]} which build_plan.py
reads, and (--apply) rewrites the cues in plan.json (t, name, static Level = peak + 1 because the files are normalised to -1 dBFS).  Run with the whisperx venv python."""
import json, os, random, subprocess, sys
import numpy as np
from scipy.signal import lfilter
job = sys.argv[1]; SR = 48000; MARGIN = float(os.environ.get("MARGIN", "5.0"))
plan = json.load(open(os.path.join(job, "plan.json"), encoding="utf-8")); SL = json.load(open(os.path.join(job, "sfx", "slices.json")))
FAM = json.load(open(sys.argv[sys.argv.index("--fam") + 1])) if "--fam" in sys.argv else None
if FAM is None:
    FAM = {"card-slide": "slide", "slide-02": "slide", "slide-03": "slide", "slide-tbl": "slide", "page-1": "paper", "page-2": "paper", "env-slide": "paper", "fold": "paper", "air": "swish", "swish-classic": "swish",
           "swish-office": "swish", "swish-flange": "swish", "pop-lid": "pop", "pop-squeeze": "pop", "pop-finger": "pop", "pop-out": "pop", "card-turn": "flick", "lift": "flick", "flap": "flick", "cloth-soft": "cloth", "cloth-fast": "cloth", "glass-info": "glass", "glass-calm": "glass", "ticks-1": "tick", "ticks-2": "tick", "ping": "ping"}
FAM = {"v3x-" + k: v for k, v in FAM.items()}
FIXED = {}          # counters keep their tick (a gentle tick only on a counting number)
ALLOWED = {"hook-tag-r2": "slide flick cloth", "ring-title": "pop ping glass", "hl-title-r2": "swish cloth", "hl-panel-a-r2": "swish flick cloth", "stat-600m": "tick pop glass", "cred-chips": "pop glass", "channel-page": "paper slide cloth glass", "hl-panel-b-r2": "swish cloth",
           "hl-panel-c-r2": "pop swish glass", "hl-short-r2": "swish cloth", "ptr-cut-r2": "pop ping glass", "strip-full-r2": "paper slide cloth glass", "play-theirs": "slide", "pair-len": "slide flick ping cloth glass", "bar-short": "swish slide flick cloth",
           "anatomy-r2": "paper slide cloth glass", "score-r3": "slide", "play-yt1": "slide", "twin-same": "flick", "play-yt2": "slide flick cloth", "twin-looks-r2": "swish flick cloth", "badge": "slide paper cloth", "fan-covers": "flick slide cloth",
           "letter-r4": "paper ping glass"}      # which sound families fit which motion (a tick only on a counting number; paper only where a page moves; pops for object pops; slides for cards; swishes for sweeps)
def rd(p): return np.frombuffer(subprocess.run(["ffmpeg", "-v", "error", "-i", p, "-ac", "2", "-ar", str(SR), "-f", "f32le", "-"], capture_output=True).stdout, np.float32).astype(np.float64).reshape(-1, 2)
def kw(x):
    b1, a1 = [1.53512485958697, -2.69169618940638, 1.19839281085285], [1.0, -1.69065929318241, 0.73248077421585]
    b2, a2 = [1.0, -2.0, 1.0], [1.0, -1.99004745483398, 0.99007225036621]
    return lfilter(b2, a2, lfilter(b1, a1, x, axis=0), axis=0)
B = rd(os.path.join(job, plan["music"]["file"])); KB = kw(B); names = sorted(FAM); Y = {n: rd(os.path.join(job, "sfx", n + ".wav")) for n in names}; KY = {n: kw(Y[n]) for n in names}
h = int(0.05 * SR)
def margin(start, n, peak):
    ky = KY[n] * 10 ** ((peak + 1.0) / 20); a = int(round(start * SR)); kb = KB[a:a + len(ky)]; best = -99.0
    for k in range(0, max(1, min(len(ky), len(kb)) - h), h // 2):
        pc = (ky[k:k + h] ** 2).sum(1).mean(); pb = (kb[k:k + h] ** 2).sum(1).mean()
        if pc > 0: best = max(best, 10 * np.log10(pc + 1e-15) - 10 * np.log10(pb + 1e-15))
    return best
ev = []
for g in plan["graphics"]:
    gid = g["id"].replace("-v3", "")
    for c in g["cues"]:
        if str(c[1]).startswith("v3x-"): ev.append((gid, round(c[0] + min(SL[c[1]]["offset"], 0.18), 3)))
ev.sort(key=lambda x: x[1]); N = len(ev); cap = int(0.2 * N + 1e-9)
def options(gid, t):
    out = []
    for n in names:
        if gid in FIXED and n not in FIXED[gid]: continue
        if gid in ALLOWED and FAM[n] not in ALLOWED[gid].split(): continue
        st = max(0.0, t - min(SL[n]["offset"], 0.18)); done = None
        for pk in (-19, -18, -17, -16.5, -16):
            if margin(st, n, pk) >= MARGIN: done = pk; break
        if done is not None: out.append((n, done, st))
    return out
opts = [options(g, t) for g, t in ev]
print("events", N, "family cap", cap)
for (g_, t_), o_ in zip(ev, opts): print(f"  {t_:7.2f} {g_:15s}", " ".join(f"{n[4:]}@{pk:g}" for n, pk, st in o_))
best = None
for seed in range(400):
    rng = random.Random(seed); order = sorted(range(N), key=lambda i: (len(opts[i]), rng.random())); pick = {}; fam = {}; use = {}
    ok = True
    for i in order:
        cand = [o for o in opts[i] if fam.get(FAM[o[0]], 0) < cap and use.get(o[0], 0) < 3]
        cand = [o for o in cand if all(pick.get(j, (None,))[0] != o[0] for j in (i - 1, i + 1))]
        if not cand: ok = False; break
        cand.sort(key=lambda o: (abs(o[1] + 18.0) > 1.2, rng.random()))
        o = cand[0]; pick[i] = o; fam[FAM[o[0]]] = fam.get(FAM[o[0]], 0) + 1; use[o[0]] = use.get(o[0], 0) + 1
    if ok:
        score = sum(abs(o[1] + 18.0) for o in pick.values())
        if best is None or score < best[0]: best = (score, dict(pick))
if best is None: raise SystemExit("no feasible assignment: raise the bed gap or relax MARGIN")
pick = best[1]; assign = {}
for i, (gid, t) in enumerate(ev):
    n, pk, st = pick[i]; assign[gid] = [n, pk]; print(f"  {t:8.2f} {gid:16s} {n:18s} peak {pk:5.1f}  margin {margin(st, n, pk):+5.1f}")
print("families:", {f: sum(1 for v in assign.values() if FAM[v[0]] == f) for f in sorted(set(FAM.values()))})
json.dump(assign, open(os.path.join(job, "work", "sfx-assign.json"), "w"), indent=1)
if "--apply" in sys.argv:
    for g in plan["graphics"]:
        gid = g["id"].replace("-v3", "")
        if gid in assign:
            t = next(t for q, t in ev if q == gid); n, pk = assign[gid]; g["cues"] = [[round(max(0.0, t - min(SL[n]["offset"], 0.18)), 3), n, round(pk + 1.0, 1)]] + [c for c in g["cues"] if not str(c[1]).startswith("v3x-")]
    json.dump(plan, open(os.path.join(job, "plan.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False); print("applied to plan.json")
