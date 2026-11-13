# BRIEF: amy-grammy-satellite, RAW SEQUENCE (AW Short, Bolt format)

**Affan, 13 Nov 2026: "start the build" + "raw sequence".** Scope = the raw cut sequence in Premiere for HIS re-edit, the
same stage as `projects/mj-son-step-outside/` on 8 Nov (RUN.md "SEQUENCE COMPLETE FOR REVIEW"). His order for AW Shorts is
raw sequence → HIS sequencing (he re-edits it) → his direction video → code build (LESSONS 2026-10-24). So: no captions,
no grade, no Topaz, no graphics, no SFX, no CTA, no music, no export, no save. Stop when the sequence is laid and read back.

The locked script and every timestamp: `PITCH.md` § The script (read it first; it is the spec). Source = `raw/x0q3Re5ksVg.mp4`
(GRAMMYS official, 1920x1080, 29.97 fps, AAC 44.1 kHz), transcript `transcript/words.json` (`clips[].words[]`, keys
`w`/`start`/`end`).

## The sequence
- Name `Amy Grammy Satellite - raw cut`, its own bin, 1080x1920, 30 fps (the Son raw cut's settings), in the AW project he
  has OPEN (ABW11 since 13 Nov: read `app.project.path`, never open, switch or save a project).
- Tracks:
  - **V1/A1**: the three spoken source pieces, linked: beat 1 (Tony 9.65 → 12.63, keep the pause), beat 8 (Amy 84.89 →
    86.79), beat 9 (Amy 92.90 → 94.92, hard cut at the end).
  - **V1 picture-ONLY** under the narrator lines (beats 2-7): no linked audio. Beat 6's Tony shot carries "And the Grammy
    goes to" in its own audio, and that must not replay under the narrator.
  - **A4 = ONE crowd/room bed** under the narrator lines: the source's own sound continuing from 12.63 s (the transcript
    has NO words from 12.63 to 69.77 s, so any stretch in there is wordless), clip gain about −15 dB so the narrator reads
    clearly (a default he can change). It runs from the end of beat 1 to the start of beat 8, with short crossfades at both
    ends. The three spoken pieces stay at full level.
  - **A2**: the narrator, ONE clip per line (beats 2-7), so he can slide or swap a line on its own. **A3**: the alternate
    narrator voice, same lines, track muted (see § The narrator).
  - **V2**: picture-only covers: the reaction cutaway in beat 4 (her band hugging), and the jump cover between beats 8 and
    9 (her mum's face over the skipped 89.2-92.4 s, "for my Blake… incarcerated", which must not be heard).
- **The PITCH "Picture" spans are starting points, not cut points.** Resolve each one on a frame sheet. Rules:
  - No source frame plays twice, except the deliberate Tony callback in beats 6-7. That callback uses podium frames not
    already shown in beat 1 when the source has them; prefer frames where he isn't mid-word.
  - Beats 3 and 4 overlap in the PITCH (30-36 vs 27-33): split them.
  - Where a span is shorter than its line (beat 2: 13.5-16 s is 2.5 s for a ~5.8 s line), extend in source order or cut to
    the next shot of the same moment. Never freeze a frame or slow footage.
  - Write the final in/out per piece into the EDL with one line on why.
- **Reframe 16:9 → 9:16 by Motion scale/position per clip** (fill the frame, face framed, never squashed). Crop out the GRAMMY
  bug (bottom right). Never show the GRAMMY lower third that reads "REHAB" (~66-75 s of the source): check one frame per
  piece.
- **Beat 7 = a stacked two-panel split** (README § 13): Tony at the podium on top, her stunned face below, each cropped to
  fill its own 1080x960 band, a white separator line on the seam (y960, the caption line). Do it with Motion on V2/V3 plus a
  white matte on V4, or, if that's fiddly, lay both clips and leave a marker "stacked split" with the panel crops written in
  it. Say which.
- **Confirm her father Mitch's face** at ~42 s before using it for "her dad grabbed her" (frame check; if it's not clearly
  him, use the next clear shot of him or her mum, and say so).
- Markers: one per beat with the beat number and the narrator text.

## The narrator (his call #1 → an AI voice; he offered his ElevenLabs free plan, 13 Nov)
**Two voices, so he picks by ear at review:**
- **A2 = ElevenLabs** (what he asked for). It is scratch only, because of the free-plan licence below.
- **A3 = Epidemic Sound voiceover**, muted: connected, his paid subscription, and possibly publishable as is.
  - Tools: `mcp__epidemic-sound__ListVoices` / `GenerateVoiceover` / `PollVoiceoverGenerationStatus` /
    `DownloadVoiceover`.
  - Default voice "Dwight" (id `b0df8b12-635e-4c3c-9216-c9acd1627bfa`, American, calm, deep). "Edward" (British, calm,
    authoritative) is the second choice.
  - Whether his Epidemic tier clears AI voiceovers for a monetised channel is NOT confirmed. Say so; he checks.
- **ElevenLabs key missing when you reach narration:** Epidemic goes on A2 (active), and ElevenLabs fills A3 when the key
  arrives. No timed gaps needed.

