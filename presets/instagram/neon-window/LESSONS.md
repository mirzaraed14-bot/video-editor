# Neon window: LESSONS (lesson → change made → file)

## 2026-10-22 · Review 1 (Marvel IG Short v1.1, `projects/_client-scott-clary/marvel-board-vs-rdj-ig/`)
Affan, verbatim: *"too glowy and i prefer you don't do the grayed out style and at 20 sec the sfx sounds goofy same with 38 sec it
needs to sound expensive"* (with a screenshot of the "$525 million" stage type).

1. **The neon is a hint, not a bloom.** Mark Brazil's measured glow (two blurs at full gain) read "too glowy" on our stage type.
   → Glows cut to about a third: stage hero (20 px, 0.32) + (5 px, 0.28); inline hero (10, 0.35) + (3, 0.3); white type (6, 0.22);
   name card (10, 0.35) + (3, 0.3); credit bar 0.5; diagram line 0.45; the strike ramp starts at 0.4, not 0.25. → `ig/build.py`
   (GLOW_*), README § numbers.
2. **No black-and-white.** The DOAC reference was B&W, but he wants the window in COLOUR: dark and neutral-cool like Mark's studio
   (gamma 1.35, contrast 1.08, saturation 0.85, a slight cool tint; stills gamma 1.15 / sat 0.92; the stage a dark slate). The low-key
   relight (room falling to black from the top) stays, a touch lighter (205/255). → `grade()` in `ig/build.py`, README.
   Consequence found in the frame checks: in colour, red type can sit on a red picture (RDJ's armour, the booking shirt). The dark
   halo behind red type goes up to (16 px, 2.2) and the name card's to (14, 2.4); the caption-band scrim on stills to 0.88.
3. **"Expensive" sound = no electric family, no narrow tones.** The two flagged cues were a neon tube stuttering on (20 s) and a
   "dramatic" short riser (38 s). Measured: their tonal prominence above 1 kHz is 38 dB and 25 dB (a narrow tone, the same thing as
   the 2026-10-08 "cricket" swells); every sound he did not flag measures 8-16 dB. Also out by the standing rule (never electric /
   UI): the neon buzz on the credit and the name card and the fluorescent hum on "lights came on". → Replaced with cinematic
   swells INTO reveals and reverberant impacts ON them: a trailer reverse swell peaking into "10 characters", a low riser peaking
   as the red line reaches 2009 + a soft reverberant impact, a clean sub impact on the credit, a reverberant thud on the name card,
   a big stage-light clunk on "lights came on". → `ig/sound.py`; the check is in README § Sound.
   **Rule from now on:** before a sound goes in, measure its tonal prominence above 1 kHz (p90 of max-bin vs its ±40-bin
   neighbourhood over the loud part); > 20 dB = reject.

## 2026-10-23 · Review 1 of the War Dogs IG Short (`projects/_client-scott-clary/war-dogs-fake-office/`, "it's good but…")
Affan: no head tracking at all in this video; no captions for the duration the hook text is up ("the first 3-4 seconds look so
cluttered: the captions, the text box, the podcast tag"); the sound under the counter climbing to $300,000,000 "should be something
else, a lot more subtle, minimalistic… a weird sound effect… definitely lower in volume".

1. **No head tracking.** The eye-locked crop (per take, smoothed) is out: ONE fixed frame for the whole video, anchored on his median
   eye position (846, 341 in 1080p), the approved pushes zooming toward that fixed point. → `ig/build.py` (EX0/EY0, `cam_frame`).
   This overrides the 2026-10-19 head-steady-across-cuts lock for this look until he says otherwise.
2. **The hook card owns the screen.** While the hook text (and the name tag) is up, there are NO captions; they start on the first
   word after it ("War Dogs" at 3.3 s). → BLOCKS in `ig/build.py`. Apply from the start next time: a hook card = a caption pause.
3. **A climbing number gets a breath, not a riser.** The clean "build-up" riser under the counter read as weird and loud. → a slow,
   broadband dark airy swell (`wd-swell-dark-airy.wav`, Epidemic 0ea4c198; 14.8 / 10.3 dB tonal) at 15 dB under the voice peak
   (~10 dB lower than the riser), its slice ending on the swell's peak as the number lands; the landing boom unchanged. → `ig/sound.py`.
Patched, not re-rendered: `build.py --patch` re-rendered only the cam shots and the hook (0-200, 560-700, 930-1005, 1540-1610,
2545-2670 at 60 fps), the rest of the picture passed through.
- 2026-10-24 (Brad Lea Ferrari IG, in-studio multi-camera, 30p source -> 60 fps Chronos): (1) a FIXED frame per take, placed so the head doesn't jump at joints (<= 9 px drift), beats head tracking on studio shoots; (2) push-ins (10-15 % within ~0.9 s) anchor on the MOUTH so the lips stay above the caption spot; (3) hold the zoom at 1.00 while type sits above the head (it touched the hair); (4) watch the speaker leaning down at a close-up's first cut (lips dropped under the captions: start the shot half a line later); (5) Epidemic files rejected by the narrow-tone check: phone-buzz, riser-dramatic, riser-reverse-layers; a small reused set repeats (pen stroke 5x, low boom 4x): source a wider set per job.

## 2026-10-25 · Chris Do "$150 sneaker" IG Short (`projects/_client-scott-clary/chris-do-sneaker-pricing/ig/`, Affan: "make the style and everything 1% better this time")
What it did better than the War Dogs IG (the BRIEF's § IG variant has the full list):
1. **The hook is Mark's stage shot**: the whole webcam frame small at the window bottom (`hookstage_frame`), the promise in the dark
   band above, the mono credit beside his head; no captions under it (they start on the first word after, 2.65 s).
2. **Mouth-anchored fixed frame per take**: every cam shot puts his median mouth at window y 590 and the pushes zoom ON it, so the
   caption top keeps a measured gap under the lips at every zoom (`lips_check()` asserts >= 20 px; tightest 43 px).
3. **One object that returns and evolves** (Mark's floating artifact cards, Brad's receipt): the sneaker lit with its price -> inside a
   floating sponsored-ad card -> beside its $150 fake -> lit again on "a different kind of buyer". The marker ring + FAKE are drawn
   strokes, never a font or a stamp.
4. **A number that climbs is a hand-drawn line chart** (Mark 10-23), point by point on each spoken number, under a quiet airy breath.
5. **Sound measured three ways** before it goes in: tonal prominence (<= 20 dB), the slice starts on its measured attack (envelope
   events listed per file), and `ig/cue_check.py` (premix - voice = the SFX alone) proves each crest lands on its frame and every cue's
   50 ms loudness sits >= 3 dB under the voice beside it (worst -6.4 dB). First pass had four cues as loud as the voice (a stinger,
   two thuds, the landing): lowered 3-5 dB; transients measuring 14-18 dB under (card slide, tag tap, chart dot) raised, since
   "quiet ticks read as none".
Caught by the 60 fps frame check, the proof sheet and the review pass (all fixed before delivery):
- **A floating card under the show bug**: the 640 px ad card at y 40 ran its corner under SUCCESS STORY. -> card at 90 % with its top
  at y 92 (bug bottom 74), all its marks scaled with it (AS). Rule: anything near the top of the window starts below y 80.
- **A hero phrase wider than a line orphans its neighbour**: "different kind of buyer" in red Playfair was > 620 px, the layout
  cannot split inside a red run, so "a" sat alone on line 1. -> hero = "different" (the stressed word). Rule: a red hero is one or
  two words; check every block's line count before rendering.
- **A drawn mark must arrive with its object**: on the callback the pair's FAKE was drawn at full strength while the shoes and prices
  were still fading in (0.35 s), so it floated alone under the burn. -> `hand_stroke(..., alpha=)` and `draw_fake_word(..., alpha=p)`;
  patched 962-1000, 1824-1850. Gotcha: `hand_stroke`'s own loop rebinds `a` to a point, so a fade argument named `a` is clobbered
  (the first patch died at the first drawn frame): it is `alpha`.
- **Every drawn stroke gets a sound, even a repeat**: the FAKE re-written under the pair's $150 (16.18-16.58) was silent, only the card
  slide 0.15 s earlier had one. -> the marker `write` slice again at 16.18, 9 dB under (24 cues).

## 2026-10-25 · Review 1 of the Chris Do IG Short: "the sound effects need to sound expensive and premium"
1. **Cheap = what a phone plays.** Measured: v1's cinematic hits (deep thud, airy hit, soft stinger, low thud) sat 25-41 dB down in
   300 Hz-6 kHz, so on a phone they vanished and only the foley came through: 8 soft taps, marker squeaks, pencil strokes, a card
   slide. -> One cinematic family only (trailer impacts, a hall tom, taiko, a reverberant impact, reverse swells, deep and clean
   whooshes, single soft deep thuds); no taps, no foley. -> `ig/sound.py` v2.
2. **Split the crack from the weight.** Every hit is HIGH-PASSED (70-150 Hz) before it is peak-normalised, so its crack, not its sub,
   sets its level; the weight is ONE sub-boom layer under the big moments (hook, the landing number, the callback).
3. **Check in the phone band, cue by cue.** `ig/cue_check.py` now renders each cue ALONE at the mixer's gain and reports it against the
   voice beside it, full band (>= 3 dB under, plus the whole SFX bus) and in 300 Hz-6 kHz (WEAK below -20 dB). v2: loudest -5.2,
   none weak. Also re-run the tonal test on the final SLICES: a trailer swell passed as a file (18.3) but its peak slice measured 20.2.
4. **A hit is placed by its attack, a swell by its crest.** Three hits had been placed by their 5 ms peak and started 100-140 ms early.
5. **Repeats get pitch steps, never the same sample 5x.** The thread's five thuds: his asks step up (0.94 -> 1.0 -> 1.06), the
   client's "Yes" sits low (0.89), each a dB louder; and check a "single" library hit is not a double (cd2-thuds-deep is 2 hits each).

## 2026-10-26 · Morgan "claw machines are rigged" IG Short (`projects/_client-scott-clary/morgan-claw-machine/ig/`, "start the ig variant")
What it did better than the Chris Do IG: Mark Brazil's CURRENT hook (checked @markbrazil 10-26: white bold sans, the promise words on a
flat red box), his camera floating as a card; transitions carry the motion (3 burns, one blue-edged; a red ink bleed into the $ card,
FX-15; a 0.3 s settle-in push on every other cut into B-roll or a card; hard silent cuts back to his face) and the only sound; the
cards are catalog moves (FX-28 dossier readout + FX-35 blur-isolate rows + FX-69/74 "1 in 20" marks; FX-11 $ split + FX-24 dashed arc
to a notched tag); the bunny returns (FX-79). The catalog pass is in the job's BRIEF.
1. **B-roll at exactly 60 fps, not x2.** Stock is 23.976 / 25 / 29.97: Chronos x2 gives 47.95 / 50 / 59.94. -> Topaz's tvai_fi with
   fps=60 on each span used (+0.5 s), frames mapped by TIME (`ig/tools/broll60.py`); qa.py measures frozen steps per shot (worst 4.3 %).
2. **A tight face crop wants a 4K plate.** Zoom 1.46-1.72 from a 2560 plate upscales his face 6-25 %. -> each cam shot as its own 4K
   Chronos plate (`ig/tools/cam4k.py`, 239 source frames, a few minutes); the 2560 plate only feeds the small hook card.
3. **A joint he turns through is ONE Chronos take.** As separate takes the cut gets no in-between frame and the take's last frame is a
   clone: his eyes stalled, then jumped 32 px (median 9). One take: no stall, 17 px across. (The YT's smooth_through, IG side.)
4. **Measure the head on the EYES.** YuNet's mouth corners move with speech (+-10 px): the same frames re-encoded flipped a joint
   verdict. qa.py now steps the eye midpoint across each in-shot joint against the median step around it.
   SUPERSEDED 2026-10-28 (Patrón #2-3 below): the eyes move with a head TILT; chain and judge on the face-box centre, prove steadiness
   with the 4K residual, and keep the window detector as a snap catcher only.
5. **Frame 0 is the preview.** The hook faded in from black, so IG's first frame was dim text. -> the whole hook (title, red box, cam
   card) on frame 0; the tag decode and the bunny pop keep the motion.
6. **An ink bleed is bright and wet, never a dark splat.** First pass: the blot inherited the dark stage (maroon) and a spiky edge
   (high-frequency noise). -> low-frequency organic edge, 22 px smoothstep feather, a thin white rim, bright red that holds to 60 % of
   the transition then clears; its radius reaches past the window corners (880 > 800 px).
7. **A floating object never covers his face**: the payoff bunny sat on his cheek at 300 px; in a tight close-up it goes in the free
   top corner (905, 300) at 250 px.
8. **No fire, no crackle under a burn.** A light-leak burn suggests a flame sound, but Epidemic's "burn up / flare" files crackle (6 and
   4 sharp onsets, > 8 dB in 15 ms, after the crest) or hiss (62 % above 4 kHz): the foley texture that reads cheap on a phone. -> clean
   whooshes rising into the cut; the check (count onsets after the crest + the share above 4 kHz) runs on every slice before it goes in.

## 2026-10-28 · Patrón "would never sell more than 20,000 cases" IG Short (`projects/_client-scott-clary/patron-20000-cases/ig/`), 30 fps check
What it does better than the Morgan IG: Mark Brazil's NEWEST type (his reels moved on in two days: 10-26 = white sans + a red box;
10-28 = white bold sans with a soft bloom + red glowing serif italic, numbers as stat lockups: tiny caps label / big serif number /
tiny caps label); ONE chart that keeps its state across five reprises (FX-73 + FX-70), the payoff a pull-out; the bottle returns three
times; a glass-glint light sweep (new); 15 different subtle swishes. The catalog pass is in the job's BRIEF.
1. **Re-check the reference before EVERY video**, even two days on: Mark's title treatment had changed (rule 5 is not a formality).
2. **Chain takes on the FACE BOX, not the eyes.** At a head TILT the eyes drop 43 px while the head barely moves; a frame that followed
   the eyes jumped the whole room (the lamp moved 15 px). -> `head()` = YuNet's box centre; a joint is a jump above 15 4K px and 2x the
   steps beside it (s08 698, s22 1838 / 1880 moved; s16 1335, the tilt, did not).
3. **Prove head steadiness from the 4K data; the window detector only catches gross snaps.** The proof: at each joint inside a cam
   shot, residual = (face-box step - the anchor shift applied) x window scale; here every joint <= 10.4 px (the three real jumps 0.0,
   the 1335 tilt 10.4 vs 8.4 px of motion beside it) -> keep it <= ~9-12 px (`ig/work/residual.py`). YuNet on a 600 px face filling
   the window gives 10-25 px of landmark noise (it said 22-28 where a gridded before/after pair showed no jump), so qa.py detects at
   half size and fails only a step >= 30 px and 3x the median around it (the YT's snap was 202 px): a catcher, not the proof.
4. **A reprise opens on its label, never on an empty chart**: the top label comes up with the words leading in, the number lands on
   its own word (`lockup(..., t_label=)`). An empty number string must not reach `big()` (it divided by zero at the payoff).
5. **Subtle mode for Shorts he scores himself**: transition swishes only, each 19-23 dB under the voice beside it (cue_check's subtle
   bands: LOUD > -18, LOST < -25), no slice with > 12 % of its energy above 6 kHz (the "hiss on a phone" note; two wide swooshes at 22 %
   were swapped for darker whooshes).
6. **The shared GPU lock only works if everyone takes it**: a Topaz pass started outside `lock.sh` ran beside a lock-queued one and one
   segment came back empty. Hold GPU jobs when the main session asks, and stop your own task (TaskStop) rather than killing PIDs.
   (2026-10-31 #5: TaskStop ends the shell, not a running render's children; let it finish or give the restart its own output.)

## 2026-10-29 · Daymond John "$30M card chain" IG Short (`projects/_client-scott-clary/daymond-card-chain/ig/`), 30 fps check
What it does better than the Patrón IG: Mark Brazil's type moved AGAIN (10-29: a small white sans line over a big white serif-italic
line, the key word on a red box); the receipts are CARDS because the story is cards (the hook's camera card flips over to Kevin wearing
the necklace, Aoki and Gary flip in as graded slabs, every other receipt floats as an artifact card, the necklace returns full-window);
13 swishes sized to their motion (flip / burn / settle families). The catalog pass and the 1 % list are in the job's BRIEF.
1. **A card flip passes through zero width.** `soft_shadow(rx = width x sx)` divided by zero on the flip's first frame (sx = 0): NaN
   pixels, cast to uint8 = a garbage column. numpy only warns ONCE per line, so the log showed one warning for three flips. -> any
   radius / scale that an ease can drive to 0 returns early (`rx < 1`), and a `RuntimeWarning` in a render log is a defect: patch the
   frames it touched (`--patch`).
2. **The hook may run to the YT's shot edge when its picture IS the hook.** The 0-3 s rule moved to 0-3.70 s here because the flip to
   Kevin wearing the necklace is the hook's payoff picture; captions start after it (3.75 s). Name the choice in the BRIEF.
3. **A hook card must never read the frames the podcast cut away from.** The cold open's cam card reads frames 0-51 only
   (`min(frame, WIDE x fps - 1)`); the wide shot (52-165) is covered by the flip and the necklace. The 60 fps hook plate is cut to
   the same 0-51.
4. **Swish takes are checked one by one, not by family.** Two "soft" Epidemic takes crackled or vanished on a phone (-32 dB); dry
   whooshes from earlier fresh sets replaced them, and two that measured LOUD were trimmed by dB until cue_check read 19-23.
5. **Seek half a frame early.** `Source._open` passed `-ss {i/fps:.4f}`: 761/30 rounds UP to 25.3667 and ffmpeg starts at frame 762,
   so every shot whose reader opened on a frame = 2 mod 3 (at 30 fps) read ONE FRAME AHEAD: lips 33 ms early, a frame of the podcast's
   wide shot inside the hook card, and the head-lock anchor switching one frame after the picture = a 25-34 px head jump at real
   joints (qa read 26.8 / 27.2 px, under its 30 px snap bar). -> `-ss (i - 0.5) / fps`. Patrón and Morgan's ig/build.py carry the old
   line: Patrón's shipped 60 fps final reads each cam shot from frame 0 of its own plate (unaffected; a B-roll clip may start one
   frame late, harmless), its 30 fps check read the cut mid-file (exposed); Morgan not checked. A `--patch` run reopens readers
   mid-shot, so the bug showed there first. INCOMPLETE for an h264 base: add `-fps_mode passthrough` too (2026-10-31 #6).
6. **Ease a push between REACHABLE end centres.** Clamping the crop centre each frame stopped the Oscars push dead when it met the
   photo's edge mid-move (a jolt qa flagged as a stray change at 23.4 s). -> clamp the two end centres at their own zoom, ease between
   them (the chord stays inside: the crop side is convex in z).

## 2026-10-31 · Mark Pincus "he ignored it" IG Short (`projects/_client-scott-clary/pincus-ignored-facebook/ig/`), 30 fps check
What it does better than the Daymond IG: Mark Brazil's type moved AGAIN (10-31, "Ronnie Fieg / 15 Years of Kith": a small sans name
label over a big BOLD SANS title, the key words on a red box, no serif); the hook deals the receipt BESIDE his card on its word (his
card carries the credit, so "Zuckerberg" lands on frame 0 without the credit naming the wrong face), then TheFacebook grows into the
screen; five read-along highlighters on the web pages (FX-34) and a hand-drawn circle on Parker; his head pinned at every jump cut.
1. **A speaker who leans needs TRACKING, not one fixed frame per take.** Pincus moves 200-300 4K px inside a take: a fixed frame put
   his lips under the captions (-103 px) and one take off the top of the frame. The approved YT tracks every frame (Affan 2026-10-20);
   so does this: a calm Gaussian (sigma 12 frames) of the FACE-BOX centre inside each take (every cut joint bounds one), plus the
   shot's mouth offset, clamped to the 4K frame.
2. **Pin each take's EDGES to the head actually there.** Free per-take averages left the two sides of a cut up to 112 px apart (a
   visible head jump). -> on the first and last frame of a take the track equals the detection there, a cosine fade over 15 frames
   (half the take when it is short, so both edges land): every measurable joint 0-2 px (the 15th is under his hand). Proof:
   `ig/work/residual.py` (track step vs face step) + `ig/work/check/sync2.py` (frame matching).
   Where the 4K frame stops the crop (he sits high in s09 and leans back 222 px at 954 in s11: at the common mouth pin the crop
   met the frame's top and the head jumped ~100 px at 954), give that SHOT its own pin (`"pin": 410`): both takes stay inside
   the frame and the cut is seamless; the shot is entered from a receipt, so its higher framing is not a same-camera punch-in.
3. **Hands read as faces.** YuNet scored his raised hand as a face for 7-10 frames at a time (x ~1000 px off, boxes 15-27 % too big):
   out by x distance from the take's median and by box size; his real fast moves are vertical and stay in.
4. **A fast move at a take's start bends a line fit.** He sits up 330 px in 17 frames at 197: the edge fit is quadratic, and the edge
   pin uses the detection ON the edge frame.
5. **TaskStop on Windows ends the shell, not its children.** A stopped `run.sh build.py` chain kept rendering (uv -> python ->
   ffmpeg) and a second build wrote the same picture file. Let a running chain finish, or give a restart its own output path.
6. **Seek half a frame early AND decode in passthrough.** With an h264 base (this cut), `-ss (i - 0.5)/fps` leaves a half-frame gap
   that ffmpeg's constant-rate rawvideo output fills by sending the FIRST FRAME TWICE (601 frames from a seek at 711, not 600), so
   after every reader reopen the picture ran one frame late, and the head pin landed a frame off at the joints (QA read 32-44 px
   "snaps" that the face data said were 0). -> `-fps_mode passthrough` on the reader. Daymond's ProRes base did not duplicate (its
   check and final are unaffected). Found by `ig/work/check/sync2.py`; read its WHOLE output (a `tail` hid the per-shot summary).

