# RUN: mj-the-dad-he-never-had ("The Dad Michael Never Had 🥹"), Abundance Wisdom Short: RAW CUT (STOP 1) placed in Affan's ABW11

## ▶ STATUS: resume here
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
