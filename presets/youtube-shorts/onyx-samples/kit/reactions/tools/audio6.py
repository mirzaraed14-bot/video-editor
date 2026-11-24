"""audio6.py <job> [--write]: the v2 mix of a reaction (Affan 2026-11-02: "the audio should be at minus six decibels constant ... normalize
all peaks, and the music ... eight decibels lower than the speaker volume. I can't even hear the music"; "the sound effects are just not
there at all"), MEASURED offline on the sequence timeline before anything is placed. Run with the whisperx venv python (scipy).

1. VOICE: every A1 clip (= every segment of transcript/cuts.json, his talk AND the inserts) is peak-normalised: his talk so the
   clip's loud words (85th percentile of its 50 ms peaks) sit AT -6 dBFS, its loudest syllable at most 4 dB into the limiter; an insert
   by its sample peak; talk gains are held within +-4 dB of the talk median (a breath-only sliver is not pushed 20 dB), the inserts
   (their Short, our samples) are normalised the same way but never left > 2 LU louder than his talk (our masters sit at -12 LUFS).
   The chain into Premiere's -6 dBFS Hard Limiter is simulated (alimiter) and reported: talk LUFS, % of words peaking at -6.
2. MUSIC: the bed (plan music file, from its entrance) runs the WHOLE video, flat, a 2 s tail fade; its level puts its short-term loudness
   8 LU under his talk's (median over 3 s windows of talk); the gap per window is reported (min / median / max).
3. SFX: every plan cue gets a clip level: its loudest momentary loudness at (local voice short-term - 11 LU) for swishes / whooshes and
   the short transients (pop, tick, hit, page, card, shutter) alike, never quieter than the bed there + 2 LU (audible on a phone,
   above the music), its peak capped 5 dB (transients) / 6 dB (swishes) under the voice's -6 dBFS peaks. Written into plan.json cues as [t, name, dB].
4. A full offline mixdown (work/mix.wav, 48 kHz) and its stats -> work/audio.json + work/audio-report.txt.
"""
import json, os, subprocess, sys
import numpy as np
from scipy.signal import lfilter

job = sys.argv[1]; WRITE = "--write" in sys.argv
SR = 48000; FPS = 60
plan = json.load(open(os.path.join(job, "plan.json"), encoding="utf-8"))
C = json.load(open(os.path.join(job, "transcript", "cuts.json"), encoding="utf-8"))["segments"]
D = json.load(open(os.path.join(job, "transcript", "cuts.draft.json"), encoding="utf-8"))["segments"]
kind = lambda s: max(D, key=lambda d: min(d["end"], s["end"]) - max(d["start"], s["start"]))["kind"]
raw = os.path.join(job, "raw", C[0]["clip"])
def rd(p, extra=None, ac=2):
    c = ["ffmpeg", "-v", "error", "-i", p] + (extra or []) + ["-ac", str(ac), "-ar", str(SR), "-f", "f32le", "-"]
    return np.frombuffer(subprocess.run(c, capture_output=True).stdout, np.float32).astype(np.float64).reshape(-1, ac)
X = rd(raw)


# ---- BS.1770 K-weighting (48 kHz) ----
def kw(x):
    b1, a1 = [1.53512485958697, -2.69169618940638, 1.19839281085285], [1.0, -1.69065929318241, 0.73248077421585]
    b2, a2 = [1.0, -2.0, 1.0], [1.0, -1.99004745483398, 0.99007225036621]
    return lfilter(b2, a2, lfilter(b1, a1, x, axis=0), axis=0)
def loud(x):      # LUFS of a block (stereo: channel powers summed)
    if len(x) == 0: return -99.0
    y = kw(x); return -0.691 + 10 * np.log10((y ** 2).mean(0).sum() + 1e-12)
def series(x, win, hop=0.1):
    y = kw(x); p = (y ** 2).sum(1); c = np.concatenate([[0], np.cumsum(p)]); n = int(win * SR); h = int(hop * SR)
    idx = np.arange(0, max(1, len(p) - n), h); return idx / SR + win / 2, -0.691 + 10 * np.log10((c[idx + n] - c[idx]) / n + 1e-12)
db = lambda v: 20 * np.log10(max(v, 1e-9))

