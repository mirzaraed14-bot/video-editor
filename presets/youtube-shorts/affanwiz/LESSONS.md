# AffanWiz Shorts: LESSONS (lesson → change made → file)

Created 2026-11-09 (Short 4). His review notes go here after each check; a lesson that repeats becomes an ENGINE rule. Kit and lane bugs go in
`lanes/chat-only/lab-notes.md`, not here.

## Short 4 `stop-remaking-viral-shorts` (build, before his review)
- **A sunglasses take needs a PITCH gate as well as yaw.** eye-line.py measures yaw only; the delivered-file gate (`projects/stop-remaking-viral-shorts/work/reading_gate.py`) adds the nose-below-the-eye-line ratio: camera band 0.56-0.68 on this take, 0.85 flags a look down.
  → a reading gate with yaw AND pitch → that job's `work/reading_gate.py` (copy it for the next sunglasses take).
- **Level every swish from its own cue_check reading, never one blanket offset.** v1's slices read 21-28 dB under the voice in the phone band (WEAK); a flat -18.5 target then left the dark slice 2-3 dB hot full band (its energy is in the lows). The fix:
  - high-pass the low-heavy slices (k2 320 Hz, k3 260 Hz);
  - target -19.5 dB phone band per cue;
  - correct for the kit normalising to the slice's own peak.
  Result: full band 19.2-24.4 dB under the voice, inside the channel's 19-23 band, none weak.
  → `PHONE_V1` + `SLICE_ADJ` in that job's `yt/build_spec.py`.
- **Dandruff: look for MORE than one fleck, on the FINISHED Short at full size.** The second particle was 4x fainter than the first and only showed after the 2x face upscale, Topaz and sharpen (frame 1640). It cost a second clean, splice and Topaz pass.
  → the first full-size check of a face now covers the whole hair zone, not only the tracked fleck → `work/speck/` (`track2.py`).
- **A dated freeze on his own face is the kit's `fx: freeze`, never a card of a cropped still.** A card cut against his live face jumps, and it skips the A grade.
  → `yt/ghost.py` (overlay) + `fx` on the face shot.
- **A real thumbnail with burned-in text: crop around the text band.** The builder left half-words ("UT TO GIVE") on the transformed cards.
  → crops above and below the band, at <= 1.4x scale → `yt/cards_b.py` `make_faces`.
- **Never fade a crop into a blurred copy of itself to fill a card.** On the v6 check, the band-free face crop faded into a darkened, blurred green copy, and at full size it read as a muddy smear over half the card.
  The fix keeps one continuous 1:1 re-crop that SKIPS the band: rows above it, a 40-row crossfade, then rows below it. The shirt carries straight on, so the join is close to invisible. The source creator's watermark (on a flat wall) was interpolated out.
  → `make_faces` face 1 in `yt/cards_b.py` (v7).
- **Under memory pressure, render `--no-hq` and splice the Topaz face shots back in.** The turn card fix needed a new picture while other sessions held ~110-120 of 127 GB, and the 4K-base picture could not render.
  → `work/splice_hq.py`, proven per shot (|dY|), + the retry-and-gate chain `work/finish_v7.sh` → recipe in `lanes/chat-only/lab-notes.md`.
- **A one-video theme colour recolours the ACCENT, not the caption base.** v1 swapped the kit's base caption voice to green, so every caption came out green. Fix: base white, emphasis green (his caption rule: white base + coloured emphasis).
  → ENGINE § Format overrides (theme colour) + the job's spec `captions.palette`.

## Short 6 `research-agent` (sequence stage, 2026-11-17)
- **He asked for "a short on the research agent" and v1 pitched the be-first STAKES with the agent as the answer; he redirected: "no the
  research agent how to build it why build how it works that angle".** → When he names a subject, the Short is ABOUT that subject (what it
  is, why, how it works, how to build it), not a stakes story that uses it as the payoff. Ask "is the named thing the subject or the button?"
  before sequencing. → `projects/claude-gta6-shorts-money/clips/research-agent/SEQUENCE.md` v2 (v1 kept as `SEQUENCE.v1-be-first.md`).

## Short 5 `ai-tools-rant` (build, before his review)
- **A pause closed on his face is a visible jump even with head tracking and `head_lock`:** the hook's 0.56 s breath and beat 6's two breaths stepped the background 16-40 px (frame pair + `bg_strips`, response over 0.44; below that the strip number is unreliable, look at the frames). → keep the breath (one span) unless the joint sits on a scene change → `work/cut/make_edl.py` of that job.
- **WhisperX ran 90-150 ms late on segment-first words of a two-telling take, and one word leaked across an EDL edge:** read the real onsets off the 5 ms energy and re-time those words before captions/graphics key off them → `work/cut/bursts.py`, `transcript/words.json` (whisperx copy kept).
- **The verbatim faster-whisper pass finds false starts the energy pass keeps ("to ... for" after "sell"):** run it on the cut before the build, not after → `work/cut/fw_cut.py`.

## Short 5 `ai-tools-rant` (after the 07:26 check, 2026-11-17)
- **He swapped the hook to the guru impression + "shut the f*** up", and the claim moved to second.** v1 had the impression first and
  the advisor moved it behind the claim ("too slow, a scene not a hook"); his read: "the hook isn't that strong … that sets the tone
  better". → A comic call-out SCENE in his own mocking voice beats a stated claim as the hook on his channel, when trimmed to start AT the
  mocked line (he cut "I'm seeing so many videos of people saying"); the claim card under the captions carries the claim meanwhile.
  → `clips/ai-tools-rant/SEQUENCE.md` v3 order. Test on Short 6 and later: does the card-claim + spoken scene hook keep holding?
