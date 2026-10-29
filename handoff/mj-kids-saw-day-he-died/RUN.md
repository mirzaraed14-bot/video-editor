# RUN — "What Michael Jackson's Kids Saw The Day He Died 💔" (Abundance Wisdom short)

## ▶ STATUS (2026-10-29) — v2 UPLOADED. Job closed.
- Affan uploaded v2 (`Final Renders\MJ Kids Saw.mov`) with no further notes; session retired. Lessons: AW `LESSONS.md` 2026-10-24 entries.

## (previous) STATUS (2026-10-24 ~22:45) — v2 EXPORTED, waiting on his review
- **`E:\Shorts\Abudance Wisdom Shorts Exports\Final Renders\MJ Kids Saw.mov`** (+ `X:\Claude Projects\Exports\MJ Kids Saw.mov`),
  v1 kept beside both as `MJ Kids Saw v1.mov`. 1088 f @30, 36.267 s, 42.7 Mb/s BT.709, 48 kHz, -13.8 LUFS, -3.1 dBTP, QA PASS.
  From `outputs/mjk_v2_60.mp4`; sheet `proof/final_v2_sheet.jpg`; test `renders/test_v2/ALL-SHOTS-v2-test.jpg`.

## (previous) STATUS (2026-10-24 ~16:00) — v2 IN PROGRESS (his v1 review)
- His v1 notes: "why is Conrad so zoomed in", "the lips are not synced properly with speakers", "captions a bit below towards
  the middle line of the canvas", "this overlay is too dark (O3) either change it or you messed up the grading".
- Fixes (only these): O1 scale 6.6 -> 5.55 (near-min full-bleed), O1 + O3 push-in depth 0.78 -> 0.87; O3 swapped to the
  Day 3 feed's well-lit Murray (ALV 706.4, scale 6.3158, centre 262,152); F4 picture -0.14 s (AP segment 92-118 measured
  picture-early; every other run measured in sync at closed-lip sounds, `proof/sync/f3_*`, `fin2_*`); caption_shift
  180 -> 90 (line y940-980). Grade untouched.
- Running: Topaz + align on O1/O3/F4 (`renders/mjk{O1,O3,F4}_aligned.mov`) -> assemble -> test frames -> full render -> export
  v2 over `MJ Kids Saw.mov` (keep v1 as `outputs/MJ Kids Saw.v1.mov`).

## (previous) STATUS (2026-10-24 ~15:10) — v1 EXPORTED, waiting on his review
- **`E:\Shorts\Abudance Wisdom Shorts Exports\Final Renders\MJ Kids Saw.mov`** + `X:\Claude Projects\Exports\MJ Kids Saw.mov`
  (= `outputs/MJ Kids Saw.mov`, from `outputs/mjk_v1_60.mp4` via `build/export.py`): 1080x1920 30 fps, 1088 f, 36.267 s,
  H.264 41 Mb/s BT.709, AAC 320k 48 kHz, -13.8 LUFS, -3.1 dBTP. QA PASS. Sheet `proof/final_v1_sheet.jpg`.
- Picture chain: `build/assemble_plan.json` (Topaz full + Stage A O5 + Topaz O1/O3/K segments) -> `renders/mjk_picture.mov`
  -> `build/finish.py render` (his AE grade, letterbox 358-1562, zooms, transitions, name cards, captions) -> export.
- Next: his review -> change only what he names -> LESSONS. Swap-ins available: his CBS/CNN Murray clips (picks O1/O3).

## (previous) STATUS (2026-10-24 ~13:00) — last 3 slots filled from LOCAL footage (his "can't you do it? urgent", at the gym)
- YouTube + Telegraph block this PC, so: O1 = AP Murray close-up (FM 86.0, scale 6.6, centre 290,214), O3 = Telegraph somber
  Murray (TEL 62.3, scale 6.2, centre 270,190), both full screen, mouths above the caption line, through his Topaz chain
  (`renders/mjkO1_aligned.mov`, `mjkO3_aligned.mov`); S2 = his Telegraph pick = trial Exh. 23, taken from the AP exhibit frame
  (FM 65.8, crop x170-450 y8-288: no AP bug / no text), Higgsfield-enhanced a7eed22a -> `build/overlays/bed_exh23_hf.png`
  (test `renders/test_v1/BED-test.jpg`). His CBS/CNN clips can still swap in later (picks O1/O3).
