# Abundance Wisdom — LESSONS

One entry per thing a job taught. Newest first. Numbers belong in [README.md](README.md),
procedure in [PLAYBOOK.md](PLAYBOOK.md).

## 2026-10-31 — labels at the bottom, every time (MJ Outthink Them v2 review)

- **Label motion graphics go at the BOTTOM, never the top** ("I told you… Nobody looks at the top"). MJ Outthink, Patrick
  and Kane shipped their cards at y0 230 because their editor briefs say "small, top third"; Conrad's sat at 1262 and was
  right. The rule now lives in README § 8 and beats the brief. → change: MJ Outthink labels moved to the low band (v3).

## 2026-10-14 — MJ "Son told Tyson" raw cut (`projects/mj-skin-son-tyson`, ABW8 Sequence 53)

- **A podcast with a burned-in ad banner** (Hotboxin': TYSONPRO.COM across the bottom 232 px): scale so the 9:16 frame ends
  on the banner's top and lift the Motion y (226.5 %, y 0.637); `plan_placement.py`'s `border` is symmetric (it would crop
  the top too), so the job carries a `fix_placement.py` post-pass.
- **"Stop dead after X" is tested from both sides:** when the next word follows within 20 ms, transcribe what FOLLOWS each
  candidate cut (from 432.81 Whisper heard "He was changing…", from 432.97 only "…changing"): that, not the RMS dip, places
  the boundary.
- **A file name is not the episode:** the bin's "Prince Jackson Opens Up…" was another interview; check by its words before
  building on it.
- **A brief's runtime is an estimate:** the locked words of this one run 38 s against a 50–55 s target; report it, never pad.

## 2026-10-13 — CBum "Born With It" raw cut (`projects/cbum-born-with-it`, ABW8 Sequence 52)

- **A cut sheet written from YouTube auto-captions carries their mishears:** the "name after 'the doctor'" ("Larry") is the
  word "literally"; one of beat 8's two "f-words" is "shit". Every word is settled from the bin copy's audio, and the
  differences go back to Affan (the sheet asks for that in B9).
- **No sequence handed over → clone an EMPTY one of his** (Sequence 48: 1080×1920, 60 fps, v3/a4), name it the next free
  number (Sequence 52), new bin named after the job; never lay into his own empty Sequence 48/49 (they may be reserved).
- **A source's OWN inserts sit inside kept lines** (CBum's shin-press clip under "woke up the next day", his burned-in
  "WARNING PICTURE IS NASTAY..." under "by the time I got home"): kept as his footage, flagged, never silently covered.
- **WhisperX can park a word a second early across a crying pause** ("I" at 620.37, spoken 621.50, before a camera cut):
  measure the onset with 20 ms RMS before trusting a start that lands next to a cut.
