# asr_words.py <wav> [offset_seconds] : WhisperX medium.en words for one wav -> <wav>.words.json (+ .txt lines). Run under asr_run.sh locks.
import sys, json, whisperx
wav = sys.argv[1]; off = float(sys.argv[2]) if len(sys.argv) > 2 else 0.0
dev = "cuda"
model = whisperx.load_model("medium.en", dev, compute_type="int8_float16", language="en")
align_model, meta = whisperx.load_align_model(language_code="en", device=dev)
audio = whisperx.load_audio(wav)
res = model.transcribe(audio, batch_size=4, language="en")
al = whisperx.align(res["segments"], align_model, meta, audio, dev, return_char_alignments=False)
words = [{"w": w.get("word"), "start": round(w["start"] + off, 3) if "start" in w else None, "end": round(w["end"] + off, 3) if "end" in w else None} for s in al["segments"] for w in s.get("words", [])]
segs = [{"start": round(s["start"] + off, 2), "end": round(s["end"] + off, 2), "text": s["text"]} for s in al["segments"]]
json.dump({"src": wav, "offset": off, "words": words, "segments": segs}, open(wav + ".words.json", "w", encoding="utf-8"), ensure_ascii=False, indent=0)
def hms(t): t = int(t); return f"{t//3600}:{t%3600//60:02d}:{t%60:02d}"
open(wav + ".lines.txt", "w", encoding="utf-8").write("\n".join(f"{hms(s['start'])}\t{s['text'].strip()}" for s in segs))
print("done", wav, len(words), flush=True)
