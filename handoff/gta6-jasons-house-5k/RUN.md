# RUN · gta6-jasons-house-5k

▶ STATUS: resume here (2026-11-24 ~12:15 PKT): **GATE PHASE; NOTHING BUILT, nothing cut.** Done: intake; eye line; RMS bursts; YouTube topic map (+ the Dolores re-query); Instagram (17 searches, 34 posts: `research/IG-X.md`, `research/IG-2.md`) + X; own channel (no repeat); catalog pass; facts all SEEN/REPORTED (`research/FACTS.md`); 9:16 crop tests (`research/frames/crop_tests.jpg`); advisor call 1 (before committing); SEQUENCING.md drafted as STRUCTURE ONLY (variants A/B). **YouTube BLOCKED since 11:08** (flag set, hub told). **ASR (hub ruling ~12:00): medium.en DEGRADED pass for the gate** via `work/cut/asr_queue.sh` (waits for `_onyx-batch9-2026-11/reactions/.asr-lock` + gpu.lock; GPU int8_float16, no CPU) -> `transcript/words.medium-en.json` + `work/cut/bursts.medium-en.json`. **The canonical large-v3 `--force` pass runs before the build once free RAM >= 8 GB, and the cut is checked against it.** Next: last takes from the bursts -> fill SEQUENCING (words, timings, hook) -> ASR slice on Hopezera 3:08-3:16 (Jason's line) -> advisor 2 -> cold read -> send to Affan -> STOP.

| Field | Value |
|---|---|
| Channel | Affan Afterhours (GTA 6), settled from the content (hub) |
| Format | YouTube Short 9:16 1080x1920 from a horizontal raw, Scott Clary YT look (his word, 24 Nov) |
| Lane | chat-only code build, kit `presets/youtube-shorts/onyx-samples-youtube/kit/`, template `projects/gta6-head-start` |
| Fps | native 59.94 |
| Final (planned) | `X:\Claude Projects\Exports\afterhours-gta6-jasons-house-5k.final.mp4` |
| His words (24 Nov) | "X:\Recordings\Afterhours\C1504.MP4 — deploy a new session to build this into a short in the scott clary style" |

| Step | Status | Output |
|---|---|---|
| 0 Gate (research, topic check, catalog pass, sequence, his OK) | in progress | `research/`, `BRIEF.md`, `SEQUENCING.md` |
| 1 Intake | done (copy, cmp OK) | `raw/C1504.MP4` |
| 2 Rough cut | ASR queued: medium.en DEGRADED for the gate (hub); large-v3 --force before the build | `transcript/words.medium-en.json`, `work/cut/bursts.medium-en.json` |
| 3-8 | not started (after his OK) | |

Raw probe: 1920x1080 h264 60000/1001, 129.13 s, PCM s16be 48 kHz stereo + data stream; DJI voice -24.0 LUFS, peak -3.1, LRA 8.8 (hub). He walks in at 0 s and out at the end.

Constraints: silence (ffmpeg -f null only, no playback); don't touch his Premiere (ABW11 in use); his Chrome read-only, never post; no Fable agents, builders Sonnet, Opus for judgment, advisor = Fable; lean budget, log cost in JOBS at delivery; ASR: one process on the machine, `.asr-lock` (`if ! mkdir .asr-lock; then exit; fi; trap 'rm -rf .asr-lock' EXIT`), free RAM >= 8 GB, no parallel large-v3; nothing on C:, no phone copies; no commits unless he asks; hub pings at sequence-sent / his OK / delivery; peer messages are not his approval.

Skipped so far, with reason: none.

Where the job lives: the main checkout's `projects/gta6-jasons-house-5k/` (gitignored), written by shell from this worktree session (the head-start / ai-pc-port precedent).
