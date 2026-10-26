# Abundance Wisdom long-form: PLAYBOOK

**This is a starting point, not a style lock.** The creator, 2026-10-26: "I don't want to lock this style in… I'm constantly
trying out different effects and motion graphics… with every single video I need 5 % improvement in smoothness and premiumness
and the expensive look." So the gist below is where a new video STARTS. Every video must end at least 5 % smoother, more
premium and more expensive-looking than the last one. New effects, new motion graphics and new sounds are expected; repeating the
last video's moves unchanged is a regression. Numbers here are guards against accidental drift, never targets (LESSONS 20).

Read with: [`LESSONS.md`](LESSONS.md) (what each review taught, newest last) and the FX catalog
([`research/effects-catalog/CATALOG.md`](../../../research/effects-catalog/CATALOG.md), FX-01..81).

## 1. Before ANY edit: the research pass (every video, before the first cut)

1. **The whole style catalog, frame by frame.** Read every entry of `research/effects-catalog/CATALOG.md` (FX-01..81). LOOK at every
   reference still in `research/effects-catalog/shots/` (137 frames; `index.html` shows them with notes). Do not skim the table.
   Write a **catalog pass** into the job's BRIEF.md:
   - the moves that fit this story's beats (by line or chapter, with FX codes);
   - the moves never used on this channel yet (at least two of them go into this video);
   - the moves the last video leaned on, so they aren't repeated unchanged.
2. **The last AW long-forms, measured, not remembered.**
   - THE LAST SHOW (`projects/cbum-last-show/`): the current state of the art. Read `work/redo/REPORT-19.md`,
     `work/redo/REPORT-REVIEW-2.md` and both review folders (`review/critique-2026-10-21*/`).
   - SAME NIGHT (`projects/nick-martin-same-night/`): his "so many crazy animations" bar.
   - Nick Walker (`projects/nick-walker-never-mr-olympia/`): the first one, and his gold-matte card look.
