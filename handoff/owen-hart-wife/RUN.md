# Owen Hart Wife — RUN

## ▶ STATUS: resume here (2026-11-04 19:25): v1 DELIVERED, waiting for his review
- **File:** `E:\Shorts\Abudance Wisdom Shorts Exports\Final Renders\Owen Hart Wife.mov` = `X:\Claude Projects\Exports\Owen Hart Wife.mov`
  = `outputs/Owen Hart Wife.mov`, sha256 dc68aaa79a01c5efd30a5118f60bff2cfde6f6492c7e51425ddb09fa1c11e25d. H.264 1080x1920
  30 fps, 1531 frames, 51.033 s, 34.6 Mb/s, PCM 48 kHz, -14.1 LUFS / -1.6 dBTP, export QA PASS. Report: [REPORT.md](REPORT.md).
- **Built from:** `renders/finish.mp4` (v4: reviews 2+3 zooms, pre_sharp, chunks from `renders/stageA_v3.mov`) +
  `renders/mix.wav` (CTA mids 23.70 / 36.25, no end screen).
- **QA:** `proof/final_edges.jpg` (30 cuts clean), `proof/final_asr.txt` (his cut word for word; "down" ends 50.86 measured, the CBC reporter starts 0.4 s after his out-point,
  no reporter), A1 gaps 0.02 s, `proof/cta_check.jpg`, brief § 5 boxes in REPORT.md.
- **CTA mid 1 moved 20.80 -> 23.70:** at 20.80 the pill sat on Bret's nose during "my dead brother"; his own Harry pills
  sit on letterboxed overlays (`proof/harry_cta_ref.jpg`), so it now enters over the O4 Jarrett letterbox.
- **Open for him:** the JR crowd fans (blur?); everything else per his Tella. Next on his notes: one finish render
  (`STAGE=renders/stageA_v3.mov bash build/render_chunks.sh`) + `build/export_cta.py`.

## ▶ previous status (2026-11-04 19:05): REVIEWS 2+3 PORTED, v4 finish rendering (chunks, renders/stageA_v3.mov)
- **Harry review 3 (relayed, README § 3 corrected):** same-camera jump cuts = ONE zoom layer; a new layer only on a change
  of person / camera / overlay. make_timeline "zooms: one per SHOT CHANGE" -> 19 zooms, `win/zoom_paper.py` PASS.
- Stage A patch done + verified: `renders/stageA_v3.mov` (3061 frames; `win/splice_check.py`: only S02 + S13-14 changed,
  `proof/martha_patch.jpg`, `proof/bret_patch.jpg`); deepest-zoom stills `proof/v3b.jpg`.
- **Running (bg):** `STAGE=renders/stageA_v3.mov bash build/render_chunks.sh` -> renders/finish.mp4.
- **Next:** export_cta → final_edges + asr_file + loudness → § 5 boxes → copies → REPORT QA_PENDING → notes.

## ▶ previous status (2026-11-04 18:55): HIS HARRY REVIEW 2 PORTED, Stage A patch rendering
- **His Harry review 2 (relayed by the Harry session, confirmed in README § 3):** the sine ease is REJECTED ("missing the
  plot"); his zoom is a TRANSITION zoom. Ported from `projects/harry-diana-photos` v3: one zoom per SHOT (restarts at 1.00
  on every cut), `zoom_curve: 'table'` + `zoom_long_after: 2.5` (finish.py `long_curve`), `depth()` with the short-shot
  cap, HOLD on O5 (Austin -55 % on his own, `win/his_zoom.py`), `win/zoom_paper.py` PASS. `pre_sharp` 0.25 + grain on the
  overlays/stills (gamma 0.85 on the video overlays), 0.5 on every face setup (`proof/cmp_faces1/2.jpg`).
  `build/finish.py` = Harry v3 + `pointer_mg` (old: `build/finish.v2ease.py`, `build/make_timeline.v2ease.py`).
- **Head-lock bug fixed:** `smooth_track.py` jump hold 60 -> 200 (x2 sources). S02 (Martha) + S13/S14 (Bret) now slow
  follows; `X_pos {'D0': 480}`. Old track: `build/track.v2.json`.
- **Running (bg):** `stage_a.py render renders/stageA_p02.mov 162:398` + `renders/stageA_p13.mov 1230:1418`.
- **Next:** splice into `renders/stageA_v3.mov` (old 0-162 | p02 | old 398-1230 | p13 | old 1418-end) → `finish.py stills`
  (S02, S13, S14 + a few) → point `build/render_chunks.sh` at stageA_v3 → export_cta → QA → copies → REPORT → notes.
- The ease-zoom chunks are parked in `renders/chunks_ease/` (not used).

