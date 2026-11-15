# RUN: speed-kicked-out-three-peat (AW Short, IShowSpeed)

## ▶ STATUS: resume here
- **15 Nov: TITLE AND TAGS given to him** (he asked "title? and tags").
  - Pick: **IShowSpeed’s Mom Kicked Him Out 🏆**. The options, the 23 tags (493 of 500 characters) and the evidence are in `proof/v21/TITLE-TAGS.md`. The raw API results are in `proof/v21/title_research.json`.
  - The pick names him: Bolt's 11.4M "His Mom Kicked Him Out On Live Stream" is about Nitro Camden, and Speed appears in it, so a title without his name could be read as that story.
  - The delivered file is unchanged.
- **14 Nov 23:20: REVIEW-2 FIXES RE-DELIVERED.**
  - The file is hash-identical (sha256 5d80b25c...) in Final Renders and Exports.
    - It replaces the 22:35 copy, and also a 23:10 copy that was out for ten minutes.
    - The 23:10 copy had the taller WIDE_A band's bottom bar crossing the 10.0 s subscribe pill. Fixed with `cta.mid_dy` 160 (under the bar, README § 12), re-exported only.
  - His notes (22:40), both fixed:
    - **The 2026 podium judder.** The source is 30p doubled to 60p, and the head lock followed the stair-step.
      - Stage A `dedup` (S22) rebuilds each duplicate frame by flow interpolation between the unique frames and interpolates the lock between the same frames.
      - `_unique_frames`: a frame is unique if its diff is >= 25 % of the p75 diff (46 of 86).
      - Face jitter 24.6 -> 10.0 (2024 12.0, 2025 11.6).
    - **The "pasty AI-ish" letterboxes.** Re-cut on Speed alone (WIDE_A / WIDE_B: 1.42x, band 560-1360, twin 2.5x), Topaz Chronos only, no Iris.
  - Gotcha: Chronos-only returned 75 of S08's 76 frames (stageT 2309). The tail frame was cloned under the transition and the concat re-done. `topaz_speed.py` now stops before the concat on any short part.
  - QA (`proof/v21/QA.md` round 3): export PASS, av_lag PASS, smooth_check all PASS. The cut and frame sheets were regenerated from this file and checked.
  - Lessons: AW `LESSONS.md` (Speed section, review 2). His sequences are untouched; nothing was saved or exported in Premiere.
  - **S03 stays the 2021 stream (`assets/clips/sewy_2021.mp4`). The research session confirmed after the 23:14 unblock that there is nothing to swap.**
    - The Apr 2020 face-cam stream (`assets/clips/old-streams/20200421_n2wj5MV78UM_sec05-23.mp4`, 720p30) is a REJECT: never use it.
    - Its face cam is a ~198x198 px inset (x 63-261, y 522-720), which would need ~5.5x against the 2021 fill's 1.62x: the pixelated look he ruled out.
    - The research session is checking late-2020 full-frame streams by thumbnail (the 4 Dec 2020 prank-call live, Fortnite squads, Rec Room, a Q&A). A pass would only be OFFERED to him as an optional one-span swap. His reviews never named this overlay, so it is never a must.
    - Its numbers and proof paths are in `assets/photos/ig/SOURCES.md`.
- **14 Nov 22:35: REVIEW-1 FIXES RE-DELIVERED (superseded by 23:10).**
  - The file is hash-identical (sha256 f03b6ed6...) in Final Renders and Exports, replacing the 22:05 copy.
  - His notes (22:15), each fixed:
    - Shannon centred (anchor = his nose, y 760);
    - both Club Shay Shay wides at FIT in a 607 px band with a 3.3x blur fill, so both people show;
    - the shake made subtle and easy-eased, with an exposure fade (`finish.shake` + `expo_fade`);
    - eased exposure fades on the 2024->2025->2026 cuts (transition 'expo');
    - labels through the caption FX stack (`finish.lt_fx`).
  - A latent bug fixed on the way: an inline comment had swallowed `Y_override` / `lock_full` / `lb_nose_y` in make_timeline2. The 22:05 render was unaffected, because track.json carried the same Y values.
  - The lessons are in the AW `LESSONS.md` (2026-11-14 Speed section).
  - QA: export PASS; all 22 cuts and the three transitions checked frame by frame (`proof/v21/cuts_sheet2.jpg`, `trans3_strip.jpg`, `final_sheet2.jpg`); av_lag PASS.
- **14 Nov 22:05: v2 FINAL RE-DELIVERED.**
  - `outputs/His Mom Kicked Him Out.mov` was copied hash-identical (sha256 d2de3f8e...) to Final Renders and Exports, replacing the 21:15 copies.
  - Fixes since 21:15:
    - S17 2-frame flash (floor_src);
    - shake re-tuned (44 px, 9-18 Hz);
    - Detroit beat = the Christmas photo of young Speed with his dad, as a portrait card;
    - a false "wide flash" note retracted.
  - Note for him: `proof/v21/NOTES.md`. QA: `proof/v21/QA.md` (round 2).
  - Open, each a one-span swap:
    - the Apr 2020 face-cam stream for S03 (research session, after the ~23:15 unblock);
    - the Mastro's original (17) if he prefers it for Detroit.
