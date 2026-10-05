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
