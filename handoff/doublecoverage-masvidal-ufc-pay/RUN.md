# Onyx sample: Double Coverage Podcast, Masvidal UFC pay (Mystic Zach + N3on; Zach Hirsch said yes)

Job folder for the sample. Research files: `projects/_onyx-doublecoverage-2026-11/research/` (API data, transcripts, searches,
CANDIDATES.md). Sequence: `SEQUENCE.md` here. Brief + teardown: `BRIEF.md` here.

## ▶ STATUS 2026-11-26 ~07:00 PKT: AFFAN'S OK RECEIVED, BUILDING (YouTube look, H1 + O1). Not rendered yet.
- **The OK (direct, in this session, 2026-11-26 ~06:45 PKT):** "OK, build it" (answer to "OK the Masvidal sequence as written (H1 + O1), or
  switch to H2?"). Look: YouTube only (the week plan's "one look"; no IG feed to aim at).
- **Build source:** `raw/masvidal-ep.mkv` = the chapter video (VP9 1920x1080, 29.97) with its audio padded to start at pts 0 (PCM 48 kHz).
  Clock: file t = episode t - 1289.4546 (re-measured on pts, xcorr 0.97). Transcript: `transcript/words.json` (WhisperX large-v3, gpu lock, 11-26).
- **Edges:** segs-v3.json's edges came from faster-whisper and are WRONG against WhisperX (7 ends inside the last word, 8 starts inside the
  previous word, 4 drops in continuous speech). The EDL is rebuilt from WhisperX words + the 10 ms envelope, no_refine, slice ASR per joint.
- **Split:** main (Opus) writes `DIRECTION.md` and does every YouTube pull through `lock.sh youtube`; a Sonnet builder executes the build
  (batch-8/9 builder rules); main QCs the exported file.

