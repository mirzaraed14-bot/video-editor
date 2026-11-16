# Abundance Wisdom: the hub session

The hub is the one main session that runs Affan's AW Shorts. It starts the build sessions, relays their reports to him,
checks every delivery, and saves his rules. Build how-to lives elsewhere: start a build at [SESSION-START.md](SESSION-START.md),
the look in [README.md](README.md), lessons in [LESSONS.md](LESSONS.md). Ideas and locked briefs come from the Cowork engine
files in `X:\Claude Projects\Abundance Wisdom\` (ENGINE, RESULTS, the newest HANDOFF), or from the Instagram method
(`research/instagram-beat-mining/`).

## ▶ HOUSE STYLE (Affan 2026-11-12 ~19:45)
**The build template is `projects/mj-son-step-outside/` ("Jafaar") exactly as shipped**: its Topaz, head tracks, zoom,
transitions, captions, mix, and its grade (his AE look, `grade_mode 'ae'`). He said it is "really close to Bolt
Motivation" and wants "that aesthetic" continued. Every other ruling of his (captions, CTA, labels, censoring) stands.

Bolt vs ours, measured, with the parameters and file:line references: `research/bolt-style-2026-11-12/findings.md`. Bolt's
differences (hard cuts only, a slow linear push, 3-word captions, the Bolt grade) are HIS CALL and are not built by
default. **Adopted on 12 Nov: stacked two-panel splits on comparison beats and reaction cutaways (README § 13)**. They
are sequencing moves and never change a cut he has locked. La Toya's "verdict on the Bolt grade" stays open.

Near-done jobs are NOT rebuilt for it; the style applies from their next step. Told on 12 Nov:
- snape-prank-build (`local_055879e1…`, building now);
- the HP fork (`local_7f87fba7…`, Hagrid raw cut).
Jermaine is still unbuilt, so its build takes this style.

## ▶ 16 Nov 04:35 PKT (hub): OVERNIGHT RUN, both builds run to the FINAL with no questions (his words, checked)
- **His words (to the Main Brain, ~04:30 PKT, checked in its transcript):** "when I wake up I want these videos done ... I don't want
  you to go like one 2 hours in and you're asking me for something ... All of these sessions will be running Opus as their main model
  and Fable as advisor". Both builds now read claude-opus-5-5 / xhigh.
- **Starts:**
  - Sirius: its own 07:03 cron.
  - Dad: its background wait (exits 02:00 UTC), plus a 02:05 UTC cron backup the hub asked for. Confirmation pending.
- **The hub's no-questions defaults (sent to both):**
  - a lock-held READ-ONLY FCP XML snapshot of his unsaved ABW11 trims first;
  - code build from his EDL on the house template, finals to Final Renders + X:\Claude Projects\Exports\, no Premiere writes;
  - no Demucs download without his OK (RAM is tight too), so use the afftdn beds;
  - no Higgsfield or paid credits; Topaz is allowed with a watermark check;
  - PoA BTS out; censor by the default;
  - log every call made without him in RUN.md "Decided without Affan".
- **Morning:** each RUN.md opens with the summary. The hub verifies each final (hashes, loudness, a contact sheet) when the builds report.
- **Usage cap (his words to the Main Brain, checked):** "I don't wanna wake up and see like some enormous amount already used entirely
  like 50% of the weekly limit ... keep everything in limits". The Main Brain set the number: 10 % of the weekly all-models meter for ALL
  overnight work. At 7 % a session finishes only the current deliverable; at 10 % it stops at a clean checkpoint with a morning summary.
  Opus works, Fable advises at decision points, Sonnet/Haiku/scripts do the mechanical work. The hub stays near idle overnight.
- **07:05 Dad:** the snapshot of his re-cut is done (57.3 → 36.2 s; beats 6 and 7 dropped; he ends on "Paris Jackson_ I Love My
  Daddy So Much.mp4", Paris as a small child on frame: HIS placement, kept and flagged in the morning summary).
  - The 07:05 backup cron landed mid-turn and ended the build turn. The hub nudged it at once to resume from RUN.md.
  - LESSON: a backup cron must say "if the build is running, carry on with it", not "do nothing and stop".
- **09:05 Dad v1 FINAL, hub-verified ~09:15:** `projects/mj-the-dad-he-never-had/outputs/The Dad Michael Never Had.mov`.
  - sha256 `c1be2701…d7fcedd` identical at outputs/, `E:\Shorts\Abudance Wisdom Shorts Exports\Final Renders\` and `X:\Claude Projects\Exports\`.
  - ffprobe: h264 1080x1920, 60 fps, 2183 frames, 36.38 s; PCM s24le 48 kHz stereo. ebur128: -14.1 LUFS, LRA 2.5, peak -1.6 dBFS.
  - Contact sheet read (`proof/final_sheet.jpg`). The two dark samples (4.5 s, 19.5 s) are designed ~0.6 s dips (luma 72 → 20 → 70 over
    35 frames), not stray frames. 32-36 s is his child end clip (Paris small, on frame): his placement, flagged.
  - Decided without him (RUN.md morning summary): no Higgsfield on the young-Michael+Joseph still (Lanczos); the beating overlay in
    gentle slow motion (a test, real speed is one line); captions on one base cross Michael's lower face at 13.3-14.8 and 17.1-19.5 s.
  - v2 running: fixes two same-camera head hops (7.48 s 25 px, 27.65 s 69 px; gate 8 px). If v2 fails QA, v1 stands. Build usage 6 %.
- **09:59 Dad FINAL = v2, hub-verified ~10:05.** Same three paths, sha256 `2f0f7506…45454ecd` identical at all three; 2183 frames,
  60 fps, 36.38 s, -14.1 LUFS, LRA 2.5, peak -1.6 dBFS. v1 kept beside it as `outputs/The Dad Michael Never Had v1.mov` (`c1be2701…`).
  - Head hops (gate 8 px): 7.48 s dx 6.3 / dy 2.5 (v1 -13.2/24.8); 27.65 s dx -1.6 / dy 6.2 (v1 12.0/69.0). Fix: OPR pair at 183 %,
    Sunrise pair at 234 %, y locked; windows inside the source limits. Hub read `proof/v2_hops.jpg`: steady across both cuts, no watermark.
  - Topaz: Iris only on native-HD shots (S12, S15, S16, S18, all 1920x1080); none on the 2003 interview (P3), OPR or the child clip
    (the A/B showed plastic lips). Watermark checked on every Topaz segment by the build.
  - Build used ~6-7 % of the week. Waits for his review; a note = a finish re-render, not a rebuild.
- **10:22 Sirius FINAL, hub-verified ~10:40:** `projects/oldman-good-sirius/outputs/Was Oldman A Good Sirius.mov`, sha256 `b93763de…a63e47`
  identical at outputs/, Final Renders and `X:\Claude Projects\Exports\`. h264 1080x1920, 60 fps, 1919 frames, 31.98 s; PCM 48 kHz.
  ebur128: -14.1 LUFS, LRA 6.3 (crowd swells), peak -1.6 dBFS.
  - Hub read `proof/final_1s.jpg`. The dark sample at ~2 s is a designed dip (luma 58 → 20 → 54 over ~30 frames).
  - Decided without him (RUN.md, 16 items; no item 12): Sirius = Grimmauld family-tree close-up slowed; Rickman 2015; Hagrid then Ron at
    y≈1395 (not his 1520, safe floor); eased zoom; subscribe prompts at 30 % and 57 %; face scale 2.0; the OotP Death Chamber rehearsal
    band ON (Radcliffe ~16: OotP BTS is OK per REVIEW1 § 2.5 + the public-figure teen rule); no Iris/Proteus on faces.
  - Open (his): Sirius's lips open near the end of the slow slot; name-card sounds at -24 dB under the voice (brief 19-23); 1080p only;
    slides judged from stills, not watched at speed; the no-band variant is buildable. Build used 8 % of the week.

## ▶ 16 Nov 03:25 PKT (hub): Sirius review 1 (his Tella, to sirius-build directly); the hub's 07:00 order sent
- **His words in sirius-build (checked):** "https://www.tella.tv/video/affans-video-3a6k3dzz start at 7am not rn just read it ane
  everythign but start the build when my limit resets". He also set that session to Opus himself (`/model claude-opus-5-5`).
  From the guide: "full effort on it using Opus as fable as your advisor".
- **His edit:** he re-cut our v6 in ABW11 from 48.98 s to 31.98 s, unsaved at 02:51. The build ran one read-only read at 03:03. The
  brief, resolved to timecodes: `projects/oldman-good-sirius/review1/REVIEW1.md`. It starts at 07:03 (cron).
- **The hub's order:**
  - Finish in CODE from his EDL (snapshot the FCP XML read-only first), copying mj-son-step-outside as shipped. No Premiere writes.
  - YouTube one at a time, in order:
    - (a) 4K OotP Sirius, suited;
    - (b) Radcliffe + Oldman BTS in costume: OotP OK (his ask, his own teen-era footage under the 14 Nov ruling); PoA BTS (13-14)
      flagged for his OK;
    - (c) an HQ Ron film frame.
  - `yt_api.py` gained the caller `sirius-build` (12 searches). Pacific day 11-15 had 0 searches at 03:20 PKT.
- **At 07:00 both builds start.** Premiere reads and writes go under premiere.lock, GPU work under gpu.lock. RAM was tight yesterday.

## ▶ 16 Nov 03:08 PKT (hub): his Tella walkthrough for the Dad Short sent to the build; START AT 07:00, not before
- **His words:** "Give this video to the session which is building the Michael Jackson Prince Jackson story arc where Michael got
  beat a lot but then it transitions Prince in Paris talking very good about him and tell that session to start the actual build
  work when the limit resets which is at 7:00 AM 4:00 hours from now not right now".
- **Video:** https://www.tella.tv/video/affans-video-8fb42orl. Sent to dad-never-had-build (local_9b79077a-6239-4c8f-ba4f-56c4e43bea19,
  Sonnet xhigh). Delivered; its turn started, but its reply is not confirmed yet.
- **The build's instructions:**
  - Hold everything until the Mon 07:00 PKT reset (02:00 UTC), with one background wait to wake it.
  - Then check the meter, take in the walkthrough (never in a browser; curl the m3u8, then ffmpeg), and resolve it into the job's BRIEF.md.
  - Then read the live ABW11 cut and build to his notes. No save or export; quiet-gate status before each write.
- **Research lanes:** all idle, still on hold. He named only this build for 07:00.

## ▶ 15 Nov 17:55 PKT (hub): the deep-research run is CLOSED: no pick; ranked board written; stopped at 92 %
- **The board:** `research/deep-research-2026-11-14/HUB-BOARD.md` ▶ THE RANKED BOARD. All six finals say no pick.
  - The Dad Short built to STOP 1 in ABW11 is HIS eight-beat sequence ("build this in premiere" ~09:00, checked): ≈120K, under the bar.
    Its "swap" variant is ≈200K, borderline.
  - Next: the armband (≈140K), Back Home (≈140K), Felton (120K).
  - The Sirius lead (40-100K) is also at STOP 1, built on his word.
- **Late:** due 10:00, ~8 h late. Nothing woke the hub after 02:55, and the meter went 65 % → 92 % meanwhile.
- **Meter 92 % / Fable 85 % at 17:47, reset in 13 h:** past the hub's own 82 % stop line.
  - Every lane is idle and none was woken.
  - His rule is 100 % at the reset, so holding or spending the last 8 % is his call.
  - Owed after the reset: hp-cast's Rickman/Snape topic (his 01:20 ask) and Felton's 16 s stage clip `DAiOcdPh7wY`.
- **Model rule (his words to the Main Brain, ~17:45, checked in its transcript):** "inform all sessions and switch back to opus
  extra and editor sub sessions will now run on sonnet as well". The hub reads Opus xhigh; the lanes read Sonnet xhigh. Every
  `start_session` from this hub passes `model: claude-sonnet-5-5`. Memory: feedback-use-fable-allowance.
- **yt_api.py** gained an `affanwiz` caller at 09:32, edited by another session.
  - "His 15 Nov OK" rests on a code comment and a memory line; the hub has not seen his words.
  - Its cap of 0 blocks only `search`, so "listings only" is not enforced (videos/commentThreads still pass). Not changed.

## ▶ 15 Nov 02:22 PKT (hub): Sirius raw cut PLACED in ABW11 (his "build it in premiere"), STOP 1 nearly done
- **His words to hp-films:** "try the sirius angle but continue searching for better ideas also" (~02:00), then "build it in
  premiere" after seeing the v6 sequence. hp-films started build session local_73783eac-87f5-4409-8bbc-d8be66046fdb from
  `projects/oldman-good-sirius/BUILD-BRIEF.md`.
- **Placed:** "Was Oldman A Good Sirius - raw cut" (bin "Was Oldman A Good Sirius"): 1080x1920 at 59.94, 48.98 s, V1/A1 10 clips,
  V2 3 covers, 4 markers.
  - Window 02:20:11-02:20:23 (he had been idle 389 s); the project read ABW11 first.
  - His active sequence ("Speed Kicked Out - v2 mom bits") was restored by id, his playhead ticks are identical, and his Sequence 02
    is untouched. No save, no export.
  - The hub checked `premiere/READBACK.md` (end 48.98 s, every span with its words) and that the lock was released.
- **Hub approved** one ~5 s V2-only window to swap the Sirius placeholder for a real PoA Shrieking Shack shot from his own
  `E:\Bullshit Folder\Henry\Severus Snape scene pack 4K.mp4`, only if the frames are clean. The OotP veil stays a placeholder.
- **Offered to him, not applied:** the ~45 s filler-trim; the v4b order. Oldman sits at a +7 dB review level.
- **02:25 STOP 1 reported and hub-checked** (`projects/oldman-good-sirius/RUN.md` ▶ STATUS has his note; Premiere and GPU locks clear).
  - **ABW11 is NOT saved: the new sequence needs his Ctrl+S.**
  - **For his call:**
    - "have I been a good Sirius?" lands at 72-75 % with ~12 s of Radcliffe after it (HP-EXECUTION wants 60-70 % and the end within
      ~3 s of the payoff);
    - beat 3 ("they killed me off too early… it's me") is a second topic;
    - the ~45 s filler-trim and the v4b order are both on offer.
  - **By ear:**
    - a short sound inside the hook (408.7-409.0);
    - "Ron" vs "wrong";
    - the 17.68 s joint sits in a crowd swell.
  - **Placeholders:** Sirius (0-2.7 s) and the veil (beat 3). The pack's only Sirius shot (him shouting at Snape, dark) is offered, not applied.
  - **Disclosed:** WhisperX large-v3 on the GPU under lock.sh 01:50-01:54 (after a RAM check), plus a medium.en CPU pass outside the .asr-lock.
    No incident.
- **02:29 Sirius swap DONE** (V2 0-2.72 s = the real PoA Shrieking Shack shot from his Snape pack, 1106.81-1109.57 s: 66 frames, one continuous
  shot, no logo or subtitle, 240 % crop, no Iris). READBACK PASS, V1/A1 unchanged, lock released.
  - **Honest note:** QUIET-MODE has been absent since his "not editing" on 14 Nov evening (memory: delete it when he says so), and
    `quietgate.py run --` returns at once without the flag. So the 4 s V2-only write ran while he was at the machine (idle ~73 s).
  - No sequence switch and no playhead move: his active sequence id and playhead ticks are identical. No save, no export.
  - To honour an "idle only" ask without the flag: check `quietgate.py status` (idle_s ≥ 150) first (lab-notes, line ~1243).
  - If he is editing again, QUIET-MODE goes back on at his word.

## ▶ 15 Nov 00:20 PKT (hub): pace.sh overlap bug found (ig-mj) and fixed
- **Seen:** two YouTube downloads ran at once at 00:14 (ig-mj's and hp-cast's), and aw-speed's thumbnail curl got in at 00:18:22.
  No bot page, no 429, no flag.
- **Cause:**
  - pace.sh, like lock.sh, took over any lock older than 30 min, even from a live download. Speed's long section held it
    23:15 → 23:45, and ig-icons took over at exactly 23:45:27.
  - Every exit then removed the lock, even when it was no longer its own, so one take-over cascaded.
- **Fix (00:19:49, tested in a scratch lock dir, 4 cases):** a lock is taken over only when its owner process is gone (or no owner
  line for 30 min, or after 4 h), and an exit removes only its own lock. Old copy: scratchpad `pace.sh.before-fix`.
- **ig-mj:** 2 of its 4 downloads got HTTP 403 on DASH format 137 (ESeXvAeuokU, snMguJ8UuyI). Allowed one retry each with HLS 270+234,
  plain yt-dlp with the default clients, after the old instances exit. No more formats after that.
- **lock.sh has the same latent bug** (youtube 30 min, gpu 90 min take-over; an unconditional release). A GPU job over 90 min
  could be joined by a second one. It is shared tooling and still unfixed: his call.

## ▶ 14 Nov 23:14 PKT (hub): YouTube CLEARED; Speed review-2 fixes re-delivered (23:10), hub-verified
- **YouTube:** ONE probe (`yt-dlp --print` on the Son Short, 06cXi5cJXMQ: 459,747 views) answered normally at 23:13, under the
  lock. Flag renamed `youtube.BLOCKED.cleared-2026-11-14`. `pace.sh youtube` cool-down raised 45 → 180 s.
  - Download slots sent: Speed's stream → ig-icons (now) → hp-films 23:35 → ig-mj 23:50 → hp-cast 00:10; bolt-celeb and ig-sports download nothing.
  - Searches and numbers stay on the API.
- **Speed v2, his review-2 fixes** (his notes 22:40): the 2026 podium judder (30p doubled to 60p; Stage A dedup by flow
  interpolation; face jitter 24.6 → 10.0), and the "pasty AI-ish" letterboxes, re-cut on Speed alone with Topaz Chronos only, no Iris.
  - The hub checked: outputs, Final Renders and Exports are byte-identical (sha256 2cd73f67…); 1080x1920, 60 fps, 38.50 s;
    −14.0 LUFS, LRA 2.2, true peak −1.6 dBFS. The contact sheet shows the wides on Speed alone.
  - His review named the letterboxes, not the Higgsfield stills, so the stills stay (fix only what he named). The 22:08 flag is
    answered by his own review.
  - Lessons already in LESSONS.md (the build wrote them: the doubled-frame head lock; Iris on small faces reads pasty AI-ish).

## ▶ 14 Nov 22:08 PKT (hub): Speed "His Mom Kicked Him Out" v2 RE-DELIVERED (22:05), hub-verified
- **Files:** `projects/speed-kicked-out-three-peat/outputs/`, `E:\Shorts\Abudance Wisdom Shorts Exports\Final Renders\` and
  `X:\Claude Projects\Exports\` (`His Mom Kicked Him Out.mov`) are byte-identical (sha256 d2de3f8e…, 268 MB).
- **Probe:** 1080x1920, 60 fps, h264 + PCM 24-bit 48 kHz, 38.50 s. **Loudness** −14.0 LUFS integrated, LRA 2.2.
- **Contact sheet:**
  - captions just under the lips; the Streamer of the Year labels sit low;
  - two subscribe prompts, no end screen;
  - the fireworks stream carries its true label (JULY 4, 2022 / SPEED WAS 17).
- **Detroit beat** = his dad's Christmas photo (dad's own IG post, Sep 2021). Speed is about 14-15, which his 14 Nov teen-era ruling
  covers. The younger boy is cropped out (checked on frames 23.4-26 s).
- **FLAG for him:** both stills (the teen cap selfie and the Christmas photo) went through a Higgsfield 4K upscale with face checks.
  - The hub looked at `proof/v21/christmas_speed_compare.jpg`: same face, a little smoother skin, crisper hair.
  - His 14 Nov Katherine rule says a real person's face from a soft source gets Lanczos only. HP-EXECUTION v1.3's new suspect is
    the AI look.
  - Keep it, or swap in a Lanczos still: one still each, his call.
- **Open:** the Apr 2020 face-cam stream for S03 (`research/aw-speed-pick-2026-11-13/yt/batch19.sh`, after the unblock); the Mastro's
  original (17) if he prefers it for Detroit.

## ▶ 14 Nov ~21:40 PKT (hub): the YouTube Data API replaces yt-dlp for research searches and numbers (his key)
- Affan made a YouTube Data API v3 key for AW research (relayed by the GTA 6 watcher session, then his own words here: "once you set
  the api up tell all the research sessions to use this instead of their normal method"). Key file and how-to:
  `X:\Claude Projects\Abundance Wisdom\` (`YOUTUBE-API.md`). Never print or copy the key; it goes in the `X-goog-api-key` header.
- **One door:** `research/deep-research-2026-11-14/yt_api.py <slug> <endpoint> ...` (the hub's, tested 21:35): reads the key itself,
  12 searches per session per Pacific day (hub 20, all 95; 100 units each), 1-unit lookups, a 12 h cache, a log, a quota flag.
- The API can't download or read captions: yt-dlp stays for finalists' source files only, after the ~23:15 probe, in the hub's order.
- First answer (21:35, exact views): Son 455,396 (35 s) · Jermaine JEALOUS 63,839 (38 s) · Snape 24,045 (44 s, 978 likes).
- All six research sessions told at ~21:40 (README ▶ THE YOUTUBE DATA API).

## ▶ 14 Nov 18:50 PKT (hub): research PACED DOWN; bolt-celeb interim
- **Usage:** weekly 33 % at 18:47 (9 % at 16:45, ~1 % after the reset), about 12 points an hour against the ~3.5 the README planned.
  The 75 % line would have fallen ~22:30, before the interims and the YouTube probe. Fable meter 24 % (its value at the reset wasn't
  recorded; re-check for the slope). Sent to all six and written in the README § Budget: gate items only, park when blocked, one
  Sonnet subagent at a time, the advisor only at its two points, past 50 % before 23:00 → interim and park, finals ≤ 72 %, a counted
  YouTube queue (the hub orders it after the probe, Speed first). He can lift the pace with a word.
- **Instagram is fine:** "No results" = phrase refusals (health, death, minors words); the freezes = Chrome freezing background
  tabs. Grids kept loading through 18:46. No flag.
- **bolt-celeb interim** (`research/deep-research-2026-11-14/bolt-celeb.md`; NOT max effort yet: B, C, E, G/H/J):
  1. CARD Tony Bennett × Lady Gaga, "he forgot her name for weeks": IG @day.taught.me 20.9M views (187x its page). It is the 12 Nov
     runner-up to Amy (`projects/tony-gaga-remembered/RUN.md`, never pitched in full), and the card must say so. Non-MJ face gate first.
  2. LEAD Bieber booed 2013 → VMA tears 2015 → Fallon "I was just feeling judged": IG proof weak so far (68K).
  3. MJ narrated: no pick. Real MJ in HD exists only in 2009 and on 35 mm film.
- **Two questions for Affan (non-blocking; the sessions work the strict reading meanwhile):** under narration, may letterboxed SD
  archive be the main picture? May biopic shots (Jaafar, 4K) stand in for a real MJ event? Strict reading on record: HQ first-party on
  every beat; SD only as letterboxed archive overlays through the Topaz chain; biopic shots only where the beat is about the biopic
  (Son, Brother).
- ig-icons has no report file yet and ig-sports' is from 17:13: both told to write it now. Board: `research/deep-research-2026-11-14/HUB-BOARD.md`.

## ▶ 14 Nov 16:42 PKT: YOUTUBE BLOCKED ("not a bot" page)
- Set by aw-speed-research: about the 17th request of a batch spaced 60 s or more apart. The HUB'S OWN channel listing at 16:34 (yt-dlp
  `--sleep-requests 3`, about 10 page requests in 24 s) most likely helped trip it. Lesson: a channel listing is a burst. Space its pages
  15 s or more apart, or don't list.
- ONE probe due ~23:15 PKT (a background timer in the hub). Clear only if it answers normally. All six research sessions plus Speed were told.

## ▶ 14 Nov ~17:15 PKT (hub): SIX DEEP RESEARCH SESSIONS (his ask, max effort), final reports due Sun 15 Nov 10:00 PKT
- His ask: 5-6 Opus sessions with the Fable advisor, the deepest research possible, banger ideas. Two HP sessions because Snape went #1
  then #5-6 (~23K): the niche is right, the execution wrong. Each report must open with the max-effort statement, or "NOT max effort yet".
- **Gate:** `MAX-EFFORT-GATE.md` § Idea research runs, items A-K, the exact statement, no quota, one card format.
- **Run folder:** `research/deep-research-2026-11-14/`:
  - README.md: lanes, rules, clock, stop lines (75 % deliver, 82 % stop);
  - CLAIMS.md and IG-SEARCH-LOG.md: append-only ledgers;
  - AW-SHORTS-NOW.md: all 274 AW Shorts with views, one paced listing at 16:45. Son ~445K, Jermaine 51K, Snape 23K, Bieber 26K,
    Burnt Hair 83K.
- **Pacing:** `projects/_onyx-batch2-2026-10/pace.sh` (new; lock.sh is untouched):
  - youtube: the same lock and BLOCKED flag as lock.sh, 45 s cool-down;
  - instagram: one page load at a time, 30 s apart, flag `.locks/instagram.BLOCKED`. Only the hub clears either flag, after one spaced probe.
- **Sessions:**
  - hp-cast `local_c08edcc2-e13a-4777-aa9b-17e04e01c145`: owns `HP-EXECUTION.md`, the Snape diagnosis;
  - hp-films `local_aa5f066e-35d1-4f67-bb87-1a54ab7b5765`;
  - bolt-celeb `local_414229a9-68e9-4ab0-9774-024fe1a5577e`;
  - ig-mj `local_6dacb48e-3a7b-4097-8855-311015f0e999`;
  - ig-icons `local_2d0127a7-d1c0-4e5a-890c-7ba5a02e5e98`;
  - ig-sports `local_ad5aa18c-a10d-45d9-a4e3-b606978ac193`.
- **Clock:** interim shortlists Sat 23:00 PKT. The hub then verifies the reports and gives him ONE ranked board, not six relays.
- **Archived:** the HP research session and the Snape build ("snape is done"). Snape's result is in RESULTS.md (Nov 14 block).

## ▶ 14 Nov (hub): usage reset to ~1 %, lean LIFTED; second cleanup
- Affan used a usage reset (Sat 14 Nov). Goal: use the full 100 % by Mon 16 Nov ~02:00 UTC, at max effort. The Speed line was told to
  resume its Phase B if usage was the only blocker.
- **Archived (finished or abandoned; findings already in files):**
  - aw-two-new-shorts `local_f3f50832…`: Beyoncé rejected (`research/aw-pick-2026-11-12.md` § Verdict); Whitney "good enough" on
    paper only (`projects/whitney-good-enough/PITCH.md`).
  - bolt-format-test `local_eb1a2dc8…` (`research/bolt-format-test-2026-11-12.md`) and amy-grammy-raw `local_c7c1f5c1…`: Amy
    rejected, lesson in LESSONS.md + memory feedback-no-below-bar-pitches. Its unsaved raw sequence is still in ABW11.
  - instagram-beat-mining-ma `local_7bc581c4…`: IG run 4/4b, no pick (`research/instagram-beat-mining/2026-11-13-run4.md`).
  - aw-shorts-harry-potte-2 `local_7f87fba7…`: HP idea 3 (Hagrid) DROPPED by Affan on 12 Nov ("just 2 topics";
    `projects/harry-potter-idea3/RUN.md`; the lesson is in memory feedback-checklist-shape-is-a-gate).
- **Kept:** ig-beat-mining (the method + read dates 15-17 Nov); aw-speed-research + speed-kicked-out-build (building); aw-mj-son-method +
  build-mj-s-brother-saw-h (delivered, waiting on his review); jermaine-mocked-skin (v2 delivered, waiting on his review);
  aw-shorts-harry-potter-n + snape-prank-build (Snape v1 re-delivered 12 Nov after his review 1; done or not is his call).

## ▶ 14 Nov ~01:00 (hub): MJ brother DELIVERED, Speed at v8
- `Michael Jackson's Brother Saw Him AGAIN.mov`, checked by the hub: Final Renders and Exports are byte-identical, h264 1080x1920 60 fps,
  pcm_s24le, 33.3 s, -14.0 LUFS, -1.6 dBTP. Contact sheet: house style, 2 subscribe prompts, labels low. The group photo (~12 s) is the
  adult brothers on stage, no child. His calls: a 17 px head jump on La Toya, the softer brothers still, "his/her makeup" by ear.
