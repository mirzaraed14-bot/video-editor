"""fillercuts.py: turn a list of filler/stutter word ranges (and long mid-sentence pauses) into frame-exact cuts on the
sequence timeline, with every edge MEASURED on the offline A1 rebuild (work/seq-a1.wav, seqaudio.py).

  PYTHONUTF8=1 python fillercuts.py <job>/tighten.json            # writes "cuts" back into the same file and prints a report

tighten.json: {"fps": 60, "remove": [[i, j, "expected words"], ...], "pauses": [[i, keep_s], ...]}
  remove  words i..j (inclusive, indices into transcript/words.json) — the text is checked so a re-transcribe can't shift it
  pauses  shorten the gap AFTER word i to keep_s seconds
A cut runs from just after the previous kept word's acoustic end (+40 ms) to just before the next kept word's acoustic
onset (-40 ms), both snapped INWARD to the sequence frame grid, so a kept word is never clipped (review 2: never cut a word
short). Measured edges: 10 ms RMS against the gap's own floor (+8 dB), not WhisperX's ends (they run early on trailing words).
"""
import json, os, re, subprocess, sys
import numpy as np

SR = 16000
path = sys.argv[1]; job = os.path.dirname(os.path.abspath(path))
T = json.load(open(path, encoding="utf-8")); fps = T.get("fps", 60)
w = [x for x in json.load(open(os.path.join(job, "transcript", "words.json"), encoding="utf-8"))["clips"][0]["words"] if "start" in x]
x = np.frombuffer(subprocess.run(["ffmpeg", "-v", "error", "-i", os.path.join(job, "work", "seq-a1.wav"), "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"],
                                 capture_output=True).stdout, np.float32)
H = SR // 100
env = 20 * np.log10(np.sqrt(np.convolve(x ** 2, np.ones(H) / H, "same")) + 1e-9)
norm = lambda s: re.sub(r"[^a-z0-9' ]", "", s.lower()).strip()


def floor_db(t0, t1):
    a, b = int(t0 * SR), int(t1 * SR)
    seg = env[a:b] if b - a > H else env[max(0, a - 4 * H):b + 4 * H]
    return float(np.percentile(seg, 15))


def acoustic_end(word, nxt_start):
    """first moment after the word where the envelope stays under floor+8 dB for 30 ms"""
    fl = floor_db(word["end"], max(word["end"] + 0.03, nxt_start)) + 8
    t = word["end"] - 0.03
    while t < nxt_start:
        i = int(t * SR)
        if np.all(env[i:i + 3 * H] < fl): return t
        t += 0.005
    return nxt_start


def acoustic_onset(word, prv_end):
    fl = floor_db(min(prv_end, word["start"] - 0.03), word["start"]) + 8
    t = word["start"] + 0.03
    while t > prv_end:
        i = int(t * SR)
        if np.all(env[i - 3 * H:i] < fl): return t
        t -= 0.005
    return prv_end


snap_up = lambda t: np.ceil(t * fps - 1e-6) / fps
snap_dn = lambda t: np.floor(t * fps + 1e-6) / fps


def quiet_frame(lo, hi):
    """the frame boundary in [lo, hi] whose ±4 ms is quietest (a cut there can't chop a vowel); None if the window has none"""
    f0, f1 = int(np.ceil(lo * fps - 1e-6)), int(np.floor(hi * fps + 1e-6))
    if f1 < f0: return None
    lv = lambda f: float(np.mean(env[max(0, int(f / fps * SR) - SR // 250):int(f / fps * SR) + SR // 250]))
    return min(range(f0, f1 + 1), key=lambda f: (round(lv(f), 0), f)) / fps
cuts, rep = [], []
for i, j, text in T.get("remove", []):
    got = " ".join(w[k]["w"] for k in range(i, j + 1))
    if norm(got) != norm(text): raise SystemExit(f"words {i}..{j} are {got!r}, expected {text!r}")
    P, N = w[i - 1], w[j + 1]
    e, o = acoustic_end(P, w[i]["start"]), acoustic_onset(N, w[j]["end"])
    e, o = max(e, P["end"]), min(o, N["start"])          # never inside a kept word, by EITHER measure (Pomp "that if": the
    a = quiet_frame(e + 0.005, min(e + 0.08, max(e + 0.02, w[i]["start"]))) or snap_up(e + 0.02)   # envelope onset ran late
    b = quiet_frame(max(o - 0.08, min(o - 0.02, w[j]["end"])), o - 0.005) or snap_dn(o - 0.02)     # and clipped the kept "if")
    if b - a < 2 / fps: rep.append(f"  skip {got!r}: no room ({a:.3f}-{b:.3f})"); continue
    cuts.append([round(a, 4), round(b, 4)])
    rep.append(f"  cut {a:8.3f}-{b:8.3f} ({b - a:5.3f} s)  ...{P['w']} [{got}] {N['w']}...")
for i, keep in T.get("pauses", []):
    P, N = w[i], w[i + 1]
    e, o = acoustic_end(P, N["start"]), acoustic_onset(N, P["end"])
    a = quiet_frame(e + keep / 2 - 0.03, e + keep / 2 + 0.03) or snap_up(e + keep / 2)
    b = quiet_frame(o - keep / 2 - 0.03, o - keep / 2 + 0.03) or snap_dn(o - keep / 2)
    if b - a < 2 / fps: rep.append(f"  skip pause after {P['w']!r}: {o - e:.2f} s already"); continue
    cuts.append([round(a, 4), round(b, 4)])
    rep.append(f"  cut {a:8.3f}-{b:8.3f} ({b - a:5.3f} s)  pause {o - e:.2f} s -> {keep:.2f} s after {P['w']!r} (before {N['w']!r})")
cuts.sort()
for (a0, b0), (a1, b1) in zip(cuts, cuts[1:]):
    if a1 < b0: raise SystemExit(f"overlapping cuts {a0}-{b0} / {a1}-{b1}")
lvl = lambda t: float(np.mean(env[int(t * SR) - SR // 250:int(t * SR) + SR // 250]))
for k, (a, b) in enumerate(cuts):
    rep.append(f"  edge levels {a:8.3f}: {lvl(a):6.1f} dB   {b:8.3f}: {lvl(b):6.1f} dB")
T["cuts"] = cuts
json.dump(T, open(path, "w", encoding="utf-8"), indent=1)
print("\n".join(rep))
print(f"{len(cuts)} cuts, {sum(b - a for a, b in cuts):.3f} s removed")
