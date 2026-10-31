# Onyx sample Shorts, YouTube look: LESSONS

Each entry: **lesson → change made → file.** A lesson that repeats becomes a README number or a PLAYBOOK rule.

## 2026-10-05: the brief and the reference (before the first build)

- **The platform picks the look.** Affan, after the MFM pilot: *"this is a classic minimalistic Instagram style… if you're aiming for YouTube
  that's gonna be a different style… whenever we are going to make a sample we are going to make it depending on what their prioritized
  platform is."* → This preset, plus § 0 in the shared PLAYBOOK (`presets/youtube-shorts/onyx-samples/PLAYBOOK.md`).
- **The reference was measured, not described.** Shawn Ryan Show, `KUMikP6a2eI` (51 s, 1.03M views in 4 days). Six analysts logged every one of
  its 1,222 frames; a script measured cuts, face size and blur on every frame; Demucs split the audio into voice, drums, bass and other.
  → `projects/_ref-yt-shorts-shawn-ryan-farm/analysis/` (`STYLE-TEARDOWN.md`, `FRAME-LOG.md`, `board/`, `make_board.py`).
- **The sound answer to the pilot's "not enough sound effects".** The reference has almost NO sound effects (silent whips; one chime on its
  sticker). It feels full because a **continuous music bed** runs ≈ 13.6 LU under the voice from the first frame to the last. The Instagram
  pilot had no bed at all. → README § 8; flagged in the Instagram README § 6; open question 1 for Affan.
- **HyperFrames' built-in `whip-pan` is not this whip.** In 0.8.16 it crossfades two blurred, edge-clamped frames over the transition.
  The reference hard-cuts to an incoming frame ~40 % off rest, mirror-filled, and halves the offset each frame. → The whip is a numpy pass
  on the picture track (README § 4, PLAYBOOK § 5); `workflows/whip-slide.py` gets written on the first job.
- **Render at the base's frame rate.** `hyperframes render --fps` accepts `24000/1001`, so a 23.976 source needs no 24 → 30 mapping (the
  `rframe()` work that took a QA round on the pilot). → README § 2.
- **Built from one reference.** Every number here comes from a single Short. Measure the first two YouTube-look samples the same way and
  move whatever doesn't hold into this file.

## 2026-10-05: Affan's first decisions on this look

- **First job = the MFM Moonbug story, rebuilt in this look** (the cut and the numbers were already verified on the Instagram pilot, and MFM
  is YouTube-first by PLAYBOOK § 0). Both looks of the same story can then be compared → `projects/mfm-nursery-rhymes/yt/`.
- **Sound = copy the reference**: bed + silent whips + one sticker sound → README § 8 and § 11.1.
- **Short borrowed clips are OK** (trailers, other creators' footage, 2–3 s, only where nothing official shows the thing) → README § 10 and § 11.2.

## 2026-10-05: the first build (`projects/mfm-nursery-rhymes/yt/`), before QA

- **The two-pass build works and is fast.** Picture pass (`yt/build_picture.py`: numpy/OpenCV crops, push-ins, SPLITs, sticker) 23 s →
  whips (`workflows/whip-slide.py`) 20 s → overlay pass (HyperFrames, transparent ProRes 4444) 45 s → ffmpeg composite 10 s. A full rebuild
  takes about 2 minutes, so framing fixes are cheap. → PLAYBOOK § 5.
- **The source's own camera cut must be a shot boundary.** MFM cuts from Shaan to Sam at base frame 661; a shot that ended at 662 showed Sam
  for one frame in Shaan's crop. The whip tool's "the picture changes most at frame N" warning caught it. → Shot boundaries snap to the
  base's joints and camera cuts (as `SAM_CUT` did on the pilot).
- **Kids' channel B-roll carries burned-in lyrics at the bottom** (Cocomelon, Pinkfong). Crop them out with a zoom and a high anchor (the
  visible bottom edge stays above ~0.87 of the source), or pick a moment without them.
- **Corporate B-roll can carry burned-in subtitles too** (Blackstone's brand film). Keep the visible bottom edge above them, and keep the
  B-roll's own text above the caption band (y < ~1000), or the caption sits on top of it ("TO BLACKSTONE" over the sign's "Blackstone").
- **A sign wider than a 9:16 crop gets a slow pan** across it (smoothstep, ~1.8 s); with the caption naming it, it reads.
- **A 320×240 source can't go full-bleed** (a 135-px-wide crop blown up 8×). It gets FIT: the whole frame at the width over a blurred,
  darkened copy of itself. The one deliberate exception to "always full-bleed".
- **Watermarks in the corners of B-roll** (Little Baby Bum's download link) are cropped out by a small zoom toward the subject.
- **Stock sites often have the same shoot filmed vertically** (Pexels 7218797 is the vertical twin of 7218612): native 1080×1920, no upscale.
- **Sam's face fills 44 % of the frame height** in a full-height 9:16 crop (he sits close to his camera), so captions land on his chin. The
  source's framing sets this; it can't be zoomed out. Accepted.
- **Avoid footage that carries a tragedy.** YouTube's footage of Blackstone's headquarters (345 Park Avenue) is dominated by coverage of the
  July 2025 shooting there, so the company's own brand film was used instead.

## QA round 1 on the MFM YouTube-look sample (2026-10-05): 4 lenses, ~45 findings, all high/medium fixed in v4

- **Check WHO is on screen against press photos, never against a clip's title.** "A conversation with Rene Rechtman & David
  Helgason" showed two men; the crop framed the wrong one (René is the bald, bearded man, per Fortune and MFM's own Short).
  → Every person-B-roll gets an identity check before the build (PLAYBOOK § 4).
- **Readable text in B-roll must not contradict the line.** Wikipedia's "50 most-viewed channels" list (T-Series, Sony's
  Culver Max, Disney Star) sat under "top 100 children's brands… none owned by big studios". → Read every legible word in a
  B-roll frame against the spoken claim; replaced with YouTube's most-viewed nursery-rhyme results (all kids' brands).