- Speed v8 (`projects/speed-kicked-out-three-peat/PITCH.md`) adds his Sept 2025 stream "I need a therapist… I feel alone", NOT max
  effort (no re-read of v8, usage 90 %). Nothing built.
- **Speed BUILD started** on his "Yes, build v8" (said to aw-speed-research): `local_0a18dba6-8ce5-4b83-9f13-58f00c68202d`
  (speed-kicked-out-build, Sonnet, `projects/speed-kicked-out-three-peat/BUILD-BRIEF.md`). STOP 1 = raw cut in ABW11, STOP 2 = finish
  stills. Budget <= 4 %, stops at 98 % weekly. Never start a second one; the hub checks the delivery.

## ▶ 13 Nov evening (hub): Amy REJECTED
- Affan: "the amy winehouse short is absolute garbage its not gonna get even 10k views". All Amy work stopped (bolt-format-test told). Its unsaved raw sequence is still in ABW11.
  Lesson in LESSONS.md and memory feedback-no-below-bar-pitches: a narrated non-MJ Bolt-format idea whose centre sits near the 60K
  floor is below the bar, so it gets "no pick", not a raw build.

## ▶ 13 Nov ~16:00 (hub): MJ brother build STOPPED and held
- His "start it" meant the Instagram research, not the build. His order: research (max pass, in aw-mj-son-method), then the
  sequence in text, then his OK, then the raw build. The hub starts nothing for it. New standing rule: `MAX-EFFORT-GATE.md`
  (root, CLAUDE.md § Rules): no sequence reaches him without max effort, the Fable advisor and a cold read of the final.
  The hub passed it to aw-speed-research.

