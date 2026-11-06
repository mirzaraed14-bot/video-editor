# RUN — gta6-complete-guide ("GTA 6 Complete Guide: Do These Before November 10th", Affan Afterhours video 27)

## ▶ STATUS: resume here (2026-11-06 ~03:45 local): STEP 7, HIS REVIEW. Saved on ABW10 › "GTA 27 - Complete Guide" (bin "GTA 27 Complete Guide"), 9:32, at 03:31:37
Next action: he watches and calls notes, then exports himself. Nothing runs until he speaks. Before ANY re-place: diff the live timeline against the plan (`hf-graphics/place-seq27.py --verify`, `hf-graphics/place-sfx-seq27.py`, a live V1 read) and treat what he changed as decisions. A re-render is a NEW version (VER auto): re-place by --remove id then --apply, re-run review/gates27.py + review/gate-frames.py, one save.
On the timeline, read live and saved 03:31:37 (window title clean): V1 296 / A1 263 / V2 71 / V3 76 / A2+A3 88 SFX / A4 37 music pieces; all 76 cells are on their newest version. Gates after the last re-place: place 147/147, SFX 88/88 + 0 extra, gate-frames 0, frame0 0 bare, lip sync 0/296 off, dead-air 0 (review/dead-air.json), CTA head gap 50-99 px, reading on face 0.6 s (252.9-253.5, "notifications", yaw 0.31, an ad-lib), 51 zoom pieces framed with no uncovered edge (review/frames/zooms.jpg, review/zoomsheet.py).
UPLOADS TODAY, Fri 6 Nov 8–11pm Pakistan time, so the draft must reach him with time to review.
**His answers (2026-11-06 ~00:55):** upload Fri 6 Nov → CTAs read **13 DAYS** · **cut "fuck" only** (cut from the voice, nothing over it; "shit", "pussy", "god damn", "big-ass" stay audible) · **Sonnet subagents** for both gates · **no settings recordings exist → menu-path graphics** from the script, never a fake console screenshot.
Takes: C1447 ONLY, measured: C1449 = AffanWiz CA-011 Kai TikTok money (job `kai-tiktok-money`), C1450 = "four levels of Shorts creators" (job `what-level-shorts-creator`), C1448 = the separate Short. All have their own sessions.
Channel from the words: Affan Afterhours (GTA). Script `script.md` = byte copy of `X:\Claude Projects\GTA 6\video27-before-you-play-SCRIPT.md` v3.1: fact-check labels + Don't-say bind.
Cut chain: `transcript/build-cuts.py` → splice RENDER=0 → polish → `pauses.py` + beats.json → `fixes.py` → cuts.final.json (261 pieces, 572.3 s with two baked 0.8x beats) · slowdowns.py · seq27.py --replay (a dropped bridge: FROM=<V1 count>) · tl-words.py → timeline-words, tlmap, v1-cuts.
Plan chain: `build-plan.py --spans` → transcript/plates.py → build-plan.py (71 cells + 5 CTAs (cta2 dropped: no clear window), 88 SFX cues) · anchors in transcript/anchors.json · censor27.py (the word straddles a joint: two A1 spans).

