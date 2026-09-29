# RUN: paris-jackson-masks ("why did Michael make his kids wear masks?")

▶ **CAPCUT RETURN CLEANED IN PLACE (2026-09-29): `kid2.mp4` → `kid2_clean.mp4`, swapped inside `ABW7.aep`, NOT saved.**
The caption export was already precomposed in ABW8 Linked Comp 31 ("kid2.mp4 Comp 1" with Deep Glow etc.), so the
footage item (#3354) was re-pointed at the cleaned file (Replace Footage, undo group "Clean CapCut caption export
(Claude)"); every effect and the precomp stay. Cleaned 24 lifted-black frames (5, 119, 239 … every ~2 s) + the chroma
runs after each 10 s mark; same size, 60 fps, 2,844 frames, range. Original `kid2.mp4` untouched.

▶ **TRANSITIONS (2026-09-29): APPLIED in `ABW7.aep` → ABW8 Linked Comp 30, read back. AE project NOT saved.**
13 from the creator's labels on layers 1–13 (no caption precomp yet, so on top of the zooms): 6 purple dips, 2 cyan
blurs, 1 pink flash (4.40), 2 peach uni.Exposure (15.80, 33.97), 2 dark-green +30 (21.17, 35.52). None after the
Aqua blocks (10.70, 45.82). Zooms and footage checked unchanged (`transitions/transitions30.txt`, `after_comp30.tsv`).

▶ **ZOOMS (2026-09-29): APPLIED in `ABW7.aep` → ABW8 Linked Comp 30, read back. AE project NOT saved** (undo group
"Abundance Wisdom zoom pass (Claude)"). 16 "Adjustment Layer 29" S_BlurMoCurves on layers 1–16, spans = the blocks:
3 yellow pull-outs (4.40, 15.80, 45.82), 13 push-ins, 9 face pivots. The two wides on Alex (1.38, 8.87) are pinned to
the centre by `zoom/centers.override.json`: the detector took the portrait painting on the wall for the top face.
The comp carries the creator's B-roll (Michael + the masked kid 4.40–6.92, the photo band 15.80–18.12, the family
photo 33.97–35.52). Next: the creator relabels the blocks → transition pass.

▶ **RESTORED AFTER A POWER CUT (2026-09-29): head lock + captions re-applied, NOT YET SAVED by the creator.**
The unsaved AE and Premiere work was lost. Re-read both apps first: comps 26–29 and Sequence 14 came back IDENTICAL
to what was built (`brief/ae_comps2629.before-powercut.txt`, `captions/brief/tracks.before-powercut.txt`), with no
keys and no .srt, so the same verified `headlock2629.jsx` and `seq14-captions.srt` were re-applied. Head lock read
back: 25 layers, worst drift 0.02 px. Captions: one caption track (C1), "WEAR MASKS" on screen at 6.3 s.
**Save both projects (ABW7.aep, ABW8.prproj) before anything else.**

▶ **CAPTIONS (2026-09-29): CAPTION TRACK ON ABW8 · Sequence 14, verified on screen.** 82 captions, max 3 words,
0.05 → 47.40 s wall to wall, ALL CAPS, italic for Alex's question (1–23), no commas/full stops, 24 coloured (29 %).
`captions/outputs/seq14-captions.srt` + cheat sheet `captions/caption-colours.md`. Grabs: 6.3 s *"WEAR MASKS"*,
45.3 s "I'M TAKING THEM" in quotes. Built from the creator's LIVE cut (26 A1 clips, 47.4 s: V1 = the head-locked
comps 26–29, raw clips on V2 in the gaps), voice rebuilt and re-transcribed (`captions/`); one fix in
`words.json` `_fixes`: "mask?" → "masks?". Median 0.54 s (dense dialogue, 202 words under the 3-word cap).
Next: Upgrade Captions To Graphics → styles → pop → CapCut → **`clean_capcut.py` on the CapCut return before AE**.

▶ **HEAD LOCK (2026-09-29): APPLIED in `ABW7.aep` → ABW8 Linked Comp 26–29, all 25 layers, proven. AE project NOT
saved** (undo group "Head lock (Claude)"). 2,462 per-frame Anchor keys + Motion Tile (the two edge-pinned wides at
tile width 111); read back from AE, every tracked nose holds within 0.02 px (unlocked 11–90 px). The comps are the
creator's current cut (0–41.0 s), including the V2 listening shot (comp 26 L1). Pre-check sheet
`brief/track_sheet.jpg` (dot on the speaker's nose, in the creator's crop), proof `brief/headlock_proof.jpg`.
- The tracker was fixed first: it sampled frames the way ffmpeg's fps filter does (nearest), not the way AE shows
  them (at or before), and read Alex's face on the listening shot's last frame (a 131 px jump). LESSONS.
- Next: the creator saves, renders → Topaz. Captions: Sequence 14.

