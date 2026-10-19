"""ig_captions.py: Instagram-look caption chunks (README § 5) from the cut's word timings -> the "chunks" list in <job>/ig/spec.json.

  python presets/youtube-shorts/onyx-samples/kit/ig_captions.py projects/<job>

Reads `<job>/ig/spec.json` → "captions": {"words": "outputs/<job>.transcript.json", "style": ..., "max_words": 4, "max_chars": 22,
"lead": 0.08, "hl": ["$20,000", "four"], "drop": [[44.31, "And"]], "breaks": [6.54]} and WRITES back "captions.chunks": [{text, start, end, hl}]. Sentence case kept from
the transcript; a chunk breaks at sentence punctuation, at a pause ≥ 0.35 s, and at the word/char caps; a chunk never ends
on "to/for/the/and/a/of"; numbers stay with their unit. Each chunk shows from `lead` s before its first word until the next
chunk starts (or 0.25 s after its last word if a longer pause follows). `hl` words get the highlight style. "breaks" (cut-timeline s)
force a chunk break there: a camera cut where the speaker changes mid-sentence (Rich Roll QA r1: "life, They're very" showed
Bryan's words while Rich was still talking).
v2 look ("captions.mode", batch 2): "stack" and "word" use their own chunker (v2_chunks below: per-word times, ONE hero per stack block);
"line" keeps this chunker and adds each word's time ("words": [[t0, t1, text, role]]) for the hero colour sweep. No mode = v1, unchanged.
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


STOP = WEAK_END | {"that", "this", "it", "it's", "you", "we", "they", "he", "she", "was", "are", "be", "have", "has", "had", "do", "so",
                    "if", "then", "there", "what", "when", "just", "like", "really", "very", "about", "from", "into", "because", "before",
                    "after", "they're", "we're", "you're", "there's", "that's", "would", "could", "should", "will", "how", "much", "did",
                    "does", "which", "other", "than", "things", "thing", "through", "literally", "basically", "actually", "going", "gonna"}
STACK_WEAK = WEAK_END | {"no", "not", "very", "so", "like", "than", "other", "who", "who's", "that", "if", "by"}   # never the last word of a block
NUM = re.compile(r"^(\$?\d[\d,.]*%?|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|fifteen|twenty|thirty|forty|fifty|sixty|"
                 r"hundred|thousand|million|billion|half|double|twice)$")


def v2_chunks(W, c, spec, hl, crosses):
    """The v2 modes (research § b, moves 4 and 5). Every chunk keeps each word's OWN time ("words": [[t0, t1, text, role]]): the words land
    exactly as they are spoken, the block itself never moves (one constant anchor, placed by ig_capy).
      stack  blocks of <= max_words (default 6) words; a block breaks on a sentence end, a comma (once it holds 3+ words), a pause
             >= 0.35 s, a forced break or a quote, and never ends on a weak word or on a number whose unit follows ("four | hours");
             ONE hero per block (the first `hl` word in it, else a number, else its longest content word): the research's "emphasis
             everywhere means emphasis nowhere" (Rich Roll had 37 highlighted words in 46 s). Shows from its first word until the
             next block starts (gaps under 1.2 s), else 0.5 s past its last word.
      word   one word at a time; a word under 0.18 s joins the next one (or the one before, at a sentence end), so nothing flashes.
    """
    mode, P = c["mode"], ".,!?;:\"“”'’"
    key = lambda w: w["t"].lower().strip(P)
    blocks, cur = [], []
    if mode == "stack":
        mw = c.get("max_words", 6)
        UNITS = {"hours", "hour", "minutes", "minute", "seconds", "days", "years", "dollars", "bucks", "percent", "million", "billion", "thousand"}
        for w in W:
            if cur:
                prev, gap = cur[-1], w["s"] - cur[-1]["e"]
                quote = prev["t"].endswith(",") and key(prev) in QUOTE_INTRO
                comma = prev["t"].endswith(",") and len(cur) >= 3
                if crosses(prev, w) or len(cur) >= mw or gap >= 0.35 or re.search(r"[.!?]$", prev["t"]) or quote or comma:
                    weak = key(prev) in STACK_WEAK or (NUM.match(key(prev)) and key(w) in UNITS)
                    if weak and len(cur) > 1 and gap < 0.35 and not crosses(prev, w) and not re.search(r"[.!?,]$", prev["t"]):
                        carry = cur.pop(); blocks.append(cur); cur = [carry]
                    else:
                        blocks.append(cur); cur = []
            cur.append(w)
        if cur:
            blocks.append(cur)
        merged = []                         # a 1-2 word scrap under 0.5 s joins the block before (it would flash as a lone line)
        for b in blocks:
            if merged and len(b) <= 2 and b[-1]["e"] - b[0]["s"] < 0.5 and len(merged[-1]) + len(b) <= mw + 1 and not crosses(merged[-1][-1], b[0]) \
                    and not re.search(r"[.!?,]$", merged[-1][-1]["t"]):
                merged[-1] = merged[-1] + b
            else:
                merged.append(b)
        blocks = merged
    else:
        i = 0
        while i < len(W):
            b = [W[i]]
            nxt = W[i + 1] if i + 1 < len(W) else None
            short = nxt is not None and nxt["s"] - W[i]["s"] < 0.18 and not re.search(r"[.!?]$", W[i]["t"]) and not crosses(W[i], nxt)
            if short:
                b.append(nxt); i += 1
            elif blocks and W[i]["e"] - W[i]["s"] < 0.18 and re.search(r"[.!?]$", W[i]["t"]) and len(blocks[-1]) == 1 and not crosses(blocks[-1][-1], W[i]):
                blocks[-1].append(W[i]); i += 1; continue
            blocks.append(b); i += 1
    out = []
    for j, b in enumerate(blocks):
        roles = ["lead"] * len(b)
        if mode == "stack":
            pick = next((k for k, w in enumerate(b) if key(w) in hl), None)
            if pick is None:
                pick = next((k for k, w in enumerate(b) if NUM.match(key(w)) and key(w) not in {"one"}), None)
            if pick is None:
                cand = [k for k, w in enumerate(b) if key(w) not in STOP and len(key(w)) >= 4]
                pick = max(cand, key=lambda k: (len(key(b[k])), k)) if cand else None
            if pick is not None and len(b) > 1:
                roles[pick] = "hero"
        else:
            roles = ["hero" if key(w) in hl else "lead" for w in b]
        start = max(0.0, b[0]["s"] - 0.03)
        nxt = max(0.0, blocks[j + 1][0]["s"] - 0.03) if j + 1 < len(blocks) else spec["frames"] / spec["fps"]
        hold = 1.2 if mode == "stack" else 0.6
        end = nxt if nxt - b[-1]["e"] < hold else b[-1]["e"] + (0.5 if mode == "stack" else 0.2)
        out.append(dict(text=" ".join(w["t"] for w in b), start=round(start, 3), end=round(min(end, nxt), 3),
                        hl=[w["t"].strip(P) for w, r in zip(b, roles) if r == "hero"],
                        words=[[round(w["s"], 3), round(w["e"], 3), w["t"], r] for w, r in zip(b, roles)]))
    return out


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
    if c.get("mode") in ("stack", "word"):                # the v2 look's animated caption modes (batch 2): their own chunker
        c["chunks"] = v2_chunks(W, c, spec, hl, crosses)
        json.dump(spec, open(sp_path, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
        n_hero = sum(1 for o in c["chunks"] for w in o["words"] if w[3] == "hero")
        print(f"ig_captions: {len(c['chunks'])} {c['mode']} chunks from {len(W)} words, {n_hero} hero words")
        return
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
        if c.get("mode") == "line":     # v2 `line` mode: the v1 chunks plus each word's own time (the hero colour sweep runs ON its word)
            out[-1]["words"] = [[round(x["s"], 3), round(x["e"], 3), x["t"], "hero" if x["t"].lower().strip(".,!?") in hl else "lead"] for x in ch]
    c["chunks"] = out
    json.dump(spec, open(sp_path, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    print(f"ig_captions: {len(out)} chunks from {len(W)} words (≤{mw} words / ≤{mc} chars), {sum(1 for o in out if o['hl'])} with highlights")


if __name__ == "__main__":
    main()