## ▶ 13 Nov ~11:30 (hub): Speed research started
- His ask: an IShowSpeed Streamer Awards Short, "the most painful version": family not supporting him, then his own mental-struggle
  lines, then every Streamer Awards win with the latest last, ending on a third-party "greatest streamer of all time". Research only,
  then the sequence: `local_f3ae46ec-1f30-4fc9-b1c8-d8b66e211f0b` (aw-speed-research, lean budget ~3-4 %, usage 81 %).
  Key flag in the brief: any footage of him before 21 Jan 2023 shows a minor.

## ▶ 13 Nov ~07:20 (hub): Jermaine DELIVERED
- `Jermaine Jealous.mov`, checked by the hub: Final Renders and X:\Claude Projects\Exports are byte-identical (cmp), h264 1080x1920 60 fps,
  pcm_s24le, 37.217 s, -14.1 LUFS, -1.6 dBTP. A contact sheet every 1.5 s plus two full frames: house style, 2 subscribe prompts, no
  watermark, no child on frame. His calls: the title (none set yet), SD Narita/courthouse overlays, 3.6 % repeated frames in the La Toya
  hook (1991 source), and the family line uses the detail's audio (it isn't in GGN). MJ brother build: STARTED on his own "start it now bruv" in aw-mj-son-method: `local_7f7e09b5-4016-40fc-bd63-6b5848cae89b`
  (Sonnet, BUILD-BRIEF.md). Never start a second one. Amy raw build running too: `local_c7c1f5c1-cfe5-4604-ad35-1def867cdfc2` (started by bolt-format-test). LEAN MODE: 80 % on 13 Nov, until the 16 Nov reset. aw-mj-son-method is running his "max pass" on the beats and feeds it in at STOP 1.