| | | |
|---|---|---|
| format | long-form YouTube | probed: 1920x1080 |
| lane | Premiere 2025, the creator's LIVE `ABW10.prproj` (`E:\Premiere Pro Exports\Adobe Premiere Pro Auto-Save\…×6\ABW10.prproj`, per `projects/gta6-world-stops/RUN.md` and `projects/gta6-feels-bigger/RUN.md`) | NEW bin + NEW sequence; he exports himself, never exportAsMediaDirect |
| preset | `presets/youtube/affan-afterhours/EDITOR.md` → `presets/youtube/affan-afterhours-facecam/` (CREATOR-HAND, HUMOR, LESSONS) | latest pattern `projects/gta6-feels-bigger/` |
| lane gaps | none (steps 7 + 8 are the creator's) | LANES.md Premiere column |
| source | C1447.MP4, h264, 60000/1001 fps, 1181.68 s, pcm_s16be 48k stereo, all streams start 0.000 | copied, cmp on the first 100 MB OK, original untouched |
| constraints | shared Premiere: by-NAME writes, ACTIVE-WINDOW.lock for QE/active sequence, message sessions before saves, stable.py before writes. Lean mode: no subagents without his yes, builders Sonnet, never Fable. Silence: no audio played. No C-drive exports. Learn from earlier jobs, never copy comps/renders/plans/SFX wavs | |
| started | 2026-11-05 22:24 | |

## Steps
| # | Step | Status | What it produced / why not |
|---|------|--------|----------------------------|
| 1 | Intake | done | `raw/C1447.MP4`; `transcript/words.json` (large-v3, 2068 words, CPU int8: the GPU run stalled 1h46 with three large-v3 jobs on the 8 GB card and was stopped before writing anything) |
| 2 | Rough cut | done | 261 pieces, 572.3 s; per-burst retakes, pauses + comedic beats, verbatim guard + removed-check on GPU, one Sonnet fresh-eyes pass (review/fresh-eyes-content.md: 1 must-fix applied; a second agent skipped for usage), replayed + verified; dead-air gate 0 flags on the final EDL (review/dead-air.json) |
| 3 | Audio polish | done | +4 dB into -6 limiter on all A1, 3-frame crossfades, censor; gain measured outside the lock (review/voice-gain.json) |
| 4 | Color grade | skip | channel style: no grade (video 26) |
| 5 | Graphics | placed, NOT converged | 71 cells + 5 CTAs placed on V2/V3. edit-review: one full round (two Sonnet agents, `review/edit-review/round1-*.md`), every fix applied but one (`round2.md`), changed cells checked by eye; round 2 not run, for usage, so the definition of done (a clean full round) is unmet. A second round is available on his word. `workflows/graphics-qa.py` cannot run (it needs a placement.json this placer does not write): review/gate-frames.py + review/gates27.py + review/frame0.py stand in |
| 6 | SFX | done | 51 fresh screened Epidemic files (`sfx/PALETTE.md`, ids disjoint from all earlier GTA jobs), 88 cues, none > 2x, read back 88/88 + 0 extra after the last re-place |
| — | Music | done | Loungin / First Born / Brooklyn / Take a Ride / Loungin on A4, out under 35 visible zooms, 0 problems |
| 7 | Review | waiting on him | handed off 2026-11-06 ~03:45; uploads today 8-11pm Pakistan time |
| 8 | Export | — | his |

## Request coverage (his brief + the session brief)
- "1 % improved from the previous videos in the editing and overall style": keep the look; BRIEF.md says exactly what is better than video 26. Catalog pass first (CATALOG.md + every still).
- Keep improvised bits and jokes at his length; tighten mid-line hesitations only.
- Never show him reading; cover those spans; ask before new copy fills a span.
- SFX fresh + screened + varied + subtle. Graphics complete on frame 0, edges on a cut or butted.
- New sequence + new bin in ABW10. He exports.

### Reconciled against the SAVED sequence (03:31:37, read live, not from the plan)
- **1 %:** BRIEF.md § What video 27 does better, each item with its measured outcome. Look unchanged: same plates, type, accent, inset b-roll, cut zooms.
- **Jokes kept at his length:** `transcript/beats.json` pins his comedic beats; verbatim-guard + removed-check clean on the kept words. One ramble cut is flagged below.
- **Never reading:** review/gates27.txt, 0.6 s left on his face. Covering it cost face time on some spoken lines (flagged below). No span needed invented copy: covers are his own words or the script's rows, so no span question was raised beyond his "build graphics" answer. On-screen-only rows are flagged below.
- **SFX fresh, screened, varied, subtle:** A2+A3 88/88; sfx/PALETTE.md.
- **Complete on frame one, edges on a cut or butted:** frame0 0 bare, gate-frames 0, against a LIVE V1 read.
- **Censor "fuck" only:** two A1 pieces disabled, ~400.53-400.93 s, reversible; nothing over it.
- **13 DAYS:** cta1, 3, 4, 5, 6 on V3.
- **New bin + new sequence in ABW10, he exports:** never exported here; no exportAsMediaDirect, no AME.
- **Silence:** no audio played; ffmpeg to files or -f null only.

## Script vs what he actually said (words.json + no-VAD span ASR and energy over every gap ≥ 7 s: `work/cut/gap-check.txt`; those holes are real silence, ≤ 3 % above −40 dB)
- He never says "number four/fourteen/fifteen"; he says 16 and 17, so the counter still runs 1–17: 4/17 on the download math, 14/17 on the no-real-money line, 15/17 on "don't panic buy".
- Not said: 80 hours (14/17, the 16:28–16:46 hole is silence, so no 80-hours card and that Don't-say row is moot), the fair turn, speed test, Xbox Sleep line, kill cam/HUD line, X/TikTok muted-word steps. A card row says only what he says (video 24 lesson d12).
- Download math: he says only 100 Mbps and 10 Mbps.
- He ad-libbed: "first time Xbox has won", "big-ass USB drive", Twitter/reels spoiler rant, "considered a pussy" (2 takes, last wins), "What the fuck?" (14:13), "I will shoot that guy", "linked here or here, I don't know", the subscribe outro.
- Accuracy to carry on screen: USB = storage, copy back to play (he says "like instantly"); aim assist "almost nothing… way weaker" (self-corrected, use the last words); no real-money line needs "story mode" on the card; part 2 is preview-build ("I'll flag that as we go") so its cards carry a PREVIEW BUILD/REPORTED tag.
- Don't-say check on the words: no 99 %/top 1 %, no GTA+ price, no competitor name, no 60 fps, no rumour list. Clean so far.
- Mishears for `corrections.local.json`: Traders → Creators; wad → VOD; IG → IGN; "It says/calls" → Edge says/calls; court → code; field → feel; "by the ultimate" → buy; "order renews" → auto-renews.

## Countdown cards
Video 26: 6 "15 DAYS" lower-right (`cta1..6-alpha*.mov` on V3), all six still on his saved timeline after his own edit (`review/his-review-1/live-saved.json`, 3 Nov 19:51). Keep the format. The number depends on his upload date: 6 Nov = 13 DAYS, 7 Nov = 12 DAYS. He says "we're not even two weeks away" in the outro, which agrees with both.

## Flags for his review
- CUT by me: the "they WILL impound it" ramble (raw 829.9-837.3, confirmed: no piece of cuts.final.json overlaps it, the cut jumps 829.11 → 839.33): a stumble, and the fact row says "can".
- Beyond his words, there for the fact check: m01 "USB DRIVE = STORAGE ONLY" plus its path (the script's "you can't play them from it"), c14 credit "STORY MODE" (the no-real-money line needs it). m02's PS5 paths are the menus he says are on screen.
- Beyond his words, NO accuracy reason, one word removes each: m02 note "XBOX: AUTOMATIC UPDATES ON · POWER MODE: SLEEP" (never spoken); d05 labels his "for me, it's 5 a.m." as "Pakistan" (the time is spoken, the place is the script's).
- He never says number 4, 14 or 15, the counter still runs 1-17; 80 hours and the fair turn were not recorded.
- LEAD WITH THIS: coverage 71 % vs 57 % on video 26, the most visible change against a "1 %" brief, all from the reading cover. Under cards because yaw shows him reading: "God damn", "your VOD", "actual adult", "forget it".
- 5 countdown cards, not 6; a hand crosses the card 0.2 s on cta5 and cta6.
- The crime-video pointer needs his end card.
- Audio +4 dB against a measured +3.5 (audio-polish takes integers). He may run Enhance Speech on A1 himself.
- Head-steady: 24 of 50 joints fully locked, median ~2 px, big leans up to ~100 px remain. Inside some zooms scale steps ~4 % at a jump cut (126→130→134 at 5:11.8-5:12.4, 134→138 at 0:22) so his head keeps its size, which is the rule; the background steps instead, and that is what could show.
- s01 checklist holds 4.5 s: a screenshot frame, not a read.
- Reviews thinned for usage: one edit-review round, one rough-cut fresh-eyes agent (two is the norm).
- After 10 Nov the script's rename title applies.

## Flags
- No PS5/phone settings recordings on disk (X:\Recordings has only C1445/47/48/49/50). He says "the exact menus are on screen right now" (6:57), and the script expected him to film them. Default: rebuild the exact paths from the script as graphics (a menu path is text; never a fake console screenshot).
- C1448 = the separate Short (peer session, per him). `_c1448-intake` and `_c1449-intake` are other sessions' job folders.
- RAM ~0.4–5 GB free, GPU 8 GB full with other sessions: long jobs run on CPU or one at a time.

## Skipped, and why
- Grade: channel style.