### 2026-10-31 · Affan's note on the Pincus IG check (STANDING RULE for every IG variant)
**Captions: one solid line, no word-by-word reveal.** His words: "we are not going to do the ... caption animation ... where the caption
appears one by one ... we're just going to do one solid caption line ... 4 words per caption layer and a slight bump animation which goes
from down to up just a little bit ... very subtle but it looks very smooth easy eased ... there's too much going on right now in the
videos that we are making with the motion graphics ... we need to simplify our caption animation a lot more". Everything else on that
check was approved as is.
-> each caption is ONE line of up to ~4 words (chunked on the phrasing, never split in two), it appears WHOLE on its first spoken word and
rises 14 px into place over 0.3 s, eased in and out, fading up in 0.12 s; the next line replaces it. Position, type, the red Playfair hero
(1-2 words), the punctuation rule and starred profanity stay. Kit: the Pincus `ig/build.py` (`CHUNKS`, `make_blocks`, `draw_captions`,
an assert that every line carries exactly its chunk's words). README § Captions updated.
7. **A podcast stream can be 25 fps dressed as 30.** The Pincus RSS 4K stream repeats a frame every 5th frame (a step of ~0.1 vs
   0.7-3.0). Chronos x2 replaces each repeat with a properly timed in-between frame (the 60 fps final moves more smoothly than the 30 fps
   check), so a 60 fps sync test must leave the repeats out or it reads them as a lag (`sync60.py`: REPEAT). The same Topaz behaviour is
   in the Pincus YT final.

## 2026-10-31 · Kevin Pollak IG sample (Onyx batch 6, `projects/stillhere-pollak-acting-class/ig/`), builder lessons
1. **A 1080p podcast source builds the 30 fps check from the cut itself** (`SC` = 1, faces in 1080p px), the 60 fps final from the
   Topaz 4K plate (`SC` = 2): one `base_frame(t)` switch, the tracking and the window math unchanged.
2. **A shot's zoom keys by word text must anchor repeated words** (`wt("what", wt("have"))`): the first "what" put a key 18 s
   early and the zoom stepped 27 px in one frame at 767 (QA r1). The stage stacks keyed to word starts landed ~0.2 s late where
   WhisperX ran late: re-time those words from the envelope, never the stack.
3. **Stage stacks follow the caption punctuation rule** (they ARE the caption on their beat): no commas (QA r1).
4. **Faces for IG cam shots that the YT covers with cards** are not in the YT faces.json: scan an IG-only spec (`ig/spec.json`,
   A shots over every cam span, `yt_faces.py --dir ig`).

## 2026-10-31 · CrossExamined IG sample (Onyx batch 6, `projects/crossexamined-300k-house-check/ig/`), builder lessons
1. **Batch 6 (TFTS, CrossExamined): captions run from frame 0, under the hook title too**, by the coordinator's call citing CLAUDE.md
   Rules ("never suppress them under a hook or graphic unless told"). This CONFLICTS with Affan's own War Dogs review note above ("no
   captions while the hook text is up"), which still stands in the README and memory: OPEN for Affan to decide. Layout used: the hook's
   cards shrink (two 460x330 landscape cards) to sit between the title and the caption line.
2. **Pin head x on the EYES, y on the face box** when the speaker TURNS across a joint: the box centre moved 16 px but the eyes 38 px
   at joint 171, and a box-pinned crop let the eyes jump 47 px (now 18 px vs 10 around). A tilt moves the eyes in y (the Patrón
   lesson), so y stays on the box. And the take-edge pin takes the MEDIAN of the 3 detections nearest the edge: one outlier box on the
   edge frame was pinned exactly.
3. **Derive the frame count from the cut** (`N30` from ffprobe of outputs/<job>.mp4): a re-cut added 2 frames and the hard-coded 805
   truncated the last word's tail by 0.08 s.
4. A stage beat can carry ONE object through its states (the check dealt → memo circled → flown into a PRICE tag that inflates →
   returned stamped) with the shared drawing module `work/gfx.py`, so the YT cards and the IG window show the same object.

## 2026-10-31 · True Crime Obsessed IG sample (Onyx batch 6, `projects/tco-balloon-boy-acting-class/ig/`), builder lessons
1. **Two hosts, one window: keep the show's two-up SIDE BY SIDE** (two portrait panels, a 6 px white line, each crop inside its own half,
   each mouth on the window's mouth line); a stacked top/bottom split cannot fit a whole face in a 361 px panel without crossing into the
   other host's half. Each host gets their own tracker (faces.json per key) and a line of captions never sits on the OTHER host's face:
   it ends at the show's cut to them, but never before its own last word (`make_blocks`).
2. A drawn picture behind stage type needs its own camera and a dim ramp: white silhouettes under red Playfair read as noise; dimming the
   rows the stack uses (x 0.35) and keeping the red marks bright at the bottom made both legible.
3. A hook that fades out before a stage beat fades in leaves black frames: overlap them (hook out over 0.14 s, the lead-in rising 0.12 s
   early).

## 2026-10-31 · Roofing Insights IG sample (Onyx batch 6, `projects/roofing-cash-you-hide/ig/`), builder lessons
1. **Frame 0 shows the first caption line at full strength**: the 14 px rise starts at alpha 0, so a line timed to 0.00 was invisible on the
   preview frame; `draw_captions` now places a block that starts on frame 0 already risen.
2. **Two people on two cameras = one tracker per person** (`FACES[who]`, `SID_WHO[sid]`), each take pinned at its edges; ZB 1.45 puts a
   studio close-up's face (~385 of 1080 px) at ~540 px in the window, mouth at y 570, lips >= 26 px over the caption top.
3. A guest's credit stack (mono role + a two-line name) sits top-right under the bug: a cap brim fills the window's top middle on a tight
   close-up and a left-side stack landed on it.

## 2026-10-31 · Drinkin' Bros x Tom Berenger IG sample (Onyx batch 6, `projects/drinkinbros-berenger-inception/ig/`), builder lessons
1. **A webcam that frames the guest LOW** (mouth at 53-66 % of the source height) cannot reach MOUTH_Y inside the source: lips_check read
   -173 px. `inside(..., floor=False)` lets his window run past the source's bottom (black under his black tee, melted by CAM_LOW).
2. **Two tracked faces in one kit**: faces.json keyed per person (`FACES[key]`), a shot -> key map (`SIDKEY`), and a `freeze` on a cam
   shot (Ross's window holds his frame 124 over the program's 5-frame flash of the guest).
3. **The hook's listening card from frames outside the cut**: a separate clip of the guest's silent reaction (51 frames before the program
   cut away), shown at 0.9x over the 57-frame hook; declared in the BRIEF as a cutaway.
