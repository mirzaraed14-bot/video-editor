"""audio3.py <job dir> [--write] [--obs <cleaned mp4>] : REACTIONS-V3 AUDIO RECIPE (stems), run with the whisperx venv python (numpy + scipy).
1. VOICE  per-clip Amplify (audio7's rule: his loud words at -6 dBFS into the -6 dBFS Hard Limiter, gains within +-6 dB of the median), measured on the CLEANED voice file;
         the OBS audio under a play is muted (-96).
2. PLAYS  one baked stem per play (sfx/play-v3-<id>.wav): gain to (his talk LUFS - 2.0 LU), peaks limited to <= -6.2 dBFS, 4 ms edge fades; placed at static 0 dB.
3. BED    ONE pre-rendered stem (audio/bed-v3.wav): carved (HPF 110 Hz 4th order, -4 dB bell 3.5 kHz Q 1), ridden offline so each 3 s talk window sits GAP (12) LU under his voice
         (flattened by passes, then shifted so the momentary (400 ms) P10 >= 8 LU and no 3 s window < 9), MUTED under every play (0.25 s fade out before, 0.4 s fade in after),
         2 s tail fade; placed at a static 0 dB, no keys.
Writes plan.json (clip_gains, music, sfx_gated) with --write, and work/audio3-report.txt.
Env: BED_SRC (bed wav), BED_IN (source in, s), CLAMP (talk gain clamp)."""
import json, os, subprocess, sys
import numpy as np
from scipy.signal import lfilter, butter, sosfilt

job = sys.argv[1]; WRITE = "--write" in sys.argv; SR = 48000; FPS = 60; GAP = 12.0


def a_(k, d=None): return sys.argv[sys.argv.index(k) + 1] if k in sys.argv else d


plan = json.load(open(os.path.join(job, "plan.json"), encoding="utf-8"))
C = json.load(open(os.path.join(job, "transcript", "cuts.json"), encoding="utf-8"))["segments"]
D = json.load(open(os.path.join(job, "transcript", "cuts.draft.json"), encoding="utf-8"))["segments"]
kind = lambda s: max(D, key=lambda d: min(d["end"], s["end"]) - max(d["start"], s["start"]))["kind"]
obs = a_("--obs") or json.load(open(os.path.join(job, "seq.json"), encoding="utf-8"))["obs"]


def rd(p, extra=None, ac=2):
    c = ["ffmpeg", "-v", "error", "-i", p] + (extra or []) + ["-vn", "-ac", str(ac), "-ar", str(SR), "-f", "f32le", "-"]
    return np.frombuffer(subprocess.run(c, capture_output=True).stdout, np.float32).astype(np.float64).reshape(-1, ac)


X = rd(obs, ["-t", "400"])


def kw(x):
    b1, a1 = [1.53512485958697, -2.69169618940638, 1.19839281085285], [1.0, -1.69065929318241, 0.73248077421585]
    b2, a2 = [1.0, -2.0, 1.0], [1.0, -1.99004745483398, 0.99007225036621]
    return lfilter(b2, a2, lfilter(b1, a1, x, axis=0), axis=0)


def loud(x):
    if len(x) == 0: return -99.0
    y = kw(x); return -0.691 + 10 * np.log10((y ** 2).mean(0).sum() + 1e-12)


db = lambda v: 20 * np.log10(max(float(v), 1e-9))


def limit(x, ceil_db=-6.0):
    p = subprocess.run(["ffmpeg", "-v", "error", "-f", "f32le", "-ar", str(SR), "-ac", "2", "-i", "-", "-af",
                        f"alimiter=limit={10 ** (ceil_db / 20):.6f}:attack=5:release=50:level=disabled", "-f", "f32le", "-"], input=x.astype(np.float32).tobytes(), capture_output=True)
    return np.frombuffer(p.stdout, np.float32).astype(np.float64).reshape(-1, 2)[:len(x)]


# ---- 1 voice ----
rows, pos = [], 0.0
for s in C:
    d = round(round((s["end"] - s["start"]) * FPS) / FPS, 6); a = int(round(s["start"] * SR)); n = int(round(d * SR)); y = X[a:a + n]
    pk = db(np.abs(y).max()) if len(y) else -99; h = int(0.05 * SR)
    wp = [db(np.abs(y[k:k + h]).max()) for k in range(0, max(1, len(y) - h), h)] if len(y) > h else [pk]
    sp = [v for v in wp if v > -40] or [pk]
    rows.append(dict(s=round(pos, 4), d=d, raw=s["start"], kind=kind(s), peak=pk, p85=float(np.percentile(sp, 85)), y=y)); pos += d
for r in rows:
    if r["kind"] != "A": r["y"] = np.zeros_like(r["y"])