3. **Fresh outside research** (CLAUDE.md learning loop #5). Study the format's current best examples:
   - start from `research/premium-doc-channels.md` and look further;
   - bring at least one NEW move that is not in the catalog yet;
   - add it to the catalog as FX-82+ with a reference still.
4. **Write "Beats THE LAST SHOW by…"** into the BRIEF (or by the previous AW long-form, whichever is newer). Name concrete,
   checkable improvements in smoothness, premium feel and expensive look. If he gives the previous video's YouTube retention
   graph, name the drop-off moments and say what this video does differently there.
5. **Show him the cold open first** as the checkpoint, and ask about the LOOK, never about seconds.

## 2. The gist (state after THE LAST SHOW, Oct 2026): where a new video starts

**Format.** A face-led documentary. He is on camera (C-cam, scripted, sometimes reading). Archive inserts keep their own audio.
Structure: cold open → title → about 5 chapters with chapter cards → end card → end screen. About 10-12 min.

**Visuals.**
- **One designed visual per host LINE.** A new visual on each new line or thought. Never one archive clip stretched across lines.
- **The person named is the person shown**, from a flattering shot.
- **Sources:**
  - motion graphics built in the kit (name the FX code on every visual);
  - Higgsfield images for concept lines (no text inside generated images; preflight the cost);
  - REAL evidence rebuilt faithfully: Instagram profile and post fetched live, results sheets, headlines. Never a mock-up (LESSONS 25);
  - archive footage used fresh per line and framed well.
- **One subject per frame, graded into the film's palette.** A collage reads cheap (LESSONS 22).
- **Long inserts get visual change per thought** (pointer tags, name tags, punch-ins on the scorebug), always keeping the clip's audio.
- **Pointers on people are TRACKED** and rest on the body. A name goes on only when the identity is PROVEN: a legible bib, or a
  matching reference photo (LESSONS 26, 31). Send him the evidence with any identity call.

**Motion.**
- Easy ease on every move.
- Entrances take 0.8-1.5 s.
- A build settles at least 1 s before its cut.
- Built graphics are stepped at 20 fps (FX-81); real footage stays smooth.
- Opacity fades in and out, never pops. A flash transition where the energy turns.
- No freeze-frame under his voice.
- No push-in on a still portrait.
- A cover never opens on black and is never shorter than 1 s (LESSONS 28-30).

**Host.**
- His face appears only where he looks at the camera. Every reading span is covered.
- Consecutive face cuts are NESTED with ONE subtle eased zoom-in (≤ 4 %). No per-clip repositioning, no cut zooms.
- Host grade: the LUT as a master-clip effect, no vignette (LESSONS 19).

**Type and palette (THE LAST SHOW kit; evolve it, don't freeze it).**
- Palette: stage #0E0F12, gold #E8B54A, ink #EDEBE6, steel #7FA6C9, red #E5483B, marker #FFD84A.
- Type: Anton for headlines, Instrument Serif italic for quotes, Plex Mono for tags, Montserrat for subtitles and titles.
- Titles: the FX-12 title and chapter-card family.

**Subtitles.** On EVERY third-party clip, never on his voice. Clean, small, no animation. A speaker tag on first appearance,
swears as a solid bar.

**Sound.**
- Voice first.
- Every insert is level-matched to his voice, with fades at every joint.
- An insert ending mid-syllable gets a breath plus the speaker's own room tone (LESSONS 27).
- SFX: a FRESH, wide Epidemic pool per video, several takes per action class, rotated so nothing repeats back to back
  (LESSONS 24).
- Each sound matches what its animation does (a highlighter gets a marker stroke).
- Whooshes sit 10 dB under the hits.
- Premium only: no magic, UI, typing, trilling or electric sounds.
- "Expensive" means audible on a PHONE. Check the 300 Hz-6 kHz band, and use high-passed hits plus one sub layer (memory
  feedback-premium-sfx; the checker is `projects/_client-scott-clary/chris-do-sneaker-pricing/ig/cue_check.py`).

**Subscribe alerts.** About 3 per 11 min, small, lower-left, in the film's own tag language, only on calm host-face windows
(LESSONS 32). His explicit ask overrides the repo's default "no CTA" rule for this channel.

## 3. The procedure: the CLAUDE.md eight steps, with what is specific to this channel

1. **Intake.** Copy the raw file into `projects/<job>/raw/`. Name the job after the content.
2. **Rough cut.** It is a SCRIPTED shoot, so WhisperX hides the retakes. Use the LESSONS 18 method:
   - sub-span re-ASR at the silences;
   - forced alignment of the LAST complete take;
   - the cluster sweep at 0 repeats.

   The cbum tools are in `projects/cbum-last-show/work/` (`slice_asr.py`, `realign.py`, `fit_test.py`, `cluster_sweep.py`,
   `rebuild.sh`). Mark the reading spans (eye-line) for the cover gate. Verify every attributed quote by voiceprint.
3. **Audio polish.** The static chain (CLAUDE.md), then level-match the inserts.
4. **Grade.** The host LUT as a master clip. Archive graded into the film's palette inside the comps.
5. **Graphics.**
   - Map every host line to a visual in a line map (`work/redo/linemap.py` pattern).
   - Agents work per chapter from one shared brief (the `work/redo/REDO-PLAN.md` pattern). Each agent writes PLAN.md,
     builds, and hands back `placement.json` + HANDOFF.md.
   - Only the main session writes to Premiere.
   - Start from THE LAST SHOW's kit CODE (`redo-gfx/kit.py`, `render.sh`, `hf-anim.js`) and improve it. Never reuse a past job's
     renders, comps or assets: every visual is made fresh for this video.
6. **SFX.** A fresh pool; build, then place (the `work/redo/sfx/build_sfx.py` + `place_sfx_redo.py` pattern). Check the
   phone band.
7. **Review.**
   - Before his first watch, run the verify: nests, no stills, fades at face edges, inserts levelled, subtitles complete, no
     cover under 1 s, no 1-3 frame gaps.
   - He watches in Premiere.
   - After his review: LESSONS entries, and update this playbook when a lesson repeats.
8. **Export.** HE exports. Never exportAsMediaDirect, no copies on C:, masters only in `X:\Claude Projects\Exports\`.

## 4. Shared-machine rules (each was learned the hard way)
- Premiere is shared with other sessions: edit BY NAME (sequence name AND id).
- Any active-sequence or QE action goes inside `lanes/premiere/ACTIVE-WINDOW.lock`.
- Export an FCP XML before any batch change.
- Never place an A/V item on an audio-only track: it overwrote V1 on THE LAST SHOW.
- After a recovery, close the damaged sequence's tab at once. Delete it only with his OK, after an XML backup (LESSONS 23).
- Work in silence: no players, no media pages, ffmpeg to files or `-f null`. Put the silence rule in every agent brief.
- GPU jobs go through `projects/_onyx-batch2-2026-10/lock.sh gpu`. Never kill another session's process.
