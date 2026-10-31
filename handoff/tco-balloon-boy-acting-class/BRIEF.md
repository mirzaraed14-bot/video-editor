# tco-balloon-boy-acting-class: Onyx sample Short for True Crime Obsessed (Patrick Hinds & Gillian Pensavalle) (batch 6, TOP priority)

## ▶ STATUS: resume here
- **2026-10-31 ≈20:10 DONE: BOTH FINALS DELIVERED** (30 fps native per Affan 18:30, no Topaz): `outputs/tco-balloon-boy-acting-class.sample-yt.final.mp4`
  (= yt v4) and `.sample-ig.final.mp4` (= ig v3), copied to `X:\Claude Projects\Exports\tco-balloon-boy-acting-class.yt.final.mp4` / `.ig.final.mp4`
  with `.yt.proof-sheet.jpg` / `.ig.proof-sheet.jpg`; 1080x1920, 30 fps, 1120 frames, 37.33 s, −12.1 LUFS, −2.2 dBTP, AAC 256k.
  QA: ONE sonnet reviewer (r1, 8 findings), every confirmed defect fixed and re-verified on frames (`yt/work/verify_v4.jpg`,
  `ig/work/verify_v3.jpg`); cue checks PASS (YT swishes 19.0-22.6 dB under the voice, IG 18.6-22.0, subtle band); a faster-whisper read of
  the final button: "These two met in an acting class in 1997. That's all. Oh, really?" with no false start and nothing after.
  `workflows/graphics-qa.py` does not apply (no hf-graphics plan in this kit). To rebuild: `work/cut/make_edl.py` → splice.sh
  (AMPLIFY_DB −2) → `work/cut/patch_transcript.py` → `work/cut/cammap.py` + segstarts → `yt/build_spec.py` → yt_faces (yt + `--dir ig`,
  ig/spec.json from the YT shots) → `yt_build.py <job> vN` → `bash ig/run.sh build.py` → `bash ig/run.sh sound.py --mux --v N` → `work/finals.sh`.
