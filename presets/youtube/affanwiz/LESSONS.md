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