## ▶ 13 Nov ~05:10 (hub): two builds
- **Jermaine: FULL BUILD running** on his Tella 2 review, given in its own session ("start the full build now"). His cut is 37.27 s
  (`premiere/his_abw11.json`), the build spec is BRIEF.md § HIS REVIEW 2, and BUILD.md is the template. A Sonnet builder is on Phase 1 and
  stops at proof/r1 for a frame check. ~3 % of the week.
- **MJ "Brother Saw Him AGAIN": his YES** (given in aw-mj-son-method): order A, split from frame 1, Marlon out
  (`projects/mj-family-saw-him-again/BUILD-BRIEF.md`, Sonnet build, 3-5 %). The app's session cap blocked the start; the hub asked
  that session to retry after the archive. ONE build session only, and the hub starts none of its own.

## ▶ 13 Nov ~01:00 (hub): two pitches waiting on Affan, nothing built
- **MJ pick from the Son-method run** (`local_efbcf199-e703-401c-b80c-6b6b226f30be`, `research/aw-mj-pick-2026-11-13.md`):
  "Michael Jackson's Brother Saw Him AGAIN 🥹", ~29 s, `projects/mj-family-saw-him-again/PITCH.md` (v2, after an Opus cold read).
  Jackie's red-carpet tears → La Toya → Jaafar on his grandmother → the producer: Katherine in her wheelchair, "That's Michael."
  Prediction 60K-2M, centre 150-400K. Named risks: Jackie's tears already did 9.9M as a Short (May), and it's one idea said four
  ways. The hub checked: all 5 sources are 1080p broadcaster originals; the anchor tile has all four faces at or above Prince
  ABC (skin smoothing is his eye). No second MJ pick. Instagram hit a 429 at 00:53 (stopped for the day).
