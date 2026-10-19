# RUN — cbum-born-with-it (Abundance Wisdom Short: "BORN WITH IT", misconception, no wins)

## ▶ STATUS: resume here
**2026-10-13: CAPCUT CAPTION RETURN CLEANED + RE-POINTED** — `Caption Exports/cbum caps 2.mp4` (footage #1679, in "cbum caps
2.mp4 Comp 1" → comp 72 L1) → `cbum caps 2_clean.mp4`: 769 frames repaired (29 static frames every 2 s at ~40 % of the frame,
740 faint specks ≤ 2.3 %), `captions/capcut/clean.log`; checked on 6 frames (`verify_clean.py`): caption pixels move ≤ 5
levels, the lifted field 42–46 % → ≤ 0.3 %. #1679 re-pointed in place (`captions/capcut/cbumcaps_replace.jsx`, undo "Clean
CapCut caption export (Claude)"): size / fps / duration MATCH, the precomp layer's in/out (0.567–57.1) unchanged. ABW9 NOT saved.
**2026-10-13: TRANSITIONS on ABW8 Linked Comp 72** from his labels (`transitions/labels_comp72.tsv`): 13 = 6 Purple (−90) at
2.7 / 5.517 / 11.783 / 15.533 / 27.567 / 37.917, 3 Cyan blur at 22.017 / 31.217 / 46.667, 2 Dark Green (+30) at 40.817 /
50.533, Pink flash 7.983, Peach exposure 48.017; none after the yellow shin-press block (22.0–26.4); last block ignored.
Read back (`transitions/transitions72.txt`); stack: caption → transitions 2–14 → zooms 15–29 → footage. Undo "Abundance
Wisdom transition pass (Claude)".
**2026-10-13: LETTERBOX on comp 72's 2 FUCHSIA blocks** (relabelled after the transitions, which stay): the rash photo
2.7–5.517 and the young photo 7.983–11.783 are overlays ON the couch (no black bars): mask = the photo band measured on the
render, 2 px inside (y214–1704 / y231–1693), twins 142 % / 145 % @ 47 %, his comp 60 glow lines on both edges
(`letterbox/plan72.json`, `letterbox72.jsx`, log `.txt`; proof `letterbox72-proof.jpg`, twin covers 100 %). The 3.8 s block
outran his 2.917 s line precomp: a COPY "White Solid 1 Comp 1 (long)" (#1777, 10 s) carries those two lines
(`extend_lines72.jsx`); the template now does that by itself. Undo "Letterbox glow lines (Claude)" + "Letterbox lines:
longer line precomp (Claude)". ABW9 NOT saved.
**2026-10-13: ZOOM PASS (BlurMoCurves) on ABW8 Linked Comp 72** (his Topaz render `Topaz Exports\chris_stab_chr2_iris3.mov`
of Sequence 52, 57.1 s, 15 blocks; 5 yellow = pull out: 2.7, 8.0, 22.0, 27.6, 48.0 s): 15 `Adjustment Layer 29` zooms
with S_BlurMoCurves, 10 face pivots (block 14, the stage B-roll 48.0–50.5, pinned to the top edge: his head is at the
source's top, `zoom/centers.override.json`), every Z read back as planned. Stack: his caption "cbum caps 2.mp4 Comp 1"
(CapCut return, top) → zooms 2–16 → footage 17–31. Undo "Abundance Wisdom zoom pass (Claude)". ABW9 NOT saved.
**2026-10-13: CAPTIONS for Sequence 52 (his recut, 57.10 s), COLOURED + STACKED, rendered as his caption export:**
`E:\Shorts\Abudance Wisdom Shorts Exports\Caption Exports\cbum.mov` (H.264 1080×1920 60 fps ~25 Mbit/s + PCM voice, like
ronnie.mov) = the file he hands to CapCut. 93 captions, max 3 words, 23 coloured (red = the brief's six: BORN, INCH,
15 POUNDS, KIDNEY ×2, ANYBODY, PERFECT), 6 STACKED pairs ("+" in `captions/captions.txt`: line 2 at +65 px, line 1 holds
to the pair's end). Engine: the code-trial renderer (`captions/render_caps.py` → aw-code-trial-parents cap_render:
Gretaros 48, GPOS kerning, his gradients, the pop stretched per caption); line-1 cap top y1022 measured on ronnie.mov.
Transcript fixes (`captions/transcript/words.json`, backup `words.whisperx.json`): sebum → CBum, have this → has his,
look up to is → as. Premiere cannot colour words by script (LESSONS 2026-09-21), hence the render. Editable fallback:
`captions/flat/outputs/seq52-captions.srt` (not imported). Sheet `captions/caps_sheet.jpg`.
**2026-10-13: HEAD LOCK on ABW8 Linked Comps 66–71** (his recut of Sequence 52 replaced with AE comps, ABW9.aep): 20 layers
(16 hospital at 177.9 %, 4+1 podcast at 237 %), all label 3, 2,398 Anchor keys + Motion Tile, undo "Head lock (Claude)";
0 frames missed, `headlock/track_sheet.jpg` (dot on the nose, incl. the eye-wipes in comp 70 L5–L8), proof from AE's
read-back keys `headlock/headlock_proof_*.jpg` (every LOCK row holds the nose). ABW9 NOT saved. Next: captions on Seq 52.
**2026-10-13: RAW CUT ON ABW8 · Sequence 52 (bin "CBum Born With It"), 57.95 s — waiting on Affan's call.** ABW8 NOT saved.
Sequence 52 = a clone of his empty Sequence 48 (1080×1920, 60 fps, v3/a4), renamed; it became the active sequence.
- V1/A1: 20 clips, butt-joined 0 → 57.95 (beats 1–8 all in; neither runtime cut needed). V2: Prague posing 0–3.20
  (hard cut to the couch on "born"), leg photo 28.03–33.30 (on "my legs … so big"). A2 empty (Prague audio removed).
  8 beat markers. Read back (`premiere/readback.tsv`) = plan.
- Proven: the timeline audio rebuilt from the read-back in/outs and re-transcribed (`proof/seq52_audio.wav`,
  `proof/seq52_words.txt`) = the brief's words, in order. Joins 0.26–0.34 s of quiet; inside-sentence pauses up to 0.5 s
  (20.1 s "obviously… so", 48.4 s "look up to… as calm"). Couch −18.5 vs podcast −19.4 dBFS RMS.
- In/out table: `proof/inout_table.md`. Crops: `proof/crop_sheet.jpg` (beat 2 pinned by hand, `framing.json`).
- NOT done (raw cut only, by his scope): cards, captions, bleeps, music, loudness, leg-photo push-in, AE.
**Flags for Affan:**
1. Beat 5 line 1 ("woke up the next day… 15 pounds"): CBum's own video cuts at 4:02.44 to his clip pressing his
   swollen shin; the sheet says couch. Kept his insert.
2. Beat 5 line 2: his burned-in "WARNING PICTURE IS NASTAY..." shows on the couch for 1.25 s ("by the time I got home",
   26.78–28.03) before the leg photo covers it. Fix options: start the photo on "by the time" or patch the text in AE.
3. Bleeps: beat 7 ×1 ("fucking pitying"), beat 8 ×1 ("fucking perfect"). Beat 8's other one is "shit together", not the
   f-word (the sheet says ×2). Not bleeped yet.
4. Hook "name" after "the doctor" = the word "literally" (auto-caption "Larry"): kept, it is not a name.
5. Hook picture: Prague low-angle front double biceps (1:46.55), head high in frame under the stage light.
6. Beat 8 picture: the podcast file is 1920×810, so the 9:16 crop is a 237 % blow-up (soft); a 4K download would help.
   Leg photo: a 1080p video frame filled to 9:16 (178 %), soft too (memory: enhance sourced stills before finishing).
7. YouTube blocked this machine again (429 + bot check), so Affan downloaded the three sources himself.

## Overlay photo (Affan's image, 2026-10-13)
`assets/overlays/young_photo_src.png` (214×226, red "14" on the cabinet) → Higgsfield (5 credits):
- **A, used: `young_photo_4k_clean.png`** (3913×4096) = Higgsfield 4K upscale (bytedance, 2 cr; same framing, arm,
  sticker) + the "14" removed locally: the cabinet patch taken from version B, aligned (affine + 5 px, stiles measured),
  feathered over the digits and their red glow only (0 pixels changed outside the 14's box, 0 red left).
- B: `young_photo_hf_4k.png` (4032×4260) = Nano Banana 2.1 4K restore + "14" removed (3 cr): sharper, but a re-drawn face.
- Both AI passes changed the FACE (open-mouth mid-word → closed smile, eyes): from a 214 px source any 4K face detail is
  invented. The masked edit (mask role) is not supported on nano_banana_2_1 ("Unknown media role: mask").

## Format / lane
Abundance Wisdom short, 9:16 1080×1920, Premiere ABW8 (sequencing) → AE later. Preset
`presets/youtube-shorts/abundance-wisdom/` (PLAYBOOK § 0 Sequencing).

## Sources (Affan's downloads, `E:\Bullshit Folder\Henry\`; `broll/` stayed empty)
- f062: CBum, "Admitted to Hospital 4 Weeks Out | The Challenge I Faced This Prep", 22 Sep 2018 (F062siQfzps) — beats 1–7 + leg photo
- dark: Chris Williamson, "Chris Bumstead - The Dark Side Of The Road To Greatness (4K)", 10 Jul 2023 (AncMbHY6b2A) — beat 8, window 14:30–15:45 only
- prague: CBum, "Open Bodybuilding Posing Routine | EVLS Prague Pro" (S08Ll8VMLic) — hook picture, posing only

## Sequencing (PLAYBOOK § 0)
`sources.json` (windows f062 90–690 s, dark 870–960 s; scene cuts) → `raw/*.mov` → `transcribe.sh` → `find_quote.py`
per beat → `beats.json` (beat 7 in measured 621.46: WhisperX put "I" at 620.37, before a camera cut) → `resolve_beats.py`
→ `edl.json` (57.95 s, 7 pauses tightened, 2.20 s) → `plan_placement.py` + `framing.json` → `proof/crop_sheet.jpg` →
`premiere/create_seq.js` (clone of Sequence 48) → `place_sequence.py` → `premiere/place.jsx` → `premiere/readback.js`.
Leg photo: `assets/legphoto_src_282.0.png` (F062 4:42.0) → crop x 556–1363 → `assets/legphoto_9x16.mp4` (8 s, 60 fps).
