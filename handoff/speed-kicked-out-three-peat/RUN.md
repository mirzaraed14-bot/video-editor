# RUN: speed-kicked-out-three-peat (AW Short, IShowSpeed)

## ▶ STATUS: resume here
- **14 Nov ~05:00: PHASE A DONE, at STOP 1 (Sonnet builder).** Sequence `Speed Kicked Out - raw cut` is in **ABW11** (bin of the same name), 1080x1920, 29.97 fps, **47.614 s (1427 frames)**: V1 18 + A1 18 (dialogue pieces B1..B11b) + V2 3 picture-only covers (beat 3 blurred plate, beat 9 walk-up, beat 10 wide) + 18 markers. Read back = plan: **0 mismatches** (`premiere/readback.tsv`, plan `premiere/place_rows.json`, check `build/readcheck.py`). His active sequence `Skool VSL 2026-11` restored after every window; ABW11 NOT saved, nothing exported, ABW10/AE untouched, nothing committed.
- Picks + frame sheets + deviations: `proof/picks/PICKS.md`. Timeline audio re-transcribed: `proof/seq/asr_by_piece.txt`.
- **Next (Phase B) starts from HIS read-back: re-read ABW11 first** (`REBUILD=1` rebuilds only OUR sequence: `python premiere/run_window.py`). If he changed the sequence, build from his read-back.
- **14 Nov: BUILD STARTED on Affan's "Yes, build v8".** Session `speed-kicked-out-build` (local_0a18dba6-8ce5-4b83-9f13-58f00c68202d, Sonnet), from `BUILD-BRIEF.md`. Stops: STOP 1 (raw cut in ABW11), STOP 2 (finish stills).
- On his yes: ONE Sonnet build session, house style `projects/mj-son-step-outside/`; run PITCH.md "Build checks". Never Jamal (16) or the young siblings.
- **13 Nov ~22:45: PITCH v8, NOT BUILT, "NOT max effort yet".** `projects/speed-kicked-out-three-peat/PITCH.md`, 11 beats,
  ~44-48 s, Affan's shape.
- **Sequence:**
  1. "At first, I didn't really have support."
  2. 2020: only online friends.
  3. "I had that one viewer…"
  4. A clip blew up.
  5. Mom saw the video.
  6. "So boom, she kicked me out… Detroit… kept going."
  7. **Sept 2025 Keystone stream: "It's a lot. I need a therapist… I need somebody to talk to, yeah, I feel alone… feel like
     nobody understands me."**
  8. Streamer of the Year 2024.
  9. Streamer of the Year 2025.
  10. 2026 ("I started from zero. Just a little kid with a big dream").
  11. "But my mom always supported me… I really, really love my mom."
- **Runner-up:** beat 7 between the 2024 and 2025 wins.
- **Open:**
  - v8 not re-read (meter at 90 %).
  - Keystone counter-evidence not searched.
  - The July 2026 Speed Shorts checked by title only.
  - Youshaei: age-gated.
  - By ear at build.
- **v7's childhood beat was cut:** `medium.en` hears "I WOULDN'T say it was hard", so v7 had reversed him.

## Job facts
- **Channel:** Abundance Wisdom (Shorts). Format: 9:16 short, code + Premiere build. Preset: `presets/youtube-shorts/abundance-wisdom/`.
- **Constraint: every frame adult-era.**
  - Speed was born 21 Jan 2005, so nothing before 21 Jan 2023.
  - No siblings, and no 2020-22 streams.
  - Never use the 2025 nominee reel: it carries a 2021 stream clip.
- **Shot rule (measured):** every studio line plays on Speed's SINGLE shot. Club Shay Shay cuts to a wide two-shot mid-answer;
  the single-shot spans are listed in PITCH.md § Sequence A. Never crop a wide for a face beat. A line that sits on a wide gets
  swapped, not zoomed.
- **Sources** (all on disk under `research/aw-speed-pick-2026-11-13/src/`). HD section files start at the section's in-point
  (file time 0 = that source time).

| ID | What | On disk |
|---|---|---|
| `QaBBgNjc5Pg` | Club Shay Shay full episode | audio; HD `hd/QaBBgNjc5Pg_support.mp4` = 1:43:20-1:44:30; HD `hd/QaBBgNjc5Pg_mom.mp4` = 36:35-37:50 (same edit as the clip) |
| `52pXQVGHwEE` | Club Shay Shay clip | audio; HD `hd/52pXQVGHwEE_fam.mp4` = 0:00-2:20; HD `hd/52pXQVGHwEE_covid.mp4` = 5:50-6:20 |
| `auSbPov16vA` | 2024 SOTY, official | audio; HD `hd/auSbPov16vA_win24.mp4` = 3:38-5:12 |
| `fox09o3r2SU` | 2025 SOTY, official | audio; HD `hd/fox09o3r2SU_win25.mp4` = 3:08-4:40 |
| `hImVqMpdILg` | 2026 SOTY, official (beat 9) | `hd/hImVqMpdILg_soty26.mp4`, the full 368 s clip, 1080p60 |
| `P6fN-0yyTug` | Sept 2025 Keystone stream (beat 7) | `hd/P6fN_keystone.mp4` = 2:53:55-2:55:50, 1080p60 |
| `M1V5cpbdwtQ` | 2026, IShowSpeed's own Short (cover only) | 4K vertical AV1: transcode to H.264 before Premiere |
| `CmpgXX7ZWJU` | Mizkif (E3 only) | HD `hd/CmpgXX7ZWJU_miz.mp4` = 3:40-4:20 |