**ElevenLabs:**
- **CONNECTED, 13 Nov, as a claude.ai connector, not via `.mcp.json`** (the placeholder entry was removed).
  - Tools: `mcp__6c826a7b-d2e0-4c0d-bffd-c2373fbf69c0__*`. Load them with ToolSearch: `account_get_usage`,
    `creative_list_voices`, `creative_generate_speech`, `creative_get_flow_run_status`, `creative_show_flow_results`.
  - Checked: tier FREE, 0 / 10,000 characters used.
  - `creative_generate_speech` spends credits, so:
    - pass `generations_count: 1`;
    - run `estimate_only` first;
    - never re-call it to retry a run (each call charges again).
- **Voice:** one consistent voice for every line. Default = "Oliver Silk - British Deep Gravel" (the 2 Oct Kanye Bolt test;
  voice_id `jfIS2w2yJi0grJZPyEsk`, a library voice, found via `creative_list_voices`). If the free key
  refuses library voices, use the calmest premade male narrator voice (list `/v1/voices`) and name it in RUN.md. One take
  per line at default settings. Only re-take a line when a word is wrong (re-ASR each take against its text).
- Budget: about 560 characters a pass, well inside the free 10K a month.
- **Licence, written into RUN.md:** the free plan is NON-COMMERCIAL with attribution, and audio made on it does not gain
  commercial rights after an upgrade. So this narrator is a **scratch for his re-edit only**. The published Short needs the
  lines regenerated on a paid plan (Starter), another licensed voice, or his own read: his call at review.
- Lay the timeline on the A2 voice's line lengths. A3's lines start at the same in-points; where an A3 line runs longer,
  note it, don't re-time A2.
- Expected length about 40 s (PITCH: narrator 103 words, source 18).

## If Premiere isn't running, or the open project isn't the AW project (ABW11)
- Don't open, switch or start anything.
- Prepare all of it, then report what's ready and stop: the EDL, `premiere/place.jsx`, the narrator takes, the proof sheets
  and the A1 re-ASR (built from the EDL).
- The placement window then runs on his word.

## Optional, time-boxed (≤ 2 YouTube requests)
Trace the original of `v7trR7a3ILU` (OhMyAmy fan Short, 109K: Amy on camera about meeting Tony Bennett, likely the 2011
*Duets II* session/EPK). If an original ≥ 720p exists where SHE says it was him saying her name, download it into `raw/`
and place the line in the bin only (never in the sequence: the script is locked). Tell him it could replace narrator
beat 7. YouTube only through `projects/_onyx-batch2-2026-10/lock.sh youtube`, ≥ 60 s apart; stop at a bot check or 429
(write `.locks/youtube.BLOCKED`).

## How (copy the Son raw-cut kit, adapt; never edit the Son's files)
`projects/mj-son-step-outside/`: `edl.py` (word-exact EDL from words.json, valley-based edges), `build_place.py` →
`premiere/place.jsx`, `premiere/run_window.py` (takes `premiere.lock`, restores his active sequence, never saves),
`premiere/readback.js`, `premiere/pp.py`, `premiere/delete_ours.js`. Read its RUN.md § Tool notes first:
- 29.97 fps sources on a 30 fps sequence: request each in-point at the first source-frame boundary at/after the target
  1/30 s boundary (+0.1 ms);
- start re-encode windows on a frame boundary.

Premiere-safe re-encodes go in `h264/` if needed.

## Hard rules
- **Premiere:** `premiere.lock` for every window (SESSION-START ground rules); a new sequence only, his other sequences never
  touched; his active sequence restored after every window; never save; never export; never overwrite a file Premiere has
  already imported; `lanes/premiere/dialog-watch.py` closes modals (don't run your own).
- **Silence:** never play audio or video; ffmpeg to `-f null` for analysis; no players; close media tabs.
- **No drug words heard:** her speech skips 89.2-92.4. Her death is not in the Short. No minors on frame.
- **GPU** (WhisperX re-ASR) only under `lock.sh gpu`; `WHISPERX_DEVICE=cpu` when it's held. Never kill another session's
  processes.
- **Files:** on X: only (ElevenLabs output lands in `projects/_elevenlabs/`; move this job's takes into `audio/narrator/`).
- **Model roles:** no Fable agents; any helper agent gets `model` passed (Sonnet for mechanical work).
- **Budget:** about 1.5 % of the weekly plan (78 % used at the start, 13 Nov). Check `get_usage`.

## Done =
1. The sequence is laid and read back (`premiere/readback.tsv`).
2. A1 + A2 rebuilt from the read-back and re-transcribed: the script's words in order (narrator lines included), and
   nothing from 89.2-92.4 heard. The A4 bed is wordless.
3. A crop contact sheet of V1/V2 at 0.4 s steps (`proof/timeline_crops.jpg`): no REHAB, no bug, faces framed.
4. `RUN.md` ▶ STATUS rewritten.
5. A plain report to him: the sequence name, length, the voice used, and what's open. Open items to cover: the licence;
   Mitch; the split; the v7trR7a3ILU trace; his title and London-line calls.

His approval button says only "approved". The code build is a separate later step after his re-edit + direction.
