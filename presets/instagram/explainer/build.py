#!/usr/bin/env python3
# /// script
# dependencies = []
# ///
"""
Caption-style preset builder (talking-head explainer).

Run it from the copy inside the job's hf-graphics/captions project after setting the
per-job block below:  uv run build.py

TIMING SOURCE OF TRUTH: the canonical transcribe-once transcript
(projects/<job>/outputs/<job>.transcript.json) — WhisperX large-v3 word timings
remapped through cuts.json. It is guaranteed to match the rendered audio, so
captions stay on-beat with zero manual adjusting. NEVER time captions off an
ad-hoc subset; that is what caused the back-half drift.

Emits a HyperFrames composition: a black Coolvetica box centered on the
graphics/face seam, pre-sized to each full phrase, words popping in on their own
word-level timestamps. Re-runnable — tweak the STYLE block and re-render.
"""
import json, html, re, math, pathlib, os
import sys
# Windows consoles/pipes default to cp1252, which can't encode the ⚠/→ glyphs in this
# script's status lines: a cosmetic print must never kill a pipeline step (it did once,
# 2026-08-13, mid-splice on a real Windows job). Force UTF-8; no-op on macOS/Linux.
for _s in (sys.stdout, sys.stderr):
    try:
        if (getattr(_s, "encoding", "") or "").lower().replace("-", "") != "utf8":
            _s.reconfigure(encoding="utf-8")
    except AttributeError:
        pass

HERE = pathlib.Path(__file__).parent


def _repo_root():
    """The repo root: the nearest ancestor holding transcript-corrections.json. This file runs from a
    COPY inside the job (projects/<job>/hf-graphics/captions/build.py) as often as from presets/, so a
    fixed parent depth is wrong half the time. Override with VIDEO_EDITOR_REPO."""
    env = os.environ.get("VIDEO_EDITOR_REPO")
    if env:
        return env
    for p in pathlib.Path(__file__).resolve().parents:
        if (p / "transcript-corrections.json").exists() or (p / "presets" / "caption-corrections.json").exists():
            return str(p)
    return str(pathlib.Path(__file__).resolve().parents[3])


REPO = _repo_root()
CORRECTIONS = f"{REPO}/transcript-corrections.json"
if not os.path.exists(CORRECTIONS):   # pre-2026-08-31 location
    CORRECTIONS = f"{REPO}/presets/caption-corrections.json"

# ===== SET PER JOB (the only lines you touch) ==============================
JOB        = f"{REPO}/projects/CHANGE-ME"                                 # the job folder
TRANSCRIPT = f"{JOB}/outputs/{pathlib.Path(JOB).name}.transcript.json"    # canonical source of truth
ALPHA      = True          # True = the step-5 overlay: transparent comp, rendered to renders/captions-alpha.mov
                           #        and placed on the top graphics track like any graphic (2026-09-04)
                           # False = burn onto BG for a flat look-check (the preview path, not the deliverable)
BG         = "assets/captions-bg.mp4"   # ALPHA=False only: the render to preview over, copied into this project
HOOK_END_T = None          # None = caption the WHOLE video; or set seconds to preview just the hook
# ===========================================================================

# ----- STYLE KNOBS (the locked preset) --------------------------------------
FONT_SIZE  = 49            # px
TEXT_COLOR = "#ffffff"
BOX_COLOR  = "#000000"
BOX_RADIUS = 14            # px
BOX_PAD    = "14px 24px"
ANCHOR_Y   = 960           # box vertical CENTER (px) = exact frame middle (1920/2). seam=960
UPPERCASE  = False         # natural case for v1

TAIL       = 0.50          # s to hold the final phrase after the last word ends

# chunking
MAX_WORDS  = 4
MAX_CHARS  = 24
GAP_BREAK  = 0.45          # pause (s) after a word forces a new chunk

