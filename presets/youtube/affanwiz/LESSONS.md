# affanwiz — LESSONS (append-only; the channel's learning log)

One entry per lesson: **what was learned → what changed → where**. Newest at the bottom. A lesson that repeats
becomes a README number or a PLAYBOOK rule (say so in the entry). Written after every creator review and whenever
a job teaches something.

## 2026-09-23 · channel set up, monetized-before-gta6

- **AffanWiz is its own channel** (English personal brand promoting the creator's Skool community), separate from
  Affan Afterhours and from the Urdu `@affanwizu` reels. → its own preset folder, `presets/youtube/affanwiz/`.
- **The handover is a Premiere sequence with a pre-enhanced voice on A1.** → PLAYBOOK § Intake.
- **No script is supplied for the rough cut** (the creator said to go without one) → cut from the transcript alone.

## 2026-09-23 · rough cut, monetized-before-gta6

- **WhisperX word STARTS ran ~250–400 ms late after long pauses on this setup** (Enhance-Speech voice, near-silent
  room): 5 kept lines lost their first syllable ("I normally", "I got 10,000", "And this happened", "I don't even
  know", "I'll give you") because polish-boundaries only searches 250 ms before the claimed start, then grafts.
  → every IN after a ≥ 0.65 s pause gets an envelope check before replay (job `transcript/fixes.py`); tool fix
  suggested for `polish-boundaries.py`.
- **Merged/compressed words hid whole phrases**: "all it took" sat 1.1 s after where WhisperX put it and the cut
  dropped it. → slice re-ASR of every pinned or ⚠ boundary is not optional on this channel's footage.
- **The creator talks in retakes and restarts** (last take always wins, they re-stated "one more thing", "I would
  100%", "the good thing about longs"); ~58 % of the take was cut. → expect heavy retake grafting on every job.

## 2026-09-23 · overlays, monetized-before-gta6

- **The creator's overlay direction is now the channel's frame** (reference image supplied): no overlay fills the
  screen, tiny ones at 50 % width, Higgsfield-enhanced, animated matte under, drop shadow on each. → README § 1a (locked).
- **Higgsfield's upscaler invents text on tiny crops** (an 81×42 view-count badge came back with made-up lettering
  over the eye icon). A prompted `gpt_image_2_5` edit with the exact text spelled out is faithful. → README § 1a.
- **Spell out every glyph in the prompt, including emoji**: "screaming face" produced 😱 where the original was 😭.
  Compare every generated overlay with its original before it ships. → PLAYBOOK § Overlays.
- **The upscaler rejects images wider than ~2:1** and some portrait jobs at 4k (2k worked). Pad wide strips to 16:9
  with their own edge colour, then crop back. → PLAYBOOK § Overlays.
- **Premiere's Drop Shadow is invisible on a dark matte** (100 % opacity darkened it ~12 %). Shadows are baked into
  the overlay PNG; a video overlay's shadow is burned into its matte segment. → README § 1a.
- Spend on job 1: 67.5 Higgsfield credits for 28 enhanced overlays (incl. retries and one false "nsfw" flag).

## 2026-09-28 · rough cut, charlie-best-youtuber

- **The rough cut goes on the creator's own handover sequence, not a new one.** Job 1 replayed onto a new sequence;
  the creator objected on job 2. → PLAYBOOK § Intake item 5 (clear the handover sequence, replay onto it; the
  project backup is the safety net).
- **The creator doesn't want to approve steps one by one.** A project-local allow list (`.claude/settings.local.json`:
  Bash, Edit, Write, premiere-pro tools) lets the pipeline run unattended when auto mode's check is down.
- **Sync is measured every job: Sequence 12's voice sat 68 ms (4 frames) late** against the camera (job 1: 15 ms). The
  creator lines the Enhance-Speech mp3 up by eye; `sync-dual-audio.py` fixes it at intake. → PLAYBOOK § Intake item 3.
- **polish-boundaries overshoots tight cuts into the NEXT, killed word, and the mechanical reviewer missed all 13**
  (e.g. "...like a human. But" kept 321 ms of "But"). → after polish, run a LEAK SWEEP: any killed raw word
  overlapping a kept clip by > 60 ms gets its OUT moved to the energy dip before it (job `transcript/fixes.py`,
  `review/leak-fixes.json`), then re-ASR the tails. WhisperX starts can be early too, so confirm leaks on the envelope.

## 2026-09-28 · music drop-outs, charlie-best-youtuber

- **The music drops out wherever the creator punches in** ("when it gets zoomed in the music also gets pulled out… it
  feels like this is an important part"). Their punch-ins are static Scale 127 on V1. Sequence 12: 37 punch-ins →
  34 drops (adjacent ones merged), 58.8 s of music removed, every edge within 0.3 ms of the punch-in's.
  → PLAYBOOK § Per step, Music row (becomes a README look rule if it repeats on the next video).
- **Razoring through QE is clean**: `qe.project.getActiveSequence().getAudioTrackAt(n).razor(tc)` at the SEQUENCE
  fps (Sequence 12 = 60) splits the clip, and the right-hand piece keeps its level and the right source offset. Lift the
  piece with `trackItem.remove(false,false)`. Hard cuts only; fades are offered, not assumed.

## 2026-10-04 · the creator ports the Game Informer style (Affan Afterhours) to this channel

- **"We're picking up this editing style from my other channel for our next video"** (YouTube `EsnIehnZUhs`). It was
  our own job `gta6-hurricanes`, so the spec came from two sources that agree: the live ABW8 · Sequence 16 (read-only;
  identical to the published master but for one pop) and the master `Weather GTA.mov` through the five style tools.
  → `STYLE.md` (self-contained copy, numbers), README § 1 rewritten, § 1a partly superseded, PLAYBOOK rows 4–7.
- **YouTube blocks yt-dlp here without cookies** ("Sign in to confirm you're not a bot"). The creator's OWN video is
  already on disk: check `E:\Shorts\Abudance Wisdom Shorts Exports\Final Renders\` (match on duration; oEmbed gives the
  title without signing in) before reaching for a download. Their Chrome is the fallback they named.
- **The timeline beats the measurement on zooms and speed.** `style-report.py` saw 11 zoom steps and 4 "slowed
  stretches"; the timeline holds 22 cut zooms (14 inside nests) and every clip at 100 %. Read the live project when it
  exists; the tools are for exports without one. (`slowmo-scan.py` also crashed on a cp1252 console: fixed in place.)
- **Cut zooms sort into two families by what they land on**: emphasis 103–135 % on the claim, the punch 139–203 %
  re-centred on the joke and the self-roast. → STYLE § 2.
- **The drop-out tool had to learn nests**: in this style 14 of 22 cut zooms sit inside nests and every face run has
  a keyframed push, which a V1-only `getValue()` scan would miss or misread. → `lanes/premiere/music-dropouts.py`
  (static scale > 100 on V1 + inside nests, pushes excluded), proven read-only: exactly the 22 reference ranges on
  Sequence 16, 35 punch-ins on Sequence 12, all already silent.
- **Correction:** the Volume Level 0.1778 on every clip is **0 dB** in the DOM's encoding (v = 10^((dB−15)/20)), not
  −15 dB as job 2's notes said. Levels were never changed; only the label was wrong.

## 2026-10-04 · job 3, kick-fake-viewers (CA-003, ABW8 · Sequence 27): rough cut + assets from the script

- **The creator's joint spec is now the channel's: ~2 frames of silence out, ~1 in** (`POLISH_TAIL_MS=33
  POLISH_LEAD_MS=17`). At that tightness every edge matters: the mechanical review found 7 clipped words (a missing
  "thirty", "four thousand" without "four hundred channels", the 'f' of "For"/"First", the 's' of "views"), 9 mouth clicks
  followed by dead air at INs, and 6 fragments of killed words riding on edges. → PLAYBOOK § 2; keep the exhaustive
  exact-span review on every job at this tightness.
- **Split on the envelope, not on transcript gaps.** Splitting at every WhisperX gap ≥ 0.40 s cut a phrase in two
  ("He didn't say I | buy bots", a 15 ms overlap that aborted splice) and dropped speech WhisperX never placed
  ("masters | like"). `quiet_run()` in the job's build-cuts.py: split only where the audio is quiet ≥ 0.40 s.
- **The per-burst pass earns its keep on this channel too:** 6 hidden retakes ("dropped dropped", a second "and to be
  clear", "Bots can / Bots can", "Kick / Kick's", "or not or", "you guys" misplaced by 2 s). → PLAYBOOK § 2.
- **The creator films the script out of order and with life in between**: a phone call mid-take, a pickup line said
  30 s late ("Bots can be sent to you by anyone" → moved back to its script place), no cold open / close in the take.
  Read the whole raw before authoring; say what is missing.
- **Script → assets is a repeatable step** (PLAYBOOK § Assets). What worked: their Chrome to find + verify (signed in to
  X, so X search with date filters finds the clips the research cites); yt-dlp for X (no login) and YouTube via the
  `mweb` client (360p only); headless 2x page captures, or a 1.7x-zoomed full-size capture in their Chrome when bot-
  blocked. What failed: Reddit (blocked), X search for 2023 posts (empty), ppc.land (ad gate), Chrome tabs freezing on
  `scrollIntoView` after a CSS zoom (open a fresh tab), screenshots saved at the PREVIEW scale (never pass `scale` with
  `save_to_disk`), a CDN ".png" that was a JPEG (Premiere's File Import Failure modal blocked the bridge).
- **Transcribe every quoted clip before placing it**: the Adin clip held the quote at 6–12 s, a slur at 23.6 s, and
  offensive chat on screen; the script's second Adin quote was not in it at all. → `assets/SOURCES.md` columns.
- **A "let it play" clip gets its own gap**: replayed with a 16.9 s hole after "Listen to exactly what he says.", the
  clip on V2/A2 (never A1: audio-polish processes every A1 clip). `review/tools/replay-gap.py`.

## 2026-10-13 · the channel moves to the IGN-missions style (STYLE.md v2) — Sequence 27 restyled

- **"Replicate that style exactly for the AffanWiz channel"** (Afterhours video 22, 8:17). It was our own job
  (`gta6-ign-missions`, Sequence 39), so the spec came off the creator's FINAL timeline (read live, read-only) + the
  published master through the style tools + every graphic sampled entering/settled/leaving → `STYLE.md` v2, the v1 Game
  Informer port kept as `STYLE-v1-game-informer.md`. What changed vs v1: **graphics = full-frame "IGN dossier" plates +
  alpha overlays** (blurred footage plate, warm-white Inter type, pink underline that draws, refined UI diagrams), not inset
  cards over gradient mattes; b-roll insets sit over their OWN blur; **premium SFX** (soft whoosh, pen line, glassy ticks,
  chimes) instead of pops; **no face push** (no nests), cut zooms median 135 %; music beds on their own track, out under
  every zoom.
- **Reuse the reference job's tools, re-anchored**: build-plan (word-anchored beats, edges on V1 cuts, neighbours butt),
  build-comps (same HEAD/helpers at 60 fps), build-plates, place-gfx, place-sfx, place-music, face-pass, active-window —
  copied into `projects/kick-fake-viewers/` and pointed at Sequence 27 (60.00 fps, not 59.94). Gotchas found adapting:
  the face planner snapped to clip STARTS only, so a zoom ran 3 frames into the Adin gap (snap to ends too); a section of
  advice outran a 160 s song (add a turn, the bed resumes in sync).
- **This script is proof-heavy**: 24 graphics at 3.7/min, face 53 % (reference 62 %); the first 30 s was all graphics
  until three short beats were handed back to the face (longest face-less run 12 s).
- **The "my theory" graphics name nobody and show no recognisable streamer** (the phone's feed is a blurred Kick Browse
  thumbnail): the theory must not read as an accusation.
- **The legal list goes on screen when the take misses it**: the reported-drops meter says "reported" (he never says it).
- **A plate is blurred, not anonymous: check every plate for readable text.** At σ≈26 and ×0.38, big type still reads: the
  N3on-chapter plate under the dot room (KM@15, his channel page) carried a legible business email. Change → g03 re-sourced
  to KM@140 (N3on on camera), placed as `g03-plate-v2.mp4`; the check = a contact sheet of `compositions/_bg/*.jpg` before
  placing. → `projects/kick-fake-viewers/build-plan.py`.

## 2026-10-22 · CA-007 "I Ranked Every Streamer's Content Machine" (ABW10 › "CA-007 Streamer Tier List") — STYLE v2, + the first "1 % better" pass
- **A spine graphic carries a list video**: the TIER BOARD (S/A/B/C/F, the thumbnail's layout) appears at every verdict as
  a compact SIDE board on the face (right third, x 1450–1850, dark glass card), the newest entry dropping in, and fills the
  whole frame once for the spoken recap. → `projects/streamer-content-machines/hf-graphics/gfx/build-comps-B.py`.
- **Side cards keep the face on screen while information lands** (chapter tags top-left for the five archetypes, the
  census / Expedia / clipper-math / recipe cards on the right): a proof-dense script got 25 full-frame graphics (3.5/min)
  + 17 side overlays, face 50 % (the script's density; the reference was 62 %, CA-003 53 %). The no-stray-frame gate skips
  side overlays (they never cut the face). → `build-plan.py` (region 'side'), `review/gate-frames.py`.
- **A fresh, wide SFX set per job** (the 2026-10-21 variety note): 53 Epidemic files in 12 classes, every one ≤ 20 dB tonal
  prominence, takes rotated in time order (none twice in a row) → 157 cues over 42 distinct files. Real bells/chimes all
  fail the prominence rule (21–86 dB): the "chime" class is soft timpani. → `sfx/LIBRARY.md`, `build-plan.py` § SFX.
- **The take, not the script, sets the numbers**: on-screen numbers follow his words; live pages had moved (xQc TikTok 48 vs
  his 47, Adin 5.8M vs 6M, Speed's best Short 30M vs 28M), so captures are cropped/dimmed where their own number competes.
- **WhisperX merges repeated lines on a heavy-retake take**: rebuild the words per energy burst (faster-whisper per burst,
  wav2vec2-aligned per burst, numerals keep faster-whisper) and measure every cut edge on the envelope; a spectral check
  catches clipped fricatives ("five" played as "ive"). → `projects/streamer-content-machines/review/tools/`, `transcript/build-cuts.py`.
- **ABW10's 59.94 sequences display DROP-FRAME**: QE razors need DF timecode (lab-notes 2026-10-22).

## 2026-10-23 · CA-007 review (Tella walkthrough) — four must-fixes ("otherwise I literally cannot upload this")
- **Lips out of sync at 1:24, 1:56, 2:50, 3:22, 3:49, 4:59, 5:50** → my 2026-10-22 stray-razor "heal" (`.end =`) SLIPPED 50 V1
  pieces (−3 … −240 frames); no gate compared V1 with A1. Change → V1 rebuilt from HIS A1 with a video-only subclip, zoom edges
  pre-split (no QE razor), `work/sync_audit.py` = 0 off; the audit is now a gate after every V1 write (PLAYBOOK + lab-notes).
- **"Whenever I'm looking down reading off the phone … cover the whole thing"** → head-pitch measurement (`review/tools/look_down.py`),
  covers on every ≥ 60 % reading clip (37 → 0 s visible), the archetype titles full-frame, side cards that sat on reading lines
  made full-frame. Face share falls to ~34 % (his ask). → PLAYBOOK rule.
- **"SFX very cheap … recycling one sound effect … I need variety, crisp, expensive"** (v1 had 42 files, but 44 near-identical
  ticks/thuds dominated) → a new premium set (`sfx2/`, 77 takes in 16 classes), 157 → 110 cues (a pen per underline and a click
  per list row were the tick-fest: `THIN` in `build-plan.py`), no take more than 3 times or twice within 60 s, and a class that
  runs dry BORROWS a sibling class's take (`FALLBACK`) instead of repeating: 69 different files. → PLAYBOOK rule.
- **Head-pitch 40–60 % ≠ reading**: the 12 such clips on CA-007 were all camera-facing looks/gestures; real reading = head
  tipped fully down (compare against a ≥ 60 % frame, `review/frames/ref-reading.jpg`). Eyeball them; don't cover by number.
- **"A clean animation each minute prompting them to join the Skool community"** → CTA side cards + a full plug card. → PLAYBOOK
  (the channel's CTA exception). Once the reading covers took the face away, 3:00–5:00 had NO face window: that minute's CTA rides
  INSIDE a full-frame comp as a chip (same template, scaled .85, top-left above the comp's own rows), never skipped; a fourth CTA
  inside 70 s at the end was retired instead. Every CTA line is his words (his ask + the plug in the take), none invented.
- He cut two lines himself ("$40 per 100,000"; "CaseOh is also"): his A1 became the EDL (`work/edl_from_a1.py`); his hand wins.