# ---- 1. voice ----
rows, pos = [], 0.0
for s in C:
    d = round(round((s["end"] - s["start"]) * FPS) / FPS, 6); a = int(round(s["start"] * SR)); n = int(round(d * SR))
    y = X[a:a + n]; pk = db(np.abs(y).max()) if len(y) else -99
    h = int(0.05 * SR); wp = [db(np.abs(y[k:k + h]).max()) for k in range(0, max(1, len(y) - h), h)] if len(y) > h else [pk]
    sp = [v for v in wp if v > -40] or [pk]; p85 = float(np.percentile(sp, 85))
    rows.append(dict(s=round(pos, 4), d=d, raw=s["start"], kind=kind(s), peak=round(pk, 2), p85=round(p85, 2), y=y)); pos += d
END = pos
talk = [r for r in rows if r["kind"] == "A" and r["d"] >= 0.25]
NORM = lambda r: min(-6 - r["p85"], -6 - r["peak"] + 4) if r["kind"] == "A" else -6 - r["peak"]   # talk: its loud words AT -6, the loudest <= 4 dB into the limiter
med = float(np.median([NORM(r) for r in talk]))
CLAMP = float(os.environ.get("CLAMP", "6"))      # talk gains held within +-CLAMP dB of the talk median (4 -> 6 on 2026-11-02: 22 of 88 DB clips sat on the +-4 rails)
for r in rows:
    g = NORM(r); r["want"] = round(g, 2)
    if r["kind"] == "A": g = min(max(g, med - CLAMP), med + CLAMP)
    r["gain"] = round(g, 2)
if os.environ.get("RAILS"):
    for r in rows:
        if r["kind"] == "A" and abs(r["gain"] - r["want"]) > 0.01:
            print(f"  rail {r['s']:7.2f} +{r['d']:.2f}s peak {r['peak']:6.1f} p85 {r['p85']:6.1f} want {r['want']:+6.2f} got {r['gain']:+6.2f} -> loud words peak at {r['p85'] + r['gain']:6.1f} dBFS")
def build(gains=True):
    out = np.zeros((int(round(END * SR)) + SR, 2))
    for r in rows:
        a = int(round(r["s"] * SR)); y = r["y"] * (10 ** (r["gain"] / 20) if gains else 1.0); out[a:a + len(y)] += y
    return out[:int(round(END * SR))]
def limit(x, ceil_db=-6.0):
    p = subprocess.run(["ffmpeg", "-v", "error", "-f", "f32le", "-ar", str(SR), "-ac", "2", "-i", "-", "-af", f"alimiter=limit={10 ** (ceil_db / 20):.6f}:attack=5:release=50:level=disabled",
                        "-f", "f32le", "-"], input=x.astype(np.float32).tobytes(), capture_output=True)
    return np.frombuffer(p.stdout, np.float32).astype(np.float64).reshape(-1, 2)[:len(x)]
V = limit(build())
talk_mask = np.zeros(len(V), bool); ins_mask = np.zeros(len(V), bool)
for r in rows:
    a, b = int(round(r["s"] * SR)), int(round((r["s"] + r["d"]) * SR))
    (talk_mask if r["kind"] == "A" else ins_mask)[a:b] = True
talk_lufs = loud(V[talk_mask]); ins_groups = {}
for r in rows:                                    # each insert range: its loudness after normalisation, held <= talk + 2 LU
    if r["kind"] != "A": ins_groups.setdefault(round(r["raw"] - r["s"], 1), []).append(r)
for k, grp in ins_groups.items():
    yy = np.concatenate([g["y"] * 10 ** (g["gain"] / 20) for g in grp]); L = loud(yy)
    if L > talk_lufs + 2:
        for g in grp: g["gain"] = round(g["gain"] - (L - talk_lufs - 2), 2)
V = limit(build()); talk_lufs = loud(V[talk_mask])
wins = []
for r in rows:
    if r["kind"] != "A": continue
    a = int(round(r["s"] * SR)); y = V[a:a + int(r["d"] * SR)]
    for k in range(0, max(1, len(y) - int(0.4 * SR)), int(0.4 * SR)): wins.append(db(np.abs(y[k:k + int(0.4 * SR)]).max()))
wins = np.array(wins); at6 = float((wins >= -7.0).mean() * 100)

