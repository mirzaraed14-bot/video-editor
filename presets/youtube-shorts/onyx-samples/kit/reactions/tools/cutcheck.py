"""cutcheck.py: prove a tighten.json cut list OFFLINE before it touches Affan's timeline.

  <whisperx-venv python> cutcheck.py <job>/tighten.json

Applies the cuts to work/seq-a1.wav (hard cuts, exactly what a razor + close-gap does), then for every joint:
  - transcribes ±2.5 s around it (Whisper large-v3, the venv the rough-cut skill builds) and prints before/after text,
  - reports the sample step across the joint and the 5 ms RMS on each side (a click shows as a step >> both sides).
Writes work/seq-a1.tight.wav for listening.
"""
import json, os, subprocess, sys
import numpy as np

SR = 16000
path = sys.argv[1]; job = os.path.dirname(os.path.abspath(path)); T = json.load(open(path, encoding="utf-8"))
src = os.path.join(job, "work", "seq-a1.wav")
x = np.frombuffer(subprocess.run(["ffmpeg", "-v", "error", "-i", src, "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"], capture_output=True).stdout, np.float32)
cuts = T["cuts"]
keep, pos, joints = [], 0, []
for a, b in cuts:
    keep.append(x[pos:int(round(a * SR))]); pos = int(round(b * SR))
    joints.append((a, sum(len(k) for k in keep) / SR))
keep.append(x[pos:])
y = np.concatenate(keep)
subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "f32le", "-ar", str(SR), "-ac", "1", "-i", "-", os.path.join(job, "work", "seq-a1.tight.wav")],
               input=y.astype(np.float32).tobytes(), check=True)
try:                                              # ctranslate2 finds cuBLAS through torch's bundled DLLs on this box
    import torch; os.add_dll_directory(os.path.join(os.path.dirname(torch.__file__), "lib"))
except Exception:
    pass
from faster_whisper import WhisperModel           # noqa: E402  (whisperx pulls faster-whisper in)
try:                                              # CUTCHECK_DEVICE=cpu: run beside another agent's GPU job (batch 2 shares one GPU)
    if os.environ.get("CUTCHECK_DEVICE") == "cpu": raise RuntimeError("cpu requested")
    m = WhisperModel("large-v3", device="cuda", compute_type="float16"); m.transcribe(np.zeros(SR, np.float32), language="en")
except Exception:
    m = WhisperModel("large-v3", device="cpu", compute_type="int8")
txt = lambda seg: " ".join(s.text.strip() for s in m.transcribe(seg, language="en", beam_size=5, vad_filter=False)[0])
for (a, b), (_, jt) in zip(cuts, joints):
    i = int(round(jt * SR)); r = lambda s: 20 * np.log10(np.sqrt(np.mean(s ** 2)) + 1e-9)
    step = abs(float(y[i]) - float(y[i - 1]))
    before = txt(x[max(0, int((a - 2.5) * SR)):int((b + 2.5) * SR)])
    after = txt(y[max(0, i - int(2.5 * SR)):i + int(2.5 * SR)])
    print(f"cut {a:8.3f}-{b:8.3f}  joint {jt:8.3f}  rms L {r(y[i - 80:i]):6.1f} R {r(y[i:i + 80]):6.1f} dB  step {20 * np.log10(step + 1e-9):6.1f} dB")
    print(f"    before: {before}\n    after : {after}")
print(f"tight length {len(y) / SR:.3f} s (was {len(x) / SR:.3f})")
