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
