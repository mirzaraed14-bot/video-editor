# RUN — gta6-travis-scott-hired

## ▶ STATUS: resume here (updated 2026-09-19)
**Next action:** none — SHIPPED. The creator exported and uploaded it themselves (2026-09-20). The learning pass is done: `POSTMORTEM.md` (what they kept, added and changed, measured), channel `LESSONS.md` + `PLAYBOOK.md` + `sfx.json` updated, and the zoom-RATE rule implemented in `transcript/plan-face-zooms.py` + `lanes/premiere/face-nests.py`.

| | | |
|---|---|---|
| format | long-form YouTube, **the GTA 6 EXPLAINER format** | probed: 1920x1080, 60000/1001 (59.94) |
| lane | Premiere 2025 (25.x) | ⚠️ the creator's LIVE project `ABW6.prproj`, bin **`GTA 6 Travis Scott`**, **`Sequence 20`** (id `47593b87-ec90-4579-86ca-825dc3701a4f`), not a job project. Every write is scoped to that bin and sequence |
| preset | `presets/youtube/affan-afterhours/` (channel) + the job's `STYLE.md` (explainer grammar, § 4b overrides) | house craft from `presets/youtube/default/`, recoloured navy `#12102A` / white / hot pink `#FF2E9A` |
| lane gaps | step 4 grade: Premiere 25.0 cannot run the scripted grade (manual recipe or skip, decided at step 4) · step 8 is the creator's · scripted `importFiles` failed mid-session in ABW6 on 2026-09-18 (lab-notes): watch the raw import | from LANES.md + lab-notes |
| source | camera `E:\Skool Recordings\5 Sept Batch\C1291.MP4` 1577.08 s, 59.94, PCM scratch · mic `TX01_MIC021_20260919_085416_orig.wav` (DJI Mic Mini 2S, 32-bit float mono 48k, 1508.56 s, peaks +7.2 dBFS on 52 transients) | both originals untouched at their own paths |
| constraints | none (the video makes no one-pass claim) | |
| started | 2026-09-19 | |

## Steps

