# REVIEW 1 → v3 (16 Nov 2026 ~18:40-19:25 PKT, his three notes on v2, a finish re-render, not a rebuild)
- **v3 ships.** `outputs/The Dad Michael Never Had.mov` (= `… v3.mov`): 2183 frames, 60 fps, 36.383 s, -14.1 LUFS, -1.6 dBTP, export QA PASS. Hash-identical copies (sha256 `e9ef733d…e92287`):
  - `E:\Shorts\Abudance Wisdom Shorts Exports\Final Renders\The Dad Michael Never Had.mov`
  - `X:\Claude Projects\Exports\The Dad Michael Never Had.mov`
  - Both replaced the v2 copies there (checked as `2f0f7506…` first). v2 is kept as `outputs/The Dad Michael Never Had v2.mov`.
- **His notes, and what changed:**
  1. **"It's not 'as you could', it's 'as he could'."** Fixed in the caption (18.65-19.52 s). Forced alignment re-run: same word timing, only the word changed. Whisper and the Tella transcript both heard "you"; his ear wins.
  2. **The Michael "Do you like being a father?" shot (Walters 1997, 24.30-26.27 s) was too pixelated.** He offered "enhance it using Topaz properly … or letterbox". It stays full frame, now with real Topaz Iris.
  3. **The little Paris clip (31.92-36.38 s) was still pixelated: "I don't know how it's still pixelated when you used Topaz".** The honest answer: **v1/v2 never ran an upscale model on either shot.** They got only Chronos (frame smoothing), on a frame already blown up 2.7x and 3.4x, plus a light hqdn3d denoise on Paris. That was my spec's "no Iris on SD / a child's face" rule, carried over from the small-face "pasty" lesson.
- **The fix for 2 and 3:**
  - Topaz Iris (his recipe values) x4 runs on the ORIGINAL source at its native size (960x720 / 480x360), before the shot is magnified (`build/hd_sources.py`).
  - Stage A reads the enhanced copy with exactly the same framing: anchor x k, scale / k (`build/stage_a.py` `hd` key, `build/v3_patch.py`).
  - **Iris vs Proteus A/B** (his values, `proof/v3/enh_ab_*.jpg`): Proteus only blurred the blocks; Iris removed them, and both faces stay recognisably themselves.
  - Paris is still on frame as he placed her. Her face now carries an AI face-recovery pass (Iris), done because he asked for Topaz; it rebuilds detail from her own frames.
  - Whether Iris on SD faces becomes a standing rule is PENDING his reaction to v3 (LESSONS and the Topaz memory say so).
- **Proof:**
  - **Same framing as v2:** ECC shift ≤ 0.5 canvas px and scale 1.000-1.001 on 9 checked frames (`proof/v3/sa_v3_check.txt`).
  - **The enhanced files line up:** the Walters extraction is frame-exact (diff 0.000), and Topaz keeps frames one-to-one (motion signature corr 0.997 at lag 0, 0.87 at ±1). Paris registration PASS (`proof/v3/hd_*_reg*.txt`).
  - **Graded at phone size, v2 vs v3:** `proof/v3/graded_phone_v2_v3.jpg` and `graded_crop_v2_v3.jpg`.
  - **No boiling:**
    - the kit's smooth_check passes on S14, S19 and S20 (0 % duplicate frames; judder 6.61 / 2.40 / 1.72, v2 6.73 / 2.44 / 1.75) (`proof/v3/smooth_check_v3.txt`);
    - full-resolution face sharpness swings frame to frame as much as v2's (S14 18.5 vs 18.6 %; Paris 5.7-6.9 vs 6.5-7.1 %), with no 6-frame pulse (`proof/v3/beat_check.txt`);
    - 12 consecutive frames through Michael's blink are steady (`proof/v3/blink_strip_v3.jpg`).
  - **v3 differs from v2 only where intended:** the caption chunk (17.6-24.3 s, encoder ripple included), S14 and the Paris clip. Every other frame is ≤ 0.05 mean diff, and the audio is byte-identical (same mix.wav, md5 `16c8b949…`) (`proof/v3/v3_vs_v2.txt`).
  - **Caption and edges:** the caption reads AS HE COULD (`proof/v3/caption_as_he_could.jpg`), and the edges around every changed cut are clean, with no watermark (`proof/v3/v3_edges.jpg`).
