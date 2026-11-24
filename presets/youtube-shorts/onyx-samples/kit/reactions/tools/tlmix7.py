"""tlmix7.py <sequence name> <job dir> [--cached]: the TIMELINE MIX SIMULATOR (REACTIONS-V3 Q1).

Reads the PLACED sequence by name (tlread7.read_audio: DOM only, never activates, never writes), renders the mix offline with ffmpeg the way
Premiere plays it, writes <job>/work/tlmix.wav + work/tlmix-report.txt and measures the V3 audio gates A1-A6 on 3 s windows.
Run with the whisperx venv python (numpy + scipy):
  ~/.cache/video-editor/whisperx-venv/Scripts/python.exe tools7/tlmix7.py "<sequence>" <job dir> [--cached]
(--cached re-uses <job>/work/tl-read.json from the last readback instead of asking Premiere.)

VALUE -> dB (the ExtendScript property scales; proof in AUDIO-ROOT-CAUSE.md):
  Volume > Level (and Channel Volume L/R)  raw = 10 ** ((dB - 15) / 20)   (Adobe: slider -inf..+15 dB, raw 1.0 = +15 dB; 0 dB reads 0.17782794)
  Amplify Left/Right/Gain                  raw = (dB + 96) / 144           (Adobe: -96..+48 dB; 0 dB reads 0.66666667)
  Hard Limiter Maximum Amplitude           raw = 1 + dBFS / 100            (0.94 = -6 dBFS; lab-notes 1090).  Input Boost: assumed 0 dB (default raw 0.6667)
Per-clip chain (Premiere order): source slice -> Volume Level (static or keys) -> Channel Volume -> Amplify -> Hard Limiter (ffmpeg alimiter 5/50 ms)
-> track -> sum. Keys are in the clip's MEDIA time (key t - inPoint = time into the clip); between keys the level is interpolated linearly in dB.
Mono source clips: the Amplify 'Gain' slider is used as-is (the -3 dB centre pan law of a mono clip on a stereo master is NOT modelled).
Track faders (Audio Track Mixer) are not exposed to the DOM: reported as not readable, assumed 0 dB.
"""
import json, os, subprocess, sys, math
import numpy as np
from scipy.signal import lfilter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import tlread7

SEQ, JOB = sys.argv[1], sys.argv[2]
SR = 48000
db = lambda v: 20 * np.log10(max(float(v), 1e-9))
def lvl_db(raw): return 20 * math.log10(raw) + 15 if raw > 1e-9 else -96.0   # Volume>Level / Channel Volume raw -> dB
def amp_db(raw): return raw * 144.0 - 96.0                                  # Amplify raw -> dB
def hl_db(raw): return (raw - 1.0) * 100.0                                  # Hard Limiter ceiling raw -> dBFS

# ---- readback ----
cache_json = os.path.join(JOB, "work", "tl-read.json")
if "--cached" in sys.argv and os.path.exists(cache_json): TL = json.load(open(cache_json))
else:
    TL = tlread7.read_audio(SEQ); json.dump(TL, open(cache_json, "w"), indent=1)
END = TL["end"]; N = int(round(END * SR))

def P(c, comp, prop):
    for m in c["comps"]:
        if m["name"] == comp:
            for p in m["props"]:
                if p["n"] == prop: return p
    return None

# ---- DSP helpers ----
def kw(x):
    b1, a1 = [1.53512485958697, -2.69169618940638, 1.19839281085285], [1.0, -1.69065929318241, 0.73248077421585]
    b2, a2 = [1.0, -2.0, 1.0], [1.0, -1.99004745483398, 0.99007225036621]
    return lfilter(b2, a2, lfilter(b1, a1, x, axis=0), axis=0)
def loud(x):
    if len(x) == 0: return -99.0
    y = kw(x); return -0.691 + 10 * np.log10((y ** 2).mean(0).sum() + 1e-12)
def limit(x, ceil_db):
    p = subprocess.run(["ffmpeg", "-v", "error", "-f", "f32le", "-ar", str(SR), "-ac", "2", "-i", "-", "-af", f"alimiter=limit={10 ** (ceil_db / 20):.6f}:attack=5:release=50:level=disabled",
                        "-f", "f32le", "-"], input=x.astype(np.float32).tobytes(), capture_output=True)
    return np.frombuffer(p.stdout, np.float32).astype(np.float64).reshape(-1, 2)[:len(x)]
