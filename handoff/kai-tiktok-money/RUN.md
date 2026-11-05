# RUN: kai-tiktok-money (AffanWiz CA-011 "Kai Cenat Accidentally Showed His TikTok Money")

## ▶ STATUS: resume here (2026-11-05 22:50)
Transcribing on CPU (`transcript/words.json` is the output; the GPU run starved behind Topaz and two other sessions' WhisperX, see Flags). Next: read the transcript, measure reading, author the cut, send `review/SEQUENCING.md`, wait for his OK. **Nothing on ABW10 until he says yes.**

| | | |
|---|---|---|
| channel | **AffanWiz**, CA-011 | identified by transcript + script match; `presets/youtube/affanwiz/` |
| format | long-form YouTube 16:9 | probed: 1920x1080 h264, 60000/1001, 637.64 s (10:37), pcm_s16be 48k stereo, streams start 0.000 |
| lane | Premiere 2025, live ABW10.prproj | new bin + new sequence "CA-011 Kai TikTok Money"; he exports himself, never exportAsMediaDirect |
| shared Premiere | ABW10 is shared | by-NAME writes; QE only inside `lanes/premiere/ACTIVE-WINDOW.lock`; previous active sequence restored; message other sessions before the one save |
| preset | `presets/youtube/affanwiz/STYLE.md` v2 | PLAYBOOK standing rules 1–4 |
| lane gaps | none | Premiere column: no ⚠/⛔ (7 ✋, 8 ✋ the creator), same as CA-010 |
| source | `raw/C1449.MP4` = byte copy of `X:\Recordings\Afterhours\C1449.MP4` | `cmp` identical; 4 899 480 176 B |
| constraints | keep improvised bits; kill only retakes, stumbles, filler, dead air · ≥ 5 % better than CA-010 (BRIEF) · he exports · CA-010 TOOLS copied as code only · work in silence · LEAN: no subagents without his OK, Sonnet for builders/reviewers, never Fable · no C-drive exports · on-screen numbers = his words | |
| started | 2026-11-05 22:24 | |

## Steps
| # | Step | Status | What it produced / why not |
|---|------|--------|----------------------------|
| 1 | Intake | done | `raw/C1449.MP4`, `brief/` script + refs |
| 2 | Rough cut | running | transcribe on CPU |
| 3 | Audio polish | — | |
| 4 | Color grade | skip (planned) | STYLE § 1: no grade on this channel |
| 5 | Graphics | — | |
| 6 | SFX | — | |
| — | Music | planned | his beds out under every zoom (STYLE § 4), open ~10 dB over the body bed (LESSONS) |
| 7 | Review | — | |
| 8 | Export | his | he exports himself |

## Request coverage
- "1 % better": BRIEF § better. Evidence on the timeline: pending.
- "Steal something from other channels": BRIEF § stolen move (Coffeezilla tilted map → the Money Map; Johnny Harris chart zoom). Proof frame: pending.
- "Overlays wherever I look at the screen": measured by pose (`transcript/pose-raw.json`, `review/pose-bins.jpg`). Coverage number on the placed timeline: pending.
- Sequencing OK before the timeline: pending.

## Flags to report
- **"Swimwear" read as "screen".**
- **His original's read-only flag was cleared for ~15 min and restored.** My intake used a hard link for the first transcribe and a later `chmod u+w` on it hit the shared file. The contents never changed (`cmp` identical, mtime 22:16), `IsReadOnly` is back to True.
- A stray python (PID 46044, the stopped GPU WhisperX, parent shell gone) may still be alive and holds `projects/_c1449-intake/transcribe.log`, so that empty folder can't be removed yet. Auto mode refused the Stop-Process. Remove `_c1449-intake` when it exits.
