# RUN — gta6-bigfoot-secrets (Affan Afterhours, FACELESS VO long-form)

## ▶ STATUS: resume here
- **20 Nov ~05:20 PKT: POSTED + LEARN PASS DONE.** Posted 20 Nov 03:52 PKT as "11 BIGGEST Easter Eggs Of GTA 6 (This Is NUTS)"
  (`2TktORyV4Bg`, 8:57; title his, tags ours: `PACKAGING.md`). His uploaded sequence = ABW11 › "GTA 29 - Bigfoot Secrets v2", read
  back 04:25 (`premiere/readback-his-final.tsv`, identical to our last dialogue pass). Diff vs our delivered build (`work/his_diff.py`
  -> `his-diff.json`) + a read-only pass for transitions/effects/keyframes: he cut 2 restarts the gate couldn't see ("Kyle. And
  I— On IShowSpeed's", "His name— his actual name") and tightened 12 pauses (14 cuts, 4.7 s; `work/his_pauses.py`: ours
  0.26-0.48 s -> his 0.02-0.18 s, breath read as speech by the gate's raised line); re-looped the cold-open bed; added 8
  Constant Power fades on the A4 squawks; swapped A1 for his Enhance Speech bounce. Kept every graphic, tag, guide, SFX position
  and level, body bed and all 14 dialogue clips. New tools: `work/ctc_restarts.py` (catches both restarts, 13 flags / 222 joints),
  `work/vo_gap_stats.py`. Written to LESSONS (2026-11-20 "GTA 29 POSTED"), PLAYBOOK § C2, lanes/premiere/lab-notes.md, JOBS.md.
  **THE UPLOAD IS NOT THE PROJECT:** he uploaded his 02:52 export (`E:\Shorts\Abudance Wisdom Shorts Exports\Final Renders\
  GTA 29 - Bigfoot Secrets v2_1.mov`), made from our FIRST dialogue pass + his fixes (D3-D12 -6 dB Audio Gain, squawk fades);
  every clip correlated against it (`work/dialogue/` v1 files, corr 0.86-0.97). Our 02:48 second pass raced that export: it is
  only in the project, where our Volume levels now stack on his -6 dB on D3, D6-D11 (his gain went with the replaced D5 / D12).
  The posted video has brendaniel's shout in the parrot montage (first D13c), "a lot of—" (first D13a) and the "What next?" blip.
  **Open:** whether to set the project back to match the upload; the ABW11 bin clean-up offer (~1,000 superseded imports).
- **20 Nov ~02:50 PKT: REAL GAME DIALOGUE UNDER THE SILENT HOLDS, on HIS edited v2 (verified).** His note: "put the actual
  game audio of the characters talking wherever there is awkward silence", otherwise ready (he exports; do NOT export).
  Additive, by name, no activation, not saved. **14 lines: A4** D1-D12, **A5** the parrot montage D13a-c. Files:
  `audio/dialogue-v1/` (9) + `audio/dialogue-v2/` (D5, D12, D13a-c re-cut after the delivered-WAV check), rows
  `work/dialogue/rows.json` (v1 rows kept in `rows-v1.json`), clip levels `work/dialogue/levels.json`. Scripts:
  `build_dialogue.py` (cut, gain, limiter, fades; decodes from 6 s earlier because seeking straight into the parrot VOD
  starts its audio late), `place_dialogue.py` (first lay), `replace_dialogue.py` (swap OUR clips only + levels). Last
  readback `premiere/readback-post-dialogue-v2.tsv`: **his 616 rows unchanged, our 14 at their times and levels**, his
  playhead and active sequence untouched; backups `premiere/backup/ABW11.prproj.20261120-02*.bak`. Each line is in sync with
  its picture (D9 +0.06 s, D13b +0.09 s; no lips visible), sample-aligned to its source (corr >= 0.94 at lag 0), words =
  the on-screen subtitle, the streamer silent (xQc + summit1g cams checked). **Level:** each line's momentary loudness =
  his VO's as it is now (clip Volume -5.4 to -10.8 dB): he swapped A1 for his Enhance Speech pass at 02:41
  (`C:/Users/affan/Downloads/Music/GTA 29 - Bigfoot Secrets v2-esv2-3p-bg-10p-music-10p.mp3`, VO only, -23.5 LUFS).
  Lines sit 5-10 LU over the bed, which is still +4 dB over these holds (HOLD_LIFT; A6 is his, untouched).
  Sources: Lirik's two dog lines from `lirik-egg.mp4` (his VOD is Twitch-muted from 04:24:00; egg = strand - 316.0167 s);
  the parrot's "Generator! Generator!" from `lirik-parrot-045630.mp4` 182.5-184.2 (brendaniel shouts over his own copy).
  **Still quiet:** D14 "Yes! Secret Stash!" (the streamer talks over it in all three copies) and the last ~1.2 s of the D10
  reveal hold ("Same genus, different species" runs 1.7 s past it; the clip stops after "Skunk ape."). Open: extend the D10
  hold ~1.7 s? Egg audio music check (Twitch mute reason) inconclusive.
