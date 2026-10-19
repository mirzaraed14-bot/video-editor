"""Check a caption job's transcript BEFORE writing a single line (PLAYBOOK § 2, Gates B + the ending rule).

usage: python presets/instagram/affanwizu/transcript_check.py projects/<job>
       (run after transcribe.sh and codeswitch_pass.py; re-launches itself in the WhisperX venv)

Prints, against an independent speech detector (Silero):
  DROP     a pause in words.json (> 1 s) that holds real speech: Whisper lost words there
  ENDING   speech after the transcript's last word: the ending was dropped or squeezed early
           (Seq 17, 20, 29, 51 — the most common failure on this channel)
  SILENCE  a pause with no speech at all (a timeline gap or a real pause): end the caption there with `@<sec> |`
  LOOP     the same three words 3+ times within 17 words
  LONG     one word over 0.9 s
and, for every DROP / ENDING / LOOP, what the English listener (transcript/codeswitch.json) heard in that window,
which is usually the missing text. Re-decode those windows wide (ur + en) before writing the lines.
"""
import glob, json, os, subprocess, sys


def _reexec():
    home = os.path.expanduser("~/.cache/video-editor/whisperx-venv")
    py = os.path.join(home, "Scripts", "python.exe") if os.name == "nt" else os.path.join(home, "bin", "python")
    if os.path.exists(py) and os.path.abspath(sys.executable).lower() != os.path.abspath(py).lower():
        sys.exit(subprocess.call([py, *sys.argv], env=dict(os.environ, PYTHONUTF8="1", PYTHONIOENCODING="utf-8")))
    sys.exit("transcript_check: needs faster-whisper (the WhisperX venv). Run transcribe.sh once to create it.")


try:
    import numpy as np
    from faster_whisper.vad import get_speech_timestamps, VadOptions
except ImportError:
    _reexec()


def main():
    job = sys.argv[1].rstrip("/\\")
    d = json.load(open(os.path.join(job, "transcript", "words.json"), encoding="utf-8"))
    ws = [w for c in d["clips"] for w in c["words"] if "start" in w]
    media = [p for e in ("mp4", "mov", "mkv", "m4v") for p in glob.glob(os.path.join(job, "raw", f"*.{e}"))][0]
    raw = subprocess.check_output(["ffmpeg", "-v", "error", "-i", media, "-map", "0:a:0", "-ac", "1", "-ar", "16000", "-f", "s16le", "-"])
    a = np.frombuffer(raw, np.int16).astype(np.float32) / 32768
    end = len(a) / 16000
    sp = [(t["start"] / 16000, t["end"] / 16000) for t in get_speech_timestamps(a, VadOptions(min_silence_duration_ms=120, speech_pad_ms=0))]
    cov = lambda x, y: sum(max(0.0, min(e, y) - max(s, x)) for s, e in sp)
    csp = os.path.join(job, "transcript", "codeswitch.json")
    cs = json.load(open(csp, encoding="utf-8"))["words"] if os.path.exists(csp) else []
    heard = lambda x, y: " ".join(w["w"] for w in cs if x - 0.3 <= w["start"] <= y + 0.3) or "(English listener: nothing)"
    word = lambda w: w.get("w", w.get("word", ""))
    issues = []
    prev = 0.0
    for w in ws + [{"start": end, "end": end, "w": ""}]:
        if w["start"] - prev > 1.0:
            c = cov(prev, w["start"])
            last = w["start"] >= end
            if c > 0.4:
                issues.append(("ENDING" if last else "DROP", prev, w["start"], f"{c:.1f}s of speech, no words"))
            elif not last:
                issues.append(("SILENCE", prev, w["start"], "no speech: end the caption here"))
        prev = w["end"]
    for i, w in enumerate(ws):
        tri = [word(x) for x in ws[i:i + 3]]
        if len(tri) == 3 and (i == 0 or [word(x) for x in ws[i - 1:i + 2]] != tri):
            win = [word(x) for x in ws[i:i + 17]]
            n = sum(win[k:k + 3] == tri for k in range(len(win) - 2))
            if n >= 3:
                issues.append(("LOOP", w["start"], ws[min(i + 17, len(ws) - 1)]["end"], f"'{' '.join(tri)}' x{n}"))
        if w["end"] - w["start"] > 0.9:
            issues.append(("LONG", w["start"], w["end"], f"'{word(w)}' {w['end'] - w['start']:.2f}s"))
    print(f"transcript_check  {os.path.basename(job)}: {len(ws)} words, last word ends {ws[-1]['end']:.2f}s, cut {end:.2f}s, "
          f"speech {sum(e - s for s, e in sp):.1f}s")
    for kind, x, y, note in sorted(issues, key=lambda t: t[1]):
        print(f"  {kind:<8} {x:7.2f}-{y:7.2f}  {note}")
        if kind in ("DROP", "ENDING", "LOOP"):
            print(f"           English listener: {heard(x, y)}")
    bad = [i for i in issues if i[0] in ("DROP", "ENDING", "LOOP")]
    print("  OK: transcript complete" if not bad else f"  {len(bad)} spot(s) to re-decode before writing captions")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