- Next: assemble (+ O1 98-195, O3 833-952 'seg') -> test frames of O1/O3 -> full finish render -> 30 fps .mov export ->
  QA -> `E:\Shorts\Abudance Wisdom Shorts Exports\Final Renders\MJ Kids Saw.mov` + copy in `X:\Claude Projects\Exports\`.

## (previous) STATUS (2026-10-24 ~11:20) — test frames APPROVED ("Katherine looks right now"), waiting on his 3 files
- Picture of every shot approved except the 3 slots still black: O1 + O3 Murray (CBS nkRPK9EubAw, CNN DoOwJr3K8AA ~4:37
  teary), S2 Telegraph bedroom photo. Higgsfield enhance: his YES (2026-10-24). Kids DONE: job 0eb74f64 (nano_banana_2 2k,
  1.5 cr, balance 1257.25 before) -> `build/overlays/kids_remembering_dad_hf.png` (1696x2528), S4 centre [848, 1121], test
  `renders/test_v1/KIDS-hf-test.jpg`. Bed photo: enhance the same way (upload -> PUT with If-None-Match: * -> confirm ->
  generate nano_banana_2 2k, image_references) as soon as he saves it.
- On arrival: picks for O1/O3 (full screen, scale = 1920/h; Topaz only if SD looks soft — test both), S2 still (letterbox),
  their test frames -> full finish render -> audio mux -> 30 fps export -> QA -> Exports.

## (previous) STATUS (2026-10-24 ~11:15) — his v1 frames note applied (Katherine lower), waiting on his OK + files
- His note on test v1: "They look good but Katherine should be placed lower so that the captions are on her nose... the
  mirrored effect is looking really ugly". Done: KJ nose y561 -> 870 (captions on her nose), zoom pivot y870; her shots
  re-rendered (`renders/mjk_stageA_K.mov` 1814-2176 -> Topaz `mjkK_*` -> `mjkK_aligned.mov`, spliced 'seg' in
  `build/assemble_plan.json`). Test: `renders/test_v1/KATHERINE-v1b-test.jpg` (no mirror visible). Everything else as v1.

## (previous) STATUS (2026-10-24 ~10:45) — TEST FRAMES v1 sent (`renders/test_v1/ALL-SHOTS-v1-test.jpg`), waiting on his OK + files
- Picture: Topaz done (2179 f) -> `align_frames` (2176) -> `renders/mjk_picture.mov` (one-pass: Topaz faces + Stage A O5).
- Fixed on the way: caption_shift sign (+ = UP; native ink y1030-1070 -> +180 = line y850-890; -307 had put them at 1350 on
  the name cards). Skin (his grade untouched, pre-grade levelling, `build/skin_png.py`): Faheem gamma 0.74 + sat 0.58
  (0.27/0.96/1.9 -> 0.39/0.68/1.37), Katherine sat 0.55 (0.42/0.8/2.4 -> 0.43/0.61/1.8); Alvarez untouched (0.6-0.73/0.5-0.7/1.5-1.65).
- Still black (files owed): O1 + O3 Murray (CBS nkRPK9EubAw, CNN DoOwJr3K8AA), S2 Telegraph bedroom photo. Higgsfield
  enhance of kids + bed photos waits on his yes (~4 credits).
- Next: his OK on the frames -> slot the three files (+ their test frames) -> full finish render (60 fps) -> audio mux ->
  30 fps export `MJ Kids Saw.mov` to `E:\Shorts\Abudance Wisdom Shorts Exports\Final Renders` + copy in X:\Claude Projects\Exports
  -> QA (LUFS/TP on the file, no child... n/a per his call, captions vs lips, safe zones).

## (previous) STATUS (2026-10-24 ~10:00) — CODE BUILD running (his answer: "direction video wins", kids photo + Paris/Janet)
- Build = `build/` (copied from MJ siblings v6; `make_timeline.py` writes `timeline.json` + `overlays/picks.json`). Internal 60 fps
  (his calibrated chain), export decimated to 30 fps (brief). 2176 frames = 36.2667 s (his edit; clip src = in + (end-start),
  Premiere's outPoint is stale -> no overrun at the end, no FM repeat).
- Sync: TEL picture = audio - 0.3667 s (his Paris fix; re-measured visually on "Paris" 0.38 and "proceeded" 0.36,
  `proof/sync/`); FM + 60M in sync within ~1 frame. Auto (mouth-motion / MediaPipe) correlation was too noisy on SD: use strips.
- Framing (one caption line under the lips): courtroom letterbox band 358-1562 at scale 4.0 (his 346 % exposes the band edges
  when the head-locked nose moves), AT nose y745, FM y704; Katherine full-bleed 1.7787 nose y561 (forehead cut); lips y835;
  captions shifted -307 (line ~y848); face zooms pivot on the lip line, depth 0.87.
- Done: his A1 rebuilt (`seqref/raw/a1.wav`, 2-frame equal-power crossfades), captions (`captions/captions.txt` ->
  `caps_capcut.mov`, 49 captions, brief's red words), track + Stage A (`renders/mjk_stageA.mov`), audio
  (`renders/mjk_audio.wav`: level-matched to Katherine, NR on courtroom, fresh Epidemic set `build/sfx/`, his Dumbledore's
  Farewell bed 14 LU under, out by 27.4), overlays: O5 Paris/Janet (memorial 9546.4 @0.8x, scale 1.9), S6 morgue (his
  Higgsfield 9f72348b, crop 44,48-2004,1836, scale 0.8 centre 1329,800), S4 kids (E! "Remembering Dad" 634x1024, NOT yet
  enhanced: Higgsfield ~2 cr pending his OK).
- Owed by him: CBS nkRPK9EubAw + CNN DoOwJr3K8AA (Murray O1/O3, full screen) + the Telegraph bedroom photo (S2) — the
  Telegraph site blocks this PC. Pending slots render black until then.
- Running: Topaz (`renders/mjk_stab_chr2_iris3_prob4.mov`) -> align_frames -> assemble (Topaz faces + Stage A O5) -> finish
  stills of EVERY shot -> his OK -> full render -> 30 fps export.

## (previous) STATUS (2026-10-24 ~09:30) — direction video RESOLVED (BRIEF.md § HIS SEQUENCE), waiting on his answers
- His sequence dumped (`seqref/seq_his.tsv`), Tella video downloaded + transcribed + every "this" mapped (BRIEF.md table).
- Asked him: minors in S4/S5 vs the brief's rule; downloads he must do (CBS nkRPK9EubAw, CNN DoOwJr3K8AA); music default.
- Next on his answers: rebuild his A1, per-clip lip sync, fetch overlays (Telegraph photo + Higgsfield enhance, his Higgsfield
  morgue still, memorial Paris/Janet, kids photo), then the code build (method `projects/mj-siblings-found-out/build/`).

## (previous) STATUS (2026-10-24 ~08:10) — PAUSED: waiting on HIS sequencing + his direction video
- He approved the raw sequence v2 (Murray cutaway under "crying and screaming" kept), then stopped the build: **"I haven't
  done the sequencing and no creative video yet."** Order from here: he re-edits "MJ Kids Saw - raw cut" in ABW10 himself →
  sends his Tella direction video → THEN the code build. Nothing was built (only reads: build pipeline, overlay candidates
  `proof/cutaway_candidates.jpg`, his library list). His answers already in hand for the build: outside child-free overlays
  OK (his MJ morgue still, adult MJ, courtroom cutaways); defaults stated in BRIEF.md § Code-build gate (30 fps etc.).
- On his go: dump HIS sequence read-only (`premiere/readback.js` style, like MJ siblings `seqref/seq_his.tsv`; rebuild his A1),
  resolve the direction video into BRIEF.md, then build. Never save/export ABW10.

## (previous) STATUS (2026-10-24 ~07:40) — RAW SEQUENCE v2 PLACED
- v2 (his ask: get Alvarez on camera): he downloaded Alvarez's full testimony (YouTube Parts 2–4 of the Day 3 fan upload;
  `raw/ALV_Testimony_Day3.mp4` = `Henry\Alberto-Alvarez-SnapYT.App_2.mp4`, 540x304, no bug; transcripts `win/alv/`).
  Beat 1 "Dr. Conrad Murray said," now comes from it (ALV 368.00–369.07 + 369.32–370.02): Alvarez on camera, no cutaway.
  Re-placed after checking the v1 sequence was untouched (readback identical); readback 0 flags; 39.73 s; active restored.
  v1 kept as `premiere/place_v1_tel.jsx` / `readback_v1_tel.tsv`.
- Found: the Telegraph SPLICED his testimony. Real order (ALV 322–386): "Paris screamed out, Daddy" → Q&A (was she crying /
  MJ palms up looking toward Paris / did you escort them out) → "Dr. Conrad Murray said… Don't let them see their dad like
  this ×2. And I proceeded… kids, don't worry… Everything is going to be okay. And so I walked them out…". Same event, same
  order: meaning kept. **"the children were crying and screaming" is NOT in Parts 2–4** (the Telegraph took it from elsewhere
  in his testimony), so it stays on TEL's Murray cutaway (tl 26.75–29.40) unless he wants more parts searched. The ALV stream
  drops ~1.6 s where he says "kind of ushered them out and said" (381.7–382.8), so beat 3 stays TEL.

## (previous) STATUS (2026-10-24 ~07:00) — RAW SEQUENCE v1 PLACED
- **ABW10 › bin "MJ Kids Saw" › "MJ Kids Saw - raw cut"** (clone of "Onyx reaction template (empty)", 1080x1920 60 fps):
  22 clips V1/A1 + 4 beat markers, **39.78 s**. Readback (`premiere/readback.tsv`): every clip's V/A offsets identical (sync
  0 ms), in-points within one source frame of the plan. His active sequence restored to **Sequence 22**. Not saved (he saves).
- Open with him: (1) **runtime 39.8 s vs the brief's ≈55 s** — the brief's ranges were timestamp estimates; the exact words,
  with fillers + pauses > 0.25 s removed (rule B1.1), run 39.8 s. Trims 1 + 3 were NOT applied (the lawyer's question and
  both "Don't let them see" stay). (2) **three picture-not-speaker spots**: TEL's defence-table cutaway under "Dr. Conrad
  Murray said," (tl 1.63–3.45), AP's bedroom exhibit photo under the lawyer's question (tl 6.33–8.35), TEL's Murray cutaway
  under "the children were crying and screaming" (tl 26.80–29.45). He asked for links to Alvarez's full testimony (Day 3,
  29 Sep 2011: playlist PLE69405D24B07F03D; full trial PLkHDG8vZbx393KXNVyiFF0IHyzLJZZmHJ) — if he downloads it, re-sync TEL
  pieces to it (same courtroom feed) and re-place. (3) 60 fps raw sequence (his template) vs the brief's 30 fps final.
- Next on his OK: the code build (method `projects/mj-siblings-found-out/build/`, v6) + the BRIEF.md § "brief vs standing
  rules" questions (captions height, ≤4 s face-cam overlays, music bed, export path).

## Sources (`raw/`, originals in E:\Bullshit Folder)
| Code | File | Original | Format |
|---|---|---|---|
| TEL | `TEL_Alvarez_2011.mp4` | `Henry\Michael-Jackson-Paris-SnapYT.App.mp4` | 620x348 25 fps, 172 kbps, Telegraph bug lower right |
| FM | `FM_FaheemMuhammad.mp4` | `Henry\Guard-describes-scene-SnapYT.App.mp4` | 640x360 25 fps, 252 kbps, AP bug top right |
| 60M | `60M_Katherine_2013.mp4` | `Drake\Katherine Jackson on Michael's Changing Face and the Scandals _ 60 Minutes Australia.mp4` | 1920x1080 29.97, "60 AUSTRALIA" bug lower left |
| ref | `ref_MurrayTrialDay2_Faheem.mp4` | `Henry\Conrad-Murray-Trial-SnapYT.App.mp4` | 320x240, lock 1 only |
Transcripts: `transcript/words.json` (TEL + FM full, 60M window 2290–2380 s); edge checks `win/snip/` (isolated
faster-whisper re-ASR) + 20 ms RMS. Note: the brief's TEL times run ~4 s early ("Paris screamed" is at 32.1, not 28).

