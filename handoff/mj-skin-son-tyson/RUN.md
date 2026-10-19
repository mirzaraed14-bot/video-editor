# RUN — mj-skin-son-tyson (Abundance Wisdom Short: "Michael Jackson's Son Told Mike Tyson The TRUTH About His Skin 💔")

## ▶ STATUS: resume here
**2026-10-15 00:4x: REDONE after the restart.** The 10-14 export never produced a file (Premiere restarted, AE closed unsaved;
ABW9.aep last saved 18:46, before the edits). Reopened ABW9 had the dirty `mj2.mp4` and no letterbox → re-ran
`captions/capcut/mj2_replace.jsx` (#1985 → `mj2_clean.mp4`, MATCH) and `letterbox/letterbox79.jsx` (same build: L34 mask
522..1441, twin L35 242 % @ 47 %, lines L29/L30; comp 48 layers). Affan exports himself; ABW9 NOT saved by us (he saves).
**2026-10-14 ~19:00: EXPORT STARTED (he asked: "start the export") — Sequence 53 (the only sequence holding Linked Comp 79, V4 0–36.433)**
via `export/export53.js` = `exportAsMediaDirect(entire, lanes/premiere/premiere-templates/vertical-1080x1920-60-h264-cbr24.epr)` →
`export/mj-son-tyson-skin.mp4` (temps `.m4v`/`.aac` while writing). SLOW: Dynamic Link renders comp 79 through the open AE at
~12 s/frame (≈1 MB of ~110 MB after 13 min, dialog 0 %) → estimate 6–8 h, Premiere behind the modal "Encoding Sequence 53" the
whole time. NOT cancelled; his call. ABW9 still UNSAVED (*): never close/restart AE during it (Dynamic Link would read the saved
file and drop the letterbox + caption re-point). When it lands: remux `-c copy` to `E:\Shorts\Abudance Wisdom Shorts Exports\Final
Renders\MJ Son Tyson Skin.mov` (never touch mj.mov), ffprobe (36.43 s, 1080×1920, 60, ≥20 Mbps), frames (letterbox ~11.5 s:
the twin is 47 % so Seq 53 V1–V3 shows under it, a caption, a transition peak, a mid-zoom), loudness vs −14 LUFS.
**2026-10-14: CLEAN CAPS on comp 79**: `mj2.mp4` (#1985, his CapCut return) → `mj2_clean.mp4` (464 of 2186 frames cleaned;
`captions/capcut/clean.log`); verify: caption pixels max change 4, lifted-black field 41–46 % → ≤0.4 % (`captions/capcut/verify_clean.txt`);
#1985 re-pointed in place (`captions/capcut/mj2_replace.jsx/.txt`: size/fps/duration MATCH, "mj2.mp4 Comp 1" layer unchanged 0.783–36.433).
**2026-10-14: FUCHSIA LETTERBOX on comp 79, L32 → now L34 (10.4–12.5, the gurney photo)**: band measured on his render 506..1443
(slides in from 533 over the first 0.3 s), full width → mask y 522..1441 (x −60..1140, feather 0), twin L35 242 % @ 47 %, his
glow lines L29/L30 (copies of comp 60's bar, y 522 / 1441) under the zooms, above his grade (`letterbox/plan79.json`,
`letterbox/letterbox79.txt`, proof `letterbox/letterbox79-proof.jpg`). The bottom line half-covers the exhibit's "SA073164".
Fresh dump `letterbox/after_all79.tsv`: 48 layers. ABW9 NOT saved.
**2026-10-14: TRANSITIONS on ABW8 Linked Comp 79** from his labels (`transitions/labels_comp79.tsv`): 13 = 6 Purple (−90) at 1.9 /
3.333 / 10.4 / 16.317 / 27.333 / 33.2, 3 Cyan blur at 12.5 / 14.333 / 22.367, 2 Dark Green (+30) at 7.45 / 19.317, 2 Peach
exposure at 25.133 / 30.45; last block (Aqua) ignored. Every value read back (`transitions/transitions79.txt`); comp now 41 layers
(transitions on top, then the zooms, then the footage; no caption layer yet). Undo "Abundance Wisdom transition pass (Claude)".
ABW9 NOT saved.
**2026-10-14: ZOOM PASS (BlurMoCurves) on ABW8 Linked Comp 79** (his Topaz render `mj_stab_chr2_iris3.mov` of Sequence 53,
36.43 s, 14 blocks; 4 yellow = pull out: 10.4–12.5, 14.33–16.32, 22.37–25.13, 25.13–27.33): 14 `Adjustment Layer 29` zooms,
6 face pivots, every Z read back as planned; fresh dump: zooms 1–14 on top (no caption layer yet), footage 15–28, one zoom per
block (`zoom/zoom.txt`, `zoom/after_comp79.tsv`, preview `zoom/zoom-preview.jpg`). Undo "Abundance Wisdom zoom pass (Claude)".
ABW9 NOT saved. Seen in his render (flagged, not touched): the 2005 courthouse photo at 1.9–3.3 (brief: no 2004–05
courthouse), the Getty/AFP gurney photo at 10.4–12.5 (watermark), Paris (a child) in the umbrella photo at 25.1–27.3.
**2026-10-14: CAPTION EXPORT for Sequence 53 (his recut, 36.43 s): `E:\Shorts\Abudance Wisdom Shorts Exports\Caption Exports\mj.mov`**
(H.264 1080×1920 60 fps + PCM voice, like ronnie.mov / cbum.mov) = the file for CapCut. 59 captions, max 3 words; interviewers
(Tyson, the co-host) italic; red = the brief's words; 5 stacked pairs (`captions/captions.txt`, "+"). Engine
`captions/render_caps.py` (the CBum one; line-1 cap top y1022). Sheet `captions/caps_sheet.jpg`. No transcript fixes needed.
**2026-10-14: HEAD LOCK on ABW8 Linked Comps 73–78** (his recut of Sequence 53 as AE comps, ABW9.aep): 12 layers (7 Hotboxin',
5 Oprah 4K), 1,392 Anchor keys + Motion Tile, undo "Head lock (Claude)"; proof from AE's read-back keys
`headlock/headlock_proof_*.jpg` (every LOCK row holds). Comp 76 L1/L2 (Prince in profile toward Tyson): YuNet failed (L1
locked onto the burned-in logo corner, L2 missed 48/66) → CSRT box tracks (`headlock/head_box_track.py`): L1 his head box,
L2 the cap's "Heal Los Angeles" logo; YuNet-only track kept in `headlock/track_yunet_only.json`. Big swing: comp 74 L4 (the
co-host, x −195..306 / y −215..334 comp px; Motion Tile mirror may show at the extremes). ABW9 NOT saved.
**2026-10-14: RAW CUT ON ABW8 · Sequence 53 (bin "MJ Skin Son Tyson"), 38.38 s — waiting on Affan's call.** ABW8 NOT saved.
Sequence 53 = a clone of his empty Sequence 48 (1080×1920, 60 fps), renamed; it became the active sequence.
- V1/A1 14 clips, butt-joined 0 → 38.38, all 7 beats. V2: Prince's next shot 12.18–12.50 (covers the podcast's cut to the
  co-host under "…report."), the Paris STAND-IN 22.37–27.98 (beat 5). A2 empty. 7 beat markers. Read back = plan
  (`premiere/readback.tsv`). In/out table `proof/inout_table.md`; crops `proof/crop_sheet.jpg`.
