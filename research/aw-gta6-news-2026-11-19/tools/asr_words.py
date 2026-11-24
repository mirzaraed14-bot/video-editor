# Word-timed ASR for short reaction clips (faster-whisper medium.en, GPU). For READING words; quotes are re-checked against frames/subtitles.
import sys, os, json, glob
import torch
os.add_dll_directory(os.path.join(os.path.dirname(torch.__file__), "lib"))
os.environ["PATH"] = os.path.join(os.path.dirname(torch.__file__), "lib") + os.pathsep + os.environ["PATH"]
sys.stdout.reconfigure(encoding="utf-8")
from faster_whisper import WhisperModel
m = WhisperModel("medium.en", device="cuda", compute_type="float16")
for a in sys.argv[1:]:
    segs, info = m.transcribe(a, language="en", word_timestamps=True, vad_filter=False, condition_on_previous_text=False)
    out = []; 
    with open(os.path.splitext(a)[0] + ".txt", "w", encoding="utf-8") as f:
        for s in segs:
            f.write(f"{s.start:7.2f}-{s.end:7.2f}  {s.text.strip()}\n")
            out.append({"start": s.start, "end": s.end, "text": s.text, "words": [{"w": w.word, "s": w.start, "e": w.end} for w in (s.words or [])]})
    json.dump(out, open(os.path.splitext(a)[0] + ".words.json", "w", encoding="utf-8"), ensure_ascii=False, indent=0)
    print(a, len(out))
