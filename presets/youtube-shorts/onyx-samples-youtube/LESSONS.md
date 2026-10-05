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
