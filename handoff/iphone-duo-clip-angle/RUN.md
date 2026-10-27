# RUN — iphone-duo-clip-angle (AffanWiz CA-009 · ABW10 · "CA-009 iPhone Duo Clip Angles")

## ▶ STATUS: resume here (2026-10-27) — DRAFT COMPLETE on ABW10 › "CA-009 iPhone Duo Clip Angles", at his review (step 7)
Steps 1–6 + music DONE, every gate green (read back by name, 2026-10-27 ~13:30):
- **Cut** 138 segs, 7:25.8 (`transcript/cuts.json`); A1 = EDL clip for clip; dead-air gate PASS.
- **Lip sync** `work/sync_audit.py`: 206 V1 pieces, 0 out of sync (V1 re-laid from the video-only subclip, zoom edges pre-split).
- **Face** 51 cut zooms + 1 stretch gag ("Stupid.", recentred x 0.19), `work/face_pass.py --verify` 0 mismatches.
- **Voice** +4 dB (measured) → −6 dBFS on 138/138 A1 (`work/audio_chain_check.py`).
- **Reading** (rule 2) `review/tools/reading_gate.py`: 15 reading segments, 0 s visible.
- **Graphics** 24 full-frame (V2 plate + V3 alpha) + 11 side (6 CTA cards, struck title, 3-steps ×3) + the g22 CTA chip; 59/59 rows;
  graphics-qa 0 FAIL / 187 waived by design; gate-frames 0; edit-review 3 rounds (`hf-graphics/review/ROUNDS.md`).
- **SFX** 84 cues on A2/A3 from the fresh `sfx/` library (54 files, ≤ 3 uses, ≥ 60 s apart), `place-sfx.py --verify` 84/84, 0 extra.
- **Music** A4: 53 pieces, 6 sections, out under all 49 zoom ranges, `work/place_music.py --verify` 0 problems.
- **CTA** (rule 4) about once a minute: 0:59 · 2:00 · 3:11 · 3:51 · 4:44 · 5:40 · 6:31 (chip in g22) · 7:12 plug card (to 7:22) · 7:22 last card.
**SAVED** ABW10 2026-10-27 13:29:27 (lock free; Onyx Editor + GTA 24 sessions cleared it). NOTE: the open ABW10 is the file at
`E:\Premiere Pro Exports\Adobe Premiere Pro Auto-Save\(×6)\ABW10.prproj` (an Auto-Save path; every session saves there). Proof:
`outputs/CA-009-proof-frames.jpg`. He exports himself. NEXT: his review → LESSONS from his notes.

| | | |
|---|---|---|
| format | long-form YouTube | probed: 1920x1080, 60000/1001 fps, 664.66 s (11:05), PCM stereo 48 k (the camera audio IS the voice; no separate Enhance-Speech file handed over) |
| lane | Premiere (ABW10, shared) | `.setup-complete` lane=premiere; NEW bin + NEW sequence "CA-009 iPhone Duo Clip Angles" |
| preset | `presets/youtube/affanwiz/` STYLE.md v2 (IGN-missions) + PLAYBOOK (CA-007 standing rules) + LESSONS | |
| number | **CA-009** (START-HERE guessed CA-008; in `creator-shorts/` CA-008 = Zack D. Films, CA-009 = "Speed Bought the iPhone Duo. 20 Clippers Got Nothing.") | script copied to `brief/CA-009-speed-clippers-SCRIPT.md` |
| lane gaps | step 4 grade: none by style (STYLE § 1); step 8: he exports himself | |
| constraints | fresh build: CA-007 TOOLS copied as patterns only (no comps, renders, plans, SFX, music or assets) | |
| started | 2026-10-27 | |

## Steps
| # | Step | Status | What it produced / why not |
|---|------|--------|----------------------------|
| 1 | Intake | done | `raw/C1410.MP4` (byte copy of `X:\Recordings\Onyx\C1410.MP4`, original untouched) |
| 2 | Rough cut | done | 138 segs, 7:25.8; reviewers A+B applied; dead-air PASS; replayed 138/138, sync 0 off |
| 3 | Audio polish | done | +4 dB (measured) → −6 dBFS on 138/138 A1, read back by name |
| 4 | Color grade | skip | STYLE § 1: no grade (the lit room is the look) |
| 5 | Graphics | done | 24 full-frame + 11 side, 59/59 rows placed; graphics-qa 0 FAIL; edit-review 3 rounds (11 + 4 + 1 fixed, `hf-graphics/review/ROUNDS.md`) |
| 6 | SFX | done | 84/84 cues A2/A3, fresh Epidemic library (69 takes), verified |
| — | Music | done | A4: 53 pieces (after the ctaF change), 6 sections (Loungin −20 · First Born −24 · Take a Ride −25 from 10.304 · Brooklyn −24 · Grizzy −25 NEW (−34.8 LUFS, matched to his beds) · Loungin −23), 0.45 s turns, OUT under all 49 zoom ranges (built in, `work/place_music.py --apply-cut`), verify 0 problems; beds downloaded fresh to `music/beds/` |
| 7 | Review | waiting | the creator |
| 8 | Export | skip | he exports himself (never exportAsMediaDirect on ABW10; nothing on C:) |

