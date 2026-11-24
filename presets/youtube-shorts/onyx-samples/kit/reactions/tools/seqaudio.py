"""seqaudio.py: rebuild a sequence's A1 offline (no export in Affan's project) from each clip's own source + in point.

  PYTHONUTF8=1 python seqaudio.py <a1.json> "<Sequence N>" <out.wav>

<a1.json> rows: [name, start, end, inPoint, mediaPath, ...] (the A1 readback). Each clip's slice is decoded from ITS file
(an "Audio Extracted_N.wav" is a partial extract with its own timebase, so in points never map onto the recording),
placed at its sequence start, mono 48 kHz. Words transcribed from the result are already in sequence time.
"""
import json, subprocess, sys
import numpy as np

SR = 48000
a1, name, out = sys.argv[1:4]
rows = json.load(open(a1, encoding="utf-8"))[name]["a1"]
end = max(r[2] for r in rows)
buf = np.zeros(int(round(end * SR)) + SR, np.float32)
for nm, s, e, i, path, *_ in rows:
    dur = e - s
    raw = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{i:.4f}", "-t", f"{dur:.4f}", "-i", path, "-vn", "-ac", "1", "-ar", str(SR),
                          "-f", "f32le", "-"], capture_output=True).stdout
    x = np.frombuffer(raw, np.float32)
    a = int(round(s * SR)); n = min(len(x), int(round(dur * SR)))
    if n < int(round(dur * SR)) - SR // 100:
        print(f"  ⚠ {nm} @ {s:.3f}: source gave {n / SR:.3f} s of {dur:.3f} s")
    buf[a:a + n] = x[:n]
buf = buf[:int(round(end * SR))]
pcm = (np.clip(buf, -1, 1) * 32767).astype("<i2").tobytes()
subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "s16le", "-ar", str(SR), "-ac", "1", "-i", "-", out], input=pcm, check=True)
print(f"{name}: {len(rows)} A1 clips -> {out} ({end:.3f} s)")
