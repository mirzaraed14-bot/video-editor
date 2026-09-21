---
name: background-music
description: "Lays a background music bed UNDER the voice on a near-final cut — a FLAT constant bed by default (no ducking, no fade-in, −20 dB, short tail fade-out only). Ducking + fade-in are opt-in. OPTIONAL, format-agnostic (any short or long video). Runs after SFX (step 6), before Review (step 7). Triggers: add background music, add a music bed, lay music under, BGM, add a soundtrack, put music behind this."
---

# Background Music — Flat Bed Under the Voice

Optional conditional pass — after step 6 (SFX), before step 7 (Review). Takes a near-final cut and lays a music bed under the voice.

**The default is a FLAT bed:** the music sits at **one constant level for the whole video** — no sidechain ducking, no fade-in — with only a short tail fade-out at the end. The voice is measured to −17 LUFS before the −6 dBFS limiter, so a quiet fixed bed (−20 dB starting gain) sits under it. A peak limiter guards the sum; there is **no loudnorm** on the flat path (single-pass loudnorm on a finished mix pumps and re-introduces the very level variation we're avoiding).

> **Why flat is the house default:** ducking (music dipping under the voice and swelling back up in the gaps) made past mixes get audibly *louder and quieter in parts*. The bed’s **gain stays fixed**; the song itself can still vary in loudness. That's the default. Ducking and fade-in are **opt-in only.**

Most useful on **short-form explainers**, but works on any format. It's opt-in — skip it unless asked.

## When to run
After **SFX (6)**, before **Review (7)** — the slot CLAUDE.md's conditional-pass table gives it. Captions are already on the timeline by then (a step-5 graphic on short-form). Use the latest edited timeline on an app lane, or the latest rendered cut on the chat-only lane; never mix against raw footage.

## Where the music comes from
Drop a track into `projects/<job>/audio/`. Two ways to get one:
1. **Your own / licensed track** — drop an `.mp3`/`.wav`/`.m4a` into `audio/`. Use the newest file there.
2. **Generate one** (royalty-free, no copyright strikes — on brand) via the vendored `media-use` skill: `node .claude/skills/media-use/scripts/resolve.mjs --type bgm --intent "<mood>" --project projects/<job>` (run its sign-in Preflight first per `media-use/audio/references/bgm.md`; there is NO `npx hyperframes bgm` command). Prompt the mood to match the reel, write the result into `audio/`.

If `audio/` is empty and no track is pointed at, ask one line: *"Drop a music track in `audio/` or want me to generate one — what vibe?"*

## Run it
```bash
.claude/skills/background-music/scripts/mix-music.sh \
  <near-final-video.mp4> \
  projects/<job>/audio/<track>.mp3 \
  projects/<job>/outputs/<job>-music.mp4 \
  [bed_db] [duck] [fadein] [source_in]
```
- Output is non-destructive — `<job>-music.mp4`, never clobbering the no-music cut. That music-mixed file is what **Export (8)** promotes as the deliverable.
- `bed_db` — music gain. **Default −20 (quiet starting gain).** Recording loudness varies; verify the actual mix and adjust the whole bed if needed. Stay negative — this is a bed, not a duet. Balance is taste; re-run with a different `bed_db` to tune.
- `duck` — **`off` (default) = FLAT constant bed, no ducking.** `on` = opt-in sidechain auto-duck (music dips under voice, swells in the gaps) **and** re-normalizes the whole mix to −14 LUFS. Only turn it on when you specifically want the bed to breathe with the talking.
- `source_in` — optional reviewed source start in seconds; otherwise use the shared sustained-entrance candidate below.
- `fadein` — music fade-in seconds at the start. **Default `0` = no fade-in (the bed is just there).** Pass e.g. `2` for a 2-second fade-in. Opt-in.

**Default (flat) needs only the three required arguments** — no flags needed:
```bash
mix-music.sh cut.mp4 audio/track.mp3 out-music.mp4
```

## On an app lane (Premiere ✅, others by hand)
The near-final cut lives on a timeline, not in a file, so the bed goes on the **music track** (A5 on the `youtube/default` map) with the same numbers. Premiere is scripted; the loop is apply → bounce → listen:
```bash
uv run lanes/premiere/place-music.py projects/<job> --apply     # newest audio/ track → A5, onset-trimmed, −20 dB, 2s tail, read back, saved
uv run lanes/premiere/place-music.py projects/<job> --bounce    # music-only WAV bounce in-Premiere (no AME) + LUFS: the proof it plays
uv run lanes/premiere/place-music.py projects/<job> --verify    # readback vs the numbers (exit 1 on drift)
uv run lanes/premiere/place-music.py projects/<job> --remove    # take it off before a re-place
```
`--bed-db -27` retunes the level, `--track <file>` overrides the newest-file pick. A level change on an already-placed bed is `--remove` then `--apply --bed-db N` (the level lives in a keyframe and must be rewritten through it, never set statically: [`lanes/premiere/lab-notes.md`](../../../lanes/premiere/lab-notes.md)). Resolve and CapCut: the same numbers by hand (onset in-point, −20 dB, 2 s tail), stated in RUN.md as done by hand ([`LANES.md`](../../../LANES.md) § Background music).

## Tuning notes
- **Start at the sustained musical entrance, not the first transient.** Run `uv run workflows/music-onset.py <track> --json`. It compares a one-second sustained envelope with the main bed in the first 60s and adds 16ms of attack pre-roll. Sparse intro sounds must not leave the hook effectively silent. This is a candidate, not a beat detector: inspect/listen to the opening and the voice+music balance. Keep an intentional quiet intro only when it fits the request; use `--source-in N` on Premiere or the final positional `source_in` on `mix-music.sh` to set the reviewed entrance. Record the chosen source start, level, and evidence in RUN.md. Never hardcode a previous song’s timestamp.
- Premiere persists the selected track, gain and source start in `hf-graphics/music-plan.json`; later verify/apply reuses those approved values. An explicit `--track`, `--bed-db` or `--source-in` overrides them. After a duration change, retain the approved entrance/gain and move the 2s tail fade to the actual ending.
- The chat-only mix script loops the track to cover the full video and fades the tail out over the last 2s (2026-09-04; always on — a clean ending, not a level move).
- Voice intelligibility is the priority. If the bed feels too present, drop `bed_db` further (e.g. −27). If it's buried and you want it more felt, raise gradually after listening. Keep it flat — don't reach for ducking just to make it louder; lower the bed or raise it as a whole.
- **Don't default to ducking.** It's there for the rare case you want the bed to swell in the gaps. The flat bed is the house sound.
- Verify after: play it, or `ffprobe`/`ebur128` the output. On the flat path the bed sits at a constant level (the mix's loudness range tracks the *voice*, not the music); on the duck path the mix is re-normalized to −14 LUFS.