- **Bolt-format contender** (bolt-format-test, `local_eb1a2dc8…`): Amy Winehouse's 2008 Grammy by satellite,
  `projects/amy-grammy-satellite/PITCH.md`. 85 % narrator (his voice or one AI voice is his call), IG 3.8M, 1080p GRAMMYS
  source (checked). Centre ~70K against AW's 6-19K non-MJ base rate, so the hub leads with the MJ pick. Runner-up Tony × Gaga.
- Usage 56 % on 13 Nov 01:00, reset 16 Nov 07:00 PKT.
- **Jermaine Jealous raw cut re-laid in ABW11** (his ask, 13 Nov ~01:40: "resequence it inside the new premiere project"): sequence
  `Jermaine Jealous - raw cut`, bin `Jermaine Mocked Skin`, 47.15 s, unchanged v3. The hub checked: it is the active sequence in
  ABW11, and its read-back is identical to the ABW10 v3 read-back. Unsaved, lock released. Waiting on HIS REVIEW, then the house style.

- **14 finished sessions ARCHIVED on his ask** (13 Nov ~02:00: "too many, I'm getting confused"; archive, not delete): Harry Diana,
  Paris, MJ Outthink, Conrad, Patrick, Kane, Katherine, Owen Hart, Ronaldo, La Toya, Mother (Burnt Hair), Son, Bieber, Victory Tour.
  The session ids below still work: unarchive one to reopen an old ask. Kept: MJ research, both IG beat-mining sessions,
  Jermaine, the HP line (research, fork, Snape), and the 12 Nov two-Shorts research with its Bolt-format test (Amy).

