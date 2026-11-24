"""bleed7.py <job dir> [--cam <camera file>] [--cam-off <cam_t - OBS_t>] [--extra <file>...]: DESKTOP-AUDIO BLEED (REACTIONS-V3 A7).

OBS has ONE stereo track: his mic and the desktop audio mixed. For every file he PLAYED (plan.json plays: their Short, our samples; plus --extra files)
this finds where that file's audio sits under his talk in the KEPT spans of the cut (cuts.json segments whose draft kind is 'A' = his own talk),
how loud it is against his voice, whether the synced CAMERA audio is clean over the same spans, and what a reference cancellation leaves behind.
Never plays anything: ffmpeg decodes to arrays, one spectrogram still per worst span.  Run with the whisperx venv python (numpy + scipy):
  ~/.cache/video-editor/whisperx-venv/Scripts/python.exe tools7/bleed7.py <job dir>
Writes <job>/work/bleed/{bleed-report.txt, bleed.json, spec-*.png, clean-*.wav}.

Method (16 kHz mono/stereo):
 1. DETECT: GCC-PHAT (200-6000 Hz) of every 4 s OBS window (hop 2 s, whole recording) against each played file -> offset (OBS t - file t) clusters.
 2. MEASURE: for each kept talk segment and each offset cluster, least-squares fit of the file (both channels, +-8 sample taps) to each OBS channel over the
    overlap: bleed = explained power, voice = the residual (his voice + room); level = 10 log10(bleed / voice), F statistic for significance.
 3. CAMERA: the camera file (cam t = OBS t + cam_off) over the same spans: noise floor (P5 of 50 ms RMS over the recording), voice level (P90), and whether the file
    correlates with it (peak normalised xcorr over +-250 ms against the null); spectrogram still OBS vs camera.
 4. CANCEL (prototype): subtract the fitted file from the OBS span; residue measured on a synthetic injection of the same file at the same measured level into a
    bleed-free talk segment (the truth is known there), plus the re-measured F on the real span after cancelling.
"""
import json, os, subprocess, sys
import numpy as np
from scipy.signal import butter, sosfiltfilt
from scipy.fft import rfft, irfft, next_fast_len

JOB = sys.argv[1]; SR = 16000
def arg(name, default=None):
    return sys.argv[sys.argv.index(name) + 1] if name in sys.argv else default
HERE = os.path.dirname(os.path.abspath(__file__))
plan = json.load(open(os.path.join(JOB, "plan.json"), encoding="utf-8"))
C = json.load(open(os.path.join(JOB, "transcript", "cuts.json"), encoding="utf-8"))["segments"]
D = json.load(open(os.path.join(JOB, "transcript", "cuts.draft.json"), encoding="utf-8"))["segments"]
kind = lambda s: max(D, key=lambda d: min(d["end"], s["end"]) - max(d["start"], s["start"]))["kind"]
raw = os.path.join(JOB, "raw", C[0]["clip"])
OUT = os.path.join(JOB, "work", "bleed"); os.makedirs(OUT, exist_ok=True)
FPS = 60
def rd(p, ss=None, t=None, ac=2):
    c = ["ffmpeg", "-v", "error"] + (["-ss", f"{ss:.3f}"] if ss is not None else []) + (["-t", f"{t:.3f}"] if t is not None else []) + ["-i", p, "-vn", "-ac", str(ac), "-ar", str(SR), "-f", "f32le", "-"]
    y = np.frombuffer(subprocess.run(c, capture_output=True).stdout, np.float32).astype(np.float64)
    return y.reshape(-1, ac) if ac > 1 else y
db = lambda v: 10 * np.log10(max(float(v), 1e-20))

# ---- kept spans (his talk) in OBS time + sequence time ----
segs = []; pos = 0.0
for s in C:
    d = round(round((s["end"] - s["start"]) * FPS) / FPS, 6)
    segs.append(dict(a=s["start"], b=s["end"], seq=round(pos, 3), kind=kind(s), text=s.get("transcript", ""))); pos += d
talk = [s for s in segs if s["kind"] == "A" and s["b"] - s["a"] >= 0.3]
O = rd(raw, 0, float(os.environ.get("BLEED_LEN", "1200")))            # BL (11-11): BLEED_LEN=454 (its cut runs to raw ~430)
print(f"OBS {len(O) / SR:.1f} s, {len(talk)} kept talk segments, {sum(s['b'] - s['a'] for s in talk):.1f} s")

