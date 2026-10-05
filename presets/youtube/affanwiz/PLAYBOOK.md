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
| 2 Rough cut | **TIGHT joints (creator, 2026-10-04): ~2 frames of silence after a block's last word, ~1 frame before the next block's first** → run polish with `POLISH_TAIL_MS=33 POLISH_LEAD_MS=17`, and split kept ranges wherever the ENVELOPE is quiet ≥ 0.40 s (a WhisperX gap alone is not silence: it hid speech in 'masters / Like'). **Keep improvised bits natural** (asides, jokes, the advice section); kill only retakes, stumbles and dead air, never to match the script. **Run a per-burst transcription of the whole raw first** (`projects/kick-fake-viewers/review/tools/bursts.py`): it found 6 retakes WhisperX had merged. House rules (`rough-cut`) + two channel checks after polish: (1) every IN after a pause gets an envelope check for a clipped first syllable (WhisperX starts run late here); (2) a LEAK SWEEP: no killed raw word may overlap a kept clip by > 60 ms (LESSONS 2026-09-28). Then the replay goes ONTO the handover sequence. |
| Assets (from the script) | The creator's script + research live in `X:\Claude Projects\Personal Brand English - Skool Community\creator-shorts\CA-NNN-*-SCRIPT.md / -RESEARCH.md` (copy both into the job's `brief/`). **Gather every "Screen:" item and every source the research names** (creator, 2026-10-04: "use Claude in Chrome to get those… put it inside of the sequence"): find + verify in their Chrome (they are signed in to X; Reddit is blocked); videos with yt-dlp (X needs no login; YouTube only via `--extractor-args youtube:player_client=mweb`, which caps at 360p); article stills via `workflows/page-record.mjs --scale 2`, or a full-size capture from their Chrome at 1.6–1.8x page zoom when the site bot-blocks headless; check every file's real type (a CDN ".png" was a JPEG and Premiere refused it behind a File Import Failure modal). Transcribe every clip that is quoted and note its usable span + flags (slurs, chat text) in `assets/SOURCES.md`. Import into bin `PBE Video NEON / CA-NNN assets`; lay them RAW on V2 under the words they illustrate; a clip the script says to "let play" gets a gap in V1/A1 and sits on V2/A2. Tools: `projects/kick-fake-viewers/review/tools/` (import-assets, replay-gap, place-assets). |
| 3 Audio | the voice is already Enhance-Speech'd by the creator; apply the measured gain + −6 dBFS limiter as usual |
| Creator's hand pass | after the rough cut the creator does their own face cut, nests, cut zooms and nested zooms, and drops the overlays onto V1. **Never touch the nests.** |
| 5 Overlays | **README § 1a (locked).** Order: FCP XML backup of the sequence → `inventory` (every V1 clip: source size, scale, effects) → plan (standard 1700×972 box, tiny ones 960 px wide, enhance if > 1.1×) → Higgsfield (max 4 concurrent jobs; the upscaler fails past ~2:1, so pad wide strips to 16:9 with their own edge colour and crop back; ~200 px crops go to `gpt_image_2_5` with the exact text) → QA every result side by side with its original (invented text = reject) → `build-overlays.py` (Lanczos to size, shadow baked, 1920×1080 canvas) → `place-overlays.py import / place / fx / verify` in chunks of 6 slots → one-frame Premiere render of a few slots as proof. |
| Music | the creator lays the music bed on A2 themselves (STYLE § 4: one Epidemic bed per section, a gap before each new song, ~12.5 dB under the voice). **The music DROPS OUT under every cut zoom / punch-in** (a STATIC Scale > 100 on V1 or inside a nest; a keyframed push never counts; the creator used 127 on job 2): razor A2 at the punch-in's edges, lift the piece under it, hard cuts, the surviving pieces keep their level and play on from where they were. Adjacent punch-ins merge into one drop. Order: `save_project` + prproj copy + an A2 JSON record (the undo) → one test range → all → read back 0 music under any punch-in, V1/A1 identical, levels unchanged. Tool: **`uv run lanes/premiere/music-dropouts.py "<sequence>"`** (plan, read-only) → `--apply --backup projects/<job>/premiere-backup` (does the backup, the razor, the read-back and puts the active sequence back; nest-aware, proven 2026-10-04 on Sequences 12 and 16). |
| 4 Grade | **none** (STYLE § 1). |
| 5 Overlays, the STYLE way (from 2026-10-04) | **STYLE § 3 replaces the § 1a frame.** Slots come from the creator either way: overlays they dropped on V1 (job 1), or face clips dragged UP TO V2 + a Tella walkthrough (the reference video's convention; ingest per `feedback-walkthrough-videos`). Tracks: V1 face · V2 the creator's slot blocks (left untouched) · **V3 one matte per slot, varied palette** · **V4 the overlay**, ProRes 4444 alpha, 85 % filled inset, 22 px corners, baked shadow. Source footage 1080p H.264 into a bin named after the video's topic; preview every picked shot's whole span before rendering; quotes verified twice. Pattern: `projects/gta6-hurricanes/overlays/build.py` + `place.py`. |
| 5b Face motion | the creator's pass on jobs 1–2. If asked to do it: STYLE § 2 (push every run, cut zooms on the emphasis and the punch, music out under each) with `lanes/premiere/face-nests.py`, picks written to `transcript/face-zooms.json` so the creator can veto them by name. |
| 6 SFX | **a pop on every overlay entrance and internal switch**, A3, −6 dB clip, exits silent (STYLE § 4). Pattern: `projects/gta6-hurricanes/overlay-sfx.py` (reads the switch frames off the SLOTS render). |
| 7–8 | the creator's review, then export as the channel always has. |

## After every review

Read what changed (`premiere-bridge.mjs diff-edl`, `place-graphics.py --diff`, `place-sfx.py --diff`) plus what was
said, and append to `LESSONS.md` as *lesson → change → file*.
