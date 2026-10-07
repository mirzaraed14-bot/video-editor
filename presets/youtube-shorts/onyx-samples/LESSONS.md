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

## Reference study 2 (2026-10-05, before the Rob Dial build `projects/mindsetmentor-23k-call/`)

| Account (reel) | Views | What it does |
|---|---|---|
| @melrobbins (12.8M followers; reels 1.3–2.1M) | 1.3–2.1M | One static shot, white caption boxes, no graphics at all. |
| @jayshetty (a 4.8M reel) | 4.8M | 1 s of him in B&W, then warm cinematic stock B-roll under his voice the whole story long; small white captions. |
| @robdial's own reels | — | B&W grade on him, small YELLOW sentence-case captions. |

**Applied to the Rob sample:** Rob in B&W, warm B-roll for the story beats (faceless when he says "I"), HIS yellow captions (the new
`plain` caption style: colour/size/weight per job, dark glow + soft radial scrim), only three diegetic graphics, each an object
from the story itself: an iOS incoming-call banner (`call` card, with a vibrate sound), the `$23,000` count-up in a dark pill
(`number` + `"box": true`), and a bank notification (`notify` card, with a ding). Credit line "Rob Dial · The Mindset Mentor"
(his team's condition), delayed past the hook (`credit_t0`), in a pill (`credit_pill`).
- **Diegetic UI beats abstract graphics for a told story.** A phone call in the story = the phone's call screen; money arriving = the
  bank's notification. They read instantly and need no kicker.
- **A bright B-roll shot behind yellow captions fails contrast** (a sunset time-lapse measured 1.4–2.9:1 on 9 frames even with the
  scrim). The fix lives in the PICTURE, not a heavier scrim: `grade.shade` {y0, y1, a} darkens the bottom of that one shot (kit
  `yt_picture.py`, 2026-10-06). A heavier caption scrim reads as a grey haze.
- **QA r2 sound:** soft "return" whooshes at −22 dB are inaudible under a voice + bed (best excess −10 dB). Returns get the brighter
  `tick` at −22 when a whoosh would have to be louder than the entrances; never drop a return's sound (README § 6).
- **Caption timing with a 0.15 s lead:** back-to-back words make a chunk vanish before its last word is spoken. The next chunk starts
  at max(first word − 0.15, last word of the previous chunk + 0.06).

## Reference study 3 (2026-10-06, before the Chris Do build `projects/thefutur-nonprofit-15k/`)

Same method (grid views from Chrome; 16-frame sheets drawn from each reel's own video in the built-in browser, nothing downloaded).

| Account (reel) | Views | What it does |
|---|---|---|
| @thechrisdo `DdMhWYUgUfW` (12 Sep, 68.6 s) | 240K | Multicam stage role-play: wide, medium, close and an audience cut, a new angle every 2–5 s. Captions are **WHITE text on a BLACK box** (square-ish corners, 2 lines, sentence case, mid-low frame). The thumbnail/opening is one huge yellow condensed number: "$1000". **Correction to study 1:** it said "white boxes, black text"; the frames show black boxes with white text. |
| @thechrisdo `DdmLEIqAbGE` (22 Sep, 54.9 s) | 112K | Same stage format, small plain white captions with no box, a yellow label box at the end. His recent top three are all live money role-plays (240K / 112K / 111K): the format IS his brand on Instagram. |
| @chriswillx (Modern Wisdom) `Dd6ts6OxAgV` (30 Sep, 65 s) | 1M (feed: daily, 200K–1.1M) | A **white label box with black bold Title Case** ("Are You Mocked For Your Healthy Habits?") holds for the first ~8 s, under a small plain caption. After that: tiny ONE-WORD white captions at chest height, and the picture alternates between a wide and a close angle every 4–8 s. No graphics at all. |
| @thedankoe `Dd6gGIJKgI1` (30 Sep, 28.5 s; feed peaks 33.9M / 9.1M / 7.1M) | 101K | Faceless: pure black canvas, one small thin line of type in the upper third, thin white circles, dots and lines that keep moving (a dot orbits, travels a path, a line draws out). Huge negative space. |

**What changes for the Chris Do sample:**
- **Two angles from one 4K camera** (Modern Wisdom, Chris's own multicam): alternate a wide and a punched-in close on the speaker
  every 3–6 s, on word boundaries; cut to the woman for her lines (the exchange is the visual).
- **His caption house style:** white text on a black box, sentence case.
- **A title label held over the hook** (Modern Wisdom + his yellow one-word title): a question in a box for the first ~3 s.
- **The one GRAPHIC beat is Dan Koe-minimal:** a black canvas, thin-line geometry, small type. For "$1,000 vs $15,000": two circles
  whose AREAS are in the ratio of the money (1:15), drawn as thin white lines, small numbers under each. No count-up, no gold.

## Rob Dial sample, QA rounds 2-3 (2026-10-06, `projects/mindsetmentor-23k-call/`, final v6)
- **A stock cutaway's last frames can be a frozen hold** (c01's frames 140-145 = frame 139): the shot froze 0.25 s on her face mid-word.
  Check the tail of every B-roll clip for repeated frames before choosing `src_in`; shift the shot, never stretch it.
- **The ~1.5 s rule needs about 0.7 designed sounds per second** (34 cues in 49.4 s). Cut cues alone gave 0.49/s; the gaps were closed with
  ticks at -22 dB placed where the voice leaves room (each measured: audible yet >= 21.9 dB under any word).
- **A cue that belongs to a cut peaks ON the cut**, so its `t` sits ~0.07 s before the boundary (the kit starts the sound 0.05 s before `t`).
- **A card must not state what the speaker hasn't said yet**: "Wire transfer received" while he says "I'll get it wired" → "incoming".

## Batch 1 builds, QA round 1 (2026-10-06): what the reviewers caught on Chris Do, Rich Roll, Harbinger, Pomp
- **Every rough-cut joint INSIDE one camera take is a jump cut unless the angle changes ON it** (Chris Do: two pose jumps inside one
  long shot, HIGH). Before writing shots, list the visible picture jumps (frame-diff peaks on the base) and put a shot boundary, with a
  zoom step of at least x1.18, on each one. A punch-in of a few % reads as a mistake; `r` is per SECOND, so keep push-ins ~6 % per shot.
- **A stock clip is checked at full size, frame by frame, before it's used**: the "bank teller counter" was a coffee shop with a
  stranger's face, a card-network decal and a duplicate frame every 6th frame; a "revolving door" carried G Pay / VISA decals and an
  hours sign; a "bank facade" carried a real store's name. Text, logos and faces in stock = swap the clip (or use the speaker).
- **A named real person never gets a stranger's face as a stand-in.** When no faceless clip exists, stay on the speaker.
- **Hook frames: crop strangers out** (a man behind the guest in the hook) and keep the title label off the guest's head (measure the
  hair top across the shot, not on one frame).
- **Diegetic cards must match who does what**: an incoming-call banner reading "Zac's dad · calling…" said the dad called; the speech
  says the TELLER called the dad → "Rhonda Jackson · PNC Bank · calling…".
- **A bright B-roll shot behind white or yellow captions** gets `grade.shade` (a bottom gradient in the picture), measured to ≥ 4.5:1.
- **The ~0.7 designed sounds per second** (Rob Dial lesson) is needed on every sample: the first builds all came in at ~0.5/s with 3-7 s
  silent stretches; the reviewers measured gap-fill ticks that stay ≥ 11-20 dB under the words they touch.
- **The audio must cover the last frame**: a cut 7 frames shorter than the picture leaves a silent tail; set `frames` to the audio length.
- **Kit:** `ig_build.fps_arg` passed "30.0" for an integer rate and HyperFrames refused it (fixed: "30"). Topaz Iris with frame
  interpolation ("fi") dropped 8 of 26 frames on a near-static two-up take: run `topaz-iris.py --no-fi` on talking heads (fixed by
  re-doing the take and splicing it back to the exact frame count).

## Affan's review of batch 1 (2026-10-06): captions just below the lips
- *"I like the shorts you have made but the distance between the captions and the lips of the viewer needs to be shorter… I was constantly
  moving my eyes up and down naturally which creates irritation… I don't want the captions on top of the lips but conveniently below."*
- → `kit/ig_capy.py` (new): per shot, the caption top = the lowest mouth line of the shot (YuNet mouth landmarks, now stored by
  `yt_faces.py`, mapped through the crop) + 0.075 × face height + 6 px. Checked on Rob, Chris Do and Rich Roll frames: the landmark sits on the
  lips and the caption lands on the chin, ~60-95 px under the lip line (was 300-700 px under it). Wired into `ig_build.py` and `yt_build.py`;
  `captions.fixed_y: true` turns it off. All batch-1 samples re-rendered with it (Rob v7, Chris Do v5, Rich Roll v6, Harbinger v5, Pomp v4, Rollo).

## Lip-line captions, QA round 3 (Pomp) + round 2 (Rollo), 2026-10-06: a chunk must move ON the cut
- **A chunk on screen across a cut kept ONE shot's height** (ig_capy placed each chunk by its mid-time): in the other shot it sat on the
  mouth (Pomp: 13 runs, 61 frames, e.g. "that Alameda" over Zac's lips) and the caption height changed mid-shot 25 times. Rollo: a chunk that
  starts ~0.13 s before its word (the lead) took the NEXT shot's height 3-4 frames before the cut (onto his lips 3 times).
  → `kit/ig_capy.py`: (1) SNAP: a chunk that would appear 1..lead frames before a cut appears ON it (the chunk before holds to the cut);
  never later than its own lead, so the text still lands on/before the word. (2) MOVES: a chunk spanning a cut is placed per SEGMENT and
  jumps to the new shot's lip line exactly on the cut frame (`"moves": [[frame, y]]`, read by `ig_overlay.py` and `yt-captions.js`).
  Instagram keeps the hand-tuned `start`/`end` and writes the effective `show`/`hide`; YouTube rewrites start/end (regenerated each build).
  Re-rendered every sample: Rob v9, Chris Do v7, Rich Roll v7, Harbinger v6, MFM v11 (audio null -91 dB vs the previous finals).
- **A face inside a screen capture is not the speaker**: a post photo / avatar in a FIT inset was read as Rollo's face and put a caption on
  the screenshot. → an inset face counts only if it is inside the inset and >= 0.3 of its height (speaker insets measure 0.55-0.60).
- **The label paint-out left a hard rectangle** on Pomp's dark wall (mask `g < 30` took the whole background) and a ghost of the letters
  (the drop shadow). → `yt_picture.fill_box`: each column blends the box's clean top rows into the clean rows just under it (past the shadow),
  feathered at the side edge: a bookshelf's spines continue, a wall stays a smooth gradient.
- **(r3, later the same night) The snap must never make a caption LATE.** A blanket "up to lead frames" snap assumed every chunk had
  its full lead; Rollo's "IS GOING TO DO." came out 0.077 s after "is". → snap only while the chunk still appears >= 0.02 s before its
  first word (the measured onset, else the transcript start - 0.055 s). Instagram's 0.08 s lead leaves no room, so Instagram chunks keep
  their time and only MOVE on the cut.
- **Mouth corners are not the lower lip.** The corner line barely moves when the mouth opens; the lower lip drops 0.09-0.12 x face height
  below it (Rollo, measured on 880-1320 px faces; Pomp: the box clipped the lower lip on 85 frames). Default gap 0.075 -> **0.13** x face
  height (spec `captions.lip_gap`). Rollo's targets from the reviewer's ruler reads came out within 2 px on s01/s23/s25, 20-45 px lower
  (still on the chin) elsewhere. Where the caption can't go low enough (a tight face low in the source, the crop window already at the
  frame's bottom edge), lower the watermark (`watermark_y`, Rollo 1360, hook moved with it), never the caption onto the lip.
- **Topaz on every sample, Affan's rule (2026-10-06)**: interpolation (replace duplicate frames) always, Iris only for <= 1080p.
  Rich Roll's 4K cut had 113 exactly-repeated frames (8.5 %); Chronos per take -> 4, frame count exact. `base_hq` = `<job>.topaz-fi.mov`.

## Affan's review 2 of batch 1 (2026-10-07): lesson -> change -> file
- **Per-shot caption heights read as captions jumping** ("the base positioning shifts… that's going to mess with the viewer's head").
  The lip-line fix of 2026-10-06 overshot: he wanted the captions CLOSE, not moving. -> one constant y per video (`ig_capy.py`
  constant mode) + consistent framing; README rule 2.
- **Punctuation**: only `! ?` and quotes. -> caption builders strip the rest; README rule 1.
- **The rise looked choppy at 30 fps.** -> overlay at 60 fps; README rule 3.
- **Quiet SFX are no SFX** (Rob, Rich: "the sound effects are not there"; the samples had 34-76 cues at -22 dB under voice + bed).
  -> one audible, crisp Epidemic SFX per graphic; README rule 6.
- **All-yellow captions** (Rob). -> white base, coloured emphasis words; rule 7.
- **Hook for strangers** (Rob): a personal story from someone the viewer doesn't know needs the who + why-care set up first; rule 9.
- **Clip choice** (Rich Roll): a personal story with nothing in it for the viewer fails however it's edited; pick a moment that gives
  the viewer something to take away (the engine's selection step now asks "what does a stranger get from this?").
- **The minimal look reads "too basic" on Chris Do and Harbinger** -> both move to the Sean Ryan (YouTube) look; Rob and Rich keep this
  look with more motion graphics and SFX.

## 2026-10-08 · Rich Roll re-pick (Bryan Johnson's five sleep rules)
- **The value bar decided the pick**: a stranger leaves with a protocol (heart rate before bed + five free rules with numbers).
- **New cards for informational clips**: `heart` (a beating heart + an ECG line: "one marker"), `receipt` (his "accounting system" metaphor
  drawn literally, one tick per item, a stamp on "you can't cheat it"), `rules` (a numbered list that builds one rule per beat, colour
  swatches in a sub line). Each entrance and each row has its own Epidemic sound.
- **Cards go BELOW the caption band when the speaker's single frames the face high** (Bryan): the face is never covered, the captions sit
  just under the lips, the cards fill the chest area (y 900-1600).
- **Rough-cut joints**: audio-qa's click flags were real both times: a word's sibilant tail ("eyes?") and an onset ("So") clipped by the
  refiner. Read the 5 ms envelope at every flagged joint and set the boundary by hand (`no_refine`).
- **A list card never opens as an empty box** (v2: the 5-rule card sat as a dark panel for 0.9 s before rule 1). The `rules` card now
  GROWS: a clip-path measured off the laid-out rows reveals the title strip, then one row per beat (the drop shadow lives on a wrapper
  so the clip does not cut it). Set explicit `line-height` on every text class a card measures, or font fallback shifts the clip.
- **Measure a tall card's bottom on the overlay alpha, not by eye**: 5 rows with subs ran 1105 -> 1649, past the 1620 band. Lifted to
  y 1070 (bottom 1611); the caption line (top 911) still clears it by ~85 px.
- **The `splice.sh` video offset** (yt-dlp sections keep the video's real start time): an A/V desync of 4.95 s shipped in the v1 base;
  fixed in splice.sh (`video_offset`), Topaz re-run on the corrected base.
- **QA r1 (Rich Roll): the caption "rise" was a no-op on LEFT-aligned captions.** `.cap .inner` is `display:inline` there (for
  the multi-line box clone), and CSS transforms do nothing on an inline box, so 49 of 52 chunks hard-cut in. The kit now animates the
  absolutely-positioned `#c{i}` (moves set `top`, so they don't collide). Verify a rise by measuring the overlay alpha over frames
  +0..+12 after a chunk start, not by eye.
- **Epidemic files carry lead-ins** (measured 5 ms RMS): `pop-glass` has a soft pre-tick and the real pop at 0.595 s, `whoosh-light`
  is silent until 0.42 s (crest 0.75), `whoosh-air` until 0.14 s. Untrimmed, every pop and title whoosh landed ~0.6 s after its card.
  `ig_build.ES_LEAD` trims them with a 5 ms fade-in; clicks/ticks were raised from 8 to 3 dB under the voice peak (they lived
  above 6 kHz and read as nothing on a phone). **Rob Dial's v15 was built before this fix** (Epidemic kit, centred captions, so its
  rise is fine): its pops/whooshes land late too; rebuilding it is a `--skip picture` run if Affan wants.
- **A card's entrance sound can be chosen** (`"sfx_kind": "pop"`): a whoosh under continuous speech is masked, a transient pop is
  not. Receipt rows tick 0.08 s BEFORE each word so the click clears the word's onset (a tick on the "s" of "stressed" vanished).
- **Captions break on a speaker-changing camera cut**: `captions.breaks` [t, ...] (cut-timeline s) forces a chunk break.
- **A source camera cut 1 frame before an EDL joint** leaves one frame of the other camera in the previous shot's crop (a 33 ms
  flash): end that shot one frame early (`cut18 = F(starts[i18]) - 1`). Look for scene cuts within ±2 frames of every joint.
- **A hook is a stake, not a label**: "5 rules for better sleep." -> "One number at night / decides your sleep." (his own claim).
  A serif title line holds ~19 characters at the title size before it wraps.