_src = {}
def source(path, t0, t1):
    d = _src.get(path)
    if d is None or t0 < d[0] or t1 > d[1]:
        a = 0.0 if d is None else min(d[0], t0); b = t1 if d is None else max(d[1], t1)
        if d is None and "raw" in path.replace("\\", "/").split("/"): b = max(b, 400.0)    # an OBS recording: read the first 400 s once
        a = max(0.0, a - 1.0); b = b + 1.0
        c = ["ffmpeg", "-v", "error", "-ss", f"{a:.4f}", "-t", f"{b - a:.4f}", "-i", path, "-vn", "-ac", "2", "-ar", str(SR), "-f", "f32le", "-"]
        y = np.frombuffer(subprocess.run(c, capture_output=True).stdout, np.float32).astype(np.float64).reshape(-1, 2)
        d = _src[path] = (a, b, y)
    a, b, y = d; i0 = int(round((t0 - a) * SR)); n = int(round((t1 - t0) * SR))
    o = y[i0:i0 + n]
    if len(o) < n: o = np.concatenate([o, np.zeros((n - len(o), 2))])
    return o

def clip_gain(c, n):
    """(per-sample dB curve of Volume>Level, [L dB, R dB] of Channel Volume + Amplify)."""
    lv = P(c, "Volume", "Level"); g = np.zeros(n)
    if lv and lv.get("tv") and lv.get("keys"):
        kt = np.array([k[0] - c["i"] for k in lv["keys"]]); kv = np.array([lvl_db(k[1]) for k in lv["keys"]])
        g += np.interp(np.arange(n) / SR, kt, kv)
    elif lv: g += lvl_db(lv["v"])
    cvd = [lvl_db(p["v"]) if p else 0.0 for p in (P(c, "Channel Volume", "Left"), P(c, "Channel Volume", "Right"))]
    am = P(c, "Amplify", "Left"), P(c, "Amplify", "Right"), P(c, "Amplify", "Gain")
    if am[0] and am[1]: amd = [amp_db(am[0]["v"]), amp_db(am[1]["v"])]
    elif am[2]: amd = [amp_db(am[2]["v"])] * 2
    else: amd = [0.0, 0.0]
    return g, [cvd[0] + amd[0], cvd[1] + amd[1]]

def render_track(T):
    res = []
    for c in T["clips"]:
        if c.get("disabled"): continue
        d = c["e"] - c["s"]; n = int(round(d * SR))
        y = source(c["path"], c["i"], c["i"] + d)[:n]
        g, lr = clip_gain(c, len(y))
        y = y * (10 ** (g[:, None] / 20)) * np.array([10 ** (lr[0] / 20), 10 ** (lr[1] / 20)])[None, :]
        hl = P(c, "Hard Limiter", "Maximum Amplitude")
        if hl: y = limit(y, hl_db(hl["v"]))
        res.append((c, y))
    return res

# ---- render + classify ----
tracks = TL["tracks"]
stems = {k: np.zeros((N, 2)) for k in ("voice", "plays", "bed", "sfx")}
cues = []; plays = []; talk_spans = []
def put(stem, c, y):
    a = int(round(c["s"] * SR)); m = max(0, min(len(y), N - a)); stems[stem][a:a + m] += y[:m]
for T in tracks:
    if T["muted"]: continue
    for c, y in render_track(T):
        nm = c["name"].lower()
        if nm.startswith("play-"): put("plays", c, y); plays.append((c, y))
        elif T["i"] == 0:
            put("voice", c, y)
            am = P(c, "Amplify", "Left")
            if not am or amp_db(am["v"]) > -60: talk_spans.append((c["s"], c["e"]))
        elif (c["e"] - c["s"]) > 0.6 * END: put("bed", c, y)
        else: put("sfx", c, y); cues.append((c, y))
MIX = stems["voice"] + stems["plays"] + stems["bed"] + stems["sfx"]
sf = os.path.join(JOB, "work", "tlmix.wav")
subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "f32le", "-ar", str(SR), "-ac", "2", "-i", "-", "-c:a", "pcm_s16le", sf], input=MIX.astype(np.float32).tobytes(), check=True)
talk_mask = np.zeros(N, bool)
for a, b in talk_spans: talk_mask[int(a * SR):int(b * SR)] = True

