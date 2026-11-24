# LAUNCH MODE: GTA 6 hour drops (Afterhours, from 19 Nov 2026)

## ▶ STATUS: resume here (2026-11-18, 05:45 PKT)

**19 Nov, launch day: he started his 1-hour recordings (his words verbatim in `X:\Claude Projects\GTA 6\FEEDBACK.md`, 19 Nov).**
- **SUPERSEDED the same day (~2.5 h into play, his call, FEEDBACK 19 Nov): his play recordings feed CAMPAIGN FUNNY MOMENTS only.**
  - Each hour feeds a funny-moments long-form sequence in Premiere (`FUNNY-MOMENTS-STYLE.md`) plus viral funny Shorts.
  - His footage is also banked as overlays for other videos.
  - The What If series, guides (money, etc.) and GTA 5 vs 6 comparisons (graphics, animals, police…) are RESEARCH-LED faceless voice-over videos, like Video A, made from streamer footage. Their slate is a separate research session.
  - The afterhours-ideas hour mining no longer drives the What If series.
- *(Earlier the same morning, now replaced:)* **Each hour feeds up to three Premiere sequences** (his call; it replaces § 6's code-built long-forms):
  - **Funny campaign moments.** The RAW lane, no OK step. Cut in his old Urdu funny-gaming style, being measured into `FUNNY-MOMENTS-STYLE.md`.
  - **The What If episode the hour serves.** The DIRECTED lane: bits go into its sequence each hour; the story order goes to him for an OK before the finished cut (his sequencing rule).
  - **Any other idea that works.** Banked by `afterhours-ideas` first.
- **Drop folder:** `X:\Recordings\Afterhours\GTA6-launch\H01\`, created 19 Nov.
- **No rehearsal ran**, so hour 1 is the first real PS5 footage through the tools.
- **Disk:** X: had 292 GB free at the start.
- **His clap method (19 Nov, replaces the mute step):**
  - He plugs a pair of mic earphones into the controller and claps twice (the PS recording hears it through that mic, the camera through the DJI).
  - Then he swaps to his Sennheisers (no mic) to play.
  - Risk: with no headset mic, the DualSense's built-in mic may take over and put his voice into the game track. He was asked to press the controller's mute once after the swap.
  - Check on hour 1 whether his voice is in the PS file.
  - With no end clap, drift is assumed 0 (about 2 frames an hour). A camera restart mid-hour needs another clap.

**Status (18 Nov, about 08:00 PKT):** **built and tested end to end on SYNTHETIC input; not yet on real PS5 footage.**

**Added 18 Nov ~18:30 PKT: the IGN review test list.** The IGN-AMA video was shelved (his call). Its reviewer claims are now a
first-session test list at `X:\Claude Projects\GTA 6\launch-ideas\IGN-REVIEW-TEST-LIST.md`.
- He says "IGN check, <the thing>" before testing a claim.
- The scan flags it as **S12**: the window runs forward from the words, which never enter a clip. Unit test:
  `_selftest/unit_ign_check.py` PASS.
- The ideas skill ticks the list each hour (`afterhours-ideas` step 1).

**The tools** live in `projects/gta6-launch/tools/` (`README.md` runs them all):
- `hour_desk.py`
- `clap_sync.py`
- `moment_scan.py` + `scan_config.json`
- `build_short.py` + `styles/kai.json` (the default; `stack.json` and `bubble.json` as alternatives)
- `qa_short.py`

**Measured on the synthetic tests:**
- **Clap sync:** offset to within 1 ms, including on 4K VP9 + Opus WebM.
- **WhisperX large-v3** on his real voice: **10.9 s per audio minute**, so about 10 min for an hour (GPU memory peaked at
  7.6 of 8.2 GB, so nothing else on the GPU while it runs).
- **4K VP9:** decodes at about 5.4x real time.
- **A 20–30 s Short:** builds in about 20–30 s.
- **The Premiere mezzanine:** an hour takes about 49 min at 4K or 22 min at 1440p, on demand only.
- **The QA gate** caught every planted defect: stray frames, caption mismatches, spoiler words, uncensored swears.

The proofs are in `projects/gta6-launch/_selftest/proof/`.

**Builder findings:**
- **Opus-in-WebM `-ss 0` bug:** ffmpeg decodes the PS5 audio 20 ms early when given an explicit `-ss 0`. The tools avoid it.
- **End and restart claps under loud game audio are the weak link**, so the ritual now says pause or open a menu, then
  clap twice.
- **No end clap** means 0 ppm assumed drift, about 2 frames off per hour.
- **His camera framing** puts the face top at y ~190–215 in the Kai crop, under the 200 px UI band. Ask for a little
  more headroom.
- **Camera files** must be fed in recording order.
- **Intake copies,** so each hour costs its size twice on disk.
- **Censoring mutes words:** ambiguous words like "weed" and "drugs" mute ordinary talk too, so tune the list after
  hour 1.
- **Premiere and VP9 WebM:** unverified. The mezzanine covers it.

**How he records (answered 18 Nov):** "ps5 own recording but the tv speaker strat cant work ill have earbuds on".
- The camera can't hear the game, so the files are lined up with **the clap** (§ 3): the PS5 records his mic just long
  enough to catch one clap, then he mutes it.
- His other three decisions (§ 5) are unanswered, so the defaults stand. Don't re-ask them.

**Two lanes (his ruling, 18 Nov; verbatim in `X:\Claude Projects\GTA 6\FEEDBACK.md`):**
- **RAW** (Shorts and long-forms cut from his play): fully automated, with **zero creative direction from him** and **no
  OK step**. The system applies his whole rule set (`RAW-CLIPS.md`). An automated QA gate (`qa_short.py`) and a fresh
  Sonnet reviewer replace his review: a failure goes to `HOLD/`, never to `READY/`.
- **DIRECTED** (the What If series, his systems-vs-GTA-5 video): made after each play session, with his direction and the
  full max-effort gate. The ledger collects their material from every hour.
- **Posting stays his.**

**The look (18 Nov):** copy Kai Cenat's official Shorts. Low effort, output over polish. Being measured into
`X:\Claude Projects\GTA 6\research\streamer-clips-2026-11-18\COPY-SHEET-kai-cenat-shorts.md`. What a viral streamer
clip has goes in `ANATOMY.md` there, and that tunes the moment scan.

**His unlock: 09:00 PKT, Thu 19 Nov** (his word, 18 Nov).
- **Who is ahead of him** (MATHS from PlayStation's rolling midnight): New Zealand (16:00 PKT on the 18th), Asia, and
  the UK and Europe (from 05:00 PKT).
- **Who unlocks with or after him:** the US East coast at about 10:00 PKT, and the US West coast at 13:00.
- **What that means:** "first look" clips will already exist when he starts. His edge is his own reactions, plus speed.

**Open, his to answer:**
- **Does his camera run a full hour?** The largest file on disk is ~23 min at 50 Mbps. If it stops, the mid-hour
  restart is: start the camera again, then unmute, clap, mute again. The tools pair every camera file with its own clap.

**Idea mining every hour (his ask, 18 Nov):** the `afterhours-ideas` skill (`.claude/skills/afterhours-ideas/SKILL.md`).
- It mines each hour for What If episodes and brand-new ideas, and banks them in
  `X:\Claude Projects\GTA 6\launch-ideas\IDEAS.md`.
- At the end of each play session, the max-effort gate runs on the best of them before they are pitched.

**His PS5 records 4K WebM (18 Nov).** At 4K the PS5 won't save MP4, only at 1080p.
- **Keep 4K: it is better for Shorts** (MATHS). A 9:16 crop of 4K is ~1215 px wide, scaled down to 1080 so it stays
  sharp. A 1080p capture gives a 608 px crop stretched 1.8x.
- The code path reads WebM directly: this ffmpeg has `vp9_cuvid` (GPU decode) and `opus`.
- Premiere 25.0's WebM support is not checked here, so anything going to Premiere gets an automatic MP4 mezzanine
  (HEVC on the GPU).
- The GB per hour at 4K is measured on the rehearsal.

**The eye test (proposed to him):** on the rehearsal and on hour 1, he notes his own clip-worthy moments privately.
The scan picks blind, and the two lists are compared: what was caught, what was missed, and what was picked that he
wouldn't. The misses tune the scan.

**YouTube bot-blocked this PC at 06:10 on 18 Nov** (`projects/_onyx-batch2-2026-10/.locks/youtube.BLOCKED`).
- The block came from the streamer-clips research: the second block today, and about the 13th since 24 Oct.
- **The risk:** the launch-day watcher runs on this machine's yt-dlp (its pre-flight is one manual `python watcher.py`),
  so a block still up at launch blinds its searches. The API key part is unaffected.
- **Rule until launch:** no YouTube downloads from any session. A hub runs one spaced probe a few hours later and clears
  the flag only if the probe answers normally (lock.sh's rule).

**Before the first hour lands:** suggest he compacts this session. The resume block here is current, and every advisor
call re-reads the whole context.

**Waiting on:** the rehearsal recording, through the exact launch chain (§ 3).

**Next action:** when the rehearsal file lands, run § 2 end to end on it:
- time every stage;
- build one Short in both looks;
- cut a 2–3 minute long-form test;
- write the measured numbers into § 4.

**His unlock:** midnight PKT, Thu 19 Nov. That is PlayStation's rolling midnight; his GTA VI tile's countdown settles it. New Zealand unlocks first, at 4 PM PKT on the 18th.

**What already exists, and must not be rebuilt:**
- The launch calendar: growth plan § 7d.
- The Shorts research: `SHORTS.md` § 8, § 10.
- The finds watcher (off until his go on launch day).
- All of these live in `X:\Claude Projects\GTA 6\`, the content engine. Its session is "Research: why Afterhours views fell + launch plan" (`local_2d4a2596-…`).

## 1. His ask (18 Nov, voice-dictated, the gist in his words)

- "It's literally officially 24 hours till the release date… just wanted to make sure that everything is officially in place."
- **A long-form:** a video "completely covering all the fundamental changes… the police system, the crime system, the stealing system, the shop system… the NPC system… the animal system", each compared to GTA 5.
- **"Anything can go viral"** because the game is so big: "me reacting to the loading screen".
- **The system he wants:**
  - He records one hour, with commentary ("I'm not going to silently play it"), and hands it over.
  - The editor scans the whole hour, identifies viral long-form and Short ideas, and starts editing the long-form.
  - At the same time, other sessions "make the shorts from that exact one hour" while he keeps playing.
  - "Full on blast mode": Shorts for YouTube and Instagram, "more efficient than these big streamers".
- **On streaming:** "I don't mind streaming… I will only stream for you… I won't stream it publicly". He assumed a stream can't be grabbed, which is why he chose hourly recordings.

## 2. The loop: one hour of play becomes content

| # | Stage | Who | What |
|---|---|---|---|
| 0 | Play | him | **The clap ritual (start of every hour), done in this order:**<br>1. Start the camera.<br>2. Start a new PS5 recording.<br>3. Say the hour number.<br>4. **Pause the game or open a menu** (the clap must beat the game's sound), then **clap twice**.<br>5. Press the controller's mute button (it glows orange).<br>6. Play.<br>**End of the hour:** pause, unmute, clap twice, then stop both recordings.<br>**If the camera stopped mid-hour:** restart it, then pause, unmute, clap twice, mute again.<br>Camera files are handed over in recording order.<br>Commentary on, always. **Say "clip that" right after anything good** (the cheapest lever: the scan starts from those markers). No story spoilers needed from him; the scan filters them |
| 1 | Drop | him | The hour's files go to `X:\Recordings\Afterhours\GTA6-launch\H01\` (H02, …). He messages the hub "H1 in" (from his phone through Remote Control is fine) |
| 2 | Hour desk | script, run by the hub or one Sonnet xhigh sub-session | Intake into `projects/gta6-launch/H01/raw/` (copy, never move) → probe → sync face and game **off the claps** (the start clap gives the offset, the end clap the clock drift; a missed end clap falls back to the drift measured on the rehearsal. `workflows/sync-dual-audio.py` can't do this alone: after the mute, the two files share no sound) → one 1080p scan proxy with the face in a corner → **transcribe his voice ONCE** (WhisperX large-v3, `gpu.lock`, never two large-v3 at once) → moment scan (his "clip that" markers, voice loudness peaks, laughs and shouts, transcript hits, game-audio spikes) → `candidates.json` plus a contact sheet per candidate |
| 2b | Visual sweep | one Sonnet helper | Covers the moments with no reaction and no noise (a glitch, a weird NPC, a detail he didn't comment on), which signals can't hear. It reads contact sheets of the whole hour (a frame every 2–5 s) and flags anything odd as an extra candidate |
| 3 | Picks | the hub (Opus + Fable advisor) | Every candidate scored against the bar. The output is a numbered list: **Shorts** (the moment, the title, "the viewer gets: ___"), **long-form beats** logged into `projects/gta6-launch/SYSTEMS-LEDGER.md` by system (police/wanted, crime, car theft, shops/robbery, NPCs, animals, money, map, details), and skips. It goes to him under the gate he picks (§ 5) |
| 4 | Shorts build | one Sonnet xhigh sub-session per hour batch | It is handed the words and cut ranges: no re-transcribe, and no large-v3 of its own. Each Short lands in `X:\Claude Projects\Exports\GTA6-launch\READY\` as `<name>.mp4`, with a `<name>.txt` beside it (YouTube title, Instagram caption, hashtags, pinned comment) |
| 5 | Long-forms | content engine, then an edit sub-session | Built from the ledger once a system has enough first-hand tests. The engine writes the sequence and runs the max-effort gate; then an edit sub-session builds it (the answer on how is in § 6) |
| 6 | Disk | the hour desk | Once an hour is processed and its Shorts are built, its raws move off X: (§ 4, disk) |

**Sub-sessions** all run Sonnet 5.5 at xhigh (from 15 Nov). spawn_task takes no model, so set it after the spawn: `set_session_model claude-sonnet-5-5` and `set_session_effort xhigh`.

## 3. The rehearsal (before unlock, 18 Nov)

**What to record:** 5–10 minutes of GTA 5 (or any PS5 game if GTA 5 has gone), recorded exactly the launch way.
- Commentary on, and say "clip that" once or twice.
- Doing it on GTA 5 also banks GTA 5 footage for the side-by-sides (N2, and his systems-vs-GTA-5 idea).

**What it measures:**
- Codec and container: does Premiere read it?
- HDR or SDR, and fps.
- Whether his voice is in it, and whether it is separate from the game audio.
- **GB per hour**, against the disk (§ 4).
- The sync: does the camera hear enough of the game to line the two files up?
- One full pass timed: drop → transcript → picks → first Short.

**What comes back from it:**
- one Short in both looks;
- a 2–3 minute long-form test cut (the growth plan's 14 Nov test edit, which never ran);
- the pick sheet.

**PS5 settings to check before recording.** These are from memory, not verified on his console, so confirm each one in the menu:
- Captures → video clip format **MP4**;
- the highest resolution the disk allows;
- clip length **1 hour**;
- the recent-gameplay buffer as long as it goes (the safety net if he forgets to restart a recording);
- **"include mic audio" ON**, but only so the PS5 file hears the clap. He mutes the mic right after the clap, so the
  rest of the hour is game sound only. His real voice comes from the camera and DJI.
  - **Test 1:** that the mute button really silences the capture.
  - **Test 2:** which mic the PS5 uses with his earbuds plugged in (the earbuds' own mic or the controller's). Either
    one works for the clap.
- **HDR off while capturing** (an HDR capture looks washed out on the PC);
- streamer mode on, or the radio off (already in the plan).

**With a capture card instead**, also check **HDCP off** (Settings → System → HDMI).

## 4. Capacity (estimates until the rehearsal measures them)

**Disk** (MEASURED for the camera; the PS5 rate is unknown):
- His camera records 1080p60 H.264 at 50 Mbps plus PCM audio, about **23 GB per hour** for the face alone (C1447 and C1453 probed). The PS5 capture is on top of that.
- X: has 358 GB free and E: has 176 GB.
- At an estimated 35–55 GB per hour, X: holds about **7–10 hours of play**. The plan's 60–80 hours do not fit.
- **Options (his call):**
  - a lower camera bitrate (the face is small in every layout);
  - move each processed hour to another drive;
  - an external drive.

**GPU:** one RTX 3060 Ti (8 GB), with 6.2 GB already in use on 18 Nov at 05:30.
- Transcription runs one at a time, under `gpu.lock`.
- Launch Shorts are time-sensitive, so they take the lock first (`memory/feedback-news-shorts-gpu-priority.md`). Ask the holder to pause; never kill it.

**Usage** (read 18 Nov):
- **42 % of the week is used, 58 % left for every channel**, until the reset at Mon 23 Nov 07:00 PKT.
- Measured costs (`memory/reference-usage-costs.md`): a GTA long-form costs **5–13 %**, and a lean code-built Short 1.5–2 %. An hour batch of Shorts and the per-hour scan are not measured yet.
- **The estimate** (unmeasured until the rehearsal's own costs replace it): with all 58 % on GTA, about 3 long-forms, about 15 Shorts and about 10 hours scanned by Monday. With half of it, about 1–2 long-forms and about 8 Shorts.

**Turnaround per hour:** not measured. The estimate is 45–90 minutes from the drop to the first Shorts. The rehearsal sets the promise.

## 5. Decisions (asked 18 Nov), and the defaults taken until he answers

| Decision | Default until he answers | Why it is his |
|---|---|---|
| **How he records** | **ANSWERED 18 Nov:** PS5's own recording plus the Sony camera, with earbuds on, so the files are synced by the clap ritual (§ 2, stage 0) | His hardware |
| **The gate on launch Shorts** | **ANSWERED 18 Nov:** the raw lane has no OK step. Automated QA plus a fresh reviewer stand in for his review. The directed lane keeps the full max-effort gate | His ruling |
| **The look** | **ANSWERED 18 Nov:** copy Kai Cenat's official Shorts (the copy sheet is being measured) | His ruling |
| **Who posts** | He posts from the READY folder | He said "you start to upload". This session has no upload path, and Chrome is read-only on his accounts by his own standing rule |
| **Usage priority this week** | GTA gets priority from unlock to Monday, the other hubs go lean | It is shared with AW, Scott, Onyx, Urdu and AffanWiz |
| **Story spoilers** | No story cutscenes or plot reveals in Shorts. The open world, systems, reactions and the loading screen are all in | His watcher rule keeps story out (FEEDBACK 14 Nov) |
| **Reaction Shorts** | **In**, from his ask on 18 Nov (the loading-screen reaction). This reverses the watcher's "no reaction" line for his own first-play Shorts only. The HANDOFF ban on reaction long-forms stands | Recorded as his direction |
| **The repeat check** | The working line from `SHORTS.md` § 8: a first-hand test is not a repeat if it shows the game doing it and adds something | Open since 14 Nov |

## 6. Long-forms: the editing side's answer to growth plan § 7d point 4

The content plan asked the editing side three options: a template, a code build, or overflow help. **Answer (the default, his to overrule):**
- **Launch-week gameplay long-forms are code-built** from the hour clip bank:
  - a rough cut on his commentary;
  - the game full frame with his face as PiP (`CREATOR-HAND.md` § 3, his own screen + PiP format);
  - few cards.
- That keeps them parallel to everything else and off his Premiere project, which edits one timeline at a time.
- It is delivered as a finished file in Exports, **plus a Premiere project he can open, tweak and export himself**.
- **The risk:** a code-built long-form is new on this channel. The rehearsal's 2–3 minute test cut is the proof before launch.

**His systems-vs-GTA-5 idea** is logged, not pitched:
- The ledger collects every system test from every hour, so it can be built either as his one big all-systems video or as the "What Happens…" series (his 10 Nov direction: one system per episode, § 7d).
- The two compete for the same first-hand material: an all-systems video first takes the freshest hook of each episode.
- Which shape ships, and when, goes through the max-effort gate with real footage.

## 7. The odds, logged (don't edit; `SHORTS.md` § 10, 14 Nov)

For launch-week gameplay Shorts, taken as a set of ten or more in the first seven days:
- the median is most likely 3–15K;
- the chance at least one passes 100K is about 40 %, and that one passes 500K about 10 %.

The biggest risk: **"they go up late, or in the old look"**. Speed is the lever this system pulls.