- FLAGS for Affan / the main session: (1) the sides were INVERTED in SEQUENCING (★ below; the sent title "She swore Balloon Boy was
  real" is backwards: HE did); (2) "1997" is the year the Heenes MARRIED per Wikipedia (they met at an acting school in LA), spoken by
  Gillian, captioned as said, on no card; (3) the frame-0 news alert is a 2009 KMGH / Fox News broadcast frame (licensing flag);
  (4) beat 1 keeps Patrick's overlapping "Oh my God, really?" (it is under Gillian's "I've ever seen"); (5) NO beat before the button and NO
  hold after "Oh, really?" (the false start "They-" was cut; the source has no silent tail): the brief's timing ask is not met, a 0.4-0.5 s
  silent freeze on the last two-up frame is the only option (Affan's call); (6) no music bed (he scores the samples).
- **20:00 QA r1 (ONE sonnet reviewer, defects only, on YT v3 + IG v2; scratch in the session scratchpad review/tco/) → fixed:**
  (1) HIGH: Patrick's two "NO!" shots (s08, s12) put the seam caption on his open mouth (he leans in): z0 1.3 + fy_out 0.28 on those two;
  (2) the cut ended 14 ms into "really?" (out 62.40): out-point 62.4333 (her "That's" starts 62.434; fw at 62.42 / 62.47 hears none of it);
  (3) the YT marks panel showed headless figures: the mg-marks camera pulled back (the whole trio, X marks at panel y ~500);
  (4) the watermark sat on Patrick's hairline in the YT two-ups: bottom panel fy_out 0.40 → 0.44;
  (5) IG: 2 near-blank frames between the hook and the first stack: the hook leaves in 0.14 s and the stack's lead-in starts rising
      0.12 s early; (7) the IG tags' decode shortened 0.42 → 0.30 s;
  (8) a FALSE START "They- these two met" before the button (58.81-58.95, voiced; fw with the prompt reads "They -"): the button now
      starts after it (58.967), so the cut is 37.33 s / 1120 frames.
  Kept by design (reported, not defects): the IG leaves "This is" uncaptioned under the title (the standing no-captions-under-the-hook
  rule) and the 2009 lockup shows "2009" for "in 2009".
- **19:55 YT v3 built** (`outputs/…sample-yt.v3.mp4`, 1123 f, 37.43 s, 30 fps, −12.1 LUFS, −2.3 dBTP; proof `yt/work/proof_v3.jpg`): 20
  shots, 8 whips (only into / out of pictures; the cuts between the hosts and into their two-ups are the show's own hard cuts), 49
  caption chunks (Gillian magenta, Patrick the house white → red; 18 wiped, 37 %), 2 name tags, 7 swishes 19.0-22.6 dB under the voice
  (yt/cue_check.py; subtle band 19-23; its "WEAK on a phone" flags are the louder Pincus band). Lip sync on the cut (work/cut/avsync_cut.py,
  mouth box from the landmarks vs the voice): best lag 0 / 0 / +1 / +2 frames on Patrick's four clean spans. IG rendering
  (`ig/build.py`, 30 fps). Next: IG mux + cue check, ONE sonnet reviewer on both, fix, finals.
- **18:47 THE CUT IS DONE** (`outputs/tco-balloon-boy-acting-class.mp4`, 1125 f, 37.50 s, 30 fps; `work/cut/make_edl.py`, every
  edge pinned; AMPLIFY_DB −2; audio-qa: timeline exact, joints clean, limiter transparent; the two "ambience holes" (0.77 s, 5.03 s) are
  joints into the hosts' GATED digital silence (−70..−80 dBFS between words), not crossfade dips). Verbatim faster-whisper pass on the
  cut (`work/cut/fw_cut_v2.txt`) reads every beat; `work/cut/patch_transcript.py` (RUN AFTER EVERY SPLICE) drops two phantom edge words,
  re-times "in 1997" (WhisperX interpolated the digits +0.3 s) and tags every word with its speaker.
- **★ SPEAKER CORRECTION (report to the main session): SEQUENCING / the miner have the two sides INVERTED.** By voice (wespeaker
  clusters on 225 windows, cross-checked against the show's own camera: cluster G on Gillian's cam 76 / Patrick's 0, cluster P 0 / 41)
  AND by camera at every beat: **Gillian = HOAX (the skeptic): beats 1, 3's question, 4a, 5 and the BUTTON 7. Patrick = NOT A HOAX (the
  believer): beats 2, 3's "No.", 4b "All right, convince me", 6 "I want to pause the recording", and "Oh, really?".** The words and the
  order are untouched; only the labels flip, and the story is the same shape (the believer cracks, the skeptic drops the acting class).
  The approved TITLE "She swore Balloon Boy was real" is backwards (HE swore it was real): it is not on screen anywhere; the main
  session should fix it before it goes to Affan / Patrick.
- **Beat 1 overlap (kept, task brief "keep the overlap if it's clean"):** Gillian's "…thing I've ever seen" is spoken UNDER Patrick's
  "Oh my God, really?" (19.3-20.9 raw; ASR alternates between the two voices, "seen" is only heard past 20.31), so the beat's own words
  cannot end before his reaction: beat 1 runs to where both stop (21.03). His interjection is captioned in his colour after her line.
- Beat 6 starts on Patrick's slurred "I wanna" (43.97), right after "…this shit." (no trace of it in the cut; the phantom word dropped).
- Fact flag (GATE 5): en.wikipedia "Balloon boy hoax" (API 2026-10-31): "Richard Heene and Mayumi Iizuka met at an acting school in Los
  Angeles, and married in 1997." The acting class is right; **1997 is the year they MARRIED**. The button is Gillian's spoken line
  (approved, main session: "the year is the host's"), so the caption carries her words; no card shows 1997. Flag for Affan.
- **2026-10-31 18:30 AFFAN (via the coordinator), overriding BUILDER-BRIEF steps 3 + 6: NO Topaz (no Iris, no Chronos), NO 60 fps**
  ("30 fps is good enough for prospecting"). Both looks render at the source's native 30 fps from the 1080p cut; the QA'd render IS
  the final. WhisperX stays on CPU; no GPU needed.
- 18:25: BRIEF written; raw sections cut (`raw/tco_section_A.mkv` = src 210-312, `_B.mkv` = src 520-600; frame-exact: section A
  frame 0 = source frame 6300, both streams start 0); WhisperX large-v3 on CPU running. The source repeats ~21 % of its frames (a
  webcam under a 30p label): accepted (no Chronos per Affan's 18:30 call).
- Doc INSERT in the source (never used): src ≈ 541.4-544.8 (dissolves in/out; `work/cut/layout.json`).
- SFX fresh set (x1-x8 downloaded, measured with sfx3_measure.py): KEEP tco-cloth-var (tonal 11.3), tco-deep-rustle (11.8),
  tco-soft-airy (11.9), tco-swoosh-light (11.2, 4.7 % > 6 kHz), tco-arm-clean (12.5, a very short flick); OUT tco-cloth-flap (13.5),
  tco-softs (18.3 tonal), tco-rustle-by (18.6 % above 6 kHz = hiss on a phone).
- Source clock (measured, FFT xcorr of the feed MP3 vs the source window, 10 s chunks, `work/cut/`): **src t ≈ feed t − 516.6 s at
  feed 12:00-14:40, drifting to − 523.5 at 17:20 and − 530 at 19:40** (the YouTube upload is edited differently: inserts / trims).
  src = YouTube t − 600 (window 0:10:00-0:28:00). The upload carries the Netflix doc's clips (one seen at src ≈ 544): never used.

## The job
- Show: **True Crime Obsessed** (Patrick Hinds & Gillian Pensavalle), 960K subs. Two hosts recap true-crime docs WITH COMEDY: the
  banter is the show. Patrick must approve anything that goes live. Richest prospect of the batch (handoff money check: Patreon est.
  $120-300K/month): this must be the best sample of the batch.
- Approved pick (`projects/_onyx-batch6-2026-10/SEQUENCING.md` § "TCO v4"; miner `tco/PICKS-v3-E1.md` pick 1): **"She swore Balloon
  Boy was real. Then the acting class came up."** Episode 461 "Trainwreck: Balloon Boy", YouTube gC3qX8-Q_TQ, a SCENE in the room
  (ENTERTAINMENT track), ≈ 44 s. The viewer gets: the hosts fight over a hoax everyone remembers, and the last line flips it.
- Source: `source/gC3qX8-Q_TQ_0.10.00-0.28.00.mp4` (1920x1080, 30/1 fps, AAC 44.1k; pulled by the main session). The show's edit:
  each host's own webcam full-frame, a side-by-side TWO-UP (Gillian left, Patrick right) on overlaps, and Netflix doc inserts.
- Both looks from ONE cut: YouTube (Sean Ryan look, `presets/youtube-shorts/onyx-samples-youtube/`) + Instagram (neon window,
  `presets/instagram/neon-window/`, kit = the Pincus `ig/` via the Still Here job's adaptation, same batch).
- Deliver: `outputs/tco-balloon-boy-acting-class.sample-yt.final.mp4` / `.sample-ig.final.mp4`, copies
  `X:\Claude Projects\Exports\tco-balloon-boy-acting-class.yt.final.mp4` / `.ig.final.mp4`, a proof sheet each.

## The beats (followed EXACTLY; found by their WORDS; nothing added, nothing re-ordered)
Hook card 0-3 s: "BALLOON BOY, 2009 · 'OUR SON FLOATED AWAY.' HE WAS IN THE ATTIC." (the hook font has no "·": set as "/")
1. HOOK (VOICE: Gillian; SEQUENCING said Patrick, see ★ above; feed 0:12:22): "this is the most poorly written, poorly acted thing I've ever seen."
2. (VOICE: Patrick): "we all thought this was a hoax in 2009. And I thought this was like the unraveling of how it wasn't a hoax."
3. (VOICE: Gillian asks, Patrick "No.", Gillian "What?", Patrick "No. Wait.", Gillian "Come on.", Patrick "No."; feed 0:12:47): "do you think this was a hoax? No. What? No. Wait. Come on. No."
4. (VOICE: Gillian … Patrick; feed 0:13:16): "This is all completely manufactured, I believe" … "All right, convince me."
5. (VOICE: Gillian; SEQUENCING said Patrick; feed 0:17:35): "everyone just happens to stop right in the middle, right in the perfect
   spot of the camera … It's almost like they have marks on their lawn."
6. (VOICE: Patrick; kept, the cut is 37.3 s; feed 0:18:04): "I want to pause the recording and watch the documentary again, looking at it from this perspective."
7. BUTTON (VOICE: Gillian; "Oh, really?" = Patrick, kept; feed 0:18:19): "These two met in an acting class in 1997. That's all." (+ "Oh really?" if clean)
- Speakers as SENT: Patrick = hoax, Gillian = not a hoax. **By voice AND face they are the other way round** (★ in ▶ STATUS): Gillian =
  HOAX, Patrick = NOT A HOAX. The words and order are untouched; the labels on screen follow the voices; reported to the main session.

## Decisions (with reasons)
- **Comedy timing is the product** (task brief): beat 3's exchange keeps its rhythm (its silences shortened by hand, out of the tight pass),
  beat 1 keeps the overlap. **What shipped vs the brief's "a beat before the button" and "hold the reaction, then cut": NOT MET, reported.**
  The pre-button pause was her own 0.3 s, but QA r1 found a false start "They-" in it, so the button now starts ~5 frames after
  "perspective."; and the source has NO silent hold after "Oh, really?" (her "That's all they just met" starts ~20 ms after his "really?"),
  so the cut ends on "really?" (the clean loop into her first line). The only way to a hold is a silent 0.4-0.5 s FREEZE on the last two-up
  frame: offered as an option for Affan (a taste call; it costs the loop), not built.
  In the stumble pass an interjection in crosstalk is the other host, never a stumble.
- **No card steps on the punchline.** The button plays on the faces; the only sound there is at most one soft swish.
- **No "1997" on any card**: the year is the host's claim (main session's GATE 5); the caption carries his/her words, a card says
  ACTING CLASS only.
- **No music bed; SFX = soft Patrón-style swishes only**, one per graphic entrance, sized to the move; cuts back to a face silent
  (memory feedback-premium-sfx SUPERHERO + UNDER HIS MUSIC). A bed is a mix-only rebuild if Affan wants one.
- **No Netflix/doc footage or audio, no frame of the family's own video** (it is the family's / the news's). Real 2009 news photos
  only if HQ and checked; an illustration where the thing was only ever on the family's tape.

## Catalog pass (2026-10-31; CATALOG.md FX-01..81 read in full; all 137 reference stills in `research/effects-catalog/shots/` LOOKED AT
## on labelled tiled sheets: 79 singles at 480x270, 58 four-frame strips at 1600 px wide)
- **Fits this video** (a live two-person argument about a 2009 news event + an illustrated "home video" + a fact that flips it):
  - **FX-11 Rival Colour Split** (as a FACE SPLIT): both hosts at once on the overlap ("Do you think this was a hoax? / No. / What?")
    with their sides labelled, HOAX vs REAL: the argument itself becomes the picture.
  - **FX-42 Kin Tag**: each host's name + their side the first time they are on screen alone, so a stranger knows who argues what.
  - **FX-58 Speaker-Coded Subs**: caption colour = voice (Patrick the house red wipe, Gillian magenta: her hair is the show's colour).
  - **FX-41 Year Ghost**: a giant wide "2009" over the shot on "a hoax in 2009".
  - **FX-21 Red Silhouette Set + FX-23 Pointer Tag**: the family's backyard REBUILT as a thin-line drawing seen through a camcorder
    viewfinder (REC, static camera), silhouettes run and stop dead on red tape X marks: "marks on their lawn" made literal and clearly an
    illustration (never their footage).
  - **FX-29 Float Frame / FX-33 Dust Void Drop**: one real 2009 photo of the balloon in the sky as a floating card over its own blur.
  - **FX-40 Slow-Burn Portrait**: the reaction after the button held on the listener's face with a slow creep, then cut.
- **Not used before on an Onyx sample:** FX-11 as a two-host face split with sides, FX-41 Year Ghost, FX-21 line-drawing reconstruction.
- **Leaned on last time, avoided here:** FX-27 quote card + FX-28 dossier + FX-79 echo (Pollak, today), FX-34 highlighters (Pincus x5),
  stat charts (Patrón, MATG). No document receipts: the story has no document to show.

## What this one does better than the last ones (rule 5; Pollak YT/IG 2026-10-31, Pincus 2026-10-31, MATG 2026-10-23)
1. **The argument IS the picture**: the first Onyx sample built on two people disagreeing live; a face split with their sides on the
   overlap and on the button's reaction, each voice its own caption colour, so a stranger follows a two-person scene at a glance.
2. **An illustrated reconstruction instead of stock or borrowed footage**: the "marks on the lawn" joke drawn as a line set through a
   camcorder viewfinder, the first sample to rebuild an event nobody may show.
3. **Comedy timing as a measured rule**: the punchline lands on faces with a held reaction (no card, no hit), the overlap kept intact;
   the first sample where the cut is tuned for a laugh rather than tightness.

## IG variant (neon window; `ig/build.py`, kit = the Pincus IG via the Still Here job)
- Same cut, beats and pictures as the YT. Hook on frame 0: Mark Brazil's 10-31 title ("Balloon Boy, 2009" / "Our son floated away" /
  He was [in the attic] on a red box) over the 2009 news alert as a float card; no captions under it (0-2.1 s).
- Stage stacks (the stack IS the caption) for three moments: "the most poorly written / *poorly acted* / thing", "Do you think this was
  a / *hoax?*" (GILLIAN, TO PATRICK), "It's almost like they have / *marks on / their lawn*" over the drawn legs on their red X marks.
- The 2009 search photo as a float card under a stat lockup (OCTOBER 15 / *2009* / FORT COLLINS, COLORADO).
- Each host on her / his own camera (tracked on the face box, pinned at every take's edge, mouth at window y 536); the show's TWO-UP kept
  side by side as two portrait panels with a white line; the rewind as a horizontal split under Patrick (white line, captions on it).
- Mono name tags (red bar flickers on, the name and the side decode in): PATRICK HINDS / SAYS: NOT A HOAX, GILLIAN PENSAVALLE / SAYS: HOAX.
- Captions: one whole line ≤ 4 words, 14 px eased rise, white Inter + one red Playfair hero ("acting class" closes the loop on "poorly acted").
- **Better than the Pollak IG (the 1 %):** (1) two people in one window: the show's own two-up becomes a designed side-by-side with the
  white line, the argument visible at once; (2) a drawn reconstruction (the viewfinder backyard, the marks, the rewind) instead of photos
  of places; (3) each host's side named on screen as a decoding tag, so a stranger follows the fight from the first line.

## GATE 5 (facts on screen) — to verify before any card renders
- Balloon Boy: 15 Oct 2009, Fort Collins, Colorado; the parents (Richard and Mayumi Heene) said their 6-year-old son Falcon was in the
  balloon; he was found hiding in the attic (of the garage). The hook's 'OUR SON FLOATED AWAY.' is a PARAPHRASE in quote marks
  (approved wording): flagged.
- "These two met in an acting class": the Heenes met at a Hollywood acting school (2009 reporting). The year 1997 is the host's.

## Sources
| Use | File | From |
|---|---|---|
| Frame 0 (YT DOC on a screen card; IG hook float card): the 2009 live news alert "ALERT / 6-YEAR-OLD BOY TRAPPED ALONE INSIDE BALLOON", Ft. Collins, CO, 12:49 PM, KMGH | `yt/assets/broll/b-news-alert.jpg` (1920x1080) | foxnews.com/us/balloon-boy-hoax gallery (a57.foxnews.com …/1920/1080/Child-Trapped-in-Flying-Balloon10.jpg), the 15 Oct 2009 broadcast frame (KMGH / Fox News). LICENSING flag: a TV news frame, as the Pollak TV frame / the Daymond press stills |
| "in 2009" (YT FX-41 year ghost card; IG float card under the stat lockup): Colorado Army National Guard aviators searching for Falcon from a UH-60 Black Hawk, 15 Oct 2009 | `yt/assets/broll/b-search-2009.jpg` = `work/img/cand/dvids213676.jpg` (3872x2592) | Wikimedia Commons via the en.wikipedia API, DVIDS 213676, Sgt. Benjamin Crane, PUBLIC DOMAIN (credit printed small on the YT card) |
| The backyard in a camcorder viewfinder, its tape X marks, its rewind (FX-21 / FX-55; both looks) | `yt/assets/broll/mg-backyard.mp4`, `mg-marks.mp4`, `mg-rewind.mp4`, `mg-2009.mp4` | built: `yt/cards.py` (PIL line drawing; the IG draws the same set square via the same functions). An illustration, never the family's video |
| Their own two-up (both hosts live) | the cut itself (frames 99-151, 417-449, 857-892, 1090-1123) | their episode |
| Swishes | `assets/sfx/epidemic/tco-cloth-var / tco-soft-airy / tco-swoosh-light / tco-deep-rustle` (sliced by `yt/sound.py`) | Epidemic (Download log x1-x8) |
Not used: no YouTube B-roll (no NEEDS-YOUTUBE.md), no Netflix footage or audio (the doc insert under frames 708-793 is covered by the drawing), no stock person, no Higgsfield.

## Download log (logged BEFORE each pull)
| # | File | Source | Size | Why |
|---|---|---|---|---|
| v1 | `source/gC3qX8-Q_TQ_0.10.00-0.28.00.mp4` | main session (YouTube gC3qX8-Q_TQ, window 0:10:00-0:28:00, 1080p30 H.264) | 174 MB | the source (not pulled by me) |
| d1 | `work/img/cand/dvids213676.jpg` | https://upload.wikimedia.org/wikipedia/commons/e/eb/In_Search_of_a_Flightless_Falcon%2C_Colorado_Aviators_Help_in_Search_for_Lost_Boy_DVIDS213676.jpg (en.wikipedia API imageinfo: 3872x2592, public domain, Sgt. Benjamin Crane, Colorado National Guard, 2009-10-15) | 2.7 MB | a real 2009 photo of the search (Black Hawk over Colorado) |
| x1-x8 | `assets/sfx/epidemic/tco-*.wav` (repo library) | Epidemic Sound SFX, `DownloadSoundEffect` WAV, none in MANIFEST before (Pollak took ph-*, TFTS e435dfaf / e62847da): 79611651 "Cloth, Flap, Whoosh, Soft, Short, Multiple" · 8f1a6bfe "Swooshes, Swish, Low, Cloth Movement, Variations" · f040a2a4 "Swooshes, Whoosh, Softs" · 279037ea "Swooshes, Whoosh, Deep, Rustling Nice" · a22e3c51 "Swooshes, Whoosh, Medium, Rustle By" · f7461a2e "Fight, Cloth, Arm Whoosh, Clean" · 073cf199 "Designed, Whoosh, Soft Airy" · c52cf22f "Swooshes, Whoosh, Designed, Swoosh, Light" | ≈ 0.1-0.6 MB each | candidates for the Patrón-family soft swishes (each measured: tonal p90 ≤ ~13, phone band, > 6 kHz share) |
| c01-c10 | `work/img/cand/c01..c10.*` (candidates) | Bing Images in the built-in browser (query "balloon boy 2009 balloon flying saucer sky Fort Collins", large), `a.iusc` m JSON: foxnews.com/us/balloon-boy-hoax gallery (a57.foxnews.com …/2018/09/1920/1080/12.jpg, Child-Trapped-in-Flying-Balloon10/25/24/15/6.jpg, 808f1d4e-…25.jpg, Balloon-Lands5/8.jpg), denverpost.com 2009 "20091015__20091016_A01_CD16BALLOONMAINp3.jpg", dailycamera.com 2009 "20091015_125222_balloon.jpg" | ≈ 0.1-0.6 MB each | the hook's real 2009 picture: the silver saucer balloon in the sky (a news photo; never a Netflix still or the family's video) |
| d2 | `work/img/cand/dvids213675.jpg` | https://d1ldvf68ux039x.cloudfront.net/thumbs/photos/0910/213675/2000w_q95.jpg (DVIDS 213675, same set, public domain) | ≈ 0.5-1.5 MB | second frame of the same search |
