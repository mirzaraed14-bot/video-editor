# JOBS — the Affan Afterhours job log

Every Afterhours job since video 22, where it lives and where it stands. Each job's own `RUN.md` "▶ STATUS" block is
the source of truth; this file only points at it. Older videos, and how each one performed: `ERAS.md`.
Lessons from these jobs live in `LESSONS.md` (Shorts and channel-wide) and `../affan-afterhours-facecam/LESSONS.md`
(long-form face-cam).

## ▶ STATUS: resume here (2026-11-10)

The **Afterhours Editor** session is the dispatcher for this channel. Affan sends it a recording path, and it opens a
fresh session for each video (§ How a new video starts). Nothing is running from the dispatcher itself.

**Waiting on him:**
- **`gta6-ai-pc-port` (C1453, Short):** v1 delivered 2026-11-10 03:07. Three things wait on him: his review, his OK
  on the speck removal, and his answer on C1454. The evidence already answers that last one: C1454 is AffanWiz
  Short 4 (`projects/stop-remaking-viral-shorts`), not part of this Short.
- **`gta6-all-fit-inside` (C1445, Short):** v4 delivered 2026-11-04 23:49. No later notes or music answer are on file.
- **Long-forms 23, 24, 26 and 27:** each was left at his review (step 7), with planned uploads on 2026-10-24,
  10-27, 11-04 and 11-06. None of their RUN.md files records a shipped-timeline diff (phase D, EDITOR.md § 4). Once
  they're up, run it and write his KEEP/NEVER verdicts into facecam LESSONS, where each video's new treatments are
  listed as pending.

## The log

| # | Title | Job (`projects/…`) | Raw | Where | State (last on file) |
|---|---|---|---|---|---|
| 22 | You Can't Just Play The Missions In GTA 6 | `gta6-ign-missions` | C1339 | ABW8 › Sequence 39 | **shipped** 2026-10-22 (he exported) |
| 23 | The Day The World Stops For GTA 6 | `gta6-world-stops` | C1388 | ABW10 › "GTA 23 - The Day The World Stops" | review 1 applied + saved 2026-10-23 10:32 |
| 24 | 14 Mistakes You'll Make On Day 1 Of GTA 6 | `gta6-day1-mistakes` | `Onyx\C1409` | ABW10 › "GTA 24 - 14 Mistakes On Day 1" | full draft saved 2026-10-27 13:39, at his review |
| 26 | Why GTA 6 Will Feel MUCH Bigger Than It Is | `gta6-feels-bigger` | C1425 + `script.md` | ABW10 › "GTA 26 - Feels Bigger Than It Is" | review 1 closed 2026-11-03 19:51 |
| 27 | GTA 6 Complete Guide: Do These Before November 10th | `gta6-complete-guide` | C1447 | ABW10 › "GTA 27 - Complete Guide" (9:32) | saved 2026-11-06 03:31, at his review |
| S | They All Fit Inside | `gta6-all-fit-inside` | C1445 | code build → `Exports/` | v4 delivered 2026-11-04 |
| S | The Head Start (video 27's Short) | `gta6-head-start` | C1448 | `Exports/afterhours-gta6-head-start.final.mp4` | **approved, no notes** 2026-11-06 |
| S | AI Ports | `gta6-ai-pc-port` | C1453 | `Exports/afterhours-gta6-ai-pc-port.final.mp4` (30.33 s) | v1 delivered 2026-11-10, speck removed at source |

There is no row 25: `X:\Claude Projects\GTA 6\` numbers video 24 as "video 25", and this log uses the channel's numbering.

Recordings in `X:\Recordings\Afterhours\` that turned out to be OTHER channels (folder ≠ channel): C1427 = AffanWiz
CA-010, C1449 = AffanWiz CA-011 (`kai-tiktok-money`), C1450 = AffanWiz Short 3 (`what-level-shorts-creator`),
C1454 = AffanWiz Short 4 (`stop-remaking-viral-shorts`). And one Afterhours recording landed in the Onyx folder:
C1409 = video 24.

## How a new video starts (the dispatcher's checklist)

1. **Probe the file:** dimensions, fps and duration. Check its neighbours recorded the same minute, and grep
   `projects/*/RUN.md` / `BRIEF.md` for the camera number in case another session already took it.
2. **Settle the channel from the content, never from the folder** (see the list above).
3. **Find the last video of its kind**, the bar this one must beat by 1 % (CLAUDE.md § learning loop, item 5):
   - Short → the newest approved Afterhours Short (today: `gta6-head-start`).
   - Long-form → the newest long-form (today: `gta6-complete-guide`).
4. **Spawn one fresh session per video.** Write a self-contained brief covering:
   - the raw path and its probe;
   - his words verbatim;
   - the files to read (EDITOR.md first);
   - the bar to beat;
   - the stated default for every open question: the session builds v1 on those defaults and delivers it, with the
     questions in the delivery note, never as a gate (`memory/feedback-build-dont-block-on-questions.md`). A file he
     never mentioned stays out of the build and gets one line in that note;
   - his standing constraints: silence, nothing on C:, he exports on Premiere, no Fable agents, lean usage, and
     Higgsfield only with his OK.
5. **A separate "short version" take of a long-form is its own Short job** (C1448 for C1447). Tell the long-form
   session so it doesn't ask him about it.
6. **Log the new job in the table above.**