▶ **OPENING SHOT (2026-09-29, after the creator's pass): V2 = Paris LISTENING, CHD 35:05.733–35:07.100, 0–1.383 s,
picture only, verified frame-exact.** The creator's pass (47.77 s, pauses tightened, B5 in/out moved) is untouched,
including their own opening placeholder on V1 (CHD 3:44.55 at 100 %), which the V2 shot covers exactly.
- Chosen from a whole-episode search: 424 shots; a voice classifier (Alex vs Paris, 91 % agreement with the camera)
  found every moment the camera is on Paris while ALEX speaks; the podcast never holds her longer than ~1.5 s.
  35:05 is the one where her eyes are on Alex, mouth closed, serious (two short lowered-eye blinks). Others: smiles
  (1:15, 55:05), looking down (41:38, 48:15, 69:08), eyes closed (4:26, 69:38).
- Framing 177.867 %, position X 0.3044 (face at 0.562). Premiere's program frames 0, 1, 82 match the shot's first
  and last frames (1.00); frame 83 is the creator's wide. `cover_3505b.jsx`, scan tools in `brief/tools/`.

▶ **STATUS (2026-09-29): SEQUENCED on ABW8 · Sequence 14. Read back, audio proven.** 19 clips on V1+A1 and one
picture-only cover on V2, 0 → **53.12 s**, 5 markers (one per beat: card, on-screen text and warnings in the
comments). Built from the creator's pasted 5-beat script. Project NOT saved by us. Next, per PLAYBOOK: the
creator's pass, then head lock → Topaz → captions.

| | |
|---|---|
| Channel / preset | Abundance Wisdom → `presets/youtube-shorts/abundance-wisdom/` |
| Project | Premiere `ABW8.prproj` → **Sequence 14** (1080×1920, 60 fps), bin **"Pairs Masks"** (sic) |
| Sources | CHD `E:\Bullshit Folder\KIDS\Paris Jackson- Love, Loss, & Listening to Your Intuition.mp4` (1920×1080, 23.976) · Take Two `E:\Bullshit Folder\Henry\The Michael Jackson Interview TAKE TWO_ … 4K UPSCALE_2.mp4` (1440×1080 4:3, 25 fps) |

## The cut (from the read-back)
| beat | tl | on screen | words |
|---|---|---|---|
| 1 question | 0.00–14.63 | **V2: Paris, silent** (0–3.15) → Alex → wide on Alex (9.40–11.70) → Alex → Paris (0.23 s) | Alex: "Something that I feel like so many people were obsessed with … okay, put on your masks?" (one continuous clip) |
| 2 Paris answers | 14.63–25.00 | Paris → Alex listening (23.53–25.00) | "I mean, it just it made sense … Chuck E. Cheese … no one will know who you are. Like that, that made sense to me. But it really pissed the press off." |
| 3 Michael | 25.00–35.62 | Michael (Take Two, his own camera) | "I don't want people seeing it. Because the press, they can be very mean. … I want them to be normal." |
| 4 Debbie | 35.62–51.85 | Debbie Rowe | "That was my request, not his. Michael's very proud of his children. I'm the one who's terrified. I'm the one who's seen the notes that someone's going to take his children. There's nothing more terrifying than looking at a piece of paper that says, I'm taking them." |
| 5 Paris now | 51.85–53.12 | Paris | "I always felt, you know, protected." → end (cut to black) |

## Decisions and flags (the creator decides)
1. **Beat 1 opens on a cover.** The podcast never shows Paris during the question (wide, Alex, wide, Alex; the
   wide's 9:16 crop is only fireplace). V2 carries Paris's silent 3.15 s think from CHD 16:02.67 (right after Alex's
   next masks question, no audio) until the podcast cuts to Alex. Rejected: 6:27 (listening, but smiling at a
   compliment, 1.3 s), 28:43 and 29:46 (she is talking). The audio underneath is the one continuous clip, so it
   keeps "I feel like" and two "like"s the paste leaves out.
2. **Beat 5 = Paris's line, not the backup.** It runs straight on from "…was scary" (no pause; in-point on the only
   3 dB dip). Heard in context after Debbie it reads every word; isolated, Whisper lost "you know". **Backup if it
   sounds clipped:** Debbie, Take Two 32:27.50–32:31.30, "He's not that kind of a parent. Not at all." (clean edges;
   a 2.2 s pause before "Not at all" that tightening would shorten).
3. **Beat 3:** burned-in title "Michael Jackson's Camera / Interview in Florida" at 25.64–29.82 s, partly inside the
   crop's bottom band (y ≈ 1690–1760). Michael sits high in the 4:3 frame (hair above y200).
4. **Pauses:** 7 tightened out (6.23 s). Michael's line keeps its pauses: a −30 dB bed runs under his footage, so
   cutting it would jump. Debbie's "says, … I'm taking them" pause is cut; restore it if it should breathe.
5. **Trim in beat 4:** "They're not. They're not. Whatever can be done, they're not." removed, as the paste's "…".

## Checked
- Read-back (`brief/seq14_readback.txt`): 20/20 clips on their planned frames; every clip's first and last frame
  inside its intended camera shot (sources.json `cuts`); audio continuity 0.00 ms at all 5 razors; V2 cover ends
  on the razor (3.15) under it; A2 empty; markers at 0, 14.63, 25.00, 35.62, 51.85.
- Audio proof `outputs/seq14-audio-proof.wav` (53.12 s) re-transcribed: the script in order. "Like that," is
  mumbled (the untouched source reads the same); "protected." is present once the file has trailing silence.
- 9:16 crops: `brief/seq14_crops.jpg`. Framing overrides: `framing.json` (the wides → Alex at x 0.138).
- Tool changes made for this job (LESSONS 2026-09-29): V2 covers, camera-cut splits as razors from the actual
  in-point.