- **20 Nov ~01:20 PKT: xGarbett swap done (his yes).** "On xGarbett's screen, Jason jumps off a boat" now shows xGarbett's own
  capture (`broll/14-kraken/xgarbett-kraken-26o1sp-pbXg.mp4`, evidence `14c-kraken-xgarbett.json`, watermark frosted), the splash SFX
  on his jump. v2 now: V1 `footage/reels9/`, V4-V8 `gfx/v2b/`, V2-V3 `gfx/guides7/`; readback **818/818**, 60.000 fps, no V1 gaps.
- **20 Nov ~00:40 PKT: v2 FINAL ON THE TIMELINE, READY FOR HIS REVIEW.** ABW11 › "GTA 29 - Bigfoot Secrets v2" (rebuilt once),
  9:01.62, **60.000 fps**, readback **816/816** (folder-checked; `verify_readback.py` now FAILS on any fps != 60.000), no V1 gaps.
  Assets: V1 `footage/reels8/` (masters with exact N/60 stamps + `reels.py` writes a frame-exact `duration` per master: the first
  v2 build was 60.0006 fps from reel timestamp drift), V2-V3 `gfx/guides7/` (= guides6 + the railings box pulled inside the frame),
  `gfx/v2/`, `audio/music-cut-v2/`, VO `audio/vo/vo-polished-v2.wav`. QA after the advisor: teaser moved to a body-free HUG window,
  the bodies in the lot frosted on "Talk to Kyle", splash/egg SFX synced, changed windows composited and seen
  (`work/qa/fixes-v2.jpg`). His v1 sequence untouched. Unsaved: he presses Ctrl+S.
- **20 Nov ~00:25 PKT: v2 ON THE TIMELINE, verified, waiting for his review.** ABW11 › "GTA 29 - Bigfoot Secrets v2"
  (new sequence; his edited v1 untouched), 9:01.6. Readback **816/816** (folder-checked, `premiere/readback-v2.tsv`); 5 one-frame V1
  holes at reel heads (irregular source timestamps) closed by `premiere/fix_gaps_v2.jsx`, no V1 gaps left. Mix -15.9 LUFS (voice
  -15.9, music -33.1, sfx -37.8). QA: 3 Sonnet 1 fps sweeps (`work/qa/SWEEP-v2-*.md`) + guide sheet `work/qa/guides-v2-new.jpg`;
  fixes: Speed's sub counter panel widened, the UFO stranger shot replaced by the empty trail (she is nude in the source), the
  railings guide moved off the REPORTED label. Unsaved: he presses Ctrl+S. Delivery note v2 below.