END = pos; talk = [r for r in rows if r["kind"] == "A" and r["d"] >= 0.25]
NORM = lambda r: min(-6 - r["p85"], -6 - r["peak"] + 4) if r["kind"] == "A" else -6 - r["peak"]
med = float(np.median([NORM(r) for r in talk])); CL = float(os.environ.get("CLAMP", "6"))
for r in rows:
    g = NORM(r)
    if r["kind"] == "A": g = min(max(g, med - CL), med + CL)
    r["gain"] = round(g, 2)
V = np.zeros((int(round(END * SR)), 2))
for r in rows:
    a = int(round(r["s"] * SR)); y = r["y"] * 10 ** (r["gain"] / 20); y = y[:max(0, len(V) - a)]; V[a:a + len(y)] += y
V = limit(V); tm = np.zeros(len(V), bool)
for r in rows:
    if r["kind"] == "A" and r["d"] > 0: tm[int(round(r["s"] * SR)):int(round((r["s"] + r["d"]) * SR))] = True
talk_l = loud(V[tm]); n3 = int(3 * SR); h3 = int(1.5 * SR)

# ---- 2 plays ----
rep = []; spans = []
for p in plan["plays"]:
    d = round(p["t1"] - p["t0"], 4); y = rd(p["file"], ["-ss", f"{p['src_t0']:.4f}", "-t", f"{d:.4f}"])
    if len(y) < int(d * SR): y = np.concatenate([y, np.zeros((int(d * SR) - len(y), 2))])
    y = y[:int(round(d * SR))]; L = loud(y); g = talk_l - 2.0 - L
    y = y * 10 ** (g / 20)
    for _ in range(4):
        if db(np.abs(y).max()) <= -6.2: break
        y = limit(y, -6.3)
    n4 = int(0.004 * SR); y[:n4] *= np.linspace(0, 1, n4)[:, None]; y[-n4:] *= np.linspace(1, 0, n4)[:, None]
    if WRITE:
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "f32le", "-ar", str(SR), "-ac", "2", "-i", "-", "-c:a", "pcm_s24le", os.path.join(job, "sfx", f"play-v3-{p['id']}.wav")],
                       input=y.astype(np.float32).tobytes(), check=True)
    spans.append((p["t0"], p["t1"]))
    rep.append(f"play {p['id']} {p['t0']:.2f}-{p['t1']:.2f}: source {L:.1f} LUFS -> {loud(y):.1f} LUFS ({loud(y) - talk_l:+.1f} LU vs talk {talk_l:.1f}), peak {db(np.abs(y).max()):.1f} dBFS")

# ---- 3 bed ----
srcf = os.environ.get("BED_SRC") or os.path.join(job, "audio", "ES_Dirty Treasure - Amber Spill.wav"); si = float(os.environ.get("BED_IN", "0.064"))
mus = rd(srcf); bed = mus[int(si * SR): int(si * SR) + len(V)]
if len(bed) < len(V): raise SystemExit("bed shorter than the video")
sos = np.vstack([butter(2, 110, "hp", fs=SR, output="sos")] * 2)               # 4th order HPF 110 Hz
bed = sosfilt(sos, bed, axis=0)
f0, Q, G = 3500.0, 1.0, -4.0; A_ = 10 ** (G / 40); w0 = 2 * np.pi * f0 / SR; al = np.sin(w0) / (2 * Q)
bb = [1 + al * A_, -2 * np.cos(w0), 1 - al * A_]; aa = [1 + al / A_, -2 * np.cos(w0), 1 - al / A_]
bed = lfilter(bb, aa, bed, axis=0)                                             # RBJ peaking EQ, -4 dB @ 3.5 kHz, Q 1


def sers(x, win, hop):
    y = kw(x); p = (y ** 2).sum(1); c = np.concatenate([[0], np.cumsum(p)]); n = int(win * SR); h = int(hop * SR)
    idx = np.arange(0, max(1, len(p) - n), h); return idx / SR + win / 2, -0.691 + 10 * np.log10((c[idx + n] - c[idx]) / n + 1e-12)


tv, Lv = sers(V, 3.0, 0.5); _, Lb0 = sers(bed, 3.0, 0.5)
talkw = np.array([tm[max(0, int((t - 1.5) * SR)):int((t + 1.5) * SR)].mean() > 0.6 for t in tv])


def curve(c):
    k = 2; return np.convolve(np.pad(c, k, mode="edge"), np.ones(2 * k + 1) / (2 * k + 1), mode="same")[k:-k]


def realize(g_t):
    return 10 ** (np.interp(np.arange(len(V)) / SR, tv, g_t) / 20)


