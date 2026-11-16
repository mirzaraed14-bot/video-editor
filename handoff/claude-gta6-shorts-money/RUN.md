# RUN: claude-gta6-shorts-money (AffanWiz CA-015 "Claude + GTA 6 Shorts Monetization (Not Selling You Any AI Software Lol)")

## ▶ STATUS: resume here (2026-11-16 ~17:20 PKT): RESUMED for the full edit (his "why wasn't the gta 6 video finished", via the dispatcher). Week at 8 %.
- **The disk and ABW11 disagree on purpose:** `transcript/cuts.json` is now **290 segments / 758.141 s** (batch 2: his CA-011 hand, the stray
  "And" / "so" / "So" and a 0.1 s stray burst cut; old EDL kept as `transcript/cuts.v1-placed-0932.json`). ABW11's CA-015 sequence still holds
  the **294-segment** placement, UNSAVED (ABW11 last saved 04:21). Before any graphic goes on: re-replay V1/A1 from `cuts.json`, the audio chain,
  `sync_audit`, a fresh XML. `work/save_once.py` now reads the expected count from `cuts.json`.
- **ABW11 SAVED by him at 17:42:01** ("its saved now start"). Placement part 1 started ~17:50 (Sonnet, `work/PLACEMENT-BRIEF.md` steps 1-4: rebuild V1/A1 290 + razors, audio chain, 77 zooms, head-steady; idle-gated). Part 2 (graphics + SFX) waits for the renders.
- (was) **Gate on the timeline:** nothing is placed until ABW11 shows a save after 09:32 (his Ctrl+S, or "save it" said in this session). Until then
  everything is offline: plan, comps, renders, QA.
