# Abundance Wisdom — LESSONS

One entry per thing a job taught. Newest first. Numbers belong in [README.md](README.md),
procedure in [PLAYBOOK.md](PLAYBOOK.md).

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