## ▶ previous status (2026-11-04 18:05): FINISH RENDER waiting for MEMORY (the PC is at its commit limit)
- **Done since 17:15:** `renders/stageA.mov` (3061 frames at 60 fps, like Harry's) · `renders/caps_capcut.mov` (3062) ·
  finish stills checked (`proof/finish_stills*.png`, `proof/sheetA-F.jpg`): hook pointer MG, labels, letterboxes, grays OK.
  Two fixes: `sat_level {'O': 0.72}` (Vince TSN skin 0.84/2.07 -> 0.72/1.75, `proof/sat_compare.jpg`), GMA label y0 1362
  -> 1438 (under its band, `proof/label_test_crops.jpg`). Kept: Bret's tight crop (Fox super), the TSN set logo top right,
  the white podium in O10 (all in the source). JR crowd fans of unclear age: flagged in REPORT.md, not blurred.
- **Blocked by memory:** the one-pass finish died at frame 300 (MemoryError, 120 of 127.7 GB committed: his Premiere +
  PProHeadless + AME + Photoshop + AE, plus other sessions' asr / his_zoom jobs). Now `bash build/render_chunks.sh`
  (500-frame chunks, each waits for >= 3 GB RAM + 6 GB commit headroom, retried) runs in the background -> renders/finish.mp4.
- **Next:** `python build/export_cta.py renders/finish.mp4 renders/mix.wav "outputs/Owen Hart Wife.mov"` → `win/final_edges.py`
  + `win/asr_file.py` → brief § 5 boxes → copies (E: Final Renders + X: Exports) → fill REPORT.md QA_PENDING → notes.
- LESSONS written (2026-11-04 · Owen Hart Wife build: kit gotchas). Re-run recipe: § The raw cut → Re-run recipe: the code build.

## ▶ previous status (2026-11-04 17:15): CODE BUILD, Stage A waiting on the GPU lock (Harry session holds it)
- **His Harry review applied here too (relayed by the orchestrator):** zooms = ONE smooth eased push-in per block
  (`zoom_curve: 'ease'`, sine in-out, depth 1 - min(0.08, 0.04 x dur)); head lock = static anchor per shot (Harry's new
  `smooth_track.py`; only S14 slow-follows); END SCREEN OFF (`cta.end: False`, export_cta patched), mids 20.80 / 36.25 stay.
- **Done:** everything in the previous block + `build/zoom_layers.json` (19 eased push-ins) · `renders/caps_code.mov` ·
  `renders/mix.wav` (-14.10 LUFS, -1.60 dBTP; 17 swishes, ECT card 0.30, CTA mids 17 dB under the voice).
- **Running (bg):** gpu.lock wait → `stage_a.py render renders/stageA.mov` → `captions/capcut_pass.py` → `renders/caps_capcut.mov`.
- **Next:** `finish.py stills renders/stageA.mov renders/caps_capcut.mov renders/stills.jpg <t...>` (hook MG, labels,
  letterboxes, grays, CTA band) → `finish.py render renders/stageA.mov renders/caps_capcut.mov renders/finish.mp4 --audio
  renders/dialogue.wav` → `build/export_cta.py renders/finish.mp4 renders/mix.wav "outputs/Owen Hart Wife.mov"` → QA (§ 5,
  edges, final ASR, gaps, no child) → Final Renders + Exports → REPORT.md → LESSONS.
- **Credits:** 1,042 → 981 today (incl. the Harry session's 27): this job 2 stills (4) + 7 clips (35).

## ▶ previous status (2026-11-04 ~17:00): code build started (zooms were the old curve, end screen ON)

## ▶ previous status (2026-11-04 ~15:45): BUILDING. Stretcher slot = the arrival photo, grayed (his answer).
- Producer slot: stunned crowd (default stood, no objection).

## ▶ previous status (2026-11-04 ~15:30): overlay picks in BRIEF.md § OVERLAY PICKS; 2 slots ASKED
- Catalog pass written (BRIEF § CATALOG PASS). Picks for his 11 slots written; asked him about the 2 that have no
  source: the stretcher (only the AP paramedics-in-the-ring photo exists) and a shocked producer (none on camera).
- NEXT on his answer: Higgsfield 4K on the hook photo (test the rate) → Topaz research (Bolt Motivation) → copy the
  Paris kit (`projects/paris-shock-therapy/build/` + `captions/`) and drive it from `premiere/his_v1.tsv`.
- Web fetches: a desktop-browser User-Agent was refused by the auto-mode classifier (bot-check circumvention):
  never spoof; CBC's image CDN works with plain curl.

## ▶ previous status (2026-11-04 ~14:40): HIS TELLA 1 IS IN, resolved into BRIEF.md § TELLA 1
- **He re-cut our raw cut himself** (51.03 s, read-only dump `premiere/his_v1.tsv`, now also `premiere/readback.tsv`;
  our own last placement is kept in `premiere/v1/readback.tsv`). HIS CUT IS THE SPEC: never re-place over it. Re-ASR of
  his A1 (`win/asr_a1.json`) = the brief's words in his order (no "no one", B7 from "He was everything to me").
- He marked 9 overlay slots on V2/V3 (table in BRIEF.md § TELLA 1). Sourcing scan of the doc (`guide/doc_a/b/c.jpg`,
  1 frame / 12 s): Blue Blazer promo + entrance material ~5:36–6:00 and ~21:24–21:36, the matches that went on that night
  ~18:48–19:36, Over the Edge arena ~8:24–9:36. Frame-check every pick for the fall, the post-fall ring and children.
- **ANSWERED 2026-11-04: "Use the stretcher"** (a grayed-out still, slot V2 14.23–16.47 only). Was: His Tella asks for a grayed-out image of Owen on the stretcher under "Owen
  Hart has died"; brief hard rule 6 forbids the stretcher. Default offered: a grayed-out portrait of Owen instead.
- Then the build (quote re-stated to him: his extra overlays + 2 motion graphics + the Topaz research add ~2–4 % → the
  build ≈ 7–10 % of the week; Higgsfield ≈ 20–40 credits for stills at 2 each + short letterboxed clips).

## ▶ previous status (2026-11-04 ~13:30)
- **RAW CUT PLACED in ABW10, NOT saved** (he saves): bin **"Owen Hart Wife"** › **"Owen Hart Wife - raw cut"** (clone of
  "Onyx reaction template (empty)" set to 30.00 fps, display 104). **61.80 s.** V1/A1 27 clips each (source audio
  only), V2 6 picture-only overlays, 8 beat markers. His active sequence ("Sequence 40") restored after each window.
  Placed 3 times in this session (v1 → B7 overlay fixes → final), each re-place only after `run_replace.py` confirmed
  the sequence unchanged since our last read-back. Final read-back: `premiere/readback.tsv` (= `premiere/v1/readback.tsv`).
- **Verified:** every V1/A1 clip holds exactly the measured edge (`win/verify_eff.py`), except B5 "no one", held one frame
  early (133.3667–133.9000 vs 133.4000–133.9333; re-ASR still hears "no one"). No gaps. A1 rebuilt from the read-back and
  re-ASR'd (`win/asr_a1.py`): all 8 beats are the brief's words, plus "And" before Landsberg's "you allowed".
- **Hard rule 1:** `win/gap_check.py` flags five ASR gaps over 0.25 s, all ruled out by the 5 ms level view. B5
  "continuing→None", "performers→none" and "producers→not" read 0.32–0.34 s by ASR, but the level never drops to room
  tone (min −38 to −45 dB vs a −54 floor). The closed joins hold 0.11–0.16 s. B7 "me.→I" has ~0.17 s of real quiet
  (69.80–69.97, then a soft "I"). B7 "goodbye→I" has 0.1 s + 0.19 s (72.1–72.2, soft "I" 72.2–72.3, 72.3–72.49).
  Whisper ends words early on the reverberant PA audio. B1–B4, B6 and B8 have no ASR gap over 0.25 s.
- **Picture:** `proof/sim_readback.jpg` shows adults only, no fall, no ghost frame at an overlay edge, and no uncovered
  child frame. Child check frame by frame on the exact crops: B1 and B8 Martha overlays at 10 fps
  (`proof/cc_martha.jpg`), B7 jersey→hug and B8 Owen ring at 4 fps (`proof/cc_owen.jpg`). Her son never enters the
  crop.
- **WAITING for his check of the raw cut** (his default: stop here). Then the code build: catalog pass into BRIEF.md
  (CLAUDE.md learning loop 5) → copy the newest AW build kit (`projects/paris-shock-therapy/build/`) → grade per era,
  house captions, labels, hook card, CTA mid ×2 + Road to 1M end screen (kit AS IT IS AT BUILD TIME, `--subs 540000`),
  Higgsfield Topaz 2160p on the soft 1999 clips (ONE test clip first, measure the rate), −14 LUFS / ≤ −1 dBTP,
  `Owen Hart Wife.mov`, § 5 QA, § 6 report.
- Quote + questions sent 2026-11-03 in this session (via the AW Shorts orchestrator `local_3ae3a4cf-…`).

## Job facts
- Brief (locked, Affan 3 Nov 2026, v2): [BRIEF.md](BRIEF.md), byte-identical to
  `X:\Claude Projects\Abundance Wisdom\OWEN-HART-WIFE-EDITOR.md` (23:28).
- Channel's first WWE Short (niche test). Creative locked: cut exactly as written; anything that can't be done as written
  → stop and ask him, never improvise.
- Delivery: 1080×1920, 30 fps (brief § 4), −14 LUFS, ≤ −1 dBTP, `Owen Hart Wife.mov` →
  `E:\Shorts\Abudance Wisdom Shorts Exports\Final Renders` (+ identical copy in `X:\Claude Projects\Exports\`). Never C:,
  no phone copy unless asked.
- House rules: never save or export his Premiere project (ABW10); every Premiere window takes
  `projects/_onyx-batch2-2026-10/.locks/premiere.lock`; never kill another session's processes; work in silence (ffmpeg
  `-f null` only); lean mode (no agents without asking; builders Sonnet, never Fable); YouTube is blocked on this PC:
  never bypass it (no yt-dlp, no proxies).
- Censor list (drugs / self-harm / suicide): none in the brief's words. Re-check the transcript.

## Source search (2026-11-03): NOTHING on his drives
- Searched E:\ (all of it, incl. `Bullshit Folder`, `Shorts`, `YT Downloads`, `Downloads`), X:\, D:\, G:\My Drive (top
  level), C:\Users\affan\{Downloads,Videos,Desktop} for owen / hart / martha / wwe / wwf / mcmahon / landsberg / dark side /
  off the record / jim ross / bret / the 10 YouTube IDs. Only unrelated WWE files (Logan Paul etc.).
- Asked him to download (highest quality, H.264 / MP4, not AV1) into `E:\Bullshit Folder\Owen Hart\`:

| key | what | link | need |
|---|---|---|---|
| DSOTR | Martha, Dark Side of the Ring 2020 | https://www.youtube.com/watch?v=S98fKe5NByY | B1, B8 picture |
| JR | JR on air, Over the Edge 1999 | https://www.youtube.com/watch?v=7083QUvMGzA | B2 |
| GMA | Martha on GMA 1999 | https://www.youtube.com/watch?v=5FTaJfK4aao | B3 |
| BRET | Bret, The Last Word | https://www.youtube.com/watch?v=xYqyIFK9N3E | B4 |
| OTR | Vince + Landsberg, TSN Off The Record 1999 | https://www.youtube.com/watch?v=VVfl-1X1HNY | B5, B6 |
| GLOBAL | Funeral, Global News 1999 | https://www.youtube.com/watch?v=fnaDEOkAJh4 | B7 |
| CBC | Funeral, CBC 1999 | https://www.youtube.com/watch?v=uPFaHJxiRtk | B8 audio |
| OWEN | Owen b-roll (picture only) | https://www.youtube.com/watch?v=k64gfSPQk7Q | B7 picture, B2 optional |
| DOC | Seeking Answers doc (backup for B5–B6; narrator never in) | https://www.youtube.com/watch?v=hgkr4088L84 | backup |
| JRQA | JR Q&A 2017 (swap-in only if OTR unusable/claimed) | https://www.youtube.com/watch?v=P_93L0TYskc | only if needed |

## Intake check (2026-11-04, small.en on CPU: the GPU was 100 % / 7.3 GB busy with another job)
All H.264 + AAC 44.1 k, 29.97 fps except RAW_WeekAfter (30). Times below are SOURCE times, to be locked by ear later.
| raw/ file | his file (Henry) | what it really is | brief beat | words found |
|---|---|---|---|---|
| GMA_Martha_1999.mp4 (720×480) | Martha, Bret, Stu _ Helen Hart Interview GMA 1999 05 25 | ✓ GMA | B3 | 5:42.8 "Well, yes, we did discuss this stunt. And I did voice that I wasn't comfortable with it and that I thought it wasn't safe." → 5:53.1 (then "And I did say … safety nets") |
| BRET_LastWord.mp4 (640×480) | Sad Interview; Bret Hart … | ✓ Last Word | B4 | 2:34.5 "I actually know firsthand … they wheeled my dead brother passed / right past all the wrestlers and actually pushed wrestlers out the door and said go go go you're on" 2:46.8; "And I think that is really insensitive and really cold" → ~2:51 |
| OTR_Vince_TSN_1999.mp4 (640×480) | TSN - Off The Record … (1999-07-27) | ✓ OTR ORIGINAL | B5, B6 | Vince 2:04.0 "At the time, we didn't think of not continuing. None of the performers, none of the producers, not me. No one. Now whether or not that is because as performers it is ingrained in us that the show must go on, I don't know." → 2:23.7 ("for better, for worse … think a lot worse of me" 1:57.9–2:04.0). Landsberg ~3:06 "and you allowed the entertainment to continue with the blood of Owen Hart still in the ring, I'm not sure that's not disrespectful to Owen Hart and his family." → 3:18.0. Picture: Vince lamp set (ESPN Classic Canada bug top right + "otr" date bug bottom right: crop both), Landsberg single ~3:04, two-shot ~3:07–3:16. |
| FUNERAL_CBC_1999.mp4 (854×480) | 1999 News Report On Owen Hart's Funeral + Owen's Wife Speaks (+ an identical `_2` copy) | **CBC** (Joanne Faryon, CBC News) — the title says nothing; it is the brief's FUNERAL_CBC | B8 | 1:14.9 "I'm a very forgiving person, and I'm not bitter or angry, but there will be a day of reckoning, and this is my final promise to Owen, and I won't let him down." → 1:28.2, reporter "Owen was too good…" right after. Also "I loved him ×3 … he was my whole life" 0:46–0:56 (not used). |
| FUNERAL_Global_1999.mp4 (1920×1080, upscaled SD) | From the Archives_ Canadian wrestling star Owen Hart laid to rest … | **Global** (Doug Fraser, Calgary 7 News) — the brief's FUNERAL_Global | B7 | 1:00.0 "I would just like to say that I loved him, I loved him, I loved him. And I miss him because he was everything to me. I don't know how to say goodbye. I don't know how to let him go." → 1:15.0. Promise again 2:01.4–2:14.4. |
| DOC_SeekingAnswers.mp4 (1920×1080) | Owen Hart_ How WWE Continued The Show … | ✓ DOC (narrator elsewhere) | B5–B6 fallback (not needed: OTR has both) | **JR's live PPV announcement at 13:41.6–14:12.1**: "Tragedy befell the World Wrestling Federation and all of us. Owen Hart was set to make an entrance from the ceiling and he fell from the ceiling and I have the unfortunate responsibility to let everyone know that Owen Hart has died. Owen Hart has tragically died from an accident here tonight." Picture = the PPV broadcast, JR + Lawler at the desk (Sky Sports Live bug top right), then an arena wide from ~14:12 (post-fall: never use). Narrator starts 14:12.1 ("This was only announced…"). Also JR 2017 Q&A (swap-in) 12:43–13:41. Music under JR's words: unchecked. |
| RAW_WeekAfter_1999.mp4 (640×480) | Owen Hart, the Week After | **Raw, 31 May 1999** (JR: "a little over a week ago at Over the Edge … funeral services were held earlier today"), NOT the PPV announcement | — | Picture only, maybe: adult Owen "In Memory of Owen Hart 1965–1999" tribute ~0:54; funeral crowd shots (child check needed). |

| DSOTR_Martha_2020.mp4 (1280×720, 30) | Martha Hart on Owen Hart will NEVER be in the WWE Hall of Fame _ Dark Side of the Ring (08:22) | ✓ DSOTR clip (76.8 s, not the episode) | B1, B8 picture | 0:19.0 "I would never allow for Owen to be recognized by a company that actually is responsible for his death." → ~0:27.0. Before it: an unnamed male voice (0:00–0:19, not used). After it: Owen's son, adult (0:30+), not used. |
| JR_OverTheEdge_1999.mp4 (1280×720, 30) | Jim Ross announces the death of Owen Hart (WWF Over The Edge, 1999) (08:23) | ✓ JR PPV | B2 | 0:00 "Here in Kansas City tragedy befell the World Wrestling Federation and all of us." 0:08.2 "Owen Hart was set to make an entrance from the ceiling and he fell from the ceiling." 0:14.1 ‖ 2.9 s pause ‖ 0:17.0 "And I have the unfortunate responsibility to let everyone know that Owen Hart has died." 0:26.3 "Owen Hart has tragically died from an accident here tonight." 0:32.3. Picture: JR + Lawler at the desk the whole clip (one camera: closing the pause = a same-camera jump, head lock in the build). |

Owen b-roll (k64gfSPQk7Q) not downloaded: the doc + RAW_WeekAfter + DSOTR 1:02–1:05 (Owen in the ring) have adult Owen
footage for B7's picture.

### DSOTR picture problem (can't be done exactly as written → asked him, 2026-11-04 ~08:35)
Shot cuts (scene > 0.25): Martha is ON CAMERA only **0:22.2 → 0:26.43** (≈ 4.2 s, all of it speaking this line).
- 0:19.0–0:22.2 = home video, **a child on Owen's shoulders** (hard rule 5) under "I would never allow for Owen…".
- 0:26.43–0:29.6 = home-video ECUs (a young face: treat as a child) under "…his death".
- No DSOTR listening shot exists in this clip for B8 (brief: "a listening shot, so her lips don't fight the 1999 audio").
Proposed fix (default, pending his yes):
- **B1**: frame 1 = her on-camera face cropped to the EYES (mouth out of frame) under the hook card for 0:19.0–0:22.2
  (frames from 0:22.2–0:26.4, reversed if needed, Harry Diana precedent), then her real on-camera shot IN SYNC from
  0:22.2; JR's desk picture comes in a split second early under "…his death" (L-cut) instead of the home video.
- **B8**: the same eyes-only tightest crop of her 2020 face, slow push-in, so her mouth never shows under the 1999 audio.

## Cost quote (sent)
- ≈ 7–9 % of the weekly cap (≈ $150–200) in this session, lean: raw cut in ABW10 ≈ 2–3 %, code build + render + QA +
  report ≈ 5–6 %. Basis: `reference-usage-costs` (ABW Short built in code 4–6 %), the Paris build quote (7–10 % incl.
  overlay sourcing), Harry Diana's raw-cut flow.
- Higgsfield (only on his yes): Topaz 2160p on the soft 1999 clips, the played 9:16 crops with short handles. Measured rate
  on Paris: 5 credits / 2.7 s (no preflight exists for video). ≈ 45–50 s of 1999 footage → up to ≈ 100 credits. Balance
  1,042 (2026-11-03). Upload ONE clip first and measure the real rate before the rest.
- Local Topaz (free, GPU time): AW step 3; Proteus on every sub-1080p source (LESSONS 2026-10-31).

## Open questions (sent to him, defaults in brackets)
1. Music: brief wants a tense pulse + piano; his rule = music is his job, code builds ship with NO bed. [no music]
2. Subscribe CTA end screen after the hard cut on "let him down"? Brief hard rule 7 says no end card, and the 4.0 s end
   screen has no speech (hard rule 1) and would push past § 5 "Runtime ≤63s". [hard cut from "down" straight into the
   end screen's black; the 63 s limit and the always-talking rule count up to "down" only; his confirm needed; same open
   question as Harry Diana]
3. Current subscriber count for the end screen (`cta.py render --only end --fps 30 --subs N`). [540,000]
4. Mid pills ×2 (35–45 % / 70–80 %), off the hook, every label and the promise. The pill sits in the label band
   (y1392) and the brief puts a label on B1, B2, B3, B4, B5 and B7, so: mid 1 in B4 after Bret's label leaves ("pushed
   wrestlers out the door"), mid 2 can ONLY land on B6, Landsberg's "blood of Owen Hart still in the ring". Exact slots
   set on the real cut. [yes, those two spots]
5. Captions: house look (max 3 words, ~1 in 3 coloured, no commas/full stops, one constant base just under the lips
   ~y940–1130, labels low ~y1260–1280, above y1620; brief also wants nothing in the bottom ~20 %, so keep label bottoms
   above y1536) instead of the brief's word-by-word at 62–68 %. [house look]
6. Upscale: free local Topaz on everything (Proteus on every sub-1080p source) is the default; Higgsfield Topaz 2160p
   on the soft 1999 clips is an add-on, up to ~100 credits (balance 1,042), one test clip first because the 5 credits /
   2.7 s figure comes from one job and may be a minimum, not a rate. [local only until yes]
7. Check the raw cut in ABW10 before the build, or straight through to the .mov? [stop after the raw cut]

## Decisions
**Affan, 2026-11-04 (his words):** "Yeah don't add any music And do add the call to action at the end And yes upscale it
with the captions Yeah B basically yes to everything But except the music"
1. Music: **none** (his job). No pulse, no piano; the brief's music cues are skipped.
2. CTA: **end screen YES**: hard cut on "down" straight into the Road to 1M end screen's black. The 63 s limit and hard
   rule 1 count up to "down". Mid pills ×2 at the default spots (B4 after Bret's label; B6 Landsberg).
3. Subs: default **540,000** (he took the defaults; re-ask only if the render waits days).
4. Captions + labels: **house look**, not the brief's word-by-word at 62–68 %.
5. Upscale: **YES, Higgsfield add-on approved**: Topaz 2160p on the soft 1999 clips, up to ~100 credits; ONE test clip
   first to measure the real rate, then the rest. Local Topaz/Proteus underneath as usual.
6. Check point: default = **stop after the raw cut in ABW10** for his check, then build.
7. **Martha picture gaps (2026-11-04 ~08:40, his words): "Yeah just use some sort of like a painful overlay I just that
   that just fits the moment".** So: NOT the eyes-only crop. Where Martha's 2020 face isn't usable (B1's first ~3.2 s over
   the child home video, B1's last ~0.5 s, and all of B8 since no DSOTR listening shot exists), lay a painful overlay
   that fits the line (adults only, no fall / stretcher / post-fall ring). Frame 1 should still be Martha's face if a
   fitting painful shot of her exists (e.g. her at the funeral, cropped clear of the boy), so the § 5 box holds.

## Pipeline
| # | Step | Status |
|---|---|---|
| 0 | Brief saved, sources searched, quote + questions sent | ✅ 2026-11-03 |
| 1 | Intake: his downloads (`E:\Bullshit Folder\Henry`) → `dl/` (copies), `seq_src/` H.264 CRF 12 + PCM 48 k (native fps), audio windows → `raw/` | ✅ 2026-11-04 |
| 2 | Words (faster-whisper large-v3, `win/transcribe_fw.py`: WhisperX died twice) + edges (quiet runs, 5 ms view, re-ASR from every in-point) | ✅ 61.80 s |
| 2b | Raw sequence in ABW10 (30 fps), read-back verified, A1 re-ASR, gap check | ✅ |
| 2c | His check of the raw cut | ⏳ waiting |
| 3–8 | Code build (grade, captions, labels, CTA, upscale) → render → § 5 QA → § 6 report | pending |
| — | Music | none (his answer 2026-11-04) |

## The raw cut (actual, from the read-back; source = each upload's own clock)
| Beat | Timeline | Source in → out (pieces) | Words |
|---|---|---|---|
| 1 | 0:00.00–0:06.57 | DSOTR 0:19.77–0:26.33 | "I would never allow for Owen to be recognized by a company that actually is responsible for his death." |
| 2 | 0:06.57–0:19.60 | JR 0:08.23–0:09.37 · 0:09.73–0:11.37 · 0:12.33–0:14.13 · 0:17.03–0:23.27 · 0:24.23–0:26.47 | "Owen Hart was set to make an entrance from the ceiling, and he fell from the ceiling. And I have the unfortunate responsibility to let everyone know that Owen Hart has died." |
| 3 | 0:19.60–0:24.00 | GMA 5:48.30–5:49.57 · 5:49.97–5:53.10 | "I did voice that I wasn't comfortable with it, and that I thought it wasn't safe." |
| 4 | 0:24.00–0:31.20 | Bret 2:38.13–2:39.60 · 2:40.93–2:45.37 · 2:45.47–2:45.97 · 2:46.17–2:46.97 | "They wheeled my dead brother right past all the wrestlers and actually pushed wrestlers out the door and said, go, go, go, you're on." |
| 5 | 0:31.20–0:41.93 | OTR 2:03.87–2:04.93 · 2:05.17–2:06.30 · 2:06.67–2:08.03 · 2:08.77–2:10.07 · 2:10.47–2:11.73 · 2:11.93–2:12.87 · 2:13.37–2:13.90 · 2:17.83–2:20.97 | "At the time, we didn't think of not continuing. None of the performers, none of the producers, not me, no one. It is ingrained in us that the show must go on." |
| 6 | 0:41.93–0:46.27 | OTR 3:09.90–3:12.40 · 3:12.60–3:14.43 | "And you allowed the entertainment to continue with the blood of Owen Hart still in the ring." |
| 7 | 0:46.27–0:55.90 | Global 1:02.13–1:04.77 · 1:05.17–1:06.17 · 1:07.87–1:13.87 | "I loved him, I loved him, I loved him, and I miss him, because he was everything to me. I don't know how to say goodbye. I don't know how to let him go." |
| 8 | 0:55.90–1:01.80 | CBC 1:21.37–1:25.73 · 1:26.33–1:27.87 | "There will be a day of reckoning, and this is my final promise to Owen, and I won't let him down." HARD CUT |

V2 (picture only, "painful overlays", his answer 2026-11-04):
- B1 0:00.00–0:02.43: Global 2:04.00, Martha in the black hat at his funeral (her son cropped out), over DSOTR's home video
  of a child. 2020 Martha in sync from 0:02.43 ("…to be recognized").
- B7 0:46.27–0:49.30: Global 1:13.87, Owen with his arms raised in the spotlight.
- B7 0:49.30–0:55.90: Global 1:22.30, Owen in his #1 jersey dissolving (the source's own dissolve) into Owen hugging a
  wrestler in the ring. Both cover the family photos with children.
- B8 0:55.90–0:57.53: Global 2:19.00, Martha with the flowers ("There will be a day of reckoning").
- B8 0:57.53–1:00.27: DSOTR 1:02.00, Owen smiling in the ring corner ("…my final promise to Owen").
- B8 1:00.27–1:01.80: Global 2:07.00, Martha in the hat, the hook's shot ("I won't let him down").
Framing: JR pinned (the detector took Lawler); B6 = Landsberg speaking in the two-shot, then Vince silent for "with the
blood of Owen Hart still in the ring".

### Runtime and the brief's options
- 61.80 s (target ~60, cap 63). The brief's over-time options used: **B6 ends on "…still in the ring"**, and **Vince's
  "Now whether or not that is because as performers" is dropped**. Not used for time: B2 "Owen Hart has tragically
  died…", B3 head "we did discuss this stunt", B4 tail "really insensitive and really cold", B5 head "for better, for
  worse…", B8 head "I'm a very forgiving person…". B7 kept whole (the brief's 63 s trim not needed).
- Before the six edge fixes the cut read 63.03 s with leaked words; the fixes (§ lesson in AW LESSONS 2026-11-04) took
  it to 61.80.

### Brief § 5 at the raw-cut stage
- [x] Frame 1 is Martha's face (1999, at his funeral); first words "I would never allow".
- [x] No reporter or narrator audio (re-ASR of the read-back A1).
- [x] No child on any frame (V1 under every child shot is covered: `proof/sim_readback.jpg`).
- [x] No fall footage, stretcher or post-fall ring.
- [ ] Bret and Vince labelled: markers carry the label text; the labels themselves are the build.
- [x] Order as the brief.
- [x] No documentary narrator (the doc is not used at all).
- [x] Last words "I won't let him down", hard cut (the end screen follows in the build, his answer).
- [x] Runtime 61.80 s ≤ 63.
- [ ] −14 LUFS: the build's mix.

### Re-run recipe
```
python premiere/make_beats.py                                                     # sources.json, beats.json, framing.json
python ../../presets/youtube-shorts/abundance-wisdom/resolve_beats.py . --fps 30  # -> edl.json
uv run ../../presets/youtube-shorts/abundance-wisdom/plan_placement.py . --fps 30 # -> placement.json
python ../../presets/youtube-shorts/abundance-wisdom/place_sequence.py . "Owen Hart Wife - raw cut" "Owen Hart Wife" premiere/place.jsx
python premiere/run_replace.py     # re-place ONLY if unchanged since premiere/v1/readback.tsv (it checks); first time: run_window.py
python premiere/pp.py premiere/readback.js > premiere/readback.tsv
python win/verify_eff.py ; python win/verify.py ; uv run --with pillow python win/sim.py --readback proof/sim_readback.jpg
<whisperx-venv python> -I win/asr_a1.py ; uv run --with numpy python win/gap_check.py
<whisperx-venv python> -I win/asr_plan.py   # the same re-ASR on the PLAN (edl.json), before touching Premiere
```

### Re-run recipe: the code build (2026-11-04, Harry's kit; GPU steps under `../_onyx-batch2-2026-10/.locks/gpu.lock`)
```
PY=$HOME/.cache/video-editor/whisperx-venv/Scripts/python.exe
python build/topaz_faces.py                       # face excerpts -> renders/{DSOTRa,JRa,GMAa,BRETa,OTRa,OTRb}.mov (GPU)
python build/make_timeline.py                     # his_v1.tsv -> timeline.json, centers.json, pieces.json, overlays/picks.json
$PY build/finish.py centers                       # -> zoom_layers.json: AFTER EVERY make_timeline (it is not written there)
rm build/track.raw.json   # only after a SOURCES framing change; then:
uv run --with scipy ... build/stage_a.py track ; python build/smooth_track.py
python build/dialogue.py                          # -> renders/dialogue.wav (stage_a render needs it)
$PY build/stage_a.py render renders/stageA.mov    # GPU, ~24 min
python captions/make_words.py ; python captions/make_plan.py ; <uv> captions/render_caps.py render renders/caps_code.mov
$PY captions/capcut_pass.py renders/caps_code.mov renders/caps_capcut.mov      # GPU
$PY build/finish.py stills renders/stageA.mov renders/caps_capcut.mov proof/finish_stills.jpg <t,...>   # + build/skin_png.py
bash build/render_chunks.sh                       # -> renders/finish.mp4 (500-frame chunks, retried; no audio needed)
python build/mix.py renders/mix.wav               # -> -14.1 LUFS / -1.6 dBTP
python build/export_cta.py renders/finish.mp4 renders/mix.wav "outputs/Owen Hart Wife.mov"   # mids only, no end screen
python win/final_edges.py "outputs/Owen Hart Wife.mov" ; $PY -I win/asr_file.py "outputs/Owen Hart Wife.mov"
```

### Notes for the build
- Bugs to crop or push past: VICE (DSOTR, bottom right), ABC + clock (GMA, bottom right, visible in the raw crop), Fox
  Sports Net super + "Bret Hitman Hart" (bottom, visible), ESPN Classic Canada + "otr 07.27.99" (OTR), Global News bug +
  the "Credit: WWE" text (Global Owen footage). JR's file has no bug.
- JR's file is a tight upscale: at 266 % the crop is soft. The Higgsfield pass matters most for JR, GMA, Bret and OTR (480p).
- B2's four closed pauses are same-camera jump cuts on JR (head lock / steady across cuts in the build).
- DSOTR has a music bed under Martha (source audio, kept).
- ABW10 is open from `E:\Premiere Pro Exports\Adobe Premiere Pro Auto-Save\…\ABW10.prproj` (an Auto-Save folder path):
  told Affan, in case he expects his main ABW10 file.