## ▶ 12 Nov evening (hub)
- **Beyoncé pick REJECTED by Affan (12 Nov ~22:45: "not getting the vibe").** His direction instead: the Son Short proves MJ still works,
  "we just need to be better in finding moments": a NEW research session for MJ Shorts that copies how the Son moment was found
  (`research/instagram-beat-mining/2026-11-08-run2.md` § Evening: MJ replaced).
- **Son Short ("Saw His Dad AGAIN", pub 11-10) is a HIT, not a flop:** 179.5K at 2 d 11 h, #1 of the last 10, 89.9% APV, 94%
  Shorts feed, still climbing (RESULTS Nov 12 block). It was 5.3K at hours old. MJ family lane is alive; the house style is its build.
- **Two-new-Shorts research** (`local_f3f50832-3ca9-45e3-8c52-4ec408eb6845`, `research/aw-pick-2026-11-12.md`): ONE pick,
  "Why Beyoncé's Mother Couldn't Defend Her 💔" (`projects/beyonce-what-they-didnt-know/PITCH.md`, ~37 s, Tina ET 2025 1080p
  + Beyoncé 2013 film audio). Instagram gate OPEN (two 429s); everything else passes. The hub checked the anchor tiles: Tina is
  in the Prince class, and the 2013 webcam footage holds at 70% on blurred fill. No second pick (Will Smith killed, Emma Heming
  Willis benched). Usage 49 → 53%.