- **Screencast scrolls stutter** (Chrome's screencast delivers frames unevenly). → `page-record.mjs --full` takes ONE
  full-page still and the kit pans over it (`pan_y`), perfectly smooth.
- **Face-follow crops shook ±10–25 px per frame**: a running median over face samples taken every 2nd frame flips between
  neighbours, and samples leaked in from the next shot. → `kit/yt_picture.py` fits a straight line to the detections INSIDE
  the shot (slope capped at 2 px/frame).
- **B-roll at 25/30 fps dropped frames at 24** (visible judder on pans). → The kit CONFORMS every clip (each source frame
  becomes one output frame: 0.96x / 0.8x speed); only time-lapses retime.
- **Cut exactly on the base's own joints and camera cuts**, including ones that fall inside a planned shot (split that shot
  with a whip). Two frames of the next take before a whip read as a glitch.
- **Mattes are read frame-exactly** (decode and skip), never with a seek: a one-frame lead put the sticker in front of Sam.
- **The sticker sound sits ≥ 15 LU under the voice** (at −6 dB it masked "What?"), and library SFX lose their leading
  silence before placement (UI Save.wav opened with 0.28 s of nothing).
- **Master = one static gain into an oversampled peak limiter**, not loudnorm: loudnorm's "linear" mode silently fell back to
  dynamic (pumping) whenever a peak needed limiting. The mix now fails loudly if that ever happens.
- **Timeline steps at (frame − 0.25) / fps**: rounding to the exact boundary made a third of the hook-title steps land a frame
  late (a visible stutter). The caption kit already did this.
- **Wide wordmarks**: a 9:16 crop can't hold "Blackstone" whole, and a pan never shows it complete. → FIT with a `crop` box: the
  sign plate fitted to the width above the captions, over a blurred, darkened copy of the shot.
- **The YouTube look is now a spec-driven kit**: `kit/yt_picture.py` + `projects/<job>/yt/spec.json` (MFM's spec reproduced
  the hand-written build pixel for pixel). New jobs write a spec; nothing is copied from another job.

## Rollo (`projects/rationalmale-hacked/`), QA round 2, 2026-10-06
- **The hook's timing was frame counts measured at 24 fps** (11 in / hold to 56 / 21 out): at 30 fps it ran 2.47 s, not 3.2 s.
  → `yt_overlay.py` scales the counts by fps / 24.
- **Watermark vs lip captions**: a talking head shot tight puts the lips low, and the captions (capped above the watermark) could not
  get under them. → spec `watermark_y` (Rollo 1295); ig_capy keeps the glyph centre <= watermark_y - 90 (bottom >= 20 px over it).
- **Cyan = a verbatim read-out only.** "PASSCODE WAS CREATED" was cyan while the card on screen said "A passkey on Android has been
  added": a paraphrase is white. Check every cyan chunk against the frame it plays over.
- **A self-correction is captioned as SPOKEN** ("fake pill", not the corrected "coin" said two repeats later in the source), and a
  short word the transcript missed ("or a") still gets captioned (the chunk text may hold words the word count does not consume).

## Affan's review 2 of batch 1 (2026-10-07)
- **MFM's sample is "perfect, don't even touch it"**: the benchmark for this look.
- **Rollo**: the style is right, but punch-in cuts on the same camera and whips between two shots of the same camera are noise in an
  already dynamic edit. -> whips only on a real scene/camera change; same-camera joints keep one keyframed push-in (README rules 4-5).
  This overrides the QA reviewers' ×1.18 zoom-step and whip-every-cut rules.
- **This look is now the default upgrade** for samples that read "too basic": Chris Do (the two people instead of B-roll overlays),
  Harbinger and Pomp (the full style: overlays, face split screens).
- Captions: constant position, `! ?` and quotes only, 60 fps overlay (README rules 1-3).

## 2026-10-08 · Harbinger + Pomp Sean Ryan rebuilds (kit lessons)
- **FACE SPLIT**: a SPLIT's bottom can be a second face from the SAME base frame (`"bottom": {"face": key, "face_x", "fy_out", "z0"}`),
  only inside a source two-up range where both faces are live (Harbinger: Sean top, Jordan below). `yt_faces.py` scans both faces per
  frame with `face_x` hints. Raise the bottom's z0 (2.0) when the source box carries a name plate under the guest.
