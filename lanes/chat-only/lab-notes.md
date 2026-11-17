# Chat-only lane: lab notes

- **2026-10-06: yt-dlp section downloads start the audio after the video (0.05–4.9 s).** The rough-cut tools read audio from
  time 0 of the stream while `splice.sh` trims on container time, so every cut landed early by the offset. Workaround (and
  rule): normalise at intake with `aresample=async=1:first_pts=0` (details: `.claude/skills/rough-cut/SKILL.md` § Gotchas).
  Found on batch 1 of the Onyx samples (`projects/mindsetmentor-23k-call`, 52 ms; `pomp-blockfi-ftx`, 4.86 s).

## 2026-10-06 — finalize.sh promotes a `--preview` render
`./finalize.sh <job>` picks the NEWEST render in `outputs/`, and the Onyx kits (`ig_build.py`/`yt_build.py --preview`) write the 720p
`*.preview.mp4` a moment after the full file, so the dry run said `PROMOTE <job>.sample-ig.v6.preview.mp4 -> <job>.final.mp4` and would have
DELETED the full-quality v6. Workaround until fixed: promote by hand (`cp outputs/<job>.sample-ig.vN.mp4 outputs/<job>.final.mp4`, then the
Downloads copy) and skip `--apply`. Fix to make: exclude `*.preview.mp4` from the promote candidates.

## 2026-10-06 — on Windows, Python's `/tmp` is NOT Git Bash's `/tmp`
A native-Windows Python resolves `/tmp/video-editor/<job>/cuts.json` against the CURRENT DRIVE (`X:\tmp\...`), while `splice.sh`
(Git Bash) reads `C:\Users\<you>\AppData\Local\Temp\video-editor\...`. A re-cut written from Python silently left splice
replaying the stale EDL. Workaround: write the EDL from bash, or resolve the path with `cygpath -w /tmp/video-editor/<job>` first.
(A stray `X:\tmp\video-editor\rationalmale-hacked\cuts.json` from this mistake is safe to delete.)

## 2026-10-28 · YT Shorts kit: head tracking lags a fast head at jump cuts (CA-009 Short)
- **Symptom:** `head_track` (track_eye, sigma 12, linear edge blend) left the eyes 100-140 px off at three in-shot joints of a
  fast-moving speaker (short takes, a hand gesture). An offline replay at sigma 3 still gave 132 px.
- **Workaround:** `head_track: false` (the chained eye lock) plus the new opt-in spec key `head_chain_n: 2` (default 4) in
  kit/yt_picture.py `eye_track`.
- **Gate:** step the eye midpoint across each in-A joint on the delivered frames. Script:
  `projects/iphone-duo-clip-angle/clips/reupload-wont-go-viral/work/head_snap_gate.py`.

## 2026-11-06 · YT Shorts kit, Afterhours mic (`projects/gta6-head-start`)
- **WhisperX collapses restarts on this mic, and an RMS read does not show them.** The first sequencing said "one clean pass"; four lines had
  restarts and the lengths were 3 s out. Workaround: per-burst faster-whisper (`work/cut/bursts.json`), force-aligned burst by burst
  (`work/cut/align_bursts.py`), `FW_DEVICE=cpu` while the GPU lock is held. Rule: no takes or lengths quoted before the burst pass.
- **A doubled word in a verbatim read can be a Whisper window seam.** "obviously obviously" read once on a re-read of the slice, both passes;
  "don't - don't" appeared only with the filler prompt. Test: a stumble counts only if it reads the same with and without that prompt.
- **`workflows/grade-picture.py` only knows whole shots.** A SPLIT is graded whole, so its drawn bottom panel shifts (channel pink 235,39,152 ->
  253,58,185) while every other card is excluded, and every non-A shot gets the DOC look, so a split's face does too. Workaround: set
  `grade_look` for DOC as well as A; `work/hook_panel.py` puts the panel back from `picture.whip.ungraded.mp4` after sharpen and keeps sharpen's
  fingerprint. Fix to make: a per-region exclusion in the grade.
- **POP defaults crush a low-key room** (mic and shirt to black, face dark orange). Set `grade_look` per job and test on stills before a full
  render; the approved numbers are in the channel's `LESSONS.md` 2026-11-06.