# ---- 2. music ----
M = plan["music"]; mus = rd(os.path.join(job, M["file"]))
si = M.get("source_in", 0.0); bed = mus[int(si * SR): int(si * SR) + len(V)]
if len(bed) < len(V): raise SystemExit(f"the bed is {len(bed) / SR:.1f} s from its entrance, the video {END:.1f} s: pick a longer track or loop it")
tv, Lv = series(V * talk_mask[:, None], 3.0); tb, Lb = series(bed, 3.0)
tk = np.array([talk_mask[max(0, int((t - 1.5) * SR)):int((t + 1.5) * SR)].mean() > 0.6 for t in tv])
talk_st = float(np.median(Lv[tk])); bed_st = float(np.median(Lb[:len(Lv)][tk]))
bed_db = round(talk_st - 8 - bed_st, 1)
gap = Lv[tk] - (Lb[:len(Lv)][tk] + bed_db)
fade = np.ones(len(bed)); nf = int(2.0 * SR); fade[-nf:] = np.linspace(1, 0, nf)
# the RIDE (2026-11-02 reviewer: one flat bed gain left the voice-minus-bed gap at 2-17 LU because the track has its own dynamics, and
# REACTIONS-V2 rule 2 wants it ~8 dB under the voice "consistent"): every 0.5 s, the gap of the 3 s window around it (voice = everything on
# A1: his talk AND their clip / our sample) minus 8, clamped +-RIDE dB, smoothed over ~3 s, keyed every 1 s; none in the 2 s tail fade
RIDE = float(os.environ.get("RIDE", "4"))
ride = []
if RIDE > 0:
    tr_, Lr = series(V, 3.0, 0.5); _, Lbr = series(bed, 3.0, 0.5); n_ = min(len(Lr), len(Lbr)); tr_, Lr, Lbr = tr_[:n_], Lr[:n_], Lbr[:n_] + bed_db
    ok = Lr > -40; corr = np.where(ok, np.clip(Lr - Lbr - 8.0, -RIDE, RIDE), np.nan)
    idx = np.arange(n_); good = ~np.isnan(corr)
    corr = np.interp(idx, idx[good], corr[good]) if good.any() else np.zeros(n_)
    k = int(os.environ.get("RIDE_K", "4")); corr = np.convolve(np.pad(corr, k, mode="edge"), np.ones(2 * k + 1) / (2 * k + 1), mode="same")[k:-k]
    for t in np.arange(1.0, END - 2.5, 1.0):
        ride.append([round(float(t), 2), round(float(np.interp(t, tr_, corr)), 1)])
    rt = np.arange(len(bed)) / SR
    gain = 10 ** (np.interp(rt, [0.0] + [a for a, _ in ride] + [END], [ride[0][1] if ride else 0.0] + [b for _, b in ride] + [ride[-1][1] if ride else 0.0]) / 20)
else:
    gain = np.ones(len(bed))
B = bed * 10 ** (bed_db / 20) * (fade * gain)[:, None]
_, Lb2 = series(B, 3.0); gap = Lv[tk] - Lb2[:len(Lv)][tk]          # the gap AFTER the ride (reported)