# reveal
REVEAL        = "word"     # "word"   = each word pops in on its OWN word-level timestamp (on-beat),
                           #            inside a box PRE-SIZED to the full phrase (box never resizes)
                           # "phrase" = whole phrase pops in together at chunk start (no per-word sync)
PHRASE_STAGGER = 0.05      # s between words in "phrase" mode
WORD_FADE  = 0.13          # s per-word fade-in
WORD_RISE  = 6             # px rise
# box itself never animates — hard cut on/off, pre-sized to the full phrase
# ---------------------------------------------------------------------------

# ----- transcription fixes (display text only; source transcript untouched) -
cfg = json.load(open(CORRECTIONS))
AUTO = {k.lower(): v for k, v in cfg.get("auto", {}).items()}
FLAG = {w.lower() for w in cfg.get("flag", [])}
# optional per-job overrides — corrections.local.json next to this build.py, for
# context-specific calls (e.g. "school"→"YourBrand" in THIS video). Keeps the shared map conservative.
_local = HERE / "corrections.local.json"
if _local.exists():
    lc = json.load(open(_local))
    AUTO.update({k.lower(): v for k, v in lc.get("auto", {}).items()})
    FLAG = (FLAG | {w.lower() for w in lc.get("flag", [])}) - set(AUTO)
_split = re.compile(r"^(\W*)(.*?)(\W*)$")  # leading punct / core / trailing punct

def fix_word(text):
    pre, core, post = _split.match(text).groups()
    low = core.lower()
    if low in AUTO:
        return pre + AUTO[low] + post, ("auto", core, AUTO[low])
    if low in FLAG:
        return text, ("flag", core, None)
    return text, None

words = json.load(open(TRANSCRIPT))["words"]
words = [w for w in words if w.get("type", "word") == "word" and w["text"].strip()]
if HOOK_END_T is not None:
    words = [w for w in words if w["start"] < HOOK_END_T]

fixes, flags = [], []
for w in words:
    new, note = fix_word(w["text"])
    if note and note[0] == "auto":
        fixes.append((note[1], note[2])); w["text"] = new
    elif note and note[0] == "flag":
        flags.append(note[1])

COMP_DUR = round(words[-1]["end"] + TAIL, 2)

# group into chunks — respect clause/sentence punctuation so phrases read naturally
chunks, cur = [], []
for i, w in enumerate(words):
    cur.append(w)
    t = w["text"].rstrip()
    chars = sum(len(x["text"]) for x in cur) + (len(cur) - 1)
    gap_next = (words[i + 1]["start"] - w["end"]) if i + 1 < len(words) else 99
    ends_sentence = t.endswith((".", "!", "?"))
    ends_clause = t.endswith((",", ":", ";"))
    brk = (
        ends_sentence
        or (ends_clause and len(cur) >= 2)
        or len(cur) >= MAX_WORDS
        or chars >= MAX_CHARS
        or gap_next > GAP_BREAK
    )
    if brk:
        chunks.append(cur); cur = []
if cur:
    chunks.append(cur)

# build markup + timeline
caps_html, tl_js = [], []
for ci, ch in enumerate(chunks):
    start = ch[0]["start"]
    nxt = chunks[ci + 1][0]["start"] if ci + 1 < len(chunks) else COMP_DUR
    wspans = "".join(
        f'<span class="w" id="c{ci}w{wi}">{html.escape(w["text"])}</span>'
        for wi, w in enumerate(ch)
    )
    caps_html.append(f'<div class="cap" id="c{ci}"><div class="box">{wspans}</div></div>')
    # box: NO animation — hard ON at chunk start, hard OFF at next chunk (seek-safe)
    tl_js.append(f'tl.set("#c{ci}",{{opacity:1}},{start:.3f});')
    for wi, w in enumerate(ch):
        at = (start + wi * PHRASE_STAGGER) if REVEAL == "phrase" else w["start"]
        # words always occupy layout, so the box is pre-sized to the FULL phrase and
        # never resizes; each word just pops in (opacity + rise) on its own timestamp
        tl_js.append(
            f'tl.fromTo("#c{ci}w{wi} ",{{opacity:0,y:{WORD_RISE}}},'
            f'{{opacity:1,y:0,duration:{WORD_FADE},ease:"power2.out"}},{at:.3f});'
        )
    tl_js.append(f'tl.set("#c{ci}",{{opacity:0}},{nxt:.3f});')  # hard-kill, seek-safe

