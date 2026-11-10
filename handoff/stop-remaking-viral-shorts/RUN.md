# RUN — stop-remaking-viral-shorts

**Next action:** WAITING for Affan's review of the check `X:\Claude Projects\Exports\affanwiz-stop-remaking-viral-shorts.check.mp4` (**v7**, swapped in 2026-11-09 21:44; it replaces v6 and v4). v7 = v6 + the turn card's "TRANSFORM IT A LOT" phase rebuilt (face 1 = one continuous 1:1 re-crop, no blurred green smear; the source creator's SPEEDZYY watermark is interpolated out of that crop, his call pending: "Keep it visible" = delete the interpolation lines in `yt/cards_b.py` `make_faces`, re-render the turn card, rerun `work/finish_v7.sh`). No open defects. If he approves, the check IS the final (rename `outputs/*.sample-yt.v7.mp4` to `.final.mp4`, `finalize.sh`). A note = data + ONE finish render. Under memory pressure, use the `finish_v7.sh` pattern, never a blind chain. His prediction for RESULTS row 4 is still blank.

| | | |
|---|---|---|
| channel | **AffanWiz** (English personal brand) — Short 4 | content: Shorts-creator advice, Skool sign behind him; no CA script matches (unscripted take) |
| format | **Short**, 9:16 1080x1920, native 59.94, from a 16:9 face-cam take | Scott Clary YouTube format (AffanWiz ENGINE § line 3), like Short 3 |
| lane | **code-built** (onyx-samples-youtube kit, `yt_build.py`), MP4 to `X:\Claude Projects\Exports\` | `.setup-complete` says premiere, but AffanWiz Shorts are code-built per the channel ENGINE; ABW10 untouched |
| preset | `presets/youtube-shorts/affanwiz/` (ENGINE, FINDINGS, RESULTS, UPGRADES new) + Scott kit | Scott ENGINE/UPGRADES + `research/shorts-style-radar.md` read; radar pass 2 added 2026-11-09 |
| source | `raw/C1454.MP4` (copied from `X:\Recordings\Afterhours\C1454.MP4`, original untouched, still read-only) · 1920x1080 h264 59.94p · PCM · 119.62 s | the cut reads `work/speck/C1454.clean2.mov` (both specks removed, lossless) |
| constraints | green theme THIS VIDEO ONLY (spec `captions.palette` green voice + `hook.grad` + cards; kit yellow untouched) · silence · exports only to X:\ Exports · no git commit · no Fable agents | |
| started | 2026-11-09 | |

## Steps
| # | Step | Status | What it produced / why not |
|---|------|--------|----------------------------|
| 1 | Intake | done | `raw/C1454.MP4` (cp -p, original read-only untouched); job renamed from provisional before splice |
| 2 | Rough cut | done | 23 segments from `work/speck/C1454.clean.mov` (`work/cut/make_edl.py`, last takes, card lines tight / face pauses >= 0.38 s only, +0.24 s beat before "No!"); 43.98 s; audio-qa 22 joints clean; both verbatim passes on the cut read clean (`work/cut/fw_cut_v1.txt`); 4 words re-timed in words.json (whisperx copy kept) |
| 3 | Audio polish | done (baked by splice) | voice-gain measured +2 dB → −6 dBFS limiter; peaks kissing, 0.0044 % pinned |
| 4 | Color grade | n/a (Short) | POP grade + sharpen ride the build (Scott set) |
| 5 | Graphics | done (v7 check delivered: turn-card fix in) | 6 cards (`yt/cards_a.py` scan + crt, `yt/cards_b.py` post/grid/turn/bars, shared `yt/cardkit.py`) + the 2024 Year Ghost as a kit freeze + `yt/ghost.py` overlay; reviewed frame by frame, 6 defects fixed (see BRIEF § Build) |
| 6 | SFX | done | 15 swishes (Short 3's approved set), each levelled from cue_check to -18.5 dB phone-band under the voice; v4: none weak, loudest -16.3 dB full |
| 7 | Review | WAITING | check `affanwiz-stop-remaking-viral-shorts.check.mp4` in Exports (v7, 2026-11-09 21:44) |
| 8 | Export | — | |

## Request coverage (his three asks, 2026-11-09, voice-dictated)
1. **Dandruff speck** removed, tracked, no blur blob, no swim/flicker; proof = full-size before/after stills + a real-speed clip of the fastest head-move span → `work/speck/`. Every shot where it shows.
2. **1 % better** → research + catalog pass (BRIEF § Catalog pass) + ≥ 2 moves new to the channel, logged in `presets/youtube-shorts/affanwiz/UPGRADES.md` (created 2026-11-09: AffanWiz numbers never go in Scott's files).
3. **Green theme today only** → caption emphasis, MG accents, green gradients; per-video override recorded here and in BRIEF; preset locked yellow untouched.
- Standing: reading covered (eye-line.py), face ≤ 4 s, sequencing OK first, prediction locked in AffanWiz RESULTS before upload, title ≤ 5 words.

## Gates on the delivered check (v7, 2026-11-09 21:44)
- **What changed from v6:** only the turn card (s11, frames 2122-2530): face 1 is one continuous 1:1 re-crop of the source Short (skips the caption band with a 40 px blend), no blurred green copy; SPEEDZYY interpolated out of that crop (phase 1, the source Short shown as-is, still carries it).
- **How it was built:** `work/finish_v7.sh` (waited for commit < 110 GB: 124-127 GB until 20:49, then 101 GB and it started): picture `--no-hq` try 1, `splice_hq.py` gate PASS (A shots |dY| 2.52-2.79 vs v5 Topaz, untouched B 0.00-0.01, s09 4.67, s11 0.55), grade try 1, sharpen try 1, composite try 1. Log: `work/finish-v7.log`.
- **v7 vs v6, per shot (decoded frames, mean |dY|):** every shot 0.00 except s11 1.06 (the fix) and s10 0.06 (max 0.55, encoder noise next to the changed frames).
- **Audio:** the v7 audio stream is byte-identical to v6's (md5 c9daf896...), so loudness (-12.2 LUFS, LRA 2.7, TP -2.2), sync, the mute and SFX carry over from v6 below.
- **Reading:** 0.00 s over |yaw| 0.25 or pitch 0.85 (`work/reading_gate.py` on v7); face 11.98 s in 5 runs, longest 3.42 s.
- **Picture:** 1080x1920, 60000/1001, 2636 frames. Full-size checks: turn 2200/2300/2380/2450/2500 (`work/v7check/`), 20-frame sheet `outputs/*.proof-check.v7.jpg` (also in Exports as `.check.proof.jpg`).

## Gates on the previous check (v6, 2026-11-09 20:08, superseded by v7)
- **What changed from v4:** grid cards apart (the YOURS copy's own caption reads whole), YOURS label at y 252 (out of the top 200 px), turn card: no cut-off thumbnail words (face 1 = band-free crop over a soft fade). Everything else is the same spec.
- **How it was built (memory pressure: other sessions held 110-127 of 127.7 GB commit):** the 4K-base picture OOM'd twice, so the picture rendered `--no-hq` (1080 base) and `work/splice_hq.py` spliced the A shots (his face) back from v5's Topaz picture (`yt/work/picture.whip.ungraded.v5hq.mp4`), per shot. Proof before the splice: untouched B shots |dY| 0.00-0.01, A shots a steady 2.5-2.8 (sharpness only), only s09 grid (4.67) and s11 turn (0.23) changed. Grade succeeded on try 5, sharpen on try 1, composite on try 1, each gated on its own fingerprint.
- **Topaz faces confirmed on the final:** face-box Laplacian variance v6 vs v4 within 1-2 % on 5 face frames (623/630, 848/850, 243/245, 276/273, 529/524); v6-v4 mean |d| on face frames 0.5-2.3, the same as untouched card frames (0.4-2.2) = encode noise.
- **Dandruff:** unchanged from v4 (source-level, both passes, all 7170 frames; the A shots are the same Topaz frames).
- **Reading:** 0.00 s over |yaw| 0.25 or pitch 0.85 (`work/reading_gate.py` on v6); face 11.98 s in 5 runs, longest 3.42 s.
- **Audio:** -12.2 LUFS integrated, true peak -2.2 dBFS, LRA 2.7; voice in sync with the base cut at 6 points (0.0 ms lag, ncc 0.995-1.000); "f***" muted 24.889-25.199.
- **SFX (`yt/cue_check.py`):** 15 cues, full band 19.2-24.4 dB under the voice, phone band -19.5 to -19.7, none weak, bus at its loudest -19.2 dB (PASS).
- **Picture:** 1080x1920, 60000/1001, 2636 frames, 43.98 s; POP grade + sharpen 0.55/0.40, cards excluded. Full-size checks: grid 1900, turn 2300/2450 (`work/v6check/`), 20-frame sheet `outputs/*.proof-check.v6.jpg`.
- **Captions:** white base + green emphasis, below the lips (unchanged overlay).

## Gates on the previous check (v4, 2026-11-09 16:40, superseded)
- **Dandruff:** pass 1 (main fleck) 0 px outside the box on all 7170 raw frames, top-hat 106 → 11; pass 2 (a second, fainter fleck found on v3) 0 px outside the box on all 7170 frames, top-hat 24 → 12 (max 35, under hair texture). Viewed at full output size on every face shot incl. the fastest move (80 s raw) and frame 1640 where v3 showed the tick: clean. Proof media: `work/speck/proof/`.
- **Reading:** 0.00 s over |yaw| 0.25 or pitch 0.85 on every face frame of the file (`work/reading_gate.py`); face 11.98 s in 5 runs, longest 3.42 s (1.87 s of it the frozen 2024 beat under the overlay).
- **Audio:** -12.1 LUFS, true peak -2.2 dBFS; voice in sync with the cut (0.0 ms lag, ncc 0.993-0.999 at 6 points); "f***" muted 24.889-25.199.
- **SFX:** 15 cues, none weak on a phone, loudest -16.3 dB full band under the voice.
- **Picture:** 1080x1920, 60000/1001, 2636 frames, 43.98 s; Topaz Iris 2x base (no watermark on the frames checked); POP grade aimed at the room (cheek hue 19-24, sat .34-.38) + sharpen 0.55/0.40, cards excluded.
- **Captions:** white base + green emphasis (checked at full size), below the lips; numbers and words as he says them.

## Flags to report
- The last line: both verbatim passes on the cut hear "That will be pushed 100 times more" (captions say so).
- Not watched or heard at real speed by a person (no playback here).
- Short 1 overlap (same topic family): said in the sequence.

## Skipped, and why
- **30 fps check → a native 59.94 check.** The source is true 59.94p, so there is no Chronos step: the check is built at 60 on the Topaz 4K base and, if he approves it, is the final. Saves a second build.
- **rough-cut fresh-eyes second pass (two subagents): not run.** Usage lean. The cut was instead read against two verbatim faster-whisper passes on the spliced cut (plain + filler prompt), both clean, plus the RMS profile at every edge.
- **edit-review fresh-eyes rounds: not run.** Usage lean. Every card was reviewed by me frame by frame, which caught 6 defects; v4 got a 20-frame proof sheet and full-size checks of captions, the freeze, hair and audio. One Sonnet frame-sheet review round on v5 is the stand-in (see below).
- **graphics-qa.py: not applicable.** It gates hf-graphics/HyperFrames comps; this Short is the onyx YT kit's spec build.
- **Background music: not run.** He scores himself (memory "music is his job"; ENGINE: no bed).
- **Output-level dandruff detector: invalid, not used as a gate.** It flags hair highlights. The proof is at the source (bit-exact + top-hat, both passes, all 7170 frames) plus full-size crops of every face shot.

## Fresh-eyes review round (Sonnet, 46 full-size frames of v5, 2026-11-09) and how each finding was settled
- **Fixed:**
  - The YOURS copy was tucked under the original's ring, so its real caption read "OU A PRESENT": the cards are now apart (OX 330, YX 760).
  - The YOURS label's top was at y 193, inside the 200 px band: moved to y 252.
  - The turn card had a hard edge at y ~680: now a 190 px fade.
  - Before that review (advisor): the turn card had cut-off thumbnail words, fixed by crops around the band; the swishes ran hot, fixed by high-pass + -19.5 dB phone target.
- **Intended, not changed:**
  - The 100x bar running off the frame top: the approved design (it breaks the frame, to scale).
  - The YouTube page's body lines cut at the card edge during the push-in: a camera move into a document; the highlighted lines stay whole.
  - The "warp" on frames 640/655: none. They are the same held freeze frame with the 2024 slam over it.
- **Checked, NOT dandruff:** the white spots at the crown on frames 980-1000 (the "No!" shot) and 2110. The flyaway hair forms loops there and the wall shows through the gaps. They appear only while a loop is open (raw 2748, 4500), they sit on the head's silhouette, and the curved strands are visible around them. Left as they are, because painting them out would change his hair's outline. **Named to him for a call.**