- **"Do the captions AND the colouring, some layered"** (Sequence 52): Premiere still cannot colour words by script, so
  the coloured, stacked layer is RENDERED as his caption export (the file he takes to CapCut) with the code-trial engine
  (`projects/cbum-born-with-it/captions/render_caps.py`): captions.txt `+` = a stacked second line (+65 px, the caption
  above holds to the pair's end). His caption base moved: line-1 cap top y1022 on ronnie.mov (Seq 46) vs 1031.75 on
  peace.mov (Seq 28); measure the latest export before each render.
- **Sheet runtimes are estimates:** "68 s with everything" came to 57.95 s after the measured tighten, so neither of its
  runtime cuts was needed.

## 2026-10-12 — letterbox look on comp 65 (Ronnie Coleman, `projects/ronnie-coleman-truths/letterbox`)

- **His current letterbox build (comp 60, 4 instances) differs from README § 5's older one:** the line precomp is
  `White Solid 1 Comp 1` (white solid Scale [100, 1] at y1497 inside a 2.92 s 1080×1920 comp), each bar layer at
  **Scale [202, 100], Position x 1086**, so line y = layer y + 537; bars sit **above** the grade adjustment layers
  and below the zooms; twins at 184–256 % (2–22 % past the fill scale) and **33–63 %** opacity (median 47); masks hand
  drawn, x bleeding 56–92 px past each side, edges on the band or up to 12 px inside. → PLAYBOOK § the letterbox pass.
- **Copy his bar with `layer.copyToComp(comp)`** instead of rebuilding Deep Glow: every plugin setting comes across.
  Find the new layer by `layer.id` (not "index 1").
- **ExtendScript: property objects held across `layer.duplicate()` / `moveAfter` go stale** ("invalid numeric result"
  on read-back). Re-fetch the mask by name before reading it back.
- **His caption layer travels from short to short** (comps 47 and 60 carry the SAME Turbulent Displace Evolution keys:
  0 → 9197.8 at 50.967 s → 6139 at 52.517 s). On a short past ~51 s that is a fast backwards wiggle, then none. Build a
  new caption layer by copying his (`copyToComp` + `replaceSource`, `projects/ronnie-coleman-truths/captions/capcut/
  place_caption65.jsx`) and flag the Evolution keys whenever the short runs past 50.97 s.
- **Fuchsia (13) relabels a block for this pass, which is NOT a transition colour:** run the letterbox pass after the
  transition pass has read the labels, and never re-run transitions over a fuchsia block unasked.

## 2026-10-11 — the caption wiggle is BROAD and SLOW (his review of the code-rendered short)

- **"Captions have way too much wiggle"**: his Turbulent Displace (Amount 4, Size 100, Complexity 1, Evolution ~180°/s)
  measured on his export moves whole words together: ~2 px rms, correlated over ~100–150 px (letters 30 px apart move
  as one), changing over ~0.4 s. A fine noise field of the same strength reads as jitter. Any code rebuild of his
  caption chain uses the measured field (`projects/aw-code-trial-parents/render/aw_render.py` `turbulence`).

## 2026-10-10 — head lock comps 55–59 + captions Sequence 40 (`projects/nutcase-shark-tank`, Shark Tank / Nutcase)

- **A speaker who laughs his way OUT of the frame must not be chased.** The tracker keeps finding the face at the edge,
  and the lock then swings the frame 500–800 px (most of it Motion Tile mirror). Lock until the unlocked nose passes
  the crop edge, then HOLD the last anchor (`track.json` `held_from`; raw kept in `track_raw.json`). Comp 56 L2 from
  frame 118, comp 59 L4 from frame 100. Earlier jobs topped out at ~300 px x / ~160 px y; flag anything beyond.
- **`headlock_proof.py jsx` wrote nothing with a relative output path** (AE resolves it against its own folder): the
  tool now makes the path absolute.
- **A multi-speaker pitch (Shark Tank):** upright = the sharks (the short's wisdom and punchlines), italic = the founders
  pitching/answering, read off the shot list (who is on screen per comp layer) and the uncut source.

## 2026-10-10 — captions rendered from TEXT, matched to his Premiere render (code trial, `projects/aw-code-trial-parents`)

- **The "Revised Light pop" is stretched to each caption's duration** (preset applied with scaled keys): on every
  graphic of Seq 28 the Graphic Group Scale runs 100 → 105 at 13.6 % of the clip (linear) → 112 at the clip's END
  (eased in). A short caption pops fast and a long one slowly, so the fixed-time `POP` table in `build.py` can never
  match more than on average (~2 % off mid-pop). Exact curve: `projects/aw-code-trial-parents/render/cap_pop.py`.
- **His caption font size is 48.0** (a float in the Source Text blob), tracking 0, with the font's GPOS kerning
  (Metrics). PIL without raqm (this machine) ignores GPOS: AY/AV/WA/LY pairs come out ~5 px wide each. Read the pairs
  with fontTools (`render/kerning.py`). PIL `getbbox()` on a single glyph returns the advance box, not the ink.
- **The second line's offset is per caption**: each V5 graphic carries its own Motion position (+63 / +65 / +67 px
  under the V6 line in Seq 28). Read it, never assume one pitch.
- **CapCut returns the caption layer 6 frames late**, and its Motion Blur (blur 0.81, multiple 6, bilateral) only
  shows at caption changes: an optical-flow smear between the two layouts over ~4 frames either side of each cut.
  That smear is part of his look in the final. Model: `render/capcut_blur.py`.

## 2026-10-06 — Sequence 30 (Martin Fitzwater vs Nick): head lock comps 50 + 52, captions

- **A sequence can carry parked clips past the short** (Seq 30: the short ends 53.32 s, raw leftovers sit at 121–226 s
  after a gap). Caption only the short: trim the read reference at the end of the first contiguous run before
  transcribing (make_plan consumes every transcript word).
- **A cut that joins two words fools both decoders the same way** ("I went as far as blocking" → "I wouldn't start as
  blocking", beam 1 and beam 5 agreed). Agreement between decodes of the CUT proves nothing: decode the UNCUT source
  around the joint, then fix words.json `_fixes` with times from the RMS.
- **When a commentator reads a comment on screen, the screen settles the words** ("Nick responds and says very" = his
  Instagram reply "very", visible in the frame). Quoted comment + reply = italic; the commentators themselves upright.
- **Scale-100 layers of 1920×1080 footage in the 1080×1920 comp are letterboxed:** left unlocked and asked (comp 50 L3–L4).

## 2026-10-05 — zoom pass on ABW8 Linked Comp 46 (Nick Walker parents, 19 blocks, ABW9.aep)

- **Two-shot reaction blocks need a SIDE pivot, decided per block from the full frames:** a pull-out's deepest
  frame is its FIRST (block 5: Nick at x 0.02–0.20 → pivot x100), a push-in's is its LAST. Remember the region a
  pivot keeps is NOT centred on it: at depth Z the source x range is `[c(1−Z), c + (1080−c)Z]`, so to keep
  x0..x0+1080·Z the pivot is `c = x0 / (1 − Z)` (block 17: keep 0.10–0.80 at Z 0.70 → c = 360).
- **Two faces wider apart than the crop:** keep the one whose face is whole-able (mom, crying) and the other's
  profile front (eyes + nose); never split both faces down the middle. Said in the report.

## 2026-10-04 — the creator's recut of Sequence 28: head lock (ABW9 comps 40–44) + captions

- **The creator recut after the sequencing:** beat 5 came BACK ("My parents have been with me…", plus "Second year in
  a row, I'm gonna miss the Olympia" from `'24 Olympia Announcement.mp4`), the reaction tail went, finals footage
  became picture under the VO, and cutaways of his MOM and DAD (listening) were framed from the interview. Comps and
  the sequence were READ, never assumed from the sequencing plan.
- **Head lock in `ABW9.aep` (new project file), 17 of 17 layers locked, incl. the parents' listening cutaways** (a face
  in footage the creator framed; the "speaking shots only" rule is about overlays and stills). The 4K interview at
  Scale 100 / 156 is a zoom-in, not letterboxed: locked like the rest. Proof from AE's read-back keys: worst drift
  0.023 px. Profile shots: the YuNet nose dot sits just past the tip, a constant offset that does not hurt the lock.
- **Captions with an AI voice-over on A2:** `sequence-captions.py read` mixed A1 only, so the narrator would have
  had no captions. → `--voice A1,A2` (PLAYBOOK § 4). Narrator italic (as Seq 23); Greg Doucette's quoted insult
  upright like the commentators, split from the narrator's "being called a" at the speaker change.
- **A word the two decoders disagree on ("Everyone says/said"):** a beam-5 context re-decode + the creator's own script
  decide; the fix goes in words.json `_fixes`.

## 2026-10-04 — fifth sequencing job (ABW8 · Sequence 28, `projects/nick-walker-parents`)

- **The AI voice-over can already be ON the sequence (A2, ElevenLabs, cut in pieces) and "re-sequence the VO to the
  script" means: hold each VO line's slot as a placeholder beat of EXACTLY its pieces' length, then shift the later
  pieces by the clips placed before them** (`trackItem.move(seconds)`, relative, last piece first so nothing overlaps;
  in/out kept). → `place_sequence.py` now only refuses when the tracks it lays onto (V1/A1, +V2/A2 with covers) hold
  clips, and proves the creator's other clips untouched after (PLAYBOOK § 0).
- **"Put all the source material in the new bin":** every source is laid from the job's bin. A file that already sits
  in an older job's bin is imported AGAIN into this bin (same file on disk, no second download) and that item is laid,
  so the older bins stay as they were. → `place_sequence.py`.
- **Check the disk before downloading.** Of three YouTube sources, two were already local (matched by yt-dlp title +
  duration without downloading); one of the local finals had a second copy in another job's broll — the one the
  project already used was taken.
- **"Let the reaction play, cut before the interviewer"** = an untouched segment (`tighten: false`) anchored on the
  last spoken words with a measured `in`, split for framing where the subject changes (dad's hug, then mom's) — the
  speech before it stays tightened as its own segment.
- **Beat 5 "drop first if over 58 s"**: dropped (53.3 s without, ~62 s with) and kept under `beats.json` `_dropped`
  with its anchors, plus a note on the B4 marker.
- **A ranged marker (BLEEP over a swear):** `marker.end = <seconds number>` works; assigning a `Time` object fails
  the whole evalScript AFTER `createMarker` already ran (a duplicate marker was left; deleted). → lanes/premiere/lab-notes.md.
- **`placeholder_note`** on a placeholder beat now becomes its marker comment (was a hard-coded "arrest footage" note
  from an earlier job).

## 2026-09-29 — fourth sequencing job (ABW8 · Sequence 14, `projects/paris-jackson-masks`)

- **"Open on her face while she listens" when the source never shows her listening → a V2 cover.** The CHD question
  is wide, Alex, wide, Alex. A beat's `"cover"` in `beats.json` is now a picture-only V2 insert (resolve_beats →
  edl `covers` → plan_placement track-2 row → place_sequence removes its A2 audio). Pick the face by transcript AND
  frames: of 20 short Paris cutaways only one was truly silent, and she was smiling at a compliment; the one used is
  her silent think right after Alex's NEXT masks question (same topic, same tone).
- **In-points floor to the SEQUENCE grid (1/60 s here), not the source grid.** 20/20 clips from 23.976 and 25 fps
  sources landed on 60 fps multiples, 0–13 ms early. The 2026-09-23 "source grid" reading came from 29.97 sources,
  where both grids coincide. Never predict the floor: the placer now reads the in-point Premiere took.
- **Camera-cut splits are RAZORS on one placed clip**, the frame computed from that actual in-point and the cut:
  audio continuity 0.00 ms at all five, every clip's first and last frame inside its shot. The old both-grids search
  cannot work at 23.976/29.97 (the grids meet every 16.7 s): it drifted a split up to 1 s late and ran one piece
  past its segment. Two razors planned from the plan's in-point sat 4–5 ms before their cuts (a frame of the wide in
  Alex's crop); a cover ending on the source's own cut is re-pinned the same way.
- **"If it doesn't land by ear" is tested IN CONTEXT.** Paris's closer runs straight on from "…scary" (no pause, the
  in-point on a 3 dB dip). Isolated, Whisper heard "I always felt protected" (p0.33, "you know" lost); joined after
  Debbie's last line it read every word. A one-second slice is not an ear.
- **A breath inside a long pause leaves a wordless tightened piece** (0.32 s at −36 dB between "looking at" and "a
  piece of paper"): split the segment at the pause instead.
- **Check a broadcast source for burned-in titles inside the beat**: "Michael Jackson's Camera / Interview in
  Florida" runs 4.2 s under Michael's line, partly in the crop's bottom band; "DEBBIE ROWE" had faded before hers.
- **The creator rejected the "thinking, looking down" cover: a listening shot means eyes ON the host, mouth closed,
  while the HOST speaks.** Found by a voice classifier (MFCC stats + logistic regression, taught by the camera since
  the podcast shows the speaker: 91 % agreement; Alex's questions score 0.03-0.07 "Paris") crossed with the Paris
  shots: 15 real listening windows in 72 min, none over 2 s. Mouth-motion from YuNet landmarks could NOT tell talking
  from listening (0.035 vs 0.026). Tools: `projects/paris-jackson-masks/brief/tools/`.
- **`setInPoint` floors TWICE: to the source frame, then to the sequence grid.** A 23.976 shot starting at 2105.7286
  can only be entered at 2105.7167 (the frame BEFORE the cut) or 2105.7667 (a frame late). The exact first frame is
  reached with the razor: lay one frame early, razor at frame 1, delete the head, `move(-1/60)`. Proven on the
  Program monitor: timeline frame 0 went from the Alex frame to Paris.
- **Program-monitor grabs lag one playhead move.** Set the playhead twice, then grab, and judge by correlation
  against frames extracted by exact pts (`-copyts` + `select=between(t,..)`); `-ss` seeking landed a frame off.
- The bin was named "Pairs Masks": find bins by their content, not the exact name.
- **Zoom pass, comp 30: a portrait painting is a "confident face".** The Call Her Daddy wall portrait (y 2–100)
  outranked Alex in the wide, so the top-most-face rule pivoted both wides at y200, pushing in toward the painting.
  `zoom_pass.py` now reads `<work>/centers.override.json` ([{start, center_y, why}]); the plan prints MANUAL.
  Preview every pivot that lands on y200: it is either a face at the very top or not a person.
- **The face check only guards the TOP edge; a deep push can cut a face off the SIDE** (comp 34, 2026-09-30): in a
  4.5 s block the camera follows Nick right, and at 0.70 about x540 half his face left the frame at the block's end.
  The override now takes `center_x`; x1000 kept him whole in all 8 full-depth samples. In the preview, check faces
  near the left/right edges too, not just the red line.
- **Who says what in crosstalk: compare voices WITHIN the recording** (Seq 19 captions, 2026-09-30). A studio
  reference of Nick (Olympia TV) against the press-conference PA mic scored everything near 0 (room + mic mismatch);
  pyannote `wespeaker-voxceleb-resnet34-LM` embeddings of the press-conference lines against each other split two
  voices cleanly (0.4-1.0 vs 0.0-0.1), anchored on a line whose speaker is certain from the content. It reversed my
  text-only reading of who said "I still don't know who you are". Runs in the whisperx venv, no token needed.
- **Speech under music is where WhisperX drops words** (Seq 23, Kanye's play-off at the 2008 GRAMMYs): 12 s of his
  protest were missing. Re-decode each A1 clip with ±2.5 s of source context (faster-whisper, no VAD) and keep the
  words whose midpoint is inside the clip's in/out; a word straddling a seam is partly audible and stays, a word
  that ends before the in-point goes (the leading "I"). `make_plan.py --hang 0.8` now keeps captions off a long
  music stretch (opt-in; the default stays wall to wall). The narrator voice-over was captioned in italic.
- **"No face" on a bowed head behind sunglasses means centre pivot, and the glasses get cut** (comp 39, a 0.70
  pull-out): measure the face on the block's first frame (glasses top → chin) and pin its centre in
  `centers.override.json`. Every "no face" block in the preview gets this look.
- **The transition pass read a SOLID as a footage block** (comp 39, "Black Solid 1" 2.88–11.58 under the narrator): it
  started with the next block, so that block's cut moved onto 2.88 (a doubled dip, none at 6.33). Blocks are now
  only FootageItem layers that are not solids (precomps like "Pre-comp 1" are skipped too).
  → `transition_pass.jsx.tmpl`. Read the transition log's "cut at" against the block list every run.
- **The head tracker sampled the wrong frames.** `-ss in` + `fps=60` drops the frame straddling the in-point and
  takes the NEAREST source frame, while AE shows the frame at or before; at 23.976 the track ran up to a frame ahead
  of the picture and read the next shot's face on a clip's last frame. `head_track.py` now decodes with real
  timestamps (`-copyts`, bounded by `-t`: `select` alone decodes to end of file, 15 min instead of 11 s) and picks
  frames as AE does. Earlier locks (29.97/24/60 fps sources) were at most a frame early, never across a cut. Whisper drops the LAST word of a
  file with no trailing silence (pad 0.8 s before judging an ending).

## 2026-09-27 — zoom pass on ABW8 Linked Comp 25 (Nick Walker, 20 blocks, one Topaz render)

- **The face picker took the biggest box, and on bodybuilders the biggest box is not the face.** YuNet fires on
  torsos, glutes and knees at 0.53-0.84; the real stage face (0.88-0.93) is smaller. Block 4 (side pose)
  read the glutes at y1006 and kept the centre pivot, which would have pushed the real face (top y191) to y56.
  On the stacked split (Fouad top, Nick bottom) it protected Nick, the bigger face, and the 0.70 pull-out cut
  Fouad's face off the top. `zoom_center.py` now drops posters, protects the TOP-most confident (>= 0.8)
  face, and falls back to the largest box when nothing is that sure.
- **Checked against the earlier comps before running:** the Eminem and MJ zoom frames (66 samples) give the
  same pivots as shipped. The first version fell back to the top score, and a 0.74 hat brim beat a 0.72
  Eminem close-up; the regression check caught it. Re-run that check after any change to the picker.
- **Accepted false hit:** Nick's raised fists (0.83) sit above his face on the arms-up shot, so block 18
  pivots at y200 instead of y420. Pivoting higher only moves the real face further from the top edge, so the
  cost is a tighter bottom, not a cropped face.
- No doubles, glow bars or caption precomp in this comp: 20 zooms on top, 13 face pivots, read back exact.
- **Between the zoom and transition passes the creator added** the caption back (`nickkk.mp4 Comp 1`), a
  Lavender `Adjustment Layer 34` sharpen per block, glow bars on 3 blocks, turned one block into a double (169 %),
  and switched the zooms/glow bars/caption OFF (preview speed). Three yellow blocks stayed yellow = no
  transition (fast posing cuts). The transition pass read 20 blocks correctly; nothing of theirs moved.
- **The caption came back UNCLEANED** (`Caption Exports/nickkk.mp4` went straight into AE). `clean_capcut.py` fixed 17
  frames of the known ~40 % lift (5, 119, 239 ... every ~2 s; 5 min 19 s for 39.7 s of 4K) and found a SECOND,
  milder pattern: frames 601-749, 1201-1349, 1801-1949 (the 2.5 s after every 10 s mark), 1.3 % of pixels each,
  CHROMA only (luma unchanged), in a band around the caption line (rows 2046-2128): encoder colour ringing next to
  the text. Neutralised with the same mask; the text itself is never touched. Worth a look on the next export.

## 2026-09-27 — the creator's caption edits on the Eminem short (data, read off `hailieee.mp4`), applied on Seq 09

Compared caption by caption with my Seq 08 SRT (all 57):
- **Green Shade is now in use** for success / money / career: CAREER, MONEY, SUCCEEDED (I had yellow or red). → README § 8.
- **Much less colour:** ~19 of 58 captions coloured (mine: 27+). Most of my reds went white (LIVE, FAIL, NEVER KNEW
  HIM), numbers went white except 3.9 (pink). → README § 8 density line.
- **Spoken forms:** "GONNA" where he says gonna (the transcript had "going to"); tiny flash captions ("GOING TO",
  0.22 s) folded into the next line.
- **Two-line builds** (OF DRIVE / AND MOTIVATION, FROM COLLEGE / 3.9) and one 4-word caption to keep a phrase whole.
- **No italics** on the other speakers' questions this time (one data point; the README rule stands until it repeats).
- **An annotation line** under the stinger: "*TALKING ABOUT HIS FATHER*" with HIS FATHER in light blue.
- **They captioned a fragment I had dropped** ("YOUR GIRL" — Whisper's full-context "Girl," was right; my isolated
  re-listen said "No"). → When a full-context pass and a short isolated slice disagree, flag, don't drop.
- Tooling: `make_plan.py` / `make_srt.py` now accept `<green>` → the creator's "Green Shade" style.

## 2026-09-27 — third sequencing job (ABW8 · Sequence 09, `projects/nick-walker-olympia-win`)

- **The frame check caught TWO misattributions in one sheet.** Beat 2's "He will never win the Mr. Olympia title"
  (Greg's video, 6:38) is Nick's own coach on camera, voicing what critics would say. Beat 4's "he'd be fighting
  for 10th place" is the VOB host, not Shawn Ray (the host says "Sean" seconds earlier; Shawn only says "That's
  true"). **Check who is on screen AND who is being addressed, for every quote, before placing.** The sheet's own
  alt fixed beat 2; beat 4 is flagged.
- **A reaction video's "quote" may be the clip it reacts to.** Read the words around the quote ("Nick and I…",
  "rather than that, I'd rather…") before trusting the attribution.
- **A split inside one continuous 29.97 fps clip can only land where the 60 fps grid and the source grid line up
  (~every 16.7 s).** `plan_placement.py` moved a 4136.4 split to 4137.395. If the crop can cover both halves, drop
  the split instead. *(Fixed 2026-09-29: splits are razors now, exact at any source rate.)*
- **A long "pause" before an announcement is usually crowd roar, not silence** (−19 dB): trim it by hand, since the
  RMS tightener correctly leaves it.
- **Whisper invents a leading word on an assembled cut** ("If Nick Walker's…", "Girl, how old…"): re-hear the first
  second alone before believing it.

## 2026-09-26 — the "black static" frames: ROOT CAUSE FOUND (months of manual frame-cutting)

- **Symptom (every short for ~6 months):** about 10 visible one-frame flashes per export of a dark diamond mesh over
  the whole picture. The creator's workaround: razor the bad frame out in Premiere, then slow a nearby block to
  99 % to close the one-frame gap.
- **Cause: CapCut's caption export, not the edit.** The 4K HEVC it writes (~4 Mbit/s) lifts the black background on
  ONE frame every ~2 s: frames 5, 119, 239, 359, 479, 600, 719 … (every ~120 frames at 60 fps), identical in every
  export checked (hurt2, hailieee, wacko 2, untrue). On those frames luma goes 16 → 17 on ~35 % of pixels and
  chroma drifts to 126–131 (pure black is 128). When one lands on an HEVC keyframe (600, 1200, 1800, 2400) the noise
  also carries, faintly (~1.3 % of pixels), into the frames that reference it until the next keyframe, 2.5 s later.
  The file that goes INTO CapCut is clean.
- **Why it shows:** in AE that "black" is keyed out and the caption stack (Deep Glow Unmult → Bevel Alpha → 2 × Drop
  Shadow at 255 → Sharpen 70 → Turbulent Displace) turns a 1–3-level field into a visible mesh across the frame.
  Proved on `Hurt Finall.mp4`: every one of the 25 predicted frames breaks from its neighbours (959 and 1439 show
  the mesh; the difference image is the diamond grid).
- **Fix: `clean_capcut.py "<CapCut export>"`, run on the file BEFORE it goes into AE.** On the dirty frames only, pixels
  that are black in both neighbours and faint here go back to pure black; caption pixels are never touched.
  Verified on hurt2.mp4: 617 dirty frames → 0; captions within 0.4 levels on every frame; same frame count and tags.
  The manual frame-cutting is no longer needed.
- **Encoding gotcha found on the way:** a raw pipe into ffmpeg has no colour info; tag the INPUT exactly like the
  output, or ffmpeg converts (it read the pipe as BT.601 and shifted every coloured caption ~13 levels).
- My first glitch detector (downscaled grey frames) saw nothing: a fine mesh averages away. Detect it at full
  resolution, on the source layer, not the export.

## 2026-09-26 — transitions on comp 18 (16 from the creator's labels)

- **The transition template had the same doubles bug the zoom pass had,** with a worse symptom: the
  twin sorted as "the next block", so the cut read as the double's OWN start, and it would have
  produced two transitions at the wrong frame. It now merges same in/out layers first. Any pass that
  walks "blocks" must group doubles.
- **The caption came back before the transitions** ("hailieee.mp4 Comp 1", Sharpen + Turbulent
  Displace, on top of the zooms). Order in the finished comp: caption → transitions → zooms → glow
  bars → Adjustment Layer 32 (sharpen/look).

## 2026-09-26 — zoom pass on a comp with doubles, glow bars and stills (ABW8 Linked Comp 18)

- **"Double layers" = one shot.** The creator's aesthetic stacks a 100 % layer over a 198–229 % twin
  with the same in/out (both yellow, or both default). One zoom goes above the pair; the smaller copy is
  the one the face check reads. `zoom_pass.py` now groups by in/out explicitly, and a group pulls out if
  any of its layers is yellow.
- **The template took a glow bar for the caption layer.** Its caption test matched "Comp 1", and the glow
  bars are "White Solid 3 Comp 1" precomps. The zooms would have gone in between the two bars of a pair.
  Glow bars are now skipped; with no caption in the comp, the zooms go on top (README § 2 stack).
- **Stills in the build comp** (Higgsfield .png at 150–165 %) get their layer transform passed to
  `zoom_center.py` as `map`, so the face check measures them where they sit in the comp.
- **A relative work dir silently does nothing in AE** (it resolves paths from its own install folder):
  `zoom_pass.py` now makes the work dir absolute.
- Six blocks came back "no face" (B&W profiles). Preview every block at its deepest zoom
  (`projects/eminem-hailie/zoom/preview.py`, stills placed as the comp places them) before running.

## 2026-09-26 — the creator's recut of Sequence 08, and its captions (data)

Measured from the live Sequence 08 before captioning (`projects/eminem-hailie/captions/brief/tracks.txt`):
- **They added the 60 Minutes stinger back** ("I never knew him… Never met him, never knew him", 35.1–39.3 s),
  even though the paste stopped at beat 4. So the paste is what to sequence first, not the final word.
- **They replaced the whip-pan under Tyson's question** with a clean Eminem close-up from 3:34 (206 %), and
  put music-video B-roll on V2/V3 and a slowed music bed on A2. The weak broadcast shots I flagged were acted on.
- **They kept some of the pauses I had cut** ("I have … a niece"), took "that's kind of like a daughter" over
  "pretty much like a daughter", and dropped "so" before "when I think". 36.7 → 39.3 s.
- **Captions on a recut: re-transcribe the SEQUENCE audio** (`workflows/sequence-captions.py read`; ~40 s of
  audio) rather than moving the source transcript through A1. The source transcript was already known to drop
  fillers and mistime numbers. The re-listen caught a 0.25 s fragment of Tyson's "I know" that reads as a word.
- The Program monitor's timecode does not repaint in a background window grab; the picture does. Check a
  caption against the picture, not the readout.

## 2026-09-26 — second scripted head lock (ABW8 Linked Comp 07–13, ABW7.aep)

- **The comps are the truth, not my sequencing plan.** The creator recut before "Replace with AE
  Composition" (20 clips instead of 32, one new clip at 206 %). Read the layers straight from AE
  (source, in-point, scale, position) and track those.
- **Hold the nose at its MEDIAN, not at frame 1** (`apply_headlock.py --hold median`, now the default).
  The creator's crop is set on the playing clip, so a head that moves early parks off-centre under a
  frame-1 hold (comp 10 L1: x 180 vs 421). Position stays untouched either way.
- **A border baked into the source + a lock = the border slides in, and Motion Tile mirrors it.**
  At fill-height scale there is 0.5 px of clean margin. Fix without changing the framing: a
  Transform effect "Border out (Claude)" (per-axis scale that pushes the border out of the layer)
  BEFORE Motion Tile, with the layer Scale divided by the same factors (`"prescale"` in the map).
- **AE scripting: adding or moving an effect invalidates every property reference already held**
  ("Object is invalid"). Look each one up again after any structural change. The applier is
  idempotent (clears keys, sets absolute values), so a failed run is fixed by running it again.
- The ffmpeg `-ss` grab in the check sheets shows the NEXT frame at a clip's last frame when a camera
  cut follows; AE shows the previous one. That is a sheet artifact, not a flash.

## 2026-09-25 — second sequencing job (ABW8 · Sequence 08, `projects/eminem-hailie`)

- **Sequence from what the creator PASTES, not the whole Content Engine file.** The MD held six drafts and
  a stinger; the creator: "do the sequencing that I've sent you". Read the MD only to locate lines.
- **Pause removal is now built into `resolve_beats.py`** (`"tighten"` in beats.json): cuts are placed at
  measured silence against the clip's own room tone (10th percentile + 6 dB), keeping 0.10 s after
  and 0.06 s before, removing any pause ≥ 0.13 s. This is the 2026-09-23 recut lesson, applied
  automatically: 14 pauses, 10.3 s on a very slow 2002 take.
- **WhisperX silently drops fillers and mistimes spoken numbers:** "my main *like* source", "Haley is
  *um* 23", "3.9" given 0.2 s, "point nine" labelled as Tyson's "Wow". **The proof that catches it:**
  rebuild the audio from Premiere's READ-BACK in/outs and re-transcribe it. That caught the "like"
  after the cut was already placed.
- **Camera cuts in the silent tail of a clip become its edge** (`sources.json` `"cuts"`, from ffmpeg
  `scdet`); otherwise the 60 fps round-up shows 1 frame of the next shot.
- **Channel frames baked into a source** (Mike Tyson's official uploads: a 26/30 px red frame) are
  scaled out (`sources.json` `"border"`) → 187 % instead of 178 %.
- **The face detector fails on B&W profiles and listeners** (9 of 17 Tyson clips). Set those by hand
  in `framing.json` from ruled frames, and always check a contact sheet of the actual 9:16 crops.

## 2026-09-24 — transitions by label (ABW8 Linked Comp 06)

- **The creator labels for transitions AFTER the zoom pass, and relabels yellow pull-out blocks too**
  (no markers used). So the order is fixed: zoom pass first (reads yellow), transitions second (reads
  the new labels); after that the labels no longer say which blocks pull out — `apply.tsv` does.
- Now a reusable tool: `transition_pass.py "<comp>" <out.jsx>` (template `transition_pass.jsx.tmpl`).
  8 transitions built and read back on the first run.

## 2026-09-24 — zoom pass on the Topaz render (ABW8 Linked Comp 06)

- **The creator called it "Linked Comp 08"; the project has no 08.** The comp holding the Topaz render
  with yellow/default labels was 06 (the active comp). Check by content, say which one was used.
- **In the build comp the blocks are the creator's, not the cuts:** 11 blocks, one 16 s block
  (13.92–29.90) spanning several 60 Minutes cuts → one zoom, depth 0.67. AE label 3 (Aqua) is the
  default footage label = push in.
- **The Topaz render blurs 2–4 frames at EVERY cut** (33 frames over 10 cuts; the export is sharp
  there, and the frames before a cut soften too). Enhancement-only and Chronos-only renders of the same
  cut stay sharp, so by elimination it is the **Full-Frame stabilisation** smoothing across the edit.
  The AE head lock already holds the faces, so stabilisation adds little — flagged to the creator.
- The first zoom plan sampled the cut frames → 2 "no face" and one false pivot. Sampling 0.1 s inside
  each block fixed all three.

## 2026-09-23 — Topaz settings matched to a competitor frame (ABW8 hurt.mov)

- **Focus fix is the lever, not the sliders.** On footage blown up 180–270 % (60 Minutes 960×720 at
  267 %), the frame only holds ~⅓ of its pixels of real detail; Strong (25 % → 4×) lets Iris rebuild at
  the scale the detail actually lives. Standard left it soft.
- **A second pass at 1× (Proteus, detail 60 / sharpen 60) adds the crisp edges** Iris won't give
  (pushing Iris's own sliders made it softer). Costs ≈ 3× the enhancement time. Numbers → PLAYBOOK § 3.
- **A reference frame from a competitor is GRADED; ours is compared before the creator's CC.**
  Normalise contrast out before measuring (creator's correction, same day). Raw numbers said "the
  source can't get there" (5.1 vs 8.5); normalised, two passes already match the competitor's edges,
  and the grain I'd recommended doubled their texture — so grain came back out.
- Topaz here is **5.0.4**: no Rhea, no Starlight (the newer models for very low-quality footage).

## 2026-09-23 — captions on a sequence Claude built (ABW8 · Sequence 03)

- **Creator: "max 3 words per layer."** Earlier guidance allowed 4 on fast lines; on this job 3 is a
  hard cap (66 captions at 218 wpm, median 0.70 s). Treat 3 as the cap unless told otherwise.
- **No re-transcription for a sequenced job:** `timeline_words.py` moves the per-source transcript
  onto the sequence clock through the live A1 clips (read AFTER the creator's recut — the audio still
  points at the sources even when V1 was replaced with AE comps). A clip outside every transcribed
  window gets its own short extract, transcribed once and merged.
- **Trim slivers:** a cut can leave a 20–40 ms prob-0 word at a clip EDGE ("anything, it | It is");
  drop it. Short prob-0 words MID-clip are real ("in a bed", "harm a child") — an edge-blind rule
  dropped both on the first try.
- **Italic also covers words Michael quotes from someone else** (the police remarks), as on the
  Destiny job — flagged to the creator as a choice they can flip.
- `make_srt.py` had "captions 1–11" hard-coded from Sequence 22 in the cheat-sheet; it now lists the
  real italic runs.

## 2026-09-23 — first scripted head lock (ABW8 Linked Comp 02 + 03, ABW7.aep)

- **The creator's handoff for the head lock: they "Replace with After Effects Composition" over the
  Iris (default-label) clips; Violet clips are never locked.** The linked comp keeps Premiere's scale
  (88.9–266.8 % here, not the 546 % of the reference short), and the lock works on it directly.
  → PLAYBOOK § 2.
- **Pipeline:** `head_track.py` (YuNet nose, every 60 fps frame, from the source files) →
  `headlock_map.json` (comp/layer → clip, with the comp's sequence offset) → `apply_headlock.py`
  (per-frame linear Anchor keys + Motion Tile 340/mirror, one undo group) → `headlock_proof.py`
  (read back from AE, rebuild frames, locked vs unlocked sheet). 21 layers, 2,513 keys, one run.
- **The lock is framing-independent:** Anchor(t) = Anchor(0) + (nose(t) − nose(0)), Position
  untouched — so the creator can re-slide Position afterwards and the nose stays held.
- **Never judge a lock by re-detecting the nose on the blown-up comp frame.** YuNet's anchors stop
  around 256 px; on a 750 px face the landmark wandered 100–230 px and a perfect lock "failed".
  Rebuild the frame from the source + AE's read-back anchors and check the crosshair by eye.
- **A nose lock through a profile turn holds the nose, not the face** — the face swings around it
  (60 Minutes 22.3–23.5 s: ~40 px residual vs ~120 px unlocked). Expected, same as AE's tracker.
- **Check the tracked face is INSIDE the crop.** A clip the creator added (60 Minutes wide shot) had
  Michael outside their crop; the tracker still found him at the frame edge. Flag it, don't reframe.
- **`comp.saveFrameToPng` writes nothing on these comps either** (no Sapphire on them) — proof has to
  come from the rebuild, not an AE still.

## 2026-09-23 — the creator's recut of Claude's first sequence (data)

Measured from the live V1 after their pass (`projects/mj-allegations/brief/v1_live.txt`):
- **82.55 → 49.23 s.** Dropped the held arrest gap and the misattributed "his wife" beat, cut
  Elizabeth Taylor to one 3.6 s line ("if they'd planned an assassination…") and the restroom beat's
  closing "it's all right. It's okay."; KEPT both drop candidates (Bashir, and "even though I was
  hurting" at 38.47–41.80).
- **They cut the pauses INSIDE quotes.** Jumps within one continuous source: 0.13, 0.23, 0.27,
  0.27, 0.30, 0.45, 0.48, 0.50, 0.50, 0.58 s, plus 1.08, 1.73, 3.78, 4.07, 6.80 s phrase drops.
  Claude's sequence kept every quote continuous. **Next time: remove breaths/pauses ≥ ~0.13 s inside
  a quote at sequencing** (the head lock + zoom hide the jump).
- **They added lines Claude's draft didn't have** (60 Minutes 573.0 "One time I asked to use the
  restroom." + 575.4 "And they said, sure, it's right around…", Sawyer 974.77 close-up) — the sheet
  is a starting point, not the cut.
- Music added by them, as agreed.

## 2026-09-23 — first job where Claude SEQUENCES (ABW8 · Sequence 03, allegations cut)

- **Pipeline for a cut sheet → timeline**, all in this folder: `find_quote.py` (locate a quote by its
  words), `beats.json` in the job (word anchors per beat, optional measured `in`/`out` overrides),
  `resolve_beats.py` → `edl.json`, `plan_placement.py` → `placement.json` (framing + splits),
  `place_sequence.py` → the ExtendScript that lays it. The placer refuses a non-empty sequence.
- **A cut sheet's timestamps belong to whichever upload the researcher watched.** Every source in the
  bin was a different upload (Katherine at 11:02, not 9:36; Bashir "Part 16", not "10/10"; 60 Minutes
  timed from an excerpt). **Locate by words, never by the sheet's clock.**
- **Frame-check every beat before placing it** — it caught a **misattribution in the locked build**:
  the "Lisa Marie" answer is Elizabeth Taylor on camera. Also verify "no child on frame" at ≥ 12 fps,
  not 6 samples (a hand at the frame edge needed a close look — it was his).
- **The aligner's word boundaries are soft; measure the audio at every edge that matters.** Four edges
  were wrong by 30–200 ms (a stretched "that", an early "it", "anything," decaying 150 ms later than
  aligned). RMS in 10 ms steps settles it.
- **Premiere FLOORS in-points to the source's own frame grid** (29.97 → 33 ms steps) and the pinned
  duration drags the out-point with it — up to 41 ms clipped off a word. Pre-snap every in-point UP to
  the source grid. **A split inside one continuous source must land on BOTH grids** (source fps and
  60 fps), or a sliver of audio is skipped mid-word (16 ms inside "No," on the first pass).
  *(Superseded 2026-09-29: the floor is the SEQUENCE grid; splits are razors from the actual in-point.)*
- **Framing at sequencing = the creator's habit:** scale to fill the 1920 height, slide the crop onto
  the face; split a quote at any camera cut so each shot gets its own crop. The face detector will
  pick the biggest face — in a wide two-shot that was the interviewer, so check which face it found.
- **Sources missing from the bin get searched for on disk first** (the Neverland statement was in
  `C:\Users\affan\Videos`), and anything still missing gets a held gap plus a marker, never a silent skip.

## 2026-09-21 — transitions by block label (comp 06)

- **The signalling rule the creator chose:** label the block, and the label is the transition that
  comes AFTER it. One colour per block, each cut owned by the block before it. It removes the
  ambiguity of labelling pairs. Yellow stays zoom-out; a marker is the escape hatch for a block that
  needs both. → README § 7.
- **Use their own .ffx where the shape matches, and say when it does not.**
  `Simple Brightness Fade In & Out.ffx` and `Music Media Co Uni Expose.ffx` were applied, then
  retimed onto the cut. Their `Gaussian Blur Preset.ffx` ramps UP then down, which is not the
  50 → 0 they asked for, so that one is built directly — and that difference is worth stating
  rather than silently substituting.
- **The cut is where the NEXT block starts, not where this one ends.** They nudge blocks, so block 13
  ended at 31.333 while block 14 began at 31.233; the visible cut is the later layer's in-point.
- **Skip the creator's own annotation layers** (a text layer named `*after his death*`, label 1 Red)
  when walking blocks — they are not shots and their label is not part of the map.
- **Shell gotcha:** writing docs through `python -c` inside bash silently ate every backticked span
  (command substitution). Write markdown with the file tools, not through a shell string.

## 2026-09-21 — creator's review of the first scripted zoom pass (comp 06)

Diffed my 15 zooms against what they left. **9 kept untouched, 4 depths tuned, 2 shots re-timed,
1 curve reshaped.** Nothing was deleted and no layer was re-built by hand.

- **Every one of the 7 face pivots survived unchanged** (y665, 577, 664, 587, 613, 520, 344).
  The `zoom_center.py` rule and the y200 threshold are **validated** — keep them.
- **Depth tweaks, all within ±0.10 of my value:**

  | shot | span | mine | theirs | direction of the fix |
  |---|---|---|---|---|
  | 11.77 | 1.37 s | 0.78 | **0.85** | shallower — they treat ~1.4 s as a TINY block |
  | 13.13 | 3.00 s | 0.70 | **0.80** | shallower — a 3 s shot is not automatically a deep push |
  | 19.57 | 1.73 s | 0.78 | **0.73** | deeper |
  | 21.30 | 6.98 s | 0.70 | **0.67** | deeper — confirms 5 s+ goes past 0.70 (their measured median 0.68) |

  → **Bucket edges to use next time:** tiny (≤ ~1.4 s) 0.85–0.87 · standard 0.78 ·
  long 3–5 s 0.70–0.80 · very long (5 s+) **0.67**. The spread on the 3–5 s band means length alone
  does not decide it; ask, or leave 0.70 and expect a tune.
- **Two shot boundaries nudged** (6.02 → 6.00, and the pull-out 31.33 → 31.23, 0.1 s earlier).
  Zoom spans are theirs to fine-tune; do not re-derive them from the footage layers after their pass.
- **The final shot's curve was reshaped** to a much harder front-load (10 % of the time covering 46 %
  of the move, 88 % by half, versus my 34/60). Candidate rule, one instance only: **the last shot of a
  short lands faster than the house curve.** Watch for it on the next job before making it a rule.
- Everything else kept my curve exactly (0.34 / 0.60 / 0.80 at 10/50/90 %).

## 2026-09-21 — first scripted zoom pass (ABW6 Linked Comp 06)

- **Direction comes from the creator's labels, not from Claude's judgement:** AE label 2 (yellow) =
  pull out, default = push in. They label the footage before handing the comp over. → PLAYBOOK.
- **Two ExtendScript traps, both silent:** `moveAfter` throws "cannot move a layer before or after
  itself" when the new layer is already at that index (it aborted the first run with a modal on the
  creator's screen), and **nested `?:` is evaluated LEFT-associatively**, which collapsed every
  depth bucket to one value — the run "succeeded" and was wrong. Print the derived numbers in the
  script's own log and read them before declaring success.
- **Verify a curve by sampling it, not by trusting the eases you set:** re-sampled all 15 applied
  moves and compared against the 108-move house curve — worst deviation 0.022 of the move distance.

## 2026-09-21 — BlurMoCurves, measured across all 121 instances (9 shorts)

- **Two of my earlier "rules" were coincidences of one short and are now retracted:**
  direction alternating shot to shot (really 45 % = chance) and size continuity across a cut
  (really 29 %). Never generalise a craft rule from a single video — n=12 looked convincing and was wrong.
- **Center XY is off-centre 45 % of the time** (x always 540, y median 699, range 83–851): the zoom is
  aimed up into the face. The reference short happened to be all-centre, which hid this.
- **The curve is the signature, and it is not "easy ease":** 35 % of the distance in the first 10 % of
  the time, a long drift, then 18 % in the last 10 %. Verified by sampling the real value through 108
  moves rather than reading keyframe handles — **ease speed/influence numbers were misleading**
  (departure speed reads 44x the average rate, which means nothing until you sample the curve).
- **My earlier interpolation readout said HOLD on every key; it is BEZIER (6613).** Print the raw
  enum number, never a mapped label, when a readback looks impossible.
- **13 of 121 instances do not move at all** — Z Dist parked at 1.00 or 0.80. The effect doubles as a
  static size hold, so "has BlurMoCurves" does not mean "has a zoom".
- Depth scales with shot length (0.19 under 1.5 s → 0.32 over 5 s), and a push-in always departs from
  exactly 1.00. → README § 3.

## 2026-09-21 — per-word caption colour is NOT scriptable in Premiere

- Probed an upgraded caption graphic on the creator's own timeline: its `Text` component
  (`AE.ADBE Text`) exposes only `Source Text` (an opaque blob) plus transform params — **no fill
  colour, no character-range styling**. Opacity/Motion/Vector Motion are settable; the type is not.
- So on the editable route the creator colours the emphasis words by hand. Claude's job is to make
  that pass fast: `caption-colours.md` lists clip number, timecode, the caption, the exact word and
  the creator's own style name, and repeats it grouped by style.
- **The only path to scripted colour is a .mogrt** that exposes a colour swatch (or a separate
  emphasis-text field); the template is authored once by hand in AE/Premiere, then
  `getMGTComponent()` params are settable per instance.

## 2026-09-21 — a rendered caption layer cannot take the creator's preset

- **The mistake:** I delivered captions as a .mov. The creator's "Revised Light pop" is a Premiere
  preset that only applies to graphics, so a video layer locks them out of their own animation.
  **Ask what the caption layer has to accept downstream before choosing its format.**
- **The editable route that works on Premiere 25.0:**
  1. `make_srt.py` writes an `.srt` (text, timings, `<i>` on the other speaker's lines).
  2. `importFiles` the .srt, then **`seq.createCaptionTrack(item, 0)`** — or the bridge's
     `create_caption_track` with `sequenceId` + `projectItemId`. (`seq.captionTracks` does NOT exist
     on 25.0: probing it throws, which is what killed the first attempt.)
  3. In Premiere: **Upgrade Captions To Graphics** (confirmed present in this build's menu strings)
     turns the track into editable text graphics; select all → text style → drop the preset on.
- **There is no caption READ API**, so a created track cannot be verified by script — say so instead
  of claiming it landed.
- **Trade-off to state plainly:** the rendered layer carries the per-word gradients automatically;
  the editable route needs those ~20 emphasis words coloured by hand (cheat-sheet generated by
  `make_srt.py`). Per-word colour cannot be scripted in Premiere.

## 2026-09-21 — creator's first caption review (Sequence 22)

Six corrections, all now rules:

- **No punctuation except `?` and `!`.** No commas, no full stops. (My first pass carried both.)
- **Sensitive words are censored, not avoided:** `sex` → **S*X**.
- **Pink means love, affection AND women** — hence S*X pink (it is about affection here, not shock),
  LISA MARIE pink ("she was a woman"), KITCHEN pink. Pink is wider than "tenderness". → README § 8.
- **Emphasis colouring is per phrase, by feel:** DAY TO DAY yellow, WAKING UP yellow,
  SOMEBODY blue in "sleeping with somebody". Colour the phrase that carries the beat, not just nouns.
- **The pop was wrong and it shows.** My eased 8 % curve read as a different animation. Measured the
  creator's export frame by frame: a steady climb toward the preset's 112 % (+1.6 % @0.05 s,
  +5.3 % @0.20 s, +9.0 % @0.60 s). `build.py` now interpolates the measured table.
  **Measure the creator's own frames before modelling any animation — the nominal preset values lie.**
- **Open:** a literal application of their Premiere preset is only possible on native text graphics,
  which scripting cannot create. A rendered layer must imitate the curve.

## 2026-09-20 — first captions job (ABW6 · Sequence 22, Lisa Marie / MJ)

- **The caption tooling now exists:** `build.py` (renders the layer) + `make_plan.py`
  (captions.txt + words.json → plan, validating every word against the transcript). Job:
  `projects/lisa-marie-mj/`.
- **Calibration beats guessing:** two caption widths measured off the creator's own export
  ("YOU SHOULD NOT SAY" = 634 px, "REALLY DON'T KNOW" = 603 px) plus the 39 px cap height solve to
  **Gretaros size 52, tracking −0.5**. Rendered strings then landed within 2 px of theirs.
- **Their white captions are flat white**; only the emphasis words carry a gradient (top → bottom,
  darker at top). Sampled stops are in README § 8.
- **Bug found and fixed: per-character tracking must draw on ONE baseline** (`anchor='ls'`).
  Drawing each character with `anchor='lt'` floated every comma and full stop up to cap height,
  so they read as apostrophes. Always QA a frame with punctuation.
- **The deliverable is a black-background .mov**, exactly like their own Premiere caption export, so
  it feeds CapCut directly and skips one export. On the timeline it needs blend mode Screen to preview.
- **Scripted import worked this session** (contrary to the 2026-09-18 note): `importFiles` +
  `overwriteClip` onto the first empty video track, verified by readback.

## 2026-09-20 — teardown of the "Wacko Jacko" short (ABW6 / Sequence 11 → ABW7 / ABW6 Linked Comp 03)

- **Lesson: the zoom is a Sapphire Z-space move, not a scale keyframe.** Every shot gets its own
  adjustment layer with `S_BlurMoCurves`, Z Dist animated across the *entire* shot with
  pop-then-settle easing. → Recorded as README § 3. Never animate layer Scale for the push.
- **Lesson: zoom size is continuous across a cut.** A pull-out starts at the value the previous
  push-in ended on (0.80 → 0.79, 0.84 → 0.69). → README § 3. A zoom that restarts at 1 every shot
  reads as wrong.
- **Lesson: the "complete" letterbox is one mask plus a 198 % / 43 % twin.** The same mask on both
  copies works because masks scale with the layer. → README § 4.
- **Lesson: the glow bar is a 1 %-tall white solid precomp**, glowed with Deep Glow (Unmult),
  bevelled, and double drop-shadowed; it is placed on the mask edge (offset +592 px from layer centre).
  → README § 5.
- **Lesson: the grade is one preset file, not a stack to rebuild.** Four of the nine effects hide
  their settings from scripting (Looks, Curves, Hue/Sat channels, Sapphire), but that is irrelevant:
  the creator's own method is "new adjustment layer, drag `Affan CC Preset` on", and that `.ffx`
  was verified to contain all nine effects. `applyPreset()` reproduces it exactly.
  → README § 6. *(Corrected the same day: the first note said to duplicate their layer — unnecessary.)*
  **Generalise it:** before concluding something can't be scripted, ask the creator how they actually
  do it; a saved preset beats reverse-engineering values.
- **Lesson: two-line captions are two graphics on two tracks**, not one two-line text block; the
  second line sits 59 px below. → README § 8.
- **Lesson: italic marks the other speaker.** The interviewer's questions are italic, the subject's
  answers upright; non-speech is italic inside asterisks. This was invisible in the earlier
  export-only analysis. → README § 8.
- **Lesson: the caption "pop" is a slow ~7 % growth across each caption's life**, not a snap on entry.
  → README § 8.
- **Lesson: the channel's loudness has tightened.** Older shorts ranged −20 to −11.6 LUFS; this one
  is −15.3 LUFS / −1.4 dBTP. Treat −15.3 as the current target until told otherwise.
- **Lesson: the opening can be an ElevenLabs voiceover**, not only source audio (voice
  "Christopher – Gentle and Trustworthy", first 5.57 s), carrying the same Studio Reverb as the speech.
- **Lesson: AE scripting quirks.** `-r` forwards to the running instance, but the script path must be
  unquoted inside the PowerShell ArgumentList array, and a heavy dump can take minutes — chunk it and
  poll for a result file.

### Second pass, same day — gaps closed

- **Lesson: a short is TWO AE comps, not one.** Comp 1 is the head lock, rendered out and sent to
  Topaz; comp 2 is the build. The `_stab_` in `<job>_stab_chr2_iris3.mov` marks the first stage.
  → README § 10.
- **Lesson: the head lock is baked as per-frame Anchor Point keyframes** (linear, one per frame) on a
  heavily scaled layer (≈ 546 %), with **Motion Tile** (Output Height 340, Mirror Edges) covering the
  exposed edges. Earlier note said "write Position keyframes" — wrong property, and it missed Motion
  Tile. → README § 10, PLAYBOOK § 2.
- **Lesson: the "Revised Light pop" is readable** in `Effect Presets and Custom Items.prfpset`
  (Premiere profile folder): Vector Motion Scale 100 → 105 → 112 % over 0.367 s, with the text rising
  0.5 → 0.448 of frame height. No need to eyeball it. → README § 8.
- **Lesson: bar shadows and caption shadows differ** — Distance 5 on the glow bars, 12 on the caption
  precomp. Same two-shadow stack otherwise.
- **Lesson: caption colours are saved Premiere Text Styles**, not per-word fills — Gretaros,
  Gretaris Italic, Red Shade Greators, Pink Shade, Light Blue Shade, Orange Yellow Shade, Green Shade.
  Apply the style by name and the gradient, shadow and weight come with it. → README § 8.
- **Lesson: only three mask bands are ever used** in the reference short: y 440–1484 (h 1044),
  452–1468 (h 1016) and 504–1412 (h 908), with the fill twin at 198 % (217 % / 221 % on two shots).

### Open questions from this teardown (ask before replicating)

1. **The 36-piece speed pattern on the render track.** The finished render is re-imported, sliced into
   36 pieces on a 2-second grid, with speeds alternating **1.0 / 0.99** and the first 0.1 s at **0.7**.
   What is this for — music sync, a retime, or platform-side handling? Claude has not replicated it.
2. **The speech stem naming** `<job>-esv2-27p-bg-10p-music-10p.mp3` — which tool produces it, and do
   the percentages need setting per job?
3. **Music level.** Every clip sits at default gain, so the balance is baked into the stem. How is the
   music level actually set?
4. **Grade sections.** The grade is split into 6 spans with slightly different sharpening
   (BCC Unsharp Amount 17 vs 7, Unsharp Mask on/off). Is that per source-clip quality, by eye, or a rule?

- 2026-10-17 (ABW10 Seq 05 roadster captions): **captions came in before the words** (worst 0.56 s) and two lines were misheard
  ("is your system" = "are we talking", "want to go" = "wanna go"). Change: transcribe the clean A1 dialogue rebuilt from the
  sequence's A1 clips, not the finished render's mix, and when two timings exist take the LATER start per word; read the transcript
  once against the audio for misheard phrases before writing captions. File: `projects/abw10-comp04/captions/` (merge in RUN.md).

- 2026-10-20 (direction video, Katherine "day Michael died", ABW10 Seq 13): **one zoom layer per same-shot run.** Consecutive cuts
  of the same camera on the same person get ONE BlurMoCurves zoom spanning all of them and NO transition between them (else it
  zooms "out, out, out" on one shot and reads jarring); a new layer only where he asks for one. Transitions go only at camera or
  overlay changes, by the label-colour rule (purple dip, cyan gaussian, dark green exposure). File: `projects/katherine-day-michael-died/BRIEF.md`.
- 2026-10-20 (same): **Topaz on jittery footage** (still shaky after head lock / overlays): raise the interpolation a few points and
  lift the SECOND stabilisation pass slightly; never go to three passes (the lips slow down and captions can't keep up).
- 2026-10-20 (Katherine "day Michael died", the first short BUILT IN CODE from a direction video, `projects/katherine-day-michael-died/`):
  **caption height on ABW10 is NOT the ABW8 trial's.** His ABW10 finals (Paris Life, Linked Comp 09) put line 1 at y1093–1134;
  the trial engine (Nick Walker, ABW8) lands it at y980. Measure his latest final before reusing a position; the code build keeps
  it as data (`timeline.json caption_shift`). File: `projects/katherine-day-michael-died/build/finish.py`.
- 2026-10-20 (same): **Seq times dumped at 4 decimals are not frames** (1.7667 = frame 106.002): `t >= t0` matching put every
  "…67" cut one frame late vs the audio. Snap every time to the 60 fps grid before rendering. File: `build/stage_a.py`, `build/finish.py`.
- 2026-10-20 (same): **head lock in code = optical flow on the UPPER face + the face detector low-passed** (the detector's nose
  point alone wobbles 1–9 src px per frame): lock error 2–3× lower on 22 of 25 shots; keep the steadier per shot. And **Topaz's
  full-frame stabiliser partly fights a head lock** (it smooths the background, which moves once the head is pinned): measured
  better on some shots, worse on others; his "jittery after head tracking" note is this. File: `build/stage_a.py`, RUN.md.
- 2026-10-20 (same): **Topaz changes the frame count** (+1..+3: chr-2 near cuts and in black gaps, prob-4 one at the end); re-grid
  by CONTENT (`build/align_frames.py`, banded DP), not by guessing at cuts. `zoom_center.py`'s detector fails on extreme close-ups
  (no face / partial boxes): apply its rule to geometry measured from landmarks + the locked nose instead.
- 2026-10-21 (Katherine short, his review of v2): **"KAT, YOU HAVE TO COME DOWN TO THE HOSPITAL"** — Joe calls her Kat. Every
  ASR pass heard "can't you have to", and a "Kate" prompt scored 0.00, so the caption agent kept the ungrammatical reading as a
  stumble. Lesson: when quoted speech parses badly ("can't you have to"), test a NAME / nickname for the first word before
  calling it a stumble, and flag it to him instead of deciding. Change: job `captions/transcript/words.json` + `captions.txt`.
- 2026-10-21 (same): **a letterbox overlay's face must sit clear of the caption band** (line 1 y1093–1134, a stacked line to
  ~y1199): the MJ smiling overlay had the captions across his smile. Frame overlays so the feature that carries the beat (a
  smile, the eyes) sits below ~y1215 or above ~y1080; keep the band full of picture (scale up rather than leave black).
  Change: `timeline.json` O3 scale 1.10 → 1.25 about src (668, 442), mouth now y1243–1290.
- 2026-10-21 (same): his MJ morgue still (`projects/katherine-day-michael-died/raw/mj-morgue-still.webp`, 1280², "People v.
  Murray / SA073164" + a stock ID burned in under the photo): crop to the photo (x96–1255, y35–1155, right-aligned so the
  head stays in through the zoom-out), never show the burned-in text. Reusable for the next MJ short.

- 2026-10-21 (MJ siblings "found out he died", the 2nd short built in code, `projects/mj-siblings-found-out/`): **when he re-edits
  our raw cut in Premiere, HIS sequence is the source of truth** (dump it read-only: `seqref/seq_his.tsv`): picture from his V1
  in-points (he slipped Tito's video 0.25 s to fix the CNN package's A/V sync himself), audio from his A1, V2 clips = his
  overlay slots. File: `build/timeline.json`.
- 2026-10-21 (same): **the AW grade turns broadcast skin orange-red**: graded skin measured HSV-sat 0.80-0.85 / R/G 2.2-3.2 on
  CNN/ABC/60 Minutes footage (Katherine's final was 0.64-0.71 / 2.3-2.7, his "very red" note). Measure graded skin per source
  AND per overlay and level saturation before the grade (`sat_level`; target ~0.54 / R/G ~1.6); re-check after Topaz (La Toya
  drifted pink). File: `build/finish.py`, `build/sat_probe*.sh`.
- 2026-10-21 (same): **black overlay slots make Topaz chr-2 swallow frames** (13 here, vs +1..+3 on Katherine): align_frames'
  band of 6 failed; widen it (24) or render the overlays into Stage A before Topaz. File: `build/align_frames.py`.
- 2026-10-21 (same): **wav2vec2 mis-times numbers and stretched words** ("15 minutes" placed 0.3 s early, "weak" 0.2 s short):
  gate every cut edge with 10 ms RMS against the body level, and re-ASR a 3 s snippet when an edge is loud. The rough-cut
  planner would have cut both words. File: `projects/mj-siblings-found-out/beats.json`.
- 2026-10-21 (same): **his D1 call: "its eye balls i believe"** (Jermaine: "I pulled his eyeballs back to look in his eyes") — the
  ASR split eyeballs/pulls; when a 0.2 s syllable stays ambiguous, flag it with the time and let him settle it.
- 2026-10-22 (MJ siblings, same job): **the final AAC 320k encode overshoots a brick-wall limiter by ~1.8 dB true peak** (the WAV
  measured -1.2 dBTP, the mp4 +0.6). Measure true peak on the ENCODED file; give the limiter ~2 dB of headroom (-3.2) and
  re-mux the audio (`-c:v copy`) instead of re-rendering the picture. File: `projects/mj-siblings-found-out/build/audio.py`.
- 2026-10-21 (same): name lower thirds added on his OK (the brief's 'essential with four faces'): Gretaros white name +
  his caption gold relation, under the caption line, 2 s from each speaker's FIRST FACE (not the beat start when the beat
  opens on an overlay). File: `projects/mj-siblings-found-out/build/finish.py` (lt_card).
- 2026-10-22 (MJ siblings v4, HIS REVIEW): **(1) the grade made Black skin "too black... like chocolate", not the real colour**:
  the AW grade + my saturation cut darkened/muddied dark skin; match HOW HE GRADES BLACK FACES on his own finals (measure
  them: `E:/Shorts/Abudance Wisdom Shorts Exports/Final Renders`). **(2) artifacts / pixelation on faces** (worst on the grey
  Oprah MJ overlay): the Topaz chain scales the WHOLE frame to 270 wide before iris x4, which wrecks good 1080p overlays;
  overlays from clean sources must skip that chain. **(3) SFX 10 dB lower.** **(4) captions must not cover the speakers'
  mouths**: frame each face so the caption line sits just UNDER the lips (memory: captions-just-below-lips), zoom included.
  File: `projects/mj-siblings-found-out/` (v5).
- 2026-10-22 (MJ siblings v5, the fix for his v4 review): **the "chocolate" skin was mostly a PIPE bug, not the grade**: every
  splice tool fed ffmpeg an UNTAGGED rawvideo yuv420p pipe, ffmpeg read it as BT.601 and wrote BT.709, so each generation made
  skin ~7 % darker and redder; v4 went through five (raw Y 119 -> 73). Rule: every rawvideo writer tags its INPUT
  `-color_range tv -colorspace bt709 -color_primaries bt709 -color_trc bt709`, and the enhanced picture is assembled in ONE
  pass from first-generation sources (`build/assemble.py` + a plan), never by chained splices. Measured fix (landmark cheeks,
  `build/skin_stats.py`): La Toya luma 0.31 -> 0.63, R/G 3.02 -> 1.70; Tito 0.17 -> 0.40, 2.64 -> 1.76; Jermaine 0.28 -> 0.39,
  sat 0.30 -> 0.48. File: `projects/mj-siblings-found-out/build/`.
- 2026-10-22 (same): **his grade BRIGHTENS dark skin; the trial layer-43 fit (Nick Walker) darkened it.** On his own pair
  (`Final Renders/mj_stab_chr2_iris3.mov` -> `MJ Final Skin.mp4`) dark skin rises ~1.2-1.35x in luma (Ronnie 0.293 -> 0.346,
  MJ 0.443 -> 0.590) with R/G about kept. Fit his grade as per-channel quantile curves on his pre/post pair (`build/fit_grade.py`
  -> `grade_curves.json`, 76 frames, centre region, no caption rows / letterbox / dips) and validate by re-applying to the pre
  file (0.557 vs his 0.590). The PRE sharpen bands + Sharpen 40 went too: they turned Topaz texture into blocky speckle.
- 2026-10-22 (same): **overlays skip Topaz**: the chain's 270-px downscale before iris x4 pixelated clean 1080p overlays
  (the grey Oprah MJ); Stage A overlay frames go straight into the one-pass assembly. **Topaz still speckles 300-500 % face
  upscales** (Jermaine's / Marlon's forehead shine -> white 1-4 px dots): a 5x5 grey opening on luma, applied only where the
  blurred neighbourhood is warm mid-luma skin (`finish.py despeckle`, timeline `despeckle: [setup]`), removes them and keeps
  catchlights, teeth, sunglasses glints and the mic grille.
- 2026-10-22 (same): **lips vs captions on a push-in: pivot the zoom ON the lip line.** The face-top pivot rule moves the
  pivot up, which pushes the lips DOWN into the caption band during the push (Tito, v4). Pin the lips (nose y so the lower lip
  sits <= 1084, caption top 1093; `zoom_pivot_override`) and, when the face is too big for both rules (face top -> lip span
  x zoom > 884 px), make the zoom SHALLOWER (Tito 0.85 instead of 0.75-0.82) rather than give up either the caption rule or
  the top-200 safe zone. Name cards obey the same rule: a card that lands on a mouth moves (Jermaine's above his letterbox
  band, y0 175). Check: `build/lip_check.py` (zoom included) + YuNet face top on the render.
- 2026-10-22 (same, his call on v5): **a mouth that is already clear beats a deeper punch.** Marlon (sunglasses, CBS memorial,
  300 %): lifting his lips above the caption line needed ~600 %, not the ~390 % first quoted; with the captions on his nose
  and his mouth free he chose to keep 300 % ("his mouth is clear"). Quote the MEASURED zoom before asking for a softness trade.
- 2026-10-22 (MJ siblings, his review of v5: "the whole grading is so soft... I told you to just reduce the blackness"):
  **fix ONLY what he named, and never swap out his grade.** v5 replaced his AE stack (layer-43 look + PRE sharpen bands
  unsh/ssh/bccu + Sharpen 40) with curves fitted on one MJ pair, without sharpening -> soft, flat, hazy. The CORRECTION to the
  entry above: the v4 darkness came from the splice-pipe drift feeding his stack, not from the stack itself; his stack on
  the one-pass (drift-free) picture gives his channel look (crisp, contrasty, warm brown skin) — v6. Reference for "how my
  grading looks": his own finals in `E:/Shorts/Abudance Wisdom Shorts Exports/Final Renders` (e.g. `toya yt final.mov`:
  cheek skin luma 0.55, sat 0.55, R/G 1.55, face p10 0.08). Show him test frames of EVERY shot before a full render.
- 2026-10-24 (MJ kids saw, `projects/mj-kids-saw-day-he-died/`, raw sequence): **news packages splice courtroom testimony.** The
  Telegraph's Alvarez clip joins "Paris screamed out, Daddy" straight to "Dr. Conrad Murray said…" (≈40 s of Q&A cut) and drops in
  "the children were crying and screaming" from elsewhere in his testimony; its cutaways (defence table, Murray) sit under his
  words, and the brief's timestamps ran ~4 s early. Match by WORDS, check what is on screen under every piece (one frame per piece),
  and for "speaker on camera" use the uncut trial feed (fan uploads: `Conrad Murray Trial - Day N` / per-witness playlists; their
  playlist RSS `youtube.com/feeds/videos.xml?playlist_id=…` lists exact video links when YouTube pages are blocked). Live-stream
  uploads DROP audio/picture (Alvarez lost ~1.6 s on "kind of ushered them out and said"): diff the words before swapping a piece.
- 2026-10-24 (same): **his order for AW shorts is raw sequence → HIS sequencing (he re-edits it) → his direction video → code
  build.** An approval button must say only "approved"; mine bundled "start the code build" and he had to stop it.
- 2026-10-24 (Paris "won't post on his birthday", the 3rd short built in code, `projects/paris-wont-post-birthday/`):
  **Topaz's login token can lapse MID-RUN**: the chain kept going and only step 3 (prob-4) came out with a "Topaz Labs"
  WATERMARK on every face ("Critical error refreshing token Could not establish connection"; topazlabs.com reachable = the
  app's own sign-in). Check a frame of EVERY Topaz output for the watermark before assembling; after he signs in, re-run only
  the dirty step (`build/topaz_step3.py` on the clean step-2 file). Never work around the licence.
- 2026-10-24 (same): **search his drives before asking for downloads** (he asked "have you checked my machine?"): 2 of 4 sources
  were already in `E:\Bullshit Folder\Henry` — one a BETTER copy (Paris's original vertical IG video instead of the news
  package that wraps it). `find` by title words over E:, X:, C:\Users\affan takes ~15 s.
- 2026-10-24 (same): **her IG video carries a thin bright glitch line** (dashed, 2-8 px, ~24 % of the used frames, also a faint
  variant in bursts next to strong ones): detect per frame (row brighter than both rows +-5 px over >35 % of the width / of
  its right 70 %; faint tier only near a strong band) and repair by vertical interpolation IN STAGE A, before Topaz.
  `build/ig_line.py` (cache `build/ig_lines.json`). seq_render frames are H x W x 3 uint8, not C x H x W float.
- 2026-10-24 (same): **podcast A/V offsets can be large**: Jack Osbourne's upload has the picture 0.37 s AHEAD of the sound
  (mouth-darkness vs speech-envelope cross-correlation on 7 shots, `build/av_offset.py`; CONFIRMED on a bilabial: the lips close
  for the "m" of "my dad" 0.37 s before it sounds, `build/mouth_strip.py`). His own IG slip (+0.10) measured +0.13 by the same
  method. Measure every talking source; he only said "a bit out of sync".
- 2026-10-24 (same): **captions vs an OPEN mouth**: the YuNet lower-lip estimate (corners + 0.18 x width) is a closed mouth;
  open, the lip/teeth reach ~25-30 px lower (P1/P5 touched the caption top y1093 at lip ~1078-1089). Target lower lip <= ~1060.
- 2026-10-24 (same, Premiere): cloning the 60 fps "Onyx reaction template (empty)" and setting 30 fps with setSettings leaves
  the 60 fps TIMECODE display (videoDisplayFormat 108): the sequence then READS half its length ("the runtime is just 16 seconds")
  and QE razors silently miss; set videoDisplayFormat 104 too. In-points are FLOORED twice (source grid, then sequence grid):
  pass the first source frame at/after the wanted time and verify on the read-back. A "pause" on a phone line can be a quiet
  word (cutting a 0.66 s "gap" deleted "probably"): re-ASR the snippet after every cut.
- 2026-10-24 (MJ kids saw, code build, `projects/mj-kids-saw-day-he-died/build/`): **head lock inside a letterbox needs a bigger
  scale than the letterbox look itself.** His "346 %" band (TEL 348 px -> 1204 px) leaves the band edges exposed (mirror strips)
  as soon as the locked nose moves (TEL nose y 101-120, FM 116-141 src px): solve scale + nose Y per setup from the tracked noses
  so every frame fills the band (here 4.0, AT nose y745, FM y704). One caption line for courtroom + a full-bleed close-up
  then forces a trade: his call was **Katherine LOWER, captions on her NOSE** (nose y870): with her lips on the line (nose y561)
  the bottom mirror tile showed ~490 px and "looked really ugly".
- 2026-10-24 (same): **caption_shift is POSITIVE = UP** (the layer's native ink y1030-1070; -62 put ABW10 captions at 1093).
  A sign slip put them on the name cards; check one finished still before believing a caption height.
- 2026-10-24 (same): **when YouTube / a news site blocks this PC and he is away, fill the slot from footage already on disk**
  and say so: the trial packages carry their own Murray cutaways (AP close-up, Telegraph defence table) and the exhibit photos
  (Exh. 23 = the Telegraph bedroom photo: crop clear of the AP bug + "People v. Murray" text, Higgsfield-enhance, 1.5 cr).
  SD overlays (640x360 at 600 %) DO go through his Topaz chain; the "overlays skip Topaz" rule is for clean HD overlays.
- 2026-10-24 (same): **graded skin per source still needs levelling before his grade**: AP Faheem came out 0.27 luma / 0.96 sat
  (the "chocolate" case) and 60 Minutes Katherine 0.42 / 0.8 / R/G 2.4 (the "very red" case). Pre-grade gamma 0.74 + sat 0.58
  (Faheem) and sat 0.55 (Katherine) brought them to 0.39 / 0.68 and 0.43 / 0.61 / 1.8 with his AE stack untouched; he approved
  the frames. Measure with `build/skin_png.py` on the test stills.
- 2026-10-24 (MJ kids saw, HIS REVIEW of v1): **(1) "why is Conrad so zoomed in"**: an SD 16:9 overlay full-screen is already a
  5.3x blow-up; stacking an extra framing scale (6.6) + a 128 % push-in read as far too tight. SD full-screen overlays: the
  minimum full-bleed scale (+ just enough to hide the source's black edge rows) and a shallow push (<= 115 %). **(2) "the lips
  are not synced properly"**: a news package can carry a DIFFERENT A/V offset per segment: AP's Faheem 92-118 s ran picture
  0.14 s early while its 39-63 s segment was in sync. Measure every source SEGMENT (closed-lip sounds, fixed mouth crops on the
  finished frame; the letterbox twin fools a face detector), not one point per file. **(3) captions "a bit below, towards the
  middle line"** (this short: line y940-980 instead of just under the lips at y850). **(4) a dark overlay ("too dark... or you
  messed up the grading")**: lifting the blue Telegraph cutaway only went milky; swap to a well-lit shot of the same subject
  (the Day 3 feed's Murray cutaway, 706.4 s) rather than push the grade.
- 2026-10-26 (MJ × Joe appointment, sequencing): **`resolve_beats.py` "tighten" misses pauses on three kinds of source** because
  its pause threshold is the WHOLE file's 10th-percentile floor + 6 dB: gated podcast audio (Art Of Dialogue: floor −95, the
  pauses sit at −80…−90, so 1.0–1.5 s silences stayed), restaurant room tone (NewsOne JJ: speech pauses at the noise level),
  and compilations with silent cards (the detail.). WhisperX also hides pauses by stretching a word ("is" 0.78 s, "child"
  1.7 s). Fix that worked: re-transcribe the A1 rebuilt from the READBACK, list every word gap > 0.22 s with its RMS, and
  hand-split the real ones as explicit `in`/`out` pieces (two rounds here). Also: a compilation's question and answer can
  come from different interviews (JOW: beat 6 dated ~1993 by the Tyson/Jordan line that follows it) — date every piece by
  its own picture and words, never by the brief's source note.
- 2026-10-26 (Derek "daughters", raw sequence, `projects/derek-lunsford-daughters/`): **a brief's "(X only)" line can hold
  other voices.** On a family vlog call, per-word pyin (Derek 100–160 Hz, his wife 200–275, the child on the phone 300–475) +
  a 2 fps lips sheet split the speakers: two of the four "Derek only" lines were his wife's, and the daughter's "Dada" sat
  between his words (dropped). `tools/f0_words.py`. **Two recordings of one PA call** (his arena vlog vs the broadcast)
  align by band-passed envelope cross-correlation (+112.10 s, r 0.755): take the AUDIO where the name is clean and the
  PICTURE from the other at the same moment (per-piece V2 covers). **`place_sequence` re-pins any cover whose `to` is a
  number** (`to_src`, meant for a cover ending on the covered footage's own cut): for covers synced to ANOTHER source it
  wrecked two ends (one before its start, one at 3831 s) — null `to_src` in placement.json for those. **The face detector
  picks the wrong person in two-shots** (B-roll with a second bodybuilder, the bed shot, three men from behind): render
  the crop sheet (`tools/crop_sheet.py`, first/mid/last frame per row as framed) BEFORE placing and pin `framing.json`.
  Also: `plan_placement.py` needs `uv run --with opencv-contrib-python-headless --with numpy`; a beat's `drop_candidate`
  must be an int; a "laugh" in a pause can be a room VOICE ("yeah, that's"): the re-ASR of the readback found it.
- 2026-10-28 (Derek "daughters", code build from his Tella): **never open his Tella link in a browser** (it autoplays WITH SOUND
  and interrupted him): curl the share page, the signed `prod-stream ... manifest.m3u8` is in the HTML. **His guide timecode
  is read in seconds, not minutes**: one ffmpeg crop pass (program-monitor timecode + the sequence duration) + rapidocr in one
  batch (11 s for 613 frames; per-frame ffmpeg seeks into the HLS copy took 40+ min). The duration showed he recorded on a
  LIFTED layout (gaps) and closed them at the end: map "this" against HIS current clips, not the raw placement.
  **Captions from a mixed A1 drift** where a crowd roars (wav2vec2 put "I said, homie" ~2 s early): build the caption
  words.json from each SOURCE transcript mapped through his A1 in/outs (pure arithmetic). `finish.py` letterboxes every
  'overlay' unless it carries `'full': True` (his "only this one is letterbox" = full on all the others). A Zoom-call
  panel (956x540 of a 1920x1080 frame) fills 9:16 at 3.6; measure eyes/mouth with YuNet before choosing a deeper scale
  (4.46 cut his eyes off). Broadcast "reaction" shots: the call itself is often only on a super-wide; the first FRONT
  close-up of the athlete came 15 s later (medal presentation) — check the next camera before settling for a back shot.
- 2026-10-26 (MJ × Joe appointment, code build): **a source decides where its face can sit.** With one caption line (lips
  ~y835), a face that sits HIGH in its 16:9 frame (podcast mediums: Art Of Dialogue bodyguard, Fiddes) exposes a mirror strip
  at the top at 177.87 % — scale it up instead (2.4 / 1.95 / 2.75 = tight, his taste); a face that sits LOW with a bug under it
  (NewsOne JJ) goes in his 440-1484 letterbox band with the captions on the nose (his Katherine note) — the band ends above the
  bug, no delogo, no mirror. Check `stage_a.py sheet` for mirror tiles before rendering. Also: Topaz `align_frames` can drop /
  hold a few frames; check they fall in still slots or on cuts.
- 2026-10-27 (MJ × Joe appointment, HIS REVIEW of v1) — lesson → change → file:
  **(1) "use the exact same interview where he answers the question" for the hook.** A "freeze from this interview where Joe is
  just looking" means the SAME interview as the answer that follows, even when another clip sits in his source monitor (v1 read
  his source monitor = the Larry King clip). → hook = JJ 832.6–834.8 (Joe silent, lips closed, staring toward the interviewer;
  found by listing the interview's silent spans per camera shot, then frame strips) → `projects/joe-jackson-appointment/build/make_timeline.py` F0.
  **(2) A letterboxed clip's blurred background must fill the WHOLE screen.** His twin (198 %) covers a 1044–1204 px band, not a
  thin one (JOW at his 60.87 % = 657 px band left black above/below). → per-shot `twin_scale` (3.0, about the band centre) →
  `build/finish.py` letterbox(); rule: twin_scale >= 1920 / band height.
  **(3) "Remove the music, the music is my job; keep the sound effects of the transitions."** A brief that names a music bed
  does not make music Claude's call on AW shorts (PLAYBOOK division of labour: music = creator). → no bed by default, SFX kept
  → `build/audio.py` MUSIC = None.
  **Outcome (2026-10-27):** v2 (only those three notes changed) was UPLOADED as delivered, no second round. The 4th code build
  shipped after one review: his Tella direction video + sequencing-first held the creative calls, so the notes were
  source/framing/music, not taste.
  **Build notes not logged above (2026-10-29 close-out):** warm-lit TV skin (NewsOne JJ restaurant: luma 0.32-0.41, sat
  0.84-0.88, R/G 2.0-2.5) read orange through his grade → per-source `gamma_level` 0.74 + `sat_level` 0.58 in
  `build/make_timeline.py` (→ 0.42-0.49 / 0.51-0.55 / 1.42-1.52); measure skin on a stage-A frame before the full render.
  `rough-cut/scripts/transcribe.sh` finds only video containers in raw/ (a .wav = "no clips found"): wrap audio as
  `ffmpeg -c:a pcm_s16le x.mov`. faster-whisper on CUDA failed on cublas64_12.dll here → device cpu, int8.
- 2026-10-28 (Flex Wheeler "told doctors to take his leg", `projects/flex-wheeler-leg/`, CANCELLED before intake): **a brief
  can be locked on story and still die on source quality.** Both sources were a 2020 podcast (probably a remote call) and his
  own 2021 vlog with music under it. The brief flagged the picture as its lock 1 ("check that Flex's face holds at 1080×1920")
  but left the check for after the download. When he opened the links he dropped the short: "the source video quality is very
  bad the audio is very bad". Change: on a new brief, hand him the source links FIRST, before working the cut (this PC can't open
  YouTube, so he is the one who can watch them). Flag the risky ones in the same line: a remote call, a phone vlog, music or
  noise under the voice, an old upload. He decides go / no-go before any sequencing. A rescue plan (stills over his audio, punch-ins ≤115 %) cannot fix bad audio.
- 2026-10-28 (Janet "couldn't cry", `projects/janet-couldnt-cry/`, intake): **YouTube downloads worked again**: B2's plain
  yt-dlp commands (no cookies, yt-dlp 2026.08.19) fetched all four sources, the 1.4 GB 4K one included. "Blocked" is not
  permanent: try the brief's commands once before asking him to drop files in (never with cookies/proxies). AV1 comes down
  for most 2009-2011 uploads: transcode before a Premiere import.
- 2026-10-28 (same): **a fan clip of a broadcast can be a LONGER cut of the same interview with different camera cutting.**
  The Dateline restore (DL) puts the hook line on a wide two-shot and "I was in Paris" on a Jackson 5 CHILDHOOD montage; the
  2011 fan upload (WR) holds the same takes on Janet's close-up. Band-passed envelope cross-correlation found the same audio
  (r 0.81-0.96, a per-piece offset because the broadcast trimmed pauses) → keep one audio, swap the picture per piece
  (`win/xcorr.py`). Check what is on screen UNDER every word of a quote, not only at the brief's in-point.
- 2026-10-28 (same): **when the GPU is shared** (other sessions' Topaz / renders at 100 %), full-source WhisperX crawls (8 min
  of audio > 20 min); CPU faster-whisper large-v3 int8 on just the beat windows (+-10 s) took ~5 min for all of them
  (`win/win_asr.py`).
- 2026-10-28 (Derek "daughters", HIS REVIEW of v1): **(1) "lot of artifacts in some places"** = the 2026 OlympiaTV finals
  upload is INTERLACED (ffmpeg idet: TFF 120/120) while its header says progressive (3.8 Mb/s): every moving edge combed
  into horizontal tears, then the zoom and his sharpen magnified them. Run `idet` on EVERY broadcast/event source before
  placing it; fix = `bwdif=mode=send_field:parity=tff` (59.94 progressive, smoother on the 60 fps timeline) + a light
  `hqdn3d=1.5:1.5:4:4` into an intermediate, then re-render only those overlay frames (`assemble.py` "seg"). **(2) "Derek
  looks too red"** (his vlog corridor, warm tungsten): graded skin sat 0.87-0.97, R/G 3.2-3.4 → pre-grade `sat_level`
  {'jrn': 0.45} → sat 0.66-0.68, R/G 1.9 (`build/skin_png.py`), his AE grade untouched — the same "very red" fix as MJ Kids
  Saw's Katherine. Measure every face source's graded skin on the test stills BEFORE sending them (target ~0.4-0.5 luma,
  sat 0.6-0.7, R/G 1.4-2.0); this one was visible on my own v1 sheet.
- 2026-10-28 (Derek "daughters", HIS REVIEW of v2): **"10-14 sec the captions are mismatched, speakers are saying something
  else"** = WhisperX word times on broadcast PA audio (announcer over a crowd): it cannot align "$100,000" (no letters), so it
  squeezed the number into 0.5 s and put the announcer's next word "and" 0.4 s later, INSIDE his cut, when the real "and"
  (forced wav2vec2 on the spoken form "one hundred thousand dollars") sits 0.6 s AFTER his A1 cut. Result: an AND card shown
  during "...thousand dollars", a word nobody says. Every ASR pass agreed on the TEXT; only the times were wrong, so a text
  re-ASR does not catch it. **Gate:** for every broadcast/PA clip and every spoken number, force-align the known text with
  numbers written out (`projects/derek-lunsford-daughters/tools/force_align.py <media> <start> <dur> "<text>" <out>`), map it
  through his A1 in/outs, and drop any caption word that falls outside its clip; end a clip's last card ON the cut.

- 2026-10-28 (Janet "couldn't cry", raw sequence): **a word every A1 re-ASR misses at a piece's END was cut off, not
  misheard.** "about his death" read "about his." in every pass; the real "death." sat 0.25 s after "his" (1614.30-1614.53),
  past an out placed from the window-ASR's stretched word times. Before placing, re-ASR each piece ALONE plus one with
  0.5 s more context: a word the context run hears and the piece run doesn't is outside the piece. The same pass found a
  "to ... to cry" stutter that the long-window ASR had merged.
- 2026-10-28 (same): **a restore compilation can use a speech as silent B-roll.** the detail.'s 4K "Janet's own words" laid
  the BET speech picture under Dateline audio, so audio correlation found nothing; picture-motion alignment
  (`projects/janet-couldnt-cry/win/vis_align.py`) placed it at BET 0-17.2 s only, too short for the beat. Check a "better
  copy" covers the beat's PICTURE and AUDIO before promising it.
- 2026-10-28 (same): **crowd/applause hides pauses from a whole-window floor.** BET's 3 s pause after "My" and the
  joined-beat "quiet" runs were both wrong at the beat floor; a +-3 s local floor at 10 ms (`win/strip.py`) shows the real
  edges. Judge B1.1 gaps on the SOURCE floor; the joined-cut floor counts soft word tails as silence.
- 2026-10-28 (Janet "couldn't cry", HIS REVIEW of v1, REVISED): **the caption line is HIS height, never one source's.**
  v1 put the line at ~64 % (y1250-1290, caption_shift -220, the brief's 62-68 %) so DL's tight, low 4:3 close-up kept its
  lips above it, then placed BET and Michael's message LOW to match. His note: "the caption should be here" (his mouse on
  the hook's nostril line = y1060, 55 %), "drag this footage up ... so it still sits under her lips", "all of these things
  are placed too low just because the captions are placed too low". Fix = caption_shift -10 and the two letterboxed
  sources lifted 210 px with their bands and zoom pivots (a finish-side translate of the reviewed picture, `lift` in
  `projects/janet-couldnt-cry/build/finish.py`, no Stage A / Topaz re-run). Rule: his approved finals carry the line at
  y940-980 (Joe v3, MJ Kids Saw) to y1092-1129 (MJ Siblings), measured on their frames (`projects/janet-couldnt-cry/win/
  ref_*.png`); start there, move letterboxed / placeable sources to put the lips over it, and let a full-bleed close-up
  that cannot move carry the line on its nostril / upper-lip line (his own mark on the hook; UPLOADED that way
  2026-10-29 after this one review) rather than drag the whole short's line down. A brief's % number does not override his own position.
- 2026-10-28 (same): **head lock with a cover clamp.** The lock holds the nose at (540, Y) only while the picture still
  covers the frame (`projects/janet-couldnt-cry/build/stage_a.py` cover_clamp; DL's 'content_x' = the 4:3 picture inside
  its pillarbox); past that the face moves in frame instead of a Motion Tile mirror. Needed when a speaker lowers and lifts
  her head inside one shot (S12: 550 src px of travel).
- 2026-10-28 (same): **a fan clip of the same interview is a cover layer, not a source swap.** Where he laid WR's close-up
  on V2 over DL's wide / childhood montage, the shot list uses the visible layer and the audio stays DL's (his A1); each
  cover starts at DL time minus the measured offset (<= 1 frame).
- 2026-10-28 (same): **edge checks on a 30 fps export: seek to f/30 - 5 ms.** Seeking to (f + 0.5)/30 returns frame f+1 and
  shows a false "stray frame" before every cut (`projects/janet-couldnt-cry/win/final_edges.py`).
- 2026-10-29 (MJ siblings): **v6 UPLOADED** — confirms the shipping recipe: his AE stack (layer-43 look + PRE sharpen bands +
  Sharpen 40) unchanged, on a one-pass BT.709-tagged picture; overlays skip Topaz; despeckle only on Topaz-speckled faces;
  zoom pivots on the lip line with a shallower depth when a face is too big; test frames of every shot before the render.
- 2026-10-29 (MJ kids saw): **v2 UPLOADED** with no further notes after his four v1 fixes (SD Murray overlays at near-minimum
  full-bleed + <= 115 % push, per-segment lip-sync on the AP package, captions on the middle line, a well-lit overlay swapped in
  for a dark one). Courtroom shorts can ship from trial footage already on disk when YouTube is blocked (`projects/mj-kids-saw-day-he-died/`).
- 2026-10-29 (Katherine "never got over him", `projects/katherine-never-got-over-him/`, raw sequence): **a word ASR hears at a
  piece's head ALONE is often invented; the JOINED cut decides.** Pieces read alone opened on "Then when", "And I go", "But I"
  (abrupt starts); with the previous piece in front, two were artifacts and two were real leaks: Jermaine's piece ran 0.17 s
  into a voiced "be-cause" (no gap, so the level strip showed nothing) and Michael's own "But" sat 0.15 s before "I". Check
  every head with the PREVIOUS piece in front and every tail with the NEXT piece after (`win/asr_a1.py` + a joined-context pass),
  not only each piece with its own context.
- 2026-10-29 (same): **a burned-in subtitle bar can be cropped out instead of covered**: KAT's bar = rows 788-939 on every frame,
  so 250 % with the frame ending on row 784 never shows it (brief: never two sets of subtitles). That crop is ~430 px for a
  ~340 px face, so a fixed position clips her when the camera drifts: Position keys from a 5 fps YuNet face track
  (`premiere/fix_framing.py` → `kat_keys.js`, key time = media time). Also: a slowed cover clip is rendered with `-t` BEFORE
  `-i` (after `-i` it caps the retimed OUTPUT: a 1.73 s slot got a 1.40 s file), and a cover over a shot that DISSOLVES out
  runs to the dissolve's last blended frame (PHM crowd → Michael, 1536.64), or the crowd ghosts for 2 frames.
- 2026-10-29 (Katherine "never got over him", his Tella direction 1): **caption colours were drifting to white + red only;
  he wants a MIX.** White constant, ONE accent per caption, varied through the short by meaning: pink love · yellow
  happiness · red evil/bad · blue mellow/emotional · green very positive · orange too. Now in README §8 ("Colour MIX").
- 2026-10-29 (same): **his re-cut is the spec.** He took the 58 s raw sequence to 30.9 s himself (dropped beat 4 and the
  Larry King line, extended two Jermaine edges, let Katherine's ending run continuous and fade out). Build from a read-only
  dump of HIS sequence (`premiere/his_dump.js`; real out = inPoint + duration, the dump's outPoint runs ~0.17 s long), never
  re-place over it. Zooms are grouped per run of same-shot jump cuts (he named them by selecting the clips), and each
  transition sits on a zoom-group boundary.
- 2026-10-29 (same): **check placed framing against FRAMES, not just against the plan.** v2's verify passed while one Jermaine
  piece (88.8–90.4, camera reframed so he sits at x≈0.2) was framed on the cabinet and his hand: the face track had locked
  onto the wrong side. A contact sheet of every placed clip's first/mid/last frame catches it; the plan comparison cannot.
- 2026-10-29 (same): **"captions in the middle + bump the face up"** = his Janet line (y≈1058) with the lips lifted just
  above it. A full-bleed close-up can only lift by exposing what is below the picture (Katherine: her burned-in subtitle
  bar; Joe: past the frame at the 115 % cap), so the lift needs a bottom band; test frames of B black band vs C AW §4 fill +
  glow line went to him (`projects/katherine-never-got-over-him/proof/lift_options.jpg`). **He picked C** (the AW §4
  dimmed 198 % fill at 43 % + glow line under the lifted picture): default for any future lift that exposes a bottom band.
- 2026-10-29 (same, note 2): **a silent crying pause gets a stage-direction caption.** "The silent pause where Katherine is
  crying you will put a caption of quote unquote tears up." → a "tears up" card over the measured room-tone span only
  (level strip of his A1, not the ASR word gap, which put her next word 0.3 s early), same line and style as the speech, one
  accent (blue = emotional). If it repeats on another short, it becomes a README §8 rule for any wordless emotional beat.
- 2026-10-29 (same, build): **the lift's band size is set by the LOWEST lip, not one test frame.** With a fixed band (his
  workflow: the mask is fixed in frame space), each source row lands at edge − (clean rows below it) × scale, so a speaker
  who bows (Katherine crying, lips 130 source rows lower) needs a 560–585 px band to keep the lips clear in every frame.
  Measure the setup's lip range first (`build/geom.py`), and if the band grows past the test, show both settings on the
  deciding frames. He chose the tested ~375 px band: lips clear while upright, the caption meets the mouth only in a bow.
  The lifted setups lock x only (y static per camera), so the picture doesn't swim under the band → `projects/katherine-
  never-got-over-him/proof/lift_choice.jpg`, `build/geom.py`.
- 2026-10-29 (same, build): **a speaker who turns to profile is locked on the centre of the head, not the nose.** A nose
  lock at x540 cut the back of Jermaine's head on the left edge in clips 7–9. Lock nose + the smoothed face-box offset
  (`build/head_dx.py`, σ 0.25 s): his head stays whole and centred → `projects/katherine-never-got-over-him/build/`.
- 2026-10-29 (same, build): **pre-grade skin levelling again** (3rd code build in a row: Joe Appointment, Janet, Katherine):
  layer 43 took Katherine to sat 0.61–0.66 / R/G 1.82–1.93, Joe 0.59 / 1.82, Michael 0.65. Fixed with sat_level kat 0.72 /
  jow 0.70 / oprah 0.72 / jerm 0.9 + gamma 0.85, giving 0.47–0.59 / 1.50–1.70. **Now the default: measure skin on the first stills
  of every build (`build/skin_png.py`) and level before the grade.**

- 2026-10-29 (Kane "didn't deserve it", his Tella direction): **the caption colour MIX is a cross-short rule, not a
  Katherine one-off.** He gave it again unprompted on a second short the same day ("white and blue, white and pink, white
  and green… not just one colour combo", "gradient colours, not plain colours") → README §8 "Colour MIX" applies to every
  AW short.
- 2026-10-29 (same): **a downloaded source can carry its own A/V offset.** His note "the lips and the audio are not synced"
  on B1: Ashton's SnapDownloader file has the picture ~0.16-0.20 s AHEAD of its audio (container start times all 0, so
  ffprobe does not show it). Measured at bilabials: `projects/kane-didnt-deserve-it/win/plosive_check.py` tiles the mouth
  at every 25 fps frame over a 5 ms energy strip; the lips must be shut during the audio's b/p/m closure. A mouth-ROI
  frame-difference xcorr was too weak to trust (r ≈ 0.1, sign flipped between windows). Check every talking source this
  way before render; fix by slipping that source's picture against its audio, never by moving the cut.
- 2026-10-29 (same): **transitions dictated as colours.** "This will be purple fading into this": he selects clip A, says
  the colour, selects clip B. The colour is his label code (README § transitions: purple dip, dark green flash, peach
  exposure blur, cyan gaussian). Map each to its cut by the white selection outline + the timeline TC in the frame; a cut he
  does not name stays straight; he also names same-camera jump cuts. Self-corrections ("purple… dark green actually"):
  the last word wins.
- 2026-10-29 (Kane "didn't deserve it", code build): **an overlay's first frame can belong to the shot before it.** The
  clip pack's penalty starts at 75.233; a 0.1 s contact sheet read "75.2 = close angle" and the build started at 75.20, so
  the first exported frame showed the wide angle. Find the cut at 1/60 s steps before setting any overlay `s0`, start 1-2
  frames inside the shot, and read the exported cuts (`win/final_edges.py`) before delivery: that check caught it.
- 2026-10-29 (same): **Janet's build kit, two latent bugs fixed in the Kane copy:** (1) `finish.py` read timeline.json as
  cp1252, so any non-ASCII card text (·) came out as "Â·": open it with utf-8; (2) `audio.py` ramped every speaker block to
  ZERO over 20 ms at its edge, a ~40 ms dip at each speaker change: hand the per-speaker gain over as a smoothed curve.
- 2026-10-29 (same): **a bigger caption for one beat** (the brief's English-only uncle lines): `big:` in captions.txt →
  make_plan `big` flag → render_caps multiplies the pop scale (1.35) and the stacked pitch, through a local copy of the
  engine's draw(); the shared trial engine stays untouched.
- 2026-10-29 (same): **when YouTube blocks a pick** (geo-block or the bot check, never bypassed), the same broadcast may be
  on Dailymotion (yt-dlp, plain) but often only as wide league highlights; judge it for a full-screen 9:16 crop before
  using it, and say what was swapped in the report.
- 2026-10-29 (Kane, same): **check the caption line against EVERY speaker's mouth on the final, not one test still.** The
  uncle's handheld face sits low in his frame; at the standard full-bleed size the line sat ON his mouth for 4 s, missed by
  the per-shot still sheet (one frame per shot). Fix by his rule (lift the face, never the line): bigger scale within the
  ~115 % SD cap, nose held higher, zoom pivoted ON the caption line, and a bottom mirror-filled lift inside the UI band.
  Topaz's stabiliser smeared that handheld face: re-run that segment `topaz-iris.py --no-stab`.
- 2026-10-29 (Kane, his review answers): **"Use the kids" + "if it's low quality do letterbox format on it".** A brief's
  hard rule (no minors) can be lifted by him for ONE slot; it stays in force everywhere else and the report says so. The
  kids footage existed nowhere local or on Dailymotion; his SnapDownloader file was a fan's zoomed phone shot (1080p30,
  1.6 Mb/s, figures ~600 px tall). **His letterbox for a low-quality overlay** in the code kit = an overlay shot WITHOUT
  `'full'` + its own `band` / `twin_scale` / `twin_blur`, source at native 100 % (README § 4, 1044 px band) so nothing is
  upscaled. Three numbers to get right before rendering: (1) lift the band until the smallest face clears the caption line
  (here 150 px: the son's chin ~60 px above y1040); (2) a lifted band moves the twin's centre, so the twin must reach
  `2 * max(cy, 1920 - cy) / band_h` (2.12 here), not 1920 / band_h; (3) pivot the overlay's zoom on the band centre, or the
  115 % first frame pushes the top glow bar into the top-200 safe zone (measured y203 → y288). **Topaz Iris on tiny faces
  in a phone shot draws artifacts** (a dark "goggles" band across a 40 px child's face, a shirt number rewritten): compare a
  2x crop of the smallest face before and after Iris. PENDING HIS REVIEW: v3 shipped O6 without Iris (his standing rule
  is Iris on every <=1080p source); his answer decides whether this becomes a rule. **A grass pitch through the warm grade goes neon** (chroma 0.59 vs 0.15-0.43 on every other shot): level it with
  the per-source `sat_level` (0.62) before the grade, measured against the other shots, never by touching his grade.

- 2026-10-31 (Patrick Stewart "father so angry", his Tella 1 on my SEQUENCE PREVIEW, `projects/patrick-stewart-father-angry/`):
  **a sequence preview as a plain MP4 before any build worked**: he answered it with one Tella (one cut, five picture
  notes, "apart from that you can start"), so the build ran once on a locked cut. Keep it for brief-driven shorts.
- (same) **Under 60 s matters to him because of MUSIC**: "if the video is over a minute the song selection ... starts to
  get blocked" (YouTube Shorts over 60 s lose most licensed songs). Flag every cut that lands over 60 s with the exact
  word cut that would get under it. Tightening every joint to the MEASURED acoustic edge gained nothing here
  (`seq/edl.edgetest.py`: 61.9 vs 61.73 s): wav2vec2 + 0.08 / 0.10 s pads already sit on the speech; time comes from words.
- (same) **A line ABOUT the father plays over the FATHER's picture, not the subject listening** ("for this part you need
  to use his father's, not his overlay"): when the words are about someone we have a photo of, the photo wins the cover.
- (same) **Caption colour MIX, third time asked** ("a lot of coloured captions, not just one colour caption, like I've told
  you before"): count it in QA: 37 of 88 captions coloured (1 in 2.4) over all six accents, never one colour twice in a
  row unless it is one phrase split across two captions.
- (same) **Topaz jitter = the stabiliser's "Reduce jittery motions" passes = `tvai_stb ... reduce=N`**: he wants 2 ("just
  below three"), his own 2026-10-10 export log carries reduce=2; `workflows/topaz-iris.py --reduce 2` (default 0). Run
  it per shot (`--segments` at every shot start, `--no-enhance` for 1080p) on the 60 fps Stage A, where 25p repeats are
  exact copies for Chronos.
- (same) **Father photos through Higgsfield, his ask ("Topaz doesn't really do a good job of scaling pictures")**: what
  worked = `nano_banana_2_1` 4k, the soft photo as image 1 + "restore, keep EVERYTHING, use the other images ONLY for his
  facial features" (3 credits). What failed: (1) the plain `upscale_image` (bytedance 4k) left a soft ghost and drew
  letter-like marks by the eyes; (2) giving a YOUNG portrait older references aged him and reframed it 16:9 → restore a
  young photo with NO references and the source pre-cropped to the output aspect (5:4). Check every restore at full size
  for rewritten badges / faces (the regiment beret badge came back as a plausible winged badge: unverifiable, say so).
- (same) **Brief rule "nothing about his death" can be lifted by him for one card**: his opener note asked for "passed
  away"; the card states the date (28 OCTOBER 2026, checked in three outlets), never "yesterday" (false on publish day).
- (same) **The opener "motion graphic in my own style that originates from his head"** = a glow ring on the ear (tracked
  through the zoom-out: point → pivot + (p − pivot) / z), a glow line drawn down the frame edge that turns into the
  card's top rule (AW §5 glow bar), the lt_card NAME / hairline / gold line rising in under the caption line over a soft
  dark scrim (his white shirt behind it). `build/finish.py opener()`. PENDING HIS REVIEW.
- (same) **An over-exposed SD source under his AE grade turns orange and "painted"** (AMN09 360p stage light: cheek luma
  0.89, 7 % clipped): level it BEFORE the grade with exposure (`gain_level` 0.62), a slight soften against the PRE
  sharpen bands (`pre_blur` 1.6 px), desaturation (`sat_level` 0.45) + grain = the brief's "desaturated archive grade".
- (same) **Burned-in lower third on a full-bleed crop: the clean rows must FILL the frame**: LW's bar starts at row 912, so
  `content_y` [0, 905] needs scale >= 1920 / 905 = 2.12 (at 1.9 the clamp centred and showed the bar). And a head lock
  that would drop a high face toward the caption line by mirror-filling the TOP band reflects the top of his head into
  it: never `expose_top` on a face whose crown is near the frame top (rejected sheet `proof/stageA_sheet_exposetop.jpg`).
- (same) **The trial engine's caption turbulence field is 60 s long** (`aw_render.TURB['dur']`): a 61.7 s short crashed at
  61.2 s; lengthen it in the job's finish.py (`R.TURB['dur'] = ...`), never in the shared engine.
- (same, build) **Skin levelling, 4th build in a row: measure on the EXPORT, not only on test stills.** The finish test
  frames looked fine, the first export measured LW R/G 2.21 / LIFE 1.96-2.08 / WDY2 1.87 (his 1.50-1.70): sat_level LW
  0.55, LIFE 0.62, WDY2 0.75 + gamma 0.85, re-rendered as 3 frame ranges (`finish.py render --frames a:b`) and spliced
  (`build/splice_multi.py`), not a full re-render. Pink / red-lit sets (Loose Women, BBC theatre) need it most.
- (same, build) **Topaz per shot is measurable, so measure it**: `win/hold_scan.py` (runs of >= 3 identical frames the
  input did not have) + a high-pass wobble metric. Chronos + stabiliser evened every talking shot, but on a near-still
  listener (LW) and a handheld 29.97p crowd video (CP) it ADDED holds / wobble: those keep Stage A. A 29.97 source needs
  no interpolation for a 30 fps export at all.
- (same, his v1 note) **Under 60 s: HE picks the line, and he picked a MEANING cut, not the shortest tail.** Offered "my
  father. Understand him," (−1.7 s); he cut "because he just made me angry and fearful when he was around" (−3.9 s,
  57.77 s). Next time offer two or three candidate lines with their seconds, including mid-beat explanations, not one.
  A late cut re-renders cheaply in the code kit: picture = old frames minus the removed range, finish only from the last
  transition before the cut, splice (pin anything random-seeded by length, e.g. the caption turbulence field).

**2026-10-31 — "Why Everyone Underestimated Michael Jackson"** (`projects/mj-outthink-them/`, 9th code build): his locked
brief v3 → sequence PREVIEW (45.1 s) → his Tella 1 (letterbox the London footage, HD + Higgsfield parent photos, cut
"shrewd behind it all" and "girl is mine / publishing's mine", Eddie's colour follows Michael's voice, purple dip, Bashir
lip sync, transitions + zooms "you know my rules") → built and DELIVERED v1 ~17:40 (41.37 s, Final Renders + Exports,
REPORT.md). At his review.
- **A Tella on a preview records the preview's SOUND too**: the transcript interleaves the clip's words with his notes. The
  preview's burned tag (beat · source · in-point / preview seconds) read off the Tella frames at 1, 2 and 4 per second
  (`brief/tella/f/labels*.png`) maps every Tella second to a preview frame, so each "this" resolves to an exact moment.
  Keep the tag on every sequence preview.
- **"Fade the colours when he's pretending to be Michael"**: an impressionist's voices separate by pitch + the story
  (`win/pitch.py`: Eddie's own 80-130 Hz; his Michael 140-250, his Paul 180-400). Saturation keys on the line cuts with
  0.2 s fades (faded = 0.22, not grey), and the zoom as chained KEYS in one layer (push-in, +0.04 pull-back per Michael
  line; `finish.py z_at` 'keys'): no reset across the same-camera jump cuts.
- **A 115 px face in a 640x358 stage video cannot take a hard head lock**: the track noise (10-17 Proteus px) shakes the
  picture. Gaussian on the nose track (sigma 6 source frames, `build/smooth_track.py`) keeps the follow; a letterboxed
  lock clamps to the BAND, not the frame (`stage_a.py band_clamp`).
- **Caption base when the talkers' sources frame the head high** (Eddie / Matt / Bashir: the cover clamp leaves lips at
  y720-850): raise the ONE base inside his y940-1130 (`caption_shift` −85 → ~y950-1000) and move the letterboxes and
  photos up to it; a finish-side `lift` (90 px) moves a letterboxed source without re-rendering Stage A / Topaz.
- **An HD interview frame cropped 9:16 is an extreme close-up once letterboxed** (Katherine cut at the eyebrows): crop the
  WIDE frame instead (logo and background photo frames out), upscale that (Higgsfield 4K, 2 credits) and band it.
- **Whisper invents grammar at a joint** ("He's / There's two sides to him" after "lipstick", "going to", "are you",
  "can" for "do"): settle every caption word with forced-alignment hypotheses (`win/fa_hyp.py`) + windowed Whisper on the
  source, and prove the joint with a 5 ms strip (the "he's" scored 0.08: it was the /t/ aspiration of "two").
- **"His lips are not synced" on a question asked off camera**: measure the bilabials (`win/plosive_check.py`, fps-aware):
  in sync within a frame on 7 events (no slip). The interviewer's voice over the subject's closed mouth is what reads as
  unsynced; say so in the report rather than slipping a synced source.
- **One 8 GB card, four sessions**: wait on the holder's pid with a background until-loop (+ ≥ 4.5 GB free), let the parent
  order the queue, run Topaz + finish back to back, then send "card free". Chronos stuttered the near-still listener
  shot (Bashir's question): keep Stage A there (`win/hold_scan.py`), Patrick's rule held.
- (same, my QA after v1) **Scan the FILE for silences, every build**: a 0.56 s room-tone pause sat inside Eddie's last line
  because wav2vec2 stretched "that's" over it (the third stretched word in two days: Patrick's "And", this job's payoff
  "that"), so the piece never split at the pause. A 10 ms RMS scan at 22 dB under speech (> 0.25 s runs) found it (0.66 s)
  and proves it gone in v2. Fix = measured OVERRIDE + EDGES in seq/edl.py, then the late-cut recipe (picture minus the
  frames, finish from the zoom group's changed key only, splice). Whisper's segment gaps in a re-ASR are the cheap tell.

- 2026-10-31 (Conrad Murray "didn't kill MJ", `projects/conrad-murray-didnt-kill-mj/`, his Tella on my SEQUENCE PREVIEW):
  **a brief written from YouTube captions doesn't know who speaks.** The brief gave "None. None. Absolutely nothing." to
  Murray; a two-speaker voice match on the same recording (`win/who.py`: MFCC GMMs trained on known Hayes / known Murray
  speech, LLR per word) showed Murray "None." / Hayes "None? Absolutely nothing?" / Murray "Nothing." Run it on every
  interview exchange the brief attributes; lips can't settle it when the broadcaster laid a reaction shot under the line.
- (same) **"If the camera shot is not actually at him it's not worth it, keep it at the reporter"** (his Tella): never put
  a silent listening shot of the subject under the subject's own words ("he's not speaking but he's speaking, the viewer
  will be confused"); the interviewer on screen is right, and a wide two-shot avoids a same-camera jump between two of her
  close-ups. The reverse (the subject listening under the interviewer's words) is fine (B1 hook).
- (same) **A level dip is not a word edge.** My "Jackson" edge (9:58.72) came from a dip in the level strip: it was the
  /k/-/s/ closure INSIDE the name, and the ASR join test "heard" Jackson anyway (it fills names in). He heard "Jacks-".
  Find edges with wav2vec2 CHARACTER alignment + the spectral centroid (s = 3-5 kHz, n = ~1 kHz) before trusting a dip.
- (same) **Letterbox = his answer for low-quality sources, per shot** (360p courtroom, CNN 720p Katherine), and they
  ZOOM IN while the 60 Minutes HD parts ZOOM OUT ("this is too zoomed in already"). Build the band from the source's
  CLEAN rows only (top + content_y * scale), so a burned-in lower third can't enter it, and set the band top so the top
  glow bar is still below y200 at the END of the push (a 1.16 push moved it from 230 to 173).
- (same) **Labels = lower thirds from the BOTTOM with "a little nice animation integrated with my AW style"**: the card's
  rule as his glow bar drawing out from the centre, the name rising, the role/year following (`finish.py lower_thirds`).
- (same) **His height, measured per shot, not per camera**: the mouth corners must sit at <= 950 (listening), 920 (talking)
  or 890 (a subject who opens wide), the caption block being y~1020-1070 (`win/shot_y.py`); one height per same-camera
  run (head steady across cuts), the most-lifted one. When a lift exposes the bottom, fill it with the blurred REAL bottom
  edge stretched down and darkened (`stage_a.soft_fill`): the Motion-Tile mirror drew a collar "V" and, blurred, his lips.
- (same) **Skin levelled per camera SETUP, not per file**: Hayes and Murray share the 60M file but measured R/G 2.17 vs
  2.7-2.8 under his grade; `sat_level` keyed by setup (M60 0.46 + gamma 0.85, H60 0.55, M911 0.72, H911 0.85) -> 1.5-1.7.
- (same) **Purple added to the caption styles** (his Tella: "white and purple"): his "pink" is already violet-magenta
  (#9D10C0 -> #DE64F1), so purple = a blue-violet (#5C28D6 -> #B08CFF) to read apart from it.
- (same) **Write the catalog pass BEFORE Stage A** (it was written during the build here; it changed nothing, but the rule
  is before the first edit).
- (same) **YouTube: one bot check (HTTP 429) cleared on a plain retry 3 min later; subtitle requests kept 429ing**:
  download video and subs separately so a sub error never aborts the video.
- (same, build) **Topaz on a SHARED GPU can take hours** (the per-shot stb + Chronos pass ran 7 of 49 segments in 25 min
  while another session's finish render held the card). For tripod interviews the head lock already steadies; the 25p
  cadence can be evened IN Stage A with the engine's Horn-Schunck flow in-betweens (`stage_a.interp_frame`, flows cached
  per frame pair, ~2 fps). **Never interpolate across a source cut**: a flow blend of Hayes into Murray made a warped frame
  at two cuts inside the 911 clip (final QA, frame by frame); detect the cut by the frame difference and hold the shot's own
  frame (and its head-lock anchor).
- (same, QA) **`fps=1` contact sheets sample the LAST frame of each second (k + 0.47 s)**: "9 s" showing Murray was 9.47,
  after the 9.43 cut. Pull exact frames by number (`select=eq(n,…)`) before chasing a "wrong picture".
- (same, audio) **A whispered answer can vanish under a transition swish's pre-roll** (Murray's 2nd "Yes", RMS -33 dB vs
  ~-13 dB speech): the final-mix re-ASR caught it. Fix = that piece +8 dB and the swish STARTING on the cut; a label that
  enters with a transition shares its swish. Re-ASR the final mix every time; ASR in long windows drops quiet short words
  from context, so confirm a "missing" word in an isolated window before changing anything.
- (same, his note on v2) **Labels go at the BOTTOM** (README § 8, memory feedback-labels-at-bottom): v3 moved the four
  name cards from y0 230 to y0 1270 (London: y0 1385, on the twin fill under its band) and re-rendered ONLY the card
  frame ranges (`finish.py render --frames`, `build/splice_multi.py`). And **`caption_shift` is positive-UP**
  (`finish.py` samples pre(y + s)): my −85 meant to raise the line moved it DOWN to ~y1135; measure the caption text rows
  on a test still after ANY shift change (white-pixel rows), never trust the sign from memory.
- (same, v3) **`build/splice_multi.py` / `splice_ranges.py` darkened every frame ~4-5 luma levels per pass**: the raw
  yuv420p writer had no input range, so ffmpeg range-converted on the way in (63.8 → 60.2). Caught only because the
  v2 → v3 frame diff showed EVERY frame changed, not just the card windows. Fix: `-color_range tv -colorspace bt709`
  BEFORE `-f rawvideo -i -` in the writer (patched in mj-outthink-them; every other job's kit copy still has it). After
  any splice, diff old vs new frame by frame: only the replaced ranges may change.
