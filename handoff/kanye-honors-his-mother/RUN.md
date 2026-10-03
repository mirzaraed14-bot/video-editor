# RUN: kanye-honors-his-mother (Kanye West honours his late mother as he wins Best Rap Album, GRAMMYs 2008)

▶ **CAPCUT RETURN CLEANED IN PLACE (2026-10-02): `yeeee.mp4` → `yeeee_clean.mp4`, swapped inside `ABW7.aep`, NOT saved.**
The caption export sits precomposed in ABW8 Linked Comp 39 ("yeeee.mp4 Comp 1", Deep Glow etc.); footage item #3863
re-pointed at the cleaned file (undo group "Clean CapCut caption export (Claude)"), every effect and the precomp kept.
Cleaned 18 lifted-black frames (5, 119, 239 … every ~2 s) + the chroma runs after each 10 s mark; same size, 60 fps,
2,148 frames, range. Original `yeeee.mp4` untouched. `captions/capcut/yeeee_replace.jsx` / `.txt`.

▶ **TRANSITIONS (2026-10-02): APPLIED in `ABW7.aep` → ABW8 Linked Comp 39, read back. AE project NOT saved.**
10 from the creator's labels on layers 2–11, directly under the caption precomp (`yeeee.mp4 Comp 1`): 4 purple dips
(2.88, 6.33, 9.48, 26.58), 1 peach uni.Exposure (16.77), 5 dark-green +30 (18.95, 21.80, 23.80, 28.98, 35.80). None
after the Aqua block, the red "Black Solid 1" or the sandstone "Pre-comp 1". Every creator layer checked unchanged.
The first run put the 6.33 dip on 2.88 (the black solid was read as a block): template fixed, re-run cleaned its own.

▶ **ZOOMS (2026-10-02): APPLIED in `ABW7.aep` → ABW8 Linked Comp 39, read back. AE project NOT saved** (undo group
"Abundance Wisdom zoom pass (Claude)"). 12 "Adjustment Layer 29" S_BlurMoCurves on layers 1–12 over the Topaz render
`Sequence 23_stab_chr2_iris3_prob4.mov` (39.33 s): 4 yellow pull-outs (18.95, 21.80, 35.80, 37.77), 8 push-ins, 6 face
pivots. Block 6 (18.95, the head bow, 0.70 pull-out) pinned at y567 by `zoom/centers.override.json`: YuNet found no face
behind the sunglasses with the head down, and the centre pivot cut the glasses at the top. Block 7 is the letterboxed
audience shot (comp 37 L1): the pull-out widens its black bands, the creator's yellow. Next: labels → transitions.

▶ **CAPTIONS (2026-10-02): CAPTION TRACK ON ABW8 · Sequence 23, verified on screen.** 41 captions, max 3 words, ALL CAPS
in the style pass, no commas/full stops, 16 coloured (39 %), the narrator italic. `captions/outputs/seq23-captions.srt`
+ cheat sheet `captions/caption-colours.md`. Grabs: 1.2 s "YOU GONNA PLAY", 5.0 s *"KANYE WEST"* (narrator).
- Built from the LIVE cut (37.77 s, 16 A1 clips: Kanye + the ElevenLabs narrator "Oliver Silk" 2.9–11.1 s), checked
  unchanged right before import. WhisperX lost Kanye under the play-off music; each clip re-decoded with context from
  the source: + "Come on, you gonna play music on me?" (0–2.1) and "mother, I appreciate all the support. I appreciate
  all the prayers. It would be in good taste to stop the music then." (11.1–16.5). 16.8–23.8 = music/applause only
  (the source's "Um, I appreciate" is in the cut-out part), left uncaptioned via `make_plan.py --hang 0.8`.
  The invented leading "I" at 23.8 dropped (the clip starts inside "appreciate"). Fixes: `words.json` `_fixes`.
- Next: Upgrade Captions To Graphics → styles → pop → CapCut → clean the return (in place if already in AE).

▶ **HEAD LOCK (2026-10-02): APPLIED in `ABW7.aep` → ABW8 Linked Comps 35–38, 10 of 11 layers, proven. AE project NOT
saved** (undo group "Head lock (Claude)"). 1,488 per-frame Anchor keys + Motion Tile; read back from AE, every tracked
nose holds within 0.01 px (unlocked 19–331 px). Sequenced by the creator; comps read from AE (`brief/ae_comps3538.txt`).
- Source: `E:\Bullshit Folder\Henry\Watch Kanye West Honor His Late Mother As He Wins Best Rap Album In 2008 _ GRAMMY
  Rewind.mp4` (1920×1080, 29.97), every locked layer at 196 %, Position 428/1007 (the creator's framing).
- **Left alone: comp 37 L1 (0–2.00, src 113.05) at Scale 100 = letterboxed** (PLAYBOOK § 2 step 6: Motion Tile would
  fill the bands). Waiting on the creator: lock as is, or "fill the frame and lock" like Nick Walker comp 22.
- **Big real moves:** Kanye bows his head at the start of comp 36 L1 and L3; the lock holds the face, so the picture
  slides up to 459 px (comp 36 L3) and 201 px (L2) on screen. Pre-check `brief/track_sheet.jpg`: the dot on his nose
  in all 10.
- Next: the creator's answer on comp 37 L1, then render → Topaz.
