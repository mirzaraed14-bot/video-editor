# RUN: "Why Everyone Underestimated Michael Jackson 😳" (Abundance Wisdom short)

## ▶ STATUS: resume here (2026-10-31 ~18:35): DELIVERED v3 (labels at the bottom) → at his review
- His note on v2 (via the parent, verbatim in memory feedback-labels-at-bottom): labelling motion graphics at the BOTTOM.
  v3 = ONLY that: `lower_thirds` y0 230 → 1270 (London 1385, on the twin fill under its band); finish re-rendered for
  the card ranges only (`outputs/lt_v3_{0,380,592,1018}.mp4`) + `build/splice_multi.py` onto v2's finish →
  `outputs/mj_finish_60_v3.mp4` (frame diff vs v2: only frames 9-121 / 385-498 / 599-710 / 1025-1136 change) → export.
  **`MJ Outthink Them.mov` 40.80 s, MD5 5d4652500d9aff76b46f3a6654618275** in Final Renders + Exports; v2 kept as
  `(v2 40.8s)`, v1 as `(v1 41.4s)`. Phone copy (he's out): **`outputs/MJ Outthink Them (phone).mp4` 26.56 MiB**.
- Measured on the v3 file: captions y1117-1160, card name ~y1290-1330 / role ~y1359-1401 (London 1405-1516), < y1620.
- **KIT BUG found + fixed here (not elsewhere):** `build/splice_multi.py` / `splice_ranges.py` wrote raw frames without
  declaring their range, so ffmpeg range-converted them: every splice pass darkened luma ~4-5 levels. v3's first splice
  came out 4.5 darker (caught by the v2/v3 diff, re-spliced after the fix). `picture_v1` (S10 splice) was darkened the
  same way BEFORE the finish, so v1-v3 are all graded from a ~5-level darker picture than Topaz's output: consistent
  with what he reviewed, left as is. The copies in other jobs' kits (Patrick, Kane, Conrad...) still carry the bug.
- **Caption line is ~y1135, not the ~y950-1000 I reported for v1/v2** (`caption_shift` is positive-UP; −85 moved it down).
  Kept (he named only the labels); REPORT flags it with the fix on offer.

## (previous) ▶ STATUS: resume here (2026-10-31 ~18:00): DELIVERED v2 (40.80 s) → at his review
- v2 = v1 minus a 0.56 s room-tone pause inside Eddie's last line (advisor QA; wav2vec2 had stretched "that's" over it):
  `seq/edl.py` v5 (OVERRIDES + EDGES "four" out 579.24 / "that's" in 579.79; v4 kept `seq/edl.v4.*`), make_timeline (the
  split Michael line = ONE span: one fade, one pull-back), `renders/picture_v2.mov` (= picture_v1 frames 0-2049 +
  2084-2481), dialogue + mix (-14.0 LUFS / -1.6 dBTP), captions v5 (`renders/caps_capcut_v5.mov`, 2448 f), finish
  re-rendered ONLY frames 1934-2448 (`outputs/mj_fin_tail_v2.mp4`, parent's GPU slot) + spliced onto v1's finish →
  `outputs/mj_finish_60_v2.mp4` → `export.py` → **`MJ Outthink Them.mov` 40.80 s, 1224 f, MD5 6f813097…** in Final Renders +
  Exports; v1 kept beside it as `MJ Outthink Them (v1 41.4s).mov` (all three places). "card free" sent again 17:55.
- Proofs v2: `proof/final_edges.jpg` (22 cuts), `proof/final_sheet_v2.jpg`, silence scan (no gap > 0.25 s at 22 dB; v1's
  0.66 s found by the same scan), re-ASR `win/asr/FINAL_v2.json`, Eddie lip sync `proof/ed_plos_buy.png`, skin on export.
- NOTE: track.json shot IDs are v4's (S20-S22 = LDN); a Stage A re-render needs `stage_a.py track` again first.

## (previous) STATUS (2026-10-31 ~17:45): DELIVERED v1 → at his review
- `MJ Outthink Them.mov` (41.37 s, 1241 f @ 30 fps, 40.7 Mb/s, PCM 48 kHz, **-14.1 LUFS / -1.6 dBTP** on the file, MD5
  a8c344b67eaa31032c4a08221b1c3ec2) in `E:\Shorts\Abudance Wisdom Shorts Exports\Final Renders\` + `X:\Claude Projects\Exports\`
  (= `outputs/`). § 8 QA + § 9 report: `REPORT.md`. Proofs: `proof/final_edges.jpg` (21 cuts), `proof/final_sheet.jpg`
  (1 per s), `proof/final_plos.png` (Peter Pan lip sync on the file), re-ASR `win/asr/FINAL.json`.
- Chain: `renders/picture_v1.mov` (Topaz + S10 Stage A) → `build/finish.py render … outputs/mj_finish_60.mp4 --audio
  renders/mix.wav` (11.5 min, 3.7 fps) → `build/export.py`. "card free" sent to Conrad + parent at 17:34.
- A note from him → change the DATA (make_timeline / captions.txt / edl.py), re-render only the touched frame range
  (`finish.py render --frames a:b`), splice (`build/splice_multi.py`), export: one finish render per note.
- LESSONS appended (AW shorts LESSONS.md, 2026-10-31 MJ Outthink); memory project-abundance-shorts-automation updated.

## (previous) STATUS (2026-10-31 ~16:00): HIS TELLA 1 RESOLVED (BRIEF 13-22) → seq v4 → FULL CODE BUILD running
- Tella: `brief/tella/` (guide.mp4, guide.json, labels*.png = Tella s → preview time). DECISIONS 13-22 in BRIEF.md.
- **Seq v4** (`seq/edl.py`, v3 kept as `seq/edl.v3.*`): "He's shrewd behind it all" + "the girl is mine / your publishing's
  mine" cut → **41.37 s, 19 segments**; new joints measured ("lipstick" out 6463.212 on the /k/ dip; "money" out 580.997).
- Stills (stills/src crops → Higgsfield bytedance 4K upscale, 6 credits, balance 1104.75; all checked full size, no
  rewritten features): `stills/hf/katherine_up4k.png` (60 Minutes Australia 1080p @38:36, calm), `joe_up4k.png` ("Joe
  Jackson FINALLY Speaks" 1080p @5:43, black hat, above the watermark), `mj_paul_up4k.png` (the B&W Paul-waving + Michael
  photo, Howard Stern clip @1:01, cropped inside its border, adults). MJ + Paul = brief v3's optional cutaway, placed over
  "Michael done bought the Beatles" to break Eddie's 8 s colour run (face-cam 4 s rule), letterboxed.
- Bashir lip sync: measured IN SYNC on 7 events (no slip, DECISION 20); `win/plosive_check.py` (fps-aware), `win/pitch.py`.
- Kit = Patrick's `build/` + `captions/` (copied). Envs: track = `uv run --with opencv-python-headless --with scipy`;
  render = whisperx venv python (torch). Topaz: `build/topaz_src.py` Proteus x4 LDN02 a (129.5-144.5, 243-246), x2 EDDIE
  (545.8-581.6) → `renders/*_prob*.mov`.
- DONE (~16:15): `build/make_timeline.py` (22 shots; LDN head-locked in band 420-1450, Joe band 300-1560, MJ+Paul band
  380-1420, Katherine full frame 0.57; every mouth at y~990; Eddie MICHAEL lines sat 0.22 with 0.2 s fades, B5 opens
  faded; Eddie zoom = keys (push-in, +0.04 pull-back on each Michael line); transitions purple 6.23 · green 9.83 · cyan
  13.10 · purple 16.93 · peach 19.23 · cyan 28.10 · purple 35.93; warmth +1 on LDN/BASH) → `stage_a.py track` (+
  `band_clamp` for lb locks) → `build/smooth_track.py 6` (LDN only: 115 px face, noisy lock) → `renders/stageA.mov`
  (2482 f) · `build/dialogue.py` (+ bleep, LDN afftdn) → `renders/dialogue.wav` · `build/mix.py` (fresh Epidemic set,
  `build/sfx/SOURCES.md`, -21 dB) → `renders/mix.wav` **-14.10 LUFS / -1.60 dBTP** · captions: `captions/make_words.py`
  (words by ear: "he had … who's", "he said 60, I gave you 64", "how do you buy", bleeped word uncaptioned) →
  `captions.txt` (62 captions, brief red words + colour MIX) → `make_plan.py` → `render_caps.py` → `capcut_pass.py`.
  `finish.py`: `keys` zoom layers (z_at). Catalog pass (scoped) in BRIEF.md.
- DONE (~17:25): GPU waits (Conrad's Topaz, then his Stage A; parent ordered the queue: me next, then "card free" to
  Conrad + parent after my finish render). Topaz `workflows/topaz-iris.py --no-enhance --reduce 2 --segments <22 shot
  starts>` → `renders/stageA_topaz.mov` (2482 f, 34 min, no watermark `proof/topaz_check.jpg`); `win/hold_scan.py`: repeats
  gone everywhere except S10 (Bashir's question, near-static: Chronos added 3-7 frame holds) → S10 kept from Stage A
  (`renders/S10_stageA.mov`, `build/splice_multi.py`) → `renders/picture_v1.mov`. Test stills v1-v3 (`proof/fin_test*_grid.jpg`):
  caption base MEANT to rise to ~y950-1000 (`caption_shift` -85; v3 measured: it moved DOWN to ~y1135, the shift is positive-up),
  London lifted 90 px in the finish ('lift', band 400-1380), Katherine re-sourced WIDE (60 Minutes x600-1920, Higgsfield 4K
  `stills/hf/katherine_wide_up4k.png`, 2 more credits = 8 total, balance ~1102.75) in band 300-1300, Joe band 300-1480,
  MJ+Paul nose-mid y800; skin (his R/G 1.5-1.7): LDN sat 0.75 (1.46-1.54), Katherine 0.45 (from 2.78), Joe 1.50.
- RUNNING: `finish.py render renders/picture_v1.mov renders/caps_capcut.mov outputs/mj_finish_60.mp4 --audio renders/mix.wav`.
- NEXT: message Conrad (local_a9997639) + parent "card free" → `build/export.py outputs/mj_finish_60.mp4 renders/mix.wav
  "outputs/MJ Outthink Them.mov"` → `win/final_edges.py` + lip sync on the file (plosive_check "Peter Pan") + re-ASR →
  copies to Final Renders + Exports → § 8 QA + § 9 REPORT.md → LESSONS + memory.

## (previous) STATUS (2026-10-31 ~13:35): SEQUENCE PREVIEW SENT → waiting on his OK + whether he sends a Tella
- `X:\Claude Projects\Exports\MJ Outthink Them - SEQUENCE PREVIEW.mp4` = `seq/preview.mp4` (v3, **45.13 s**, 21 segments,
  -14.4 LUFS / -1.9 dBFS, face-tracked 9:16 crops, bleep, covers). Proofs: `proof/preview_sheet3.jpg` (first/mid/last of
  every shot), preview re-ASR `win/asr/PREVIEW.txt` (every joint clean; "the next day" with the bleep). Table: `seq/inout.md`.
- The sequence = data: `win/fa_all.py` → `win/fa/*.json` (wav2vec2 on by-ear text) → `seq/edl.py` (PIECES v3, EDGES = measured
  cut points, OVERRIDES, BLEEPS, COVERS) → `seq/edl.json` → `seq/preview.py` (copied from Patrick; + per-frame face tracking,
  + bleep). Tools: `win/fine.py` (5 ms strips), `win/mute_test.py` (which word is in a span), `win/who.py` (speaker
  embedding: Eddie vs Vlad), `win/bleep.py`, `win/cuts.py`, `win/sheet.py`.
- Flags for him (BRIEF DECISIONS 8–12): swearing (cut + bleep), host cover, words by ear, Vlad's laugh, payoff.
- NEXT on his answer: Tella → transcribe (`win/asr_guide.py` from Patrick) + frames → BRIEF DECISIONs; then the build:
  copy Patrick's `build/` + `captions/` kit → Stage A per shot (face lock) → Topaz Proteus on LDN02 copy a (640×358) + BASH?
  (1080p already) → grade (warm filmic LDN02 + BASH, clean EDDIE/MATT; skin R/G measured per source first) → labels →
  captions y≈1060 colour MIX (re-ASR the final cut for the open words) → audio (LDN02 light de-noise, level match, 3-frame
  crossfades, -14 LUFS / <= -1 dBTP on the encoded file, swishes) → export both folders → § 8 QA → § 9 REPORT → LESSONS.

## Sources (final)
| Code | File in raw/ | From | State |
|---|---|---|---|
| LDN02 a | LDN02_a_exposes_sony.mp4 | Henry\Michael jackson exposes sony.mp4 (his pull) | 640×358 29.875 fps, magenta cast, frontal: USED |
| LDN02 b | LDN02_b_rare_speech_1080p60.mp4 | Henry\...RARE Speech ... (Londra 2002).mp4 | 1440×1080 in 1080p60, fan camcorder, watermark: not used |
| EDDIE | EDDIE_Griffin_VladTV.mp4 | Henry\Eddie Griffin on Friendship with Michael Jackson... | 720p 23.976, VLADTV bug bottom-left, unbleeped |
| MATT | MATT_Fiddes_Dodge.mp4 | Lonely\Michael Jackson's Bodyguard_ Matt Fiddes.mp4 | 1080p25; host shot 1:47:43.46-45.86 |
| BASH | BASH_PeterPan_2003.mp4 | Henry\LIVING WITH MICHAEL 4K JACKSON PART 2.mp4 | 1080p 23.976 fan upscale, pillarboxed |
| JOEDOC | JOEDOC_Joe_Jackson_doc.mp4 | Henry\My Son, Michael Jackson - Joe Jackson ... (4K 2160p) | 1080p; Katherine 11:53, Joseph 14:02.5 |
| PUBLIC | PUBLIC_MJ_Paris.mp4 | Henry\Michael Jackson in Public.mp4 | 720p29.97; MJ hat + sunglasses 0:52 |

## In/out locks so far (SOURCE seconds; by ear = Whisper re-ASR of the window alone + wav2vec2 + 5 ms level strip)
| Beat | File | Words | In → out | Notes |
|---|---|---|---|---|
| 3 | MATT_Fiddes_Dodge.mp4 | "People think he's like this clown … He's shrewd behind it all" | 6460.82 → 6464.428 | in after a breath (6460.69-6460.79), /p/ burst 6460.85; "all" runs into "He's a clever dude" with no gap: out on the dip 6464.43 |
| 3 | same | "Two sides to him, you've got Katherine Jackson" | 6466.44 → 6467.905 | "yeah" 6466.305-6466.41 (Matt or Dodge) cut; in inside the /t/ closure dip before the burst 6466.455 |
| 3 | same | "very" (2nd) · "calm and loving, he had Joseph Jackson, who was a ruthless businessman" | 6468.50 → … → 6471.975 | v3 "is very, very" → "very": "is" is a −27 dB "z" 6467.915-6467.97, clean; 0.44 s pause very→calm tightened; out on the dip before "and" (6471.995) |
| 3 (v2) | same | "… and I see that guy put the specs on, he'd be like we're doing this, that deal, I'm not paying for that hotel (make sure they know I'm coming)" | → 6477.76 (6478.72) | v2 only |
| 4 | BASH_PeterPan_2003.mp4 | BASHIR "You don't want to grow up?" / MJ "No, I am Peter Pan" | 102.97 → 105.50 | "up" 103.87 → "No" 104.27 (0.40 s, tightened); "Pan" ends 105.47; doc music bed under it; next "Are you not" 107.09 |
- Words by ear vs the brief: "Katherine Jackson **is** very, very calm" (wav2vec2 "is" 0.88-0.97, "who's" 0.00); "he had / you had"
  and "who's a / who was a" unresolved by wav2vec2 (Whisper twice: "he had", "who was"): the caption pass re-ASRs the final cut.

## Job facts
- Format: AW short, 1080×1920, 30 fps export, full bleed, −14 LUFS / ≤ −1 dBTP on the encoded file, no music.
- Template job: `projects/patrick-stewart-father-angry/` (seq/edl.py, seq/preview.py, win/*, build/*, captions/*).
- Export: `E:\Shorts\Abudance Wisdom Shorts Exports\Final Renders\MJ Outthink Them.mov` + identical copy in
  `X:\Claude Projects\Exports\`. Never C:, no phone copy unless asked.
- GPU: one 8 GB card shared with the Patrick + Conrad Murray sessions: `nvidia-smi` before WhisperX / Topaz / finish
  render, one at a time; if busy, message the parent (local_3ae3a4cf), never kill another session's processes.
- Started by session local_3ae3a4cf (the parent); shared notes folder
  `C:\Users\affan\AppData\Roaming\Claude\side-session-notes\local_3ae3a4cf-7107-4cdf-a50e-e1b313072860\`.
