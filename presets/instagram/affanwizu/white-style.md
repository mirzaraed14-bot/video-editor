# @affanwizu: "white" captions (MEASURED 2026-09-18)

The creator's second caption style, used on the comedic/commentary reels (oushi, petrol, Rain, SAFAI).
Font and size were **read out of the creator's own Premiere project** (ABW6: every white caption is an
Essential Graphics text layer set in Tahoma 48). Everything else was measured off four exports.
Builder: [`build.py`](build.py) `--style white`. Procedure: [`PLAYBOOK.md`](PLAYBOOK.md).

## The frame (the creator's, never ours)

Black 9:16 canvas. The footage fills a full-width window (e.g. y288 → y1605 on SAFAI, y285 → y1635 when
the 1920×1080 source is scaled 125 %), and the title sits in the black band just above it. We only add captions.

## The look

| | Value | How it was found |
|---|---|---|
| Font | **Tahoma** (regular), upright | named in ABW6's text layers; glyph IoU **0.82–0.83** vs the exports, dx 0 / dy 0 |
| Size | **48 px** at 1080 wide | ABW6 (48.0), confirmed by the fit (47 → 0.45, 49 → 0.47) |
| Colour | **white #FFFFFF** | reads (253,253,253) inside strokes after export |
| Shadow | **black 95 %, 4 px right / 3 px down, 2 px blur, 1 px spread** | fitted on 26 caption-switch frame pairs with no jump cut under them (error 8.85 → 6.34); the optimum is shallow, so neighbouring values look identical |
| Position | centred on x540 by advance width. **The baseline moves per reel**: oushi 1146, SAFAI 1140, petrol 1116, Rain 1096 | `--y`; default 1140 |
| Lines | one line; longest seen ~38 chars | |
| Motion | none: hard cut on, hard cut off | |

## Text rules (differ from the yellow style)

- **Mixed case.** Mostly lowercase; a line may start with a capital (`Politics ki jo`, `Poli science`).
- **ALL CAPS = shouted/emphasis lines**: `EXPERT OPINIONS`, `AAP BOL KYUN RAHE HO?`, `KAL PETROL BAND KARDO`, `3 GHANTAY BAAD`.
- **`?` is kept** on questions (`apki sunega kon?`, `na theek hai?`). No other punctuation. A word cut off
  mid-sentence gets a hyphen (`ga-`).
- Title: Title Case (`Political Genius Uncles At Mehfils`) or ALL CAPS, same font, white, above the window. The title is the creator's.

## Timing and phrasing

The same as the yellow style ([`deep-talks-style.md`](deep-talks-style.md) § Timing, § Phrasing):
switch on the first word, hold until the next line, never a gap, first line from frame 0.

## Placement (both styles)

Across 11 reference reels the caption baseline sits a median **chin + 115 px** (`workflows/chin-line.py`
→ `median_chin`); 5 of 11 are within 12 px of that. Close-ups and chest-down framings are the creator's
call (socccc sits over the mouth), so the value is a per-reel `--y`, stated in the review sheet.