- **Snape Short delivered** by the HP line (`Harry Potter Thought Snape HATED Him.mov`): the hub verified 3 identical copies,
  1080x1920, 43.93 s, **30 fps** (the Jaafar template shipped at 60). His call on a 60 fps re-export is open.
- Still open from before: Whitney's censor call.

## ▶ STATUS: resume here (2026-11-10, written before a /compact)

**Nothing is running from the hub.** Every linked session was idle at the last status. Weekly usage: 76 % on 7 Nov, reset
Monday ~02:00 UTC (07:00 Pakistan time). The advisor is Fable 5.2 since 10 Nov (his `/advisor fable`, live after the compact).

**10 Nov strategy research (after Bieber and Son flopped):** `research/aw-strategy-2026-11-10.md`.
- Nothing broke: the 18-29 Oct MJ death-lane run was a hot streak, and it ended. Every other Short since early October (MJ or
  not) opened at 3-80K on day one, September's band, with viewers holding (stayed 68-78%).
- YouTube's 1 Oct "original content" Shorts change is a live risk (clip peers fell, narrated ones grew). Our feed columns show
  no sign of it: misses aged 5-13 days still get 79-94% of views from the Shorts feed.
- Oxygen chamber DROPPED (Gate 5: his manager confirmed the sleep plan to UPI in 1986).
- Pick run `research/aw-pick-2026-11-10.md`: nothing cleared every gate. Ranking: Whitney/Bobbi (best bet), Dolly (clipped at
  407K), Britney 2008 "jail" (2026 DUI undercuts it), MJ "Dangerous" in court.
- No guarantee line typed.
- Later the same day, the Instagram pass (all six names) found nothing stronger.
- Dolly is killed: the Walters beat was clipped right after her death (25 Aug: 407K, 175K, 91K Shorts dated 25 Aug-1 Sep).
- Whitney's sources top out at 720p re-uploads of 2012 TV.
- The proposed default is Jermaine first: the MJ cut already in ABW10, waiting on his direction. Whitney second; deeper
  Instagram mining goes to the ig-beat-mining session.
