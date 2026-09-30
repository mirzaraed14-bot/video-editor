# LESSONS — affan-afterhours-facecam

Appended after every review, unasked: *lesson → change made → file*. Channel-wide lessons stay in
`../affan-afterhours/LESSONS.md`; only what is specific to this style lives here.

## 2026-09-25 · second vertical short: 3 words max (ABW8 · Sequence 06, `projects/gta6-collectors-box`)

- **The cap moved from 4 (Sequence 04) to 3 the same day.** So the cap is set per short: ask for it, or
  default to 3 (the stricter figure, and their Abundance Wisdom cap). The route repeated, so it became a
  tool: `workflows/sequence-captions.py` (read → transcribe → captions.txt → srt → import).
- **Whisper writes spoken prices as digits and can inflate them:** "two seventy" became `$270,000`. The
  0.6 s of speech gave it away, and a re-listen with digit tokens suppressed confirmed it. Check every
  number's duration against its words. Fix goes in `corrections.local.json`, which the tool applies.

## 2026-09-25 · first vertical short captioned (ABW8 · Sequence 04, `projects/vice-city-heat-arena`)

- **The creator: "captions 4 words max per layer" for this short.** The long-form rule (no captions) does not
  cover shorts. First data point: an editable Premiere caption track (.srt), ≤ 4 words, wall to wall, with
  the creator's censor/punctuation habits from their other captions. One-off until a second short repeats
  it. → `projects/vice-city-heat-arena/RUN.md`. No shorts caption *style* exists yet: ask or measure one
  before styling.

## 2026-09-21 · measuring the style (before any job ran in it)

- **A face detector cannot measure a talking-head edit on its own.** A game character's close-up (Lucia in the GTA 6
  trailer) passed a size-and-centre rule and read as the creator; the face box jitters ±10 % with a head turn, which
  read as "cut zooms" at 12/min. What worked: the SET as identity (a hue histogram of the frame matched against the
  creator's own shots, cosine ≥ 0.70 — `workflows/style-set.py`), and the BACKGROUND as the zoom meter (feature
  matching on the wall/sign/monitor with the person masked out — `workflows/style-zoom.py`). → both are now stages
  of the standard style measurement; `style-report.py` refuses to quote face-box zoom numbers when a zoom track exists.