- **Transcripts:** faster-whisper small.en scouts in `scout/`. Run WhisperX on the chosen windows at build.
- **Check at build:**
  - The official @TheStreamerAwards "WINS Streamer of the Year 2026" upload. It was not up at ~19:00 on 13 Nov. If it's up, use
    it as the beat 10 source and note what its announcer says after the name.
  - Every word, by ear.
  - The proof frames: `proof/cutmap_*.jpg`, `proof/finish/anchor_same_region.jpg`.

## Builder log
- 2026-11-14 ~03:50 Phase A started (Sonnet builder, session local_f3ae46ec... child). Orientation done: BUILD-BRIEF, RUN, PITCH, SESSION-START, Son BUILD/RUN/QA, Jermaine ABW11 scripts. GPU busy (gpu.lock = Scott Topaz job, VRAM 7.0/8.2 GB) -> edges on CPU. Mezzanines go to `seq_src/`, wavs to `wav/`.
- 2026-11-14 Phase A (Sonnet builder). GPU busy all session (gpu.lock = a Scott Clary Topaz job; VRAM 7/8 GB) and RAM tight (1-5 GB free): everything ran on CPU, large-v3 failed to load twice (`mkl_malloc`), `medium.en` + wav2vec2 did the English windows, large-v3 `id` loaded once RAM freed (Indonesian). **WhisperX alignment is unreliable on the quiet Keystone audio and on the announcer windows (word times off by 0.2-1 s, e.g. 'It's' at 21.07 vs 23.2), so every piece edge is set from the audio itself: 10 ms RMS valleys near each PITCH edge (`build/edges_final.py`, `valleys.py`), cross-checked with `build/probe_asr.py`.**
- Mezzanines: `seq_src/spd_*.mp4` (libx264 crf 14, whole HD sections from t=0, soty26 from 280.000 s = a frame boundary); covers `spd_cover_b3.mp4` (baked blur+darken of the wide), `spd_walkup_v.mp4` (video only). Placer = Jermaine's `place_v3.jsx` body via `build/plan.py` (generates `premiere/place.jsx`).
- **Premiere in-point rule (confirmed twice here): the stored in-point = floor_seq(floor_src(request))**, i.e. floor to the source frame, then to k/29.97 in source time. Ask for the first SOURCE frame at/after the target (+0.3 ms); `plan.py` stores the expected value in `rows[i][10]` and `readcheck.py` compares against it. The first two placements had in-points 8-33 ms off the intent (B11b would have clipped the "I"); third placement exact. `place.out` always says "bridge_unavailable" yet the placement DOES apply (the read-back is the proof).
- `deleteSequence` works (own sequence only): `REBUILD=1 python premiere/run_window.py` deletes + recreates + places + reads back + restores his active sequence in one lock window. Three windows used (3:56, ~4:30, ~4:50); premiere.lock released each time.
- Shot-cut maps: the default `select='gt(scene,0.25)'` MISSED the single->wide cut at 34.70 on the Club Shay Shay file; use 0.06 on that show. Cuts used: support 34.70 (single->wide), 37.45 (wide->single); covid 12.89-18.10 single; fam wide 0-3.80, single 47.63-52.72 / ..62.81 / 105.56-111.28; win24 card->audience 20.75; win25 grid->walk-up 17.98; soty26 wide 319.37-322.93, then podium.
- Findings that changed the PITCH (all in `proof/picks/PICKS.md` § Deviations): beat 11's last line is on the wide; its clean start is "I really, I really, really love my mom"; beat 7's "yeah" is "'cause" to two ASRs; podium crop 444 not 520 wide.
- Phase A re-ASR (`build/seq_audio.py`, medium.en CPU): all lines present + in order; Shannon "Right."/"Correct." absent; beat 2 contains Speed's own "right?" (pitch check, PICKS § 9). Indonesian: `transcript/edges_id.json` (large-v3 id on the source) = the reconstruction. Weekly meter at STOP 1: 95 % (90 % at start; ~5 % used, over the 4 % aim because 3 Premiere windows + two failed large-v3 loads + shot-map re-checks). **Stopped at STOP 1.**