def duck(env):
    for a0, a1 in spans:
        i0, i1 = int(a0 * SR), int(a1 * SR); fo, fi = int(0.25 * SR), int(0.4 * SR)
        s0 = max(0, i0 - fo); env[s0:i0] *= np.linspace(1, 0, i0 - s0); env[i0:i1] = 0.0
        e1 = min(len(env), i1 + fi); env[i1:e1] *= np.linspace(0, 1, e1 - i1)
    nf = int(2.0 * SR); env[-nf:] *= np.linspace(1, 0, nf); n0 = int(0.02 * SR); env[:n0] *= np.linspace(0, 1, n0); return env


def measure(B):
    rows_ = []
    for k in range(0, len(V) - n3, h3):
        if tm[k:k + n3].mean() > 0.6: rows_.append(loud(V[k:k + n3]) - loud(B[k:k + n3]))
    mt = []; n4 = int(0.4 * SR)
    for k in range(0, len(V) - n4, int(0.2 * SR)):
        if tm[k:k + n4].mean() > 0.9:
            lv_ = loud(V[k:k + n4])
            if lv_ > -40: mt.append(lv_ - loud(B[k:k + n4]))
    return np.array(rows_), np.array(mt)


BL = float(os.environ.get('BED_LIM', '0'))


def mk(g_t):
    B_ = bed * realize(g_t)[:, None]
    return limit(B_, BL) if BL else B_      # V3 A6: the bed STEM is peak-limited so a bed transient on a limited -6 dBFS voice peak cannot push the mix over -5 dBFS


gdb = np.full(len(tv), float(np.median((Lv - GAP - Lb0)[talkw])))
for it in range(14):
    B = mk(gdb)
    _, Lb = sers(B, 3.0, 0.5); err = np.where(talkw, GAP - (Lv - Lb), np.nan); ok = ~np.isnan(err)
    e2 = np.interp(np.arange(len(tv)), np.arange(len(tv))[ok], err[ok]); gdb = gdb - 0.85 * curve(e2)
    gdb = np.clip(gdb, np.median(gdb) - 20, np.median(gdb) + 20)
    if os.environ.get('DBG'): print(it, 'gdb', np.round([gdb.min(), np.median(gdb), gdb.max()], 1), 'err', np.round([np.nanmin(err), np.nanmedian(err), np.nanmax(err)], 1))
for it in range(10):
    B = mk(gdb); gp, mt = measure(B)
    need = max(0.0, 9.3 - gp.min(), 8.3 - np.percentile(mt, 10), 11.7 - np.median(gp))
    if need < 0.05: break
    gdb = gdb - need
B = mk(gdb) * duck(np.ones(len(V)))[:, None]
B = B * 10 ** (float(os.environ.get('BED_TRIM', '0')) / 20)   # 2026-11-13 additive: Affan lowered every batch-7 bed by 6-9 dB by hand (clip gain); batch 9 bakes BED_TRIM=-7 (default 0 = unchanged)
gp, mt = measure(B)
print('pre-duck worst windows:', sorted(zip(np.round(gp,1), range(len(gp))))[:5])
_bt = float(os.environ.get("BED_TRIM", "0"))
rep.insert(0, f"BED stem: carved (HPF 110 4th order, -4 dB @3.5k Q1), ridden: 3 s talk windows {len(gp)}: median {np.median(gp):.1f} (want {GAP - _bt:.0f}) min {gp.min():.1f} (>= {9 - _bt:.0f}) P10 {np.percentile(gp, 10):.1f} "
              f"max {gp.max():.1f} (<= 18); momentary P10 {np.percentile(mt, 10):.1f} (>= 8), median {np.median(mt):.1f}; ride {gdb.min():.1f}..{gdb.max():.1f} dB; bed peak {db(np.abs(B).max()):.1f} dBFS")
rep.insert(0, f"VOICE {len(rows)} clips, talk gains median {med:+.1f} dB; talk {talk_l:.1f} LUFS; length {END:.3f} s")
print("\n".join(rep))
open(os.path.join(job, "work", "audio3-report.txt"), "w", encoding="utf-8").write("\n".join(rep) + "\n")
if WRITE:
    os.makedirs(os.path.join(job, "audio"), exist_ok=True)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "f32le", "-ar", str(SR), "-ac", "2", "-i", "-", "-c:a", "pcm_s24le", os.path.join(job, "audio", "bed-v3.wav")], input=B.astype(np.float32).tobytes(), check=True)
    plan["clip_gains"] = [[r["s"], (r["gain"] if r["kind"] == "A" else -96.0), r["kind"]] for r in rows]; plan["voice_gain"] = int(round(med)); plan["voice_gain_ranges"] = []
    plan["music"] = dict(file="audio/bed-v3.wav", source_in=0.0, bed_db=0.0, gaps=[], ride=[], why="V3 stem: carved, ridden offline, muted under plays; static 0 dB, no keys"); plan["sfx_gated"] = True
    json.dump(plan, open(os.path.join(job, "plan.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False); print("written plan.json")
