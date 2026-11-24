"""voiceclean7.py <job dir> <out name.mp4>: REACTIONS-V3 A1/A7. ONE cleaned full-length voice file.
Reads work/bleed/bleed.json (bleed7 run on the CURRENT cut). For every hit whose cancel residue is <= -30 dB (the recommended 'reference cancellation'), takes the bleed it
estimated at 16 kHz (OBS span minus work/bleed/clean-<seq>.wav), upsamples it x3 and SUBTRACTS it from the 48 kHz original over the span (so the voice keeps its full bandwidth),
with 10 ms edge fades on the subtraction. Everything else is the OBS audio sample-for-sample (same timeline, so words.json and every EDL in/out still hold).
Output: raw/<out name>.mp4 = the OBS video stream-copied + the cleaned audio as AAC 320k 48 kHz stereo. Then seq.json "obs" -> that path.
Run with the whisperx venv python (numpy + scipy)."""
import json, os, subprocess, sys
import numpy as np
from scipy.signal import resample_poly
job, outn = sys.argv[1], sys.argv[2]; SR = 48000; S16 = 16000
C = json.load(open(os.path.join(job, "transcript", "cuts.json"), encoding="utf-8"))["segments"]
raw = os.path.join(job, "raw", json.load(open(os.path.join(job, "work", "v2", "cuts.json"), encoding="utf-8"))["segments"][0]["clip"])
B = json.load(open(os.path.join(job, "work", "bleed", "bleed.json"), encoding="utf-8"))
def rd(p, sr, ss=None, t=None):
    c = ["ffmpeg", "-v", "error"] + (["-ss", f"{ss:.4f}"] if ss is not None else []) + (["-t", f"{t:.4f}"] if t is not None else []) + ["-i", p, "-vn", "-ac", "2", "-ar", str(sr), "-f", "f32le", "-"]
    return np.frombuffer(subprocess.run(c, capture_output=True).stdout, np.float32).astype(np.float64).reshape(-1, 2)
X = rd(raw, SR); n0 = len(X); O16 = rd(raw, S16, 0, 1200)      # whole-file 16 kHz array, sliced by index exactly as bleed7 does (an ffmpeg -ss seek on AAC can be one frame off)
for h in B["hits"]:
    inj = (h.get("cancel") or {}).get("injected_residue_db")
    if not (h["bleed_db"] > -30 and inj is not None and inj <= -30): print("  skip", h["seq"], h["bleed_db"], inj); continue
    a, b = h["a"], h["b"]; o16 = O16[int(a * S16):int(b * S16)]; cl = rd(os.path.join(job, "work", "bleed", f"clean-{h['seq']:.2f}.wav"), S16)
    m = min(len(o16), len(cl)); est16 = o16[:m] - cl[:m]; est = resample_poly(est16, 3, 1, axis=0)
    if os.environ.get("VC_REPLACE"):      # REPLACE the span by bleed7's cleaned 16 kHz span (verifiable: bleed7 re-measures ~0), upsampled x3 (band-limited to 8 kHz for this span only), 10 ms crossfades
        i0 = int(round(a * SR)); new = resample_poly(cl[:m], 3, 1, axis=0); n = min(len(new), len(X) - i0); f = int(0.01 * SR)
        w = np.minimum(np.minimum(np.arange(n), np.arange(n)[::-1]) / f, 1.0)[:, None]; low = resample_poly(resample_poly(X[i0:i0 + n], 1, 3, axis=0), 3, 1, axis=0)[:n]
        hi_part = X[i0:i0 + n] - low[:n]; X[i0:i0 + n] = (1 - w) * X[i0:i0 + n] + w * (new[:n] + hi_part)      # keep his >8 kHz detail (no bleed there), replace the <8 kHz band
        print(f"  replaced {a:.3f}-{b:.3f} (seq {h['seq']}) by the cleaned 16 kHz band + the original >8 kHz"); continue
    i0 = int(round(a * SR)); n = min(len(est), len(X) - i0); e = est[:n].copy(); f = int(0.01 * SR); ramp = np.minimum(np.minimum(np.arange(n), np.arange(n)[::-1]) / f, 1.0)[:, None]
    before = 10 * np.log10((X[i0:i0 + n] ** 2).mean()); X[i0:i0 + n] -= e * ramp
    print(f"  cancelled {a:.3f}-{b:.3f} (seq {h['seq']}): span {before:.1f} -> {10 * np.log10((X[i0:i0 + n] ** 2).mean()):.1f} dB, removed bleed {10 * np.log10((e ** 2).mean()):.1f} dB")
tmp = os.path.join(job, "work", "voice-clean.f32")
X.astype(np.float32).tofile(tmp)
out = os.path.join(job, "raw", outn)
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", raw, "-f", "f32le", "-ar", str(SR), "-ac", "2", "-i", tmp, "-map", "0:v:0", "-map", "1:a:0", "-c:v", "copy", "-c:a", "aac", "-b:a", "320k", "-shortest", out], check=True)
os.remove(tmp); print("wrote", out, os.path.getsize(out) // 1048576, "MB")
