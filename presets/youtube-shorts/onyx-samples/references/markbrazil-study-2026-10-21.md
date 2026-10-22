# @markbrazil (Mark Mastrandrea, Open Residency): frame-by-frame study, 2026-10-21

Asked by Affan on 2026-10-21 ("analyze mark brazil's style frame by frame ... scan his last 10 reels") as the candidate look for
the Instagram variant of the Scott D. Clary Short `projects/_client-scott-clary/marvel-board-vs-rdj/`. This file extends the
2026-10-12 notes on him in [batch2-style-research.md](batch2-style-research.md) (row 8 and moves 7, 8, 13): those are confirmed
here, with numbers added and two corrections (caption position, red colour).

**Method.** All 13 reels came from the built-in browser, logged out. Each reel's 1080x1920 VP9 stream (from the page's own DASH
manifest) was loaded into a muted, off-screen, never-played `<video>` and drawn to a canvas. Nothing was saved except the key
frames below. **Every frame was scanned** (23.976 fps, 10,300 frames). The scan recorded a luma-difference signal per frame
(cuts, plus graphic entrances by screen region), mean luma, and dark rows every 0.5 s. Type positions and sizes come from
bright-pixel row bands on full-resolution frames. Colours are medians of the text pixels. Animation timings come from
1-frame strips. Audio was decoded in memory (OfflineAudioContext) and **never played**: levels and bands only.
Fonts were identified by eye at 1:1, so treat them as "closest bundled match". Key frames are in
[`markbrazil-shots/`](markbrazil-shots/), cited as (01)…(25).

## The reels

