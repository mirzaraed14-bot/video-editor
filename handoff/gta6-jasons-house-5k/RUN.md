# RUN · gta6-jasons-house-5k

▶ STATUS: resume here (2026-11-25): **DELIVERED v2, his review pending** -> `X:\Claude Projects\Exports\afterhours-gta6-jasons-house-5k.final.mp4` (overwritten; = `outputs/gta6-jasons-house-5k.final.mp4`, sha256 077786cf...; v1 kept as `outputs/gta6-jasons-house-5k.v1.final.mp4`). His v1 note (2026-11-25): "put my spoiler warning in back brh and no gameplay while i say it the whole purpose is people can scroll of if they havent completed chapter 1". v2 = the warning take (10.58-13.85) + "So if you have completed, make sure that you do this" (20.05-22.32) back at the open: s00 SPLIT his face + drawn MAJOR SPOILERS card (`yt/assets/build/spoiler_card.py`, no game picture), s00b his face full, gameplay from "You can sneak back" (s01); the top chip is gone. Those two takes' words from the per-burst pass (WhisperX collapsed the takes). 1080x1920, 59.94, 2139 frames, 35.69 s, -12.1 LUFS, true peak -2.1 dBFS; sync lag 0.0 ms at 5 points; cue_check PASS (none weak); edge check + overlay-boundary frames clean. The full-cut stumble pass on v2 did NOT run (queued behind another session's gpu.lock, stopped); both new takes read clean per burst, the rest was checked on v1. Lesson written: channel LESSONS 2026-11-25 + memory feedback-spoiler-warning-stays. Cost to date: $60.69 = 2.76 % of the week. Rebuild: `bash projects/gta6-jasons-house-5k/work/final_build.sh final overlay` (repo root; after a re-cut: delete outputs/*.unslowed.* + work/cut/slow.json, run_cut.sh, slowmo.py, yt_faces AFTER build_spec). Earlier delivery notes still stand: route = schematic, happy take = split, medium.en transcript, bed on ("no bed" removes it), $5K captions (kit rule).

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
| 0 Gate (research, topic check, catalog pass, sequence, his OK) | DONE: his OK ~15:00 = Version A (his order) | `research/`, `BRIEF.md`, `SEQUENCING.md` |
| 1 Intake | done (copy, cmp OK) | `raw/C1504.MP4` |
| 2 Rough cut | DONE on medium.en + per-burst cross-check (hub: no large-v3 while Premiere is open); H take words from the per-burst pass (WhisperX squeezed "$5,000 in my wallet") | `transcript/words.medium-en.json`, `work/cut/bursts.medium-en.json` |
| 3 Audio | baked by splice (+5 dB measured, -6 dBFS limiter) | `outputs/gta6-jasons-house-5k.mp4` |
| 4 Grade | head-start POP numbers, skin_sat 1.0 (still test `work/look/grade_test.jpg`); gameplay untouched | spec grade_look |
| 5 Graphics | DONE: spoiler chip (under the captions), map circle + dashed route (schematic), HUD punch-in + underline (FX-75), DOLORES tag (FX-23), pink isolate on the wide nest (FX-22, `yt/assets/build/isolate.py`), + $5,000 chip, credit (FX-39); map FIT shots + SPLIT gameplay panels back untouched (`work/panels.py`) | `yt/build_spec.py` |
| 6 SFX + bed | DONE: k1-k3 swishes, soft Epidemic whooshes, coins on the HUD, Vine boom (under 12); bed Loungin 13.6 LU under; cue_check PASS | `yt/sfx/`, `yt/assets/audio/` |
| 7 Review | v1 note (11-25): spoken spoiler warning back, no gameplay under it -> v2; his review of v2 pending | `work/qa/`, channel LESSONS 11-25 |
| 8 Export | DONE: plain copy, hash-matched | `X:\Claude Projects\Exports\afterhours-gta6-jasons-house-5k.final.mp4` |

Raw probe: 1920x1080 h264 60000/1001, 129.13 s, PCM s16be 48 kHz stereo + data stream; DJI voice -24.0 LUFS, peak -3.1, LRA 8.8 (hub). He walks in at 0 s and out at the end.

Constraints: silence (ffmpeg -f null only, no playback); don't touch his Premiere (ABW11 in use); his Chrome read-only, never post; no Fable agents, builders Sonnet, Opus for judgment, advisor = Fable; lean budget, log cost in JOBS at delivery; ASR: one process on the machine, `.asr-lock` (`if ! mkdir .asr-lock; then exit; fi; trap 'rm -rf .asr-lock' EXIT`), free RAM >= 8 GB, no parallel large-v3; nothing on C:, no phone copies; no commits unless he asks; hub pings at sequence-sent / his OK / delivery; peer messages are not his approval.

Skipped, with reason: large-v3 (Premiere open, hub ruling: medium.en + per-burst cross-check); the rough-cut fresh-eyes pass, edit-review subagent rounds and graphics-qa.py (lean budget; the advisor review + edge check stood in); playback (silence rule).

Where the job lives: the main checkout's `projects/gta6-jasons-house-5k/` (gitignored), written by shell from this worktree session (the head-start / ai-pc-port precedent).