# ---- played files ----
files = []
for p in plan["plays"]:
    f = p["file"]
    if f not in files: files.append(f)
for i, a in enumerate(sys.argv):
    if a == "--extra": files.append(sys.argv[i + 1])
F = {f: rd(f) for f in files}
for f in files: print(f"  played file {os.path.basename(f)}: {len(F[f]) / SR:.1f} s")
sos = butter(4, [200, 6000], btype="band", fs=SR, output="sos")

# ---- 1. DETECT: GCC-PHAT windows ----
def phat_windows(f, W=4.0, hop=2.0):
    ff = sosfiltfilt(sos, F[f].mean(1)); Lf = len(ff); w = int(W * SR); nfft = next_fast_len(Lf + w)
    FF = rfft(ff, nfft); res = []; fr = np.fft.rfftfreq(nfft, 1 / SR); BM = ((fr >= 200) & (fr <= 6000)).astype(float)
    om = O.mean(1)
    for s0 in np.arange(0.0, len(om) / SR - W, hop):
        x = sosfiltfilt(sos, om[int(s0 * SR):int(s0 * SR) + w]); X = rfft(x, nfft)
        R = np.conj(X) * FF; R /= (np.abs(R) + 1e-9); R *= BM; c = irfft(R, nfft)
        k = int(np.argmax(np.abs(c))); d = k if k < nfft // 2 else k - nfft                # file t of the window start = d / SR
        sig = 1.4826 * np.median(np.abs(c - np.median(c))) + 1e-12; sc = abs(c[k]) / sig
        res.append((float(s0), float(s0 - d / SR), float(sc)))
    return res
clusters = []
for f in files:
    ws = phat_windows(f); good = [w for w in ws if w[2] > 20.0]
    used = set()
    for i, w in enumerate(good):
        if i in used: continue
        grp = [j for j, v in enumerate(good) if abs(v[1] - w[1]) < 0.03]
        for j in grp: used.add(j)
        if len(grp) >= 3:
            offs = np.median([good[j][1] for j in grp]); t0 = min(good[j][0] for j in grp); t1 = max(good[j][0] for j in grp) + 4.0
            clusters.append(dict(file=f, off=float(offs), obs0=t0, obs1=t1, n=len(grp), score=float(max(good[j][2] for j in grp))))
print(f"offset clusters (OBS t = file t + off): {len(clusters)}")
for c in clusters: print(f"  {os.path.basename(c['file'])}: off {c['off']:.3f} s, seen OBS {c['obs0']:.1f}-{c['obs1']:.1f} ({c['n']} windows, PHAT score {c['score']:.0f})")

# ---- 2. MEASURE ----
TAPS = 2
def regressors(f, a, b, off, n=None):
    """file samples aligned to OBS [a, b) (both channels, TAPS lags each side); zeros outside the file."""
    n = n if n is not None else int(round((b - a) * SR)); i0 = int(round((a - off) * SR)); X = []
    ff = F[f]
    for ch in (0, 1):
        for lag in range(-TAPS, TAPS + 1):
            idx = np.arange(n) + i0 + lag; col = np.zeros(n); ok = (idx >= 0) & (idx < len(ff)); col[ok] = ff[idx[ok], ch]; X.append(col)
    return np.array(X).T
def pe(x): return np.vstack([x[:1] * 0, x[1:] - 0.95 * x[:-1]]) if x.ndim == 2 else np.concatenate([[0.0], x[1:] - 0.95 * x[:-1]])
def fit(y, X):
    """y (n, 2) OBS channels, X (n, p): LS per channel -> (bleed power, residual power, F, cleaned)."""
    n, p = X.shape; Pd = Pr = 0.0; cl = np.zeros_like(y)
    for c in range(2):
        h, *_ = np.linalg.lstsq(X, y[:, c], rcond=None); fit_ = X @ h; Pd += (fit_ ** 2).sum(); Pr += ((y[:, c] - fit_) ** 2).sum(); cl[:, c] = y[:, c] - fit_
    Py = (y ** 2).sum(); R2 = min(Pd / (Py + 1e-20), 0.999999)
    Fs = (R2 / p) / ((1 - R2) / (2 * n - 2 * p)) if R2 > 0 else 0.0
    return Pd / n, Pr / n, Fs, cl
