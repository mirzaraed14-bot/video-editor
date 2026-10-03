"""@affanwizu caption QA: the gate a caption job must pass before the .srt goes to the creator.

usage: python caption_qa.py projects/<job> [--srt <file>]
       (runs inside the WhisperX venv for the Silero speech detector; re-launches itself there if needed)

Calibrated 2026-10-01 on the creator's own 211 lines (Khayal, balcony, BELIEVE, UNi:
reference/*.captions.json). Checks, in order of how badly they hurt a reel:

  FAIL  hanging caption  speech under a cue > 0.45 s x words + 0.6 s. The creator's worst line is
                         0.78 s/word; a line over the limit is showing over words that aren't in it
                         (Whisper dropped them). Seq 15 shipped one: "aye age ni" held 5.1 s over
                         four lines of speech.
  FAIL  uncaptioned      speech inside a deliberate caption gap (an empty '@<sec> |' line), before the
                         first caption or after the last (Seq 17 lost its whole closing sentence).
  WARN  connector        an Urdu word Whisper writes INSTEAD of the creator's English connector
                         (ایسا for "doesn't mean", ایسی طرح for "it's just that", خاص طور for
                         "especially" ...). Listen; caption what was SAID.
  WARN  ENGLISH         an English word the code-switch pass heard (transcript/codeswitch.json, from
                         codeswitch_pass.py) that the caption on screen at that moment doesn't show:
                         the Urdu pass translated or dropped it. Caption what he SAID.
  WARN  loop            the same three words 3+ times within 15 words of the transcript: Whisper looping,
                         and real speech is usually missing right after it (Seq 11, Seq 26).
  WARN  long word        one transcript word > 0.9 s: a merged repeat or a translated phrase.
  WARN  spelling        a split or formal form the creator never types (SPELLING below, counted on
                         their own 142 lines: "aap ko" 0 vs "aapko" 5, "aur" 0 vs "or" 6 ...).
                         --fix rewrites captions.txt with them (prints every change; rebuild after).
  WARN  >5 words.

Exit 1 on any FAIL.
"""
import glob, json, os, re, subprocess, sys

def _reexec_in_whisperx_venv():
    home = os.path.expanduser("~/.cache/video-editor/whisperx-venv")
    py = os.path.join(home, "Scripts", "python.exe") if os.name == "nt" else os.path.join(home, "bin", "python")
    if os.path.exists(py) and os.path.abspath(sys.executable).lower() != os.path.abspath(py).lower():
        env = dict(os.environ, PYTHONUTF8="1", PYTHONIOENCODING="utf-8")
        sys.exit(subprocess.call([py, *sys.argv], env=env))
    sys.exit("caption_qa: needs faster-whisper (the WhisperX venv). Run transcribe.sh once to create it.")

try:
    import numpy as np
    from faster_whisper.vad import get_speech_timestamps, VadOptions
except ImportError:
    _reexec_in_whisperx_venv()

PER_WORD, SLACK = 0.45, 0.6
SPELLING = [   # split / formal form → how the creator types it (reference/*.captions.json, 2026-10-01)
    (r"\baap ko\b", "aapko"), (r"\baap ke\b", "aapke"), (r"\baap ka\b", "aapka"), (r"\baap ki\b", "aapki"),
    (r"\baap ne\b", "aapne"), (r"\bjis mai\b", "jisme"), (r"\bis mai\b", "isme"), (r"\bus mai\b", "usme"),
    (r"\bis ka\b", "iska"), (r"\bis ke\b", "iske"), (r"\bis ki\b", "iski"), (r"\bis ko\b", "isko"),
    (r"\bus ka\b", "uska"), (r"\bus ke\b", "uske"), (r"\bus ki\b", "uski"), (r"\bus ko\b", "usko"),
    (r"\bus ne\b", "usne"), (r"\bin ko\b", "inko"), (r"\bin ka\b", "inka"), (r"\bin ke\b", "inke"),
    (r"\bin ki\b", "inki"), (r"\baur\b", "or"), (r"\bkya\b", "kia"), (r"\bliye\b", "lye"),
    (r"\bchahiye\b", "chahye"), (r"\bhazaar\b", "hazar"), (r"\blakh\b", "lac"), (r"\bkar do\b", "kardo"),
    (r"\bkar lo\b", "karlo"), (r"\bho gaya\b", "hogya"), (r"\bho gya\b", "hogya"), (r"\bkar rahe\b", "karhe"),
]

def respell(txt):
    out = txt
    for pat, new in SPELLING: out = re.sub(pat, new, out)
    return out
