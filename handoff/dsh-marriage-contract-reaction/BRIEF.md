# dsh-marriage-contract-reaction: Affan's reaction to our Digital Social Hour (Sean Kelly) samples (ABW10 "Digital Social Hour reaction")

## ▶ STATUS: resume here
- **2026-10-19 PREPARED IN ABW10** ("Digital Social Hour reaction", bin "Onyx batch 3 reactions (2026-10-19)"): **168.42 s (2:48.4)**,
  49 segments; razored (34 razors at 23 edges), layout 91 clip edits (--layout-check 0 leaks at keys, 7 between-key slips max 2.90 px,
  `anim_kps=60`), V3 showcase frames / V4 MG (20 events) / V5 captions, house chain +9 dB into −6 dBFS on all 49 A1 clips, 41 SFX
  (A2 28, A4 13), Snowbrain bed on A3 at −19.2 dB from 5.704 s (its sustained entrance; placed 1 frame long, trimmed to 168.4167
  by ExtendScript), 25 ms ramps at the hard sample edges 19.8 / 23.1 / 98.98 / 103.53 / 109.72 / 129.3 / 143.62 / 148.17, --verify 0 problems.
  Proof: `work/grabs-sheet.jpg`. He exports.
- Inputs: OBS `raw/2026-10-19 07-56-27.mp4`; camera C1386 (−5.548 s, −28 ppm). He played (VLC): yt v3 + ig ig2 → master-file cards
  (`../dsh-marriage-contract/outputs/…sample-yt.v3.mp4` from 0 and from 25.62, `…sample-ig.ig2.mp4`).
- **2026-10-19 (later): "1.29 million … million" was NOT a stumble.** Forced alignment with the number SPELLED OUT fits the plain
  sentence best ("one point two nine" 224.88-226.39, ONE "million" 226.71, 0.81; every two-million variant scores 0.11-0.25) and
  Whisper hears one "million": the second "million" was a tightasr hallucination, and wav2vec2 cannot align digits ("1.29").
  Nothing was cut. The caption was fixed instead (ops: phantom first "million" out, "1.29" re-timed to 48.30-49.81), rendered to
  `overlays/captions-r2.mov` (Premiere held captions.mov) and relinked with projectItem.changeMediaPath; captions.mov now holds the
  same content. --verify 0 problems, proof re-grabbed.
- **Face x is SET BY HAND** (facex.py hit the leather chair on 9 of 11 beats): after every build_plan.py + facex.py run:
  `tools3/facefix.py plan.json 0.0=1132 10.72=1104 53.90=1075 94.10=921 96.65=921 97.87=921 137.35=1005 139.08=1060 154.37=1113
  155.98=1113 156.50=1113` (camera grids work/grid-face*.jpg).

## The cut (keep.json → author3 → splice/polish → jointcheck ×3 → pins ×4 → seqmap3 → tightasr → tightwords3)
- Kept: intro, the title read, name + 600M "views to short form", "a statement, not a title", their Short 3.3 s, the audio (Shure
  mics, mixer, earbud sound), 3-line captions vs one line / four words, 1.29M subscribers yet no value, the editor's job, how the clip
  was made (19 s + a caption), what a viral short needs (hook, route to payoff, payoff, the middle = value), no solution / cut off,
  no music, OUR YouTube cut in two passes (0-4.55 his first start; 25.62-45.20), his read of it ("trap", "talking to men", the
  debate start to end), "that's how a viral short is made", OUR Instagram cut 4.55 s (REORDERED before his "take a look… Instagram
  version" line), more minimalistic / subtle, "if Sean wants to upload this" (REORDERED after the Instagram comment), sign-off.
- Pins: `work/pins.json` (round 1), `pins2.json` (business, line, take-2 "the", short, samples' z, yeah / right / uh out), `pins3.json`
  ("right" out after "the hook", "here" restored), `pins4.json` ("form" restored). The ambiguous ones were decided by
  `tools3/falign.py` (forced alignment) and `tools3/endtest.py` (Whisper on each candidate end), not by the free ASR times.
- Captions: `work/tightwords.ops.json` (shift for the "form" pin, form inserted, title / Shure / payoff, the double "million",
  a hallucinated "right" / "at" / "listen" / "uh" removed) + corrections (Afan. → Affan.).

## Look (Reaction I): see build_plan.py docstring. Hero = what a viral short needs, drawn ON their Short: a gold scrub along its own
progress bar with a tick as each part starts (hook, route, payoff) under a three-step build (the one card allowed past 6 s, lifted to
y 640 so the bar stays visible). PT Serif Italic, rise entrances, pop-soft + thud-low on cards, tick-glass on selects. Voice +9 dB
(his talk −26.4 LUFS).

## Download log
| # | File | Source | Size | Why |
|---|---|---|---|---|
| a1 | `assets/channel-avatar.jpg` | yt3.googleusercontent.com s900 (URL from `_onyx-batch3-2026-10/dsh/meta/*flat.json`) | — | channel card |
| a2 | `audio/ES_Snowbrain - Shiruky.wav` | Epidemic Sound recording 701297a6-757f-442f-86a7-c763788fd219 (WAV, full) | 62 MB | the bed (never used before; −11.7 LUFS) |
