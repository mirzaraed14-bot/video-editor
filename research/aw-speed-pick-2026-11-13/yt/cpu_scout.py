"""CPU scouting transcript (faster-whisper small.en, int8). Usage: python cpu_scout.py OUTDIR file1 [file2 ...]
Writes <stem>.scout.txt ([h:mm:ss.s] text per segment) and <stem>.words.json (word times) per input."""
import sys, os, json
from faster_whisper import WhisperModel

for s in (sys.stdout, sys.stderr):
    try:
        s.reconfigure(encoding="utf-8")
    except Exception:
        pass

out = sys.argv[1]
os.makedirs(out, exist_ok=True)
model = WhisperModel("small.en", device="cpu", compute_type="int8", cpu_threads=8)


def hms(t):
    return f"{int(t // 3600)}:{int(t % 3600 // 60):02d}:{t % 60:04.1f}"


for f in sys.argv[2:]:
    stem = os.path.splitext(os.path.basename(f))[0]
    segs, info = model.transcribe(f, language="en", vad_filter=True, word_timestamps=True, beam_size=1)
    lines, words = [], []
    for s in segs:
        lines.append(f"[{hms(s.start)}] {s.text.strip()}")
        for w in (s.words or []):
            words.append([round(w.start, 2), round(w.end, 2), w.word])
    open(os.path.join(out, stem + ".scout.txt"), "w", encoding="utf-8").write("\n".join(lines) + "\n")
    json.dump(words, open(os.path.join(out, stem + ".words.json"), "w", encoding="utf-8"))
    print(f"done {stem}: {len(lines)} segs, {info.duration:.0f}s", flush=True)