- Proven: timeline audio rebuilt from the read-back + re-transcribed (`proof/seq53_audio.wav`, `seq53_words.txt`) = the
  brief's words in order; Tyson stops dead on "white" (tested: "He was" starts at 432.81); no lupus; beat 6 from "I'm a
  black American", beat 7 from "But when people". Joins ≤ ~0.35 s quiet (beat 3 edges measured); one 0.58 s pause inside
  Michael's beat-7 sentence after "But" (his delivery, kept).
- Framing: Hotboxin' has a burned-in TYSONPRO.COM ad banner (y848+): scaled 226.5 %, Motion y 0.637 so the frame ends on it
  (`fix_placement.py`); its "HOTBOXIN' PODCAST" watermark still shows at the bottom. Beat 6 at 108 % of fill (tighter than 4).
**Flags for Affan:**
1. RUNTIME 38.4 s, not 50–55: the locked words run that long (every beat in, the host's whole question kept).
2. BEAT 5 PICTURE: "Michael Jackson in Public" (4QySPvhsMX0) has NO umbrella shot (Paris, mostly with children). Stand-in:
   0:58.5, him alone. Beat 5 audio kept. Needs real umbrella footage or the call to drop beat 5.
3. BEAT 1 PICTURE: the split-screen press photos (Off the Wall / early 2000s) were not supplied: Tyson's own shot for now.
4. "So this is officially not a rumor?" = the co-host in the black cap on his own camera (exact: "So I'm hearing from you,
   that is real. This is officially not a rumor."). Prince's answer has no "Yeah": "I think it was even on the autopsy
   report." (the co-host's "He had that." between them left out).
5. LEVEL: the podcast sits ~10 dB under the 1993 / home-movie audio (−27 vs −16 dBFS RMS): for the audio pass (no gain in a
   raw cut, lane rule).
6. Oprah lines are from his 4K excerpt (`Skin Michael/…Upscale(1).mp4` = the full interview +24:00.0): sharper than the 1080
   full file he listed.
7. The bin's first "Prince Jackson Opens Up…" file is a different interview (no Tyson): not used.

## Stills (Affan's photos, Higgsfield bytedance upscale, 6 credits net; failed 4K tries refunded)
`assets/stills/`: `mj_young_vitiligo_phone_4k.png` (3303×4096, vitiligo patches kept, pose/expression same),
`mj_2005_courthouse_white_suit_2k.png` (2160×3360; 4K failed twice) — **Santa Maria courthouse 2005: the brief forbids
2004–05 courthouse footage**, `mj_with_mother_katherine_2k.png` (2160×2528; 4K failed twice; not "him alone").
`mj_umbrella_stairs_alone_4k.png` (3276×4096) = THE beat-5 picture (alone, umbrella, aircraft stairs): to replace the Paris
stand-in on V2 22.37–27.98 on his yes. `mj_umbrella_with_paris_4k.png` (3002×4096): Paris (a child) in frame, usable only
cropped to Michael. 10 credits for all five.
Declined 2026-10-14: removing the Getty Images / AFP watermark from the People v. Murray gurney photo (Getty 128287429):
license it from Getty for a clean file, then a light retro-keeping cleanup. Not in the brief either.

## Sources
- prince (wrong episode, see above), oprah (full 1993, 1440×1080 50 fps), oprah4k, phm — `sources.json`, windows in `raw/`.
