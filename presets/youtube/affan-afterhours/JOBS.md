# JOBS — the Affan Afterhours job log

Every Afterhours job since video 22, where it lives and where it stands. Each job's own `RUN.md` "▶ STATUS" block is
the source of truth; this file only points at it. Older videos, and how each one performed: `ERAS.md`.
Lessons from these jobs live in `LESSONS.md` (Shorts and channel-wide) and `../affan-afterhours-facecam/LESSONS.md`
(long-form face-cam).

## ▶ STATUS: resume here (2026-11-14)

The **Afterhours Editor** session is the dispatcher for this channel. Affan sends it a recording path, and it opens a
fresh session for each video (§ How a new video starts). Nothing is running from the dispatcher itself.

**The content engine** (research, topics, scripts, packaging, predictions) is a separate workstream in
`X:\Claude Projects\GTA 6\`. Its instructions are that folder's `CLAUDE.md`; its live session is "Research: why
Afterhours views fell + launch plan". Scripts for the edit come from there, and so do the reach diagnosis and the launch
calendar (`research/growth-plan-2026-11-10.md`).

**Every job in the log below is up on his channel** (titles, dates and views read on 10 Nov from his public pages:
`X:\Claude Projects\GTA 6\research\growth-2026-11-10\uploads-table.md`). The Head Start's match is by length, not
confirmed by him. Posted lengths don't always equal our builds (They All Fit Inside, video 27), so he edits after
handoff. No notes came back on AI Ports or They All Fit Inside, so their open questions are closed. Their editing
sessions (videos 24, 26 and 27, and the three Shorts) were archived on 14 Nov at his OK; their state is in each job's
`RUN.md`.

**Still open on the editing side:**
- **Phase D for long-forms 23, 24, 26 and 27:** none of their RUN.md files records a shipped-timeline diff (EDITOR.md
  § 4). Run it against his ABW10 sequences and write his KEEP/NEVER verdicts into facecam LESSONS, where each
  video's new treatments are listed as pending. Video 27 is 9:14 on his channel against our 9:32 sequence; phase D
  will show what changed.
- **Launch week is a new long-form format.** The content plan is a "What Happens…" series, one game system per
  episode, built from his own PS5 gameplay capture with his face as a picture-in-picture. It starts 19–20 Nov and runs
  at five a week to 9 Dec (growth plan § 7d; `research/what-happens-series-2026-11-10.md`). The plan asks for a
  2–3 minute test edit (capture + face PiP) before 19 Nov, because the first episode runs on a 24-hour clock. No
  preset for this format exists yet.
- **Rule settled 14 Nov:** the max-effort gate wins for Afterhours too: research, the sequence as text, his OK, then
  the build (step 4 below).
- **Disk you could free** (regenerable build files, offered by the job sessions, not done): `gta6-head-start` has a
  7.7 GB Topaz base and about 750 MB in `yt/work`; `gta6-all-fit-inside` has about 13 GB. Finals, raws, base cuts and
  build scripts stay either way, but a re-render would need Topaz again.

## The log

| # | Title (working) | Job (`projects/…`) | Raw | Where | State · posted as (views on 10 Nov) |
|---|---|---|---|---|---|
| 22 | You Can't Just Play The Missions In GTA 6 | `gta6-ign-missions` | C1339 | ABW8 › Sequence 39 | **posted** 9 Oct 02:27 PKT as "GTA 6 Just Got A Whole Lot More Interesting..." (8:16 · 1,792) |
| 23 | The Day The World Stops For GTA 6 | `gta6-world-stops` | C1388 | ABW10 › "GTA 23 - The Day The World Stops" | **posted** 24 Oct as "No Game Has Ever Had This Much AURA" (7:42 · 1,533) |
| 24 | 14 Mistakes You'll Make On Day 1 Of GTA 6 | `gta6-day1-mistakes` | `Onyx\C1409` | ABW10 › "GTA 24 - 14 Mistakes On Day 1" | **posted** 27 Oct, same title (8:59 · 3,767) |
| 26 | Why GTA 6 Will Feel MUCH Bigger Than It Is | `gta6-feels-bigger` | C1425 + `script.md` | ABW10 › "GTA 26 - Feels Bigger Than It Is" | **posted** 3 Nov as "Why GTA 6 Map Will Feel MUCH Bigger Than It Is" (8:56 · 124) |
| 27 | GTA 6 Complete Guide: Do These Before November 19th | `gta6-complete-guide` | C1447 | ABW10 › "GTA 27 - Complete Guide" (9:32) | **posted** 6 Nov, same title (9:14 · 105) |
| S | They All Fit Inside | `gta6-all-fit-inside` | C1445 | code build → `Exports/` | **posted** 5 Nov as "How Many GTAs Can Fit In GTA 6?" (58 s · 4,059). Our v4 is 62.2 s, so he trimmed or re-cut it; no notes came back |
| S | The Head Start (video 27's Short) | `gta6-head-start` | C1448 | `Exports/afterhours-gta6-head-start.final.mp4` | **approved, no notes** 2026-11-06; posted 6 Nov as "17 Things To Do Before GTA 6" (52 s · 3,239), very likely ours (our final is 52.35 s) |
| S | AI Ports | `gta6-ai-pc-port` | C1453 | `Exports/afterhours-gta6-ai-pc-port.final.mp4` (30.33 s) | **posted** 10 Nov 22:05 PKT as "GTA 6 PC Won't Take A Year!!" (per the GTA 6 growth plan); assumed to be our v1 (speck removed at source), posted length not checked; no notes |

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
   - **the max-effort gate** (`MAX-EFFORT-GATE.md`, his ruling 14 Nov): research every beat, send the sequence as text
     opening with the max-effort statement, wait for his OK, and only then build. After the OK (our reading, which
     both rules agree on, not his words), smaller open questions don't stop the build: take the stated defaults and
     list them in the delivery note. A file he never mentioned stays out of the build and gets one line in that note;
   - his standing constraints: silence, nothing on C:, he exports on Premiere, no Fable agents (pass the sub-session
     `model` per `memory/feedback-use-fable-allowance.md`), usage per `memory/feedback-usage-budget.md`, and
     Higgsfield only with his OK.
5. **A separate "short version" take of a long-form is its own Short job** (C1448 for C1447). Tell the long-form
   session so it doesn't ask him about it.
6. **Log the new job in the table above.**