rows = []
CTRL = [-23.0, -13.0, -7.0, 7.0, 13.0, 23.0]       # control offsets (s): the SAME fit against a different part of the file = the chance level of this statistic on his (coloured) speech
def measure(f, a, b, off, y):
    X = regressors(f, a, b, off, len(y)); live = np.abs(X).sum(1) > 0
    if live.sum() < 0.2 * SR: return None
    Pd, Pr, Fs, _ = fit(pe(y)[live], pe(X)[live]); return db(Pd / (Pr + 1e-20)), db(Pr), Fs, float(live.sum() / SR)
for s in talk:
    a, b = s["a"], s["b"]; y = O[int(a * SR):int(b * SR)]
    for cl in clusters:
        f = cl["file"]; ov0, ov1 = max(a - cl["off"], 0.0), min(b - cl["off"], len(F[f]) / SR)
        if ov1 - ov0 < 0.3: continue
        m0 = measure(f, a, b, cl["off"], y)
        if m0 is None: continue
        nulls = [m[0] for m in (measure(f, a, b, cl["off"] + c_, y) for c_ in CTRL) if m is not None]
        mu, sd = (float(np.mean(nulls)), float(np.std(nulls)) + 0.5) if len(nulls) >= 3 else (-99.0, 1.0)
        rows.append(dict(seq=s["seq"], a=a, b=b, text=s["text"], file=os.path.basename(f), file_path=f, off=cl["off"], overlap=float(ov1 - ov0), bleed_db=m0[0], voice_db=m0[1], F=float(m0[2]), null_db=mu, z=(m0[0] - mu) / sd))
hits = [r for r in rows if r["z"] > 5 and r["bleed_db"] > r["null_db"] + 3 and r["bleed_db"] > -55]
best = {}
for r in hits:
    k = (r["a"], r["file"])
    if k not in best or r["z"] > best[k]["z"]: best[k] = r
hits = sorted(best.values(), key=lambda r: r["seq"])
print(f"kept talk segments with a played file audible under his voice (z > 5 vs control offsets): {len(hits)} of {len(talk)}")
for r in hits:
    print(f"  seq {r['seq']:7.2f} OBS {r['a']:7.2f}-{r['b']:7.2f} {r['file']:34s} bleed {r['bleed_db']:+6.1f} dB re his voice (chance {r['null_db']:+.1f}, z {r['z']:.0f}, overlap {r['overlap']:.1f} s)  '{r['text'][:50]}'")

# ---- positive control: inject a played file at known levels into kept talk segments and see whether the detector finds it ----
rng0 = np.random.default_rng(3); long_ = [s for s in talk if s["b"] - s["a"] >= 1.5]; ctrl_f = files[1] if len(files) > 1 else files[0]
print("POSITIVE CONTROL (injected at a known level re his voice, 12 segments >= 1.5 s each; detected = z > 5 vs control offsets):")
for lvl in (-20, -30, -40):
    det = 0; zs = []
    for s_ in rng0.choice(len(long_), size=min(12, len(long_)), replace=False).tolist():
        sg = long_[s_]; a, b = sg["a"], sg["b"]; y = O[int(a * SR):int(b * SR)]; off = a - 8.0
        Xs = regressors(ctrl_f, a, b, off, len(y)); add = np.stack([Xs[:, TAPS], Xs[:, 2 * TAPS + 1 + TAPS]], 1)
        g = np.sqrt(10 ** (lvl / 10) * (y ** 2).mean() / ((add ** 2).mean() + 1e-20)); yi = y + g * add
        m0 = measure(ctrl_f, a, b, off, yi); nl = [m[0] for m in (measure(ctrl_f, a, b, off + c_, yi) for c_ in CTRL) if m is not None]
        if m0 is None or not nl: continue
        z = (m0[0] - np.mean(nl)) / (np.std(nl) + 0.5); zs.append(z); det += z > 5
    print(f"  {lvl} dB re voice: detected {det}/{len(zs)}, median z {np.median(zs) if zs else float('nan'):.1f}")

# ---- 3. CAMERA ----
cam = arg("--cam"); cam_off = arg("--cam-off")
if cam is None:
    for c_ in json.load(open(os.path.join(JOB, "seq.json"), encoding="utf-8")).get("cameras", []):      # kit: the camera + sync json come from seq.json (prep.sh writes work/sync.json)
        sp = os.path.join(JOB, c_.get("sync", "work/sync.json"))
        if os.path.exists(sp):
            j = json.load(open(sp))
            if "offset_s" in j and "camera" in j: cam = j["camera"]; cam_off = j["offset_s"]; break