Lines = []
def out(s=""): Lines.append(s); print(s)
out(f"TLMIX7 '{SEQ}' | {JOB} | length {END:.3f} s | tracks " + ", ".join(f"{t['name']}{'(MUTED)' if t['muted'] else ''}[{len(t['clips'])}]" for t in tracks))
out("track faders (QE track component 'Track > Volume', 1.00 = unity): " + str([t.get('fader') for t in tracks]) + "; mute " + str([t['muted'] for t in tracks]))
for t in tracks:
    if t.get('fader') not in (None, '1.00'): out(f"   !! {t['name']} fader {t['fader']} is NOT unity and is not modelled")
n3 = int(3 * SR); h3 = int(1.5 * SR)
V, B = stems["voice"], stems["bed"]

# ---- A1 ----
w3 = [(k / SR, db(np.abs(V[k:k + n3]).max())) for k in range(0, N - n3, n3) if talk_mask[k:k + n3].mean() > 0.5]
a1 = 100 * np.mean([abs(p + 6) <= 1.0 for _, p in w3]) if w3 else 0; pk_all = [p for _, p in w3]
out(f"A1 voice peaks per 3 s talk window: {a1:.0f} % within 1 dB of -6 dBFS ({len(w3)} windows; need >= 90 %); min {min(pk_all):.1f} / median {np.median(pk_all):.1f} / max {max(pk_all):.1f} dBFS"
    + (f"; outside: {[(round(float(t), 1), round(float(p), 1)) for t, p in w3 if abs(p + 6) > 1.0][:14]}" if a1 < 100 else "") + f"   A1 {'PASS' if a1 >= 90 else 'FAIL'}")

# ---- A2 ----
rows = []
for k in range(0, N - n3, h3):
    if talk_mask[k:k + n3].mean() > 0.6:
        lv_, lb_ = loud(V[k:k + n3]), loud(B[k:k + n3]); rows.append((k / SR + 1.5, lv_, lb_, lv_ - lb_))
gap = np.array([r[3] for r in rows]) if rows else np.array([0.0])
med, mn, mx = float(np.median(gap)), float(gap.min()), float(gap.max())
A2W, A2N, A2X = float(os.environ.get('A2_WANT', '12')), float(os.environ.get('A2_MIN', '9')), float(os.environ.get('A2_MAX', '18'))   # 2026-11-13 additive (batch 9: 19/16/25); defaults unchanged
bad9 = [(round(float(r[0]), 1), round(float(r[3]), 1)) for r in rows if r[3] < A2N]; bad18 = [(round(float(r[0]), 1), round(float(r[3]), 1)) for r in rows if r[3] > A2X]
out(f"A2 bed LU under his voice, 3 s talk windows ({len(rows)}): median {med:.1f} (want {A2W:g}) / min {mn:.1f} (want >= {A2N:g}) / P10 {np.percentile(gap, 10):.1f} / P90 {np.percentile(gap, 90):.1f} / max {mx:.1f} (want <= {A2X:g})")
out(f"   windows closer than {A2N:g} LU: {len(bad9)} {bad9[:10]}; windows more than {A2X:g} LU under: {len(bad18)} {bad18[:6]}")
out(f"   his talk ST median {np.median([r[1] for r in rows]):.1f} LUFS, the bed under it {np.median([r[2] for r in rows]):.1f} LUFS; windows where the BED is louder than his voice: {sum(g < 0 for g in gap)}   A2 {'PASS' if abs(med - A2W) <= 1.5 and mn >= A2N and mx <= A2X else 'FAIL'}")

# momentary view (a 400 ms window, only where his voice is speaking): the 3 s view hides soft words
mt = []; n4 = int(0.4 * SR)
for k in range(0, N - n4, int(0.2 * SR)):
    if talk_mask[k:k + n4].mean() > 0.9:
        lv_ = loud(V[k:k + n4])
        if lv_ > -40: mt.append(lv_ - loud(B[k:k + n4]))
