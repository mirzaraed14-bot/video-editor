"""sfxprep3.py <job dir> <name=src[:maxlen]>...: REACTIONS-V3 SFX prep from CLEAN Epidemic originals (sfx/src/<src>.wav). The ONLY processing is LINEAR: trim the lead-in (to 30 ms before the first 5 ms window within
20 dB of the file's peak), cut to maxlen (20 ms fade-out), 3 ms fade-in, one gain that puts the sample peak at -1 dBFS (so a placed clip's static Level = target peak + 1 dB). No clipping, no EQ, no soft clip.
Writes sfx/<name>.wav (24-bit 48 kHz stereo) and an sfx/slices.json entry {offset = crest time in the trimmed file, len}. Example: sfxprep3.py <job> v3x-pop-lid=v3-pop-lid v3x-air=otn-air:0.55"""
import json, os, subprocess, sys
import numpy as np
job = sys.argv[1]; SR = 48000
SLp = os.path.join(job, "sfx", "slices.json"); SL = json.load(open(SLp, encoding="utf-8"))
for spec in sys.argv[2:]:
    name, src = spec.split("=", 1); mx = None
    if ":" in src: src, mx = src.split(":"); mx = float(mx)
    y = np.frombuffer(subprocess.run(["ffmpeg", "-v", "error", "-i", os.path.join(job, "sfx", "src", src + ".wav"), "-ac", "2", "-ar", str(SR), "-f", "f32le", "-"], capture_output=True).stdout, np.float32).astype(np.float64).reshape(-1, 2)
    h = int(0.005 * SR); n = len(y) // h; e = 20 * np.log10(np.sqrt((y[:n * h].reshape(n, h, 2) ** 2).mean((1, 2))) + 1e-9)
    k0 = int(np.argmax(e > e.max() - 20)); a = max(0, k0 * h - int(0.03 * SR)); y = y[a:]
    if mx: y = y[:int(mx * SR)]
    nf = int(0.02 * SR); y[-nf:] *= np.linspace(1, 0, nf)[:, None]; ni = int(0.003 * SR); y[:ni] *= np.linspace(0, 1, ni)[:, None]
    y *= 10 ** (-1.0 / 20) / np.abs(y).max()
    e = 20 * np.log10(np.sqrt((y[:len(y) // h * h].reshape(-1, h, 2) ** 2).mean((1, 2))) + 1e-9); off = round(float(np.argmax(e)) * 0.005 + 0.0025, 3)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "f32le", "-ar", str(SR), "-ac", "2", "-i", "-", "-c:a", "pcm_s24le", os.path.join(job, "sfx", name + ".wav")], input=y.astype(np.float32).tobytes(), check=True)
    SL[name] = dict(src="./sfx/src/%s.wav" % src, offset=off, len=round(len(y) / SR, 3), note="v3 clean original, linear trim + gain only")
    print(f"{name:20s} from {src:18s} len {len(y) / SR:.2f} s crest at {off:.3f} s (file peak -1.0 dBFS)")
json.dump(SL, open(SLp, "w", encoding="utf-8"), indent=1)