## Request coverage (START-HERE.md, 2026-10-27)
- Premiere, raw → review-ready sequence, the CA-007 way with its review fixes built in → ABW10, new bin + sequence.
- Keep his improvised bits; cut only retakes, stumbles, dead air → build-cuts KEEP comments.
- Catalog pass before the edit, ≥ 5 % better than CA-007 → `BRIEF.md` § Catalog pass / § Better than CA-007.
- (1) Lip sync: audit after ANY V1 write (`work/sync_audit.py`), never `.end =`, DF timecode for QE razors.
- (2) Never show him reading: measure pitch AND yaw (sunglasses), every reading span under a FULL-FRAME graphic.
- (3) SFX premium + varied: fresh wide Epidemic set (16 classes, THIN, ≤ 3 uses, ≥ 60 s apart, FALLBACK, no chopped tails),
  audible on a phone (high-passed hits + one sub layer), each sound sized to its motion.
- (4) Community CTA about once a minute (side card top-left, his words only: $1 / a call with him / 3 modules / a free audit /
  Jan 31), a full CTA card over his plug, a chip inside a full-frame comp where a minute has no face window.
- On-screen numbers = his words; FLAG "$20 a month" (Claude Pro, not Max). Capture the real Shorts he quotes, fresh.
- Blur the small clip channels' usernames (script fact flag); the 212K "Speed leaks his number" video was a long-form upload.
- First ~10 s shows the clip-search grid (1.2K / 953 / 18), not his face (the locked engine prediction's failure risk).
- Finish: every gate green, ONE save cleared with the other ABW10 sessions, a short report with proof frames.

## Shared Premiere (ABW10)
Busy sessions at start: Afterhours Editor [98d1d7], Onyx Editor [2ff1db]. Active sequence at start: "Joe Appointment - raw cut".
By-name writes; QE work only inside `lanes/premiere/ACTIVE-WINDOW.lock`; one file per importFiles; message them before every
save and lock; restore the active sequence after each window; never touch their bins/sequences or "CA-007 Streamer Tier List".

## Flags to report (on screen = his words; these go to him, never silently fixed — sources `assets/SOURCES.md`, 27 Oct)
- Number is CA-009, not CA-008 (see table).
- "23 Shorts, 20 under 5,000": today there are ~100 clip Shorts of the Duo stream, 80 under 5K (same ~87 % ratio, bigger count).
  Nothing sits at 953 today (990 / 827 nearest); "1,200" and "18" have real lookalikes. On screen: his numbers, as what he saw.
- The 212K video (Speedy Boykins, "iShowSpeed LEAKS His Phone Number…") is a 61 s HORIZONTAL long-form upload, not a Short, and is
  now 330K. 12 of the 100 clip Shorts did use the phone-number moment and they were the best performers (47 % of all views).
- The take never says what the 212K video did differently (the cold open's "what did that one do" loop is not paid off in words);
  the graphic shows its real title at "212,000 views" so the viewer sees the different moment.
- "Crops, flips, speeding it up, filters, captions that type out what people say": YouTube's own words are "minor technical edits or
  template-based changes" + (Rene Ritchie) "not just VO descriptions of what's happening on screen"; flips / speed-ups appear in no
  official source. Shown as his list; the card's credit quotes YouTube's real wording.
- "January 31st, the requirements are getting doubled": doubled for NEW YPP entrants (8,000 h or 20M Shorts views) from Feb 1, 2027;
  Jan 31 is the deadline to accept the new terms; existing members not impacted.
- Claude "$20 a month": true for Pro billed monthly ($17 on annual); Max shows "From $100" (no $200 price on the page now).
- Skool today: 236 members, $1/month (matches the CTA).
- YouTube flagged this machine's IP during capture (CAPTCHA, 429s): expect a bot check on YouTube/Studio for a while.
- Footage of Speed is 360p (YouTube gave no 720p without a token): used only as blurred plates or small insets.

## Skipped, and why
- Step 4 grade: STYLE § 1 (no grade on this channel).
- Step 8 export: he exports himself.