transform = "uppercase" if UPPERCASE else "none"
word_default_display = "inline-block"  # words always reserve space → box = full phrase width
caps_block = "\n        ".join(caps_html)
tl_block = "\n      ".join(tl_js)
body_bg = "transparent" if ALPHA else "#000"
bg_layers = "" if ALPHA else (
    f'<video id="bg" class="clip" src="{BG}" data-start="0" data-duration="{COMP_DUR}" data-track-index="0" muted playsinline></video>\n'
    f'      <audio id="bg-audio" src="{BG}" data-start="0" data-duration="{COMP_DUR}" data-track-index="10" data-volume="1"></audio>')

HTML = f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1080, height=1920" />
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
    <style>
      @font-face {{ font-family: "Coolvetica"; src: url("assets/fonts/Coolvetica-Rg.otf") format("opentype"); font-weight: 400; font-display: block; }}
      * {{ margin: 0; padding: 0; box-sizing: border-box; }}
      html, body {{ width: 1080px; height: 1920px; overflow: hidden; background: {body_bg}; }}

      /* caption rail — dead-centered (h + v) on the frame middle / graphics-face seam */
      .cap {{
        position: absolute; left: 540px; top: {ANCHOR_Y}px;
        transform: translate(-50%, -50%);
        opacity: 0; width: 1000px; text-align: center; pointer-events: none;
      }}
      .box {{
        display: inline-block; max-width: 1000px;
        background: {BOX_COLOR}; border-radius: {BOX_RADIUS}px;
        padding: {BOX_PAD};
        font-family: "Coolvetica", sans-serif; font-weight: 400;
        font-size: {FONT_SIZE}px; line-height: 1.04; letter-spacing: 0.5px;
        color: {TEXT_COLOR}; text-transform: {transform};
        white-space: nowrap;
      }}
      .w {{ display: {word_default_display}; opacity: 0; }}
      .w + .w {{ margin-left: 0.30em; }}
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="{COMP_DUR}" data-width="1080" data-height="1920" style="position: relative; width: 1080px; height: 1920px; overflow: hidden;">
      {bg_layers}

      <section id="captions" class="clip" data-start="0" data-duration="{COMP_DUR}" data-track-index="1">
        {caps_block}
      </section>
    </div>

    <script>
      window.__timelines = window.__timelines || {{}};
      const tl = gsap.timeline({{ paused: true }});
      {tl_block}
      window.__timelines["main"] = tl;
    </script>
  </body>
</html>
"""

(HERE / "index.html").write_text(HTML)

# report
print(f"source: {pathlib.Path(TRANSCRIPT).name}  |  COMP_DUR={COMP_DUR}s  (bg must be >= this)")
if fixes:
    print("auto-fixed:", ", ".join(f"{a}→{b}" for a, b in fixes))
else:
    print("auto-fixed: (none)")
if flags:
    print("⚠ REVIEW these in context:", ", ".join(sorted(set(flags))))
print(f"chunks: {len(chunks)}")
for ci, ch in enumerate(chunks):
    print(f"  {ci:2d} [{ch[0]['start']:5.2f}] " + " ".join(w["text"] for w in ch))
print("wrote index.html")
if ALPHA:
    print("render (the step-5 overlay, straight alpha):\n  npx hyperframes@0.8.16 render . -c index.html --fps 30 --quality standard "
          "--video-frame-format png --format mov --output renders/captions-alpha.mov")
else:
    print(f"render (flat preview over {BG}):\n  npx hyperframes@0.8.16 render . -c index.html --fps 30 --quality standard --output renders/captions-preview.mp4")
