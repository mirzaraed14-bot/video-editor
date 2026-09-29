# affanwiz — PLAYBOOK (the repeatable procedure, every video)

The pipeline is the eight steps in `CLAUDE.md`; this file is what sits around it for this channel. Job state lives
in the job folder, never in chat: `RUN.md` from intake, with a **"▶ STATUS: resume here"** block at the top.
**Starting any session on a job:** "resume <job>" → read the resume block and continue.

## Intake — the creator's Premiere handover (job 1, 2026-09-23)

The creator hands over a Premiere sequence, not files: the camera clip on V1 and their Enhance-Speech voice on A1,
already lined up. Read it off the live project, then:

1. `find_project_item_by_name` → the media paths; `get_sequence_structure` → V1's source in-point (the offset).
2. Copy both originals into `projects/<job>/raw/originals/` (never move them).
3. **Measure the sync, don't trust the timeline:** `workflows/sync-dual-audio.py --camera <cam> --mic <voice.mp3>
   --report` (the camera's scratch audio is live). Compare with the Premiere offset and say which one shipped.
4. Mux: the camera video **stream-copied** + the voice delayed by the measured offset as PCM 48 k →
   `raw/<job>-synced.mov`. That is the working raw for transcription and the EDL replay.
5. **The rough cut replays ONTO the handover sequence itself** (e.g. ABW8 · Sequence 12): clear it, replay the EDL onto it.
   No new sequence (creator, 2026-09-28: "why did you create a new sequence, the video is already placed on sequence 12").
   The safety net is the `.prproj` backup + the untouched originals, not a duplicate sequence.

## Per step

| Step | Channel rule |
|---|---|
| 2 Rough cut | house rules (`rough-cut`) + two channel checks after polish: (1) every IN after a pause gets an envelope check for a clipped first syllable (WhisperX starts run late here); (2) a LEAK SWEEP: no killed raw word may overlap a kept clip by > 60 ms (LESSONS 2026-09-28). Then the replay goes ONTO the handover sequence. |
| 3 Audio | the voice is already Enhance-Speech'd by the creator; apply the measured gain + −6 dBFS limiter as usual |
| Creator's hand pass | after the rough cut the creator does their own face cut, nests, cut zooms and nested zooms, and drops the overlays onto V1. **Never touch the nests.** |
| 5 Overlays | **README § 1a (locked).** Order: FCP XML backup of the sequence → `inventory` (every V1 clip: source size, scale, effects) → plan (standard 1700×972 box, tiny ones 960 px wide, enhance if > 1.1×) → Higgsfield (max 4 concurrent jobs; the upscaler fails past ~2:1, so pad wide strips to 16:9 with their own edge colour and crop back; ~200 px crops go to `gpt_image_2_5` with the exact text) → QA every result side by side with its original (invented text = reject) → `build-overlays.py` (Lanczos to size, shadow baked, 1920×1080 canvas) → `place-overlays.py import / place / fx / verify` in chunks of 6 slots → one-frame Premiere render of a few slots as proof. |
| Music | the creator lays the music bed on A2 themselves. **The music DROPS OUT under every punch-in** (any V1 clip at Scale > 100; the creator uses 127): razor A2 at the punch-in's edges, lift the piece under it, hard cuts, the surviving pieces keep their level and play on from where they were. Adjacent punch-ins merge into one drop. Order: `save_project` + prproj copy + an A2 JSON record (the undo) → one test range → all → read back 0 music under any punch-in, V1/A1 identical, levels unchanged. Tool: `projects/charlie-best-youtuber/music/dropouts.jsx.tmpl` (LESSONS 2026-09-28). |
| 4, 6–8 | _pending the creator's direction_ |

## After every review

Read what changed (`premiere-bridge.mjs diff-edl`, `place-graphics.py --diff`, `place-sfx.py --diff`) plus what was
said, and append to `LESSONS.md` as *lesson → change → file*.