mt = np.array(mt)
out(f"   momentary (400 ms, speaking only, {len(mt)} windows) voice-minus-bed: P10 {np.percentile(mt, 10):.1f} / median {np.median(mt):.1f} / P90 {np.percentile(mt, 90):.1f} LU; windows < 3 LU: {100 * np.mean(mt < 3):.0f} %, < 0 LU (bed louder): {100 * np.mean(mt < 0):.0f} %")

# octave-band balance over his talk (the bed's bass is not 'under' his voice just because the 3 s LUFS says so)
from scipy.signal import welch
vm = V[talk_mask].mean(1); bm = B[talk_mask].mean(1)
f, pv = welch(vm, SR, nperseg=8192); _, pb = welch(bm, SR, nperseg=8192)
bands = []
for fc in (63, 125, 250, 500, 1000, 2000, 4000, 8000):
    m = (f >= fc / 1.414) & (f < fc * 1.414); bands.append(f"{fc}:{10 * np.log10(pv[m].sum() / (pb[m].sum() + 1e-18) + 1e-12):+.0f}")
out("   octave bands, voice-minus-bed dB over his talk (Hz:dB): " + " ".join(bands))

# ---- A3 / A4 ----
bed_ref = float(np.median([r[2] for r in rows])) if rows else -30
out("A3 bed under each play (bed level inside the span; the bed's talk median for reference; level 0.25 s before / 0.4 s after):")
for c, y in plays:
    a, b = int(c["s"] * SR), int(c["e"] * SR); inn = loud(B[a:b]); pre = loud(B[max(0, a - int(0.25 * SR)):a]); post = loud(B[b:b + int(0.4 * SR)])
    out(f"   {c['name']} {c['s']:.2f}-{c['e']:.2f}: bed inside {inn:.1f} LUFS (talk median {bed_ref:.1f}; {inn - bed_ref:+.1f} dB), peak {db(np.abs(B[a:b]).max()):.1f} dBFS; before {pre:.1f}, after {post:.1f}  -> {'MUTED' if inn < -60 else 'NOT MUTED'}")
talk_l = loud(V[talk_mask]) if talk_mask.any() else -99
out(f"A4 plays vs his talk ({talk_l:.1f} LUFS over his talk, A1 stem):")
for c, y in plays:
    a, b = int(c['s'] * SR), int(c['e'] * SR); lp = loud(stems['plays'][a:b]); pk = db(np.abs(stems['plays'][a:b]).max())
    out(f"   {c['name']}: {lp:.1f} LUFS = {lp - talk_l:+.1f} LU vs talk (want -1..-3), sample peak {pk:.1f} dBFS (want <= -6)  {'PASS' if -3.2 <= lp - talk_l <= -0.8 and pk <= -5.95 else 'FAIL'}")

