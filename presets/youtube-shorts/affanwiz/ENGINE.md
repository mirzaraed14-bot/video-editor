# AffanWiz · Shorts: ENGINE

Channel folder per the shorts-engine method, created 2026-10-28 when the first AffanWiz Shorts were clipped from his own long-form.
Every number about AffanWiz Shorts lives here, never in Scott Clary's or Abundance Wisdom's files.

- **Read order:** this file, then FINDINGS.md, then the job's row in RESULTS.md.
- **The long-form channel's own look and rules** (a separate thing): `presets/youtube/affanwiz/`.

## The line for one Short
1. **Pick.** From his uploaded long-form's transcript, on the viral bar (`projects/_onyx-batch3-2026-10/VIRAL-BAR.md` A–E +
   AW-VIRAL-STUDY § 6). Send the sequencing to Affan as full text. He may send his own sequence as text: follow it exactly; where his
   text is a cleaned transcript, the captions follow the audio and every difference is listed for him.
2. **Lock the prediction** in RESULTS.md BEFORE upload: Claude AND Affan, the 7-day range, the biggest failure reason, and a 5K/5M
   pre-mortem. Never edited afterwards.
3. **Build** in the Scott Clary YouTube format: `presets/youtube-shorts/onyx-samples-youtube/` kit + CLIENT-SHORT-RECIPE.md.
   - **Read Scott's NEWEST style set first** (Affan 2026-11-05, Short 3: "I've updated its style set and everything so you have to
     [consult] it before you start"): `presets/youtube-shorts/scott-clary/ENGINE.md` + `UPGRADES.md` + `research/shorts-style-radar.md`.
     He keeps changing it, and AffanWiz Shorts follow its latest version, so never rebuild last week's Short. The session that built
     the newest Scott Short can answer questions by SendMessage. Then log ≥ 2 moves new to THIS channel in `UPGRADES.md`.
   - Job folder `projects/<long-form job>/clips/<name>/` when clipped from his long-form; a standalone take gets its own
     `projects/<name>/` (Shorts 3 and 4). Log the job in `presets/youtube/affanwiz/JOBS.md`.
   - A 30 fps check goes to Affan before the 60 fps final. A native 59.94 take needs no frame interpolation: its check IS the final
     if he approves (Short 4).