CONNECTORS = {   # Whisper's Urdu stand-in → what the creator actually says (seen in his reels)
    "ایسا": "doesn't mean / it's not like", "ایسی طرح": "it's just that", "اسی طرح": "it's just that / etc",
    "خاص طور": "especially", "خاص کر": "especially", "شاید": "most likely / maybe", "لیکن": "but",
    "یقین": "believe me", "ویسے": "by the way", "بہرحال": "anyway", "مثال کے طور": "for example",
    "وجہ": "the reason … is because", "فرق نہیں": "no offense", "حقیقت": "that's a fact",   # Seq 26
}

def spoken_words(txt):
    """Words as SAID: '250,000' is "two hundred fifty thousand", 'SL' is "es el"."""
    n = 0
    for t in txt.replace("“", "").replace("”", "").split():
        digits = re.sub(r"\D", "", t)
        if digits:
            v = int(digits); sig = len(digits.rstrip("0")) or 1
            n += sig + (v >= 100) + (v >= 1000)
        elif t.isupper() and 1 < len(t) <= 4:
            n += len(t)
        else:
            n += 1
    return n

NUMBER_WORDS = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven",
                "twelve", "fifteen", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety",
                "hundred", "thousand", "million", "lakh", "lac"}

def english_misses(cues, cs_words, pad=0.4):
    """Runs of English words heard by the code-switch pass that no caption on screen at that time contains."""
    import difflib
    norm = lambda t: re.sub(r"[“”\"!?.,،۔]", "", t.lower().replace("’", "'"))
    out, run = [], []
    def flush():
        if run:
            on = [c for c in cues if c[0] < run[-1]["end"] + pad and c[1] > run[0]["start"] - pad]
            out.append((run[0]["start"], " ".join(w["w"] for w in run), " / ".join(c[2] for c in on)))
            run.clear()
    for w in cs_words:
        tok = norm(w["w"]).strip("'")
        dur = w["end"] - w["start"]
        if not re.search(r"[a-z]", tok) or len(tok) < 2 or tok in NUMBER_WORDS:
            flush(); continue
        if w.get("prob", 1) < 0.2 or dur < 0.03 or dur > 1.5:
            continue          # prompt leakage looks like this: "video script" at p 0.00, 0 s or 2.7 s long (Seq 15)
        on = [norm(c[2]) for c in cues if c[0] < w["end"] + pad and c[1] > w["start"] - pad]
        words = [x for t in on for x in t.split()]
        squashed = " ".join(on).replace(" ", "")
        hit = tok in words or tok.replace(" ", "") in squashed or any(
            difflib.SequenceMatcher(None, tok, x).ratio() >= 0.8 for x in words)
        if hit: flush()
        else: run.append(w)
    flush()
    return out

def srt_cues(p):
    cues = []
    for b in open(p, encoding="utf-8").read().strip().split("\n\n"):
        L = b.strip().split("\n")
        if len(L) < 3 or " --> " not in L[1]: continue
        f = lambda s: int(s[:2]) * 3600 + int(s[3:5]) * 60 + float(s[6:].replace(",", "."))
        a, z = L[1].split(" --> ")
        cues.append((f(a), f(z), " ".join(L[2:]).strip()))
    return cues

def speech(media):
    raw = subprocess.check_output(["ffmpeg", "-v", "error", "-i", media, "-map", "0:a:0", "-ac", "1", "-ar", "16000", "-f", "s16le", "-"])
    a = np.frombuffer(raw, np.int16).astype(np.float32) / 32768
    ts = get_speech_timestamps(a, VadOptions(min_silence_duration_ms=120, speech_pad_ms=0, threshold=0.5))
    return [(t["start"] / 16000, t["end"] / 16000) for t in ts]

