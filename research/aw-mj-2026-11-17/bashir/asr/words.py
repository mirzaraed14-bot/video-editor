import sys, json, glob, os, whisperx
dev = "cuda"
model = whisperx.load_model("medium.en", dev, compute_type="int8_float16", language="en")
align_model, meta = whisperx.load_align_model(language_code="en", device=dev)
jobs = []
for wav in sorted(glob.glob("*.wav")):
    out = wav.replace(".wav", ".words.json")
    if os.path.exists(out): continue
    off = float(wav.split("_")[-1][:-4]) if wav.startswith("tt_") else 0.0
    jobs.append((wav, off))
for wav, off in jobs:
    audio = whisperx.load_audio(wav)
    res = model.transcribe(audio, batch_size=1, language="en")
    al = whisperx.align(res["segments"], align_model, meta, audio, dev, return_char_alignments=False)
    words = [{"w": w.get("word"), "start": round(w["start"] + off, 3) if "start" in w else None, "end": round(w["end"] + off, 3) if "end" in w else None} for s in al["segments"] for w in s.get("words", [])]
    json.dump({"src": wav, "offset": off, "words": words, "segments": [{"start": round(s["start"]+off,2), "end": round(s["end"]+off,2), "text": s["text"]} for s in al["segments"]]}, open(wav.replace(".wav", ".words.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=0)
    print("done", wav, len(words), flush=True)
