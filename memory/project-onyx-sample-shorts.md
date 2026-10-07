---
name: project-onyx-sample-shorts
description: "Onyx Influence sales samples: a re-edited Short per podcast prospect plus Affan's reaction video; own minimal motion-graphics look in presets/youtube-shorts/onyx-samples/, NOT Abundance Wisdom"
metadata:
  node_type: memory
  type: project
  originSessionId: 4f6ff510-e01c-4ae4-a5c4-8388b194173e
  modified: 2026-10-07T17:46:48.659Z
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