- **Duplicate frames do not mean slow motion.** Half the frames repeat wherever a 30 fps game clip sits on the 60p
  timeline, and a held pose repeats frames at any speed. The creator's face cam is real 60p. A slow-down with the
  pitch kept (Premiere's default) shows only as two signals agreeing: 3+ consecutive words at ≤ 0.75x the speaker's
  characters-per-second AND repeated frames over the same face time. → `style-report.py` (d). Four found across the two
  videos, all ~0.6x, 1–3 s.
- **The "cut it midway" device is rarer than the creator's description suggests:** one measurable chopped word in two
  videos. Plan it as a spice (≤ 2 per video), not as a rhythm.
- **The third reference ("CAN'T Do Anymore", 17k) has no local master and the creator dropped it (2026-09-22):** the
  two measured masters are the spec. If it ever matters, `yt-dlp` is installed and the five tools take any file.

## 2026-09-21 · what the frame-by-frame read added to the numbers

- **The 170k video has MORE cards than the 35k one (11 vs 4), not fewer — and every card is the spoken sentence set in
  type.** The probe counted "1 still" because a creeping card is not motionless. → posters are counted from the
  catalogue, never from the probe; the rule is 1–1.6 per minute on tweetable lines (README § 4b, NUMBERS.md).
- **The slow motion is on the INSERTS.** Face slow-downs are 1–2 per video; game footage and reaction clips are slowed
  as a matter of course (0.5x → 0.03x). A speed-ramp plan belongs in the overlay plan, not the face plan.
- **Hard cuts only, both videos, every boundary** — verified at 1/10–1/20 s. No transition of any kind is part of
  this style.
- **Two long face-only stretches per video are deliberate** (36 s, 39.5 s): the argument and the opinion get nothing.
  A density rule that fills every 6 s bare stretch would break this style; the density lives in the cut zooms.

## 2026-09-22 · gta6-pc-release, the first job cut in this style

- **The shoot is a teleprompter read, and it cuts 65 %.** 16:18 of raw → 5:51 on the timeline, 141 clips. Of the
  raw, **8.7 minutes was silence** (the creator reading ahead between lines) and 23 take groups held 31 superseded
  takes. The speech itself was 7.4 min; keeping the last take of every group gives 6.8 min; the necessity filter
  took it to 5.85. Expect that shape again on a scripted shoot — the kill is mostly dead air and retakes, not lines.
- **The delivered pace is well under the style's 200+ wpm**, because the pauses are between sentences rather than
  inside them. Cutting every inter-sentence pause is what gets it there; do not also cut inside lines.
- **Boundaries on the OBS voice track need absolute-dB judgement** (channel LESSONS, same date) and long-span
  WhisperX words need pinning. Budget for it: eleven boundaries were hand-corrected on this job.
- **Keep two or three pauses, pinned.** The ones kept here: the punchline beat ("Oh, shit… 2028."), one rhetorical
  tag ("…on PS3… right?") and the drumroll on the video's central claim ("November 2027 is… when the PC version
  will be released"). Everything else goes.

## 2026-09-22 · the creator's own finished edit, measured against the rough cut handed to them

Diffed `premiere-backup/ABW6-FINAL-shipped.prproj` against `transcript/cuts.json`. Their comedy grammar is its
own file now: **[`HUMOR.md`](HUMOR.md)**. Everything below is the general editing.

### They cut another 10 % out of an already-ruthless rough cut
351.1 s handed over → **312.4 s of source kept** (their timeline reads 315.7 s; the 80 % clips stretch it).
**37.1 s removed across 31 spans.** The rough cut was not tight enough, and the pattern in what went is specific:

- **A funny three-beat aside that restates a point already made still dies.** The whole PC-building gag went —
  "a lot of people probably built a PC" / "got bored waiting" / "sold the PC, built another one", ~5.3 s. It IS
  funny. It was cut anyway, because the 19-month wait had already landed. *Funny is not a reason to keep.*
- **The redundancy I talked myself into keeping was cut.** "Making a game for PC is like making a shoe." was
  flagged at cut time as redundant against the line after it, and kept for "rhetorical parallelism". They cut it.
  Trust the necessity filter over the rhythm argument.
- **They ENTER SENTENCES LATER than I do.** Heads get trimmed: "So the internet" (1.65 s) off the opening line,
  "First, I'm gonna" (3.89 s), "GTA 5 came" (0.88 s). I keep the whole sentence; they start mid-phrase.
- **Connective tails go:** "That's the deal.", "easy", "Right?", "okay.", "Then PS5." — all sub-second, all cut.
- The weak line already flagged in RUN.md ("this is the one I actually think is the biggest deal…", 4.40 s) went,
  confirming the flag was right.

### What they ADDED to the overlays
- **V3 19 → 23 clips.** Nothing of the handed-over work was removed. They added the opening meme themselves
  (a facepalm meme), used a **screenshot** rather than a video for the five-stages cue (matches the preset's
  "found artefacts cut in raw"), and **nested one overlay** (`Nested Sequence 129`) — nesting is not just for
  face runs, it is how they treat an overlay too.
- **V2 matte 19 → 26 clips.** They extended the matte under their OWN additions, including the meme at 0:00.
  **The matte is universal: every overlay gets one, no exceptions.** Placing overlays without it is unfinished.
- They added a V4 track and left it empty.

### Numbers for the next job
| | |
|---|---|
| final runtime | 315.7 s |
| V1 clips | 127 (19 of them nests) |
| cut rate | 24.1 / min |
| median clip | 1.77 s · shortest 0.20 s · 26 under 1 s |
| slow-downs | 10, **all exactly 80 %** (see HUMOR.md) |

### Tooling note
Premiere 25.0 stores keyframes as encoded parameter blobs inside the `.prproj`, so **cut-zoom scale values and
hold lengths could NOT be read from the file.** The zooms live inside the 19 nests. Get them next time off the
LIVE project while it is open (bridge `getKeyframes`), or measure an export with `workflows/style-zoom.py`.
A first attempt at the removal diff was wrong by 4x because it read only V1 and never recursed into the nests —
`scratchpad/removed.py` has the version that reconciles.

## 2026-09-25 — gta6-vice-city-sign rough cut: WhisperX hides retakes on the OBS voice track

- The canonical `words.json` merged repeated phrases into single stretched words, so **11 cut rows that looked
  like one clean take each actually contained a retake** ("or through the Heat's last home game" three times,
  "the Rockstar logo" twice, "most of it is going toward turning" twice…). polish-boundaries and dead-air-qa
  cannot see this: the audio is continuous speech.
- **Change made: transcribe the ASSEMBLED cut before replay, every face-cam job.** Concatenate the kept spans,
  run faster-whisper large-v3 over it, and read it as a script. Each suspect is located with a per-burst
  transcription of the raw window, and every splice is PROVEN by transcribing exactly the kept spans. Long-window
  ASR collapses repeats and short concatenations hallucinate them, so only the exact-span test counts.
- The creator said "keep the improvised jokes": kept every aside, cut only retakes, stumbles and dead air.
  Result 1070 s raw → 5:59, 146 clips.

## 2026-09-30 — gta6-hurricanes rough cut (ABW8 · Sequence 16): transcribe per burst FIRST
- The creator synced it in Premiere and said so: **their in-points are the offset** (camera = OBS + 19.3833 s),
  muxed verbatim with the camera-mic tail exactly where they switched A1. No measuring when they say it's synced.
- **Change made: a per-burst transcription of the whole raw BEFORE authoring** (`review/raw-bursts.txt`: split on
  energy gaps, transcribe each burst alone). It showed the hidden retakes up front ("In Rockstar games" x3,
  "Braking gets worse" x3, "30 plus land" x2), so the first EDL was already close; WhisperX alone would have hidden them.
- The mechanical reviewer running EVERY joint through exact-span ASR still found 5 real ones the long-pass cut
  transcript missed (a "ha-" fragment, a trailing "I th-", "I, I, I", "the a store", "what happened—"). Keep that
  review exhaustive; the long single-pass transcript both misses fragments and invents doubles.
- Result: 752.8 s of voice → 6:48, 122 clips. Jokes kept whole (the zoo, the hiking punch line, "I don't know why I
  did that", "Where was the tweet? God damn it"), their long pauses trimmed to ~0.5 s instead of cut.

## 2026-09-30 — gta6-hurricanes overlays from the creator's Tella brief (ABW8 · Sequence 16)
- **The brief convention:** the creator drags the face clips that want an overlay UP TO V2 and talks through each
  one in a Tella walkthrough with the screen audio muted. 43 blocks → 24 slots; the playhead timecode at each
  sentence resolves "here". Their standing overlay rules, said three times: **edges bleed** (inset, never full
  frame), **a creative colour matte behind every overlay, varied, never one colour**, **drop shadow on the overlay**,
  screenshots clean (Higgsfield-enhance when soft), downloads into the bin named after the video's topic.
- **Change made: overlays are baked as ProRes 4444 alpha clips** (85 % inset, 22 px rounded corners, shadow baked in,
  because Premiere's Drop Shadow is near-invisible on a dark matte, lab-notes) on **V4**, with a per-slot animated
  gradient matte on **V3**: separate clips, so a matte or an overlay can be swapped alone. Tool:
  `projects/gta6-hurricanes/overlays/build.py` + `place.py` (additive; refuses if V2 moved since the brief).
- A "quote" overlay is a Higgsfield BACKGROUND (no text, 0.25 credits) with the exact quote set in type by us:
  the quote is verified against two sources first (Rob Nelson / IGN, 2026-08-27).
- Preview every segment's frame BEFORE rendering: 4 of 44 picks landed on the wrong shot (ESRB card, a social
  post, a text card, the creator's own face in their Wolverine video). Trailer/compilation shots are short; check
  the whole span, not one frame.

## 2026-09-30 — gta6-hurricanes, the creator's pass and three calls (ABW8 · Sequence 16)
- **The creator's pass, read off the timeline:** 18 nests + 22 gradual pushes (100→105/110) on V1, cut zooms as
  razor-cut clips with a static scale > 100 (on V1 and inside the nests), music on A2 (three Epidemic tracks). The
  overlays were untouched: 48/48 V3/V4 clips where they were placed.
- **Cut zoom = the music drops out for that block.** Lesson → change: `music-dropouts.py` finds every cut zoom
  (a static scale step, nests included, the gradual pushes excluded) and lifts the A2 music inside it. 22 ranges;
  the music was already silent in 5 (the creator had cut those by hand, so this is their rule, not ours) and lifted
  in 17 (29.95 s). Graduated to PLAYBOOK § Music.
- **Overlay switches pop.** Lesson → change: `overlay-sfx.py` puts an Epidemic mouth-finger pop on every overlay
  entrance and internal switch, 44 on A3. Graduated to PLAYBOOK § 6 SFX.
- **A rapid run of stills gets NO push** (C02: four Game Informer screenshots at 0.4 s each, each pushed in 5 %: "too
  flashy… very jarring"). Lesson → change: `build.py` `NO_PUSH = {2}`, re-rendered as `ov-c02-v2.mov`. One-off so
  far; if it repeats, a still held under ~1 s never moves.