## Ranges (source seconds; `edl.json` / `placement.json` are the exact frame-snapped values)
| Beat | Src | Pieces (in → out) | Words | Trimmed inside |
|---|---|---|---|---|
| 1 | TEL | 32.08–33.71 · 34.32–35.44 · 35.60–36.30 · 39.96–41.56 · 42.80–44.08 | "Paris screamed out, Daddy. Dr. Conrad Murray said, don't let them see their dad like this. Don't let them see their dad like this." | "uh, don't let the, don't let them" false starts (36.3–39.96), "um" (41.6–42.8), pause Murray/said |
| 2 | FM | 35.72–37.74 · 47.16–48.84 · 49.56–52.06 · 53.16–57.81 · 93.28–95.51 | "What did you see when you first came in? I saw Mr. Jackson's feet near the side of the bed on the ground. And as I continued to walk over, I could see the rest of his body. Immediately [I] was shocked, just seeing him." | "When I came into the room, I saw Alberto standing up, kind of pacing" (not in his words), pauses 1.0 + 1.1 s, "you know" before "immediately" |
| 3 | TEL | 45.20–47.90 · 48.60–50.17 · 50.72–51.67 · 52.20–52.98 · 53.24–54.62 · 60.88–62.11 · 62.80–63.58 · 64.36–64.99 | "I proceeded to turn around to the children and kind of ushered them out and said, kids, don't worry. We'll take care of it. Everything is going to be okay. … the children were crying and screaming." | "um" ×1, "kid-" stammer, first of "we'll, we'll", "uh", "And he said he had a reaction… the housekeepers," (not in his words), a 0.7 s sob + pauses |
| 4 | 60M | 2327.69–2330.69 · 2331.96–2333.43 · 2345.18–2348.41 · 2349.18–2351.81 | "they went back in that morgue where Michael was about ten times. She said, the children are hugging Michael and kissing him. And, you know, he was dead, but they were still doing that." | "No, I don't think so. Because" (before), 1.6 s pause, lock-3 passage 2333.4–2345.2, 0.9 s pause; ends on the camera cut at 2351.816 = hard cut on "that." |
Edge uncertainty for his ear: FM 93.28 starts right after "you know" (no silence between; the brief heard "[I]" there).

