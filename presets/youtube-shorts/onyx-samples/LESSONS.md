# Onyx sample Shorts: LESSONS

Each entry: **lesson → change made → file.** A lesson that repeats becomes a README number or a PLAYBOOK rule.

## 2026-10-04: the brief (before the first build)

- **A new look, not Abundance Wisdom.** Affan: *"another style, not abundance wisdom, something more minimalistic yet
  visualistic with motion graphics."* → README written from scratch, with no Abundance Wisdom mechanics → README § 1.
- **Mix the shot types inside one clip.** Three directions were mocked up (clean card · full-bleed + pop-ins · split
  explainer). Affan chose a mix: *"for a few seconds just the person talking, then the next shot can be a visual
  motion graphic while they get zoomed out into a rectangle, with text above and below."* → the four-mode shot
  grammar (FULL / CARD / GRAPHIC / SPLIT) → README § 3.
- **Finish = fully automatic MP4**, no Premiere step, so samples keep pace with the yeses → README § 2, PLAYBOOK § 5.
  (This is the explicit yes to the chat-only route that CLAUDE.md requires on a machine that has an app lane.)
- **Claude also edits Affan's reaction video** → PLAYBOOK § 7.
- **Pilot = My First Million** (Shaan Puri said yes on 2026-10-03), the Moonbug / Cocomelon story →
  `projects/mfm-nursery-rhymes/`.

## Sourcing finding (pilot)

- MFM posted the same Moonbug story as a Short twice: **May 2025 → 923K views** (48 s, `Q2fX7137Re4`) and
  **Sep 2026 → 51K views** (42 s, `PcTU0yaDfd4`, the one the permission email named). Source episode:
  `PKQo1Q2QkME` (Mar 2025), chapter "3B of nursery rhymes rollup", 0:00–21:55. → Always check a show's past
  Shorts on the same story; the gap is the reaction video's strongest line → PLAYBOOK § 1.2.
- YouTube rate-limits auto-caption downloads (HTTP 429). Download the Short and transcribe it locally instead.
  It's 42 s, and the file is needed for the reaction video anyway → PLAYBOOK § 1.1.

## Pilot cut (2026-10-04, `mfm-nursery-rhymes`)

- **WhisperX stretches a word's end over the laugh that follows it** ("crack" read as 63.24–64.38; RMS shows the word ends
  at ~63.6 and a laugh starts at 64.0). The refiner trusts that span, so it would have kept the laugh. → **Measure the RMS
  envelope at any punchline ending** (`projects/mfm-nursery-rhymes/work/rms.py` pattern), set the out-point by hand and
  mark `no_refine` → PLAYBOOK § 2.
- **WhisperX can start a word late after a pause** ("His" read as 632.95; the acoustic onset is ~632.54), and the refiner
  then flags a false "merged-repeat". → Same fix: measure, split, set the boundaries by hand.
- **A YouTube podcast source is pre-mastered**: the voice-gain step measured 0 dB and the limiter still ran hot. → Splice
  Onyx sources with `AMPLIFY_DB=-2` by default.
- **Spoken numbers get checked before they reach the audio, not only the graphics.** Little Baby Bum's "$65M" contradicted
  the only public estimate ($8–11M, undisclosed deal), so the line was cut from the cut itself, not just from the screen.
  Where a spoken number is defensible but a commenter could still question it, a small grey source line goes on the CARD
  ("incl. $11M earn-out", "backed by Blackstone"). It's a credibility signal, not clutter.

## QA round 1 on the pilot render (2026-10-05, `mfm-nursery-rhymes` v1): 32 confirmed / 12 refuted, about 15 unique

Multi-lens review: 5 lenses (captions, framing, motion, audio, facts), each defect sent to a skeptic who tried to refute it.
Script: `projects/mfm-nursery-rhymes/work/qa/onyx-sample-qa-r2.js`; results in `work/qa/qa-v1-result.json`.

