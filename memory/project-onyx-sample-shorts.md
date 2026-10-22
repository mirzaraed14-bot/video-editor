---
name: project-onyx-sample-shorts
description: "Onyx Influence sales samples: a re-edited Short per podcast prospect plus Affan's reaction video; own minimal motion-graphics look in presets/youtube-shorts/onyx-samples/, NOT Abundance Wisdom"
metadata:
  node_type: memory
  type: project
  originSessionId: 4f6ff510-e01c-4ae4-a5c4-8388b194173e
  modified: 2026-10-11T23:49:03.135Z
---

Started 2026-10-04. Affan's agency Onyx Influence emails US podcast hosts for permission to use one of their Shorts.
When a host says yes, the video repo makes a **sample Short** (a better re-edit of a moment from their show) and
edits **Affan's reaction video** to it. Both go back to the host with the ask. The sample is the sales piece.

**Why:** the email side worked (4 yeses from 32 delivered on 2026-10-03), but nothing closes until the host
sees what the service would do for them. Affan wants the editing as automated as the email outreach was.

**How to apply:**
- Read `presets/youtube-shorts/onyx-samples/` (README = look v0, PLAYBOOK = funnel procedure, LESSONS) before any
  Onyx job. It is a NEW look Affan asked for: *"minimalistic yet visualistic with motion graphics"*. **No Abundance
  Wisdom mechanics** (no glow bars, flashes, Gretaros, head lock, grade preset).
- Shot grammar: FULL / CARD (the speaker morphs into a rounded rectangle with text above and below) / GRAPHIC / SPLIT,
  mixed in every clip (Affan picked "a good mix of all formats").
