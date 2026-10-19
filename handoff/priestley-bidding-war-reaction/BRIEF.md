# priestley-bidding-war-reaction: Affan's reaction to our Daniel Priestley samples (ABW10 "Daniel Priestley reaction")

## ▶ STATUS: resume here
- **2026-10-19 PREPARED IN ABW10** ("Daniel Priestley reaction", bin "Onyx batch 3 reactions (2026-10-19)"): **168.35 s (2:48.4)**,
  54 segments; razored (28 razors at 24 edges), layout 94 clip edits (--layout-check 0 leaks at keys, 11 between-key slips max
  2.92 px, `anim_kps=60`), V3 showcase frames / V4 MG (19 events) / V5 captions, house chain +8 dB into −6 dBFS on all 54 A1 clips,
  42 SFX on A2 + A4, "Rich (Instrumental Version)" bed on A3 at −17.5 dB from 0.244 s, 25 ms ramps at the hard sample edges
  19.02 / 23.2 / 91.58 / 126.48 / 141.6 / 145.4, --verify 0 problems. Proof: `work/grabs-sheet.jpg`. He exports.
- Inputs: OBS `raw/2026-10-19 07-42-37.mp4`; camera C1385 (+33.376 s, −26 ppm). He played (VLC): yt v5 + ig ig3 → master-file cards
  (`../priestley-bidding-war/outputs/…sample-yt.v5.mp4`, `…sample-ig.ig3.mp4`).
- **Face x is SET BY HAND** (facex.py locked onto the leather chair in EVERY beat, x 221-527; his face is at 908-1076): after every
  build_plan.py + facex.py run: `tools3/facefix.py plan.json 0.0=908 6.18=908 25.30=1029 71.17=1076 74.05=1076 76.12=1076 77.52=1076
  79.47=1076 126.48=1057 157.50=1057 159.73=1057 160.68=1057` (measured on camera grids, work/grid-face.jpg).

## The cut
- Kept: intro, name + 600M, the title read aloud (description closed: the feed cuts it off), "very big title", their Short 4.2 s, "no
  hook in this… not Daniel's fault… the job of the clipper", how he finds a hook (forward / backward, a statement), "just a clip with
  captions", the wrong title + people misled, **his live retitle in Notepad ("Billionaire on the great AI revolution")**, YouTube
  dynamic vs Instagram minimal, OUR YouTube cut 0-34.9 s (graft at sample 3.77: his first start + his full play), his verdict,
  OUR Instagram cut 3.8 s, minimal / premium / no zoom-ins, the sign-off.
- Captions: tightasr per stretch + `work/tightwords.ops.json` (if you do so → happy to do so, base → basically; forced alignment
  `tools3/falign.py` scored 'happy' 0.99 vs 'if' 0.49) + corrections (Priestly → Priestley).

## Look (Reaction H): see build_plan.py docstring. Hero = the retitle carried through: COMPLETELY WRONG on the Short's burned-in
title → Notepad framed while he types → the new title set ON the Short (mock_title on the paused frame, mid-low under its own
caption, where our samples carry their hook). Crimson Text Italic, wipe entrances, shutter-film on selects, whoosh-soft + thud-thin
on cards. Voice +8 dB (his talk −25.3 LUFS). Review fixes before render: a spotlight on the whole player had no room for its tag
(→ the opening frame's top half), the closed-description view was pushed in to the cut-off title, Notepad's left edge framed.

## Download log
| # | File | Source | Size | Why |
|---|---|---|---|---|
| a1 | `assets/channel-avatar.jpg` | yt3.googleusercontent.com s900 (URL from `_onyx-batch3-2026-10/priestley/meta/*flat.json`) | — | channel card |
| a2 | `audio/ES_Rich (Instrumental Version) - Mindme.wav` | Epidemic Sound recording d34c8a2b-1f65-49e3-9efb-0a06b99e58c3 (WAV, full) | 50 MB | the bed (never used before; −13.3 LUFS) |
