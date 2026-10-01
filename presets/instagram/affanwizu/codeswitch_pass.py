"""@affanwizu code-switch pass: a second listener whose only job is to hear the creator's ENGLISH.

usage: python codeswitch_pass.py projects/<job>      (re-launches itself in the WhisperX venv)
→ projects/<job>/transcript/codeswitch.json  (words with times; `caption_qa.py` reads it)

Why (measured 2026-10-01 on four finished reels, reference/): Whisper's Urdu pass TRANSLATES or DROPS the
English connector phrases the creator mixes in ("doesn't mean" → ایسا, "it's just that" → ایسی طرح, "most
likely" / "but" / "as such" gone). A code-switched initial prompt makes Whisper keep English in Latin script:
19 of 34 English test phrases vs 3 of 34 without. The same prompt also makes it HALLUCINATE: it pastes the
prompt into hard stretches and skips speech. So this pass is never the transcript. `words.json` stays the
timing backbone; this pass only answers "was English said here?", and segments that echo the prompt are
discarded.

The prompt must reach EVERY stretch: faster-whisper applies `initial_prompt` to the first 30 s window only
(one run caught "most likely" and then went back to translating), so the cut is split at pauses into
<= 10 s chunks, as WhisperX does, and each chunk is decoded on its own with the prompt.
"""
import difflib, glob, json, os, re, subprocess, sys

def _reexec():
    home = os.path.expanduser("~/.cache/video-editor/whisperx-venv")
    py = os.path.join(home, "Scripts", "python.exe") if os.name == "nt" else os.path.join(home, "bin", "python")
    if os.path.exists(py) and os.path.abspath(sys.executable).lower() != os.path.abspath(py).lower():
        sys.exit(subprocess.call([py, *sys.argv], env=dict(os.environ, PYTHONUTF8="1", PYTHONIOENCODING="utf-8")))
    sys.exit("codeswitch_pass: needs faster-whisper (the WhisperX venv). Run transcribe.sh once to create it.")

try:
    import numpy as np
    from faster_whisper import WhisperModel
    from faster_whisper.vad import get_speech_timestamps, VadOptions
except ImportError:
    _reexec()

# Built from Seq 11 / Seq 17 lines only (none of the reference reels), Urdu script with English kept in Latin.
PROMPT = ("آج ہماری list میں ہے SL Aesthetics Clinic. by the way، I don't know، which means، I would say، "
          "it's not about the views، if they focus on this، imagine how profitable that is۔ "
          "میں نے کوئی video script نہیں کی، میں صرف بات کر رہا ہوں۔")
_norm = lambda t: re.sub(r"[\s،۔,.!?]+", " ", t).strip().lower()

def echoes_prompt(text):
    a, b = _norm(text), _norm(PROMPT)
    if len(a) < 12: return False
    return a in b or difflib.SequenceMatcher(None, a, b).find_longest_match(0, len(a), 0, len(b)).size >= 0.6 * len(a)

def main():
    job = sys.argv[1].rstrip("/\\")
    media = [p for e in ("mp4", "mov", "mkv", "m4v") for p in glob.glob(os.path.join(job, "raw", f"*.{e}"))]
    if not media: sys.exit(f"codeswitch_pass: no cut in {job}/raw/")
    raw = subprocess.check_output(["ffmpeg", "-v", "error", "-i", media[0], "-map", "0:a:0", "-ac", "1", "-ar", "16000",
                                   "-f", "s16le", "-"])
    audio = np.frombuffer(raw, np.int16).astype(np.float32) / 32768
    sr, CH = 16000, 10.0
    regions = get_speech_timestamps(audio, VadOptions(min_silence_duration_ms=300, speech_pad_ms=120))
    chunks = []
    for r in regions:
        a, b = r["start"] / sr, r["end"] / sr
        if chunks and b - chunks[-1][0] <= CH: chunks[-1][1] = b
        else:
            while b - a > CH: chunks.append([a, a + CH]); a += CH      # one long breathless stretch
            chunks.append([a, b])
    dev = os.environ.get("WHISPERX_DEVICE", "cpu")
    m = WhisperModel("large-v3", device=dev, compute_type="int8" if dev == "cpu" else "float16")
    words, dropped = [], []
    for a, b in chunks:
        segs, _ = m.transcribe(audio[int(a * sr):int(b * sr)], language="ur", initial_prompt=PROMPT, word_timestamps=True,
                               beam_size=5, vad_filter=False, condition_on_previous_text=False)
        for s_ in segs:
            if echoes_prompt(s_.text):
                dropped.append({"start": round(a + s_.start, 3), "end": round(a + s_.end, 3), "text": s_.text}); continue
            words += [{"w": w.word.strip(), "start": round(a + w.start, 3), "end": round(a + w.end, 3),
                       "prob": round(w.probability, 3)} for w in (s_.words or []) if w.word.strip()]
    os.makedirs(os.path.join(job, "transcript"), exist_ok=True)
    out = os.path.join(job, "transcript", "codeswitch.json")
    json.dump({"prompt": PROMPT, "words": words, "dropped_prompt_echoes": dropped}, open(out, "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    eng = [w for w in words if re.search(r"[A-Za-z]", w["w"])]
    print(f"codeswitch_pass: {len(words)} words, {len(eng)} in English, {len(dropped)} prompt echoes discarded → {out}")
    print("  " + " · ".join(f"{w['w']}@{w['start']:.1f}" for w in eng))

if __name__ == "__main__":
    main()