# ---- 3. SFX ----
SL = json.load(open(os.path.join(job, "sfx", "slices.json"), encoding="utf-8"))
TRANS = ("pop", "tick", "hit", "page", "card", "shutter")
AUD_MIN = float(os.environ.get("AUD_MIN", "6"))   # dB a cue's loudest 50 ms must clear the bed by (raised up to the peak caps)
cache = {}
S = np.zeros_like(V); report = []
tV, LV = series(V, 3.0, 0.05); tB, LB = series(B, 3.0, 0.05)
def at_series(ts, Ls, t): return float(Ls[min(len(Ls) - 1, max(0, int(round((t - ts[0]) / (ts[1] - ts[0])))))])
for g in plan["graphics"]:
    new = []
    for c in g.get("cues", []):
        t, name = c[0], c[1]
        if name not in cache: cache[name] = rd(os.path.join(job, "sfx", name + ".wav"))
        y = cache[name]; m0 = max(series(y, 0.4, 0.02)[1]) if len(y) > 0.45 * SR else loud(y)
        ev = t + SL[name]["offset"]; vst = at_series(tV, LV, ev); bst = at_series(tB, LB, ev)
        a0, a1 = int((ev - 1.5) * SR), int((ev + 1.5) * SR); vpk = db(np.abs(V[max(0, a0):a1]).max())
        trans = any(k in name for k in TRANS)
        target = max(vst - 10, bst + 2)
        gdb = target - m0
        pk = db(np.abs(y).max())
        cap = -11 if trans else -12                  # 5 / 6 dB under his -6 dBFS peaks (v1 sat 15 dB under and read "not there at all")
        gdb = min(gdb, cap - pk, vpk - (5 if trans else 6) - pk)
        gdb = round(float(np.clip(gdb, -40, 6)), 1)
        a = int(round(t * SR))
        # audibility = the cue's loudest 50 ms window vs the (ridden) bed in that SAME window (K-weighted power; momentary LUFS understates transients)
        ky = kw(y); kb = kw(B[a:a + len(y)]); h = int(0.05 * SR); best = -99.0
        for k in range(0, max(1, min(len(ky), len(kb)) - h), h // 2):
            pc = (ky[k:k + h] ** 2).sum(1).mean(); pb = (kb[k:k + h] ** 2).sum(1).mean()
            if pc > 0: best = max(best, 10 * np.log10(pc + 1e-15) + gdb - 10 * np.log10(pb + 1e-15))
        if best < AUD_MIN:                           # loses to the bed: raise it, still >= 3 dB (transients) / 4 dB (swishes) under his -6 peaks
            up = min(AUD_MIN - best, (-8.5 if trans else -9.5) - (pk + gdb), vpk - (2.5 if trans else 3.5) - (pk + gdb))
            if up > 0: gdb = round(gdb + up, 1); best += up
        yy = y * 10 ** (gdb / 20); S[a:a + len(yy)] += yy[:max(0, len(S) - a)]
        mm = m0 + gdb
        report.append(f"{t:8.2f} {g['id'][:16]:16s} {name:14s} voiceST {vst:6.1f} bedST {bst:6.1f} cueM {mm:6.1f} (under voice {vst - mm:4.1f}, over bed {mm - bst:+4.1f}; 50ms over bed {best:+5.1f}) peak {pk + gdb:6.1f}  level {gdb:+.1f} dB")
        new.append([c[0], c[1], gdb])
    if WRITE: g["cues"] = new

# ---- 4. mixdown ----
MIX = V + B + S
sf = os.path.join(job, "work", "mix.wav")
subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "f32le", "-ar", str(SR), "-ac", "2", "-i", "-", "-c:a", "pcm_s16le", sf], input=MIX.astype(np.float32).tobytes(), check=True)
st = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", sf, "-af", "ebur128=peak=true", "-f", "null", "-"], capture_output=True, text=True).stderr
I = [l for l in st.splitlines() if l.strip().startswith("I:")][-1].split()[1]; TP = [l for l in st.splitlines() if "Peak:" in l][-1].split()[1]
lines = [f"VOICE: {len(rows)} A1 clips, talk gains median {med:+.1f} dB (clip range {min(r['gain'] for r in rows if r['kind'] == 'A'):+.1f}..{max(r['gain'] for r in rows if r['kind'] == 'A'):+.1f}),"
         f" inserts {sorted({r['gain'] for r in rows if r['kind'] != 'A'})[:3]}...; into the -6 dBFS limiter: talk {talk_lufs:.1f} LUFS, "
         f"{at6:.0f} % of 400 ms talk windows peak within 1 dB of -6 dBFS",
         f"MUSIC: {M['file']} from {si:.3f} s, bed_db {bed_db:+.1f} dB (talk ST median {talk_st:.1f} LUFS, bed {bed_st + bed_db:.1f}); voice-minus-bed per 3 s "
         f"window: min {gap.min():.1f} / P10 {np.percentile(gap, 10):.1f} / median {np.median(gap):.1f} / P90 {np.percentile(gap, 90):.1f} / max {gap.max():.1f} LU (bed ride +-{RIDE:g} dB, {len(ride)} keys); under the inserts too (continuous); "
         f"closest windows (centre s: LU) {', '.join(f'{t:.1f}: {g:.1f}' for t, g in sorted(zip(tv[tk], gap), key=lambda x: x[1])[:4])}",
         f"SFX: {len(report)} cues", *report,
         f"MIX: integrated {I} LUFS, true peak {TP} dBTP -> {sf}"]
open(os.path.join(job, "work", "audio-report.txt"), "w", encoding="utf-8").write("\n".join(lines) + "\n")
print("\n".join(lines[:3])); print(lines[-1])
out = dict(voice_gain=int(round(med)), ranges=[], clip_gains=[[r["s"], r["gain"], r["kind"]] for r in rows],
           talk_lufs=round(talk_lufs, 1), at6=round(at6, 1), music=dict(file=M["file"], source_in=si, bed_db=bed_db, gaps=[], ride=ride,
           why=f"bed {bed_st:.1f} LUFS ST at 0 dB; talk ST {talk_st:.1f}; bed set 8 LU under (window gap median {np.median(gap):.1f})"), mix_I=I, mix_TP=TP)
json.dump(out, open(os.path.join(job, "work", "audio.json"), "w", encoding="utf-8"), indent=1)
if WRITE:
    plan["clip_gains"] = out["clip_gains"]; plan["voice_gain"] = out["voice_gain"]; plan["voice_gain_ranges"] = []; plan["music"] = out["music"]; plan["sfx_gated"] = True
    json.dump(plan, open(os.path.join(job, "plan.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    print("written into plan.json")