- **A burned-in show label on every base frame** (Pomp's "The Pomp Podcast", top left) leaks into a speaker crop: `base_inpaint`
  [[x0, y0, x1, y1]] paints it out of the base before every A / SPLIT render (fill_box, the FIT shot's column blend).
- **A wide title card or wordmark (BlockFi, The Americans) cannot survive a 9:16 crop**: make that shot FIT (fitted over its own blur).
- **A webcam-tight guest (face ≈ 50 % of the frame at z0 1.0, the crop can't zoom OUT) puts the lips low**: the constant caption
  line is capped at `watermark_y − 90`, so the default watermark (1160) pulled captions onto Sean's and Zac's mouths (QA r1, MED).
  Fix the spec, not the picture: `captions.lip_gap` 0.04 (the 0.13 default is ~118 px on a huge face), `watermark_y` 1340, the hook at
  y [1400, 1478]; push-ins on such a face stay ≤ 0.012/s or the crown leaves the frame.
- **A camera change INSIDE a sentence** (the source cut to the other person for 0.18 s): an A shot's `"freeze": [[f0, f1]]` holds the
  last good frame instead of flashing the wrong face (Rich Roll).
- **Sound (QA r1):** `whoosh-light` crests ~0.7 s after its start: trim its head (`lead` 0.40) so the crest lands on the hook;
  split-entrance `whoosh-air` 4 dB lower (it masked a word for 0.1 s at 2 dB under the voice peak).
- **Caption colour = voice also covers QUOTED voices** per person: a `captions.palette` entry adds a colour (green for the third
  quoted voice). Attribute a line by CONTENT, not by the show's camera: Pomp's reaction shot sat under Zac's "How do you not have the
  money?" (the raw runs on into his next sentence); the B-roll covers that reaction so the picture never contradicts the colour.
- yt-dlp sections of a stock clip can report `r_frame_rate` as "60/1,": parse the first field only.
- **QA r2 (Harbinger):** a dark night B-roll does not open with `black` + `contrast` (contrast runs first and pulls the mids back
  down). New `grade.gamma` key, applied FIRST; pair it with a negative `black` (a black-point crush) or the shot goes milky:
  `{"gamma": 0.6, "black": -0.07, "sat": 1.2}` lifted the house facade from mean luma 0.09 to 0.17 with the window still glowing.
- **A last word clipped by a WhisperX end that runs early** ("here." ended 230.488 in words.json, the vowel actually decays to
  −28 dB at 230.58, and the next word's fricative starts 230.60): measure the 10 ms RMS + spectral centroid, move the segment end
  into the gap, and correct BOTH word edges in `words.json` (else the export keeps a phantom next word that starts before the cut).
- **Extending a cut after Topaz has run**: never redo the whole 4K base. Re-splice (the first N frames null at −91 dB and decode
  identical), run `topaz-iris.py` (Iris 2x, then FI) on the LAST take only, and stream-copy concat it onto the old base's frames
  [0, take start): ProRes is intra-only, so `-frames:v` + concat `-c copy` is exact. Splice with the job's original `AMPLIFY_DB`
  (Harbinger: 0) or the voice changes level under an approved mix.
- **QA r1 (Pomp): attribute every caption chunk by VOICE, not by the show's camera or by reading the raw transcript.** Two chunk pairs
  were coloured for the wrong person ("FTX blew up in November" is Zac; "How do you not have the money?" is Pomp). A speaker embedding
  per chunk (pyannote wespeaker, cosine vs known spans: same speaker 0.8–0.9, the other < 0.35) settles it in a minute — run it on
  every two-person sample before the colours are locked (Pomp `yt/work/qa-r1/emb3.py`).
- **A source's burned-in sponsor lower-third can sit under the label we already paint out**: check a SPLIT top panel at its FIRST
  frames (before the push scrolls it away). Fix with the top panel's start zoom (`SP(..., top_z0=1.12)`) when the crop can clear it.
- **Read a stock clip's first second before trusting a `src_in` of 0**: y08 "FTX arena" opened on 0.5 s of a coin shot.
- **A chyron that NAMES the thing being said (Voyager) must be readable**: a 9:16 crop shows ~32 % of a 16:9 width, so a lower-third
  that carries the noun goes FIT, like a wide wordmark.
- **A low-frequency thump at a joint** (the segment started inside the tail of a filler hum, 55–140 Hz): mute the voice over the burst
  with the ramps OUTSIDE the next word's onset (`yt_mix` ramps sit outside the range: end the range ≥ 10 ms before the onset).
- **QA r2 (Pomp): turning a masking whoosh DOWN makes it vanish** (−5 dB put the split whooshes ~15 dB under the voice, below the bed:
  "no SFX" on a phone, the review-2 complaint). Fix a whoosh that masks a word by MOVING its crest (≈ 0.30 s after the cue for
  `whoosh-air`) into a voice gap at the normal level (`under` 6–7), never by lowering it. Find the gaps on the voice stem first.
- **Fixing one end of a stock clip can move the defect to the other end**: a later `src_in` slid Pomp's SBF clip onto its closing
  dissolve. Check a B shot's FIRST and LAST frames after every `src_in` change (and every clip's source for dissolves).
- **A centred 9:16 crop of a walking subject**: SBF walked at x 0.6–0.8 and the centred crop cut him at the edge. Use `pan` [x0, x1]
  to follow him; `z0` > 1 with `cy` 0.0 (top-aligned) also drops a news lower-third out of the bottom.
- **Cutting a ProRes base by stream copy: seek on the OUTPUT side** (`ffmpeg -i in.mov -ss T -frames:v N -c copy`, with T = frame start − 5 ms). An input-side `-ss` keeps the packet before the seek point, flagged discard: each part decodes fine alone, but the concat demuxer keeps that packet, and the joined base gained a frame (Rich Roll: 1387 instead of 1386). Always check `nb_read_packets` == `nb_read_frames` and run a PSNR identity check against the source frames before building on a patched base.
- **The start of a segment can sit inside the previous word** (Harbinger: 26.70 was inside "Because"; "-cause" played uncaptioned before "I think"). WhisperX ended "Because" at 26.69, but the [k]-vowel-[z] ran to 26.865. Measure the real gap (10 ms RMS) and move the start onto the frame inside it. Muting the fragment would only patch over the bad cut.
- **Affan's review (2026-10-08): the whooshes are too loud.** Chris Do's hook `whoosh-light` (+6.8 dB gain) and split `whoosh-air` (+7.0, under 2) were cut by exactly 10 dB (`WHOOSH_TRIM`; mix-only rebuild, picture bit-identical, audio null -49 dB outside the whooshes). Start every new sample's whooshes 10 dB under that level. Pops, ticks and hits are not whooshes: they keep their audible level.
- **A comment pasted mid-line silently deleted three SFX cues** (Pomp yt9, 2026-10-08): `sfx = [hook]   # note + [splits...]` made the split whooshes part of the comment, and the shipped final had only the hook. The yt8→yt9 check gain-matched the audio OUTSIDE the cue windows and never looked inside them. Rules: (1) every spec builder asserts its cue count (`assert len(sfx) == 1 + n_splits`); (2) after any mix change, isolate each intended cue (premix − voice) and confirm it is present at its new level, not just that the rest of the audio nulls.

## 2026-10-12 · batch 2 direction (Affan, before the build)
- **Lesson:** "when I do split screens I always have a white line in the middle… it feels organized", and the captions sit ON that
  line, with the base caption position set for the whole video so a split arriving 5-10 s later finds them already there (batch 1 had
  no line: "the one thing I don't like"). **Change:** `kit/yt_picture.py` draws a white seam line on every SPLIT (`split.line`, default
  6 px white; a line holds the seam still unless `bob_amp` is set); `captions.on_seam: true` pins every chunk's glyph centre to
  `split.seam` (+ `seam_dy`) for the WHOLE video (`kit/yt_overlay.py`) and skips the per-shot lip placement (`kit/yt_build.py`).
  **File:** the kit; the rule is memory `feedback-split-screen-white-line`.
- **Lesson:** never lock the look; each sample must beat the last one (Affan's general rule). **Change:** research Sean Ryan's
  channel again before each batch and write the improvement into the job BRIEF. **File:** onyx-samples PLAYBOOK § Batch mode.

## 2026-10-12 · batch 2 build findings (reported by the build agents; worked around in the jobs, kit NOT yet changed)
- **A section download can start its VIDEO seconds after its AUDIO while ffprobe reports start_time 0 for both** (Jay Clouse:
  5.743 s), so splice.sh's offset check misses it. **Change:** measure the A/V offset at intake by a mouth-movement or clap check,
  not only the stream start times; that job trimmed with `-ss 5.743`. **File:** the onyx-samples PLAYBOOK § 1.3 (intake).
- **`yt_picture.py` conforms 24/25/30 fps stock wrongly on a 60 fps base** (25 fps B-roll played at 0.42x; Jeremy set `speed` 1.0001
  to dodge it) and **ignores `fx_out` on a SPLIT's top panel** (Jay). **`whip-slide.py` steps once per frame**, so at 60 fps a whip
  lasts 0.13 s (Jeremy re-timed it in `yt/build.py`). **Topaz fails on a 3-frame take** (drop that `--segments` boundary).
  **`captext.clean()` strips "·"** from hook lines. **File:** the kit, to fix deliberately (each job's BRIEF § Kit lessons has the detail).
- **A tight remote-call webcam face cannot be full-frame with captions on the seam** (the caption line lands on the mouth): every
  David Altizer shot became the top of a split. Plan for it at the storyboard.
- **Topaz on a sourced THUMBNAIL waxes faces and invents texture**: Lanczos + light sharpening instead.

## 2026-10-14 · batch 3 kit upgrade (before the 6 YouTube builds; spec `projects/_onyx-batch3-2026-10/STYLE-RESEARCH.md` § A1, B1, D, G)
- **Lesson:** stock did the storytelling in batch 2 (47 of 55 inserts in three samples; 9 stock actors as real people) and the one
  sample built from real artefacts (MrBeast) is the one that looks like Shawn Ryan, whose 2026 Shorts run on RECEIPTS (articles with a
  highlighted line, dated charts, the show's own episode card) and MARKS (a red circle on the map, blue boxes on a menu).
  **Change:** shot kinds `DOC` and `CHART`, and `marks`, `chart`, `fx` on any shot, drawn into the picture → `kit/yt_picture.py`
  (keys), `kit/yt_devices.py` (drawing); README § 13; PLAYBOOK § 3 gate (≥ 50 % real inserts, 0 stock actors, ≤ 2 marks) and § 4b.
- **Lesson:** "fast set-up, slow payoff" was written down and never measured (batch 2: 1.99-2.66 s after the turn; Victor ended on a
  0.60 s face). **Change:** `kit/yt_build.py` prints the payoff report and warns under 3.0 s (`allow_fast_payoff` to override).
- **Lesson:** 3 of 4 batch-2 hooks had only a whoosh (-18.8 to -22.8 dB, inaudible on a phone), and hand-written cue lists drop cues
  (the Pomp comment bug). **Change:** `kit/yt_cues.py` plans every device's cue from the same keys that draw it, adds a missing hook
  hit, and `yt_build.py` asserts the pair → `kit/yt_mix.py` places them by PEAK (`under`) with sliced tails (`dur` / `fade`).
- **Lesson:** `3:48 PM`, `$2.3 MILLION`, `250,000` reached captions.json (QA X4). **Change:** `kit/yt_captions.py` `numerals()`; the
  19-character limit is checked after it (a spelled-out number may need its chunk split).
- **Kit facts found while building it:** a body-text line in a 4K desktop capture is ~1600 px wide, so a full-width card shows it at
  ~20 px: crop the front card to the sentence (a clipping) over the whole page; a cover-fitted plate of a cropped clipping reads as giant
  blurred letters (the plate now comes from the back-most source, uncropped); a push centred on a highlight near a card's edge pushes
  that edge out of frame (the focus now glides 70 % to the centre); numpy `(h, w, 1)` broadcasting was 5x slower than same-shape
  arrays in the per-frame composites. Regression: the batch-2 MrBeast spec rebuilds its picture bit-identical (1103 / 1103 frames).
- **Not built (cheap list, § D):** D5 (renders / type cards for abstract nouns), D7 (the host's question first) and D8 (32-45 s) are
  sourcing / cut rules (README § 10, PLAYBOOK § 2), not code; D10 grade stays a per-spec recommendation (a kit default would change
  batch-2 rebuilds). Known kit bugs still open from batch 2 (out of this scope): `fx_out` ignored on a SPLIT's top (fixing it changes
  the shipped MrBeast picture, its s12: make it an opt-in key), and 24/25/30 fps stock conformed wrongly on a 60 fps base.

- 2026-10-15 (Scott Clary FUBU, client job): `SPLIT` gained `"flip": true` (yt_picture.py; backup .bak-2026-10-15): B-roll ABOVE the seam, the speaker BELOW (Affan: "Daymond at the bottom, New York, London and Paris on top"). "top" still names the speaker so yt_faces scans it. Also: Montserrat in the hook has no "·" glyph (renders blank): use "/" in hook lines.
- 2026-10-15 review: "everyone knows him" beats "the brand's classic face": for a popularity beat Affan wants the most globally famous wearer (50 Cent over LL Cool J, whom he did not recognise). Pick the face a casual viewer names instantly.
- 2026-10-17 (Scott Clary Bombas): `prop` (yt_picture.draw_prop): an RGBA product cutout on a shot that whips in from the right, floats mid-frame with a soft shadow and whips out left. Affan: "a sock appearing through a whip transition, it just hangs in the middle and then goes away".
- 2026-10-19 (Scott Clary, from AW): `head_lock` (yt_picture: face fit restarts at each joint of a jump-cut run) and `fps_out` (yt_build: Topaz Chronos doubles the finished picture per shot, overlays render at the new rate). Affan: the AW grade is NOT for face videos; head lock is.
- 2026-10-19 (batch-3 Wellness, his own bed Gibran Alcocer "Idea 23", soft solo piano): Affan "music needs to be up by 6 dB" over the 14.5 LU-under default → 8.5 LU under (both looks). A sparse, quiet piano bed at 14 LU under reads as no music; start such beds around 9 LU under, keep 13-14 for dense/beat beds.
- 2026-10-19 (Serhant calendar, Affan: "his face shouldn't be moving up and down with the cuts"): head lock rebuilt. (1) z0 1.0 leaves NO vertical room (a 9:16 crop of 16:9 uses the full height): A shots under head lock run at z0 1.2. (2) Anchor on the EYES, not the face box (YuNet boxes the lower face when he looks down). (3) CHAIN the takes: each take's first frames land where the previous take's last frames were (eyes + eye spacing), one run-wide offset; matching take medians was not enough. (4) Joints from the EDL can be 1-2 frames off the real cut: `workflows/cut-frames.py` snaps them (53 -> 55). Re-detecting faces on the render to 'measure' the lock is too noisy; judge with eye-line close-ups and a guide line (`headlock-proof.png`).
- 2026-10-20 (Serhant calendar, Affan: "WHERE IS THE DAMN HEADTRACKING" + "LOOK AT THE SHAWN RYAN SHOW AGAIN"): (1) **head_track** = the AW head lock: the crop follows the EYES on every frame (Gaussian over +-8 frames inside a take, faces scanned `--step 1`), the spec's fy_out is then the eye line (0.32); chaining only at the cuts was not what he meant. (2) **A shot `r` is a RATE PER SECOND**: the reference pushes LINEARLY at ~8-14 %/s (x1.39 / 3.5 s, x1.5 / 4.6 s, opener ~24 %/s); the old `push()` gave 2-6 % a whole shot. Now `r = min(0.10, 0.55 / dur)` (x1.55 a take, base z0 1.12), the split's speaker panel ~+25 % over the split.
- 2026-10-20 (Affan's Tella 'Video Editing and Head Tracking Feedback', on the calendar Short v8): "too poppy" = tracking + cut zooms + constant in-and-out. RULES now: (1) head tracking CALM (`head_track_sigma` 12 frames + a 9-detection median: no bounce, no 'goes to the bottom for no reason'), NO size-following (`head_track_scale` off: it pumped in and out); (2) NO cut zooms: one continuous zoom curve per speaker run; (3) zoom ONLY on emphasis: `zoomkeys` [[frame, scale], ...] eased (smoothstep), in toward the emphasised line, back out 'midway'; a quick zoom-in right after a whip is liked; the zoom-out on the last line is liked; (4) splits are NOT head-tracked (`track=False`). Replaces the per-second linear push for Affan's client Shorts.
- 2026-10-23 (MATG, Affan on the 54 s cut: "there are some pauses which I don't like… the YouTube style is basically all quick cuts, jump cuts… not so hard that part of the speech gets cut, but the cuts have to be quicker"): the YT look has NO audible pauses. Every silence over ~0.15 s between kept words (inside a line or at a joint) goes down to 2-3 frames @ 24 fps, measured on the 10 ms RMS envelope (never on WhisperX stamps: they squeeze numbers) and frame-snapped with the normal J-cut joints; never clip a word edge. Apply at the cut, before any graphics are timed.
- 2026-10-23 (MATG pacing pass, how it was done; `projects/matg-targeting-is-dead/work/tight/`): (1) pauses = the raw's 10 ms envelope per segment (`pauses.py`), then the 5 ms envelope at both edges (`edges.py`) and a voicing/centroid check (`what.py`: the plateaus inside most pauses were BREATHS, unvoiced and ~2.5 kHz); cut points on the 24 fps grid with >= 15 ms after the decay (the J-cut crossfade adds 15 ms) and >= 30 ms before the onset, leftover quiet closest to 0.100 s; 11 pauses, 2.375 s. The transcript-gap candidates were half wrong (3 were continuous speech, 2 real pauses were not on the list). (2) The cut is a strict subset of the old one, so EVERYTHING downstream is remapped, not rebuilt: `work/tight/map.json` (kept old-frame ranges); the Topaz 4K stream-copied through it (output-side seek per range + concat: 1242 ProRes packets md5-identical to the old file at the mapped indices, no re-run); faces.json remapped; the spec's literal frames wrapped in MF()/MT() and proved by `check_remap.py` (every shot edge, cue, chart, stack, highlight, mark, pin = old value through the map). (3) A cut pause can starve a 1-word caption chunk (`"HEY` 12 f -> 4 f): diff the chunk durations old vs new after any pacing pass. (4) `yt_build` hands Topaz Chronos (fps_out) only the shot starts as `--segments`: a jump cut INSIDE an A / SPLIT shot must be added by hand (run topaz-iris yourself, then `--skip picture`), or Chronos morphs across the cut. (5) The A-shot crop is CLAMPED to the source frame's bottom: on a webcam face that sits low (Kipp's mouth at 61 % of his frame) `fy_out` does nothing past the clamp and only `z0` lifts the mouth above the seam captions (z0 1.38); compute it, don't nudge fy_out. (6) An inline comment after a chunk in the chunk list swallowed the rest of that line (2 chunks, the Pomp bug again): the spec's word-count assert caught it; never put a comment mid-list.
- 2026-10-24 (Brad Lea / Dropping Bombs, `projects/bradlea-ferrari-camry/`, YT builder): (1) **A podcast CLOSE-UP camera cannot be a full-frame A shot with on_seam captions**: Brad's close-up has mouth-eye 213 px (face 50 % of 1080) vs 125 px on the medium/wide cams; at z0 1.2 the crop is clamped and his mouth lands on the 1092 seam captions (z0 >= 1.45 would be needed = an extreme close-up). Those runs became SPLITs with the close-up in the top panel (z0 1.05). Measure mouth-eye per camera from `yt/work/faces.json` BEFORE choosing A vs SPLIT. (2) **Dropping a "filler" before a number can drop the number**: "they paid me [1.3 s] thir- [0.22 s] -teen thousand dollars": the 0.25 s low-centroid burst was "thir-", and the cut without it read "$10,000" to large-v3, medium.en AND small.en. Re-ASR the cut with two models on every number. (3) `export-transcript.py` emits a word once, clamped to the FIRST segment it overlaps: a word split by a pause cut comes out 0.3 s long; patch its end after every splice (`work/patch_transcript.py` there) and tell the other builder. (4) YouTube bot-checked again (08:58 UTC): real B-roll still came from Wikimedia Commons through the en.wikipedia API (commons.wikimedia.org did not resolve here), Pexels (ids by a same-origin fetch on pexels.com/robots.txt in the built-in browser, no media played; videos.pexels.com downloads with curl) and official press galleries (toyota.com/camry: 3600x2400 PNGs on its Adobe CDN, listed in the page HTML). ferrari.com answered a bot check: not bypassed. (5) The tonal-prominence check (> 20 dB above 1 kHz = reject) throws out most "UI-ish" sounds: phone vibrate 27.6, receipt printer 24.2, digital shutter 35.3, two risers 29-33; analogue film shutter 13.0, newspaper slap 11.7, money-wad bang 10.3, pen on paper 16.4 pass. (6) `yt_overlay` "stamps" have no exit (they hold to the last frame): not usable for a mid-video beat without adding a t1.
- 2026-10-24 (Brad Lea YT, sonnet reviewer r1 on v2, kit facts): (1) a DOC whose highlight sits on the card's LEFT side pushes around that point and grows the card to the RIGHT; with `drift` 0.4 the 900 px Carscoops card ran off x 1080 for 0.9 s (headline clipped): w 820 + drift 0.15 kept it at x <= ~1010. (2) SPLIT tops are untracked by default, so a same-camera jump cut INSIDE a split pops the head (84 px at Brad's 852): `"track": true` on the top fixes it (head_track + head_lock chain). (3) A SPLIT bottom made from a 9:16 MG frame puts its lower rows in the bottom 300 px platform band: compose a 1080x828 panel with the card scaled to ~500 px at panel y 60. (4) Low booms measured "louder than the voice" in momentary LUFS while peaking 8-9 dB under it (LF energy): booms at under 10-13 with <= 1.6 s tails; and a split entrance with only a whoosh (~20 dB under the voice, under the bed) reads as "no SFX": give it a landing hit.
- 2026-10-24 (The Fantasy Footballers, `projects/ff-0-4-bye-week/`, YT builder): (1) **A story with no public document gets purpose-built motion graphics, not receipts**: nine HyperFrames comps (`yt/mg/build_mg.py`: one generic fantasy-app UI system, every beat anchored to a word through `yt/plan.py`, rendered at 59.94) placed as B shots (z0 1, r 0, no grade = the MG frame itself) and as SPLIT bottoms rendered at exactly 1080 x (1920 - seam). One recurring object (YOUR TEAM) carries the whole Short. (2) **Chronos morphs MG type** (rolls, flaps, slams): `yt/work/mg60.py` puts the NATIVE 59.94 MG frames back over the doubled picture's settled MG frames ([2 f0 + 18, 2 f1 - 4), full frame on B, rows >= seam + 3 on split bottoms); the whip frames stay Chronos'. (3) **Split-bottom MGs live between the watermark and the platform UI**: with the seam at 1060 and the watermark at ~1126-1174, panel content starts at panel y >= 130 and ends <= 1620 full-frame (r1 found the watermark over the first table row), and stays inside x 60-960 (right-hand buttons). (4) HyperFrames odometer digits: a flex column inside an `inline-flex` wrapper is STRETCHED to the wrapper height unless `align-items: flex-start` (yPercent then moves 1/10 of a digit); and element ids are global: an odometer column id `c1` collided with a chip `#c1`, so `pop("#c1")` hid the digit. (5) A 0-4 team PLAYS WEEK 5: header copy in an example graphic must agree with the record it shows (r1). (6) A stream-copied section starting on a keyframe can still carry video start_time 0.049 vs audio 0: re-cut it with the video copied and the audio decoded to PCM from the same `-ss` (both start at 0). (7) Booms 8-10 dB under the voice peak still out-weigh quiet words full-band (sub energy) while sitting 17-19 dB under them in 250-4k: measure both; booms at 12-13 under with <= 1.2 s tails.
- 2026-10-24 (FF, pre-hand-back review): **never put invented numbers on a host's REAL story.** mg08 / mg09 first showed made-up scores ("151.8 vs 162.4", "lost by 2.2") on Andy's own charity league and called it YOUR TEAM (the viewer's 0-4 example object), which also broke the object's continuity (0-4 -> 0-2 -> 0-4). Rule: a host's own story shows only what he said (ranks, "tough luck", his record) under HIS name (ANDY'S TEAM); illustrative numbers live only on the viewer's hypothetical object and carry an EXAMPLE tag.
- 2026-10-25 (Scott Clary x Chris Do, `projects/_client-scott-clary/chris-do-sneaker-pricing/`, approved FIRST PASS, "looks good"): what held: Affan's own line order, a PROMISE line as the hook card (WHY CHARGING MORE / GETS BETTER CLIENTS) with the credential moved to a `tags` pointer (EMMY WINNER / CHRIS DO, `"plate": true` over a bookshelf); a webcam guest opened on a FIT panel of his cam (room for the pointer), every other cam shot A at z0 1.25 (computed: 1.12 put the lips on the seam); purpose-built cards for every beat (`mg-cards.py sneaker|replies|dayrate`), each landing on the spoken word; face cam <= 2.7 s; pauses -45 dBFS-thresholded on a gated mic. Shot edges within 4 frames of a cut must SNAP onto it (a 1-frame sliver killed the 60 fps Topaz pass).
- 2026-10-25 (Chris Do, correction): a webcam upload tagged 60p can repeat frames irregularly (~40 % of steps frozen); one second of YDIF read by eye looked "true 60" and was wrong. Measure the SHARE of near-zero steps (YDIF < 0.3 on a centre crop over ~6 s of speech): above ~10 % = a low-rate webcam, so de-duplicate before Chronos or the 60 fps final keeps the judder (the YT v1 shipped with it; the IG session caught it).
- 2026-10-26 (Scott Clary x John Morgan, `projects/_client-scott-clary/morgan-claw-machine/`, YT v1): (1) **Scott's RSS feed carries the episode VIDEO** (`podcast:alternateEnclosure` HLS, up to 2160p AVC 30p) for many episodes: `ffmpeg -ss <s> -i <2160p variant playlist> -t <len> -c copy` pulls just the story in 4K, no YouTube, and its clock IS the podcast clock; a 9:16 crop of 4K is native 1080x1920 (no Topaz Iris). (2) **YuNet's "largest face" can be a prop**: a gold statue on the shelf scored a 918 px "face" bigger than the guest's, every A shot centred on the shelf and cut him off. Check faces.json eye y against a frame (eyes at y ~20 = not a person) and set `face_x` per A shot. (3) A cold open that COPIES the payoff's audio leaves the payoff with no caption words (export-transcript emits each source word once): `work/patch_transcript.py` there duplicates them; run it after every splice. (4) A guest with no headroom (head touching the frame top): the A crop clamps at the top, so zoom (z0 1.3) is what brings the lips down to the seam; the cold open as a LOW FIT panel left room above the head for the pointer.
- 2026-10-26 (Morgan claw, Affan's v1 review): "add a tad bit of unsharp mask and sharpen to the footage other than that it looks good". Done without a re-render: ffmpeg on `yt/work/picture.whip60.mov` (camera + B-roll), `unsharp=luma_msize_x=7:luma_msize_y=7:luma_amount=0.45:chroma_amount=0` then `unsharp=luma_msize_x=3:luma_msize_y=3:luma_amount=0.35:chroma_amount=0`, each with `enable='not(between(n,<MG card ranges>))'` so drawn cards stay clean, ProRes HQ, then `yt_build final --skip picture,overlay`. First time he asked: a lesson, not yet a preset rule; if he asks again, make it the kit's default finishing pass.
- 2026-10-26 (Morgan claw, Affan's v2 review: "removing [the casino bit] ... tighten it ... YouTube Shorts are very very tight, even
  the slightest pauses are removed ... the sound effects ... don't sound premium ... in some places the sound effect doesn't even fit
  the motion graphic"). (1) **An approved beat can still be the one to cut**: the casino set-up (bells, cheering) was in his approved
  sequence and read as a detour once built; 51.0 s -> 38.2 s. (2) **Tight = no stumbles, not just no silence**: an energy cut
  (-42 dBFS runs >= 0.08 s to 0.07 s) still left "a- the- the claw", "is the- it's", "they- they- there's", which WhisperX had
  silently dropped; a verbatim faster-whisper pass found them (CLIENT-SHORT-RECIPE § 2). (3) **Premium SFX = each sound sized to
  its motion**, never the kit's stock cues on a card (v2 had data blips on an LCD menu, glass ticks on "$100" and MADE IN CHINA, glass
  pops on a product card, a whoosh on every cut back to his face). v3: `yt/sound.py` + the CUES block, fresh Epidemic files on the hits,
  cue_check PASS, every slice <= 20 dB tonal (the gate caught a fresh reverse cymbal at 39 dB, the "cricket" again); the menu's WEAK row had to move (its slot fell inside the LCD blink at the end of the shorter card).
- 2026-10-26 (Morgan claw v3, Affan: "28 sec there's a frame position mismatch happening on John's camera after the whip transition
  finishes"). Measured on the delivered frames: his eyes snapped +202 px sideways at 29.37 s, the audio joint 8 frames after the whip
  into s14. The source was smooth there (he was turning ~30 px a frame and the joint continued that motion). Cause: `head_track`
  averages each head-lock take on its own (yt_picture.py `track_eye`, Gaussian sigma 12 frames inside the take), so a lock at a joint
  he moves smoothly through splits one motion into two one-sided averages that disagree, and the crop snaps. Tight energy cuts put
  joints mid-motion, so this will recur. Fix (spec): `head_lock` keeps only joints where the head really jumps; a joint the eyes move
  >= 10 px a frame through, with the step across it matching the mean step on each side (within 12 px), is left unlocked
  (`morgan-claw-machine/yt/build_spec.py` `smooth_through`). Gate for every Short with jump cuts inside a face shot: step the eye
  midpoint across each in-shot joint on the DELIVERED frames (YuNet, 60 fps); any step far above the neighbouring steps is a snap.
- 2026-10-26 (Morgan claw, after v3): "remove the sfx except for the transition ones, once I put music it's like too much". Under HIS
  music bed the card hits, swells and sub-booms crowd the mix; v4 keeps only the whip-cut whooshes (cuts back to the face stay silent).
  One Short so far: a lesson, not yet a rule. If it repeats, make transition-only the default for Shorts he scores himself, and
  ship the full design as a stem he can pull from.
- 2026-10-28 (Scott Clary x John Paul DeJoria, `projects/_client-scott-clary/patron-20000-cases/`, Affan's own text sequence, check v1 ->
  v2): (1) **WhisperX cannot align digits** ("1989", "20,000", "2018", "3,500,000" are interpolated): word times drifted up to 1.5 s around
  the numbers, so two cut edges clipped "cases a year" / "we were doing" and the captions ran a second early. Cross-check the number
  stretches against faster-whisper word times + the RMS (the job's `work/fix_words.py` fixes them in words.json; it also splits
  "3,500,000" into its five spoken words, because the caption rule turns "3.5M" into 30 characters). (2) **The name tag ran off the
  frame** ("that tag is not completely visible ... it's like cut out"): the default tag (x 330, dx -60) hangs its label LEFT of the dot
  and a 450 px label fell off the edge. Set `yt/tag.json` from the head position and the label's measured width, and check its bounds
  on the proof sheet; the prop must not land on it. (3) **Transition SFX under his music = subtle**: "crisp premium expensive but
  subtle ... I'm gonna put a music bed": short airy swishes (loud part 0.15-0.35 s, not 0.5-1 s builds), 19-23 dB under his voice
  (Morgan v4 sat 12-19), HP 150 Hz; a bright flyby swish measured -28 dB in the phone band (its body above 6 kHz = hiss on a phone): out.
  (4) **The sharpen pass, asked a second time** ("a slight tinge of sharpen and unsharp mask throughout"): now the standard finishing
  step, `workflows/sharpen-picture.py <job>` (cards excluded, from an untouched raw, never stacks), CLIENT-SHORT-RECIPE § 5.
- 2026-10-28 (Patrón 60 fps final, tool bug): the Topaz Chronos pass failed twice on the same take ("IndexError" in topaz-iris.py probe =
  an EMPTY output file): frames 260-318, a nearly static stretch of the $37.95 price card. yt_build split the 60 fps pass at every
  `head_lock` joint, and build_spec had locked every audio joint, including the ones inside cards and B-roll, so a static card slice
  became its own take and Chronos (rdt duplicate removal) returned nothing. Fixed twice over: yt_build.py splits only at shot starts +
  joints inside A shots (backup kit/yt_build.py.bak-2026-10-28), and the Patrón build_spec locks only joints inside A shots (`IN_A`).
- 2026-10-28 (same night, two sessions on one GPU): the IG session's Topaz jobs queue on the shared lock
  (`projects/_onyx-batch2-2026-10/lock.sh gpu`), but `yt_build.py`'s Topaz step (workflows/topaz-iris.py) does not take it, so an IG
  plate started alongside the YT 60 fps pass. When two sessions render, wrap the YT final in the lock (or message the other session
  to hold) before the Topaz step.
- 2026-10-28 (Patrón 60 fps QA, the eye-step gate caught it before delivery): at the jump cut at 61.27 s his eyes stepped +58 px and
  stayed (Morgan's snap, smaller). The source had a REAL 32 px jump there plus a steady leftward drift on both sides; `head_track`'s
  Gaussian average is one-sided at a take's edge, so both takes lagged the drift in opposite directions and the lock over-corrected.
  Kit fix (yt_picture.py `track_eye`, backup .bak-2026-10-28): within 2 sigma of a take edge it blends in a Gaussian-weighted LINEAR
  fit (no edge bias for steady motion); mid-take stays the calm average. The joint-unlock rule (`smooth_through`) still applies.
  Gate, every Short with jump cuts in a face shot: eye x-steps across each joint on the DELIVERED frames; a step that stays > ~25 px
  is a snap (a one-frame blip that reverts is the detector).
- 2026-10-28 (AffanWiz CA-009 Short "re-upload won't go viral", `projects/iphone-duo-clip-angle/clips/reupload-wont-go-viral/`, his
  own text sequence; the first Short cut from HIS long-form; check v1).
  - **(1) Head tracking lags a fast head at jump cuts.** `head_track` (sigma 12) placed the eyes 100-140 px off the pin at three
    in-shot joints where he moved quickly in short takes, then drifted back: a visible snap on the delivered frames
    (`work/head_snap_gate.py`). The offline replay `work/track_sim.py` showed sigma 3 still 132 px, so smoothing is not the cause.
    - Fix: `head_track: false` (the chained lock, each take starting where the last ended) plus the new opt-in spec key
      `head_chain_n: 2`. yt_picture.py matched each cut on a 4-frame median; 2 frames gives max 70 px at a joint where he moves
      31 px/frame, else <= 24 px.
    - Default 4 is unchanged, so other jobs render bit-identical (backup kit/yt_picture.py.bak-2026-10-28).
    - Rule: on a Short whose speaker moves a lot, run the head-snap gate before sending any check.
  - **(2) A tight 1080p webcam framing** (face box 38 % of the height) leaves the lips ~350 px above the 1092 seam at z0 1.0. z0 1.15
    puts them just above it; the hair top stays ~130 px down, so keep pushes <= 1.13.
  - **(3) The default name tag ran off the right edge again** (a 21-character credit line). Place `yt/tag.json` from the measured head
    with the label opening INTO the frame, and check its bounds on a full-size frame before the proof sheet.
  - **(4) The kit's starred profanity** ("S**T", `audio.mute`) renders through the caption cleaner, and quotes may span chunks
    ('IS LIKE "HUH?' ... 'IT'S NICE"'): both verified on full-size frames.
  - **(5) This room's noise floor is -42..-46 dBFS**, so the -42 dBFS run rule caught only fragments of each pause. The job's
    make_edl cuts each inter-word gap from its first to last quiet frame, with a threshold relative to the gap's own floor.
- 2026-10-31 (Scott Clary Pincus, client job): **`yt_build.py` never splits Chronos inside a SPLIT shot.** Its 60 fps segments are the shot
  starts plus head-lock joints inside A shots only, so the face jump cuts in a SPLIT's top (Pincus: frames 27, 48, 122) and the bottom
  panel's hard cuts (48, 73) would be blended into one morph frame each. **Workaround used:** run `workflows/topaz-iris.py` by hand
  on the UNSHARPENED `picture.whip.raw.mp4` (when the check was sharpened) with those frames added to `--segments`, sharpen, then
  `yt_build.py <job> final --skip picture,overlay`. **FIXED the same day** (Affan: "Yes, fix the kit"): `yt_build.split_edges()`
  adds, inside SPLIT shots only, the base cut's joints from `transcript/cuts.json` (where the source jumps, and only if its frames add
  up to the spec's) and the B-roll panel's own hard cuts (panel frame difference > 15 and > 8x its neighbours' median), dropping any
  edge < 4 frames from another. Regression on every 60 fps spec: the non-split jobs (Daymond, Chris Do, Morgan, Patron, War Dogs)
  and Bombas get identical edges; Pincus gets exactly the hand-run 27/48/73/122; Marvel's detected panel cuts 781/956 equal its
  `s06-bottom.mp4.json` part edges. Backup `kit/yt_build.py.bak-2026-10-31`. Detail: `projects/_client-scott-clary/pincus-ignored-facebook/BRIEF.md` ▶ STATUS.

- 2026-10-31 (Onyx batch 6, Still Here Hollywood x Kevin Pollak, `projects/stillhere-pollak-acting-class/`, builder lessons):
  (1) **A zoom key found by word text takes the FIRST match**: `wf("what")` on the last shot ("what it took") returned "what you got"
  18 s earlier, so the keys ran out of order (the IG copy stepped the picture 27 px in one frame; QA r1). Anchor every repeated word
  with `after=` and assert the keys increase. (2) **`head_lock` must cover SPLIT tops too** when the top is tracked (`"track": true`):
  build_spec's `IN_A` took A shots only and the split's jump cut at 294 snapped the head 90 px. (3) **WhisperX ran 0.2-0.25 s LATE**
  on a few words of this 1080p podcast ("yes", "I hate school"): the kit's YT captions survived (onset snap), but anything keyed to the
  raw stamps (IG lines, stage type) landed after the voice: re-time from the cut's 10 ms envelope in the job's transcript patch.
  (4) **Mixkit's 1080/1440/2160 files now answer 403 for many clips** (720 still 200): check HEAD before planning a full-bleed shot;
  a 720p clip fits a SPLIT bottom (1080x828) at 1.15x. (5) Bing via curl is still region-skewed (Kevin Hart for "Kevin Pollak");
  the built-in browser's Bing Images page + `a.iusc` m JSON works (Pincus `work/receipts/fetch.py` downloads the picks).
  (6) A section re-encoded from an input-side seek between frames starts its VIDEO one frame late (start_time 0.033 vs audio 0);
  seek on a frame boundary (k * 1001 / 30000) and both streams start at 0.