- **14 Nov ~21:15: v2 DELIVERED, first copy (superseded by the re-delivery above).**
  - `outputs/His Mom Kicked Him Out.mov` was copied hash-identical to Final Renders and Exports.
  - Note for him: `proof/v21/NOTES.md`. QA: `proof/v21/QA.md` (all pass).
  - Open swaps, each a re-render of one span, not a rebuild:
    - his 2020 face-cam streams (15) for S03 after the YouTube unblock;
    - an at-school photo for S02, if the research session finds one.
  - His sequences in ABW11 are untouched; nothing was saved or exported in Premiere.
- **14 Nov 18:40 (machine clock, PKT; earlier entries stamped ~19:30/~20:10 were mis-stamped): HIS TELLA 2 + "start the build after watching this, the final render, everything" -> FULL BUILD TO FINAL, no STOP 2.**
  - **His cut:** "Speed Kicked Out - v2 mom bits" re-sequenced BY HIM, read back READ-ONLY at ~18:45 into `premiere/rb2_v2.tsv` (38.505 s; his active sequence; unchanged: raw cut, v2b, alternates). Never touch it; the build is code from that read-back.
  - **His direction:** `BRIEF.md` § HIS TELLA 2 (deictics checked on frames `guide/deictic_a.jpg`, `guide/deictic_b.jpg`).
  - **Plan (advisor-checked 18:58):** catalog pass into BRIEF -> source stills (teen school photo; Speed + dad, REAL photos only, Higgsfield upscale with a face check, Lanczos fallback) + the old stream (E: `Lonely/IShowSpeed Original Cristan Ronaldo Sewy.mp4`, 2021, until better arrives) + podium picks (win25 ~44-48 / 60-64 s, soty26 ~328-345 s; frontal, mouth closed, no name bar, nose + face size locked to 2024, hard cuts) -> regenerate make_timeline (from rb2_v2.tsv), dialogue, captions (NFRAMES), Stage A, Topaz (delete the stale `renders/topaz/S01-S05`) -> finish stills of every new element (own gate) -> full render, mix (`build/sfx/` missing: copy from the Son), export_cta, QA, delivery.
  - **Fences:** fireworks label = 4 JUL 2022 · AGE 17 (true); no date on the kick-out or Detroit; never generate a "Speed with his dad" picture; CTAs placed by collision check.
