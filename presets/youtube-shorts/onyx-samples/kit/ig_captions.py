"""ig_captions.py: Instagram-look caption chunks (README § 5) from the cut's word timings -> the "chunks" list in <job>/ig/spec.json.

  python presets/youtube-shorts/onyx-samples/kit/ig_captions.py projects/<job>

Reads `<job>/ig/spec.json` → "captions": {"words": "outputs/<job>.transcript.json", "style": ..., "max_words": 4, "max_chars": 22,
"lead": 0.08, "hl": ["$20,000", "four"]} and WRITES back "captions.chunks": [{text, start, end, hl}]. Sentence case kept from
the transcript; a chunk breaks at sentence punctuation, at a pause ≥ 0.35 s, and at the word/char caps; a chunk never ends
on "to/for/the/and/a/of"; numbers stay with their unit. Each chunk shows from `lead` s before its first word until the next
chunk starts (or 0.25 s after its last word if a longer pause follows). `hl` words get the highlight style.
"""
import json, os, re, sys

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8")
    except Exception:
        pass

WEAK_END = {"to", "for", "the", "and", "a", "an", "of", "in", "on", "at", "with", "but", "or", "my", "your", "is"}


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
    mw, mc, lead = c.get("max_words", 4), c.get("max_chars", 22), c.get("lead", 0.08)
    hl = {h.lower().strip(".,!?") for h in c.get("hl", [])}
    chunks, cur = [], []

    def flush():
        if cur:
            chunks.append(list(cur)); cur.clear()

    for i, w in enumerate(W):
        if cur:
            text = " ".join(x["t"] for x in cur + [w])
            gap = w["s"] - cur[-1]["e"]
            if len(cur) >= mw or len(text) > mc or gap >= 0.35 or re.search(r"[.!?]$", cur[-1]["t"]):
                # don't end on a weak word: carry it into the next chunk when possible
                if cur[-1]["t"].lower().strip(".,") in WEAK_END and len(cur) > 1 and gap < 0.35:
                    carry = cur.pop(); flush(); cur.append(carry)
                else:
                    flush()
        cur.append(w)
    flush()
    out = []
    for i, ch in enumerate(chunks):
        start = max(0.0, ch[0]["s"] - lead)
        nxt = chunks[i + 1][0]["s"] - lead if i + 1 < len(chunks) else spec["frames"] / spec["fps"]
        end = nxt if nxt - ch[-1]["e"] < 0.6 else ch[-1]["e"] + 0.25
        text = " ".join(x["t"] for x in ch)
        out.append(dict(text=text, start=round(start, 3), end=round(end, 3), hl=[x["t"].strip(".,!?") for x in ch if x["t"].lower().strip(".,!?") in hl]))
    c["chunks"] = out
    json.dump(spec, open(sp_path, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    print(f"ig_captions: {len(out)} chunks from {len(W)} words (≤{mw} words / ≤{mc} chars), {sum(1 for o in out if o['hl'])} with highlights")


if __name__ == "__main__":
    main()
