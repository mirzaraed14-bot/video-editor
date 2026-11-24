"""wholecut.py <job> [--cpu] [--model medium.en]: C1-C3 proof, ONE Whisper pass (--model medium.en default) over the WHOLE cut voice (work/seq-a1.wav played as cuts.json plays it; play spans silenced),
diffed word-by-word against the DECIDED text (the words.json words inside every kept talk segment, corrections applied). Prints missing / extra words with
their cut time; writes work/wholecut.txt. Run via:  bash $KIT/tools/lock.sh gpu "$HOME/.cache/video-editor/whisperx-venv/Scripts/python.exe" -u wholecut.py <job>"""
import difflib, json, os, re, subprocess, sys
import numpy as np
if len(sys.argv) < 2 or sys.argv[1] in ('-h', '--help'): print(__doc__); raise SystemExit(0)
job = sys.argv[1]; SR = 16000; FPS = 60; CPU = "--cpu" in sys.argv
MODEL = sys.argv[sys.argv.index("--model") + 1] if "--model" in sys.argv else "medium.en"   # kit default: medium.en (lean recipe); large-v3 only on request
src = os.path.join(job, "work", "seq-a1.cut.wav") if "--reuse" in sys.argv else None
S = json.load(open(os.path.join(job, "transcript", "cuts.json"), encoding="utf-8"))["segments"]
K = json.load(open(os.path.join(job, "keep.json"), encoding="utf-8"))["keep"]
plays = [(e[1], e[2]) for e in K if e[0] == "t"]
W = [w for w in json.load(open(os.path.join(job, "transcript", "words.json"), encoding="utf-8"))["clips"][0]["words"] if "start" in w]
x = np.frombuffer(subprocess.run(["ffmpeg", "-v", "error", "-i", os.path.join(job, "work", "seq-a1.wav"), "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"], capture_output=True).stdout, np.float32).copy()
parts, decided, pos = [], [], 0.0
norm = lambda w: re.sub(r"[^a-z0-9']", "", w.lower())
for s in S:
    n = int(round(round((s["end"] - s["start"]) * FPS) / FPS * SR)); a = int(round(s["start"] * SR)); seg = x[a:a + n].copy()
    isplay = any(pa - 0.02 <= s["start"] and s["end"] <= pb + 0.02 for pa, pb in plays)
    if isplay: seg[:] = 0
    else:
        for w in W:
            m = 0.5 * (w["start"] + w["end"])
            if s["start"] <= m < s["end"] and norm(w["w"]): decided.append((pos + (m - s["start"]), norm(w["w"])))
    parts.append(seg); pos += len(seg) / SR
y = np.concatenate(parts)
try:
    import torch; os.add_dll_directory(os.path.join(os.path.dirname(torch.__file__), 'lib'))
except Exception: pass
from faster_whisper import WhisperModel
m = WhisperModel(MODEL, device="cpu" if CPU else "cuda", compute_type="int8" if CPU else "float16")
segs, _ = m.transcribe(y, language="en", beam_size=5, word_timestamps=True, vad_filter=False)
heard = [(w.start, norm(w.word)) for s in segs for w in s.words if norm(w.word)]
open(os.path.join(job, 'work', 'wholecut-heard.txt'), 'w', encoding='utf-8').write(' '.join(f'[{t:.1f}]{w}' if i % 12 == 0 else w for i, (t, w) in enumerate(heard)))
A = [w for _, w in decided]; B = [w for _, w in heard]; out = []
sm = difflib.SequenceMatcher(None, A, B, autojunk=False)
for op, i0, i1, j0, j1 in sm.get_opcodes():
    if op == "equal": continue
    t = decided[i0][0] if i0 < len(decided) else decided[-1][0]
    out.append(f"{op:8s} @ {t:7.2f}s  decided: {' '.join(A[i0:i1]) or '-'}   | heard: {' '.join(B[j0:j1]) or '-'}")
out.append(f"decided {len(A)} words, heard {len(B)}, cut {len(y) / SR:.3f} s, ratio {sm.ratio():.4f}")
open(os.path.join(job, "work", "wholecut.txt"), "w", encoding="utf-8").write("\n".join(out)); print("\n".join(out))