- **14 Nov ~20:10: Affan is opening the v2 sequences (research session's message). "Speed Kicked Out - v2 mom bits", "...v2b (your slot)" and "...v2 alternates" are HIS now:** never delete, rebuild or re-place them. `run_v2build.py`, `run_altbuild.py` and the three `*_build.jsx` are DISABLED. Any change goes into a NEW sequence ("...v2.1") built by a new script that refuses existing names. Every edge fix (mine, the cold read's, the research session's) was applied BEFORE he opened them: v2/v2b final ~19:30, alternates final ~20:00. Before any later work, re-read his sequences (they may carry his edits).
- **14 Nov ~20:00:** alternates rebuilt (16 bits, 0 mismatches; his sequence unchanged): the research session's edge fixes were applied after re-measuring each edge, and A16 was added ("You know, she even now to this day, she still supports me."). A1+A2 are a full repeat of our 950K Short.
- **14 Nov ~19:30: v2 FINAL BUILD (after the cold read) in ABW11. WAITING ON AFFAN's pick: v2 or v2b.**
  - **v2** "Speed Kicked Out - v2 mom bits" (47.6 s): the stream moments sit between "...my dad in Detroit" and "Then I kept going".
  - **v2b** "...(your slot)" (47.6 s): all new bits between "My mom seen the video" and "So boom".
  - **Alternates:** 15 bits.
  - **Checks:** check_v2 0 problems on both; his sequence unchanged; chat columns reframed off; `SEQUENCE-v2.md` is the full write-up (flags, open items).
  - **After the YouTube unblock:** the 2021 mom-house clips (C1 VOD, C7) + the birthday VOD check (research session sources them). Then one more v2 window.
- **14 Nov ~18:30: v2 BUILT in ABW11, waiting on Affan's pick/approval.**
  - **Sequences:** "Speed Kicked Out - v2 mom bits" (THE PICK, true order, 47.58 s) + "Speed Kicked Out - v2b (your slot)" (47.58 s) + "Speed Kicked Out - v2 alternates" (15 bits).
  - **Checks:** `check_v2.py` 0 problems on both; his sequence unchanged (read back before/after); frame proof `proof/v2_sheet.jpg`; re-ASR `proof/seq_v2/asr.txt`. `SEQUENCE-v2.md` is the full write-up.
  - **Rebuild:** `python build/plan_v2.py v2_inserts.json "Speed Kicked Out - v2 mom bits" v2` (+ v2b), then `python premiere/run_v2build.py` (ALT=1 also rebuilds the alternates). It deletes only OUR v2/v2b/alternates sequences, never his.
  - **No Phase B until he approves.**
- **14 Nov ~17:40: v2 PLANNED, Premiere window queued** (`premiere/run_v2build.py`, log `logs/run_v2build.log`). Premiere lock held by other builders (Rise Above 17:01, then PRW 17:32).
  - **The window builds 3 NEW sequences** beside his: "Speed Kicked Out - v2 mom bits" (THE PICK, true order, 45.4 s), "Speed Kicked Out - v2b (your slot)" (his literal placement, 45.4 s) and "Speed Kicked Out - v2 alternates" (15 bits + markers).
  - **Checks:** his original is read back before and after (must be identical); `python build/check_v2.py v2|v2b` checks every clip.
  - **The pick and why:** `SEQUENCE-v2.md`. The 2022 fireworks argument (over the EMPTY ROOM: he is shirtless live), "I'm sorry" x3 and the 2023 birthday call (UNDER FACT CHECK; probable AW repeat) all sit after "Then I kept going". True order: they happened after the 2020 kick-out.
  - **Cold read:** running, output `COLD-READ-v2.txt`.
- **14 Nov ~17:20: HIS RULING on minors:** "doesn't matter if he's a minor, we're not publishing him in a weird way". Speed's own teen streams (15-17) are IN; other children are still flagged. Memory updated (`feedback-minors-rule-hp-film-ok`).
- **14 Nov ~17:10: agent 2 (Instagram + web) done.** Files: `mom/IG_PROOF.md`, `mom/WEB_NOTES.md`.
  - **Age window:** he lived at his mom's until ~Sep 2023, so mom-house streams from 21 Jan to Sep 2023 show him at 18.
  - **The only documented angry-mom stream** is the 4 Jul 2022 fireworks one (17).
  - **Instagram:** "mom then vs now" reels at 2.0M and 1.9M.
  - **⚠ The birthday call is probably an AW REPEAT:** the drive file carries the AW monogram and our caption/letterbox style (`mom/frames/birthday_short_12s.png`).
  - All of this was forwarded to the research session (it writes MOM-MOMENTS.md).
  - **YouTube is BLOCKED** since 16:42 (a bot check). No YouTube from this session.
  - The Chrome tab group of agent 2 is gone (its tabs are closed).
- **14 Nov ~16:20: mom-moment research.**
  - **Agent 1 (YouTube) is done:** `mom/FINDINGS.md` + `mom/candidates.tsv`, downloads in `mom/src/` + `mom/local/`, transcripts in `mom/asr/`, frames in `mom/frames/`.
    - Birthday call (21 Jan 2023, his 18th, adult): `bXgeLAHCcdQ` 23.90-27.12 "my mom's really not answering on my birthday?". The dad call exists only in the fan re-edit.
    - Fireworks stream (Jul 2022, Speed 17, minor), mom off camera: "Turn that stream off!", then "I'm sorry" x3.
    - Club Shay Shay adult tellings: "So she kicked me out" (single), "you can't do this in my house" (wide), "I'm not about to stop" (single), "I want to be a streamer. She's like, boy" (single).
    - YouTube stopped at an age gate (not bypassed); the minor-era mom-house YouTube leads were not downloaded.
  - **The research session (local_f3ae46ec) owns the rest:** it writes `research/aw-speed-pick-2026-11-13/MOM-MOMENTS.md`, and I was handed it all.
  - **Agent 2** (Instagram grid proof + web dating, no YouTube) is still running.
  - **Next for me:** the v2 clone (`build/plan_v2.py`, `premiere/run_v2build.py`, `build/check_v2.py`, tested) once MOM-MOMENTS.md lands.
- **14 Nov ~15:45: HIS TELLA 1 RECEIVED -> `BRIEF.md` § HIS TELLA 1.** He edited `Speed Kicked Out - raw cut` IN PLACE in ABW11 (27.694 s, read back `premiere/readback_his_1.tsv`): Keystone/therapist beat, 2024 card, "So the Streamer of the Year award goes to", "But my mom," and "I still love my mom" removed. **That sequence is HIS now: never delete or rebuild it** (`run_window.py` refuses; `delete_ours.js` disabled). His ask: find every "mom" moment that fits his criteria (mom-house streams where she comes in angry / tells him to shut the stream, Speed sad after; Speed calling his mom on his birthday at Adin Ross' house with no proper reply; any moment "we genuinely feel bad for Speed but he still kept going") and lay them between "My mom seen the video" and "So boom, she kicked me out" for him to mix and match; **no build until he approves.** Plan: a v2 sequence = a CLONE of his sequence + the candidate bits (2020-22 minor-era clips kept apart and labelled with date + age; siblings/other children = hard no). The Phase B files (timeline/dialogue/Stage A/captions/Topaz S01-S05) are STALE against his cut.
- **14 Nov ~15:30: BUILD PAUSED BY AFFAN: "I didn't give you the Tella video, don't start the actual build".** Phase B (the code build) must NOT continue until he sends his Tella walkthrough (his review of the ABW11 raw cut: per `feedback-walkthrough-videos`: transcribe the audio, sample the frames he points at, resolve it into this job's BRIEF.md, apply his edits to the sequence, THEN build). Stopped: my Topaz driver (killed at shot S06; S01-S05 were done in `renders/topaz/`, S06.mov is partial and is re-done on a re-run), gpu.lock released, nothing else running. Nothing committed, nothing saved or exported in Premiere. Everything done so far is prep and is kept: `build/` (timeline/dialogue/Stage A/captions/finish additions, see the Builder log), `renders/stageA.mov` + `caps_capcut.mov` (Stage A and the captions are built from the CURRENT cut: if his Tella changes the cut they must be regenerated from his read-back: `python build/make_timeline.py`, `dialogue.py`, `stage_a.py track/render`, `captions/make_words.py ... capcut_pass.py`).
- **The ABW11 sequence is the revised one** (beat 11b = "I still love my mom." on the single, swapped in on the research session's relay of "resume", before this stop). If he wants the earlier wide-shot stutter back or anything else, say so; his edits are decisions.
- **14 Nov ~06:00: PHASE A REVISED on the research session's go (Affan "resume"); PHASE B NOT STARTED (weekly meter 97 %, stop at 98 %).** Sequence `Speed Kicked Out - raw cut` rebuilt in **ABW11** (his sequence was unchanged since my read-back: identical TSV; his active sequence at the window start, `Sequence 05`, restored): 1080x1920 @29.97, **47.114 s (1428 frames)**, V1 18 + A1 18 + V2 3 + markers, **0 mismatches** (`premiere/readback.tsv`, plan `premiere/place_rows.json`). ABW11 not saved, nothing exported, nothing committed. Changes vs STOP 1: **beat 11b = "I still love my mom."** (Club Shay Shay clip, single 115.16-120.62; edges from the audio: silent 115.92-116.24, speech 116.26-117.2, "She was" starts 117.32; A1 piece 116.1827 -> 117.2504 = 1.07 s, Speed pitch 151 Hz; crop `st11` = same size and face height as beat 1) replaces the wide-shot stutter; beat 2 keeps his "right?"; the 2026 grid crop stays (a tighter crop on his tile is a >3.5x upscale of a ~480 px tile and still has the blurred audience behind him: noted, not changed).
- **RESUME Phase B from here** (new session or the next meter): (1) re-read ABW11 (`python premiere/pp.py premiere/readback.js`) and compare with `premiere/readback.tsv`; if he changed it, build from HIS read-back. (2) copy the Son's kit (`../mj-son-step-outside/{build,captions,win}`) into this job (my `build/` already holds `plan.py edges*.py valleys.py faces*.py crops.py sheet.py picks_sheet.py seq_audio.py readcheck.py probe_asr.py h264.sh`; none collide with the Son's names) and patch paths/sources/beats/cards; 60 fps timeline from the read-back on the 1/60 grid from the ORIGINALS (`research/aw-speed-pick-2026-11-13/src/hd/*`, mezz time = HD time except `spd_soty26_280` = soty26 - 280; the HD files themselves are 1080p; use them as the originals). (3) head lock + zoom table, Topaz per shot (Chronos 60 / Iris / Proteus 1x; stabiliser OFF on the interview and diner shots; anchor tests in `research/.../proof/finish/`), under gpu.lock (a Scott Topaz job held it all night). (4) captions by forced alignment on the clean A1, exact words incl. beat 2 "right?", beat 7 "'cause", beat 5 per the best pass, beat 11b "I still love my mom"; (5) beat-3 counter graphic on the V2 plate + beat-10 card "3 YEARS IN A ROW - 8 STREAMER AWARDS" + translation subtitle with low label "TRANSLATED FROM INDONESIAN"; (6) finish stills into `proof/r1/` + `NOTES.md`; STOP 2.
- Words for his ear (delivery note): the Indonesian; beat 5 ("mom's seen" vs "mom seen"); beat 7 "'cause" and the whisper-quiet lines; beat 8 "Streamer of the Year"; beat 9 "...IShowSpeed".
- Picks + frame sheets + deviations: `proof/picks/PICKS.md`. Timeline audio re-transcribed: `proof/seq/asr_by_piece.txt`.
- **Next (Phase B) starts from HIS read-back: re-read ABW11 first** (REBUILD is DISABLED since his Tella: the raw-cut sequence is his). If he changed the sequence, build from his read-back.
- **14 Nov: BUILD STARTED on Affan's "Yes, build v8".** Session `speed-kicked-out-build` (local_0a18dba6-8ce5-4b83-9f13-58f00c68202d, Sonnet), from `BUILD-BRIEF.md`. Stops: STOP 1 (raw cut in ABW11), STOP 2 (finish stills).
- On his yes: ONE Sonnet build session, house style `projects/mj-son-step-outside/`; run PITCH.md "Build checks". Never Jamal (16) or the young siblings.
- **13 Nov ~22:45: PITCH v8, NOT BUILT, "NOT max effort yet".** `projects/speed-kicked-out-three-peat/PITCH.md`, 11 beats,
  ~44-48 s, Affan's shape.
- **Sequence:**
  1. "At first, I didn't really have support."
  2. 2020: only online friends.
  3. "I had that one viewer…"
  4. A clip blew up.
  5. Mom saw the video.
  6. "So boom, she kicked me out… Detroit… kept going."
  7. **Sept 2025 Keystone stream: "It's a lot. I need a therapist… I need somebody to talk to, yeah, I feel alone… feel like
     nobody understands me."**
  8. Streamer of the Year 2024.
  9. Streamer of the Year 2025.
  10. 2026 ("I started from zero. Just a little kid with a big dream").
  11. "But my mom always supported me… I really, really love my mom."
- **Runner-up:** beat 7 between the 2024 and 2025 wins.
- **Open:**
  - v8 not re-read (meter at 90 %).
  - Keystone counter-evidence not searched.
  - The July 2026 Speed Shorts checked by title only.
  - Youshaei: age-gated.
  - By ear at build.
- **v7's childhood beat was cut:** `medium.en` hears "I WOULDN'T say it was hard", so v7 had reversed him.

## Job facts
- **Channel:** Abundance Wisdom (Shorts). Format: 9:16 short, code + Premiere build. Preset: `presets/youtube-shorts/abundance-wisdom/`.
- **Constraint (SUPERSEDED 14 Nov by his ruling: Speed's own teen footage is OK): every frame adult-era.**
  - Speed was born 21 Jan 2005, so nothing before 21 Jan 2023.
  - No siblings, and no 2020-22 streams.
  - Never use the 2025 nominee reel: it carries a 2021 stream clip.
- **Shot rule (measured):** every studio line plays on Speed's SINGLE shot. Club Shay Shay cuts to a wide two-shot mid-answer;
  the single-shot spans are listed in PITCH.md § Sequence A. Never crop a wide for a face beat. A line that sits on a wide gets
  swapped, not zoomed.
- **Sources** (all on disk under `research/aw-speed-pick-2026-11-13/src/`). HD section files start at the section's in-point
  (file time 0 = that source time).

| ID | What | On disk |
|---|---|---|
| `QaBBgNjc5Pg` | Club Shay Shay full episode | audio; HD `hd/QaBBgNjc5Pg_support.mp4` = 1:43:20-1:44:30; HD `hd/QaBBgNjc5Pg_mom.mp4` = 36:35-37:50 (same edit as the clip) |
| `52pXQVGHwEE` | Club Shay Shay clip | audio; HD `hd/52pXQVGHwEE_fam.mp4` = 0:00-2:20; HD `hd/52pXQVGHwEE_covid.mp4` = 5:50-6:20 |
| `auSbPov16vA` | 2024 SOTY, official | audio; HD `hd/auSbPov16vA_win24.mp4` = 3:38-5:12 |
| `fox09o3r2SU` | 2025 SOTY, official | audio; HD `hd/fox09o3r2SU_win25.mp4` = 3:08-4:40 |
| `hImVqMpdILg` | 2026 SOTY, official (beat 9) | `hd/hImVqMpdILg_soty26.mp4`, the full 368 s clip, 1080p60 |
| `P6fN-0yyTug` | Sept 2025 Keystone stream (beat 7) | `hd/P6fN_keystone.mp4` = 2:53:55-2:55:50, 1080p60 |
| `M1V5cpbdwtQ` | 2026, IShowSpeed's own Short (cover only) | 4K vertical AV1: transcode to H.264 before Premiere |
| `CmpgXX7ZWJU` | Mizkif (E3 only) | HD `hd/CmpgXX7ZWJU_miz.mp4` = 3:40-4:20 |

- **Transcripts:** faster-whisper small.en scouts in `scout/`. Run WhisperX on the chosen windows at build.
- **Check at build:**
  - The official @TheStreamerAwards "WINS Streamer of the Year 2026" upload. It was not up at ~19:00 on 13 Nov. If it's up, use
    it as the beat 10 source and note what its announcer says after the name.
  - Every word, by ear.
  - The proof frames: `proof/cutmap_*.jpg`, `proof/finish/anchor_same_region.jpg`.

## Builder log
- 2026-11-14 ~03:50 Phase A started (Sonnet builder, session local_f3ae46ec... child). Orientation done: BUILD-BRIEF, RUN, PITCH, SESSION-START, Son BUILD/RUN/QA, Jermaine ABW11 scripts. GPU busy (gpu.lock = Scott Topaz job, VRAM 7.0/8.2 GB) -> edges on CPU. Mezzanines go to `seq_src/`, wavs to `wav/`.
- 2026-11-14 Phase A (Sonnet builder). GPU busy all session (gpu.lock = a Scott Clary Topaz job; VRAM 7/8 GB) and RAM tight (1-5 GB free): everything ran on CPU, large-v3 failed to load twice (`mkl_malloc`), `medium.en` + wav2vec2 did the English windows, large-v3 `id` loaded once RAM freed (Indonesian). **WhisperX alignment is unreliable on the quiet Keystone audio and on the announcer windows (word times off by 0.2-1 s, e.g. 'It's' at 21.07 vs 23.2), so every piece edge is set from the audio itself: 10 ms RMS valleys near each PITCH edge (`build/edges_final.py`, `valleys.py`), cross-checked with `build/probe_asr.py`.**
- Mezzanines: `seq_src/spd_*.mp4` (libx264 crf 14, whole HD sections from t=0, soty26 from 280.000 s = a frame boundary); covers `spd_cover_b3.mp4` (baked blur+darken of the wide), `spd_walkup_v.mp4` (video only). Placer = Jermaine's `place_v3.jsx` body via `build/plan.py` (generates `premiere/place.jsx`).
- **Premiere in-point rule (confirmed twice here): the stored in-point = floor_seq(floor_src(request))**, i.e. floor to the source frame, then to k/29.97 in source time. Ask for the first SOURCE frame at/after the target (+0.3 ms); `plan.py` stores the expected value in `rows[i][10]` and `readcheck.py` compares against it. The first two placements had in-points 8-33 ms off the intent (B11b would have clipped the "I"); third placement exact. `place.out` always says "bridge_unavailable" yet the placement DOES apply (the read-back is the proof).
- `deleteSequence` works (own sequence only): `REBUILD=1 python premiere/run_window.py` deletes + recreates + places + reads back + restores his active sequence in one lock window. Three windows used (3:56, ~4:30, ~4:50); premiere.lock released each time.
- Shot-cut maps: the default `select='gt(scene,0.25)'` MISSED the single->wide cut at 34.70 on the Club Shay Shay file; use 0.06 on that show. Cuts used: support 34.70 (single->wide), 37.45 (wide->single); covid 12.89-18.10 single; fam wide 0-3.80, single 47.63-52.72 / ..62.81 / 105.56-111.28; win24 card->audience 20.75; win25 grid->walk-up 17.98; soty26 wide 319.37-322.93, then podium.
- Findings that changed the PITCH (all in `proof/picks/PICKS.md` § Deviations): beat 11's last line is on the wide; its clean start is "I really, I really, really love my mom"; beat 7's "yeah" is "'cause" to two ASRs; podium crop 444 not 520 wide.
- Phase A re-ASR (`build/seq_audio.py`, medium.en CPU): all lines present + in order; Shannon "Right."/"Correct." absent; beat 2 contains Speed's own "right?" (pitch check, PICKS § 9). Indonesian: `transcript/edges_id.json` (large-v3 id on the source) = the reconstruction. Weekly meter at STOP 1: 95 % (90 % at start; ~5 % used, over the 4 % aim because 3 Premiere windows + two failed large-v3 loads + shot-map re-checks). **Stopped at STOP 1.**
- 2026-11-14 ~06:00 Phase A revision (Sonnet builder, on the research session's message after Affan's "resume"): window 4 = `REBUILD=1 python premiere/run_window.py` after confirming his sequence equalled my last read-back. Beat 11b swapped to the fam-clip "I still love my mom." (see STATUS); read-back 0 mismatches, 47.114 s; lock released; his active sequence restored. Weekly meter 97 % at this point: **stopped before Phase B** (it needs the kit copy, the 60 fps timeline, Topaz per shot under a contended gpu.lock, captions and graphics: several % of a week).
- 2026-11-14 ~15:10 **PHASE B Phase 1 in progress** (Sonnet builder; user said "resume anyway" at 97 % meter). Kit copied from the Son (build/ captions/ win/, no-clobber; the Son's per-job JSONs not copied). Done: `build/make_timeline.py` (Speed: 20 shots from `premiere/readback.tsv`, setups ST/KS/P4/P6, overlays PLATE/CARD24/G25/WALK/G26/WIDE, zoom groups, transitions on scene changes only, hard cuts on same-camera jumps and END, labels, CTA at 12.0 / 32.4, counter) -> `build/timeline.json` 2827 frames (47.117 s); `build/dialogue.py` -> `renders/dialogue.wav` (47.114 s, -16.7 LUFS pre-mix, level match per source group, 15 ms joints, last piece hard cut); `stage_a.py track` (0-1 misses on 13 face shots) + `sheet` (`proof/r1/sheet_stageA.jpg`, checked) + `render` -> `renders/stageA.mov` (2827 f). The 2026 grid crop was tightened (scale 2.0, x 1380-1920) to lose a "Tube" fragment of the YouTube logo.
- Captions: `captions/captions.txt` (exact words), forced alignment on the final dialogue (`captions/make_words.py`; two words after long pauses start on the large-v3 times: 'cause 21.75, the beat-10 "iShowSpeed!" 35.40; the Indonesian beat's English translation is timed by hand from the audio's energy phrases), `make_plan.py`, `render_caps.py` (NFRAMES 2827), `capcut_pass.py`. **large-v3 on the final dialogue (CPU, `logs/asr_l3.log`) read:** "At first, I didn't really have support. / I didn't talk to my friends. I was only talking to my online friends. / I had that one viewer, and that viewer made me keep going. / There was a clip that kind of blown up. / My mom seen the video. / So boom, she kicked me out. I moved to my dad in Detroit. Then I kept going. / It's a lot. I need a therapist. Like, I need somebody to talk to. Because I feel alone. I feel like nobody understands me. / (All right) I show speed. Man, oh, man. [Streamer] of the year. / I show speed. / So, the streamer of the year award goes to... iShowSpeed! / But my mom, my mom always supported me, you know? She just didn't understand it. / I still love my mom." Findings: beat 5 = "mom seen" (settled); beat 2's "right?" is NOT a word to large-v3 (medium.en heard "right?"): the audio is kept, the caption is NOT shown, flagged for his ear; beat 7 starts "Like, I need somebody..." (caption added) and the quiet word is "'cause"/"because"; beat 8 "All right" dropped by large-v3 (kept, flagged) and "Streamer" heard "Freeman" (captioned STREAMER, flagged).
- Added to `finish.py`: `counter_mg` (beat 3: eye icon + 0 -> 1, then "watching"; `timeline.json` 'counter'). Cards/labels use the existing lower-third system (`lower_thirds`): "2020" 3.7 s, "SEPT 2025 - DAY 23 OF A 24/7 STREAM" 16.33 s, "2024" 24.69 s, "2025" 28.06 s, "2026" 30.16 s, card "3 YEARS IN A ROW / 8 STREAMER AWARDS" 35.3 s, small label "TRANSLATED FROM INDONESIAN" 37.27 s; no label before 3.7 s (hook = claim only).
- Running now: `build/topaz_speed.py` (per-shot Topaz, stabiliser OFF, Iris on faces/grids/wide, + Proteus 1x on the Keystone shots, gpu.lock per segment) -> `renders/stageT.mov`; `captions/caps_code.mov` -> `caps_capcut.mov` -> `renders/caps_capcut.mov`. NEXT: `finish.py stills renders/stageT.mov renders/caps_capcut.mov proof/r1/<out>.jpg <times>` (first/last frame of every shot, labels, counter, card, CTA moments), `build/skin_png.py`, `win/head_measure.py` + `smooth_check.py`, then `proof/r1/NOTES.md` and STOP 2.
- ~15:20 **Waiting on Topaz** (`python build/topaz_speed.py`, log `logs/topaz.log`, per-shot files `renders/topaz/S01.mov..`, final concat `renders/stageT.mov`; it holds gpu.lock per segment and resumes/keeps finished shots if re-run). Captions ready: `renders/caps_capcut.mov` (2827 f). Finish test on Stage A already passed (`proof/r1/test/test_labels.jpg`: grade, counter, labels, card, translation label, letterboxed 2024 card, zoom layers via `finish.py centers`).
  **When stageT.mov exists, run STOP 2 stills:** `PY=$HOME/.cache/video-editor/whisperx-venv/Scripts/python.exe; T=$(python - <<'P'` ... or simply: times = for every shot `t0+1/60` and `t1-2/60`, plus 4.1,5.5,6.6,17.0,25.1,28.4,30.5,35.9,38.6 and the CTA moments 13.3 / 33.7; `bash build/glock.sh "finish stills" $PY -I build/finish.py stills renders/stageT.mov renders/caps_capcut.mov proof/r1/fs/stills.jpg <comma times>`; then `python build/tile_stills.py proof/r1/fs proof/r1/test_shots 360`; `python build/skin_png.py` on the stills; `python win/head_measure.py` / `win/smooth_check.py` on stageT; write `proof/r1/NOTES.md`; STOP 2 report. CTA pill is composited by export_cta (Phase 2): the Son's proof_r1.py composited it on the stills (E:/Shorts/Abudance Wisdom Shorts Exports/CTA/aw-cta-mid-60.mov at 1.3 s).
- 2026-11-14 18:40-20:15 **v2 BUILD from HIS Tella 2 cut (Opus session).**
  - **Read back READ-ONLY:** `premiere/rb2_v2.tsv`. His sequences are untouched; Premiere had closed by ~20:00.
  - **Brief:** `BRIEF.md` § HIS TELLA 2 (deictics resolved on frames) and § Catalog pass (all 137 stills).
  - **Timeline:** `build/make_timeline2.py` -> `build/timeline.json`: 23 shots, 2310 frames, 38.50 s.
    - S17/S18: his "I'm out" clip opens on Shannon's reaction ("Really?") and the show cuts to Speed's medium single at fam 86.336. They are split; Shannon is static at his own framing.
    - S23 holds src 34.62. The show cuts to its wide at 34.65, so his out-point would have flashed ~0.15 s of the wide before the hard cut. Audio is untouched.
    - Podium matches: 2025 = win25 48.62 at 0.8x (scale 2.756), 2026 = soty26 317.65 (scale 2.95). Both lock to the 2024 nose height (Y 840) and face size; `proof/podium/` has the measurements and `proof/v21/stageA_checks.jpg` the cut frames.
  - **Dialogue:** `build/dialogue.py` now carries the FW original (`mom/local/E_fireworks_room.mp4` = mezz + 120.000, verified by frame diff 0.37). Output `renders/dialogue.wav`, 38.505 s, -16.6 LUFS pre-mix.
  - **Words:** medium.en on the dialogue (repo rule: no large-v3), `proof/v21/asr_medium.txt`.
  - **Captions:** `captions/captions.txt` v2, 66 captions.
    - His mom's line is italic gold (FX-58) and Shannon's "Really?" italic.
    - `make_words2.py`: align, plus medium.en stamps on the fireworks and announcers.
    - `render_caps` NFRAMES 2310 -> `renders/caps_capcut.mov`.
  - **Stage A:** `renders/stageA_v21.mov` (2310 f). The first attempt died on WinError 1455 (paging file / commit exhausted by other sessions); the retry was OK.
  - **Topaz:** `build/topaz_speed.py` -> `renders/topaz_v21/` -> `renders/stageT_v21.mov`. The stale v1 parts were moved to `renders/topaz_v1_stale/`.
  - **Finish additions (`build/finish.py`):** `memory_look`, `viewer_cutout` / `viewer_counter`, `shake`, `podium_label`. Test stills are in `proof/v21/fs/`; the graphic was re-laid out after test 1 because WATCHING collided with the caption line.
  - **Stills:**
    - Teen: Commons CC BY 2.0 photo (Speed at 16, 26 Nov 2021, arcade; credit "James Parker / Flickr"). Higgsfield bytedance 4K (2 credits, balance 868.75 before). The face is unchanged (`proof/v21/teen_face_compare.jpg`). Lanczos to 1300 px gives `assets/photos/teen/teen_school.png`.
    - Detroit: NO real photo of Speed with his dad from that era was found (the web agent found none; the Halloween 2023 video was rejected: crude apron text, a probable minor sibling in costume). The research session was asked at ~19:20 to search Instagram (`assets/photos/ig/`). If nothing lands, S16 goes back to his single.
  - **SFX:** `build/sfx/` (copied from the Son) plus `es_impact_deep.wav` (Epidemic "Designed, Boom, Cinematic, Deep, Boom, Impact") on the shake cut.
- 2026-11-14 ~20:30 **Photos swapped to the research session's Instagram finds** (`assets/photos/ig/SOURCES.md`, all real originals):
  - S02 = his own IG post of 4 Jun 2021 (16, cap selfie).
  - S16 = his dad's IG story of 25 Apr 2022 (Speed 17 or younger, with his dad; taken at a Mastro's, the sign framed out).
  - Both went through a Higgsfield 4K upscale (2 credits each; one failed job was not charged; balance 864.75 after the first two, the dad retry 2 more). The faces were checked against the originals and are unchanged (`proof/v21/teen_cap_face_compare.jpg`, `dad_face_compare*.jpg`).
  - The Commons arcade photo (teen_01) is unused, so no CC BY credit is owed.
- **Captions:** caption_shift -40 (win/lips_measure.py: the lowest lips post-zoom are at 1067, mouth bottom 1089 on S05).
- **Mix:** `renders/mix_v21.wav` = -14.00 LUFS, true peak -1.60 dBTP. Swishes on the 5 overlay entrances and the 2 photos, the impact on the shake cut (no louder than the voice in its 400 ms window), card sounds on the 0->1 tick and the ISHOWSPEED label, CTA cues at 10.0 and 26.5.
- **GPU:** held 20:09-? by the HP-films session's scout-transcribe. Topaz is waiting at S12; the finish test2 is queued.
