# RUN: harry-potter-prank ("Harry Potter Thought Snape HATED Him 💔"), Abundance Wisdom Short

## ▶ STATUS: resume here
- **12 Nov 2026, ~22:30: HIS REVIEW 1 APPLIED (captions late, dailies "Clayface"), v1 re-delivered** (same file name, sha256 72d45b84568c975f…, all
  three copies identical, export QA PASS). Captions: `capcut_pass.py` `CAP_DELAY` default -2 (was the baked +6 lag). Dailies:
  `build/bake.py` dly1-4 = Proteus x2 (.50/.40) + lanczos (was x4 .61/.70). Re-run = `bash build/rebuild_c.sh` (bake → Stage A → Stage B →
  captions pass → chunked finish) then `export_cta.py` + copies. Details: REPORT.md § His review 1. Open: the reveal still on the old
  Proteus x4 (ask if it reads pasty).
- **12 Nov 2026, ~22:10: HUB-SIDE CHECK of the delivery (Opus session).** The current `.mov` (sha 4642257b…, 21:20) is the
  house-style render. It postdates `stageT.mov` (21:00) and `finish.mp4` (21:19); `(v1).mov` = c72e5aec… (20:48).
  - Identical in outputs / Final Renders / Exports. 43.933 s, −14.1 LUFS, −1.6 dBTP, PCM 24-bit.
  - Frame sheet `proof/hubcheck/sheet.jpg`: hook ×3 with FX-78, DVD band + glow bars, dailies, reveal, Rickman cover, both
    CTAs, both labels (scrim), FX-58 blue on Gambon/Rickman. The "mic over caption" look at 4.0 / 36.2 s is the caption
    smear mid-entrance, not an occlusion (`proof/hubcheck/caps_mic.jpg`).
  - **One deviation for him:** exported at 30 fps (his cut's rate); the MJ-son template shipped at 60 fps (Chronos).
    Offered as one finish re-export.
- **12 Nov 2026, ~21:50: STYLE CHANGE DELIVERED: the same file name now holds the MJ-son-style render (Stage B Topaz on faces, sigma-2 lock, depth table); `(v1).mov` in outputs/ = the earlier kit-look render. Finish = `STAGE=renders/stageT.mov bash build/render_chunks.sh` → mix unchanged → `export_cta.py`. Proofs refreshed: `final_edges.jpg`, `final_labels_cta.jpg`, `joints_stageA.jpg` (on stageT).**
- **12 Nov 2026, ~21:20: STYLE CHANGE from the hub (Affan 19:45): build in the "MJ son step outside" house style, AS SHIPPED, AE grade
  KEPT (the hub corrected itself: NOT a Bolt grade; no Bolt numbers ported; no splits / cutaways added, his cut is locked).**
  Delta vs the first v1 (kept as `outputs/... (v1).mov`, `renders/stageA_v1.mov`): (1) head lock = MJ son's `smooth_track.py` (per-frame
  nose, Gaussian sigma 2, jump > 200 px held; v1 had Harry Diana's STATIC anchors); (2) Stage B = his Topaz on the head-locked Stage A,
  one segment per shot: Chronos (rdt 0.01) + scale 270 + Iris-3 x4 on the face shots (Dan, Rickman 2015), stabiliser OFF
  (`build/topaz_faces.py` → `renders/stageT.mov`; overlay bakes stay Proteus: Iris invents faces on those tiny crops); (3) zoom depth =
  README § 3 table by block length (`depth_for`: 0.86 … 0.67), no held-0.80 override (Snape slots still hold: their slow-mo is the move).
  Already matching and kept: AE grade layer 43, `table` + `long_curve` zoom, transitions, captions (≤ 3 words, ink y 1040-1079, pop +
  CapCut smear), mix (swishes −21 dB, −14 LUFS), CTAs, labels at y0 1262. Then: finish on `stageT.mov` → mix → export → copies.
- **12 Nov 2026, ~21:00: v1 DELIVERED (second render after the advisor's checks), at his review.** `Harry Potter Thought Snape HATED Him.mov` (sha256 72d45b84568c975f…) in
  Final Renders + `X:\Claude Projects\Exports\` + `outputs/`: 43.933 s, 1080x1920 30 fps, 1318 frames, 44.1 Mb/s, −14.1 LUFS /
  −1.6 dBTP, export QA PASS. Report + open questions: [REPORT.md](REPORT.md). Proofs: `proof/final_edges.jpg`,
  `final_labels_cta.jpg`, `final_asr.txt`. A review note = data + ONE finish render (REPORT.md § Re-run recipe); keep v1 as `(v1).mov`.
  **Lessons for the hub to port (this session touched only this folder):** (1) a scouting stub video can be BLACK (`raw/hsc_2070.mp4`):
  check pixels, not just ffprobe; (2) a Topaz Chronos bake can come back SHORTER than its input window: bake a tail handle
  (`dly1` lost 9 frames; Stage A died on "source ended"); (3) Iris invents a waxy face on a ~180 px crop, Proteus does not;
  (4) `stage_a.interp_frame` flow-warps ~96 % of frames on a 59.94 fps source: snap to the nearest frame (patched here);
  (5) full-bleed pre-baked picks go at y 960, not the band's 962; (6) a label over Dan's mic needs a scrim.
  (7) a head-lock claim needs a full-size before/after joint (`proof/joints_stageA.jpg`), not thumbnails: YuNet's nose on a talking face
  moves ±50 px with pose, phase correlation on a changing face gives response < 0.3, so read the joint by eye on guide lines;
  (8) Rickman's own crop puts his nose at x ≈ 596, not 540: set `X_pos` from his readback (X = px·1080 + (nose_x − 960)·1.7778).
- **12 Nov 2026, ~20:00: picture + captions + mix built; finish render in chunks.**
  Kit = `projects/harry-diana-photos/` copied into `build/` + `captions/`. Everything is re-runnable from `build/make_timeline.py`.
  - **Order that ran:** `build/bake.py` (Topaz) → `make_timeline.py` (from `premiere/readback_abw11_1850.tsv`) → `stage_a.py track`
    + `smooth_track.py` + `render` (`renders/stageA.mov`, head lock on Dan / Rickman 2015) → `dialogue.py` → `win/asr_dialogue.py` +
    `captions/fix_words.py` + `captions.txt` + `make_plan.py` → `render_caps.py` → `capcut_pass.py` (`renders/caps_capcut.mov`) →
    `mix.py renders/mix.wav` (−14.10 LUFS / −1.60 dBTP, no music) → `build/render_chunks.sh` (→ `renders/finish.mp4`) →
    `export_cta.py renders/finish.mp4 renders/mix.wav "outputs/<name>.mov"` → copies → QA.
  - **Bakes (`renders/bake/*.mov`, 60 fps, all under the GPU lock):** Snape ×3 (Chronos 0.5x + Proteus x2, crop 450x800),
    DVD band windows A/B (Proteus x2 on the 748x478 picture), dailies ×4 (Proteus x4 on the played 270x480), reveal (Proteus x4
    on 180x320, a hair wider than the played 176x314). **Proteus, not Iris:** Iris made a waxy invented face on the reveal crop
    (`work/tz/ab_rev_faces.jpg`). No watermark (`proof/bake_sheet.jpg`, no token errors in `renders/bake/*.log`).
  - **Facts found:** `raw/hsc_2070.mp4` is a 320x180 BLACK stub with real audio (offset 2070.0 s); the podcast picture is
    `raw/hsc_dan.mp4` (2183.0-2223.0 of the E: file, 59.94 fps, kept as is). No hard cuts inside any used span (`win/scan_cuts.py`).
    His mapped framing for every clip: `proof/framing_abw11_mapped.jpg` (`win/framing_proof.py`).
  - **Decisions (mine, all changeable):** DVD interview = AW band [428,1488] with a blurred 198 % twin (his "fill with blur");
    the 400 % dailies and the 612 % reveal are full-bleed baked crops, no letterbox; Snape = FX-78 (`finish.py cine_vignette`),
    zoom hold on the three slots; zooms per README § 3 (one layer per shot change / same-camera run, depth held ≥ 0.80 on the
    soft sources); transitions purple 4.73 / green 14.93 / green 22.50 / purple 27.27 / purple 38.53, none inside the hook;
    CTAs 17.0 and 31.5; blue captions reserved for Gambon's line and Rickman's line (FX-58). Labels have NO poster thumbnail: no
    open HQ poster exists for either show (searched; Wikipedia has neither; the press art is licensed), so the plain AW lower
    third + a soft scrim (the mic ring ate "2007"); label 2 is three lines ("WITHOUT REALLY TRYING" / "BROADWAY 2011") and holds
    41.20-43.60.
  - **Captions come from the CLEAN A1** (`win/asr_dialogue.py`); hand fixes in `captions/fix_words.py` ("asked", "this whole TIME",
    4 fillers skipped).
- **12 Nov 2026, ~19:30: BUILD HANDED TO A SONNET SESSION.** Affan: "yes and fable as advisor", approving the build at
  ≈ 4-6 % of the week.
  - The session is "Build the Snape prank AW Short (v1)" (`local_055879e1-dcb0-482c-b70d-c2735918a866`, name
    snape-prank-build). It runs on `claude-sonnet-5-5`; its transcript `92eed71c….jsonl` shows advisorModel
    `claude-fable-5-2` (checked).
  - It builds v1 from BRIEF.md, Harry Diana's code build as the template, and keeps this ▶ STATUS current.
- **12 Nov 2026, ~18:45: SNAPE SHOTS SOURCED AND PICKED** (his downloads; YouTube still blocked since 15:28, so no
  request was made from here). The three picks and their source times are in `BRIEF.md` § Snape shots: PICKED; the
  proof is `proof/snape/full/picks_9x16.jpg`.
  - ~19:15: every frame of each span checked through its crop (`proof/snape/spans_all.jpg`). His ABW11 cut was re-read
    and is IDENTICAL to the 13:40 readback (`premiere/readback_abw11_1850.tsv`). The catalog pass is written into the
    BRIEF.
  - **Next: the build (BRIEF.md ▶ STATUS step 3), which waits for his OK on the corrected cost (≈ 4-6 % of the week,
    not 1-2 %).**
- **12 Nov 2026, ~13:50: TELLA 1 RESOLVED into `BRIEF.md`; that file is the resume point now.**
  - The base is HIS re-cut of v3 in ABW11 (43.93 s, `premiere/readback_abw11_tella1.tsv`).
  - Next is the Snape overlay sourcing. **YouTube is BLOCKED again**: "429/bot HP idea3 dl2 2026-11-12 13:24:01", set by
    another HP session. My search script saw the flag and made no request. Sourcing waits for the hub's clear, or for
    his own downloads.
- **12 Nov 2026, afternoon: v3 REBUILT IN ABW11.** ABW10 crashed before it was saved, and he moved to ABW11 ("do the
  sequencing inside of this new Premiere Pro project").
  - "Snape Prank - raw cut v3" is in ABW11's new bin "Snape Prank", with all three sources imported there.
  - Made by cloning HIS "Sequence 02" (1080x1920, v3/a4), because ABW11 has no empty template. The clone was emptied
    (26 clips removed; his Sequence 02 still has 26) and set to 30 fps, display 104.
  - Rows from `premiere/readback_v3.tsv` (`build_abw11.py` → `place_abw11.jsx`).
  - **Read back** (`readback_abw11.tsv`) **matches the ABW10 v3 readback on all 48 rows**: V1/A1 19 + 19, the V2 cover, 8
    markers.
  - His active sequence ("Sequence 03") was restored. **ABW11 NOT saved** (his Ctrl+S).
  - Everything below about ABW10 is history; ABW10's v1/v2/v3 were lost in the crash unless his auto-save kept them.
- **12 Nov: he asked what Dan's post-prank bit means ("what did Alan Rickman attend").** So a viewer won't get it either.
  - **DECIDED for the BUILD (Affan 12 Nov: "Yes, add a label", "but add it in the build not in the raw cut, im
    reviewiung it still"):** a low label on Dan's "come and see me in Equus" (HSC "Equus." 2202.18-2202.50, at about
    seq 39.35 in v3), e.g. "EQUUS (2007): his first big stage role, at 17". It goes in the label band at the BOTTOM
    (AW README § labels, memory `feedback-labels-at-bottom`). **The raw cut stays untouched while he reviews.**
  - "The musical" in Rickman's line is *How to Succeed in Business Without Really Trying* (Broadway, 2011).
  - Facts to keep exact:
    - Equus: London revival, Gielgud Theatre, Feb 2007; Broadway 2008.
    - Dan doesn't say which run Rickman saw, so the label doesn't either.
    - Rickman was on Broadway in *Seminar* from Nov 2011 ("he was down the road in one theater and I was up the road in
      another").
- **12 Nov 2026, ~02:20: RAW CUT v3 PLACED in ABW10. It's the one he approves.** "Snape Prank - raw cut v3" (bin
  "Snape Prank"): 48.57 s, 30 fps, V1/A1 19 clips, V2 1 cover, 8 markers.
  - His note on v2: "from 28 ish second onwards it doesn't even fit with the story alan rickman is talking about
    something else".
  - **He had tightened v2 himself** (21 clips, prank pauses cut, B6 at 28.333). v3 is a CLONE of his v2 (`clone_v3.js`),
    so 0-28.333 is his cut exactly (`readback_v3.tsv` rows 0-14 = `readback_v2_live.tsv`). Everything after it was
    replaced (`build_place_v3.py` → `place_v3.jsx`):
    - 28.33 B6, Dan (HSC 2190.63-2198.70 + 2199.23-2204.97, one 0.5 s pause cut): "Somewhere along the line, I think he
      saw that I really wanted to do this and I really wanted to work at it. And he cut short a vacation in Canada to
      come and see me in Equus. He saw every piece of stage work I ever did while he was alive."
    - V2 cover over 28.33-33.87: Rickman LISTENING (2015 clip 11.57-17.10, mouth closed, he speaks at 17.66), so
      "he" reads as Rickman, not Gambon.
    - 42.13 B7, Rickman 2015 (333.03-337.73): "Huge pride to go and see him in the musical".
    - 46.83 B8, Dan (2219.77-2221.50): "I'm so, so lucky."
  - Dropped: "this was their life… 12 to 22", "how dare he be dancing… worked at it", "Thanks for showing me that".
  - All edges sit in measured quiet. Crops: `proof/framing_v3.jpg`.
  - His active sequence ("Snape Prank - raw cut v2") was restored; v2 is left as he edited it. **ABW10 NOT saved**.
  - The Premiere lock was free (taken over at 01:35) and released after this window.
- **Next:** he approves v3 (or sends notes), then BRIEF.md and the build. The PITCH sequence table describes v1/v2; v3's
  back half is above.
- **12 Nov 2026, 01:35: RAW CUT v2 PLACED in ABW10** (superseded by v3 after his note). "Snape Prank - raw cut v2" (bin
  "Snape Prank", next to v1): 30.00 fps, 1080x1920, 0-55.70 s, 12 clips on V1 and A1, 7 markers.
  - The only change from v1 is beat 6 (R07-R09): Rickman comes from the full-frame 2015 original (`src/rickman/`), not
    the podcast oval.
  - **Read back** (`premiere/readback_v2.tsv`): spans as planned.
  - Rickman's actual source edges, checked against 20 ms loudness:
    - R07: 300.97-303.40, silent lead-in, ends in the dip after "22";
    - R08: 333.03-337.73, ends in the gap before "Funny";
    - R09: 342.97-349.70, starts in the quiet before "how" and ends at the end of "it.". Horowitz's "I" starts at about
      349.71, so up to about 10 ms of him may be audible. If he hears it, use the podcast audio for R09's tail.
  - The source is 23.976 fps on a 30 fps timeline: fine for a raw cut, but check the motion cadence at the build.
  - His active sequence ("Sequence 52") was restored. **ABW10 NOT saved** (his Ctrl+S).
  - **Premiere lock:** "heretics v3 FIX shift…" had held it since 11 Nov 08:11 (that job idle since 08:34). Taken over
    with Affan's OK ("Yes, take it over"): renamed to
    `.locks/premiere.lock.stale-heretics-0811-taken-over-20261112-0135`, owner note appended. Released after this
    window.
- **Next:** he approves the raw cut (or sends Tella notes), then BRIEF.md and the build.
- **11 Nov 2026, 02:08 (Premiere window 02:08:06-02:08:52, readback 02:09): RAW SEQUENCE PLACED in ABW10** as "Snape Prank - raw cut" (bin "Snape Prank"), 30.00 fps,
  1080x1920, 0-55.60 s.
  - It's a clone of his empty "Onyx reaction template (empty)", with both sources imported into the bin.
  - V1/A1: 12 clips each, butt-joined. 7 beat markers.
  - **Read back** (`premiere/readback.tsv`):
    - every clip's sequence span equals the plan;
    - Premiere floored each in-point one more frame (33 ms) earlier, and every edge still lands between words
      (checked against `transcript/words.json`);
    - scale and position as planned (HSC 177.78 %, DVD 400 %).
  - His active sequence was restored afterwards ("Brotherly Love reaction"). **ABW10 NOT saved**: it needs his Ctrl+S to
    keep the sequence.
- He reviews it and sends a Tella video. Next step: resolve his Tella notes into BRIEF.md (memory
  `feedback-walkthrough-videos`), then the build.
- **11 Nov, 06:52-06:58: the G4 freshness search ran** (the hub cleared YouTube at 06:48). Six requests via `lock.sh`,
  ≥60 s apart, no bot page.
  - **Our stitch was not found by title.** Recall is low: Horowitz's known 1.17M "hates me" Short didn't come up either.
  - The prank alone: 12.5M (ShenronAlt, 2012, 16:9), 2.8M (Tyler Morgan, his download), 858K (chelsea, format not
    checked).
  - Results: `meta/fresh.txt`, `fresh2.txt`, `fresh3.txt`; the row is in `PITCH.md`.
  - **Option for his review, not downloaded:** tgXZefAYRnQ (Josh Horowitz Clips, 276K, 6:16) is titled "Alan Rickman
    reflecting on playing Snape… and his pride in the young actors". It's likely the full-frame original of the clip
    that R07-R09 show only as an oval inset, so it would give a cleaner picture for beat 6 and a date for the clip.
    It needs one more spaced YouTube call.

- **11 Nov, 21:09-21:20: v2 PREPARED (placed 12 Nov 01:35, see the top).** He asked: "download the remaining bits if needed and give me
  the raw sequence asap so i can approve it".
  - **Downloaded** tgXZefAYRnQ, the full-frame 2015 Rickman original (Josh Horowitz Clips): 1080p H.264, 23.976 fps,
    594 kbps. Readable copy: `src/rickman/Alan Rickman on Snape and his pride in the young actors (2015).mp4`.
  - **Transcribed** word-aligned in `_rk/transcript/words.json`. Same words as v1 R07-R09, edges set from 20 ms
    loudness:
    - R07: 301.00-303.43;
    - R08: 333.07-337.77;
    - R09: 343.00-349.73. Tight: Horowitz talks straight after "worked at it" in the original.
  - Crops: `proof/framing_v2.jpg`. Rickman fills the frame and there's no oval.
  - **Ready to run:**
    - `premiere/build_place_v2.py` → `place_v2.jsx` and `plan_v2.json` (55.7 s);
    - `run_window_v2.py` (creates "Snape Prank - raw cut v2", places it, restores his active sequence, never saves);
    - then `pp.py readback_v2.js`.
  - **Blocked by the shared `premiere.lock`:**
    - It has been held since 08:11 by "heretics v3 FIX shift…", and that job hasn't written since 08:34.
    - My takeover (rename) was refused by the permission classifier, so it waits on Affan or the hub.

## Sources (his downloads, `E:\Bullshit Folder\Henry\`)
- `Daniel Radcliffe, Jonathan Groff, _ Lindsay Mendez talk MERRILY WE ROLL ALONG I Happy Sad Confused.mp4`: 1080p, 59.94 fps.
- `Prank on Harry Potter.mp4`: Warner's *Azkaban* DVD featurette, 854x480, 25 fps, 4:3 pillarbox. The dailies file is
  named `hp3_61_11_joke`.
- The Fallon file (`Alan Rickman Takes Jimmy to Task…`) is the helium segment, NOT the prank, so it isn't used.

## The cut (`premiere/plan.json`; words = WhisperX word-aligned `transcript/words.json`)
| Row | Seq | Source | Words |
|---|---|---|---|
| R01 B1 HOOK | 0.00-4.73 | HSC 2184.03 | "I was so intimidated by him for the first three movies… this guy hates me." |
| R02-R03 B2 | 4.73-12.77 | DVD 2.07 / 6.97 | "Michael Gambon and Alan Rickman, … took the opportunity to play a practical joke on me." (Rickman laughing on set, then young Dan) |
| R04 B3 | 12.77-18.80 | DVD 22.67 | "and Dan has asked to have his sleeping bag next to this particular girl that he fancied." |
| R05 B4 | 18.80-23.20 | DVD 35.97 | Gambon in the take: "In our dreams, we enter completely our own world." (raw dailies) |
| R06 B5 | 23.20-32.73 | DVD 51.03 | "They had put a fart machine into my sleeping bag… Michael Gambon had actually been pressing it during the take, I found out." |
| R07-R09 B6 | 32.73-46.50 | HSC 2114.77 / 2146.87 / 2157.63 | Rickman: "this was their life… from 12 to 22", "Huge pride to go and see him in the musical", "how dare he be dancing as well as the New York dancers because he worked at it." (Dan above, Rickman's oval below) |
| R10-R12 B7 | 46.50-55.60 | HSC 2166.77 / 2199.27 / 2219.80 | "Thanks for showing me that. I've never seen that before." / "He cut short a vacation in Canada… every piece of stage work I ever did while he was alive." / "I'm so, so lucky." |

**Flags for him:**
1. 55.6 s raw. Under the 60 s cap for Shorts with claimed content (a claimed Short over 60 s is blocked).
2. R10 is the source's wide stage shot (1.7 s), so Dan is small there.
3. The DVD footage is SD, cropped at 400 %. A zoom-out with blurred fill is the alternative.
4. Warner's "Raw Camera Dailies" label is partly visible bottom-right on R05/R06.
5. R01 is moved up from after the clip; his words are intact.
6. Minors: young cast in the DVD featurette, under his exception (BTS is my default reading).

Crops: `proof/crop_sheet.jpg`. Quality: `proof/anchor_fair.jpg`. Gate statement: `PITCH.md`.
