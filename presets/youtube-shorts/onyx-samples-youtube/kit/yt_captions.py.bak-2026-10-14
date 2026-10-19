"""yt_captions.py: the caption chunks of a YouTube-look sample -> <job>/yt/captions.json (README § 5).

  python presets/youtube-shorts/onyx-samples-youtube/kit/yt_captions.py projects/<job>

Reads `<job>/yt/spec.json` → "captions": {
  "words": "outputs/<job>.transcript.json" (canonical transcript: [{text, start, end, type}]) or a pilot plan.json
           ({"words_patched": [{t, s, e}]}) — either way on the CUT's timeline,
  "lead": 0.135       seconds a chunk appears before its first word's MEASURED acoustic onset (≈ 3.25 frames at 24 fps; the onset
                      is found on the voice track's 10 ms envelope near the WhisperX start, which runs 40-155 ms late; when it
                      can't be measured the chunk leads the WhisperX start by lead + 0.055 s),
  "snap": 2           a chunk change up to this many frames AFTER a shot cut moves back onto the cut; a chunk that changes VOICE
                      also moves LATER onto a cut ≤ 4 frames ahead, if that cut is still before its first word (the speaker
                      on screen and the caption colour switch together),
  "chunks": [[n_words, "TEXT", voice, wipe(, start_f)], ...]   in order, covering every word exactly once; the optional 5th item
                      pins the chunk's first frame (a measured acoustic onset, when the transcript's stamp is off)
}
voice: "main" (white, wipe → red) or another kit voice ("yellow", "cyan", "purple"): solid colour, wipe white → colour.
Rules checked: ≤ 19 characters per chunk, words used exactly once. Each chunk holds until the next one (never blank).
"""
import json, math, os, subprocess, sys
import numpy as np

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8")
    except Exception:
        pass


def load_words(path):
    d = json.load(open(path, encoding="utf-8"))
    if isinstance(d, dict) and "words_patched" in d:
        return [dict(t=w["t"], s=w["s"], e=w["e"]) for w in d["words_patched"]]
    ws = d["words"] if isinstance(d, dict) else d
    return [dict(t=w.get("text") or w.get("word") or w.get("t"), s=w.get("start", w.get("s")), e=w.get("end", w.get("e")))
            for w in ws if w.get("type", "word") == "word"]