- **PLATFORM PICKS THE LOOK (Affan, 2026-10-05):** the minimal card look above = the INSTAGRAM look (approved on the pilot;
  only note: too few SFX in places). YouTube-first prospects get `presets/youtube-shorts/onyx-samples-youtube/` (v0, written
  2026-10-05, not yet built), measured frame by frame from his reference (Shawn Ryan Show `KUMikP6a2eI`; teardown, frame log
  and a 3-image board in `projects/_ref-yt-shorts-shawn-ryan-farm/analysis/`). That look: literal full-bleed B-roll for every
  noun (~53 % of runtime), speaker-top SPLITs, ONE whip-slide with mirrored edges (a numpy pass, not HyperFrames' `whip-pan`),
  Anton caps with a stretch pop and a colour wipe, caption colour = who is speaking, a 3 s hook title, the show's name as a
  watermark, a continuous music bed ≈ 13.6 LU under the voice with almost no SFX, −12 LUFS, a loop ending. Its PLAYBOOK holds
  only what differs; the funnel steps stay in the Instagram PLAYBOOK. § 0 there says how to decide the platform
  (permission-email platform, then both feeds' activity and views/followers, else ask).
- **BATCH MODE (Affan, 2026-10-05):** every YES gets one sample in its priority platform's look; Claude picks the moment
  (engine + AW Shorts ≥300K views); no storyboard approval, Affan reviews finished samples; the Instagram look must keep
  improving from Instagram references found in his Chrome each time; the YouTube look stays as built (improve only);
  downloads approved per batch with every file logged in the job BRIEF; Topaz Iris recipe on speaker footage. Batch 1
  (Chris Do, Rich Roll, Jordan Harbinger, Rollo Tomassi, Pomp, Rob Dial): `projects/_onyx-batch-2026-10/BATCH.md`.
  Rob Dial's team: credit Rob properly. Rollo: give him a shout-out. Shared PLAYBOOK "Batch mode" section.
- **The SFX note, answered by the reference:** it feels full with almost no SFX because of the bed; the pilot had no bed.
  Whether YouTube samples follow it exactly (bed + one sticker sound) is open question 1 for Affan (README § 11).
- Finish = **fully automatic MP4** on the chat-only route (HyperFrames + ffmpeg, talking-head-recut wrapper tweens).
  This was Affan's explicit yes on 2026-10-04, even though the machine's lane is premiere.
- Affan gives the moment (episode + timestamps); default when none = the same story as the Short named in the
  permission email, re-cut from the full episode. Storyboard approval before the build, until the style is locked.
- **Selection, sequencing and trimming = the Onyx podcast clips engine** at
  `X:\Claude Projects\Hormozi Business\my-businesses\onyx-shorts-engine\` (ENGINE · FINDINGS · RESULTS), adapted on
  2026-10-04 from the Abundance Wisdom Content Engine. Affan: *"the clips selection and sequencing and how the clips is
  trimmed is what matters."* Ranked angles first (angles.md), Affan picks, then storyboard. AW rules are HYPOTHESES there.
- The trigger and the tracker live in `X:\Claude Projects\Hormozi Business\my-businesses\onyx-us-prospects.csv` (status
  `YES - make video`). Pilot job: `projects/mfm-nursery-rhymes/` (My First Million, Moonbug story).
- **Pilot status (2026-10-05):** the MFM sample is FINAL at `projects/mfm-nursery-rhymes/outputs/mfm-nursery-rhymes.sample.final.mp4`
  (built by `hf-sample/build.py`, word-anchored; 3 multi-lens QA rounds, all fixes verified). It's waiting on Affan's taste review,
  his music-bed choice, then his reaction video. The QA workflow script to reuse is `projects/mfm-nursery-rhymes/work/qa/onyx-sample-qa-r3.js`.
- **Batch 1 review 2 (Affan, 2026-10-07)**, per prospect, in `projects/_onyx-batch-2026-10/BATCH.md`:
  **MFM is perfect: don't touch it.** "Sean Ryan style/format" = the YouTube look (`onyx-samples-youtube/`, measured from the Shawn
  Ryan reference). Chris Do → Sean Ryan style with the two people instead of B-roll overlays (few or none). Harbinger and Pomp → full
  Sean Ryan style (overlays, face split screens). Rollo → keep the style, drop the same-camera punch-ins and whips. Rob Dial → keep the
  Instagram look, fix the hook (a stranger must care who he is), add audible SFX, white+colour captions, no clipped words. Rich Roll →
  re-pick a VALUABLE (informational) moment, keep his minimal style but with more motion graphics (e.g. avatars acting out the story) and
  crisp Epidemic SFX. All: [[feedback-caption-punctuation]], [[feedback-captions-just-below-lips]] (constant), [[feedback-no-same-camera-punch-ins]],
  [[feedback-sfx-on-every-graphic]]. The hook must set up a stranger: who this is and why the story matters to THEM.
- **Podcast-source traps found on the pilot** (all in the preset's LESSONS.md): episode border frames, burned-in name labels,
  two-up layouts, WhisperX squeezing numbers and starting first words late, and the 24→30 fps frame mapping (`rframe()`).
Related: [[user-abundance-wisdom-editor]], [[feedback-long-term-self-improving]], [[feedback-youtube-sourcing]].


**Reaction videos (2026-10-07 night):** Affan's reactions to the samples are edited IN his ABW8 project: Seq 33 = MFM, 34 = Chris Do, 35 = Rollo. All three are prepared and verified; HE exports ([[feedback-affan-exports-himself]]). His Tella direction is resolved in `projects/_onyx-batch-2026-10/REACTIONS-BRIEF.md`:
- his split layout, face-only only on emphasis beats, instant punch-ins allowed (his rule for this format);
- zooms into the sample cropped to the panel;
- Bebas Neue white captions with no animation, on the seam (his onyxinfluence reel is the reference);
- a channel card on the intro, clean motion graphics with Epidemic SFX, a subtle Epidemic jazz bed, no grade.
The toolkit is `projects/_onyx-batch-2026-10/reactions/tools/`. Rob Dial's reaction is next, then delivery email drafts (Affan sends).

**2026-10-08: the three on hold are FINAL** in ~/Downloads, each through fresh-eyes QA rounds: Harbinger (Sean Ryan yt7), Pomp (Sean Ryan yt9), Rich Roll (new pick, Bryan Johnson's five sleep rules, Instagram v6). The kit fixes found on the way are in both presets' LESSONS.md:
- the caption rise was a no-op on left-aligned captions;
- the Epidemic files' lead-ins made pops land 0.6 s late (`ES_LEAD`);
- whooshes that mask a word are MOVED into a voice gap, never turned down;
- caption colour is checked by speaker embedding;
- patched 4K bases are cut by stream copy with output-side seeking.
Open: Rob Dial v15 predates the SFX fix; offer a `--skip picture` rebuild.

**2026-10-08 night: reaction Seq 37 (Pomp) + Seq 38 (Rich Roll) PREPARED** in ABW8, per his note "tighten a tiny bit (filler words) … same style … a bit more motion graphics with SFX".
- Filler cuts were made on HIS timeline, each one proven first.
- 22 / 25 graphics.
- Pipeline order: REACTIONS-BRIEF.md status.
- Seq 37's V1/V3 track outputs were off when he handed it over; left as he had them.
- Rob Dial's reaction is next, then the delivery email drafts.- Reaction channel cards use the creator's REAL YouTube profile picture (fetched og:image), never a freeze frame from the video (Affan, 2026-10-08, on Seq 38's Rich Roll card; swapped by changeMediaPath so his own edits stayed).
- **Batch 2 (2026-10-12): Jeremy Miner, Victor Antonio, Scott D. Clary, Jay Clouse** (`projects/_onyx-batch2-2026-10/BATCH.md`). Affan's call: EVERY prospect gets BOTH formats, an Instagram-look and a YouTube-look sample (8 samples), cut from ONE clip per prospect ("one clip, 2 formats": same moment, same cut, edited twice). Research first; he approves the bits and sequencing and gives creative direction per video before any edit.
- **Batch 2 APPROVED 2026-10-12**: all four picks (`PICKS.md`), 8 videos, section downloads approved, no Rural Sales Show credit. YouTube look = Sean Ryan format + [[feedback-split-screen-white-line]]; Instagram look = [[feedback-instagram-expensive-minimal]]. Check Sean Ryan's channel for anything new first.
- **2026-10-12 (overnight, Affan asleep): batch 2 BUILT.** All 8 samples final in ~/Downloads (`<job>.yt|ig.final.mp4`): Jeremy (Google $88K), Victor (marketing first), Vivian/Scott (casino, $5M), Jay/David Altizer (MrBeast train); 4 build agents + a v2 Instagram kit agent (letterbox window, animated captions, 9 refined graphic kinds, `kit/V2-HOWTO.md`), shared locks `_onyx-batch2-2026-10/lock.sh youtube|gpu`; fresh-eyes QA rounds. Reactions to Rob Dial + Harbinger samples PREPARED in ABW8 from his RAW recordings ("Rob Dial reaction", "Jordan Harbinger reaction"; new tools `reactions/tools/build_seq.py author.py pins.py seqmap.py switches.py dump.py`). Next: his review, his reactions to the batch-2 samples, delivery emails (he sends).
- **2026-10-13 (overnight): his 4 reactions to the batch-2 samples PREPARED in ABW8** ("Jeremy Miner reaction", "Victor Antonio reaction", "Scott D Clary reaction", "Jay Clouse reaction"), built from RAW C1354-C1357 + OBS, each with a different hero move per `reactions/research-2026-10-13.md` (wipe / side-by-side / loupes / editor's desk) and a new Epidemic bed; status in `_onyx-batch-2026-10/REACTIONS-BRIEF.md`; then save + quit Premiere + PC shutdown as he asked ([[feedback-shutdown-after-overnight-job]]). Next: his review of the 8 samples + 4 reactions, delivery emails (he sends).
- **2026-10-14: batch 3 = six YESes** (Digital Social Hour, Smart Passive Income, Moonshots, Daniel Priestley, TFTC, Wellness + Wisdom), both looks each (12 samples), downloads approved like last time; tracker `projects/_onyx-batch3-2026-10/BATCH.md`; research agents per `RESEARCH-BRIEF.md` + `STYLE-RESEARCH.md`; the sequencing goes to Affan as text before any edit ([[feedback-sequencing-before-edit]]). Same day: Jeremy/Scott/Jay samples re-bedded with his own tracks (Exports replaced) and all 8 batch-2 samples copied to Google Drive `My Drive/Onyx Samples - Batch 2` (G: is Google Drive for desktop).
- **2026-10-15: Scott D. Clary SIGNED as Onyx's first paying client** (one Short per day for Success Story). First job: research his Daniel Lubetzky (KIND) and Daymond John (FUBU) episodes for the strongest Shark Tank story (Affan ran a Shark Tank clips channel, 100M views/month), contenders first, no edit until he picks; work folder `projects/_client-scott-clary/`. On paid credits until Monday: lean, one agent, transcripts from the podcast RSS (YouTube still blocked).
- 2026-10-15: Scott's first Short = Affan's pick, Daymond's 50 FUBU shirts (his Tella walkthrough saved at `projects/_client-scott-clary/bombas/guide/guide.mp4`); handoff for a fresh, lean session: `projects/_client-scott-clary/HANDOFF.md`. This 2-day session was retired because every turn re-read its whole history (≈ $1+/turn on Fable).
- 2026-10-19: batch 3 moved to fresh sessions (one job each): start at `projects/_onyx-batch3-2026-10/HANDOFF.md` (6 samples in order, Topaz still open on all, then the 5 reactions via REACTIONS-LEAN.md).
- 2026-10-19: batch 4 = the 4 yeses with no sample (MATG, Judy Cho, Stefanie Gass, Jon Krohn): `projects/_onyx-batch4-2026-10/` PICKS.md (moments to verify) + HANDOFF.md (one fresh session per sample). YouTube transcripts do not load in Chrome either (same block); SDS publishes transcripts on its site; Buzzsprout (Judy) blocks scripted downloads with Cloudflare.
- 2026-10-20: every Onyx email format is tracked: `X:/Claude Projects/Hormozi Business/my-businesses/onyx-email-formats.md` (ids E1/B1/R1/S3/F1/F2/A1/O1…, Hormozi map, daily one-test-per-stage loop) + `onyx-email-log.csv` + `onyx_email_stats.py` → `onyx-email-stats.md`; the daily outreach task maintains them. First email = subscriber-count credential only (no Chris Do line, Affan 2026-10-20).
- **2026-10-19: his 5 reactions to the batch-3 samples PREPARED in ABW10** (bin "Onyx batch 3 reactions (2026-10-19)": TFTC, Wellness Wisdom, Moonshots, Daniel Priestley, Digital Social Hour reaction), built from RAW C1380-C1386 + 6 OBS files, every one ≤ 3:00 (his new cap: Instagram stops suggesting longer ones), one look column each (E-I); state + tools in `projects/_onyx-batch3-2026-10/REACTIONS-RUN.md`. He exports; his review not in yet. facex.py hits the leather chair: check face framing on every reaction ([[feedback-affan-exports-himself]]).