| # | Step | Status | What it produced / why not |
|---|------|--------|----------------------------|
| 0 | Sequence | done | Sequence 20 was 60.00 fps against 59.94 footage: set to 59.94, timebase read back `4237833600` |
| 1 | Intake | done | `raw/gta6-travis-scott-synced.mov` (26:17.075, 94,530 frames) = the camera's video stream copied bit-for-bit + the DJI mic, drift-corrected, **PCM 32-bit float** (peaks +7.18 dBFS preserved). **Verified:** re-measured against the camera scratch, +0.1 ms at t=0, 0.4 ms drift end to end (0.03 frames) → `audio/sync/sync-verify.json`. `raw/originals/` = the mic original. The camera original is not copied (12 GB; the synced master carries its video bit-for-bit, as on Hot Coffee) |
| 2 | Rough cut | done → **re-cut by the creator** | **The creator's hand cut is now canonical (2026-09-19): 209 clips, 7:31.15** — `transcript/cuts.json` + `outputs/…transcript.json` rebuilt from the timeline (1,524 words; my rough cut kept as `*.roughcut-v1.json`); diff `transcript/handcut-diff.txt`; pacing lessons → channel LESSONS.md + PLAYBOOK § C row 2 · (my rough cut:)  **206 segments · 7:50.72** (69% of the mic take cut; median seg 2.05 s; 26.3 edit points/min) · decisions as data: `transcript/author-cuts.py` (take-map utterance numbers) → splice → polish → splice → `split-dead-air.py` (5 pauses 0.67–0.73 s split) → `review-fixes.py` (6 fresh-eyes fixes; 1 reviewer 'fix' REJECTED on the envelope) · dead-air gate **passed** on the final EDL · canonical `outputs/gta6-travis-scott-hired.transcript.json` · fresh eyes: `transcript/review-mechanical.md` + `review-flow.md` · **replayed onto Sequence 20: 206/206 on V1 and A1, zero gaps, every in/out exact to the EDL (readback), nothing on other tracks**, project saved |
| 3 | Audio polish | done | re-verified on the creator's cut: **209/209** A1 clips carry the chain (`--verify` exit 0) ·  `voice-gain.py`: kept speech −18.5 LUFS, true peak +5.2 dBFS → **+1 dB**; Amplify (mono Gain slider **+4 dB**, the −3 dB pan law given back) → Hard Limiter −6 dBFS on **206/206** A1 clips, every value read back, `--verify` exit 0, saved. Peaks land ~12 dB over the limiter (the DJI records hot) — flagged, not overridden |
| 4 | Color grade | **done by the creator** | an Adjustment Layer with Lumetri Color on **V3**, 0–480.2 s (read back 2026-09-19); graphics go ABOVE it. (Earlier:) **skipped** | (1) Premiere 25.0 cannot run the scripted grade (v45 donor); (2) this channel's V2 is reserved for the creator's colour mattes, so the default V2 grade layer collides; (3) the footage already measures **mean luma 0.618** (explainer target ≥ 0.33, 0 % dark frames) and the Autumn look is not in this format's spec. Manual recipe for the creator, V1 only: Lumetri → Creative > Look `assets/luts/rec709/Autumn-Rec709.cube`, Intensity 70, Saturation 115 |
| 5 | Graphics | **done** | **v2, from the creator's labels (current):** `graphics-plan.json` = 39 graphics, one per Mango/Brown/Violet block of `transcript/handcut-blocks.json` (ids b01…b75 = block index), built by `hf-graphics/author-plan-v2.py` (v1 kept as `graphics-plan.v1-mine.*`) · comps `hf-graphics/gfx/make_comps.py` (+ `fix_round1/2/3.py`, `fix_b58.py`) · **37/37 rendered and placed on V4 (b32, b48 skipped by the creator), `place-graphics.py --verify` ALL PLACED, frame-exact; V3 adjustment layer untouched (0–480.196)** · `graphics-qa.py`: 0 FAIL after the skip · 25 waived (`hf-graphics/qa-waivers.json`: the 16 Brown/Violet insets carry the channel's slow push at the timeline rate, not the house float/12 fps) · 51 warn, adjudicated: 19 tail trims of 2–5 hold frames (no comp has an exit; hard cut back to the face), 15 one-step leads, 13 dynamics (insets by spec; Mango b62/b73 sent to review), 2 parser false positives (a CSS comment read as a selector) · fixed from QA round 0: b08 "DEAL ✓" pop → slam (type never pops), b30 connectors shortened so the x1.10 overshoot clears them, b46 attribution em dash removed (source file + plan copy) · Higgsfield: **10 cr spent** (3 stills 6 cr + 2 upscales 4 cr) · **5c round 1** (3 Sonnet reviewers, 471 frames taken from the placed renders): 16 findings → **13 verified + fixed**
(b08 GTA 6 · b12 ½ Daft Punk · b14 offer leaves before the censor blocks · b16 slate clear of the slam · b20 full tag on
two lines · b24 Epic chip on the vault · b28 one pink keyword · b38 Nicki on 'Nicki' from the right · b40 marker strokes on
the producer's name · b46 'each scene' sweeps · b69 underline draws on + LOST 54 SONGS), **3 rejected** (b24 "frozen reel"
refuted by dense sampling; b56 "no pink": the cell asks for none; b40 box-through-text assertion: needs OCR); my own
re-check caught one regression (b20's full tag ran off the frame → two lines) · `fix_round4.py` + `fix_round4b.py` · swapped on V4, verify
ALL PLACED · targeted QA 0 FAIL · **round 2** (11 changed in full + a sheet of the rest): 2 findings, 1 refuted (b38 "rail missing": it is there), 1 verified — **b58** staging (Future stood on the Sony/Universal seam, Metro's crop edge floated): Travis + Future together on SONY, Metro on UNIVERSAL, Warner dimmed (`fix_round5.py`) · **round 3 (the cap)**: 2 findings, both verified, one root cause — b58's players DROPPED in from above and their flat chest-crop edges flew across the frame mid-fall → they RISE from below with no overshoot (`fix_round6.py`, b58-g); **targeted re-check CLEAN** · loop closed at the 3-round cap with every verified finding fixed and re-checked; the missing QA assertion (a cutout's crop edge inside the frame on any frame) is a spun-off task · final: `place-graphics.py --verify` ALL PLACED 37/37 on V4, `graphics-qa.py` exit 0 · (v1, superseded:) **5a done:** `graphics-plan.json` + `graphics-plan.md` (built by `hf-graphics/author-plan.py`, every edge anchored to a spoken word or snapped onto a V1 cut) · **52 graphics**: 33 full-frame (187.3 s = 39.8 %, face **60.2 %**, the format's ≥ 60 %) + 19 left-column panels beside the face (measured head zone x 80–500, `transcript/chin/`) · `validate-plan.py` **0 FAIL**, 3 expected warnings (no text animations by channel policy; full-frame > 25 % is the format; 9.3 s face stretches) · all 12 STYLE § 4.1 mechanism scenes + every surviving [ON SCREEN] beat placed · 5 stills (10 cr) · game: g02 18:40 aerial, g49 0:21.8 "Y'all know Booby?" (found by transcribing the Extended Look → `research/extended-look-transcript.txt`), g72 26:00 sunset · **5b blocked** on assets (see Next action) |
| 6 | SFX | **done** | **164 cues on A3–A5, `place-sfx.py --verify` ALL PLACED, 0 extra, levels read back**, saved · `workflows/sfx-plan.py` (channel map: A3–A5, −2 dB under house; the plan's `preset` now `presets/youtube/affan-afterhours`) + 15 hand rows (`hf-graphics/sfx-hand.json`: the quote-line rises of b22/b46 as one sound, b56's six photo pops, b58's three players arriving, b64's four milestones; b05/b18/b75 are still insets whose only motion is the push, their cut-in whoosh covers them) → `hf-graphics/sfx-snap.py` (the 29.97 audio floor hits `at` AND `src_in`: both + duration snapped; 21 cascade tails trimmed, 3 one-frame doublings dropped; original in `sfx-plan.unsnapped.json`) · a first placement drifted (6 in-points 30 ms early, 1 stray fragment) and was replaced whole by the snapped sheet ·  **bleep placed + verified:** `hf-graphics/sfx-bleep.json` (own cue sheet, job `assets/sfx/censor-beep.mp3`, 1 kHz) on **A6** 429.863 → 430.196 at −16 dB over the spoken "fuck" (envelope 429.90–430.17), A1 clip keyed 0 → −inf → −inf → 0 dB (429.853/429.863/430.196/430.206, read back); FCP XML backup first: `transcript/timeline-pre-sfx.xml` · the main cut sheet (A3–A5, channel −2 dB, `presets/youtube/affan-afterhours/sfx.json`; the plan's `preset` now points there) is written after the 5c loop dries |
| 7 | Review | **done — the creator reviewed, finished and uploaded** | Sequence 20 ready to watch: V1 209 face clips (= `cuts.json`, 451.151 s) · V3 the creator's grade · V4 37 graphics · A1 voice (chain 209/209) · A3–A5 164 SFX · A6 the bleep. Waiting on the creator |
| 8 | Export | **done by the creator** | They exported and uploaded (thumbnail + title theirs). The pipeline never rendered: on this lane step 8 was theirs. Shipped length **7:39 (459.31 s)** — my 7:31 plus their 8.1 s interview insert |

## The sync (measured, `audio/sync/sync.json`)
- The mic started **+44.904 s after** the camera; the DJI clock runs **−11.7 ppm** against the camera =
  **−17.3 ms (1.04 frames) over the take**, so the mic is resampled to hold sync end to end.
- 25 GCC-PHAT windows of 30 s, **scatter ±0.1 ms** around the fit.
- The mic covers camera 44.9 → 1553.5 s. Outside it the camera scratch is room tone (−46 dB) and two
  clicks, no speech, so nothing is lost.
- Camera scratch kept as `audio/sync/camscratch-16k.wav`.

## Request coverage
- **"sync the TX01 DJI Mic Mini 2S 32-bit float recording"** → intake; the camera audio never reaches the timeline. Evidence: `audio/sync/sync.json` + the post-mux re-measure.
- **"start the edit"** → the eight steps on Sequence 20.
- **The creator's labels (2026-09-19): "Mango = motion graphic · Brown = actual overlay from Google/Instagram or actual
  footage (enhanced in Higgsfield so it looks crisp) · Violet = Higgsfield still"** → one graphic per labelled block,
  39 labelled, 37 built; evidence = `place-graphics.py --verify` (37 placed). b32 + b48 skipped by the creator (Flags).
- **"analyze how I make cuts … the pacing should be very similar in the next video"** → `presets/youtube/affan-afterhours/LESSONS.md`
  (THE CREATOR'S HAND PASS ON THE CUT) + `PLAYBOOK.md` § C row 2. The creator's cut is not re-cut here.
- From BRIEF.md: opens on the face · the `[ON SCREEN]` posters · the 12 mechanism scenes with PNG puppets · stills at 85–90 over a dark grained matte · Extended Look footage zoomed out over the matte · the four words censored, never spoken · the face grammar (nest, cut zoom +25, gradual 100→110) is the creator's or handed back nested.

## Flags to report
- **Six pauses of 0.65 s or more in the creator's own cut** (dead-air gate, `transcript/dead-air-qa.json`; theirs, not changed): 65.64–67.12 (**1.48 s**, "…thing I found | two days of…") · 131.28 (0.73) · 181.71 (0.97) · 263.01 + 263.86 (0.68 + 0.88, one clip: "not GTA but | … | like it's literally") · 430.28 (0.69, after the bleep).
- **Face zooms DONE on the creator's ask (2026-09-19), their grammar:** 38 face runs nested (`Face nest 01…38`, bin `GTA 6 Travis Scott/Face nests`, labelled Iris), each with Motion > Scale 100 → 110 across the run; inside, 37 cut zooms (an instant 100 → 125 hold-key snap on the landing clause, 0.4–2.2 s); 4 runs ramp-only (reasons in `transcript/face-zooms.json`). `lanes/premiere/face-nests.py --verify` 38/38 · V1 209 → 107 clips · A1 209 + chain 209/209 · V4 37/37 · SFX 164/164 · bleep 1/1. Undo: the clone `Sequence 20 (backup before face zooms)` or `transcript/timeline-pre-nest.xml`. The picks are editorial: the creator's review corrects them.
- **No mix bounce was measured** (Premiere lane, no flat render; A2's music is empty right now): check the master peak on the export.
- **b32 and b48 are SKIPPED by the creator (2026-09-19):** b32 (the Discogs "appears courtesy of" credit) they place by hand
  later; b48 (the RHYNO post) cannot exist — Travis posted only a TEASER for RHYNO. FACTS F2 corrected; the spoken line
  "He wrote it was recorded live at the JOH" (283 s) stays, but whether the teaser caption says that is UNCONFIRMED.
- **The creator's cut keeps a spoken "fuck" in b73's window (~429.96–430.20):** bleeped at step 6, not cut.
- **A2 read EMPTY on 2026-09-19 18:0x** (it held the creator's music earlier); nothing of mine touched it.
- **Photo licences need a description credit:** paste block in `assets/SOURCES.md`.
- **Evidence frames come from the placed renders**, not the program monitor: the bridge `frame` grab fails on Premiere 25 /
  Windows. Valid because every graphic is an opaque full-screen on the top track (the grade sits under it).
- **Two bugs fixed in `workflows/sync-dual-audio.py` today.** (1) Its fine stage correlated the two windows'
  hard EDGES under the phase transform, so 12 of 25 windows returned exactly the coarse offset and the fit
  reported half the real drift. Fixed with a Tukey taper. (2) Its drift correction used `asetrate=48000*1.0000117`,
  which ffmpeg rounds to 48001 (20.8 ppm for an 11.7 ppm drift); fixed by oversampling 20× before the rate change.
  Added `--audio-codec` so a float recorder can stay PCM.
- **Two Windows bugs fixed in `rough-cut/scripts/polish-boundaries.py`:** (1) a hard-coded `/tmp` resolved to `E:\tmp` in
  Windows Python, so the polished EDL was written where splice never reads it; now resolved via `cygpath -w /tmp`.
  (2) its staleness guard allowed 5 s between refine and the persisted EDL; the snap took 9.8 s here, so every run read
  as stale. It now recognises splice's own byte-identical write. The clipper has the same /tmp bug (spun off as a task).
- **The polish's decay detector clipped 4 word endings and its long-span rule chopped "internet"** — found and fixed by
  the fresh-eyes pass (§ Review fixes). A word-final fricative/nasal sits under its threshold; worth a tool fix later.
- **The creator's ABW6.prproj lives inside a nested Premiere Auto-Save folder** (`E:\Premiere Pro Exports\Adobe Premiere
  Pro Auto-Save\…×6\ABW6.prproj`). Premiere prunes that folder; worth a Save As somewhere permanent.
- Shot at 59.94 fps again (the playbook's 23.976 is a doc-format spec).

## Review fixes (step 2, fresh eyes on Sonnet, adjudicated)
- Chopped word endings restored: "internet" (seg 4), "dollars" of $250,000 (seg 90), "grand" (7.5 grand), "exposure" (think of the exposure). Cause: the polish's decay detector ends a word where energy first drops below its threshold, so a word-final fricative/nasal gets clipped; and its long-span rule took the in-word dip of "inter|net" as a word end.
- A false start deleted: "Nicki Minaj-" (758.55–759.40) had survived as a 0.43 s fragment before the full take.
- "He got the call": the in-point shaved the /h/; moved to 848.72.
- REJECTED: extending "once" (the reviewer read a fictional words.json span; the extension pulled in a false-start "because-"). Heard, measured, reverted.
- Cleared as ASR hallucinations (checked on the envelope): "and this is the and this is literally…", other doubled words the reviewer listed.

## Cut decisions to report (the creator can reverse any with one word)
- **Cold open follows the creator's REDO** ("we're going to redo this actually", 3:05): take 1's "Nobody called Travis Scott. That's not a joke." (the thumbnail line) is OUT; the redo's "nobody has explained on the internet… how does Rockstar reach out to Travis Scott… Strauss Zelnick isn't ringing up Travis Scott" is IN, trimmed of its echoes and signposts.
- **Martyn Ware: "every song has two owners… they split it in half" CUT** (FACTS H4: wrong). The offer line uses the last full take + take 1's "Once. Forever." (only take 1 says it).
- **The four words were SPOKEN on the take; cut.** "His reply was, — I'm not reading that out, it's on screen" stays; the censored card covers it at step 5.
- **"11 days ago" cut** (Sept 15 is 4 days before the record date); the creator's own "just a couple of days ago" kept.
- Not recorded on the day (so not in the cut): "Once I worked out how this happens I couldn't unsee it", "two years… not one person leaked it", "picture paying ten years of rent in one go", "you can't lose a song you own, there's no landlord".

## Transcript repair (2026-09-19)
- `transcript/words.json` had the Martyn Ware offer region collapsed (9 words in 2 s at the wrong take); replaced with
  slice-re-ASR + envelope timings (each fixed word carries `"fixed"`; the original is `transcript/words.before-offer-fix.json`).
  The canonical transcript now has "The offer was $7,500. Once. Forever." at 409.12–412.4.

## Skipped, and why
- Step 4 grade: see the step table (tool gap on 25.0 + V2 reserved for mattes + footage already bright). Recipe handed over.