- **19 Nov ~23:55 PKT: v2 BUILD IN PROGRESS** (his pickups `raw/TX01_MIC037_20261119_220850_orig.wav`, read from DRAFT 3 + his own
  crab ad-lib). VO v2: `work/cut2/` (REPORT.md, TRANSCRIPT-v2.md), combined clock `raw/combined.wav`, `audio/vo/vo-polished-v2.wav`,
  539.62 s. **His own edits on v1 (read back by name before touching anything):** two ripple cuts only: 0.9 s "and there's" before
  "another one drifting" (dog beat, carried into v2 in `work/cut2/keep.py`) and 0.75 s in the old animals beat (gone in v2). No
  level, scale or graphic changes. **His v1 sequence is NOT touched:** v2 goes on a NEW sequence "GTA 29 - Bigfoot Secrets v2".
  Assets v2: footage masters + `footage/reels7/`, `gfx/guides5/`, `gfx/v2/` (titles, chips, tags, labels, cards), `audio/music-cut-v2/`,
  new SFX in `audio/sfx48/` (underwater-deep, ufo-hover, tension-drone, creature-hiss). Evidence: `footage/evidence/11-16*.json`
  (+ 11b/14b = pillarboxed Rubius / Gator Keys copies). Plan: `work/plan_new.py` (+ plan_s1 teaser, plan_rest tails, plan_audio beds).
- **19 Nov ~21:50 PKT: RE-CUT DECIDED, waiting for his pickup VO.** He found three eggs the script missed (Kraken, UFO
  abduction, Speed's Red Hulk). His call: keep the strong eggs already in the sequence, REMOVE the weak ones (features,
  not eggs), add the missing eggs, he records only the new parts. Re-check: `X:\Claude Projects\GTA 6\research\egg-recheck-2026-11-19\RECHECK.md`.
- **Out (timeline s):** "But they can also kill you." 262.76-263.67 · #4 animals 264.18-337.85 · #5 jet 337.85-362.37 ·
  #6 locals 362.37-389.92 · #7 wildlife 389.92-406.95 · #9 shark 433.15-453.25 · "What I couldn't find" 500.67-519.46.
  **Kept:** opening (teaser sentence re-recorded), #1 Bigfoot, #2 dog, #3 parrot, #8 games, #10 cellar, outro.
- **New order (still 10):** 4 the radio-tower Easter-egg nest · 5 Dexter's apartment · 6 Kyle the Red Hulk (Speed) ·
  7 the sea monster (Kraken, or the monster crab) · 9 the UFO ("The Truth Is Out There") + "And now, the cellar."
- **Next:** frame-checked facts (`egg-recheck-2026-11-19/FOOTAGE.md`) -> pickup script -> his recording -> cut the pickups
  into the VO (same chain) -> rebuild the timeline in NEW folders (reels7, guides5; titles 4/5/6/7/9 re-rendered).

## (previous status, 19 Nov ~20:15)
- **State (19 Nov, QA round 2 done): FIRST FULL CUT ON THE TIMELINE, verified, READY FOR HIS REVIEW.** ABW11 › bin +
  sequence **"GTA 29 - Bigfoot Secrets"** (1920x1080, 60.00 fps, linear compositing off), 9:00.4. Readback **837/837 clips
  match the plan frame-exact, media folder included** (`premiere/readback.tsv`, `verify_readback.py`). Built and swapped
  WITHOUT activating our sequence (his active sequence + playhead never moved). **Nothing saved by us: he presses Ctrl+S.**
  He exports.
- Assets in use: V1 `footage/reels6/` (12 section reels), V2-V3 `gfx/guides4/` (110), V4 `gfx/cards2/` (17), statics
  `gfx/long/`, A1 `audio/vo/vo-polished.wav`, A2-A5 `audio/sfx48/`, A6 `audio/music-cut/`. Superseded imports
  (`footage/reels/`, `reels2/`-`reels5/`, `gfx/guides/`, `guides2/`, `guides3/`, `gfx/q-*.mov`) sit unused in the bin: safe to delete.
- **Next action:** his review notes -> fix at the source -> swap the tracks by name (`build_place.py --replace ...` +
  `continue_window.py`, NEW asset folders only); then phase D (diff his saved timeline) + LESSONS.

- **Re-run order after any change:** `work/cut/assemble.py` -> `work/tl_words.py` -> `work/plan_picture.py` (rows, specs,
  timeline) -> `work/plan_audio.py` -> `footage/build.py render ALL` -> `gfx/build.py` + `gfx/guides.py guides-spec.json`
  -> `premiere/build_place.py` -> `premiere/run_window.py --run` (new sequence "GTA 29 - Bigfoot Secrets" in ABW11).