## (previous) STATUS 2026-11-26 ~05:15 PKT: SEQUENCE v3 READY, waiting for Affan's OK. Nothing built.
- **Sequence:** `SEQUENCE.md` (v3 after the cold read + re-read): Masvidal on UFC 251 pay, 36.74 s, hook H1 + order O1, card THE UFC WOULDN'T BUDGE. UNTIL...,
  button "they didn't have nobody else". Runner-up hook H2 (Zach's question first). Brief + download log: `BRIEF.md`.
- **The go (relayed):** the main Onyx session ("Onyx Editor", local_c15be84c) relayed Affan's words ~04:10 PKT: "tell the double coverage
  session to build it anyway and pick from the channel they gave in the email". The check-5 numbers are in the sequence note.
- **Gate:** NOT max effort yet on three named items (thin Instagram beat proof, 4 of 6 candidates not downloaded, other tellings
  searched but not downloaded); everything else done (episode read in full, chapter video + 28 frames, audio splice + ASR, primary
  facts, 3 hooks / 3 orders / 3 moments, advisor before committing, cold read applied).
- **Next, after his OK:** the raw build in the YouTube look (`presets/youtube-shorts/onyx-samples-youtube/`, `kit/yt_build.py`), from
  `../_onyx-doublecoverage-2026-11/research/cutcheck/segs-v3.json` against the chapter video (clock = episode 1289.4546 s + t). Re-find
  every joint with WhisperX large-v3 under the gpu lock first (flagged: "Corona | so then", "20 M | from the UFC"). Native 29.97, no Topaz.
- **Unsent R1 thank-you draft r-4871469005659573971 (drafted 11-25)** stays with the email session. No email from here.
- Not touched: the show-notes row, the tracker, any email. Barbell Logic.

## The ask (from the yes, 2026-11-24 17:03 UTC)
"Yep, that's fine but our YouTube shorts page is now @doublecoveragetv so would prefer if you reviewed a clip from there."
So the sample must come from @doublecoveragetv, NOT "The $1.1 Million UFC Bet" (old page, named in the E1).

## Check 5, measured 2026-11-26 (YouTube Data API, Onyx key, 16 units; data in `../_onyx-doublecoverage-2026-11/research/shorts-2026-11-26.json`)
Subs = the main channel's 565,000 (the brief said 554K; the API says 565K today). The brief's bar: weak Shorts, "median well above
~3 % of subs" = stop. The screen's coded test (`onyx-sweeps/api/yt_api_screen.py` `cmd_screen`) uses the LATEST 6 Shorts only and
fails over 5 % median or 2+ Shorts above 15 % of subs.

| | @doublecoveragetv (new Shorts page) | @DOUBL3COVERAGEPODCAST (main, old Shorts) |
|---|---|---|
| Channel | "DOUBLE COVERAGE CLIPS", created 2026-08-01, 4,790 subs | 565,000 subs |
| Shorts | 121, from 2026-08-09; 50 in the last 30 days (~1.7 a day) | 160 pulled; only 3 in the last 30 days |
| Median views, all Shorts at least 7 days old | **35,118 = 6.2 % of the main subs** (111 Shorts) | 4,425 = 0.8 % |
| The screen's latest-6 test, literally | 6,508 = 1.2 %, 0 big: PASSES, but those six are 0.1-2.1 days old | |
| Latest 6 that are at least 7 / 14 days old | median 31,231 = 5.5 % (1 big) / 38,183 = 6.8 % (1 big) | |
| Shorts above 15 % of subs (84,750), all ripe | **27 of 111** | 9 of 159 |
| 500K+ / 1M+ | **12 / 4** (George Foreman 2.08M, AG 1.50M, Nate Diaz 1.42M, Arch Manning 1.04M) | 0 / 0 |
| Length | median 20 s (9-40 s), emoji titles, sports-celebrity hooks | median 52 s |
| Monthly median | Aug 33.8K · Sep 48.4K · Oct 37.5K · Nov 30.6K | 2026 months mostly 2-4K |
| Total views | 18.0M in ~4 months, for 4,790 subs (0.27 subs per 1,000 views) | |

**Verdict: their Shorts are STRONG, so check 5 fails by the brief's bar** (median 6.2 % against "well above ~3 %"). The screen's
literal latest-6 test passes only because those six were posted in the last two days; any window of Shorts old enough to have
their views reads 5.5-6.8 %. The old page was weak (0.8 %), which is why the E1 pitched it. Since August a dedicated clips page
posting daily has fixed that. My inference, not checked: someone (in-house or an agency) already runs it.

## The one angle that might still hold (for Affan's call, not verified)
- **Views, few subscribers on the clips page:** 18M views bought the clips page 4,790 subscribers (0.27 per 1,000 views). Whether
  its reach feeds the main channel or its long-form is NOT measured. The main channel grew from 554K (the brief) to 565K. This
  would be a channel-strategy point, not an editing one, and Onyx sells editing.
- **The floor:** 21 % of their Shorts reach 100K, but the median is 35K and the November median is lower (30.6K). A sample could
  re-cut a below-median Short to show the lift, but that comparison is weaker than on our usual prospects.
- **Instagram not checked.** A weak Reels feed would be the only angle that is about editing. One paced load, if he wants it.

## Log
- 2026-11-26: session started (Affan, ~2:20 AM PKT: "start building the samples for all except barbell logic"). Read JOBS,
  PLAYBOOK, LESSONS standing rules, the YouTube look's PLAYBOOK + README, MAX-EFFORT-GATE, the show-notes row. Pulled both
  channels' Shorts through the API (no YouTube page loads, no downloads). Stopped at check 5.
- 2026-11-26 ~04:10: Affan's go relayed by the main Onyx session (build anyway, pick from @doublecoveragetv). Research started:
  6 candidate Shorts queued, the Masvidal episode audio pulled and transcribed (GPU large-v3 under the lock; CPU run hit an
  out-of-memory), YouTube API searches logged in `research/search-log.jsonl`, Instagram log lines tagged [doublecoverage].
- 2026-11-26 ~05:15: chapter video (21:30-26:05, 1080p) in; 28 frames checked; cold read (Sonnet) found 9 defects, all fixed in
  SEQUENCE v2; the 4 remaining candidate Shorts stopped in the queue. Waiting for Affan's OK.
- 2026-11-26 06:50-09:00 (Sonnet builder): cut (8 pieces; four drops not clean on envelope/spectrogram -> fallbacks), caption transcript force-aligned per piece + hand pins (retime.py), ESPN page captured (page-record --full) and sentences copied verbatim, B clips cut to yt/assets/broll/cut-*.mp4, faces scanned, grade tuned on two stills (Ruslan-style gentle look), v1/v2 picture renders (machine memory errors: retry loop in run_all.sh), v3 in progress.