- `transcript/reading.json` regenerated on the 290-segment clock (12 runs, 13.1 s). Spelling for on-screen copy: `corrections.local.json`.
- Music: **skipped, his** (channel rule; the dispatcher's brief). Not in the next steps.
- **Done offline (17:10-18:00):** graphics plan `build-plan.py` → `graphics-plan.json`: 48 full-frame + 18 side beats (14 CTA side cards + 2 full
  CTAs, max gap 59 s), face 59 %, 3.5 graphic runs/min, longest face-less run 19.7 s, reading 0.00 s visible, the re-sit joint under g26.
  Stolen move = THE PREP BOARD (FX-64, Jon Bois's grid canvas; BRIEF rewritten against the take). Barred lines (the research session's checks)
  stay on his face. Cut zooms: `work/face_plan.py` → `transcript/face-zooms.json` (77 zooms, median 130 %, hold 1.30 s, 1 extreme 250 % on
  "shut the fuck up", 1 stretch on "shilling", 200 % on "big ass balls"; 150 razors to pre-split V1).
- **18:20 (week 9 %):** graphics BUILT: 66/66 alpha renders, exact frame counts, fonts checked, graphics-qa 0 FAIL (286 waived: standing side-card /
  filter / grain / stepfps, g14-g15 white page with the type measured inside the band, exits on face-pass razors only; no full-frame band waiver).
  48 plates, 72 fresh Epidemic SFX takes (plan: 117 cues over 66 files). Proof `outputs/CA-015-proof-frames.jpg`, radar line appended.
  Editor fixes during the build: g11 rail order, g17 bars, g38 → card. Edit-review round 1 running (2 Sonnet: copy+rules, visual+timing).
  Placement part 1 armed but WAITING: he has been watching CA-015 (his active sequence) since ~17:55; it runs when he moves off it + idle 150 s.
- (17:50) **Running:** two Sonnet builders (`hf-graphics/BUILD-BRIEF.md`): A = 66 overlay comps + alpha renders + graphics-qa; B = 48 plates + a fresh
  Epidemic SFX set (`sfx/`). Next: edit-review round, then placement on ABW11 once it is saved.


## (history) STATUS (2026-11-16 ~10:00 PKT): STAGE A DONE, STOPPED at the overnight cap (week at 7 %). Rough cut on ABW11, unsaved; graphics not started

### Morning summary for Affan
- **Done:** CA-015 rough cut, **12:39.2**, is in ABW11 › bin "CA-015 Claude GTA 6 Shorts Money" › sequence of the same name
  (id 03f889a7-7a02-4628-ac2e-a7df9d7bef2f). V1/A1 294 clips each, exact to the EDL, sync audit 0. Audio chain on all 294 A1 clips: +4.3 dB
  into a −6 dBFS limiter, read back. Your active sequence and playhead weren't touched.
- **Unsaved, needs your Ctrl+S.** One Ctrl+S also keeps the AW Dad + Sirius work in ABW11. Your "Tell it it can save if it needs to"
  reached this session through the hub at ~09:45, and the save script was ready (`work/save_once.py`: one save under both locks, refuses
  unless ABW11 + V1/A1 294/294, proves the mtime, checks the path after). But this session's permission check blocked the save, because
  the OK came from another session and not from you here. Say "save it" in this session to run it, or press Ctrl+S yourself. Crash
  insurance until then: `work/CA-015-roughcut.xml` (an FCP XML of the CA-015 sequence only, File › Import).
- **You didn't record the v3 script.** C1484 + C1485 are one improvised talk (a launch-week preparation guide under your title), split by
  the camera at ~4 GB. So the cut follows your take: `review/CUT-PLAN.md`, built without your OK per your overnight rule.
- **Not done, and why:** graphics (STYLE v2 plates + overlays, CTAs, SFX, music, the face pass) are NOT started. The overnight usage cap
  (10 % of the week across all sessions; at 7 %, start nothing new) put the rough cut first. The week reached 7 % at ~10:00 PKT, so I stopped.
  Also done: **your CA-011 review diff**, read offline from the saved ABW10 (`review/ca011-review-diff.md`, lessons appended to LESSONS.md). Next step: the CA-011 review diff, then the
  graphics plan and build (BRIEF.md's stolen move must be re-picked against the take, because the take never says the lines it was built on).
- **Listen first:** the cut was re-heard by ASR, never by a person. Possible stutters at raw ~783.9 "it, it has a great editing style",
  ~322.8–330 "but I, I want to build", ~1107 "the people are, who are going", ~304–306 "clip all, the, the game". Also "99 % of you guys are
  going to be doing faces" (raw ~1128): you mean faceless, and it's kept as said.

### Next steps, in order (a fresh session can resume from here)
1. **His:** Ctrl+S in ABW11, or "save it" in this session (`work/save_once.py`). Listen to the "listen first" spots above.
2. **Optional cut pass from his CA-011 hand** (LESSONS § 2026-11-16): he deletes a sentence-start "But / So / And" right after a hard joint
   that follows a completed sentence, and a ≤ 0.2 s stray burst between a pause and a restart. Run that check over `review/cut-map.tsv` before
   graphics (a V1/A1 re-replay is cheap now and costly after graphics).
3. **Graphics (step 5):** the catalog look at the 137 reference stills, then **re-pick the stolen move and the "better than CA-011" list
   against the TAKE**: BRIEF.md's were written before the transcript and rest on lines he never said. Then `graphics-plan` → build (STYLE v2
   plates + overlays) with the look-away runs covered first, the re-sit edge at "if you guys just want the video editor client" (cut ~7:50)
   under a full-frame graphic, CTAs about once a minute (his offer is in the take at ~6:50 and ~12:00), and every first beat ≥ 0.5 s after a
   "listen first" joint (CA-011 lesson).
4. **Face pass:** cut zooms (STYLE § 2) + the head-steady lock; zoom pieces ≥ 0.5 s; one framing over the closing line (CA-011 lesson).
5. SFX (a fresh premium set), music beds (cold open −10.5, body −20…−25), all gates, a Fable advisor call, the delivery note.

### Decisions made without you
- **The cut:** your order kept; retakes, stumbles and dead air out; every improvised bit kept (the rant, the Loch Ness acting, "screw you
  guys, I'm going to hide it", "big ass balls"). Swearing not bleeped ("shut the fuck up" lands at ~1:45, after the first 7 s). Two
  fresh-eyes Sonnet reviews (12 flow + 17 mechanical findings) all applied (`review/build-report.md`).
- **Two date words cut:** "right now it's 16th of November", "this time, November 16" (wrong on a 17–18 Nov post: your time-words rule).
- **ABW11, not ABW10:** ABW10 isn't open. Opening it would switch the project under the AW session working in ABW11.
- **One working raw:** `raw/CA015-joined.mov` = C1484 + C1485 stream-copied, bit-identical to C1485 at +496.496 s (audio and picture).
- **No render:** you export yourself.
- **The research session's take notes** (`creator-shorts\CA-015-AS-RECORDED-2026-11-16.md` + PDF, sent to you): 14 checks on what you said,
  each yours to decide, with no on-screen card for any until you pick. The four that matter most: (1) the compile-streamers advice vs YouTube's
  reused-content / Shorts rules; (2) "monetized in 90 days or less, or money back" with no condition; (3) "$20 plan… Fable as advisor" (Fable
  on Pro is paid with usage credits); (4) "not selling you AI software" vs the offer's "AI content engine". The finds watcher's searches and
  channel lists stay off screen.

### State details
- Cut: `transcript/cuts.json` (294 segments), dead-air PASS, leak sweep 0. Plan: `transcript/keep-plan.md`; rows in `transcript/*-rows.txt`.
- Audio: kept speech −21.3 LUFS → +4.3 dB. (`workflows/voice-gain.py` measured `raw/C1484.MP4`, the first file in `raw/`, not the joined
  raw, so the number was taken on `review/cut-audio.wav`.)
- Looking away: 13 short runs, 13.7 s (`transcript/reading.json`, `review/reading-sheet.jpg`), thinking glances to his left, not reading.
  Overlays go there first (his standing rule).
- Premiere kit: `work/ca015_window.py`, `premiere_seq.py`, `audio_chain.py`, `sync_audit.py`; read-back `work/premiere-readback.md`.

| | | |
|---|---|---|
| channel | **AffanWiz**, CA-015 | settled by the dispatcher from the folder + the script's timing; transcript confirmation pending |
| format | long-form YouTube 16:9 | both takes 1920x1080 h264 60000/1001, pcm_s16be 48k stereo, streams start 0.000 |
| raw | `raw/C1484.MP4` (496.50 s) + `raw/C1485.MP4` (699.20 s) | byte copies (`cmp` identical) of `X:\Recordings\PBE\` |
| script | `brief/CA-015-gta6-money-SCRIPT.md` (v3, his title) + `-RESEARCH.md` + PDF; `brief/CA-015-gta6-money-SCRIPT-v2-rockstar-first.md` | copied 07:01 |
| lane | Premiere 2025, live **ABW11.prproj** (shared) | new bin + sequence "CA-015 …"; by-name writes inside `premiere.lock`, idle-gated; he exports himself |
| preset | `presets/youtube/affanwiz/` STYLE.md v2 + PLAYBOOK standing rules 1–4 | |
| bar to beat | CA-011 `projects/kai-tiktok-money/` | its review diff can't be read tonight: ABW10 isn't open |
| constraints | no gameplay, no key art (the script's edit rule) · no earnings figures of any kind · Afterhours may be named · keep improvised bits · last take wins · work in silence · Opus main, Fable advisor, Sonnet builders · overnight usage cap 10 % of the week (all sessions) · no C-drive files · nothing waits on him overnight | |
| started | 2026-11-16 07:00 PKT | |

## Steps
| # | Step | Status | What it produced / why not |
|---|------|--------|----------------------------|
| 1 | Intake | done | `raw/C1484.MP4`, `raw/C1485.MP4`, `brief/` |
| 2 | Rough cut | done | 12:39.2, 294 segs, dead-air PASS, 2 Sonnet reviewers applied (29 items), placed 294/294 on ABW11, sync 0 |
| 3 | Audio polish | done | +4.3 dB into −6 dBFS on 294/294 A1 clips, read back |
| 4 | Color grade | skip | STYLE § 1: no grade on this channel |
| 5 | Graphics | pending | not started: the overnight usage cap went to the cut first |
| 6 | SFX | pending | |
| — | Music | pending | his beds on this channel |
| 7 | Review | his | |
| 8 | Export | his | he exports himself |