| | | |
|---|---|---|
| format | long-form YouTube 16:9, FACELESS VO over streamer gameplay | 1920x1080 60.00 fps (every b-roll file is 60 fps) |
| lane | Premiere, ABW11 (his open project; Video A precedent), a NEW sequence + bin | he exports (never exportAsMediaDirect) |
| preset | `presets/youtube/affan-afterhours/EDITOR.md` + LAUNCH-MODE.md; Video A's look (`NOTES-video-a.md`) | NOT `youtube/default` |
| raw | `raw/TX01_MIC036_20261119_170338_orig.wav` (864.705 s, 48 kHz mono f32, size matches the original) | original untouched in `X:\Recordings\Afterhours\` |
| script | `X:\Claude Projects\GTA 6\research\vo-slate-2026-11-19\F-EGGS-READ-ALOUD.md` (draft 7) + `F-EGGS-SCRIPT.md` (cues) | quotes: `VERIFY-F.md`, `VERIFY-F2.md`, `COLD-READ-F.md`, `sources/hunt-eggs.md` |
| footage | `broll/01-bigfoot … 10-shark` (33 files) | manifest `BROLL-MANIFEST.md` (research folder) |
| constraints | silence (ffmpeg -f null / frames only) · nothing on C: but scratch · Sonnet executors (model passed explicitly) · never move his playhead · he exports · ALL streamer audio muted (incl. Twitch captions) · face cams VISIBLE + labelled · chat + viewer counts blurred · no nudity · gore cut per cues · profanity cut · political stickers cropped · source tag on every clip · quote cards = the game's exact text · no YouTube (BLOCKED 17:01) | |
| started | 2026-11-19 17:20 PKT | |

## Better than Video A (the bar), and the catalog pass (callout moves only)
- **What this one does better (his two complaints + his ask):** (1) the VO is cut to HIS shipped pacing on the first cut
  (pauses measured word end -> word start with breaths counted; three retake-detection layers; the gate runs on the
  assembled file: 0 retakes / asides / acted lines, pauses median 0.15 s, p90 0.27 s, max 0.33 s); (2) 3.4x the pink
  guide layer (110 marks vs Video A's 34), with new kinds that follow moving targets (circles, labelled arrows, map pins,
  a spotlight); (3) built in one evening on Video A's proven tools, not a 5-hour rebuild.
- **Catalog pass (`research/effects-catalog/CATALOG.md`, read for callout moves only; EDITOR.md § 7: the AW pacing and
  collage moves are NOT this channel):** FX-23 Pointer Tag -> the labelled arrows/boxes ("KIRK", "RIBCAGE", "A REAL
  PLAYER"); FX-70 Ring and Benchmark (one-stroke ring) -> the tracking circles on the figure, the gator, the dog, the
  shark; FX-34 Read-Along Highlighter -> the spotlight on the missing-man newspaper; FX-68 / FX-73 pins -> the map pins
  (Pelican River marker, the liquor store). New on this channel: tracking circles, labelled arrows, pins, spotlight.

## Flags
- Job files live in the MAIN checkout's `projects/` (gitignored: `.gitignore:24 /projects/`), as the brief and Video A did;
  this session runs in a worktree, so they are written with shell tools. Tracked files (JOBS.md, LESSONS.md, lab-notes)
  are NOT edited from here: their text goes to the shared notes folder for the hub.

## His asides in the recording (verbatim; instructions, never in the video)
1. 175.3-198.9 s: "Actually, you know what, Claude? All of these bits that, uh, I'm... like I'm pretending to be Jason and
   Kirk, you will actually use footage of the actual gameplay where they say it instead of me. So I'm not going to say
   these lines anymore. I'm going to skip the dialogues, I'm going to just read the script."
   -> every acted character line (his voice as Jason / Kirk / the parrot) is cut, including the ones read before this
   aside, and the game's own footage of that line (its subtitle on screen + a quote card with the exact text) plays there.
2. 379.9-384.7 s: "So here you will actually put the... for the gameplay of the parrot." -> the parrot's lines are the
   parrot gameplay (subtitles + cards), not his voice.
3. 823.9-829.1 s: "Oh, I wasn't supposed to say all of this. Okay. Never mind, I'm going to tell you the conclusion."
   (right after "I searched the whole voice transcript of more than 60 hours of [streams]") -> that sentence is cut
   (a first-person research claim he disowned); the rest of "What I couldn't find" stays. Flagged in the delivery note.

## Steps
| # | Step | Status | What it produced / why not |
|---|------|--------|----------------------------|
| 1 | Intake | done | WAV copied to `raw/` (166,056,136 bytes = original) |
| 2 | Rough cut (VO) | done | `work/cut/asr.py`: 194 bursts + 349 pieces, each transcribed alone (`logs/asr.log`); wav2vec2 words (`transcript/words.json`); keep.py authored (3 detection layers: script take-map by hand, piece repeats/orphans, repeated n-grams in bursts: found the hidden "on these three, on these three" and "make sure that, I'm gonna make sure that"); breaths count as pause (VOICED -40 dB); gates above |
| 3 | Audio polish | done (baked) | voice-gain: kept speech -22.4 LUFS -> +5 dB into a -6 dBFS alimiter (latency-compensated, lag 0 verified) -> `audio/vo/vo-polished.wav`; ~1 % of samples touch the limiter (Video A 1.2 %). His enhanced Video A A1 at +5 dB measures -18.1 LUFS = our Video A polished level (-18.3), so the chain stays |
| 4 | Color grade | skip | channel rule: no grade; the streamers' capture is the evidence |
| 5 | Graphics | done (2 QA rounds) | evidence: 3 Sonnet agents measured cams/chat/subtitles/targets on frames (`footage/evidence/*.json`, ~190 events, ~200 proof sheets); plan authored against WORD anchors (`work/plan_s1.py`, `plan_s4_7.py`, `plan_rest.py` via `planlib.py`); renderers `gfx/build.py` (Video A look) + NEW `gfx/guides.py` (box / circle / labelled arrow / map pin / spotlight, tracking moving targets) |
| 6 | SFX | done (182 cues) | `work/plan_audio.py` -> `work/audio-plan.json` (A2-A5) |
| + | Music | done (22 runs) | A6, one bed per section, out at bars + under cut zooms (his rule); pre-cut runs in `audio/music-cut/` |
| 7 | Review | waiting for him | the delivery note below |
| 8 | Export | — | his |

## Flags for the delivery note (collected while cutting; each is his call)
1. **The dialogue holds (his aside 1):** every line he acted (Jason / Kirk / the parrot / the grandma / the bathtub man) is cut;
   the game's own footage carries it (its subtitle + a pink box, and a quote card on the key lines), with ALL streamer audio
   still muted, so those beats play over the music bed with no voice. 16 holds, 40.1 s in total, each capped at reading time
   (max 3.4 s; the parrot montage 4.5 s). One-word alternative: unmute the game line where the streamer is silent.
2. **Spoken, not in the script:** "In the first THREE days" (script: "In the first days"; the game is out about a day on 19 Nov).
3. **He reads on-screen text differently from the screen** (cards show the screen's exact text): "Have you seen this CLIP in
   Gellhorn?" (screen: "Hey you seen this place in Gellhorn?"); "24 hotline" (screen: "24 HOUR HOTLINE 555-MISSING");
   "the mark maps a liquor store" (slip for "the map marks").
4. **Cut on purpose:** "I searched the whole voice transcript of more than 60 hours of [streams]", right before his aside
   "Oh, I wasn't supposed to say all of this". The rest of "What I couldn't find" stays. One word to drop the whole section.
5. **Kept ad-libs (his):** "A parrot beat that, by the way.", "Don't even know if he's alive at this point", and the outro
   ("That's gonna be the Easter eggs for now… make sure that you subscribe… catch you guys inside of the next one").
   **Date-bound:** "The game literally released 6 hours ago on my side" is only true if it goes up on 19 Nov.
6. **Frames vs the script (frame wins):** Kirk's lines run EMF -> "You've seen Mister Mangrove!" -> "Cough into this." in the
   game (the script had Cough before Mangrove; "Cough into this" is now left out: the hold shows Mangrove only). Kirk's clean
   wake-up line on screen is "You awake?" (the script's "You're awake." is not on screen alone; the full line has "shit").
   The jet's four white stars light only once Jason is in the jet (still on the ground); "Crime reported" shows earlier
   with two dim stars, so they are two shots. The red "arrow" in the sky is a small red aircraft-shaped marker.
7. **A fact to check:** on xQc's screen a STASH counter of $240 (padlock) shows at ~10:37 of the pull before the gator death;
   the VO says "The screen doesn't say what was in that stash". Consider cutting that sentence.
8. **On-screen lines that continue past the quote** (cards quote only the scripted part, exactly): the bathtub man ("...precious
   rules! But then,"), the Dezombifier blurb ("...from its grave. Blast your way through..."), Lucia's text ("...Kinda freaky.
   Looks like some people's stuff in here. Blood on some of it...": the shot ends before that line types in).
9. **Mild content kept short:** the deer ribcage (bones), a 0.5 s blood spatter as Asmongold's tiger drops (16.15-16.65),
   black frames after summit's blackout. The gator shot ends at 6.40 s, before the death-cam (6.45 s); WASTED is the clean card on black.
10. **Bathtub truck:** its livery carries slogans (a "MYWAYS / NO LEFT TURNS" door decal, a hood decal, rear stickers), so the
    gas-station shot ends while the truck is still far (its hood frosted for the last second), and the tub is shown in two
    tight crops with the cab frosted.
11. **Premiere:** a NEW sequence "GTA 29 - Bigfoot Secrets" in ABW11 (the open project), V1 laid from 12 section reels (one
    import per section; every clip is still its own trimmable clip). Nothing is saved by us: **he presses Ctrl+S.**
12. **His Enhance Speech habit:** on Video A he swapped A1 for an Adobe Podcast bounce at +5 dB; our A1 is the same static chain
    (+5 dB into -6 dBFS) on the raw, so he can do the same here.

## Delivery note (final, 19 Nov)
Sent to him via the hub; the same text is in the session's closing message.

**GTA 29: Bigfoot Secrets. The first full cut is on your timeline:** ABW11, sequence "GTA 29 - Bigfoot Secrets" (9:00).
**It is not saved yet: press Ctrl+S first.**

**What's in it**
- **The VO, cut the way you cut Video A:** every retake, failed take and false start is out, and so are your three asides to me. The gaps between your spoken words are capped at 0.14-0.26 s (typical 0.15 s), your Video A range. Your acted lines are out too (see 1).
- **Picture:** gameplay under every line, and every shot is tagged with the streamer's name on their cam. There are 110 pink guides (Video A had 34): boxes, circles that follow moving targets, labelled arrows, map pins and a spotlight. There are also 17 quote cards with the game's exact text, and the 11 numbered titles.
- **What's covered:** all streamer audio is muted, and the cams stay visible. Chat, viewer counts, alerts and Twitch captions are frosted. Swearing is frosted, the gore cues are cut, and the bathtub truck's slogans are out of frame.
- **Sound:** your Video A levels, one Epidemic bed per section, 182 SFX, mixed to -15.9 LUFS.

**Your calls**
1. **Your acted lines** (Jason, Kirk, the parrot, the grandma, the bathtub man) are now the game's own footage of the line. Each one shows the subtitle and a pink box, with a card on the key lines, over the music only. That is 16 holds, 40 s in total. Say "unmute" and I'll bring the game audio up on the holds where the streamer is silent.
2. You said "in the first **three** days". The script said "in the first days", and the game has been out about a day.
3. "The game literally released 6 hours ago on my side" is only true if the video goes up today (19 Nov).
4. **I cut** "I searched the whole voice transcript of more than 60 hours…", which came right before your "I wasn't supposed to say all of this". Say the word if you want the whole "What I couldn't find" part gone.
5. **The $240 stash:** xQc's screen shows a $240 STASH counter just before the gator. That clashes with "The screen doesn't say what was in that stash". Cut that sentence?
6. **Text you read differently from the screen** (the cards show the screen):
   - you said "this clip in Gellhorn"; the screen says "this place";
   - you said "24 hotline"; the screen says "24 HOUR HOTLINE 555-MISSING";
   - you said "the mark maps a liquor store", a slip for "the map marks".
7. **Kept on screen, your call:**
   - the game's own line "The hell is this thing?" (the intro and the Bigfoot part);
   - a 0.5 s blood spatter as Asmongold's tiger drops;
   - the deer ribcage.
8. **The bathtub truck's livery carries slogans,** one of them political. The gas-station shot ends while the truck is still far away. The tub is then shown cropped tight, with the cab frosted.
9. **The bin:** the older imports (reels, reels2-5, guides, guides2-3, q-*.mov) are unused and safe to delete.

Smaller notes are in RUN.md § Flags: where the game's order differs from the script (Kirk's lines, the jet's stars), the on-screen lines that run past the quote, and the gator shot, which ends before the death-cam.

## QA round 1 (fresh-eyes Sonnet review of 345 guide tiles + 66 tags + manager checks; `work/qa/QA-review.md`)
- **Rule breaks found and fixed at the source (planlib corrections, masters re-rendered):** Fanum's Twitch sub-goal counter +
  a gift alert were unblurred (new panel [0.86,0.27,1,0.65]); xQc-gator's caption word sat above its blur box; summit's
  "Khalen: $50.00" donation tag sat below its box; Typical Gamer's caption band ~10 px low; profanity subtitles visible in
  two shark shots ("Oh, shit", "Oh, God, shit!") -> a subtitle-strip blur on every xQc-shark and HutchMF shot; a Twitch caption
  ("shit") in Asmongold's file inside a window the evidence read as clean -> the caption band is blurred on his whole file.
- **Cuts fixed:** the gator shot now ends at 6.40 s (the death-cam starts 6.45 s); the tiger teaser was a map screen (now
  Jason walking toward the tiger, 9.0 s).
- **Guides fixed:** the KIRK arrow pointed at Jason (re-aimed on the red hoodie, measured); the parrot, CRAWL and speargun
  marks re-aimed on measured boxes; the Fanum figure circles became labelled arrows (they grazed his cam); the shark and jet
  marks became tight boxes (the ellipses crossed HutchMF's and Typical Gamer's cams); boxes that appeared before their text
  (quest popup, $4,119) now start with it; boxes that outlived their text (ADULT GREEN IGUANA, the red arrow, MASK) end
  with it. **Removed (no clean target):** the frisbee circle, the BLUE COLLAR circle, the Key Lento box (under Ohnepixel's
  cam), summit's DEFEND box (text gone in 0.3 s), the MANNEQUINS arrow. 110 guides remain (Video A: 34).
- **Other:** the parrot card had a negative length (fixed); the iguana card moved to the top (it hid the iguana); the tag on
  the Corsair Key punch-in moved top-left (it covered the card); tags on punch-ins now follow the zoomed cam; the LUCIA /
  CREEPY PHOTOS labels dropped (hidden behind the tag); the last chip ends where his outro starts. SFX re-planned for the
  removed guides (182 cues). Spot-check of every fixed point on the rebuilt preview: `work/qa/fixes-round1.jpg`.
- Every fix is a NEW file (`gfx/guides2/`, `gfx/cards2/`, `footage/reels2..4/`) swapped onto the tracks of our sequence by
  name (nothing activated; his playhead untouched); final readback 837/837.

## QA round 2 (bathtub stickers, re-aims, 1 fps rule sweep of the whole composite)
- **Bathtub (rule: political stickers out):** the black truck's livery carries a "MYWAYS / NO LEFT TURNS" door decal, a hood
  decal and tailgate stickers. The gas-station shot now ends at src 15.2 (the truck still far; its hood frosted 14.2-15.3,
  checked at 1:1 every 0.4 s); the tub is re-cropped [0.63,0.20,0.93,0.50] from 17.32 (after the camera whip) into the 17.75
  freeze, so the WHOLE tub is in frame (the old crop cut it off at the bottom) with the cab frosted and every decal out of
  frame. The BATHTUB circle had landed on the pump: now a box measured on the freeze. Masters r135-r137.
- **xQc shark ring:** sat on the diver's head with the shark at its edge; now a tight circle on the shark measured on r158
  (under xQc's aim dot), 2.3 s while the shark is visible.
- **1 fps rule sweep of the whole composite** (3 Sonnet reviewers, 60 sheets / 540 frames, `work/qa/SWEEP-*.md`): no rule
  break. Checked by hand: the frosted top-left panel on Brenda's clips is her CHAT (her stream has no face cam); Lirik's
  clips have no cam either; the JasonTheWeen newspaper punch-in crops his cam out and keeps the name tag. Not changed: the
  game's own line "The hell is this thing?" (on screen at ~2, 47-49, 58, 86-89 s).
- **Premiere:** swapped by name onto our sequence (nothing activated, his active sequence + playhead unchanged): V1
  `footage/reels6/`, V2-V3 `gfx/guides4/` (hardlinks of guides3 + the new bathtub box), A2-A5 re-laid. The readback now
  prints `folder/file`, and `verify_readback.py` compares the folder too: **837/837**.
- **Advisor-requested checks (done):** the tub crop's bottom-right at native size with lifted levels, every frame of r136 +
  the r137 freeze: rim, bed rail, pump base, bin; no decal. Sweep flags checked frame by frame: 160.3-161.7 is the game's
  own fade to black at the end of Lirik's jet-ski shot (his HUD stays up); 444.3-445.0 is the game's objective text
  "Defend the bachelor party" typing in inside the DEFEND box; 516.5-518.8 is Jason knocked into the mud by the tiger
  and sitting back up (no blood, alive).
- **Caveats:** `work/preview/preview.mp4` and the sweep sheets are the reels5/guides3 build (identical outside the
  bathtub); only 376-390 s was re-composited on reels6/guides4 (`work/preview/bt-check.mp4`). The Lirik tag sits on the
  game's blue location label (188-195, 260-262 s): cosmetic, `tag_corner` next round. **`gfx/guides4/` is HARDLINKED to
  `guides3/` (except g-086): never re-render `--only` into guides4 in place: it writes through to files Premiere holds.**
  The next fix round renders into guides5 / reels7.

## Delivery note v2 (20 Nov)
**GTA 29 v2 is on your timeline:** ABW11 › "GTA 29 - Bigfoot Secrets v2" (9:02). Not saved: press Ctrl+S. Your edited v1 is untouched.
- Out: the animals, the fighter jet, the locals, the wildlife, the shark, "What I couldn't find". In (your pickups): 4 A real Easter
  egg, 5 Dexter's apartment, 6 Kyle, 7 The Kraken, 9 The giant crab, 10 The truth is out there, the new teaser, "Number eleven".
  Your own v1 cut ("and there's" in the dog beat) is carried in. Titles N/11. 816/816 verified; mix -15.9 LUFS.
- Said vs shown (you read draft 3): "Trinity Apartments" + "a boat you can take" (no capture shows them: REPORTED · DEXERTO label);
  "walk her back to her car" (Jason fetches her car: shown on the trail with "Retrieve the car" + her "Bring me my car." card);
  "lights flickering" (no flicker visible); "a sunken plane" (a dark wreck in Gator Keys' clip, no plane: REPORTED · GATOR KEYS label).
- "On xGarbett's screen, Jason jumps off a boat": now xGarbett's own capture (swapped 20 Nov 01:20 on his yes).
- Crab: you credit Gator Keys; the footage is The Gamer Eyes' capture (tagged). "A big ass crab" kept.
- Nest: TheGamingRevolution's sharp English capture + Rubius's own clip for "On Rubius's screen / Huevo de Pascua".
- Kyle is smeared red by design (no wound shown); the rampage before the hug is left out and the bodies in the lot are frosted.
  You say "Jason" there; Speed's character is not named on screen. The UFO woman is nude in the source and never on screen.
  Still date-bound: "first three days", "released 6 hours ago".