4. **A note after delivery = data + ONE finish render** (Affan 2026-10-28, Short 1: "everything else is fine, these are very minor
   things, so don't recreate the whole video"). A text fix re-renders the overlay only (`yt_build … --skip picture`), and a level fix
   skips both (`--skip picture,overlay`). Never a new Topaz or picture pass for a note that doesn't touch the picture. The exact
   commands per job are in its BRIEF ▶ STATUS.
5. **After 7 days** (never sooner): views, stayed %, average view %, subs, feed % into RESULTS.md, then the post-mortem into
   FINDINGS.md.

## Format overrides for his own channel (2026-10-28; open items marked)
- **Same as Scott's:** no music bed (he scores), transition swishes only, hook card 0–3 s on his cam, face cam ≤ 4 s, YouTube-tight,
  sharpen every render, only his words and numbers on screen.
- **Differs from Scott's:**
  - The watermark is "@AFFANWIZ".
  - **OPEN:** a Skool CTA in the picture, or clean like Scott's with the link in the description. Built clean until he says.
  - **The credit tag (Affan 2026-10-28, "no one cares who I am"):** a result, never his name. Small line VIRAL FACELESS
    CREATOR, big line 530K+ SUBSCRIBERS (update the number when he gives a new one).
  - **Hook = his sharpest call-out line, never said twice (Affan 2026-10-28, Short 1 v2).** His spoken opener and his conclusion said
    the same thing ("they're not stupid"). He moved the conclusion ("YouTube specifically is not stupid … to get their channel
    monetized") to the top, cut the opener, and ended abruptly on the list. When the last line is the strongest, open with it.
  - **Length: 45 s or less, preferred (Affan 2026-11-04, Short 2 note: "the short shouldn't be more than preferably like 45
    seconds").** Measure the kept spans, subtract the YouTube-tight pause slack, add the joints; never estimate.
  - **The explanation beat gets motion graphics (Affan 2026-11-04: "especially the Michael Jackson explanation bit you have to
    create like motion graphics there so that the point is better conveyed").** Where he explains the method with his example,
    build ONE continuous motion-graphic scene whose picture IS the point (Short 2: an angle map whose empty slots Claude fills
    later), never a row of text cards.
  - **The most value first (Affan 2026-11-04: "the best sequence possible … with the most value possible").** Pick lines for
    what the viewer can copy (the method in order, the time it saves, the exact prompt held on screen to screenshot), and use
    his real systems as receipts: his posted AW Shorts, never mock-ups. A line he asks for goes in with his words as recorded
    (he remembered "a few minutes"; the tape says "10-20 minutes", so the card does too).
  - **Transcribe check:** WhisperX heard his "which" as "with" ("clip which Speed uploaded himself"). Read every caption chunk against
    his own text sequence before the check render.
  - **The hook card sits ON the caption line, and the captions take its place when it leaves (Affan 2026-11-04, Short 2 review 1:
    "the hook text should directly be in front of captions so when the hook text timer finishes you swap it out with captions").**
    Two lines centred on the seam (y 1041 / 1143 around 1092), never below it. Captions start with the first chunk AFTER the hook
    question; the question's own chunk is dropped, so the card's words never flash a second time. The watermark waits until the
    card has gone (3.2 s).
  - **No stutter, no breath pause (Affan 2026-11-04, review 1: "some awkward silences" and a word said twice).** WhisperX folds a
    repeated word into its neighbour ("covered" held his first "the"), so read the energy at every joint, not the transcript:
    `work/cut/pause_scan.py` and a 5 ms dB + zero-crossing profile tell a word, an "s" (6 kHz hiss) and a voiced "mm" (1 kHz) apart.
    A Whisper re-listen is a hint only: its prompt biases it ("the, the" in the prompt made it hear one). **Scope (review 2):** this tight
    pass is for the audio under the motion graphics; on his FACE a pause goes only when it removes >= 0.3 s (the next rule), because
    every cut there moves the camera.
  - **Real photos in the motion graphics, never a stylised cover crop (Affan 2026-11-04: the map's centre circle "doesn't look
    good").** His AW covers are heavy-graded; for a subject portrait use a real, sharp photo (Short 2: Alan Light's 1988 photo of
    Michael Jackson, CC BY 2.0, credit in the description).
  - **No jump cut on his face for a micro-pause, and head TRACKING on every face shot (Affan 2026-11-04, Short 2 review 2: "the
    camera just constantly moves up and down … it just kind of snaps with my head … especially in the first 5 seconds … my face will
    be in the middle and each cut will just feel very smooth").** Review 1's tight pass had cut 0.03-0.13 s quiet runs inside the hook:
    six jump cuts in 3.4 s, the camera stepping 10-148 px at each for 1-8 frames saved. Under the motion graphics the tight pass cuts
    freely (nobody sees the cut); while his face is on screen a pause goes only when it removes >= 0.3 s, and a real pause at the start
    of a face line goes onto the scene change (the face shot starts on the next word). Track the eyes on every frame (`head_track`,
    `head_edge_pin` 12, eye line `fy_out` 0.31, z0 1.2 where his head dips), never the chained lock. Gate the BACKGROUND
    (`projects/viral-clip-method/clips/find-viral-angles/work/bg_step.py`), not only the eyes: a head lock pins the eyes by design.
  - **The hook card stays until the question ends:** when the spoken hook runs past 3.2 s, `hook.hold_end` holds the card so it slides
    out as the next scene whips in (Short 2: 3.10 s, gone at 3.97 s); captions and @AFFANWIZ start there.
- **His face reads the script in places** (sunglasses, so measure head pitch AND yaw): every reading span sits under a receipt or a
  card (`presets/youtube/affanwiz/PLAYBOOK.md` rule 2).
- **A theme colour he names for one video is a per-video override (Affan 2026-11-09, Short 4: "green instead of yellow: captions and
  motion graphics green, and green gradients").** It goes in the job's spec (`captions.palette` emphasis voice, `hook.grad`) and
  job-local card code, never the kit's locked yellow. The caption BASE stays white and only the emphasis words take the colour
  (Short 4 v1 turned every caption green, caught at the check). Show the colour on real test frames of his skin and room before the
  build. The next video goes back to the kit colour unless he names one.
- **Scan his hair for specks at full size, on the finished picture too.** On C1453 and C1454 he asked for a dandruff speck to be
  removed. The second speck on C1454 was 4x fainter and only showed after the upscale, Topaz and sharpen. The method and its proof
  are in `LESSONS.md` (Short 4) and `presets/youtube/affan-afterhours/LESSONS.md` (C1453). His OK on the method is still pending.
- **The opening is now Scott's newest format (Affan 2026-11-05, Short 3 sequence, "Yes, use defaults"):** captions + @AFFANWIZ from frame 1 on the seam, the hook card below them (y 1340 / 1436), the card holding until its line ends. This reverses his 11-04 note above ("hook on the caption line, captions take its place").
- **POP grade + stronger sharpen on every render** (`workflows/grade-picture.py`, `sharpen-picture.py --mask 0.55 --sharp 0.40`), and the steady `drift` 0.025 on every face shot, from Scott's set, starting Short 3. Gate his skin hue in this warm room.
- **Decided again on Short 3 (his defaults, 2026-11-05):** on his own face only pauses that remove ≥ 0.3 s go (Scott's every-pause-closes runs under cards only); the credit VIRAL FACELESS CREATOR / 530K+ SUBSCRIBERS sits on the top-level scene, not in the first 3 s; no Skool page in the picture ("digital product" stays generic); a spoken joke ("19 crisp dollars") gets a swish, no slow-mo or boom, unless he says so.
- **A spoken number beats the script's** (he said "around 4,000", the script ~$3,800): the card says what the tape says.
- **Put a jump cut on a scene change, never on his face (Short 3 build, 2026-11-06; from his Short 2 review 2).** A pause he reads in is long, and his head moves during it, so the joint steps the camera 25-29 px even with head tracking. The ≥ 0.3 s rule above says which pauses go; this one says where the cut lands: move the line under a card so the face shot starts after it. Gate per strip (`projects/what-level-shorts-creator/work/bg_strips.py`) and trust a strip only with a phase-correlation response above ~0.5.
- **The POP grade is aimed per room:** test a still first (`grade-picture.py --test`, spec `grade_look`). His dark warm room needs a lit face and less skin saturation, not more contrast.
- **Short 3's check 2 passed on a bare "approved", no notes (2026-11-06).** One data point, not a default: it carried lines under a big built object instead of jump cuts on his face, one object across the Short, numbers that rise whole, and the POP grade aimed per room.
