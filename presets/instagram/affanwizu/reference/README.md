# @affanwizu caption ground truth

The creator's own captions, pulled frame-exact out of their finished exports (2026-10-01). Use them to check
any change to the caption pipeline against what the creator actually ships, instead of against memory.

| Reel | Lines | What it is |
|---|---|---|
| `balcony.captions.json` | 43 | typed by the creator (the reel the yellow look was measured on) |
| `BELIEVE.captions.json` | 59 | typed by the creator; upright, quoted speech, `bohat` build-up |
| `UNi.captions.json` | 40 | typed by the creator; heavy English (`over the course of`, `as such`, `recoup`) |
| `Khayal.captions.json` | 69 | **my** Sequence 15 lines after the creator's corrections: diff it against `projects/seq15-short/` |

Each line: `t0` / `t1` (seconds, frame-exact at 60 fps) and `text` exactly as on screen.

**Adding a reel:** `uv run extract_captions.py <export.mov> <out_dir>` finds the yellow caption band, logs every
switch, and writes contact sheets (one crop per caption, labelled). Read the text off the sheets, one line per
caption, then write `<reel>.captions.json` in the same shape. The band search assumes the caption sits between
y950 and y1500 (`--y0 / --y1` otherwise) and the yellow (#FFD700) style; for the white style, change `yellow()`.

**Checking a pipeline change:** make an `.srt` of a reel from `<reel>.captions.json`, put it next to the reel's
audio in `<job>/raw/`, and `caption_qa.py` must still PASS (it did on all four: the hanging-caption limit sits
above every line the creator ever wrote).
