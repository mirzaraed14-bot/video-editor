# Onyx sample Shorts: THE PROCEDURE

From a host's "yes" to a finished sample Short plus Affan's reaction video, ready to email.
Numbers and look: [README.md](README.md). Lessons: [LESSONS.md](LESSONS.md).

## Where this sits in the funnel

```
permission email ──> host says yes ──> SAMPLE SHORT (this preset) ──> Affan's REACTION video ──> reply email with the ask
   (Hormozi Business outreach)          │                                  │                          (Hormozi Business outreach)
                                         └─ projects/<job>/                └─ projects/<job>/reaction/
```

The outreach side (prospects, permission emails, replies, the ask) lives in
`X:\Claude Projects\Hormozi Business\my-businesses\` (`onyx-us-prospects.csv`, `onyx-email-automation-handoff.md`).
A row with status **`YES - make video`** there is the trigger for a job here.

## Division of labour (agreed 2026-10-04)

| Stage | Owner |
|---|---|
| Pick the moment (episode + rough timestamps) | **Affan**: *"my job will be to give you the part you need to actually edit."* When no part is given, Claude proposes one (§ 1) and Affan confirms. |
| Style direction and review of the sample | **Affan** (together with Claude) |
| Recording the reaction video | **Affan** |
| Everything else: sourcing, transcript, cut, storyboard, assets, build, render, reaction edit, drafting the delivery email | **Claude** |

## Batch mode: the standing workflow (Affan, 2026-10-05)

When there are several YESes, they run as a batch (batch 1: `projects/_onyx-batch-2026-10/BATCH.md`, the tracker and resume
point). Affan's instructions for it:
- **One sample per prospect for now**, in the look of their priority platform (§ 0). Two per prospect (one per platform) only
  if Affan says so after the batch.
- **Claude picks the moment** ("go on to their podcasts, figure out the best moments yourself"), with the Onyx clips engine
  and Affan's Abundance Wisdom fundamentals (study AW's Shorts above 300K views; `onyx-shorts-engine/AW-VIRAL-STUDY.md`).
  "The clip selection is what makes a video; the editing is the sauce on the steak."
- **No storyboard approval in batch mode**: Affan reviews the finished samples.
- **Instagram look keeps evolving**: before every Instagram-first build, look on Instagram (Claude in Chrome, his own browser)
  for accounts doing the minimal motion-graphics style better than us, take what works, and log it in this preset's
  LESSONS. Never ship the same look twice by habit.
- **YouTube look**: keep the MFM-built style for batch 1 and only improve it (`onyx-samples-youtube/`).
- **Downloads are approved per batch** (candidate audio, their Shorts, the chosen section, B-roll, one music track); every
  file is logged in its job's BRIEF (name, source, size) before it is pulled.
- **Transcripts:** YouTube refuses caption downloads from this machine (HTTP 429), so research pulls only the candidate
  sections' AUDIO and transcribes them locally, one at a time on the GPU.
- **Topaz on the speaker footage of every sample** (Affan, 2026-10-06: "still do topaz because it makes the footage very smooth; if the
  quality difference isn't there don't enhance but apply interpolation"): his frame interpolation (Chronos, replace duplicate
  frames) ALWAYS, per take (`--segments` at every joint and camera cut); his Iris enhancement only where it shows (≤1080p
  sources, `--out-scale 2`). A native-4K source gets `--no-enhance --no-stab` (Iris softened Rob Dial's 4K beard and flattened
  its contrast at phone size; the stabiliser shifted a tripod frame). Point `base_hq` (and FIT insets of the speaker that are
  not text) at the result.
- When the batch is done, tell Affan.

## 0. Pick the platform first (Affan, 2026-10-05)

Every sample is built for the prospect's **priority platform**, and the platform picks the preset:
- **YouTube-first** → `presets/youtube-shorts/onyx-samples-youtube/` (maximal B-roll storytelling, from the Shawn Ryan reference).
- **Instagram-first** → this folder's README (the minimal motion-graphics look).

How to decide (write the answer and the evidence in BRIEF.md):
1. Where did the permission email point? A YouTube Short named in the email → start from YouTube.
2. Compare the show's two Shorts feeds: posting frequency over the last 30 days, and median views ÷ followers on each
   (YouTube Shorts tab vs Instagram Reels). The platform with the stronger and more active feed is the priority.
3. If they're close, or the show barely posts on one, ask Affan in one line. Never guess silently.

## The line, per job

**Job folder:** `projects/<show>-<topic>/` (e.g. `mfm-nursery-rhymes`). `BRIEF.md` with a ▶ STATUS block, rewritten at
every milestone. `reference/` holds the show's own Shorts (the one named in the permission email, plus any of their
past hits on the same topic). `raw/` holds only the source section we cut from.

### 1. Find and pull the source
1. Start from the Short named in the permission email (the tracker's "Short named in email" column). Download it to
   `reference/` (yt-dlp, forced H.264: `-f "bv*[vcodec^=avc1]+ba[ext=m4a]/b[vcodec^=avc1]"`) and transcribe it.
2. Find the full episode it was cut from: the channel's search (`/@<channel>/search?query=<keyword>`), then the
   episode's chapters. Also note any **earlier Short by the same show on the same story**, with views. A big
   gap between them is the strongest line in the reaction video.
3. Download **only the section needed** (`--download-sections "*<start>-<end>"`, H.264, ≤1080p) to `raw/`.
   **Then normalise its time zero** (rough-cut SKILL § Gotchas, 2026-10-06): a section download starts the audio 0.05–4.9 s
   after the video, and every cut lands that much early. `ffmpeg -i dl.mkv -map 0:v:0 -c:v copy -map 0:a:0 -af
   "aresample=async=1:first_pts=0" -c:a flac raw/<name>.mkv`, the download kept in `work/raw-orig/`. Prefer the best
   available resolution (4K when offered): a 9:16 crop of 4K needs no upscale (Iris only for ≤1080p sources; interpolation on every source, § Topaz above).
4. **Default moment** when Affan gives none: the same story as their Short, re-cut from the full episode. Same
   content side by side is the cleanest comparison, and it's exactly what the permission email asked to use.

### 2. Transcript, angles and cut: SELECTION, SEQUENCING AND TRIMMING
**The method lives in the Onyx podcast clips engine: `X:\Claude Projects\Hormozi Business\my-businesses\onyx-shorts-engine\`
(ENGINE · FINDINGS · RESULTS), adapted from Affan's Abundance Wisdom Content Engine.** Affan, 2026-10-04: *"the clips
selection and sequencing and how the clips is trimmed is what matters."* Read all three files before this step.
1. `transcribe.sh projects/<job>` (add `--diarize` when two or more people talk, so FULL shots know whose face to frame).
2. Read the WHOLE transcript, then write **ranked angles** in `projects/<job>/angles.md` (ENGINE § 10). **Affan picks one.**
3. Cut the picked angle by ENGINE §§ 4–6: draft at 1.5–2× target, then cut 40–60 %; enter on the strongest word, exit on the
   button word; join sentences within one answer, never splice mid-thought.
4. Use the rough-cut engine for the splice and the static audio chain (the same one every job uses).
5. Lock the predictions in the engine's RESULTS.md before the sample is sent.

### 3. Storyboard (the gate before building)
`projects/<job>/storyboard.md`: one row per beat, giving **time · words · MODE (FULL / CARD / GRAPHIC / SPLIT) ·
kicker · bottom line · the graphic, described**. It's checked against the README § 3 rhythm rules. **On the pilot and
until the style is locked, Affan approves the storyboard before the build.** That's a 2-minute read and far cheaper
than a re-render.

### 4. Assets
Logos, photos and screenshots the storyboard names: fetched, checked at full size, enhanced if soft. They go in
`projects/<job>/assets/` with the source noted in BRIEF.md. The accent colour is sampled from the show's
branding and written into BRIEF.md.

### 5. Build and render (chat-only route)
- **FULL framing:** face-tracked 9:16 crop of whoever is talking (`workflows/face-frame.py`; per-speaker boxes
  when diarized).
- **Composition:** HyperFrames, the `talking-head-recut` mechanics. The source video sits in a wrapper that
  tweens between layouts (full-bleed ↔ card ↔ bubble ↔ split); cards and graphics are timed to word timestamps.
- Captions per README § 5, SFX per § 6, music bed if used.
- Render to `outputs/<job>.final.mp4`, plus a copy in `~/Downloads/`.

### 5b. Before writing the composition (learned on the pilot)
- **Scan the base cut for the episode's own layouts**: a border around the whole episode (row/column brightness), burned-in
  name labels (measure where they end; set the per-mode inner zoom so every window crops them), two-up spans (top-band luma
  per frame) and full-screen chart inserts. Crop the border off the base (`crop` + scale, CRF 14) and give a two-up span a
  CARD16 that crops into the speaker's box.
- **Verify every number's real audio end** (a second ASR on the slice plus the RMS envelope) before trusting its WhisperX
  stamp. Patch bad stamps in build.py.
- **Generate the composition from `build.py`** (pattern: `projects/mfm-nursery-rhymes/hf-sample/build.py` v2): every time
  anchored to words, splice joints and measured camera cuts; `python build.py` → `npx hyperframes@0.8.16 check` →
  snapshot the risky moments → render.

### 6. Self-check, then Affan's review
Before Affan sees it: run the **multi-lens QA workflow** (captions · framing · motion and render integrity · audio · on-screen
facts), with every reported defect sent to a skeptic who tries to refute it (script:
`projects/mfm-nursery-rhymes/work/qa/onyx-sample-qa-r2.js`; point it at the new render). Fix the confirmed defects,
re-render, and re-run until a round finds zero objective defects (cap: 3 rounds; the repo's edit-review rule). Defects only,
never taste. Then Affan reviews for taste. Re-render only what changed. Every note goes into LESSONS.md the same turn.

### 7. The reaction video (`projects/<job>/reaction/`)
Affan records himself reacting: their current Short, their best past Short if there is one, then our sample.
He explains what's working and what could go further. Claude edits it: cuts dead air, lays their Short and our
sample on screen where he talks about them, adds light captions or callouts, and renders. (The layout is
decided on the first one; see LESSONS.)

### 8. Delivery
Claude drafts the reply in the host's email thread (Hormozi Business outreach), using the delivery script in
`onyx-email-automation-handoff.md`: the link and the time it took, then the ask. **Affan sends it.** Then update the
tracker row.

## Speed target

A sample has to keep up with the yeses (about 4 a day in batch 1). Target: **under 15 minutes of Affan's time per
prospect** (pick the moment, approve the storyboard, review the sample, record the reaction). Everything else runs
without him.