if cam: print(f"camera {cam}  (cam t = OBS t + {float(cam_off):.4f})")
cam_rep = []
if cam:
    cam_off = float(cam_off)
    CA = rd(cam, 0, 440)
    # verify the sync sign by PHAT on a 20 s kept stretch
    t0 = talk[len(talk) // 2]["a"]; xo = sosfiltfilt(sos, O[int(t0 * SR):int((t0 + 20) * SR)].mean(1)); i0 = int((t0 + cam_off) * SR)
    xc = sosfiltfilt(sos, CA[i0 - SR:i0 + 21 * SR].mean(1)); nf = next_fast_len(len(xo) + len(xc)); R = np.conj(rfft(xo, nf)) * rfft(xc, nf); R /= np.abs(R) + 1e-9; c = irfft(R, nf); k = int(np.argmax(c)); k = k if k < nf // 2 else k - nf
    print(f"  sync check: camera audio lags the model by {(k - SR) / SR * 1000:+.1f} ms (PHAT {c[k] / (1.4826 * np.median(np.abs(c - np.median(c)))):.0f} sigma)")
    cm = CA.mean(1); h = int(0.05 * SR); rms = np.array([db((cm[i:i + h] ** 2).mean()) for i in range(0, len(cm) - h, h)])
    floor = float(np.percentile(rms[rms > -90], 5)); print(f"  camera audio: noise floor (P5 of 50 ms RMS) {floor:.1f} dBFS, whole-recording P95 {np.percentile(rms, 95):.1f} dBFS")
    om = O.mean(1); orms = np.array([db((om[i:i + h] ** 2).mean()) for i in range(0, len(om) - h, h)]); ofloor = float(np.percentile(orms[orms > -90], 5))
    print(f"  OBS audio:    noise floor {ofloor:.1f} dBFS, P95 {np.percentile(orms, 95):.1f} dBFS")
    for r in hits:
        a, b = r["a"], r["b"]; i0 = int(round((a + cam_off) * SR)); seg = CA[i0:i0 + int((b - a) * SR)]
        sm = seg.mean(1); w = [db((sm[i:i + h] ** 2).mean()) for i in range(0, len(sm) - h, h)]; vlev = float(np.percentile(w, 90)); nlev = floor
        # does the file correlate with the camera audio? max normalised xcorr over +-250 ms vs the same statistic at 40 far lags
        f = r["file_path"]
        ff = F[f].mean(1); fi0 = int(round((a - r["off"]) * SR)); fseg = ff[max(fi0, 0):fi0 + len(sm)]
        if len(fseg) > SR // 2 and len(sm) > 2 * 4000 + 100:
            nn = min(len(sm), len(fseg)); ys = sosfiltfilt(sos, sm[:nn]); fs = sosfiltfilt(sos, fseg[:nn])
            nl = 4000; cx = lambda lag: abs(np.dot(ys[max(lag, 0):len(ys) + min(lag, 0)], fs[max(-lag, 0):len(fs) + min(-lag, 0)])) / (np.linalg.norm(ys[max(lag, 0):len(ys) + min(lag, 0)]) * np.linalg.norm(fs[max(-lag, 0):len(fs) + min(-lag, 0)]) + 1e-12)
            pk = max(cx(l) for l in range(-nl, nl + 1, 8)); null = [cx(l) for l in range(5000, min(len(ys) - 1500, 12000), 100)] or [0.0]; z = (pk - np.mean(null)) / (np.std(null) + 1e-9)
        else: pk, z = 0.0, 0.0
        r["cam"] = dict(voice_p90=vlev, floor=nlev, snr=vlev - nlev, file_xcorr=float(pk), file_z=float(z))
        print(f"  cam seq {r['seq']:7.2f}: voice P90 {vlev:.1f} dBFS, floor {nlev:.1f} -> SNR {vlev - nlev:.0f} dB; file corr {pk:.3f} (z {z:.1f} vs null)  {'DESKTOP AUDIO PRESENT' if z > 6 else 'clean of the file'}")

# ---- 4. CANCEL prototype + residue on an injection ----
clean_pool = [s for s in talk if not any(h_["a"] == s["a"] for h_ in hits)]
rng = np.random.default_rng(7)
for r in hits:
    f = r["file_path"]
    a, b = r["a"], r["b"]; y = O[int(a * SR):int(b * SR)]; X = regressors(f, a, b, r["off"], len(y)); live = np.abs(X).sum(1) > 0
    Pd, Pr, Fs, cl = fit(y[live], X[live]); full = y.copy(); full[live] = cl
    _, _, F2, _ = fit(full[live], X[live])
    # synthetic truth: a bleed-free talk segment of >= the span's length, the same file chunk added at the SAME measured level re his voice
    donors = [s for s in clean_pool if s["b"] - s["a"] >= (b - a) * 0.98]
    if donors:
        dn = donors[int(rng.integers(len(donors)))]; yd = O[int(dn["a"] * SR):int(dn["a"] * SR) + len(y)]
        Xs = regressors(f, a, b, r["off"], len(y)); fpart = Xs[:, TAPS]; fpart2 = Xs[:, 2 * TAPS + 1 + TAPS]; add = np.stack([fpart, fpart2], 1)
        g = np.sqrt(10 ** (r["bleed_db"] / 10) * (yd ** 2).mean() / ((add ** 2).mean() + 1e-20)); inj = yd + g * add
        liv = live[:len(inj)]
        Pd2, Pr2, F3, cl2 = fit(inj[liv], Xs[liv]); res = cl2 - yd[liv]; residue = db((res ** 2).mean() / ((yd[liv] ** 2).mean()))
        r["cancel"] = dict(F_before=r["F"], F_after_real=float(F2), injected_residue_db=residue, injected_F_before=float(F3))
    else: r["cancel"] = dict(F_before=r["F"], F_after_real=float(F2), injected_residue_db=None)
    sf = os.path.join(OUT, f"clean-{r['seq']:.2f}.wav")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "f32le", "-ar", str(SR), "-ac", "2", "-i", "-", sf], input=full.astype(np.float32).tobytes(), check=True)
    print(f"  cancel seq {r['seq']:7.2f}: bleed {r['bleed_db']:+.1f} dB -> real span F {r['F']:.0f} -> {F2:.1f} after; injected-truth residue {r['cancel']['injected_residue_db'] if r['cancel']['injected_residue_db'] is None else round(r['cancel']['injected_residue_db'], 1)} dB re his voice")

