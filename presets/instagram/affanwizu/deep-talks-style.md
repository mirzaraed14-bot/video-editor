# @affanwizu: "aesthetic deep talks" captions (LOCKED)

Measured off the creator's own export `balcony.mov` (1080×1920, 60 fps, 44 s, 43 lines) on
2026-09-18: by pixel measurement, glyph-overlap fitting and frame-exact switch detection, not by eye.
Builder: [`build.py`](build.py). Spelling: [`roman-urdu.md`](roman-urdu.md). Procedure: [`PLAYBOOK.md`](PLAYBOOK.md).

## The frame (the creator's, never ours)

Black 9:16 canvas; the footage sits in a full-width **1080×1300 window at y364 → y1664**. The title is at
the top in the caption style (baseline y332). The creator builds this frame and the title. We only
add captions ON their finished cut.

## 🔒 The look

| | Value | How it was found |
|---|---|---|
| Font | **Ubuntu Light**, slanted **0.18 (~10°) faux italic** | true Ubuntu Italic fits at IoU 0.42, Light + 0.18 slant at 0.81 (all 43 lines) |
| Size | **48 px** at 1080 wide | word positions within 1–2 px |
| Kerning | **on** (the font's GPOS pairs) | +0.02 IoU; fixes drift in long lines |
| Colour | **#FFD700** (gold), solid | reads (253,214,0) inside strokes after the h264 export |
| Shadow | **black, 3.75 px right / 4.25 px down, 1 px blur, 100 %** | fitted on 82 frame pairs either side of a caption switch (error 3.99 vs 6.10 with no shadow) |
| Position | centred on x540 (by advance width), **baseline y1178** (ascenders at y1141) | constant across all 43 lines |
| Lines | **one line**, never wrapped; longest seen 38 chars / 795 px | |
| Case | **all lowercase**, no punctuation, English words in English, digits for numbers | |
| Motion | **none**: hard cut on, hard cut off | |

## 🔒 Timing

- A line **switches on the start of its first word** (creator's switches sit a median 0.034 s from it,
  p90 0.12 s) and **holds until the next line starts**. There is never a gap and never an empty frame.
- The first line shows from **frame 0**. The last line holds to the **end of the cut** (all four reference reels;
  `build.py` holds it 0.4 s past the final word when the transcript reaches the end, to the end of the cut otherwise).
- Switches snap to the cut's frame grid (60 fps on balcony).
- **Re-confirmed 2026-10-01 on four finished reels** ([`reference/`](reference/README.md)): on Khayal the
  creator kept the switch time of every one of my 52 unchanged lines (all within one frame), and on
  balcony / BELIEVE / UNi their hand-placed switches sit within ±0.1 s of WhisperX's first-word start.
  211 lines, zero gaps, zero empty frames. **The rule is right; keep it.**
- **A caption that "hangs" over the next words is a TRANSCRIPT defect, not a timing one.** When Whisper
  drops a stretch of speech, the line before it holds until the next word Whisper did catch: on Sequence 15
  `aye age ni` stayed up 5.1 s while four lines of speech went by. The creator's own lines never carry more
  than **0.78 s of speech per word**; `caption_qa.py` fails any line over 0.45 s × words + 0.6 s.

## 🔒 Phrasing

A natural spoken phrase, usually **3–5 words** (range 1–6). Measured on 211 lines (2026-10-01): median
**4 words** (3 on BELIEVE, the fastest talker), 6 at most on the recent reels (balcony, the oldest, reached 8),
and only 5 % over 5 — the creator's own cap for us is **5**. A line is on screen a median **0.9 s**
(0.3 s → 2.3 s). Lines end most often on `hai` / `hain` / `mai` / `aap` / `ke`, and start on `aap` / `or` /
`aik` / `mai` / `wo`: they cut where the breath is, even if it leaves `aap` hanging at a line end
(`hona chahye ke aap` / `free hon financially`). A word said alone between pauses
(`to`, `jo`) gets its own line. Lines end where the speaker breathes: often on a trailing `ke` (that)
or a verb (`banunga`, `kardi`), never mid-verb-chain.

## Output

- **Burn** (default): the creator's cut with captions → `outputs/<job>.captioned.mp4` (h264, BT.709
  tagged like the source, audio re-encoded at AAC 256k).
- **Alpha** (`--alpha`): a transparent ProRes 4444 caption layer at the cut's size and rate, for their own timeline.

## Premiere caption track (the DEFAULT deliverable since 2026-09-19)

The creator wants captions they can **fix themselves**, so a reel ships as an editable Premiere caption
track, not a rendered layer: `build.py <job> --style yellow --srt --dur <sequence end>` → `<job>.srt`, dragged
onto the sequence at 00:00. Every line is then text in Premiere's Text panel. The look is a caption
**Track Style**, set once and saved as **"affanwizu yellow"**, then applied to each new reel in one click:

| Essential Graphics (captions selected) | Value |
|---|---|
| Font | Ubuntu · Light · **48** (confirmed in ABW6 on ameer) |
| Faux Italic | **OFF on the latest reel** (ameer, 2026-09-19, upright). balcony had it on (the 0.18 slant). Follow the latest: upright |
| Fill | **#FFD700** |
| Shadow | black · opacity 100 % · angle ~139° · distance ~6 · size 0 · blur ~3 (measured 3.75 px right / 4.25 px down, 1 px blur) |
| Align / position | centred; text just under the chin (the measured chin + ~115 px baseline, e.g. y1103 on dowry-beggars) |

The rendered layer (`--alpha`) stays available for a finished file, but it is no longer the default.
