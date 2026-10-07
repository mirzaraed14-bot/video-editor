"""ig_captions.py: Instagram-look caption chunks (README § 5) from the cut's word timings -> the "chunks" list in <job>/ig/spec.json.

  python presets/youtube-shorts/onyx-samples/kit/ig_captions.py projects/<job>

Reads `<job>/ig/spec.json` → "captions": {"words": "outputs/<job>.transcript.json", "style": ..., "max_words": 4, "max_chars": 22,
"lead": 0.08, "hl": ["$20,000", "four"], "drop": [[44.31, "And"]], "breaks": [6.54]} and WRITES back "captions.chunks": [{text, start, end, hl}]. Sentence case kept from
the transcript; a chunk breaks at sentence punctuation, at a pause ≥ 0.35 s, and at the word/char caps; a chunk never ends
on "to/for/the/and/a/of"; numbers stay with their unit. Each chunk shows from `lead` s before its first word until the next
chunk starts (or 0.25 s after its last word if a longer pause follows). `hl` words get the highlight style. "breaks" (cut-timeline s)
force a chunk break there: a camera cut where the speaker changes mid-sentence (Rich Roll QA r1: "life, They're very" showed
Bryan's words while Rich was still talking).
"""
import json, os, re, sys

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8")
    except Exception:
        pass

WEAK_END = {"to", "for", "the", "and", "a", "an", "of", "in", "on", "at", "with", "but", "or", "my", "your", "is", "i", "our", "their", "his", "her"}
QUOTE_INTRO = {"like", "said", "says", "goes", "go", "asked", "asks", "went"}   # "she's like," / "I go," open quoted speech


def load_words(path):
    d = json.load(open(path, encoding="utf-8"))
    ws = d["words"] if isinstance(d, dict) and "words" in d else d.get("words_patched", d) if isinstance(d, dict) else d
    out = []
    for w in ws:
        if w.get("type", "word") != "word":
            continue
        out.append(dict(t=str(w.get("text") or w.get("t") or w.get("word")).strip(), s=float(w.get("start", w.get("s"))), e=float(w.get("end", w.get("e")))))
    return [w for w in out if w["t"]]


def main():
    job = os.path.abspath(sys.argv[1])
    sp_path = os.path.join(job, "ig", "spec.json")
    spec = json.load(open(sp_path, encoding="utf-8"))
    c = spec["captions"]
    W = load_words(os.path.join(job, c["words"]))[c.get("skip_words", 0):]
    # "drop": [[t, "word"], ...]: words the transcript places inside a kept segment that are NOT in the audio (a mis-timed
    # WhisperX word at a boundary, verified by slice-ASR); matched by text within 0.06 s
    drop = c.get("drop", [])
    W = [w for w in W if not any(abs(w["s"] - t) <= 0.06 and w["t"].strip(".,!?").lower() == str(x).strip(".,!?").lower() for t, x in drop)]
    mw, mc, lead = c.get("max_words", 4), c.get("max_chars", 22), c.get("lead", 0.08)
    hl = {h.lower().strip(".,!?") for h in c.get("hl", [])}
    breaks = c.get("breaks", [])
    crosses = lambda a, b: any(a["s"] < t <= b["s"] + 0.05 for t in breaks)      # a forced break lies between word a and word b
    chunks, cur = [], []

    def flush():
        if cur:
            chunks.append(list(cur)); cur.clear()

    for i, w in enumerate(W):
        if cur:
            text = " ".join(x["t"] for x in cur + [w])
            gap = w["s"] - cur[-1]["e"]
            prev = cur[-1]["t"]
            quote = prev.endswith(",") and prev.strip(",").lower() in QUOTE_INTRO   # "she's like," / "I go,": a quote starts, break before it
            if crosses(cur[-1], w):
                flush()
            elif len(cur) >= mw or len(text) > mc or gap >= 0.35 or re.search(r"[.!?]$", prev) or quote:
                # don't end on a weak word: carry it into the next chunk when possible
                if cur[-1]["t"].lower().strip(".,") in WEAK_END and len(cur) > 1 and gap < 0.35:
                    carry = cur.pop(); flush(); cur.append(carry)
                else:
                    flush()
        cur.append(w)
    flush()
    # QA r1 (Rob Dial): a number and its unit stay together ("thousand | dollars." split), and a one-word chunk that would
    # flash for under ~0.3 s ("now?", "owe me?") joins the chunk before it
    merged = []
    for ch in chunks:
        w0 = ch[0]["t"].strip(".,!?").lower()
        short = len(ch) <= 2 and (ch[-1]["e"] - ch[0]["s"]) < 0.30
        unit = merged and re.search(r"\d|thousand|hundred|million|billion", merged[-1][-1]["t"].lower()) and w0 in {"dollars", "bucks", "percent", "thousand", "million", "billion", "years", "days"}
        if merged and (short or unit) and not crosses(merged[-1][-1], ch[0]) and len(" ".join(x["t"] for x in merged[-1] + ch)) <= mc + 8:
            merged[-1] = merged[-1] + ch
        else:
            merged.append(ch)
    chunks = merged
    out = []
    # a chunk that opens after a forced break waits for the cut (the lead would show it over the other speaker's last frames)
    starts = [max([0.0, ch[0]["s"] - lead] + [t for t in breaks if i and chunks[i - 1][-1]["s"] < t <= ch[0]["s"] + 0.05])
              for i, ch in enumerate(chunks)]
    for i, ch in enumerate(chunks):
        start = starts[i]
        nxt = starts[i + 1] if i + 1 < len(chunks) else spec["frames"] / spec["fps"]
        end = nxt if nxt - ch[-1]["e"] < 0.6 else ch[-1]["e"] + 0.25
        text = " ".join(x["t"] for x in ch)
        if i == 0 or re.search(r"[.!?]$", chunks[i - 1][-1]["t"]):      # sentence case: a chunk that opens a sentence is capitalised
            text = text[:1].upper() + text[1:]
        out.append(dict(text=text, start=round(start, 3), end=round(end, 3), hl=[x["t"].strip(".,!?") for x in ch if x["t"].lower().strip(".,!?") in hl]))
    c["chunks"] = out
    json.dump(spec, open(sp_path, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    print(f"ig_captions: {len(out)} chunks from {len(W)} words (≤{mw} words / ≤{mc} chars), {sum(1 for o in out if o['hl'])} with highlights")


if __name__ == "__main__":
    main()
