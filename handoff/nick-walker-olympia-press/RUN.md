# RUN: nick-walker-olympia-press (Nick Walker after the 2026 Mr Olympia win: press conference + Tony Doherty interview)

▶ **CAPTIONS (2026-09-30): CAPTION TRACK ON ABW8 · Sequence 19, verified on screen.** 60 captions, max 3 words,
0.03 → 37.47 s wall to wall, ALL CAPS, no commas/full stops, 15 coloured (25 %). `captions/outputs/seq19-captions.srt`
+ cheat sheet `captions/caption-colours.md`. Grabs: 18.2 s "DON'T KNOW" (Nick's joke), 32.0 s *"THAT MOMENT"*.
- **Italic = the other speaker, decided by VOICE, not by reading:** the press-conference lines split into two voices
  (pyannote wespeaker embeddings compared within the recording). The man who opens "Well, Nick…" also says "You didn't
  even know who I was…" and "Well, you will Friday night, my friend"; Nick says "Seventh?", "I think you're still
  low-balling me", "Whatever you say" and the joke "I still don't know who you are" (the text alone suggested the
  reverse). His lines + Tony Doherty's question are italic; Nick, Bob (announcer) and the commentators upright, as Seq 09.
- One long hold: "LITTLE NERVOUS TOO" 3.3 s (24.06–27.37) over the finals-stage pause before "AND NEW" (wall to wall).
- Next: Upgrade Captions To Graphics → styles → pop → CapCut → clean the return (in place if already in AE).

▶ **TRANSITIONS (2026-09-30): APPLIED in `ABW7.aep` → ABW8 Linked Comp 34, read back. AE project NOT saved.**
11 from the creator's labels on layers 1–11 (no caption precomp yet, so on top): 2 purple dips (4.83, 23.03),
6 dark-green +30 (13.60, 19.08, 20.52, 27.18, 33.20, 35.40), 1 cyan blur (14.68), 2 peach uni.Exposure (26.25, 31.65).
The creator's zooms, footage and "Adjustment Layer 36" checked unchanged (`transitions/transitions34.txt`).

▶ **ZOOMS (2026-09-30): APPLIED in `ABW7.aep` → ABW8 Linked Comp 34, read back. AE project NOT saved** (undo group
"Abundance Wisdom zoom pass (Claude)"). 12 "Adjustment Layer 29" S_BlurMoCurves on layers 1–12 over the Topaz render
`Nick2_stab_chr2_iris3_prob4.mov` (37.98 s): 1 yellow pull-out (31.65), 11 push-ins, 5 face pivots. Block 9 (27.18–31.65,
the win, 0.70) is pinned at x 1000 / y 246 by `zoom/centers.override.json`: the camera follows Nick right, and a
centre-x push cut half his face off the right edge at 31.6 s (simulated at full depth, 8 samples: `x1000` keeps him
whole throughout). Next: the creator labels the blocks → transitions.

▶ **HEAD LOCK (2026-09-30): APPLIED in `ABW7.aep` → ABW8 Linked Comp 32 + 33, all 17 layers, proven. AE project NOT
saved** (undo group "Head lock (Claude)"). 1,761 per-frame Anchor keys + Motion Tile; read back from AE, every tracked
nose holds within 0.01 px (unlocked 1–166 px). Sequenced by the creator (no sequencing job here); comps read from AE.
- Comp 32 (23.03 s, 11 layers): `MR OLYMPIA PRESS CONFERENCE 2026 + POSEDOWN (4K).mp4` (1920×1080, 29.97) at 215 %,
  the creator's crops slid far left/right. Layers 1–6, 8, 9, 11 track Nick on the stage sofa; L7 (13.60–14.68) and
  L10 (19.08–20.52) are the other two athletes those crops show.
- Comp 33 (6.32 s, 6 layers): `2026 IFBB Olympia Weekend Tony Doherty Interviews NEW Mr Olympia Champion Nick Walker.mp4`
  at 214–240 %, moved down (y 1126–1241). L1 Nick in profile (nose near the crop's right edge, the creator's framing),
  L2–L4 Tony Doherty, L5–L6 Nick with the mic (L6 turns 123 px while talking; the lock holds it).
- Pre-check `brief/track_sheet.jpg` (dot on the right nose in all 17), proof `brief/headlock_proof.jpg`.
- Next: the creator saves, renders → Topaz.