# ---- A5 ----
h = int(0.05 * SR); rows5 = []
for c, y in cues:
    a = int(round(c["s"] * SR)); pk = db(np.abs(y).max()); lo, hi = max(0, a - int(1.5 * SR)), a + int(1.5 * SR)
    vpk = db(np.abs(V[lo:hi] + stems["plays"][lo:hi]).max())
    ky = kw(y); kb = kw(B[a:a + len(y)]); best = -99.0
    for k in range(0, max(1, min(len(ky), len(kb)) - h), h // 2):
        pc = (ky[k:k + h] ** 2).sum(1).mean(); pb = (kb[k:k + h] ** 2).sum(1).mean()
        if pc > 0: best = max(best, 10 * np.log10(pc + 1e-15) - 10 * np.log10(pb + 1e-15))
    under = vpk - pk; ok = 10 <= under <= 14.5 and best >= 4
    rows5.append((c["s"], c["name"], pk, vpk, under, best, ok))
out(f"A5 SFX cues ({len(cues)}): peak vs his local (+-1.5 s) voice peak (want 10-14 dB under), loudest 50 ms over the bed (want >= 4 dB):")
for s_, nm, pk, vpk, under, best, ok in rows5:
    out(f"   {s_:8.2f} {nm:24s} peak {pk:6.1f} dBFS, voice peak {vpk:6.1f}, {under:5.1f} dB under, 50ms over bed {best:+5.1f}  "
        + ("ok" if ok else "FAIL" + (" too loud" if under < 10 else "") + (" too soft" if under > 14.5 else "") + (" inaudible-vs-bed" if best < 4 else "")))
u = np.array([r[4] for r in rows5]); bo = np.array([r[5] for r in rows5]); nbad = sum(not r[6] for r in rows5)
out(f"   SFX summary: {len(rows5)} cues, dB under his voice peak min {u.min():.1f} / median {np.median(u):.1f} / max {u.max():.1f}; 50ms-over-bed min {bo.min():+.1f} / median {np.median(bo):+.1f}; cues failing A5: {nbad}   A5 {'PASS' if nbad == 0 else 'FAIL'}")

# ---- A6 ----
pk3 = [(k / SR, db(np.abs(MIX[k:k + n3]).max())) for k in range(0, N - n3, n3)]; over = [(round(float(t), 1), round(float(p), 1)) for t, p in pk3 if p > -4.0]
st = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", sf, "-af", "ebur128=peak=true", "-f", "null", "-"], capture_output=True, text=True).stderr
I = [l for l in st.splitlines() if l.strip().startswith("I:")][-1].split()[1]; TP = float([l for l in st.splitlines() if "Peak:" in l][-1].split()[1])
out(f"A6 mix: sample peak {db(np.abs(MIX).max()):.1f} dBFS, true peak {TP:.1f} dBTP (want <= -4), integrated {I} LUFS; 3 s windows over -4.0 dBFS: {len(over)} {over[:10]}   A6 {'PASS' if not over and TP <= -4.0 else 'FAIL'}")

# ---- CONVERSION SELF-CHECK: the dB the batch-6/7 writers INTENDED (plan.json) vs the raw property read back and converted here. Sets nothing. ----
pj = os.path.join(JOB, "plan.json")
if os.path.exists(pj):
    plan = json.load(open(pj, encoding="utf-8")); chk = []
    cg = {round(s_, 3): g for s_, g, k in plan.get("clip_gains", [])}
    d1 = [amp_db(P(c, "Amplify", "Left")["v"]) - cg[round(c["s"], 3)] for c in tracks[0]["clips"] if round(c["s"], 3) in cg and P(c, "Amplify", "Left")]
    if d1: chk.append(f"A1 Amplify: {len(d1)} clips, read-back raw -> dB minus the plan's clip_gain: max |diff| {max(abs(x) for x in d1):.4f} dB (formula (raw*144)-96)")
    m = plan.get("music") or {}
    for T in tracks:
        for c in T["clips"]:
            lv = P(c, "Volume", "Level")
            if lv and lv.get("keys") and m.get("ride"):
                want = {round(t_, 2): m["bed_db"] + r_ for t_, r_ in m["ride"]}; dd = []
                for kt, kv in lv["keys"]:
                    t_ = round(kt - c["i"], 2)
                    if t_ in want: dd.append(lvl_db(kv) - want[t_])
                if dd: chk.append(f"bed Level keys: {len(dd)} keys vs plan bed_db + ride: max |diff| {max(abs(x) for x in dd):.4f} dB (formula 20*log10(raw)+15); plan bed_db {m['bed_db']}")
    cue = {}
    for g in plan.get("graphics", []):
        for c_ in g.get("cues", []):
            if not str(c_[1]).startswith("play-"): cue[(round(c_[0], 2))] = c_[2]
    dd = []
    for T in tracks[1:]:
        for c in T["clips"]:
            lv = P(c, "Volume", "Level")
            if lv and not lv.get("tv") and not c["name"].startswith(("play-", "ES_")):
                best = min(cue, key=lambda t_: abs(t_ - c["s"]), default=None)
                if best is not None and abs(best - c["s"]) < 0.5: dd.append(lvl_db(lv["v"]) - cue[best])
    if dd: chk.append(f"SFX Level: {len(dd)} clips vs plan cue dB (matched by start): max |diff| {max(abs(x) for x in dd):.3f} dB")
    chk.append("reference points: Level raw 0.17782794 = 0 dB, 1.0 = +15 dB (Adobe slider -inf..+15); Amplify raw 0.66666667 = 0 dB, 0.69444 = +4 dB (lab-notes 1090); untouched Channel Volume reads 0.1778 (0 dB), untouched Amplify channels 0.6667 (0 dB)")
    out("SELF-CHECK (conversion): " + " | ".join(chk))
out(f"wrote {sf}")
open(os.path.join(JOB, "work", "tlmix-report.txt"), "w", encoding="utf-8").write("\n".join(Lines) + "\n")