| Reel | Posted | Views (grid) / likes | Length | Style |
|---|---|---|---|---|
| [DeuGMx5txc5](https://www.instagram.com/reel/DeuGMx5txc5/) | 2026-10-20 | 34K / 1,448 | 38.0 s | **Signature** (pyramid diagram, neon serif, lower-third) (03, 04) |
| [DerhiiUNdTx](https://www.instagram.com/reel/DerhiiUNdTx/) | 2026-10-19 | **178K** / 9,621 | 39.0 s | **Signature**, fastest cut (01, 02) |
| [DeXASMKN7kg](https://www.instagram.com/reel/DeXASMKN7kg/) | 2026-10-11 | n/a / 1,653 | 42.2 s | **Editorial B-roll collage** (Robert Greene: paper, archival, red serif) (05, 06) |
| DecKhuRtHMA, DecK4K2tbcz, DecLBFpNCfu, DecL9suNyXJ, DecMKOONTSQ, DecMTbtNi-D, DecMa1ntKR4 | all 2026-10-13, within 16 min | 399 to 5,299 / 5 to 77 | 15 to 44 s | **Plain trial-reel batch**: back-catalogue episodes, talking heads, small captions, a hook title, a mono lower-third CTA, few graphics (07 to 11) |
| Pinned [DRkNaS3DldC](https://www.instagram.com/reel/DRkNaS3DldC/) | 2025-11-27 | **1.8M** / 68K | 36.9 s | **Signature** (the benchmark) (11, 20 to 22) |
| Pinned [DMIeizEseFK](https://www.instagram.com/reel/DMIeizEseFK/) | 2025-07-15 | 988K / 34K | 40.0 s | Older: red label boxes, no neon (12) |
| Pinned [DP_yUcvjXie](https://www.instagram.com/reel/DP_yUcvjXie/) | 2025-10-19 | 556K / 23K | 34.9 s | **Signature** (12) |

Read the seven 10-13 reels as **one** sample: a batch of back-catalogue clips (trial reels, judging by 5-77 likes) cut in a
cheaper template. Their low numbers say nothing about the signature look. No editor is credited in any caption.
The signature look is what earned 1.8M, 556K and 178K, and it is the look this file measures.

## The signature look in one line

**A dark, spotlit studio shot used as a stage for type.** The wide two-shot leaves the top half of the frame empty. Small
white sans words build up there one by one, then one word lands huge in a red neon serif italic. Close-ups carry only tiny
captions. Orange light-leak burns hit the scene changes. A thin monospace tag with a red bar names the show.

## 1. Canvas, stage and shots

- **Full-bleed 9:16, no letterbox** in all 13 reels: dark rows at the top and bottom are only the studio's falloff,
  never bars.
- **The stage shot.** A locked-off, symmetric wide: two people at a table under a top spotlight, a grey-slate gradient
  background (median `#48505C`), a floor glow, and a horizon line. The people sit at y ≈ 880-1250, the top ≈ 45 % is empty.
  It recurs all through the reel: ~30 % of runtime on DerhiiUNdTx, ~45 % on DeuGMx5txc5, ~35 % on DRkNaS3DldC.
- **Close-ups and mediums** are static (no push-ins or punch-ins were seen in the sheets; there was no dedicated test for
  them), dark, and shot on a shallow lens.
- **Stacked split** (21): the wide shot on top (y 0-672, ~35 %), the close-up below (~65 %), separated by a dark gap, not a
  coloured seam. Used once per reel at most.
- **Cut rhythm** (cut = 1-frame luma jump):

| Reel | Cuts / 10 s | Median shot | 90th pct shot |
|---|---|---|---|
| DRkNaS3DldC 1.8M | 3.8 | 1.88 s | 6.05 s |
| DP_yUcvjXie 556K | 2.9 | 3.25 s | 5.88 s |
| DerhiiUNdTx 178K | **11.0** | **0.71 s** | 2.13 s |
| DeuGMx5txc5 | 2.6 (+3.9 graphic events / 10 s) | 2.46 s | 7.67 s |
| DeXASMKN7kg (B-roll) | 11.4 | 0.33 s | 2.17 s |
| Plain 10-13 batch | 1.5-3.9 | 2.2-5.4 s | 4-11 s |

  The 2025 hits run 3-4 cuts per 10 s. His newest designed reel is much faster (11 per 10 s): screen-share and B-roll
  inserts every half-second.

## 2. Type system (the core of the look)

Three voices, a 3-4x jump in size between them (all px on the 1080x1920 frame):

| Voice | Font (closest bundled) | Size | Colour | Where |
|---|---|---|---|---|
| **Caption** (every spoken word) | Inter Semibold/Bold, sentence case, full punctuation | line band 41-46 px ⇒ **~44-48 px font** | white `#FDFFFF` + a soft white glow; one or two words per line in the red serif | centred (x 539). **2025 hits: one fixed y** on close-ups, **y 1212** (top of line; p50 = p90 = 1212 on DRkNaS and DP_yUc). **Oct 2026: it varies**, median y 920-1004 (DeuG mostly 920-927; DerhiiUNdTx anywhere from 659 to 1243). On the stage shot it drops **below the table** (y ≈ 1250-1390) |
| **Lead-in / tail line** (the words around a hero) | Inter Semibold | 40-46 px | white + glow | left-aligned at **x ≈ 96** over the stage's empty top (DRkNaS), or centred (DerhiiUNdTx) |
| **Hero word / number** | **Playfair Display Bold/Black Italic** (high contrast, ball terminals) for words and money; a heavy grotesk for some numbers (DerhiiUNdTx "$1,000,000") | **~150-160 px** (red band 170-190 px incl. glow), nearly full width (x 70 → 1010); 3-line stacks at ~120-130 px, line pitch ~170 px | red with neon bloom: **2025 coral `#FF6471`** (glow `#955B69`); **Oct 2026 pure `#FF0505`** (glow `#7F1B1F`) | top half of the stage shot (y ≈ 330-830), or inline in a close-up caption |

- **Caption build** (15): words appear **on their spoken word** and accumulate into 1-3 short lines (median line width
  250-450 px, 2-5 words). Each word fades in over **2 frames** (~60 % opacity, then 100 %). There is no slide, no scale and
  no bounce. The block clears at the sentence end.
- **Hero entrance** (16): the red word **cuts in fully formed**, then its glow **blooms over 2-3 frames** (a neon tube
  striking). It holds 0.6-1.5 s.
- **List swap** (20): one white word stays fixed ("No") while the red word below it swaps every **~0.7 s**
  (Girlfriends. → Going Out. → Television. → Nothing.). Each swap is a **letter-scramble decode lasting 3-4 frames**.
- **Number re-roll** (21): "$7 million" changes to "$95 million" in place, the lead-in and tail lines unchanged.
- **Stage diagram** (19, DeuGMx5txc5): above the heads, a translucent red triangle that fills as he talks. A thin white
  vertical axis line carries two tiny serif-italic labels ("unsaturated" / "saturated"). The caption stays below the table.
  Thin, elegant, one accent colour.

## 3. Name card, lower-third, end card

- **Guest name card** (18, 19; DerhiiUNdTx 7.4-8.6 s): the guest in a **black-and-white**, soft close-up profile. The
  NAME is in red caps, **tracked very wide (~1 em)**, across the middle (y ≈ 976, nearly full width), with neon glow. The
  letters **flicker on one by one over ~8 frames (0.33 s)**, some with vertical blur, in random order.
- **Monospace lower-third** (23-25): a **red vertical bar** beside two lines of thin mono white: the show name in caps
  ("OPEN RESIDENCY") and a smaller second line ("Full Conversation on YouTube"). Measured: the whole block spans x 223-775,
  y 1325-1529. Estimated from the 1:1 crop: bar ~6 px wide, name ~48 px light mono, second line ~30 px. Entrance (measured frame by frame): the bar **glitch-flickers on over 2-3 frames**, then
  the text **decodes from random letters, left to right, in ~5 frames**. Total ≈ 7 frames (0.29 s). Placed late (32 s of
  38). The plain batch uses the same tag for its CTA ("COMMENT 'TYLER'").
- **End card**: black, a small mono "OPEN RESIDENCY", held ~3.5 s, fading to black (DerhiiUNdTx ends on 6 frames of pure black).

## 4. Transitions and opener

- **Light-leak burn** (17), only on a change of scene or source: 5 frames of full-frame **orange → red → yellow → yellow →
  orange** overexposure over the outgoing shot, a cut, then **red vertical light streaks** sweeping the incoming shot for
  3 frames. ≈ 8 frames (0.33 s) in all. The incoming shot is often the B&W name card.
- **Opener** on both 2025 hits (20): the stage shot under an orange-red leak that **wipes off left to right in ~6 frames**,
  with a bright yellow leading edge. Measured luma ramp: 102 → 137 → 158 → 202 → **231** → 121 → 79 (peak at frame 5,
  ~0.2 s). The hero list starts on frame 3. DeuGMx5txc5 opens on 2 bright leak frames. DerhiiUNdTx opens on 6 black
  frames, then the flash.
- **Motion-blur whip** into screen-share and UI inserts (DerhiiUNdTx 10.2 s). Inserts sit on **white** (a phone screenshot,
  a logo on white) or as a dark dashboard composited over the stage's empty top.

## 5. Grade

Dark and low-key. Median frame luma is 27-39 of 255 on the studio reels (73 on the white-shirt guest). Saturation is
moderate to low (median HSV S 0.18-0.31). The palette is neutral-cool (the stage background is slate blue-grey), with no
teal-orange. The only saturated colour on screen is the red type and its glow. The B&W name card is the mood shift.

## 6. Sound (measured, not heard: Affan's silence rule)

- **Music bed: confirmed on DerhiiUNdTx only.** There the sound **carries on after the last word, under the end card, at
  -16 to -21 dB RMS, then fades over ~1.5 s** to silence. On the other reels a bed is **unconfirmed**: the sub-band energy
  measured on DRkNaS3DldC was taken during speech, and a male voice reaches below 120 Hz. DeuGMx5txc5's pauses drop to
  -33 to -43 dB, so any bed there is very low.
- Speech sits around -15.5 to -16 dB RMS (20 ms frames), peaks -0.1 to -4.6 dBFS. The mix is loud and dense.
- **Sound effects can't be separated from the voice by measurement.** No broadband burst rises above the bed at the
  light-leak burns or the lower-third. Whatever SFX he uses are subtle. Our standing rule (a crisp, audible SFX on every
  graphic) stays ours, not his.

## 7. What changed from 2025 to now

The red went from coral `#FF6471` to pure `#FF0505`. Close-up captions moved up from y 1212 to y ~920-1000. The cut got 3x
faster on the newest reel, with more inserts (screen share, logos, UI). The stage-type idea, the neon serif, the mono tag and
the light leaks are unchanged. The 2025 hits are the proven version.

## 8. Taking it to the Marvel IG Short (proposal, pending Affan's OK)

- **His look needs a stage; Peter's footage is a close webcam.** So the stage has to be **built**: a dark slate gradient with a
  top spotlight cone and a floor glow, used as the type canvas for the hook, "$525 million", the collateral beat and "$4.5
  billion". Peter's cam appears as a framed panel on that stage, or as the close-up beat with small captions. The other
  option is to use the HQ stills (Iron Man, the mug shot, the HBS cover) as the canvas, B&W with red type, like his name card.
- **Keep from him:** 44-48 px word-by-word Inter captions with a 2-frame fade; one red Playfair Black Italic hero per beat with
  a 2-3 frame glow bloom; the B&W name card look (PETER CUNEO, wide-tracked red, flicker-on) as the restyled credit, in the same 0-3 s slot; the mono
  red-bar tag for "FORMER MARVEL CEO"; the orange light-leak burn only where the source changes; a dark, neutral-cool grade.
- **The built stage is a type backdrop only.** Peter is never composited into a fake studio ("document, don't manufacture").
- **Affan's rules win where the two disagree:**
  - captions carry only `! ?` and quotes (he uses full punctuation);
  - captions sit at ONE constant y per video, just under the lips (he moves them below the table on the wide shot);
  - every split gets the white separator line, with the captions on it (his stacked split uses a dark gap);
  - SFX on every graphic;
  - no music bed unless asked (Scott jobs: none);
  - every picture is sharp (his name card is a soft, shallow-focus profile: keep the B&W and the red type, drop the softness);
  - this job's review: Peter's own cam at frame 0, and the credit (FORMER MARVEL CEO / PETER CUNEO) from 0 to ~3 s.
    The name card can restyle that credit; it cannot replace it or move it.
- **Open decision for Affan: black bars or full-bleed.** His 2026-10-12 Instagram direction asks for big cinematic bars;
  Mark is full-bleed in all 13 reels. The built stage resolves both: Peter's cam as a framed panel on a black, spotlit stage
  gives the cinematic black surround, fixes the too-close webcam, and leaves the empty top for the type. The alternative
  is full-bleed, exactly like Mark.
- **Pacing target:** his 2025 hits (3-4 cuts per 10 s plus a type event every ~2 s). DerhiiUNdTx's 11 per 10 s comes from
  screen-share inserts this story doesn't have.