- Read dates: Burnt Hair 15 Nov, Bieber 16 Nov, Son 17 Nov.
- Evening: Whitney downloaded and checked (`projects/whitney-bobbi-last-day/PITCH.md`). After a re-test against the
  softest approved footage (Prince ABC, Bieber's Oslo), it **PASSES the checklist**. The earlier 'killed' read was a bad
  measurement.
- Pitched with one ask: his censor call on 'I would have went right with her'.
- Jermaine stays unpitched until its UCLA beat is replaced and its main beats get the same anchor test.

**Waiting on Affan:**
| Job | Session | What it needs from him |
|---|---|---|
| Jermaine Jealous (MJ's brother mocked his skin) | `local_0729b59b-cdba-451e-a976-e7b98a4410f4` | his direction on the 47.15 s raw cut in ABW10 (title + one word "out"/"up front" were also open) |
| Why MJ Gave Away 5 Million (Victory Tour) | `local_59aa922f-cf80-4fde-9047-81d1b48d98f8` | **REJECTED by him** on footage and audio quality (IDEAS.md); replaced by the Son Short. The unsaved sequence is still in ABW10 |
| Why Justin Bieber Walked Off His Own Stage | `local_12157f61-18f2-4fa8-a97b-dac32e70ace2` | the title pick; he already exported "Justin Final YT" |
| La Toya Betrayed | `local_d3f748df-e06e-4089-9b46-7c54053bd766` | his verdict on the Bolt Motivation look (decides the look for the rest) |
| Instagram method | `local_fd5de818-0d1c-43c9-98f2-673ea76852df` | view numbers once each Short's curve is flat (RESULTS-TRACKER.md); the method is unproven on YouTube until 4-6 flat rows |

**Finished on his side (his own "Final YT" export exists):** Harry Diana, Owen Hart Wife, La Toya Betrayed, Ronaldo Retires,
Bieber, Son Step Outside ("Jafaar"), and very likely What MJ Showed His Mother ("Burn"). Their sessions:
Harry `local_1836bd12-b423-40a8-9d24-caa48e312e5b` · Owen `local_dab7588d-f5fb-4c94-83f5-0b85a02aa394` ·
Ronaldo `local_40fe9e55-20a9-4f3c-937e-e429cb4a9ba9` · Mother `local_6dae492a-d521-4d43-9ca6-b6a0d7e2d839` ·
Son `local_60e694a4-3f6d-4d05-bd46-451642f9f0b7`.

**Older asks, NOT re-checked since 5 Nov** (read that job's RUN.md before acting; they may be done or dropped): Conrad's full
Topaz pass (`local_a9997639-1d78-42d0-b4d6-5d8f1a97c07e`); labels to the bottom on Patrick (`local_5e58eaf8-5db4-4d8d-87e4-c8a621b17b23`)
and Kane (`local_b76e56a5-15a2-4a68-a211-2effd951afca`); a dark backing behind Matt's label on MJ Outthink
(`local_9ba083d7-8d14-47e2-934a-d8599e2072dc`); reviews of Paris Shock Therapy (`local_028af0ae-f7b7-414b-9540-09cc14ff9bc1`)
and Katherine (`local_da5a006a-36b0-4117-aa32-ff0ceadb2381`). A third end-screen concept only if he asks.

The per-Short history is in memory `project-abundance-shorts-automation`; each job's own state is its `projects/<job>/RUN.md`.

## How the hub works
- **No idea is pitched until it passes [PITCH-CHECKLIST.md](PITCH-CHECKLIST.md)** (Affan, 10 Nov): facts and recent news, the downloaded sources checked by eye and ear, freshness, proof, shape, his rules. A fail is logged, not pitched.
- **A pasted locked brief = a new Short = its own session.** Offer it with a title alone; he has picked "New session" every
  time. Then send the brief verbatim plus the standing-rule conflicts. If he asks in words for a subsession, start it directly.
  Over Remote Control the offer card can't be shown, so ask in text or start it when he has asked.
- **Workstreams are linked subsessions of the hub** (his ask, 2026-11-07: "everything is in one main session"). The daily
  Instagram idea work runs on Code, not Cowork ([memory: project-instagram-beat-mining]).
- **Relay in one or two plain lines with the session link**: what happened, what is checked and what isn't, what he must do.
  He dictates by voice and is often on his phone.
- **A child's note is a report, not proof.** Check every delivery yourself before calling it done: `ffprobe` (1080x1920,
  fps, duration) and `cmp` the `X:\Claude Projects\Exports` copy against Final Renders.
- **Find deliveries by title.** The newest files in Final Renders are often his own Premiere exports (`Chop.mov`, `Push.mov`,
  `box37.mov`, `prince1.mov`: pcm_s16le plus a timecode stream), not ours. Ours are named after the title, with earlier
  versions kept as `(vN).mov`. His `<word> Final YT.mov` means he exported his final.
- **Notes arrive cut at 400 characters.** For detail, read the job's `RUN.md` STATUS block; `list_events` often returns
  almost nothing.
- **Phone copy, only when he asks** (he's outside and wants to review): two-pass libx264 3700k, maxrate 6000k, AAC 128k,
  `+faststart` gave 24 MiB for a 54 s Short. Write `<title> (phone).mp4` to the job's `outputs/`, check the size and loudness,
  send it with SendUserFile, and delete it once he has reviewed.
- **YouTube block flag (`projects/_onyx-batch2-2026-10/.locks/youtube.BLOCKED`), the hub's job:**
  - A 429 gets one spaced metadata probe about 25 min later. A real "not a bot" page gets ONE probe about 6-7 h later.
  - Clear only if the probe answers normally.
  - Every YouTube request (metadata and search too) is ≥60 s apart. No caption/timedtext fetches: transcribe locally.
  - Example: 11 Nov 00:17, the HP session's 15 s-spaced metadata probes hit a bot page. One probe at 06:48 answered
    normally, so the flag was cleared (`youtube.BLOCKED.cleared-2026-11-11`).
- **Before a new workstream, read usage** (`get_usage`) and say the cost. Lean mode: no new agents without his OK.
- **Quote his words when forwarding an approval** ("Yes to all") to a session, and say what it does not cover.

## Rules the hub enforces (owners in memory)
Subscribe CTA on every AW Short, end screen OFF (README § 12) · no minors on frame · source audio only, no music on code builds ·
censor drug/self-harm words (ask per Short) · labels low, captions just under the lips · never save or export his Premiere
projects · work in silence · no C: exports, copies to `X:\Claude Projects\Exports` · YouTube: one plain request when he says
"download them yourself", never a bypass · no Fable agents · never kill another session's processes · the shared Premiere lock.
