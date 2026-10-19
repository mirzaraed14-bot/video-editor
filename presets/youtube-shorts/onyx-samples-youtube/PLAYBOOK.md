# Onyx sample Shorts, YouTube look: THE PROCEDURE

How to build a sample for a **YouTube-first** prospect. The look and its numbers: [README.md](README.md). Lessons: [LESSONS.md](LESSONS.md).

**The funnel is shared with the Instagram look.** Read `presets/youtube-shorts/onyx-samples/PLAYBOOK.md` for the funnel, the division of
labour, § 0 (pick the platform), § 1 (find and pull the source), § 7 (Affan's reaction video) and § 8 (delivery). Those steps are the same for
both looks and live only there, so the two never drift apart. This file covers only what changes for YouTube: the angle, the storyboard,
the assets, the build and the QA.

## 2. The angle and the cut (adds to the shared § 2)

The cut follows the Onyx clips engine as usual (`X:\Claude Projects\Hormozi Business\my-businesses\onyx-shorts-engine\`). Three additions
for this look, all **hypotheses** from one reference until a YouTube-look sample is measured:
1. **Showability.** This look lives on B-roll, so rank angles partly by how many of their lines name something that can be SHOWN (a place, an
   object, a company, a person, an event). A story told in concrete nouns beats an abstract opinion. Note the count beside each angle in
   `angles.md`.
2. **The loop.** Pick the out-point so the last line runs back into the first (README § 9). Read last → first aloud before locking the cut.
3. **Who speaks.** List every voice in the cut, quoted voices included ("she goes…"), because each one gets its own caption colour
   (README § 5). Diarize when there are two or more speakers.
4. **Open on the host's question** in an interview clip (batch 3, STYLE-RESEARCH § D7; Shawn Ryan's 614K sniper Short): 0.8-1.6 s of
   the host asking, the hook card over it, then the guest's answer. The host's chunks get their own caption colour (`main` / `yellow`).
5. **Shorter by default: 32-45 s** (§ D8: Shawn Ryan's two best recent Shorts run 32.2 s and 41.2 s; batch 2 ran 44-55 s). Keep 55 s
   only when the payoff needs it; `yt_build.py` notes a runtime over 45 s.

## 3. Storyboard (the gate before building)

`projects/<job>/storyboard.md`: **one row per SHOT**, giving:
**time · words · shot (A / B / SPLIT) · the picture, described · its source (URL or stock ID, and the in-point) · caption voice and colour ·
which chunks wipe · effects (whip direction, hook title, sticker, story effect).**

Check it against the README § 3 rhythm rules before Affan sees it:
- the B-roll / SPLIT / speaker shares (≈ 50–55 / 10–15 / 35 %),
- every B-roll shot arriving 0.3–1.9 s before its noun,
- shot lengths: ~2 s in the set-up, ~4 s in the payoff: **after the turn the mean shot is ≥ 3.5 s and the last shot ≥ 3.0 s**
  (`yt_build.py` prints both and warns under 3.0 s; batch 2 ran 1.99-2.66 s after the turn),
- the first B-roll by ~0.7 s, and the last shot on the speaker (or the closing image, Y3),
- **receipts (batch 3, § D1-D2): ≥ 50 % of B-roll inserts are the real thing; 0 stock actors as a named or quoted person; every
  sourced claim that can be shown is a DOC (the article / post / chart / the show's own episode card) with its line highlighted;
  ≤ 2 marks (circle / box / underline / arrow) per video; one story `fx` at most, only when the words describe it,**
- the batch's variety rule (STYLE-RESEARCH § F): name this sample's hero move and signature device; no hero move used more than
  twice in a batch.

Until this look is locked, **Affan approves the storyboard before the build**, the same as on the pilot.

## 4. Assets

- **B-roll**, in the README § 10 order: show footage → official footage → free stock → official trailers → Higgsfield (credits approved
  first). Into `projects/<job>/assets/broll/`, one file per shot (`b03-old-farmhouse.mp4`), each checked at full size after the 9:16 crop.
  Log every source in BRIEF.md.
- **Fonts:** Anton (captions) and Montserrat Black (hook title), from Google Fonts (OFL), into `assets/fonts/` once, then reused.
- **Music bed:** Epidemic Sound, matched to the story's mood: the no-drums stem or `vocals:false`, fitted to the runtime with `EditRecording`,
  into `projects/<job>/audio/music/`. Mark its phrase accents: a word-led cut that falls within ~0.3 s of one can move onto it, but words decide the cuts.
- **Sticker** (if any): a flat red "!" PNG (`#C90506` → `#9A0204`), made once and kept in the preset's assets.
- **Watermark text:** the show's exact name, as they write it.

## 4b. Receipts and chart data (batch 3)

- **DOC stills**: capture the page as a full still (`workflows/page-record.mjs --full`, or `window-grab.sh` for an app), into
  `yt/assets/broll/`, checked at full size; measure the line to highlight as FRACTIONS of the file (x, y, w, h); log the URL and date
  in BRIEF.md. A dark-mode page takes an underline or a box, not the highlighter (it multiplies). Body text under ~20 px on the card
  is unreadable on a phone: crop the card to the sentence (a "clipping") and stack it on the full page behind it.
- **Chart data**: every number in a `chart` comes from a source logged in BRIEF.md (GATE 5) and printed small on the chart
  (`"source"`); land the draw (`t` + `draw`) on the spoken number.

## 5. Build and render: two passes

> **Current build (2026-10-14): one command, `python kit/yt_build.py projects/<job> <version>`** (README § 13 for the batch-3 keys).
> Before rendering it prints the payoff report (D3) and the cue plan, and stops if a hook card lacks its whoosh + hit pair. The
> kit places the cues of every DOC highlight / stack slap, mark, chart and fx itself (`kit/yt_cues.py`); a spec builder lists only
> its OTHER cues and still asserts their count. The steps below are the original plan the kit implements.

The whips must blur and shift the PICTURE while the captions stay sharp on top, so the picture and the overlays are built separately.

**Pass 1, PICTURE** (`projects/<job>/hf-picture/`, generated by `build.py`):
1. A HyperFrames composition of the shots only: speaker crops (face-tracked, `workflows/face-frame.py` for the boxes), B-roll and SPLITs, with
   the push-ins (README § 7), the SPLIT bob, and the sticker composited behind the speaker's matte (`npx hyperframes remove-background` on
   that shot). No captions, no title, no watermark, no audio.
2. Render it at the base frame rate (`--fps 24000/1001` or `30`) → `work/picture.mp4`.
3. **The whip pass:** apply README § 4 at every cut (`workflows/whip-slide.py`, to be written on the first job: it takes the cut list with
   directions and rewrites only the ~11 frames around each cut) → `work/picture.whip.mp4`. Snapshot two cuts and compare them with
   `board/2-whip.jpg`.

**Pass 2, OVERLAYS AND SOUND** (`projects/<job>/hf-sample/`, generated by the same `build.py`):
1. A HyperFrames composition with `picture.whip.mp4` as its base: captions (Anton, the stretch pop, the wipes, the colour per voice), the hook
   title, the watermark, and any story effect (e.g. a flicker as a brightness toggle on the base video).
2. Audio: the voice from the cut, the music bed at ≈ 13.6 LU under it, the sticker sound. Master to −12 LUFS integrated, true peak ≤ −1 dBTP.
3. Every time is **anchored to words** (the MFM pilot's `build.py` v2 pattern: `at()` anchors, segment-relative patches), so a re-cut moves
   everything with it.
4. `python build.py` → `npx hyperframes@0.8.16 check` → snapshot the risky moments → render → `outputs/<job>.sample.final.mp4`, plus a copy in
   `X:\Claude Projects\Exports\`.

Also apply the shared PLAYBOOK § 5b (the episode's border, burned-in labels, two-up spans, number checks): those traps come from the podcast
source, not from the look.

## 6. Self-check, then Affan's review

Run the multi-lens QA workflow (`projects/mfm-nursery-rhymes/work/qa/onyx-sample-qa-r3.js`, pointed at the new render) with this look's lenses:
- **B-roll:** literal (a viewer could name the noun with the sound off), early (0.3–1.9 s before the noun), sharp at full size, sourced and logged.
- **Whips:** every cut has one; the offsets halve per frame; the mirror seam holds; the captions stay sharp through it.
- **Captions:** chunking, the 3–4-frame lead, the pop, the wipe timing, the right colour for every voice, nothing hidden by a SPLIT seam.
- **Audio:** the bed is continuous and ≈ 13.6 LU under the voice, no word masked, the master at −12 LUFS, the end cut on the last word.
- **Facts:** every name, number and on-screen claim.

Every reported defect goes to a skeptic who tries to refute it. Fix, re-render, re-run: at most 3 rounds, defects only, never taste. Then
Affan reviews it for taste. Every note goes into LESSONS.md the same turn.

## Topaz (Affan, 2026-10-06)
Interpolation on every sample ("it makes the footage very smooth"), Iris only where it visibly helps (≤1080p sources):
`python workflows/topaz-iris.py <base> outputs/<job>.topaz.mov --out-scale 2 --no-stab --segments <every joint + camera cut>` runs
interpolation BEFORE Iris in one pass (Iris makes repeated frames non-identical, so interpolating an Iris file afterwards misses
half of them). Native 4K: add `--no-enhance`. Point `yt/spec.json` `base_hq` at the result; FIT insets of screen captures stay on the
1080p base (text untouched). A take that comes back with a different frame count is redone without interpolation automatically.