def envelope(path, sr=16000):
    """10 ms RMS envelope (dB) of a file's audio."""
    r = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-vn", "-ac", "1", "-ar", str(sr), "-f", "f32le", "-"], capture_output=True)
    x = np.frombuffer(r.stdout, np.float32)
    n = sr // 100
    x = x[: len(x) // n * n].reshape(-1, n)
    return 20 * np.log10(np.sqrt((x ** 2).mean(1)) + 1e-9)


def onset(env, ws, prev_end, gfloor):
    """Acoustic onset of a word whose WhisperX start is ws, searched only AFTER the previous word's end (QA r3: an
    unbounded search caught dips inside the previous word, and noise in silence). After a pause (≥ 0.12 s): the first
    10 ms frame that stays 12 dB over the noise floor (local, never below the track's absolute floor + 15 dB) for 30 ms.
    In continuous speech: the END of the dip before the word (the first frame 6 dB over the dip's minimum).
    Clamped to ws − 0.15 … ws + 0.02 (WhisperX starts run 40-155 ms late). None if nothing qualifies."""
    i = lambda t: int(round(t * 100))
    lo_t = max(prev_end - 0.03, ws - 0.25)
    a, b = max(0, i(lo_t)), min(len(env), i(ws + 0.03))
    if b - a < 3:
        return None
    seg = env[a:b]
    if ws - prev_end >= 0.12:
        floor = max(np.percentile(env[max(0, i(prev_end)):max(i(prev_end) + 1, i(ws - 0.05))], 20), gfloor + 15)
        for k in range(len(seg) - 2):
            if (seg[k:k + 3] > floor + 12).all():
                return float(np.clip((a + k) / 100, ws - 0.15, ws + 0.02))
        return None
    m = int(np.argmin(seg))
    rise = np.nonzero(seg[m:] > seg[m] + 6)[0]
    if not len(rise):
        return None
    return float(np.clip((a + m + rise[0]) / 100, ws - 0.15, ws + 0.02))


def main():
    job = os.path.abspath(sys.argv[1])
    spec = json.load(open(os.path.join(job, "yt", "spec.json"), encoding="utf-8"))
    c = spec["captions"]
    fps, end_frame = spec["fps"], spec["frames"]
    W = load_words(os.path.join(job, c["words"]))
    skip = c.get("skip_words", 0)                      # leading junk words of the transcript (e.g. a mis-heard breath)
    W = W[skip:]
    chunks = c["chunks"]
    if sum(ch[0] for ch in chunks) != len(W):
        sys.exit(f"yt_captions: chunks cover {sum(ch[0] for ch in chunks)} words, the transcript has {len(W)} (after skip_words={skip})")
    cuts = [sh["f0"] for sh in spec["shots"][1:]]                    # shot cuts, straight from the spec (no picture pass needed)
    lead, snap = c.get("lead", 0.135), c.get("snap", 2)
    env = envelope(os.path.join(job, spec["audio"]["voice"])) if spec.get("audio", {}).get("voice") else None
    gfloor = float(np.percentile(env, 5)) if env is not None else -90.0
    out, i, measured = [], 0, 0
    for spec_ch in chunks:
        n, text, voice, wipe = spec_ch[:4]
        fixed = spec_ch[4] if len(spec_ch) > 4 else None          # optional 5th item: a measured start frame (WhisperX stamps can be 0.1-0.6 s off)
        ws = W[i:i + n]; i += n
        if len(text) > 19:
            sys.exit(f"yt_captions: '{text}' is {len(text)} characters (max 19)")
        prev_end = out[-1]["last_word_end"] if out else 0.0
        on = onset(env, ws[0]["s"], prev_end, gfloor) if (env is not None and out) else None
        measured += on is not None
        t = (on - lead) if on is not None else (ws[0]["s"] - lead - 0.055)
        t = max(t, ws[0]["s"] - 0.30, prev_end - 0.05)                  # never absurdly early, never over words still being said
        f = 0 if not out else int(math.floor(t * fps + 1e-6))
        if out:
            f = max(f, out[-1]["start_f"] + 1)
        start = f
        if out:
            earlier = [k for k in cuts if 0 <= f - k <= snap and k / fps >= prev_end - 0.05]   # a cut just before: change on the cut
            later = [k for k in cuts if 0 < k - f <= 4 and k / fps <= ws[0]["s"]] if voice != out[-1]["voice"] else []
            if later:
                start = later[0]
            elif earlier:
                start = earlier[-1]
        if fixed is not None:
            start = max(int(fixed), out[-1]["start_f"] + 1) if out else int(fixed)
        out.append(dict(text=text, voice=voice, wipe=bool(wipe), start_f=start, first_word=ws[0]["s"], onset=on,
                        last_word_end=ws[-1]["e"], words=" ".join(str(w["t"]) for w in ws)))
    for a, b in zip(out, out[1:]):
        a["end_f"] = b["start_f"]
    out[-1]["end_f"] = end_frame
    for ch in out:
        if ch["end_f"] <= ch["start_f"]:
            sys.exit(f"yt_captions: chunk '{ch['text']}' has no frames")
        ch["start"], ch["end"] = round(ch["start_f"] / fps, 4), round(ch["end_f"] / fps, 4)
    json.dump(dict(fps=fps, frames=end_frame, chunks=out), open(os.path.join(job, "yt", "captions.json"), "w", encoding="utf-8"),
              indent=1, ensure_ascii=False)
    near = [(k, ch["start_f"]) for ch in out[1:] for k in cuts if 0 < abs(k - ch["start_f"]) <= 3]
    if near:
        print("yt_captions: cuts 1-3 frames off a chunk change (move a FREE cut onto it if no base joint is crossed): "
              + ", ".join(f"cut f{k} vs chunk f{f}" for k, f in near))
    print(f"yt_captions: {measured} of {len(out) - 1} chunk onsets measured on the voice track")
    wiped = sum(ch["wipe"] for ch in out)
    print(f"yt_captions: {len(out)} chunks, {wiped} wiped ({wiped / len(out):.0%}), mean {sum(ch['end_f'] - ch['start_f'] for ch in out) / len(out) / fps:.2f} s")


if __name__ == "__main__":
    main()