# ---- spectrogram stills (worst span) ----
if hits and cam:
    w = max(hits, key=lambda r: r["bleed_db"]); a, b = w["a"], w["b"]
    def spec(src, ss, name):
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{ss:.3f}", "-t", f"{b - a:.3f}", "-i", src, "-lavfi", "showspectrumpic=s=900x220:legend=0:stop=8000:scale=log", "-frames:v", "1", os.path.join(OUT, name)], check=True)
    spec(raw, a, "spec-obs.png"); spec(cam, a + cam_off, "spec-cam.png")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", os.path.join(OUT, "spec-obs.png"), "-i", os.path.join(OUT, "spec-cam.png"), "-filter_complex", "vstack", os.path.join(OUT, f"spec-{w['seq']:.2f}.png")], check=True)
    print(f"spectrogram (top OBS mic+desktop, bottom camera audio), seq {w['seq']:.2f}: {os.path.join(OUT, 'spec-%.2f.png' % w['seq'])}")

# ---- recommendation ----
rec = []
for r in hits:
    cam_ok = r.get("cam") and r["cam"]["file_z"] <= 6 and r["cam"]["snr"] >= 25
    canc = r["cancel"].get("injected_residue_db")
    if r["bleed_db"] <= -30: fx = "none needed (already >= 30 dB under his voice)"
    elif cam_ok: fx = "CAMERA audio for this span"
    elif canc is not None and canc <= -30: fx = "reference cancellation"
    else: fx = "CUT the span"
    r["fix"] = fx; rec.append(f"seq {r['seq']:7.2f} OBS {r['a']:.2f}-{r['b']:.2f} bleed {r['bleed_db']:+.1f} dB: {fx}")
print("RECOMMENDATION"); print("\n".join("  " + x for x in rec) or "  (no bleed found)")
json.dump(dict(clusters=clusters, hits=hits, all_rows=rows), open(os.path.join(OUT, "bleed.json"), "w"), indent=1, default=float)