def main():
    job = sys.argv[1].rstrip("/\\")
    if "--fix" in sys.argv:                       # rewrite captions.txt in the creator's spelling, then stop
        p = os.path.join(job, "captions.txt"); lines = open(p, encoding="utf-8").read().split("\n")
        for i, l in enumerate(lines):
            if "|" in l and not l.lstrip().startswith("#"):
                k, t = l.split("|", 1); nt = respell(t)
                if nt != t: print(f"  {t.strip():<34} → {nt.strip()}"); lines[i] = k + "|" + nt
        open(p, "w", encoding="utf-8").write("\n".join(lines)); print("captions.txt respelled: rebuild the .srt"); return
    srt = sys.argv[sys.argv.index("--srt") + 1] if "--srt" in sys.argv else None
    srt = srt or next(iter(sorted(glob.glob(os.path.join(job, "*.srt")), key=os.path.getmtime, reverse=True)), None)
    media = [p for e in ("mp4", "mov", "mkv", "m4v") for p in glob.glob(os.path.join(job, "raw", f"*.{e}"))]
    if not srt or not media: sys.exit(f"caption_qa: need <job>/*.srt and <job>/raw/<cut> (srt={srt}, media={media})")
    cues, sp = srt_cues(srt), speech(media[0])
    cover = lambda t0, t1: sum(max(0.0, min(e, t1) - max(s, t0)) for s, e in sp)
    fails, warns = [], []
    for t0, t1, txt in cues:
        n = spoken_words(txt); c = cover(t0, t1)
        if c > PER_WORD * n + SLACK:
            fails.append(f"{t0:7.2f}-{t1:6.2f}  HANGING  {c:.2f}s of speech under {n} word(s) ({c / n:.2f}s/word, limit "
                         f"{PER_WORD * n + SLACK:.2f}s): \"{txt}\"  → words are missing here; re-decode this span")
        if len(txt.split()) > 5: warns.append(f"{t0:7.2f}  {len(txt.split())} words (max 5): \"{txt}\"")
        if respell(txt) != txt: warns.append(f"{t0:7.2f}  SPELLING  \"{txt}\" → \"{respell(txt)}\"")
    # speech in a deliberate gap (time between one cue's end and the next cue's start)
    edges = sorted((a, b) for a, b, _ in cues)
    end = max(e for _, e in sp) if sp else 0
    if edges and cover(edges[-1][1], end + 1) > 0.3:      # speech after the last caption ends
        fails.append(f"{edges[-1][1]:7.2f}-{end:6.2f}  UNCAPTIONED  {cover(edges[-1][1], end + 1):.2f}s of speech after the last caption")
    if edges and cover(0, edges[0][0]) > 0.3:
        fails.append(f"   0.00-{edges[0][0]:6.2f}  UNCAPTIONED  {cover(0, edges[0][0]):.2f}s of speech before the first caption")
    for (a0, a1), (b0, b1) in zip(edges, edges[1:]):
        if b0 - a1 > 0.05 and cover(a1, b0) > 0.3:
            fails.append(f"{a1:7.2f}-{b0:6.2f}  UNCAPTIONED  {cover(a1, b0):.2f}s of speech inside a caption gap")
    words = os.path.join(job, "transcript", "words.json")
    if os.path.exists(words):
        d = json.load(open(words, encoding="utf-8"))
        ws = [w for c in d.get("clips", []) for w in c.get("words", [])] if isinstance(d, dict) else d
        ws = [w for w in ws if "start" in w and "end" in w]
        for i, w in enumerate(ws):
            tok = w.get("w", w.get("word", ""))
            two = tok + " " + (ws[i + 1].get("w", ws[i + 1].get("word", "")) if i + 1 < len(ws) else "")
            for k, eng in CONNECTORS.items():
                if tok == k or two.startswith(k + " ") or two == k:
                    warns.append(f"{w['start']:7.2f}  CONNECTOR  Whisper wrote '{k}': he often says \"{eng}\" here. Listen.")
                    break
            tri = [x.get("w", x.get("word", "")) for x in ws[i:i + 3]]
            if len(tri) == 3 and (i == 0 or [x.get("w", x.get("word", "")) for x in ws[i - 1:i + 2]] != tri):
                win = [x.get("w", x.get("word", "")) for x in ws[i:i + 15]]
                hits = sum(win[k:k + 3] == tri for k in range(len(win) - 2))
                if hits >= 3:
                    warns.append(f"{w['start']:7.2f}  LOOP  '{' '.join(tri)}' x{hits} within 15 words: Whisper looping; "
                                 f"re-decode {w['start'] - 1:.1f}-{ws[min(i + 15, len(ws) - 1)]['end'] + 4:.1f}s wide")
            if w["end"] - w["start"] > 0.9:
                warns.append(f"{w['start']:7.2f}  LONG WORD  '{tok}' {w['end'] - w['start']:.2f}s: a merged repeat or a translated phrase")
    cs = os.path.join(job, "transcript", "codeswitch.json")
    if os.path.exists(cs):
        for t, eng, shown in english_misses(cues, json.load(open(cs, encoding="utf-8"))["words"]):
            warns.append(f"{t:7.2f}  ENGLISH  heard \"{eng}\" · caption shows \"{shown}\"")
    else:
        warns.append("   --    no transcript/codeswitch.json: run codeswitch_pass.py so English gets checked")
    print(f"caption_qa  {os.path.basename(srt)}  cues {len(cues)}  speech {sum(e - s for s, e in sp):.1f}s")
    for f in fails: print("  FAIL", f)
    for w in sorted(set(warns)): print("  warn", w)
    print("  PASS" if not fails else f"  {len(fails)} FAIL(s): fix before hand-off")
    sys.exit(1 if fails else 0)

if __name__ == "__main__":
    main()