- **In a worktree session the Write/Edit hook blocked the main checkout even after a folder grant.** Writing from the shell needs his OK, and
  the OK covers only the paths he named.
- **ffmpeg range-converts every pixel of a rawvideo pipe when only the OUTPUT is tagged (2026-11-09, C1454 speck clean).** `-f rawvideo -pix_fmt yuv420p -i -` with `-colorspace bt709 -color_range tv` on the output shifted every pixel ~3.3 levels, so a "lossless" qp 0 file was not the source. Put the same `-color_range tv -colorspace bt709 -color_primaries bt709 -color_trc bt709` BEFORE `-i -` too; then the frames outside a patch are bit-identical (`projects/stop-remaking-viral-shorts/work/speck/verify.py`).
- **YT kit captions: never override the "main" voice in `captions.palette` (2026-11-09, AffanWiz Short 4).** A palette entry for "main" turns it into a solid-colour voice, so every caption came out the theme colour. For a theme colour, add ONE new voice (e.g. "green") for the emphasis chunks and leave "main" as the kit's white.
- **A "freeze-frame" beat on his own face = the kit's `fx: freeze` on the A shot, never a B card of a cropped still (2026-11-09).** A card cut against the live face is a same-camera jump (or a whip between same-camera shots) and skips the A grade; the kit freeze holds its own rendered frame, and the dated look goes in `overlay_extra`.
- **PIL card loops: draw on `cache.copy()`, never on a cached base image (2026-11-09).** Drawing onto the cached frame accumulated every earlier frame's sprites (a doubled check mark, trails).
- **Dandruff/speck removal: check the FINISHED Short at full size for MORE than one fleck (2026-11-09).** A second, 4x fainter particle (top-hat ~25-40 vs 100-140) never passed the raw detector and only showed after the 2x face upscale + Topaz + sharpen. An output-level fleck detector does not work (hair highlights at the hair top flag); prove it at the source (bit-exact outside the patch, top-hat at the tracked point) and by eye on the final.
- **A failed `yt_picture` step leaves the PREVIOUS picture in place, and grade, sharpen and the composite then ship the old frames (2026-11-09, AffanWiz Short 4 v6).** The 4K-base picture ran out of commit memory (other sessions' jobs + Premiere/AE/PS/AME held ~120 of 127 GB). `grade-picture.py` re-graded its kept `*.ungraded.*` copy of the OLD render, and the composite "succeeded" with the old cards. Gate the chain:
  1. after a picture build, require `step failed` absent from the log;
  2. require `picture.whip.*.ungraded.*` to be newer than the build start;
  3. only then grade, sharpen and composite.
  On a box near its commit limit, wait for free commit memory or use `--no-hq`; never let it grade blind.
  - **`--no-hq` softens the face shots.** When only CARDS changed, keep the Topaz faces instead:
    - render the picture `--no-hq`;
    - splice it per shot: A frames from the earlier HQ `picture.whip.ungraded.*`, B frames from the new render (`projects/stop-remaking-viral-shorts/work/splice_hq.py`). whip-slide builds every transition frame from ONE shot (shift + mirrored edge + smear), so the splice is exact.
    - Prove it first: per shot, the mean |dY| between the two sources. Untouched B shots read ~0.00, and A shots a steady ~2.7, which is sharpness only.
    - Copy the HQ `*.ungraded.*` away BEFORE grading, because the next grade overwrites it.
  - **A grade that dies mid-run (ArrayMemoryError) is safe to retry.** It leaves `picture.whip.mp4` ungraded and untouched, and refreshes the `*.ungraded.*` backup from it. Retry until its `*.graded.json` fingerprint is newer than the try.
- **AW code-build kit, `build/topaz_v2.py` (2026-11-09, Bieber):** `--redo --only S` silently rewrote every UNtargeted segment as a Topaz-less passthrough. The keep condition ignored `--only` when `--redo` was set. Fixed in `projects/bieber-walked-off-stage/build/` and `projects/mj-showed-his-mother/build/`; `projects/mj-son-step-outside/build/topaz_v2.py` still has the old line. Workaround if you meet it: hash `renders/topaz/*.mov` before any rerun and diff after.

- 2026-11-08 · `.claude/skills/rough-cut/scripts/transcribe.sh` only picks up .mov/.mp4/.mkv/.m4v in `raw/`; an audio-only `.m4a` is ignored ("No clips found"). Workaround: save audio-only pulls as `.mp4` (AAC in MP4). Seen re-transcribing two Scott episodes from the feed HLS (`research/viral2/retx.sh`).

- **2026-11-14 · Scott `pbd-urine-prank` build (a remote 2020 phone call, gated audio):**
  - **WhisperX runs ~0.15 s LATE on this gated source** (median faster-whisper minus WhisperX = -0.15 s in every row of the cut, -0.55 s on the first word after a 0.6 s digital silence). Caption clock = the verbatim faster-whisper PLAIN pass on the spliced cut (edit time) for every word the two agree on (difflib), WhisperX's text; then the RMS onset snap. Script: that job's `work/cut/retime.py`. Two PHANTOM words (the clipped front of a word before an in-point, a word that ends inside the next piece's first 30 ms) are dropped there.
  - **`PIL.ImageFont.font_variant()` RESETS a variable font's axes**: a Montserrat-VF `set_variation_by_axes([800])` font passed through `font_variant(size=...)` renders THIN (the default instance). Build the supersampled font again with the weight, never `font_variant` (job's `cards.py` `mont()` keeps `_wg`).
  - **Git Bash's `/tmp` is C:'s %TEMP% and cannot be remapped with TMP/TEMP**: `transcribe.sh` / `splice.sh` / `polish-boundaries.py` write their scratch to `/tmp/video-editor/<job>/`. To keep every intermediate on X: make that folder a directory junction to a folder in the job BEFORE the first run (`mklink /J C:\Users\<u>\AppData\Local\Temp\video-editor\<job> X:\...\<job>\work\tmp\scratch`; PowerShell, move any file already there).
  - **`npx hyperframes remove-background` loses a clear glass tube** (a urine sample tube came back as a floating cap and a smear of liquid): a photo of a transparent object goes in as a ROUNDED CARD (FX-33's own artifact is a rounded photo card), never a cut-out.
  - **YuNet misses ~30 % of the frames of a huge phone-selfie face** (a head ~540 px of a 1080 px frame, cut at the top): `head_track` interpolates between the detections (Gaussian +-3 sigma), fine; the face scan is `--step 1`.
  - **Wikimedia Commons DNS does not resolve on this machine (`curl: (6)`), but `en.wikipedia.org/w/api.php` returns `prop=imageinfo&iiprop=url|size|extmetadata` (license, author) for any `File:` title and `upload.wikimedia.org` serves the files (use a width from the thumbnail list: 1280 / 1920 / 3840).**

- **2026-11-14 · Scott `pbd-urine-prank` 60 fps final (Chronos + native cards):**
  - **`topaz-iris.py` writes its per-take intermediates to `%TEMP%` (C:, `tvai-*`, ~1 GB for a 41 s Short, deleted when the run ends).** Python's `tempfile` honours `TMP` / `TEMP`: start it as `TMP=<X: folder> TEMP=<X: folder> bash lock.sh gpu python workflows/topaz-iris.py ...` and nothing lands on C: (verified: the `tvai-*` folder appears under that folder).
  - **"Chronos failed on this take -> redone WITHOUT frame interpolation" can be TRANSIENT** (GPU contention with another session): the same take (a 138-frame card) failed twice alone and passed on the third try, a face take passed on the first. Cut the failed takes out of the c3 picture (ffmpeg `select between(n,a,b)`, ProRes), redo each alone through the lock, and put them back with an intra-only copy-concat (`-f concat` with inpoint / outpoint on frame boundaries, `-c copy`): the unchanged frames stay bit-identical.
  - **A card render that dies on a MemoryError leaves a TRUNCATED mp4 that looks fine**: check every clip's `nb_read_frames` against `dur x fps` before `mg60.py` (it dies with "card ran out" otherwise, or worse, holds the last frame).
  - **A call-window job needs no grade / sharpen pass at 60 fps** (they are baked inside the window at 30 fps by the job's picture engine): the Chronos input is the 30 fps picture itself.

- **2026-11-17 · AffanWiz Short 5 `ai-tools-rant` build (a `clips/` job on a joined 2-telling take):**
  - **Job-local scripts copied from a top-level job (`cardkit.py`, `cue_check.py`, `reading_gate.py`) compute `REPO = JOB/../..`, which is wrong for `projects/<parent>/clips/<name>`.** Walk up until a `presets/` folder exists (done in this job's copies). The kit's own scripts are fine (they resolve from their own location).
  - **`voice-gain.py` (called by `splice.sh`) needs the raw file inside `<job>/raw/` even when `cuts.json` names an absolute clip path.** For a clips job whose raw lives in the parent: `os.link(parent_raw, job_raw)` (a hardlink on the same drive; `cmd mklink /H` silently did nothing from Git Bash).
  - **WhisperX word starts ran 90-150 ms LATE on this take** (and one first-telling "weeks" ended 0.2 s after the real silence, so `export-transcript.py` leaked it into the next segment). Fix: read the real onsets off the 5 ms energy (`work/cut/bursts.py`), pin the EDL edges there (`no_refine`), and re-time the segment-first words (and that "weeks") in `transcript/words.json` (keep `words.whisperx.json`), then re-run `export-transcript.py`.
  - **A pause closed on his FACE is a visible jump even with `head_lock`:** a 0.56 s breath closed at 0.88 s of the hook stepped the background ~40 px (frame pair 52/53, `bg_strips.py` readings under 0.5 response are not trustworthy there). The hook's breath is now kept (one span). Check every face joint with a frame pair, not only the strip numbers.
  - **No SVG renderer on this machine (no cairosvg):** `yt/svgraster.py` flattens the path Beziers and fills them with PIL (4x supersample, XOR per subpath); fine for flat brand marks (Claude spark, Premiere Pr).
  - **Red test through the real overlay path:** build the job's overlay HTML (`yt_captions.py` + `yt_overlay.py`), copy `yt/hf-overlay/` per candidate, inject the POP-graded real frame as `#root`'s CSS background, then `npx hyperframes@0.8.16 snapshot . --at <t> --no-end --describe false`. `work/red-test/make_test.py`.
  - **Memory:** other sessions held the box near its commit limit (0.4-5 GB free): numpy needs `OPENBLAS_NUM_THREADS=1`, large-v3 on CPU died with `mkl_malloc` twice, `uv`/spawn failed with `EUNKNOWN`. `work/mem.py <GB>` waits for commit headroom; `work/finish.sh` wraps every heavy step in wait + retry gated on its own output.

- **2026-11-17 · AffanWiz Short 6 `research-agent` build (same take as Short 5):**
  - **WhisperX was 0.14-0.25 s late on single words ("the" 240.86 vs real 240.61), and "so a normal" has no energy valley.** Edges come from `work/cut/runs.py` (voiced runs at -38 dB, 5 ms) + `prof.py` (10 ms dB profile); the line-3 "so" was taken out on the 262.88 dip and the verbatim faster-whisper pass on the cut heard "a normal person" (no "so"). Delete a dropped word from YOUR copy of words.json, otherwise export-transcript keeps a 10 ms sliver of it in the captions.
  - **An end-edge 0.015 s later (332.175 vs 332.16) tripped audio-qa AMBIENCE HOLE at the next joint (-9 dB)**; the earlier edge passed. Re-splice cost 3 min under memory pressure.
  - **A flipped SPLIT (`"flip": true`, B-roll above, speaker below) needs `split.bob_amp: 0` and a panel card of exactly 1080 x (seam+4); the speaker half is NOT head-tracked** (`track=False`): `fy_out` 0.42 / `z0` 1.15 puts the face at y ~1200-1620 under a 0.9 s hook slide-out only if the split starts ~0.5 s after the hold ends. Add SPLIT ranges to `reading_gate.py` (it only looked at kind A).
  - **PIL `ImageDraw.Draw(im, "RGBA")` on an RGBA frame with alpha 0 still leaves the RGB behind once the frame is written as RGB** (a faded gold line stayed visible): stop drawing at alpha 0.