- **WhisperX can squeeze a spoken number into ~80 ms and then hand the rest of its audio to the next words.** "$103
  million" was stamped as "$103 million" 6.77–7.13, followed by a bogus "92 million"; the real "million" ran to 562.30
  (source). The out-point was set by that stamp, so the cut said "for a hundred". → **Every number in a cut gets an
  independent check of where its audio actually ends** (a second ASR on the slice plus the RMS envelope) before the
  out-point is locked. The stamps are patched in build.py (`PATCH`/`DROP`) → PLAYBOOK § 2.
- **Podcast episodes have their own layouts inside the "talking head"**: MFM uses a 22 px white frame around the whole
  episode, burned-in name labels, a two-up layout (both hosts in white boxes on black), and full-screen chart inserts.
  → **Scan the base cut for layout changes before the build** (top-band luma per frame finds a two-up span; row/column
  brightness finds a border), crop the border off the base, and give a two-up span a **16:9 CARD that crops into the
  speaker's box** (`CARD16`, region transform in percent) → README § 3, PLAYBOOK § 5.
- **Hand-typed times rot the moment the cut changes.** → build.py v2 anchors every animation to **words, splice joints and
  measured camera cuts** (`at()`, `JOINTS`, `TWO_UP`, `SAM_CUT`). A re-cut moves the graphics with it → PLAYBOOK § 5.
- **A layout change that also changes speaker starts before the camera cut** (`CAMCUT_LEAD` 0.18 s); otherwise the new
  speaker flashes full-frame. **Captions end at a speaker-changing cut.** A zoom change at a camera cut snaps (the
  content changes anyway); otherwise it eases with the morph → README § 4.
- **Graphics enter only after the window has landed** (morph end − 0.15 s), never over a face that's still full-frame.
- **Captions are positioned per chunk** (never at the mode switch, or they show at the old position for 1–2 frames), and
  **carry a dark pill for the whole morph**, because the moving window passes behind them → README § 5.
- **A number never shows a static "$0" and never flashes its final value**: it rises in already counting, from an HTML
  value of `$0` / `$0M`.
- **Library SFX files aren't always single hits**: `Pop 1/2.wav` hold four pops each, so a 0.6 s slice fired two of them,
  the first one late. The long `Sub Drop.mp3` is a sustained sine, not an impact. → Measure onsets and slice single hits
  (`pop-1-single.wav`, `pop-2-single.wav`); no sub-drop in this look → README § 6.
- **The approved storyboard is the contract**: numbers BELOW the card, a 220 px corner bubble. v1 drifted from both and QA
  caught it. → Fixed in v2; README § 3 now states it.

## QA round 2 (v2, 2026-10-05): every round-1 high fixed; 22 confirmed / 7 refuted, about 11 unique and mostly one-frame

- **Measured cuts must be frame-exact on the RENDER grid.** A 24 fps base under a 30 fps render: a layout boundary goes on
  the first render frame that SHOWS the new base frame, `ceil(k/24*30)/30`. One frame off at each end showed the uncropped
  two-up and a 2.5× blow-up of a hand → `TWO_UP`/`SAM_CUT` are re-measured per base frame (pattern in BRIEF).
- **A 16:9 → 1:1 reshape on a source with a burned-in label** exposes the label while the window is still wide. → Start
  the zoom at 1.82 and ease it to 1.04 on the same ease as the window. The visible fraction stays at about 55 % of the
  width, so the label (ends at 20 %) never shows → README § 3.
- **Hand-patched word stamps must be relative to their segment**, or the next re-cut silently un-patches them (it did).
- **WhisperX's first word can be ~0.3 s late** (Sam's long "I"): the in-point sat mid-vowel. → Check the RMS onset of
  the FIRST word of the cut, and patch its stamp.
- **A fade that ends "at" a cut can miss it by half a frame through q() rounding.** → End fades a few frames early
  (T − 0.34 for a 0.25 s fade).
- **Speaker cuts that happen INSIDE a segment** (the source cutting from Shaan to Sam) count as speaker changes for the
  caption clamp too.
- **Around the bubble**, morph with power3.out and delay a caption up to 0.15 s, so the window leaves the band before the
  text lands.
- Refuted, and kept as decisions: no whoosh on returns to the face; "THE THREE DEALS" (Shaan's framing, and these are the
  three he names); "0 owned by big studios" (his claim, set in his own words underneath).

