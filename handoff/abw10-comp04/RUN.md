# RUN — ABW10 Linked Comp 04 (ABW9.aep)

## ▶ STATUS: resume here
**2026-10-17: CLEAN CAPS on comp 04**: his CapCut return `roadster2.mp4` (#2247, in "roadster2.mp4 Comp 1" → comp 04 L1) →
`roadster2_clean.mp4`; verify: caption pixels max change 5 (encode noise), lifted-black field ~46 % → ≤0.4 %
(`captions/capcut/verify_clean.txt`); #2247 re-pointed in place (MATCH; precomp layer 0.667–36.2 unchanged). ABW9 NOT saved.
**2026-10-17 (review fix): roadster.mov RE-RENDERED.** Affan: "fast are we talking" (not "is your system"), "how fast do you wanna
go", and some captions came in before the words. Fixed text in `captions/captions.txt` + flat words.json ("wanna" = want+to merged);
re-timed from the clean Premiere A1 dialogue (`seqref/a1.wav`, read from Sequence 05's A1 clips; 0 ms offset vs the render) and kept
the LATER start per word: 26 words moved, worst "FOR REAL?" 0.56 s early, "YES" / "WHAT ARE THEY" / "HOW FAST" / "YOU MAKE IT" ~0.3 s.
**2026-10-17: TRANSITIONS on ABW10 Linked Comp 04** from his labels (`zoom/labels_now04.tsv`): 15 = 4 Purple (−90) at 3.183 /
7.817 / 10.617 / 34.333, 4 Cyan blur at 5.683 / 13.617 / 20.067 / 23.933, 6 Dark Green (+30) at 6.517 / 9.083 / 18.567 /
22.333 / 26.467 / 28.833, 1 Peach at 20.883; Aqua blocks none; last block ignored. Log `transitions/transitions04.txt`;
comp now 55 layers. ABW9 NOT saved.
**2026-10-17: CAPTION EXPORT for ABW10 Sequence 05 (36.2 s, Rogan × Musk Roadster thrusters):
`E:\Shorts\Abudance Wisdom Shorts Exports\Caption Exports\roadster.mov`** (H.264 1080×1920 60 fps + PCM stereo, 36.2 s).
48 captions (6 stacked, max 3 words, Rogan's questions italic, F-word censored), `captions/captions.txt`; transcript from the
Topaz render's own audio (`captions/raw/seq05-reference.mov`), fix "Roots" → ROADSTER in `captions/flat/transcript/words.json`;
plan `make_plan.py … --hang 1.0` (the 28.6–34.4 no-speech stretch stays clean); sheet `captions/caps_sheet.jpg`.
Speaker split was inferred from the words (questions = Rogan), not checked on picture.
**2026-10-17: ZOOM PASS (BlurMoCurves) on ABW10 Linked Comp 04** (footage `Sequence 05_1_stab_chr2_iris3.mov`, 36.2 s, 20 blocks;
4 yellow = pull out: 9.08–10.62, 20.88–22.33, 22.33–23.93, 28.83–34.33): 20 `Adjustment Layer 29` zooms, 2 face pivots
(0–3.18 centre y722, 15.58–18.57 centre y715), every Z read back as planned (`zoom/zoom.txt`); fresh dump `zoom/after_comp04.tsv`:
40 layers (20 zooms + 20 footage). Preview `zoom/zoom-preview.jpg` (not reviewed, budget). Undo "Abundance Wisdom zoom pass (Claude)".
ABW9 NOT saved (Affan saves). Budget for this pass: ~$1.30–1.80 of credits.
