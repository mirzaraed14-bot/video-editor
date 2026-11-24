# RUN: bigfoot-is-in-gta-6 ("Bigfoot Is In GTA 6 😳"), Abundance Wisdom Short: RAW SEQUENCE in Affan's ABW11 (STOP 1 only)

## ▶ STATUS: resume here (STOP 1 REACHED, 20 Nov 2026 22:31-22:35 PKT; waiting for his review of the raw sequence)
- **The raw sequence is PLACED in his open ABW11 and READ BACK = PASS** (`premiere/READBACK.md`, `premiere/readback.tsv`, a second by-name readback is byte-identical). Sequence **"Bigfoot Is In GTA 6 - raw cut"**, id `c0cae39d-4e01-4000-b545-8d83b4228a2e`, in the new bin **"Bigfoot Is In GTA 6"** (7 mezzanine items + the sequence, 0 offline). 1080x1920, 60.000 fps, display format 108 (his "Sequence 02" cloned, no setSettings). **V1 7 clips / A1 7 clips, nothing on any other track, 7 markers (one per beat), end 32.1001 s** (1926 frames + the 0.1 ms pin nudge, as in the MJ precedent). Every V1 clip is butt-joined; each A1 span = its V1 span.
- **Window:** 22:31:23-22:31:44 (12 s of work), idle 306 s when it started, his active sequence "Sequence 01" (`c539a9fe-adf5-4803-82e6-33c0890ebbec`) restored by id: **his playhead ticks identical before / after (9906624000000)**, and again in the final read-only window (22:32:40, `premiere/final_check.py`). His "Sequence 02" 26 clips before and after; sequences 52 -> 53. **NOT saved** (no save call; the new sequence needs his Ctrl+S), **not exported**, nothing played, lock released (`premiere.lock` is gone; only `instagram.lock` / `youtube.BLOCKED` belong to others). All 7 `importFiles` calls returned true, one file per call, and the bridge kept answering throughout (no watcher was running, so a modal would not have been logged; none blocked the window). Tracks A1-A4 read back un-muted (the clone's state).
- **Pending / for the next session:** (1) his review of the raw cut, then the real build (`graphics-build` look: 16:9 inside the 9:16 over a blurred fill, cams as insets with names, hook card, captions, covers, SFX, 2 subscribe prompts, level matching: summit1g +15 dB, xQc +13 dB; the f-words bleeped or not = his Q2 in SEQUENCE-SPICY-v3). (2) Jack (jacksepticeye) swap-in is NOT built and NOT fetched, Affan downloads it himself if it is good enough. (3) Nothing is captioned, graded, blurred, zoomed, SFX'd or musicked.
- **Done earlier (no Premiere):** Kai's 1080p60 re-pull (30.05 s, `raw/kai-vod-1080-35955.mp4`, one Twitch pull, rc 0); the beat table (`premiere/beats.py`); 7 sequence-ready mezzanines in `raw/` (pre-import checks OK, A/V sync proven vs the source: lag 0.5 ms = the seek offset on all 7); source contact sheets (`proof/sheet_starts.jpg` = beat-start frames from the SOURCE files, `sheet_edges.jpg`, `sheet_mids.jpg`) and a 9:16 layout proof from the read-back Scale / Position (`proof/sheet_layout_916.jpg`).
- **Re-place rule:** never rebuild over this sequence: a re-place = a NEW sequence name (`... v2`) and new mezzanine names (never overwrite a file Premiere has imported). Resume the kit with `python -I premiere/run_window.py --check` (read-only, takes the lock), `--readback`, or `python -I premiere/final_check.py`.
- **Never:** save, export, move his playhead, touch his other sequences, close/restart Premiere, start our own `dialog-watch.py`.

## Flags (so far)
1. **`dialog-watch.py` is NOT running** (checked twice, 22:2x; the brief said it already runs). Per the rules we do not start our own. The only guard against an import-failure modal is the pre-import checks (every mezzanine: size stable 3 s, ffprobe, full `-f null` decode, magic bytes, ASCII name, one `importFiles` per file, none overwritten). The count INSIDE the lock was 0 at 22:31:25 (`premiere/run_window.log`).
2. **B3 (summit1g, 33.0-37.3) edges are UNMEASURED** (kept as the table says, no ASR re-measure). Measured on frames: the game picture fades to black at 35.5-35.7 s and is black to the out point (about 1.6 s of black, his cam still visible).
3. **B4 (Fanum, 26.0-31.5) starts on a near-black game frame:** the picture fades in 26.1-26.4 s (luma 2.5 -> 33), so about the first 0.3 s of the beat is black (the table said 22-25 s is black).
4. **B1 frame 1** still carries the tail of the game subtitle ("...thing?") and a burned-in stream caption (the hook card covers it at the build).
5. **B7 speaker:** the line "Nope. Skunk ape. Same genus, different species." is the game character (Kirk); xQc is silent in the inset. SEQUENCE § 2 has no xQc cover list: nothing (chat, counters, donation alert) is on the xQc frames at start / mid / end. **The B7 marker's COVER text is the generic "chat, counters, any donation alert (re-check on frames at the build)", written before the frames were seen; the frames show none.** Not worth another Premiere write; the real build reads this note.
6. **Levels (clip gain left at 0 dB):** summit1g about -29.6 LUFS (+15 dB at the build), xQc about -28 LUFS (+13 dB).
7. **Kai pull path differs from the brief's command:** it was written to `projects/bigfoot-is-in-gta-6/raw/kai-vod-1080-35955.mp4` (not `research/.../media/kai-vod/`), to keep to "write only in the job folder". The 1080p file = the 720p section minus **25.000 s** exactly (frame-matched on beat 5 AND beat 6, audio lag 0 ms on both): beat 5 = in-file 6.2-10.9, beat 6 = 20.4-23.4. Both beats now use the 1080p60 file, not the 720p fallback.
8. No minors on the start, mid and end frame of each of the 7 beats (all adults: streamers + game characters); not every frame was inspected. Kai's 60 s clip has an adult-sized person behind him at about 23-27 s (age unconfirmed), outside B2's window (54.5-58.5) and B5/B6.
9. **`proof/sheet_layout_916.jpg` is computed from the read-back Scale / Position (source frames placed on a black 1080x1920), NOT a Premiere frame:** the fit-to-width look was never seen in Premiere (no playback, `premiere-bridge frame` is unreliable per lab-notes). Scale read back 56.25 (1920-wide sources) and 42.19 (B3, 2560 wide), Position 0.5 / 0.5.
10. **Tool bug for the hub (lab-notes):** after a scripted `.end` pin Premiere's clip `outPoint` reads back STALE (in-point + 0.2 here); the source out has to be `inPoint + (end - start)` (already in lab-notes 2026-10-20; `verify_readback.py` does it).

## What is placed (READ BACK = PASS, see `premiere/READBACK.md`; the table is the plan, every number matched within 2 ms)
| beat | timeline | who | source file | src in-out (s) | caption (marker) |
|---|---|---|---|---|---|
| B1 HOOK | 0.000-3.000 | Fanum | `ondisk/fanum-bigfoot.mp4` | 4.55-7.55 | WHAT THE F*CK AM I LOOKING AT? |
| B2 | 3.000-7.000 | Kai Cenat | `ondisk/kai-bigfoothunting-4096145023.mp4` | 54.5-58.5 | OH MY GOSH BRO |
| B3 | 7.000-11.300 | summit1g | `ondisk/summit-bigfootjumpscare.mp4` (2560x1440) | 33.0-37.3 | WHAT THE F*CK IS HAPPENING? |
| B4 PEAK | 11.300-16.800 | Fanum | `ondisk/fanum-bigfoot.mp4` | 26.0-31.5 | Bro... / WHAT IS THAT?! |
| B5 | 16.800-21.500 | Kai Cenat | `raw/kai-vod-1080-35955.mp4` | 6.2-10.9 (720p sec. 31.2-35.9) | OH HELL NAH (x2) |
| B6 | 21.500-24.500 | Kai Cenat | `raw/kai-vod-1080-35955.mp4` | 20.4-23.4 (720p sec. 45.4-48.4) | OH HELL NAH |
| B7 BUTTON | 24.500-32.100 | game line over xQc inset | `ondisk/xqc-kirk-0940-1060.mp4` | 93.0-100.6 | Nope. Skunk ape. Same genus, different species. |

Total 32.100 s = 1926 frames at 60 fps. Every beat = one mezzanine (`raw/bf_b<n>_<who>_s<first-frame source second>.mov`, H.264 crf 12 + PCM 48 kHz, 60 fps CFR, 0.3 s handle each side, native resolution; B3 stays 2560x1440). Framing: Scale = 1080 / source width (56.25 % for 1920 wide, 42.1875 % for B3), Position 0.5 / 0.5; no effects, no gain, no captions, no grade, no blur fill.

## Loudness per beat (the SOURCE windows, ffmpeg ebur128, measured 20 Nov ~22:45; `premiere/loudness.json`; clip gain is 0 dB in the sequence)
| beat | who | integrated LUFS | LRA | sample peak | gain to -17 LUFS pre-limiter |
|---|---|---|---|---|---|
| B1 | Fanum | -13.0 | 20.0 | -0.3 dBFS | -4.0 dB |
| B2 | Kai | -14.3 | 2.8 | -1.6 | -2.7 |
| B3 | summit1g | -31.0 | 1.2 | -17.5 | +14.0 |
| B4 | Fanum | -15.2 | 5.6 | -0.5 | -1.8 |
| B5 | Kai (night chase) | **-8.2** | 0.7 | **+0.3** (clipped at source) | -8.8 |
| B6 | Kai (night chase) | **-7.6** | 20.0 | **+0.4** (clipped at source) | -9.4 |
| B7 | game line (xQc silent) | -30.6 | 4.1 | -17.0 | +13.6 |
Spread across the cut: 23 LU (B6 vs B3). B4 -> B5 is a 7 LU jump and B5/B6 are screams over 0 dBFS: the build needs a per-beat level match plus a limiter (SEQUENCE-SPICY-v3 section 2 gave Fanum -14.6, Kai -13.2, summit -29.6, xQc -28 for whole clips; the beat windows differ, esp. Kai's chase).

## Why mezzanines (not the original files)
The originals are HEVC / VFR / Twitch mp4s; lab-notes 2026-11-07/08: a yt-dlp mp4 re-encoded before the first import gave zero File Import Failure modals. With no watcher running (flag 1) that matters more. The source seconds in the read-back = mezzanine window start (in the file name) + the clip in-point.

## Tool notes (the hub merges these into lab-notes)
- An `Edit`/heredoc that writes a Windows path ending in a backslash or a `"\\t"` arrives with the backslash collapsed: build separators with `chr(92)` and use the Edit tool for ExtendScript strings that contain `\t`.
- `ffprobe` on a section pulled from the Twitch VOD (HLS, `--download-sections`) starts at 0.0 and is frame-exact against the longer section: matching 128x72 grayscale frames at 60 fps gave a unique minimum (0.82 vs 2.77 for +-1 frame).
