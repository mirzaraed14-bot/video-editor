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
5. The rough cut replays onto a **new** sequence in the creator's project. Their handover sequence is never touched.

## Per step

| Step | Channel rule |
|---|---|
| 2 Rough cut | house rules (`rough-cut`) until the creator's first hand pass teaches otherwise → LESSONS |
| 3 Audio | the voice is already Enhance-Speech'd by the creator; apply the measured gain + −6 dBFS limiter as usual |
| Creator's hand pass | after the rough cut the creator does their own face cut, nests, cut zooms and nested zooms, and drops the overlays onto V1. **Never touch the nests.** |
| 5 Overlays | **README § 1a (locked).** Order: FCP XML backup of the sequence → `inventory` (every V1 clip: source size, scale, effects) → plan (standard 1700×972 box, tiny ones 960 px wide, enhance if > 1.1×) → Higgsfield (max 4 concurrent jobs; the upscaler fails past ~2:1, so pad wide strips to 16:9 with their own edge colour and crop back; ~200 px crops go to `gpt_image_2_5` with the exact text) → QA every result side by side with its original (invented text = reject) → `build-overlays.py` (Lanczos to size, shadow baked, 1920×1080 canvas) → `place-overlays.py import / place / fx / verify` in chunks of 6 slots → one-frame Premiere render of a few slots as proof. |
| 4, 6–8 | _pending the creator's direction_ |

## After every review

Read what changed (`premiere-bridge.mjs diff-edl`, `place-graphics.py --diff`, `place-sfx.py --diff`) plus what was
said, and append to `LESSONS.md` as *lesson → change → file*.