- **Noticed, not changed:** Paris is now clean but still soft at ~4x on the canvas, because that is the detail the 480x360 source holds. If he still finds it soft, the next step is less magnification in the letterbox (a framing change), not more AI.
- Lessons → AW `LESSONS.md` "2026-11-16 · The Dad Michael Never Had v2: his review 1". Topaz memory updated.

# MORNING SUMMARY (16 Nov 2026, built overnight 07:00-09:05 PKT, no questions asked, by his rule)
- **DONE: v2 is the version that ships.** `outputs/The Dad Michael Never Had.mov` (= `… v2.mov`): 1080x1920, 60 fps, 2183 frames, 36.38 s, -14.1 LUFS (LRA 2.5), -1.6 dBTP, PCM 24-bit. Hash-identical copies (sha256 `2f0f7506…454ecd`):
  - `E:\Shorts\Abudance Wisdom Shorts Exports\Final Renders\The Dad Michael Never Had.mov`
  - `X:\Claude Projects\Exports\The Dad Michael Never Had.mov`
- **What it is:** his own cut (snapshot of his ABW11 sequence, every trim kept) + every note from his Tella walkthrough, on the house style (the Son build's code pipeline: head lock, zoom, transitions, his AE grade in code, CapCut-style captions, low labels, two subscribe prompts, soft SFX, no music, no end screen). ABW11 was only READ (one FCP XML snapshot); nothing in Premiere was changed, saved or exported.
- **Three things to know first:**
  1. **Higgsfield was NOT used** on the young-Michael-and-Joseph still, though he asked: paid credits need his per-spend OK overnight, and his 14 Nov rule bars a generative upscale of a real face from a soft source. It is a Lanczos resize of the documentary's B&W photo. Say the word and it gets the Higgsfield pass.
  2. **The movie beating overlay is in gentle slow motion (my addition):** the two hits are 0.96 s and 0.63 s under lines of 1.38 s and 0.97 s. His lesson says slow motion is shown as a test first; real speed is a one-line change.
  3. **The end is his child clip with Paris on frame** (his own placement and his "end with this"): the one real-life child on frame.
- **v2 vs v1:** v2 fixes two same-camera jump-cut head hops that broke his head-steady rule. Michael/Oprah at 7.48 s went from dy 25 px to dx 6.3 / dy 2.5. Prince at 27.65 s went from dy 69 px to dx -1.6 / dy 6.2 (gate 8 px). The fix is 183 % / 234 % scale on those four shots with a y lock; the green edge and lower third stay out. v1 is kept as `outputs/The Dad Michael Never Had v1.mov` (sha256 `c1be2701…`, hub-verified).
- **Noticed, not changed:**
  - captions sit on one base (his rule), so on 13.3-14.8 s and 17.1-19.5 s, where Michael sits low in the 2003 frame, the line crosses his lower face;
  - Walters (1997) and the child clip are soft at their magnification: the source quality.
- **Full list of overnight decisions:** "Decided without Affan" below. Proof: `proof/final_sheet.jpg` (every 0.5 s), `proof/final_edges.jpg`, `build/BUILD-LOG.md`.

# RUN: mj-the-dad-he-never-had ("The Dad Michael Never Had 🥹"), Abundance Wisdom Short: RAW CUT (STOP 1) placed in Affan's ABW11

## ▶ STATUS: resume here
- **16 Nov ~19:25 PKT: FINAL = v3 DELIVERED** after his review 1 (see "REVIEW 1 → v3" at the top). Waiting for his next look. A note = a finish re-render on the v3 chain: `renders/stageT_v3.mov` → `build/render_chunks_v3.sh` → `export_cta.py`. Do NOT re-run `make_timeline.py`: it rewrites centers.json; v3's patch is `build/v3_patch.py`.
- **16 Nov ~10:00 PKT: FINAL = v2 DELIVERED** (see the morning summary above; v1 09:05 kept as `… v1.mov`). Captions trail the speech by up to ~0.18 s (house CapCut lateness). Waiting for his review; a note = a finish re-render (`build/`), not a rebuild.
- **Resume:** the plan is `BUILD-SPEC.md` (cut, pictures, finish settings, pipeline, gotchas) and the notes are `BRIEF.md`; a Sonnet builder executes it, with checkpoints at the stills and at the end.
- **16 Nov 2026 07:00 PKT: OVERNIGHT FINISH BUILD STARTED** (AW hub + Main Brain overnight rules: run to the final render with no questions; decisions logged under "Decided without Affan"; cap 10% weekly usage; Opus manages, Sonnet executes, Fable advises). Weekly meter read 0% at 07:00. Steps: walkthrough → read-only FCP XML snapshot of his sequence → code build on the mj-son-step-outside house style → final.
- **15 Nov 2026 09:52-10:22 PKT (machine clock): the raw cut is PLACED in Affan's open ABW11 and READ BACK = PASS. Waiting for his review. STOP 1 reached; the finish (STOP 2) waits for his OK.**
  - Sequence **"The Dad Michael Never Had - raw cut"** (bin "The Dad Michael Never Had", ABW11.prproj): 1080x1920, **60 fps** (his Sequence 02 template, cloned, no setSettings), **57.30 s** (3438 frames, ≤ 60 s with every approved word),
    V1/A1 19 clips (17 spans; B5 and B8 each split at a shot change), V2 1 cover, A2 4 clips (MUTED), 8 markers (one per beat start). Proof: [`premiere/READBACK.md`](premiere/READBACK.md) = PASS.
  - **Window 09:52:35-09:52:49 (14 s)**, he had been idle 401 s (quiet gate read inside the lock: idle ≥ 150 s, playhead steady over 4 s). His active sequence ("Was Oldman A Good Sirius - raw cut",
    `4983e3f2…`) was restored by id; **his playhead ticks are identical before and after (8259537686400)**; his Sequence 02 is untouched (26 clips before and after). Two further by-name windows on OUR sequence only (no activation, no import): 09:53:50-09:53:53 (exact A2 in-points) and **10:22:26-10:22:30** (A2 in-points moved by the denoise filter's measured 24.9 ms delay; he had been idle 180 s): his id and ticks identical both times. **No save, no export. ABW11 is NOT saved: the new sequence needs his Ctrl+S.**
  - Lock: `premiere.lock` taken for both windows and released. QUIET-MODE was absent, so I read `quietgate.py status` myself before each window (rule in lab-notes 2026-11-15).
- **For him to decide (first lines of the report too):**
  1. **The two beds are DENOISED, not isolated.** Demucs cannot run here: its htdemucs weights are not on disk (`~/.cache/torch/hub/checkpoints` holds only a wav2vec2 file), the demucs venv is CPU-only torch 2.3.1 (no GPU path, so no `gpu.lock` job),
     and downloads are barred. The muted A2 holds ffmpeg `afftdn` spectral denoise versions (beats 5 and 7). Measured on the placed spans (voice P90 over floor P10 of 20 ms frames): **beat 7 13.7 → 23.8 dB (+10.1)**, voice -1.0 dB; **beat 5 22.6 → 30.2 dB (+7.6)**, voice -0.2 dB. The filter delays its output by 24.9 ms (found by cross-correlating each A2 span with its A1 twin, peak correlation 0.89-0.98), so the A2 in-points are the A1 ones + that lag and A2 lines up with A1 to < 1 ms.
     That is noise reduction, never separation (no music is removed from under a word). **I could not listen.** Recommendation: beat 7 use A2 if it does not sound watery (it is the worst bed in the cut); beat 5 keep A1 (the bed is already ~23 dB under). To compare, disable the A1 clip of the beat and unmute A2.
     True Demucs needs his OK for an ~80 MB official weights download plus RAM headroom (commit was at 91.0 of 91.2 GB at 09:55, see Disclosures).
  2. **Beat 6 has no V2 cover.** The brief said "cover on V2"; a cover would leave Paris at 14 on V1 under it. The picture is on V1 itself: a HYBRID file (her audio from Part 2 + Michael's adult picture from the vlog archive), so **no frame of her exists in the Premiere project or in any file I made.** Tell me if he wants it literally.
  3. **The brief's times were aligner numbers and were wrong for 4 spans** (details below). All were corrected from the 5 ms envelope + a silent re-read; he is hearing the corrected cut. Beat 2 now starts on Oprah's "Were you scared of him?" (his own words), not "And were…".
  4. Pauses: only the pads between spans are closed (about 0.11 s each); beat 1's 1.3 s pause before "He said, I'm not Daddy", beat 7's 1.0 s pause and beat 5's 0.6 s pause are kept whole (his natural-speech rule; the cut is under 60 s anyway). Q→A joins in beat 3 are tight (0.11 s): an extra breath is a one-frame-count change.
  5. Beat 7 sits 1.7 LU low on purpose: its review gain is +5.3 dB, not the +7.0 that matches -17 LUFS (its source is dynamic: one transient, source 84.49 = timeline 47.2 s, peaks **+2.4 dBFS** after +5.3 and would sit near +4.1 dBFS after +7.0). It ticks on playback until the finish limiter. (My cap rule read a mono-decoded percentile that was 3 dB hot; I left the placed +5.3.)
  6. **Beat 6's picture shows Michael visibly talking (a home-video archive) under Paris's voice**, in both lines. Fine as a placeholder; the finish may want a different insert or a hold.
  7. **Beat 8's wide studio shot is framed on Alex Cooper (the host asking)**, so her face is small in the 9:16 crop; at STOP 2 it could be the AW blurred-fill letterbox or framed on Paris.
  8. (checked, not a decision) The denoised audio reads **word for word like A1** in the same silent ASR pass (`raw/denoise_gapped.small.en.txt`; only "anytime" / "any time" differs), so the denoise costs no intelligibility.
- **By ear (machine readings, I played nothing):** the lines are confirmed by two silent ASR passes (each span alone between silences, and the cut as placed): see "Listening".
- **Next:** his review → notes into this file; then STOP 2 only after his OK (head lock and the zoom table incl. beat 3's size jumps, captions, labels, 2 subtle subscribe prompts, SFX, his AE grade; no music bed, no end screen).

## Decided without Affan (16 Nov overnight, no questions by his rule; evidence beside each)
- **His cut is the base** (read-only FCP XML + readback 07:02, `snapshot/`): 36.23 s; every trim of his kept, including two that look odd. Beat 3 ends "…stop it, you're gonna", cut in the dip before "kill"; Walters's "Do you" has its "D" trimmed. Creator's hand = decision. Noticed, not changed.
- **His end clip** `Paris Jackson_ I Love My Daddy So Much.mp4` (Paris as a small child, ON FRAME) is kept as he cut it: his placement in his own cut, and his walkthrough says "end with this". It is the one real-life child on frame in the Short.
- **N1 Higgsfield NOT used:** paid credits need his per-spend OK (hub rule). His 14 Nov rule bars a generative upscale on a real face from a soft source. The still of young Michael + Joseph is a Lanczos resize.
- **N3 "regurgitate":** "-tate" ends with its final /t/ release at 1206.04-1206.06 (pitch-continuous with Michael; Oprah's next word starts 1206.57). Out = 1206.1067: +9 frames on his cut, as he asked ("five or eight extra frames"). Everything after shifts +0.15 s; END 36.383 s.
- **N4 movie scene:** Popcorn Picks "The Jackson Family's Harsh Beginning (Colman Domingo) | Michael" (YouTube `IdC5kzSwkoM`), downloaded through pace.sh, H.264, `sources/IdC5kzSwkoM/`. "Start from here, he's actually beating him" = the wide hallway swing at 255.59 (the frame he paused on). His two V2 pieces become two beats of the scene: 255.6-256.5 under "Ironing cords", 260.4-261.0 under "Whatever's around", each in gentle slow motion (Chronos, ~0.7x) to fill the line. The film's flower logo is cropped.
- **N2 Joe:** "EXCLUSIVE LEAK: Joe Jackson's FULL interview" (the one he pointed at), the stern close-up at 405.6-407.0, Chronos 0.5x to fill 2.78 s. The TV One/NewsOne strip (y > 985) is cropped.
- **N7 / Demucs:** he called the A2 denoise "extracted audios, but whatever", so original audio throughout; no Demucs, no download.
- **Slow motion on the movie beating (S09/S10) is MY addition.** He asked for slow motion only on Joe (N2). The two movie beats are 0.96 s and 0.63 s, under lines of 1.38 s and 0.97 s, so a gentle Chronos ~0.7x fills them. His lesson says slow motion is shown as a test first: easy to switch to real speed (hold or extend) at his word.
- **Picks the walkthrough left open:**
  - Joe = the stern close-up at 405.6 s, slowed 0.5x.
  - Katherine = 60 Minutes Australia (his "60 Minutes"), a silent grieving shot at 1089.3-1091.3.
  - Prince listening = Sunrise 171.62-173.0, the only true listening shot in that interview: a warm listening face, not a hard stare.
  - The still = the documentary's B&W photo of Joe and Michael (~12) in tuxes, the only clear two-shot on disk (no photo files exist).
- **Labels:** Joe, Katherine and Prince only (low). No label on Michael (the Son build didn't label him) and none on Paris: the second subscribe prompt sits there and labels never share a CTA. The question and the ending make clear she is his daughter.
- **Subscribe prompts:** 11.75 s (32 %, on face shots, kept off the beating) and 28.13 s (77 %), using the existing 60 fps CTA render. **"Boom" = a white-flash transition into "Do you like being a father?"**
- **Enhancement:**
  - Iris only where the source is native HD, decided on A/B stills for P3/OPR.
  - His child ending gets Chronos + light denoise + Lanczos, no generative face model. That is his "different enhancement for old footage", inside his Katherine rule.
- **Checkpoint 1 (stills of all 20 shots) reviewed and passed at ~08:45.**
  - No Iris on P3/OPR: the A/B showed invented skin texture and plastic lips. The ending's band is narrower ([520,1320]) so the 480x360 child clip isn't blown up 4x.
  - The "Jackson 5 Childhood Scene" file was not used: 30 fps with a duplicate every 5th frame, letterboxed, lower bitrate, no sharper.
  - **Captions keep ONE base** (his rule), so on S08 and S11, where Michael sits low in the 2003 frame, the line crosses his lower face.
- **Side note:** the sourcing helper registered a `dad-build` slug in `research/deep-research-2026-11-14/yt_api.py` (SESSIONS set) to run one search (~100 units).

## What is on the timeline (read back from Premiere)
| beat | timeline | label (low, STOP 2) | spans (source) | words |
|---|---|---|---|---|
| 1 | 0.00-8.23 | MICHAEL · 2003 | Living With Michael Jackson Part 3, 173.148-181.381 | He didn't allow us to call him Daddy. And I wanted to call him Daddy so bad. He said, I'm not Daddy. I'm Joseph to you. |
| 2 | 8.23-15.93 | MICHAEL · 1993 | Oprah 1993 (upscale), 1198.140-1205.840, one continuous take | [Oprah: Were you scared of him?] Very frightened. There's been times when he'd come to see me and I would get sick. [Really?] I'd start to regurgitate. |
| 3 | 15.93-33.72 | MICHAEL · 2003 | Part 3: 29.880-31.363 · 39.830-41.513 · 43.230-45.163 · 47.213-48.596 · 50.880-51.930 · 54.113-56.463 · 70.813-78.713 | [Bashir: Would he only use a belt?] No, more than a belt. [What else would he use to hit you with?] Ironing cords. Whatever's around. Throw you up against the wall as hard as you could. … I just remember hearing my mother scream, Joe, you're gonna kill him, you're gonna kill him, stop it, you're gonna kill him. ("Why do you do this to me?" is OUT) |
| 4 | 33.72-35.85 | MICHAEL · 1997 | Walters 1997, 598.423-600.557 | [Walters: Do you like being a father?] I love it. |
| 5 | 35.85-41.20 | PRINCE · HIS SON | Sunrise Apr 2026, 77.490-82.840 (split at 79.207) | [Host: (But) what was he like as a dad?] Awesome. Really fun to just spend time with. |
| 6 | 41.20-43.12 | PARIS · HIS DAUGHTER, 2012 | Part 2 AUDIO ONLY: 261.400-262.433 · 271.440-272.323; picture = vlog archive 121.0-122.9 (Michael, adult) | He was awesome. … He was my best friend. |
| 7 | 43.12-53.53 | PRINCE · 2026 | Prince's vlog: 80.425-85.592 · 87.725-92.975 | I'm very particular about how I tie my tie, because my dad taught me how to tie my tie. … that's a piece of him that I bring with me anytime I try to show up and represent for him. |
| 8 | 53.53-57.30 | PARIS · 2026 | Call Her Daddy: 639.338-641.155 (wide shot, then Paris from 641.057) · 642.138-644.088 | [Alex Cooper: how would you have described your dad?] Really funny guy. That was my best friend. (hard cut; the picture ends before the host's first frame at 644.1018) |
- **V2:** `SunCover` 36.567-37.567 = a held photo frame (Sunrise 78.20, the last clean frame) over source 78.22-79.20, where the broadcast's frames are corrupt, then dissolve into Prince. V1 below it is B5's photo clip, which ends at 79.207.
- **A2 (muted):** denoise versions of beats 5 and 7 (4 clips), level-matched with their A1 twins; in-points = the A1 ones + 24.9 ms (the filter delay), residual cross-correlation lag **0 samples** (`proof/a2_align_after_fix.txt`).
- **Framing (static per span; head lock and zoom are STOP 2):** fill-height (1920 / source height) with the speaker's face centred (YuNet), except beat 2 (scale 180, window starts at source y 10: the Oprah upscale has a 6 px green artifact along its top edge), beat 4 (266.7, window x 226-631 of 960: clears the burned-in RTL logo at x 50-197)
  and beat 5 (scale 230, window top-aligned, source y 0-835: clears the Channel 7 lower third whose bar starts at y 871). First and last placed frame of every span: `proof/framing_A_B1-B4.jpg`, `proof/framing_B_B5-B8.jpg` (rendered from the mezzanines with the placed Scale/Position).
- **Review levels (Volume > Level, not a mix):** kept audio of each beat to -17 LUFS integrated, one gain per beat:

  | beat | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
  |---|---|---|---|---|---|---|---|---|
  | measured LUFS | -18.1 | -20.0 | -19.0 | -17.7 | -13.9 | -19.8 | -24.0 | -16.6 |
  | gain dB | +1.1 | +3.0 | +2.0 | +0.7 | -3.1 | +2.8 | **+5.3** (not +7.0) | -0.4 |
  | result LUFS | -17.0 | -17.0 | -17.0 | -17.0 | -17.0 | -17.0 | -18.7 | -17.0 |

  Sample peaks after gain stay ≤ -1.8 dBFS except beat 7's one transient (+2.4; +4.1 at a full match). Part 2 (beat 6) had never been measured: -19.8 LUFS. The Level is a review gain: set it to 0 dB to remove it. The static -6 dBFS limiter and the master target belong to the finish.

## Listening (silent: ASR, spectra, lips; nothing was played)
- **Method:** the 5 ms envelope + band energies for every edge; small.en CPU (under `.asr-lock`, available RAM and commit checked each time) on (a) every span alone between 1 s of silence (`raw/gapped.*`), (b) the cut exactly as placed (`raw/assembled_cut.*`), (c) candidate-edge variants (`raw/var_*`). Both reads agree with the approved words (see READBACK.md).
- **What the re-reads corrected** (each was a real defect in the brief's numbers, which are WhisperX aligner times):
  - **Beat 1** started 0.65 s early (172.5 vs the real onset of "He" at 173.19: 0.7 s of dead air at the very top of the Short).
  - **Beat 2** started inside Michael's own trailing "you know, and" (1197.74); Oprah's question begins at ~1198.2 and has no "And". Now 1198.14 (quiet 1198.04-1198.2).
  - **"Ironing cords."** lost its final /s/ (a devoiced 0.29 s sibilant, 48.23-48.52, after a silent /d/ closure): out now 48.596.
  - **Beat 7** let "But" through (the vlog's "but" ends at ~80.40) and clipped "him" ("for it"): in 80.425, out 92.975.
  - Also: beat 3's "Throw" starts at 54.20 (not 53.82: 0.3 s of dead start), and the brief's out for beat 1 (181.05) would have cut "to yo-" (the "you" runs to 181.30).
- **Beat 6 (the check the brief asked for):** Part 2 reads (small.en, 254-276): Paris: "…he was just an awesome, like, down-to-earth, old soul. **He was awesome.**" (261.50-262.30) · interviewer: "Old soul?" (263.74), "What was your relationship like? What was the dynamic?" (265.9-268.3) · Paris: "Well, we were like, **he was my best friend.**" (271.24-272.44).
  So the small.en 'you're just' was **"he was just"**: no interviewer in the 258-261 stretch. **Who speaks:** she is the only person on screen in one unbroken shot, and her mouth moves with both lines (lip motion 7.4/6.3/3.9 over "he was my best friend", 2.5-1.2 over "he was awesome", against 0.1-0.4 when still) and is still while the interviewer asks (265.9-268.3: 0.4-1.6); the interviewer's lines are also 10-15 dB quieter on the file.
  `proof/lips_p2_mouth_vs_audio.txt`, `proof/p2_frames_grid.jpg`. **6B holds; no fallback to 6A.** Edges: "best friend." is followed by a clean gap (the next speech is ~2 s later, at 274.25), so no "we were kind of" leaks; the first span begins in a 130 ms dip after "soul".
- **Sunrise's corrupt-video window has clean audio** (scan of 78.2-79.3 on the file's own audio: no zero run ≥ 1 ms, no sample jump over 12x the local step, no 5 ms level step over 12 dB): the host's question ends at ~78.65 and the bed sits at -28 to -39 dBFS after it. `proof/a2_align_and_sunrise_glitch_scan.txt`.
- **Not settled by a machine:** whether the A2 denoise sounds natural; the 15 ms equal-power crossfades (finish); beat 3's hard cut after "him" (78.71) runs straight into "you know" in the source, so it is a cut inside continuous voiced speech (the ASR reads "him" and no "you" after it).

## Minors check (every new picture)
- **Beat 6 picture** (the only new cutaway): `shots.py` on the finished hybrid files (`proof/shots_m6a_*.jpg`, `proof/shots_m6b_*.jpg`: no cuts) **plus** a frame every 0.1 s across both files, handles included (`proof/b6_hybrid_dense.jpg`, 31 frames): Michael alone in a red shirt and sunglasses, adult, no logos. The archive insert it is cut from ends on a toddler at 135.5-137.3 and starts with a second person at 118.0: neither is used (121.0-122.9 only).
  Paris's own picture was never extracted: the hybrid maps her AUDIO stream only.
- **Beat 5 cover / photo:** the photo is Michael (masked, hat) with Debbie Rowe (adults); every source frame 78.12-79.52 inspected (`proof/sun_corrupt_sheet.jpg`): clean to 78.20, glitching 78.24-78.56, a photo→Prince dissolve 78.60-79.04, clean Prince from 79.08.
  The cover (the held 78.20 frame) hides 78.22-79.20.
- **Beats 1, 2, 3, 4, 7, 8:** first-and-last-frame checks of the planned windows in `research/deep-research-2026-11-14/ig-mj/proof/d2_*`, plus the first and last PLACED frame of every span in the two framing sheets. Beat 8's file ends at 644.0884, before the host's first frame (644.1018, scene score 0.41); the wide→close-up cut is frame-exact (641.0571, score 0.50).

## Disclosures
- **ASR:** small.en on CPU only (three silent passes + two variant passes + the Part 2/Walters/Sunrise windows), each under `.asr-lock`, with my own guard (available RAM ≥ 2.5-4 GB and commit headroom ≥ 5 GB). No large-v3, no GPU job, no `gpu.lock`. Premiere stayed responsive throughout.
- **Memory incident (not mine):** at 09:55 commit stood at **91.0 of 91.2 GB** and available RAM at 1.5 GB (OpenBLAS could not allocate): Premiere 16.3 GB private, Adobe Media Encoder 7.0 GB, Photoshop 4.5 GB, Tella 2.2 GB, all his. Nothing of mine was running (the last ASR had ended); by 09:56 commit eased to 89.6 GB. I ran no ASR or numpy-heavy step during it (the last metrics ran single-threaded).
- **Checks added after the advisor's read:** A2-vs-A1 cross-correlation (it found the 24.9 ms filter delay above), a stale-proof re-render (the framing sheets in `proof/` are from the FINAL edges and crops; beat 2's green top edge is gone), the Sunrise audio scan.
- **Downloads: none.** `uv run --offline` (cv2/pillow from the uv cache). Sources all on disk.
- **Premiere calls:** read-only state checks (`--check`, ×2) without the lock; the two lock windows above; a final read-only read-back window (see the log). Nothing saved, exported, closed or restarted.
- **Two bugs found and fixed in the same session:** (1) an audio-only item's in-point floors to a 29.97 grid when placed (the four A2 clips landed 17-33 ms early); `clip.inPoint = Time` afterwards sets it exactly and leaves start/end alone (read back); (2) the afftdn denoise delays its output by 24.9 ms, found only by cross-correlating A2 against A1, fixed the same way.
- **Files you can delete:** `raw/` (analysis windows), `seq_src/` is what Premiere imported (keep while the project uses it), `proof/_*.png` none left.

## How it was built (re-run recipe)
`analysis/pieces.py` (approved spans) → `analysis/edges.py` (the REAL `polish-boundaries.py` on a job-local words/cuts: its ⚠ lines were the list of edges to re-read) → `analysis/strip.py` / `bursts.py` (5 ms envelope) → `premiere/cutlist.py` (final edges on the 60 fps grid, timeline, cover, markers) →
`premiere/make_mezz.py` (H.264 crf 12 + PCM mezzanines, `setpts=PTS-STARTPTS,fps=60:round=up`, cut on a source-frame boundary) + `analysis/denoise_build.py` (A2 WAVs) → `analysis/faces.py`, `analysis/levels.py` → `premiere/build_place.py` → `premiere/run_window.py --check | --run | --fix-a2 | --readback` → `premiere/verify_readback.py` → READBACK.md.
A NEW sequence needs a new name (the driver refuses to rebuild over an existing one); edit the spans in `cutlist.py`, rebuild the changed mezzanine, and re-run from `build_place.py`.

## History
- **15 Nov 2026 ~09:00 PKT:** Affan approved his own eight-beat sequence ("build this in premiere"): his lines as pasted, Paris audio only in beat 6, beat 6 = the Part 2 line. Research: `PITCH.md` v2.0, spec: `BUILD-BRIEF.md`.
- **09:15-09:51:** edges measured and corrected, mezzanines, covers, denoise versions, framing and levels built offline (no Premiere call except two read-only state reads).
- **09:52:** window; **09:53:** A2 in-point fix; **10:00-10:22:** advisor checks (A2 alignment, stale proofs, READBACK text, Sunrise audio scan), second A2 correction at 10:22. Build session started by the hub (`local_6dacb48e…`), Sonnet.
