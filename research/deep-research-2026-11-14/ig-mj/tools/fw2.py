# CPU transcription with word times (ig-mj, 14 Nov 2026). Usage: python -I fw2.py <audio> <out.txt> [model]
# Writes <out.txt> (segments) and <out>.words.json. CPU int8, 4 threads (gentle on his Premiere); silent, nothing played.
import sys, json
from faster_whisper import WhisperModel
src, out = sys.argv[1], sys.argv[2]
name = sys.argv[3] if len(sys.argv) > 3 else "medium.en"
m = WhisperModel(name, device="cpu", compute_type="int8", cpu_threads=4)
segs, info = m.transcribe(src, language="en", vad_filter=True, word_timestamps=True)
words = []
with open(out, "w", encoding="utf-8") as f:
    for s in segs:
        f.write(f"{s.start:8.2f} {s.end:8.2f} {s.text.strip()}\n")
        for w in (s.words or []):
            words.append({"w": w.word, "s": round(w.start, 2), "e": round(w.end, 2), "p": round(w.probability, 3)})
with open(out.rsplit(".", 1)[0] + ".words.json", "w", encoding="utf-8") as f:
    json.dump(words, f, ensure_ascii=False)
print("done", out, len(words), "words")
