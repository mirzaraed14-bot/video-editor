# RUN — streamer-content-machines (AffanWiz CA-007 · ABW10 · "CA-007 Streamer Tier List")

## ▶ STATUS: resume here (2026-10-23) — REVISION 1 BUILT, GATED, SAVED in ABW10 · awaiting his re-review (`review/REVISION-1.md`)
DONE on "CA-007 Streamer Tier List" (ABW10; backup `premiere-backup/ABW10-before-revision1-2026-10-23.prproj`):
- **His cut adopted**: he ripple-deleted "$40 per 100,000" and "CaseOh is also" himself → `work/edl_from_a1.py` made his A1 the EDL
  (`transcript/cuts.json`, 165 segs, 7:02.7; old = `cuts.v1-2026-10-22.json`), timeline words re-anchored.
- **Lip sync FIXED**: V1 rebuilt from his A1 with a video-only subclip (`work/rebuild_v1.py`); `work/sync_audit.py` **203/203 in sync**;
  at his 7 times (`work/sync_at_times.py 1:24 1:56 2:50 3:22 3:49 4:59 5:50`, ±3 s windows) every piece 0 frames;
  zooms re-applied (`work/face_pass.py --verify`: 0 mismatches).
- **Reading covered**: 36 full-frame + 13 side (`build-plan.py`; v1 = `build-plan.v1.py`); clips ≥ 60 % head-down visible: **0 s**;
  the 12 clips at 40–60 % checked by eye (`review/frames/mid-reading-sheet.jpg`, `mid-zoom.jpg` vs `ref-reading.jpg`): all camera-facing.
- **Graphics r1** placed 84/84 (V2 36 plates, V3 48 alphas), gate-frames 0 problems; proofs `review/frames/r1-proof.jpg`, `r1-cta-proof.jpg`.
- **CTA** about once a minute: side cards cta1 0:54 · cta2 2:16 · cta3 2:57 · cta4 5:12 · cta6 6:17, the 4:05 one is a chip INSIDE t25
  (r2; no face window from 3:00 to 5:00), cta5 (5:44, three CTAs in 70 s) retired; + ctaF full card over the plug ($1, free call,
  3 modules, before Jan 31 when the requirement doubles). All copy = his own words (Tella ask + the plug in the take).
- **SFX v2** (`sfx2/`, 77 fresh Epidemic takes, `sfx2/LIBRARY.md`): 110 cues (v1 157; THIN list in build-plan) over 69 files,
  max 3 uses, none twice within 60 s (class FALLBACK borrows a sibling take instead of repeating); 4 flagged takes EXCLUDED
  (counter-4, whoosh-deep-1 chopped loud; swarm-2 hiss; swell-impact-4 'Horror') → 67 files; `place-sfx.py --verify` 110/110.
  Measured, NOT auditioned (silence rule): first listens 0:54 (CTA sound), 2:35 (riser), 3:50 (chapter hit), 4:27 (swell), 6:06–6:15 (tier stamps).
- **Music** 38 pre-cut pieces, 0 problems. **Voice chain** A1 165/165 (+0 dB → −6 dBFS; `work/audio_chain_check.py`, by name).
SAVED 2026-10-23 (Afterhours cleared it). NEXT: his re-review; then LESSONS from his notes. He exports himself.
Open questions to him: keep the stray "views," (after his first cut) and "B tier." (after his second)? Face share now 34 %.

## Shared Premiere (ABW10) — another session works here
The Afterhours Editor session (GTA 23, raw C1388) owns bin "GTA 23 World Stops" + sequence "GTA 23 - The Day The World
Stops". Never touch them. Sequence 19 stays the active one between windows. By-name writes; QE work only inside
`lanes/premiere/ACTIVE-WINDOW.lock`; one file per importFiles; message them before every save.

| # | Step | Status | Notes |
|---|---|---|---|
| 1 | Intake | ✅ | `raw/C1389.MP4`, script in `brief/` |
| 2 | Rough cut | ✅ | 164 segs, 7:06.2; tight joints, every edge measured |
| 3 | Audio polish | ✅ | +0 dB (−16.8 LUFS) → −6 dBFS, 164/164 |
| 4 | Grade | ⏭ skipped | STYLE § 1: no grade (the lit room is the look) |
| 5 | Graphics | ✅ | r1: 36 full-frame + 12 side (5 CTA cards, tier boards, 2 side cards) + the t25 CTA chip; gate 0 problems |
| 6 | SFX | ✅ | r1: 110 cues over 69 sfx2 files, max 3 uses, ≥ 60 s apart (v1 157 cues judged cheap) |
| — | Music | ✅ | 8 beds on A4, out under all 40 zoom ranges |
| 7 | Review | — | the creator |
| 8 | Export | ⏭ | the creator exports himself |

## Request coverage
- "start this now on premiere" / "a new sequence and new bin" → ABW10, bin + sequence "CA-007 Streamer Tier List".
- "some improvised bits… don't cut them out" → kept (see build-cuts KEEP comments); only retakes/stumbles killed.
- "in the style you made the N3on streamer video in" → STYLE.md v2 (CA-003's tools as the pattern, nothing else copied).
- "with little improvements… 1 % better" → `BRIEF.md` § What this video does better.

## Flags for the creator (so far)
- "Instagram Reels, his YouTube links" before Druski's numbers = the script's screen note read aloud: cut.
- He says "Kai Sinat"/"Kaisernet" etc.: names are fixed in the transcript only (the audio is his).
- Kept on purpose (his improvisation): the plug restates "off the runway / $1" twice (optional trim: kill 1262–1278).
- "You can be his clipper": the take never recorded the script's "you shouldn't be the Buyer" line, so "his" is made clear by
  the clipper-math card (N3on's face + his $40 / 100K rate).
- Live numbers moved since filming: xQc TikTok 48 (he says 47), Adin IG 5.8M (6M), Speed's best Short 30M (28M); Ludwig /
  CaseOh / Kai Live first-row medians lower than the script. On screen = his words. N3on and Adin ARE in the CreatorDB census
  (the script says not; he doesn't say it on camera). Streams Charts (xQc 290 h) blocked capture: typed, "approx.".
- Slow-down candidates (0.8x, his device): "well, hold that thought", "like mine". Not scripted (a speed change ripples).
- Plates are other creators' footage at 360p, used only blurred (σ≈26, ×0.38): no readable text (sheet checked).
