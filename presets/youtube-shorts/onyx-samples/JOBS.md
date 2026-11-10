# Onyx: job log + resume block

Every Onyx job, newest state first. Standing rules are in `LESSONS.md` § "Standing rules" and `PLAYBOOK.md`, not here. Each batch's own tracker holds the detail; this page says where to look.

## ▶ STATUS 2026-11-10: resume here
Live work. Each line names the file that owns the current state, so read that file rather than trusting this summary.
- **Batch 7 reactions** (Drea, Melanin, John Legend, Brotherly Love, SPI): Affan recorded all five on 11-09, and they are being edited in ABW10, bin "Onyx batch 7 reactions (2026-11-09)". Owner: `projects/_onyx-batch7-2026-11/REACTIONS-RUN.md` ▶ STATUS (session "Onyx reactions batch 7").
- **Batch 7 samples** (Drea, Melanin, John Legend): review 1 applied 11-06, with him. Unanswered: Melanin's caption height, the grade, the IG rebuild, a song per sample. Owner: `projects/_onyx-batch7-2026-11/HANDOFF.md` § Questions.
- **Rise Above, the death row guard:** source pulled, waiting for his OK on sequence v4 and its 3 s voiceless last card. Owner: `projects/_onyx-batch7-2026-11/SEQUENCING.md` § 2 (the v4 block).
- **High Performance + Ron Spomer samples:** being built by another session since 11-09.
- **Not decided by him:** Remnant Radio and Barbell Logic (recommended drop). Unanswered yes: Mulligan Brothers asked 11-05 "Could you link the channel?". That reply belongs to the email session.
- **Organic @affancuts reels:** all six have his profile header and hook (11-08) and cleaned voice mixes. Next: his music track per reel, laid on the CLEANED mixes (`X:\Claude Projects\onyx-staging\organic-clean\`). Still open: is C1438 the 7th video, and does Short 5 need a real like-count screenshot?

## Where things live
| What | Where |
|---|---|
| Funnel procedure, batch mode, platform pick | `PLAYBOOK.md` (this folder) |
| Instagram-first look, kit lessons | `README.md`, `LESSONS.md` (this folder) |
| YouTube-first look ("Sean Ryan"), its kit and lessons | `presets/youtube-shorts/onyx-samples-youtube/` |
| IG neon-window look (used for both looks since 10-24) | `presets/instagram/neon-window/` |
| Prospect tracker, emails | `X:\Claude Projects\Hormozi Business\my-businesses\onyx-us-prospects.csv`, `onyx-email-log.csv`, `onyx-email-formats.md` |
| Moment selection engine | `X:\Claude Projects\Hormozi Business\my-businesses\onyx-shorts-engine\` + `projects/_onyx-batch3-2026-10/VIRAL-BAR.md` |
| Reaction standard | `projects/_onyx-batch6-2026-10/REACTIONS-V2.md` |
| Songs on samples | `projects/_onyx-batch5-2026-10/samples_music.py` (bed 14 LU under the voice) |
| Shared download / GPU locks | `bash projects/_onyx-batch2-2026-10/lock.sh <youtube\|gpu> <cmd>` |

## Job log
(Moved out of memory 2026-11-10. Dates are when it happened.)

**2026-10-04: started.** Onyx Influence emails US podcast hosts for permission to use one of their Shorts. A yes gets a sample Short (a better re-edit of a moment from their show) and Affan's reaction video to it, and both go back to the host with the ask. The email side worked (4 yeses from 32 delivered on 10-03), but nothing closes until the host sees the work. Pilot: `projects/mfm-nursery-rhymes/` (My First Million, the Moonbug story), fully automatic MP4 on the chat-only route by his yes, built by `hf-sample/build.py`, QA script `work/qa/onyx-sample-qa-r3.js`.

**2026-10-05: platform picks the look; batch mode.** Minimal card look = Instagram (pilot approved, only note: too few SFX). YouTube-first prospects get the "Sean Ryan" look, measured from the Shawn Ryan Show `KUMikP6a2eI` (`projects/_ref-yt-shorts-shawn-ryan-farm/analysis/`). Batch 1: Chris Do, Rich Roll, Jordan Harbinger, Rollo Tomassi, Pomp, Rob Dial (`projects/_onyx-batch-2026-10/BATCH.md`).

**2026-10-07: batch 1 review 2.** MFM perfect, don't touch. Chris Do → Sean Ryan style with the two people instead of B-roll. Harbinger, Pomp → full Sean Ryan. Rollo → keep the style, drop same-camera punch-ins and whips. Rob Dial → keep the IG look, fix the hook so a stranger cares who he is, audible SFX, white + colour captions, no clipped words. Rich Roll → re-pick a valuable moment, more motion graphics, crisp Epidemic SFX. Reactions Seq 33-35 (MFM, Chris Do, Rollo) prepared in ABW8; direction in `projects/_onyx-batch-2026-10/REACTIONS-BRIEF.md`, tools `reactions/tools/`.

**2026-10-08:** Harbinger, Pomp, Rich Roll (Bryan Johnson's five sleep rules) FINAL. Reactions Seq 37 (Pomp) + 38 (Rich Roll) prepared. Rob Dial v15 predates the SFX fix (a `--skip picture` rebuild was offered).

**2026-10-12/13: batch 2** (Jeremy Miner, Victor Antonio, Scott D. Clary, Jay Clouse): both looks per prospect from one clip, 8 samples built overnight, `projects/_onyx-batch2-2026-10/`. Reactions to Rob Dial + Harbinger, then the four batch-2 reactions, prepared in ABW8 with a different hero move each (`reactions/research-2026-10-13.md`).

**2026-10-14: batch 3** (Digital Social Hour, Smart Passive Income, Moonshots, Daniel Priestley, TFTC, Wellness + Wisdom), 12 samples, `projects/_onyx-batch3-2026-10/`. Batch-2 samples re-bedded with his tracks and copied to `G:\My Drive\Onyx Samples - Batch 2`.

**2026-10-15: Scott D. Clary signed as the first paying client** (one Short a day for Success Story). That work has its own home: `presets/youtube-shorts/scott-clary/`.

**2026-10-19:** batch 3 moved to fresh sessions (`_onyx-batch3-2026-10/HANDOFF.md`); batch 4 (MATG, Judy Cho, Stefanie Gass, Jon Krohn) picks in `_onyx-batch4-2026-10/`; his 5 batch-3 reactions prepared in ABW10 (`_onyx-batch3-2026-10/REACTIONS-RUN.md`), each ≤ 3:00.

**2026-10-20:** every email format tracked in `onyx-email-formats.md` + `onyx-email-log.csv` + `onyx_email_stats.py`. First email carries the subscriber-count credential only.

**2026-10-24: both looks for every yes** (YouTube Sean Ryan + IG neon window from one approved moment). Batch 5: Brad Lea, Fantasy Footballers (`_onyx-batch5-2026-10/`).

**2026-10-26:** the Onyx page becomes his personal brand page, @affancuts (planning in `Hormozi Business/my-businesses/onyx-organic-page-brief.md`).

**2026-10-27:** batch-5 reactions (Brad Lea, Fantasy Footballers, MATG) + his first @affancuts reel "Shorts cooked" prepared in ABW10 (`_onyx-batch5-2026-10/REACTIONS-RUN.md`). After review: v2s, which he then hand-trimmed himself. He picked songs for the samples: Real Slim Shady = Brad, Big Poppa = FF, Thelema = MATG (`Exports/<job>.<yt|ig>.music.mp4`). Never re-run apply.py over a hand-edited v2.

**2026-11-03: batch 6 delivered to Drive** (`G:\My Drive\Onyx Batch 3 Nov\`, 7 shows). Emails carry Drive links shared "Anyone with the link: Viewer" (ids in `_onyx-batch6-2026-10/drive-links.json`); Roofing went out with attachments before that was found. Josh Trent's follow-up became email format U1.

**2026-11-04/05: organic batch 1** (his own C1439-C1444, IG neon window, one a day): `projects/_onyx-organic-2026-11/<job>/RUN.md`, batch status in `SEQUENCING.md`. All six 60 fps finals in Exports as `affancuts-<job>-ig.final.mp4`; Short 1 also with the profile header experiment. Built as is, never answered: the made-up view counts on Shorts 2 and 4, Short 2's caption "reviews", whether the 0.3 s pause-cut rule applies. Flagged head jumps: Short 2 3.19 s, Short 3 14.18 s, Short 4 33.07 s.

**2026-11-05/06: batch 7** (heretics, On That Note, Melanin Money, Rise Above, Remnant Radio, Barbell Logic): `projects/_onyx-batch7-2026-11/`. Restructured samples: Drea de Matteo's Sopranos money story (a reroute from heretics' permitted Short), John Legend and Melanin restructured from the permitted Shorts, Rise Above rerouted to the death row guard after he rejected the pharmacy story. Review 1 (11-06): captions off George's lips, Scott format (hook below, captions from frame 1), POP grade tuned per source, applied by `review1.py` without rebuilding.

**2026-11-07:** check of tracker + email log + Gmail: reactions owed = 6 (the batch-7 three, death row once built, Brotherly Love, SPI); yeses with no sample = 6 (Ron Spomer, Rise Above, Barbell Logic, High Performance, Chase Hughes, Remnant Radio), ranking offered, not decided. Detail in `_onyx-batch7-2026-11/HANDOFF.md`.

**2026-11-08:** profile header + his hook on all six organic reels (Short 1 was already uploaded, so it was left as it was); voices cleaned with DeepFilterNet (`onyx-staging/organic-clean/`). The plain `-ig.final.mp4` files still have the room noise.

**2026-11-09:** batch-7 reactions recorded and in edit (see ▶ STATUS).