## Locks
1. FM year — RESOLVED 2011: FM = the Murray trial, Day 2, 28 Sep 2011: same courtroom (Judge Pastor's bench + nameplate,
   the plant), same witness-stand framing, same black suit / silver tie as the Day 2 upload; the package also shows
   "People v. Murray SA073164" exhibits and Murray at the defence table. Proof: `proof/fm_sheet.jpg` vs `proof/ref_sheet.jpg`.
   Card: MURRAY TRIAL, 2011.
2. "Morgue" — RESOLVED: she says "that morgue" (WhisperX 0.55; his approved Katherine short captioned the same words
   "IN THAT MORGUE"). Caption "morgue".
3. Beat 4 join — RESOLVED: "about ten times" (ends 2333.43) → "She said" (2345.18); "When I was in that room… What are you
   all doing back there?" dropped.

## Checks
- No child on frame: every piece's frame in `proof/pieces_sheet.jpg` (Alvarez, defence table, bedroom exhibit photo with
  no person, Faheem, Katherine). The FM package's CCTV (159–175 s) is not used.
- Watermarks outside the 9:16 crops (Telegraph lower right, AP top right, 60 AUSTRALIA lower left) at the placed framing.

## Log
- 2026-10-24: brief received; job folder; 60M copied; beat-4 window transcribed (locks 2 + 3). He downloaded TEL, FM and the
  Day 2 ref; lock 1 resolved; transcripts + snippet re-ASR; beats.json → resolve_beats → plan_placement → place_sequence;
  sequence created in ABW10 and verified; active sequence restored.
