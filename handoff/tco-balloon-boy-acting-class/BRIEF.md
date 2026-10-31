# tco-balloon-boy-acting-class: Onyx sample Short for True Crime Obsessed (Patrick Hinds & Gillian Pensavalle) (batch 6, TOP priority)

## ▶ STATUS: resume here
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
1. HOOK (Patrick, feed 0:12:22): "this is the most poorly written, poorly acted thing I've ever seen."
2. (Gillian): "we all thought this was a hoax in 2009. And I thought this was like the unraveling of how it wasn't a hoax."
3. (feed 0:12:47): "do you think this was a hoax? No. What? No. Wait. Come on. No."
4. (feed 0:13:16, Patrick … Gillian): "This is all completely manufactured, I believe" … "All right, convince me."
5. (feed 0:17:35, Patrick per SEQUENCING; VERIFY BY VOICE): "everyone just happens to stop right in the middle, right in the perfect
   spot of the camera … It's almost like they have marks on their lawn."
6. (feed 0:18:04, Gillian; drop if long): "I want to pause the recording and watch the documentary again, looking at it from this perspective."
7. BUTTON (feed 0:18:19, speaker by ear): "These two met in an acting class in 1997. That's all." (+ "Oh really?" if clean)
- Speakers: Patrick = hoax, Gillian = not a hoax (confirm by voice AND face; speaker embedding per chunk against clean solo spans).
  If beat 5 is Gillian's, it is reported, never re-framed silently.

## Decisions (with reasons)
- **Comedy timing is the product** (task brief): the overlap in beat 3 stays if it is clean; a beat of reaction before the button;
  after the button, "Oh really?" if clean, then ~0.6-1.0 s of the listener's face, then the cut. This OVERRIDES the YT README § 9
  "end ≤ 0.1 s after the last word" and the tight-pause pass in those three places (pinned, `no_refine`, out of the tight pass).
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

## GATE 5 (facts on screen) — to verify before any card renders
- Balloon Boy: 15 Oct 2009, Fort Collins, Colorado; the parents (Richard and Mayumi Heene) said their 6-year-old son Falcon was in the
  balloon; he was found hiding in the attic (of the garage). The hook's 'OUR SON FLOATED AWAY.' is a PARAPHRASE in quote marks
  (approved wording): flagged.
- "These two met in an acting class": the Heenes met at a Hollywood acting school (2009 reporting). The year 1997 is the host's.

## Sources
| Use | File | From |
|---|---|---|

## Download log (logged BEFORE each pull)
| # | File | Source | Size | Why |
|---|---|---|---|---|
| v1 | `source/gC3qX8-Q_TQ_0.10.00-0.28.00.mp4` | main session (YouTube gC3qX8-Q_TQ, window 0:10:00-0:28:00, 1080p30 H.264) | 174 MB | the source (not pulled by me) |
| d1 | `work/img/cand/dvids213676.jpg` | https://upload.wikimedia.org/wikipedia/commons/e/eb/In_Search_of_a_Flightless_Falcon%2C_Colorado_Aviators_Help_in_Search_for_Lost_Boy_DVIDS213676.jpg (en.wikipedia API imageinfo: 3872x2592, public domain, Sgt. Benjamin Crane, Colorado National Guard, 2009-10-15) | 2.7 MB | a real 2009 photo of the search (Black Hawk over Colorado) |
| x1-x8 | `assets/sfx/epidemic/tco-*.wav` (repo library) | Epidemic Sound SFX, `DownloadSoundEffect` WAV, none in MANIFEST before (Pollak took ph-*, TFTS e435dfaf / e62847da): 79611651 "Cloth, Flap, Whoosh, Soft, Short, Multiple" · 8f1a6bfe "Swooshes, Swish, Low, Cloth Movement, Variations" · f040a2a4 "Swooshes, Whoosh, Softs" · 279037ea "Swooshes, Whoosh, Deep, Rustling Nice" · a22e3c51 "Swooshes, Whoosh, Medium, Rustle By" · f7461a2e "Fight, Cloth, Arm Whoosh, Clean" · 073cf199 "Designed, Whoosh, Soft Airy" · c52cf22f "Swooshes, Whoosh, Designed, Swoosh, Light" | ≈ 0.1-0.6 MB each | candidates for the Patrón-family soft swishes (each measured: tonal p90 ≤ ~13, phone band, > 6 kHz share) |
| c01-c10 | `work/img/cand/c01..c10.*` (candidates) | Bing Images in the built-in browser (query "balloon boy 2009 balloon flying saucer sky Fort Collins", large), `a.iusc` m JSON: foxnews.com/us/balloon-boy-hoax gallery (a57.foxnews.com …/2018/09/1920/1080/12.jpg, Child-Trapped-in-Flying-Balloon10/25/24/15/6.jpg, 808f1d4e-…25.jpg, Balloon-Lands5/8.jpg), denverpost.com 2009 "20091015__20091016_A01_CD16BALLOONMAINp3.jpg", dailycamera.com 2009 "20091015_125222_balloon.jpg" | ≈ 0.1-0.6 MB each | the hook's real 2009 picture: the silver saucer balloon in the sky (a news photo; never a Netflix still or the family's video) |
| d2 | `work/img/cand/dvids213675.jpg` | https://d1ldvf68ux039x.cloudfront.net/thumbs/photos/0910/213675/2000w_q95.jpg (DVIDS 213675, same set, public domain) | ≈ 0.5-1.5 MB | second frame of the same search |