## QA round 3 (v3, 2026-10-05, final): 17 confirmed / 2 refuted, no new classes; all fixed and verified on v4

- **The renderer's frame mapping is measurable, so stop guessing it**: 30 fps render frame n shows 24 fps base frame
  floor(0.8n + 0.24). → `rframe(base_k)` in build.py gives the first render frame for any base frame; use it for every
  layout boundary, camera cut and punch-on-a-jump-cut. My own frame detector was one frame low.
- **A caption that waits for a morph must wait for the FACE, not just the window**: when shrinking into the bubble, the face
  leaves the caption band about 0.28 s in. Cap the wait at 0.15 s after the word, and fix the word's stamp first if it's late
  (the "none" stamp was 0.12 s late; stacked with the wait, the caption ran 0.24 s behind).
- Three QA rounds took the pilot from 32 → 22 → 17 confirmed defects, each round smaller and closer to the frame level. The
  cap (3) held: round 4 was replaced by verifying the exact frames of each fix.

## Affan's review of the pilot (2026-10-05)

- **The look is approved:** *"this video is fine, it doesn't have any problems."* It is *"a classic minimalistic Instagram
  style."* → This preset is now the INSTAGRAM look; README header.
- **Not enough sound effects in places.** → README § 6: a sound on every visual event (returns to the face too, softer), and
  no stretch over ~1.5 s without one. Calibrate the density against the YouTube reference's measured SFX map.
- **YouTube Shorts need a different look.** Each sample is built for the prospect's PRIORITY platform (YouTube or
  Instagram) → PLAYBOOK § 0, plus a new preset `presets/youtube-shorts/onyx-samples-youtube/` built from Affan's reference
  (Shawn Ryan Show, `KUMikP6a2eI`).

## Reference study 1 (2026-10-05, batch 1): accounts doing minimal-but-visual better than our pilot

Affan: *"go onto Instagram… find channels doing that style even better than you and replicate those… keep on improving."*
Method: reel IDs and view counts from his Chrome (the Reels grid); 12-frame contact sheets drawn from the reel's own video in the
app's built-in browser (Instagram's player doesn't show in Chrome screenshots, and nothing gets downloaded).

| Account (reel) | Views | What it does that the pilot doesn't |
|---|---|---|
| @colinandsamir `Ddre8BhuIWD` (24 Sep 2026, 88 s) | **21.8M** | Opens on a participation hook: two stacked speakers labelled **A / B** under "Which hook is better?". Then a clean WHITE canvas: big bold black headline type, real UI screenshots and product shots as the visuals, an emoji sticker; quiet small captions under the speaker. Editorial, keynote-clean. |
| @aliabdaal `Ddn4prylGUE` (23 Sep 2026, 90 s) | 294K | The speaker stays FULL-FRAME; small crisp graphics float in the TOP band above his head: a kinetic title with a starburst, keyword + icon pairs ("Hiring + AI"), tiny illustrated process icons, UI/screenshot cards, app logos. Captions are a small translucent pill, sentence case. |
| @thechrisdo `DdMhWYUgUfW` (12 Sep 2026, 68 s) | 239K | Documentary-minimal: a wide stage shot, a cut to the audience member asking; captions are **white rounded boxes with black sentence-case text**; a one-word yellow title card at the start. Almost no graphics: the exchange carries it. |

**What changes for batch 1's Instagram samples** (on top of README § 1–6):
- **Less window-morphing, more full-frame speaker with graphics in the top band** (Ali): icons, keyword pairs, UI cards, logos.
- **Real artefacts as the graphics** (Colin & Samir): screenshots of the actual product, page, post or headline, on a clean light
  canvas with big black type for explainer beats. Abstract count-ups only when the number IS the story.
- **Match the prospect's own caption house style where they have one** (Chris Do: white boxes, black text). It shows we studied
  them.
- **An exchange beats a monologue** (AW study, same day): when the moment is a confrontation in the room, cut between the people
  and keep graphics minimal; the exchange is the visual.
- Next study before each Instagram build: 2–3 more accounts (candidates: @thedankoe recent reels 358K/307K, DOAC's real handle,
  @hubermanlab clips, @chriswillx).
