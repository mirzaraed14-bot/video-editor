# RUN — kick-fake-viewers (AffanWiz CA-003 · ABW8 · Sequence 27)

## ▶ STATUS: resume here (2026-10-13) — RESTYLE TO THE IGN-MISSIONS STYLE: DONE, SAVED, awaiting the creator's review
The creator (2026-10-13): analyse Afterhours video 22 ("GTA 6 Just Got A Whole Lot More Interesting…", job
`gta6-ign-missions`, Sequence 39) frame by frame and turn Sequence 27 into THAT style — overlays, editing, SFX, everything.
Spec written: `presets/youtube/affanwiz/STYLE.md` v2 (+ evidence `presets/youtube/affanwiz/reference/ign-missions/`).
Backup before any write: `premiere-backup/ABW8-before-ign-style-2026-10-13.prproj` (+ Seq 27 readbacks beside it).
Sequence 27 had not changed since 10-04 except **A2 muted by the creator** (the Adin clip's audio): left muted, flagged.

Done on Sequence 27 (all by sequence NAME; the three active-sequence windows used the shared lock and restored Sequence 51):
- **Face pass** (`transcript/face-pass.py`, word-anchored): 54 entries = 52 cut zooms (median 135 %, p25–p75 130–140,
  14 big hits re-centred on a measured face, one 250 % on "What the fuck") + 2 stretch gags ("soul is intact" 380 %,
  "God forbid" 300 %); 48 V1 razors (121 → 169 clips), A1 untouched; `--verify` 0 mismatches.
- **Graphics plan** (`build-plan.py` → `graphics-plan.json`): 24 beats, 3.7/min, face 53 %, longest face-less run 12 s.
- **Plates + b-roll** (`hf-graphics/gfx/build-plates.py`) on **V2**: 24/24 placed frame-exact (`hf-graphics/place-gfx.py`).
- **Overlays** (`hf-graphics/gfx/build-comps.py`, HyperFrames alpha ProRes 4444 at 60 fps) on **V3**: 21/21 rendered + placed frame-exact.
- **SFX** (`hf-graphics/place-sfx.py`): 76/76 cues on A3/A4 at the reference's levels, 0 extra.
- **Music** (`transcript/place-music.py`): 7 beds on a new **A5** (Loungin −20 · First Born −24 with a hole for the Adin clip ·
  Take a Ride −25 · Brooklyn −24 · Loungin −23 · Take a Ride −23), then `lanes/premiere/music-dropouts.py --music-track 5`:
  41 zoom ranges lifted, 0 music under a zoom; `--verify` 0 problems.
- Old raw asset layer (20 V2 clips from 10-04) removed (`place-gfx.py --clear-raw`); the Adin audio stays on A2.
- **Verified:** `place-gfx.py --verify` 45/45 rows · `review/gate-frames.py` 15 graphics runs, 21 overlays, 170 V1 cuts,
  0 problems · face-pass `--verify` 0 mismatches · SFX 76/76 · music-dropouts `--verify` 0 problems · offline composites
  (`review/composite-check.py`, sheet `review/frames/sheet.jpg`) show every layer stacked right. g03's plate (KM@15 showed
  N3on's channel page with a legible business email) re-sourced to KM@140 → `g03-plate-v2.mp4`.
- **Final layout:** V1 169 face clips (zooms) · V2 24 plates/b-roll · V3 21 overlays · A1 121 voice · A2 Adin audio (muted
  by the creator) · A3 64 + A4 12 SFX · A5 43 music pieces. Saved; NOT exported (the creator exports).
NEXT: the creator's review (step 7) → read the diffs (`place-gfx.py`, `place-sfx.py --diff`, V1) → LESSONS.
Left for him: 0.8x slow-downs ("What the fuck", "soul is intact", "God forbid"), A2 mute (Adin's own audio is unheard
while muted), the legal flags below.

---

## ▶ (earlier) STATUS (2026-10-04)
**ROUGH CUT + ASSETS ON SEQUENCE 27, VOICE CHAIN ON, SAVED. Next: the creator's pass, then the STYLE.md finish.**
- **V1/A1:** the rough cut, 121 clips, 6:10 of speech (+ a 16.9 s gap) = **6:26.4**, replayed onto Sequence 27 itself
  (the creator's single C1327 handover clip removed). `diff-edl`: 0 deleted, 0 boundary moves vs `transcript/cuts.json`.
  Joints ~2 frames out / ~1 frame in (creator's spec). A1 voice chain: +0 dB (kept speech already −16.6 LUFS) into the
  −6 dBFS Hard Limiter, 121/121 verified (`audio-polish.py --verify`).
- **The Adin clip** sits in the gap on **V2/A2, 0:56.3–1:13.2** (source 0.30–17.20: "everybody's inflated… I openly
  admit it… 90% of streamers inflate"), right after "Listen to exactly what he says." Its own audio plays.
- **V2: 19 gathered assets, RAW** (fit to frame, no frame/matte/shadow yet), each under the words it illustrates
  (`review/asset-placement.json`), their own audio removed. Bin: `PBE Video NEON / CA-003 assets` (27 items: 7 clips,
  20 stills). Sources, usable spans and flags: `assets/SOURCES.md`.
- Program-output proof (Premiere PNG renders): `review/proof/f0020…f1880.png`, sheet `review/proof-sheet.jpg`.
- Backup before anything touched Sequence 27: `premiere-backup/ABW8-before-rough-cut.prproj`.

| | | |
|---|---|---|
| channel | **AffanWiz** (`presets/youtube/affanwiz/`; STYLE.md is the finish for this video) | episode CA-003, `brief/` = script + research |
| format | long-form YouTube 16:9, camera 1920x1080 59.94, Sequence 27 at 60 fps | |
| raw | `X:\Recordings\PBE\C1327.MP4` (7.6 GB, 16:32, PCM = the voice) → `raw/C1327.MP4` | "no need to sync, it's already synced": the camera clip carries the voice |
| constraints | keep improvised bits natural; tight joints; last take of repeats; gather every asset the script names and put it in the sequence | creator, 2026-10-04 |

## How it is built (re-runnable, in order)
`uv run transcript/build-cuts.py` (KEEP word ranges + 10 measured P rows; envelope-quiet splits ≥ 0.40 s) →
`RENDER=0 splice.sh` → `POLISH_TAIL_MS=33 POLISH_LEAD_MS=17 polish-boundaries.py` → `python transcript/fixes.py`
(25 fixes from the mechanical review + 1 kill) → `RENDER=0 splice.sh` → `dead-air-qa.py` (PASSED) →
`review/tools/replay-gap.py --apply` (refuses unless V2–V3/A2–A4 are empty) → `audio-polish.py --apply` →
`review/tools/place-assets.py --apply` (skips placed slots) → fit-to-frame scale (scratch `fitscale.jsx`, Motion Scale =
min(1920/w, 1080/h)) → `review/tools/proof-frames.py <t…>`.
Reviews: `review/flow-review.md` (clean; 3 judgment calls kept by the last-take rule), `review/mechanical-review.md`
(13 warnings adjudicated: 7 real + fixed, 6 false alarms; 9 click heads + 3 loose joints fixed).

## What the take is (vs the script)
- **No cold open and no close were filmed**: the take starts at § 2 ("September 2024…") and ends on the plug. The cut
  opens on "September 2024" over the Dexerto headline.
- A **phone call** at 0:24–1:18 of the raw: cut.
- Retakes collapsed to the last take (the September line ×3, QueenGloria ×4, "dropped dropped", "and to be clear" ×2,
  "Bots can" ×2, the plug ×3 …); 6 of them were invisible to WhisperX (per-burst pass + slice re-ASR).
- **Moved:** "Bots can be sent to you by anyone." → after "That doesn't mean they bought anything." (its script place).
- Kept natural: "ladies and gentlemen", "What the fuck", "I make $1000 on my short… my soul is intact", the whole
  advice section, "this info isn't niche… normal people know about this shit", the full plug and "Peace."

## Flags for the creator
- Cold open / close not in the take (script § 1 and § 7).
- **Legal list:** "Asmongold dropped up to 20%" is said without "reportedly" (needs on-screen "reportedly" or a pickup).
  "Kick and Stake are both owned by the same companies" (last take) vs "the same company" (earlier take, the only one
  that calls Stake "the casino"). QueenGloria's line (last take) never names her: the clip on screen does.
- **The Adin clip has offensive chat text top-right** (a slur in a username, "shut up j…"), visible at fit-to-frame:
  crop to Adin when styling. A slur is spoken at 23.6 s of the source: the placed span stops at 17.2 s.
- "People just don't wanna be honest about it" (the script's second Adin quote) is NOT in the downloaded clip; the line
  "and calls it the thing that people don't want to be honest about" refers to it.
- N3on's Dec 2023 identical-message chat clip was not findable; the 360p Kameron footage stands in (another creator's
  commentary video). No "60,000 watching" corner-counter clip either: Kick's live Browse page stands in.
- Profanity: "What the fuck", "Oh, shit", "this shit", "and shit".

## Request coverage
- "do the rough cut first" → onto Sequence 27 itself, frame-exact. ✔
- "improvised bits… keep it natural" → only retakes/stumbles/dead air cut. ✔
- "two frames at the end of the first block and one at the next" → polish 33/17 ms, 25 edges hand-fixed. ✔
- "find all the relevant information… overlays, video links, reference post articles… use Claude in Chrome… put it
  inside of the sequence" → 27 assets in the bin, 19 placed on V2 + the Adin clip in its own gap. ✔ (2 not findable, flagged)
- "no need to sync the audio" → none done. ✔
- "notify me" → done at the end of the run.
