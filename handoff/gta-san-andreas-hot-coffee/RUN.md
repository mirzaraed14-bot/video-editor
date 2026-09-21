# RUN - gta-san-andreas-hot-coffee

## ▶ STATUS: SHIPPED. Uploaded by the creator 2026-09-18 (with their own export and thumbnail).

**The post-mortem is written: [`POSTMORTEM.md`](POSTMORTEM.md)** — the creator's grammar measured off the
timeline (labels, shares, rhythm, punch-ins, nesting, the three-layer overlay frame, music cue sheet),
the picture measured, the credit spend and waste, every tool bug, and what the creator changed by hand
after the pipeline's passes. Its durable rules are folded into `presets/youtube/affan-afterhours/`
(`PLAYBOOK.md` § 0, `README.md` § 1–§ 2, `LESSONS.md`) and `lanes/premiere/lab-notes.md`.
`transcript/parse_fcpxml.py` reads any future FCP XML export; `transcript/timeline-final.dom.json` is
the final timeline as read from the live DOM (the XML export of Sequence 12 hangs).

Still the creator's call: `n1` at scale 96; three narration date errors; the grade; three Forest blocks.

## (superseded) the Mango block is filled and the whole film is sounded

### The missing motion graphic (2026-09-17)
**m6** on **V6, 628.111 → 632.215** (10:28.11), the creator's empty Mango block. Take-Two's cancelled
game *Snow*: the box, the strike, CANCELLED / 6 JUNE 2006 / NO REASON GIVEN (FACTS.md **C9**,
VERIFIED — the Hot Coffee link is press inference, so the card never asserts one). **Scale 100**,
matching the creator's 36 other graphics; the 96 edge-bleed is a Higgsfield-overlay look, not a
graphic one. Proved on the program monitor (`outputs/frames/f0063020.png`).

### The sound pass
**104 cues placed, every one verified against the timeline.**
- **59 overlay cues** — 30 ambience beds on **A6** (new), 8 machine-hum layers on **A7** (new),
  26 diegetic spots on A5. Environments read off a frame pulled from each of the 51 unique overlays.
- **45 graphics cues** — the ten that had NO sound at all (m1–m6, n1, u1, d1, r1), in the same
  vocabulary as the existing 122.
- **16 cues dropped** as duplicates of sound the creator had already hand-placed (bank-terminal beeps
  on the hex editor, the press-conference ambience, the desk phone, three stamps, hall room tone).
- **A2 untouched** at 17 clips. Sequence end unchanged at 727.860.

Cut sheets: `hf-graphics/sfx-overlays.{json,md}`, `sfx-overlays-plan.json`, `sfx-newgraphics-plan.json`.
Sources: 11 new Epidemic files in `assets/sfx/`, 59 rendered slices in `assets/sfx/rendered/`.

### ★ The bug that nearly shipped — read this before the next sound pass
`ffmpeg -v error` SUPPRESSES `volumedetect`'s output, so the "measured" peak silently fell back to a
default and every slice got its target level applied ON TOP of its natural level instead of
normalised to it. **28 ambience beds rendered at −63…−68 dBFS instead of −30** — placed, read back
and verified, and completely inaudible. Every check passed because every check tested PLACEMENT, not
LEVEL. Caught by diffing the exported audio against the previous master window by window. Two locks
now: a measuring function RAISES on a missing measurement, and an audio window diff runs after any
pass that adds sound. Full entry: `lanes/premiere/lab-notes.md` 2026-09-17.

### Still open (the creator's call)
- **`n1.mp4`** (4:02) sits at Motion scale **96** where the other 36 graphics are at 100. It came
  from my placer, not the creator. At 96 it carries the same dark red edge as the Higgsfield
  overlays, so it may read as deliberate. **Left alone.**
- Three narration date errors; the grade (Premiere 25.0 cannot run it); three Forest gameplay blocks
  awaiting footage (08:55.89–09:06.98, 10:09.73–10:20.79, 11:15.74–11:28.07).

## The edge-bleed look was RESTORED (2026-09-17); re-anchored pass complete on the timeline

### ★ THE EDGE BLEED WAS PUT BACK (2026-09-17)
Earlier the same day I scaled 59 reenactment clips from 96 % to 101.5 %, reading the inset as
`setScaleToFrameSize()` fitting instead of filling. **It was the creator's look** — a colour mat with
film grain under the overlay track, showing through all four edges as a dark red drop shadow.

- **Restored from `transcript/timeline-v2.xml`**, the FCP XML exported before any of it, which is the
  only record of per-clip Motion scale. Values read back out per clip: **96** on the 36 that carried
  one, **100** on the 13 the creator had left at the default. Verified clip by clip against that XML:
  **58 set, 0 mismatches.** The 18 clips placed after that export (the W/N/A cold-open set) took 96
  so they carry the same edge.
- **Proof:** program-monitor frames at 5.0 s and 368.3 s — the dark red mat and its grain read on all
  four edges again. `outputs/frames/f0000500.png`, `f0036830.png`.
- **`place-reenactments.py` reverted** to `setScaleToFrameSize()`, with the reason written into the
  file so it cannot be "fixed" again.
- **Logged:** the ★ lesson in `presets/youtube/affan-afterhours/LESSONS.md`, the corrected lane entry
  in `lanes/premiere/lab-notes.md` (the section claiming a fit was a hole is replaced), and the value
  itself locked into `presets/youtube/affan-afterhours/README.md` § 1 as THE OVERLAY FRAME.
- Nothing else on the timeline was touched.

## The re-anchored pass is COMPLETE and on the timeline

All **23 rows placed and verified** - `place-reenactments.py --verify` reads ALL PLACED, and twelve
frames pulled off the PROGRAM MONITOR confirm each one composites: the retailer cards over the store
footage, all five new Mango graphics, the American in the red hoodie, the hex-editor screen, and the
three CRT screens.

**The bridge dropped mid-pass earlier and 11 rows silently never landed.** The creator caught it. The
lesson is recorded: a report that lists what was RENDERED reads exactly like one that lists what was
PLACED - say which, and prove placement with frames off the timeline.

### On the timeline now
| where | what |
|---|---|
| V5 | the whole cold open re-shot and re-anchored (w01-w10), the Netherlands flag screen, the impatient close-up, the American, the hex-editor screen, the hands typing, the upload screen, the takedown screen |
| V3 | five new Mango graphics: m1 the Rockstar credits, m2 "He calls it Hot Coffee", m3 Lowenstein + Vance, m4 the Australian rating ladder, m5 April 2008 / GTA IV |
| V7 | r1, the four retailer cards over the store footage |

### Still the creator's call
1. **Three narration errors** (HANDOFF.md section 1): 02:27 and 05:18 state wrong dates; 09:43 has
   the FTC third-party clause backwards. No alternate takes. No graphic contradicts the voice.
2. **The grade** - Premiere 25.0 cannot run it; over V1 only when it is run, because the reenactments
   are already graded by prompt.
3. **Three Forest gameplay blocks** still need footage: 08:55.89-09:06.98, 10:09.73-10:20.79,
   11:15.74-11:28.07.

## Budget
900 at the start. **~127 left.**

## Done in this pass
1. **Read the creator's re-cut timeline back** (`transcript/timeline-v2.xml` -> `timeline-v2.json`)
   and logged every change they made: reenactments moved to V4/V5, their own stills on V3, my cards
   on V6, 27 nested sequences on V1, a new **Lavender** label for their own images, ~36 extra SFX,
   re-balanced music, two more music clips, and V1 re-labelled at clip granularity (208 blocks).
2. **Found and logged the real defect**: v2 split each Violet block into EQUAL slots and cycled the
   set's clips in file order, so no shot had any relationship to the line under it. Four worst cases
   named in `SHOTS-v3.md`. The rule is now: **every row carries the words it sits under.**
3. **New set W, the Wildenborg room** - master plate + 10 angle stills + 10 videos, every one anchored
   to one of the creator's own cut points, built to their brief (2004 room in a house, the monitor the
   only light, moody and suspenseful, environment consistent across angles).
4. **Nine new motion graphics** - m1 m2 m3 m4 m5, n1 u1 d1 (the four CRT screens that have to carry
   readable words), r1 (the retailers).

## Budget
900 at the start. **~127 left** after this pass (master plate 2 + 11 stills 22 + 11 videos 82.5).

## ▶ THE CREATOR'S HAND CUT IS THE SOURCE OF TRUTH (2026-09-16)

**Step 2 is CLOSED. The creator re-cut it themselves and released the edit back. NEVER replay an
EDL over `Sequence 12` again** — `transcript/cuts.json` is history now, kept only for the diff.

**Their timeline: 12:07.86 · 291 clips on V1 · 291 on A1 · 4 Epidemic music tracks already placed
on A2** (7 clips, spanning the whole runtime). **Do not run the music pass** — music is chosen and
placed. Epidemic is for SOUND EFFECTS only.

Exported and parsed to `transcript/timeline-handcut.xml` → **`transcript/overlay-blocks.json`**
(every clip with timeline position, source range, colour label and reconstructed text) and
`transcript/handcut-prose.txt`. Re-export after any timeline change; **the colour labels are NOT in
`get_sequence_structure`**, only in the FCP XML, and that export times out client-side while
Premiere finishes writing (wait for the file to stabilise, then parse; it may be truncated, so parse
clipitems by regex and split video/audio by file offset, not by tag nesting).

### The creator's overlay plan, read off the clip colours

| Label | Means | Blocks | Runtime | Share |
|---|---|---|---|---|
| **Violet** | Higgsfield reenactment | 27 | 5:03 | 41.5% |
| **Iris** (default) | face only, no overlay | 34 | 4:35 | 37.8% |
| **Mango** | motion graphic | 16 | 1:56 | 16.0% |
| **Forest** | real gameplay | 3 | 0:34 | 4.7% |

Also asked for: **title screens, built as motion graphics**, per the script's own `[ON SCREEN]` beats.

### ⛔ OPEN DECISION — the reenactment budget does not fit

302 s of Violet at 5 s per generated shot and 9.5 credits per shot, against a balance of **340**:

| Coverage | Shots | Credits | +25% retakes |
|---|---|---|---|
| a fresh shot per 5 s of runtime | 73 | 694 | 867 |
| max two shots per block | 51 | 484 | 606 |
| one shot per block, held/slowed | 27 | 256 | 321 |

Only the last fits, and it puts a single 5 s clip under a median 8.9 s block — and under one block of
**37.6 s** (the cold open), which is not viable. **Nothing is generated until the creator picks.**
The recommendation is to move the FACT-shaped Violet blocks to motion graphics, which cost nothing
and are what the channel preset already assigns them (README § 1: reenactment for human moments,
motion graphics for facts shown).

## 🛑 (historical) HANDS OFF PREMIERE — the creator is editing (2026-09-16)

**The creator has the timeline. Do not run ANY Premiere command — not `replay`, not
`audio-polish.py`, not even `ping` — until they explicitly give the call.**

They reviewed the rough cut and **did not pass it**: repeated sentences survived the automatic pass,
and they are removing them by hand now. They are also clearing the three stacked copies themselves.

**When they hand it back, the timeline is the SOURCE OF TRUTH. Never re-replay the EDL over it**
(`rough-cut` § Learn from the hand pass). First action on the call:

```
node lanes/premiere/premiere-bridge.mjs diff-edl projects/gta-san-andreas-hot-coffee/transcript/cuts.json
```

Read what they deleted and trimmed, fold every recurring pattern into `rough-cut`'s auto-kill rules and
`presets/youtube/affan-afterhours/LESSONS.md`. Their trims are the ground truth this pipeline is
approximating. Then step 3, audio polish at the measured **+5 dB**, on the clip count THEY left.

**They are also labelling the timeline to mark the overlay plan** — see § Overlay marking below.

**Why the cut missed repeats (for the diff to confirm):** the auto-dedupe was deliberately tightened
after it twice deleted real words (it ate "turned **off the lock**" and two items from "One is called
SEX / KISSING / SNM"). Each guard added — anchor-on-the-same-word, connective-only slack, a 0.35 s
stutter window — traded recall for safety, so the pass ended up biased toward UNDER-cutting. The
remaining repeats are that bias. The fix is not to loosen the guards; it is to read the take groups by
hand where `take-map.py` shows 2+ takes and the automatic pass kept them all.

## Overlay marking — the creator's call, CLIP COLOUR LABELS

Chosen over moving blocks to V2/V3, because **V2 and V3 are already spoken for**: the long-form layout
is V1 footage → **V2 grade adjustment layer** → **V3 graphics** (CLAUDE.md § step 4). Parking footage
on those tracks would collide with the grade and the graphics placer, and lifting clips off V1 would
punch gaps into a cut that currently has none.

Mapping (confirm against what they actually applied — read it back, never assume):

| Layer | Label |
|---|---|
| Higgsfield reenactment | (creator's choice — read back) |
| Motion graphic | (creator's choice — read back) |
| Real gameplay | (creator's choice — read back) |
| Face only, no overlay | left at the default label |

Read them with `get_color_label` per clip, or `select_clips_by_color`. Colour labels survive save and
reopen, and they do not move a single frame.

| | | |
|---|---|---|
| format | long-form YouTube 16:9 | probed 1920×1080 |
| lane | **Premiere** | ⚠️ the creator's EXISTING project `ABW6.prproj`, bin **`GTA SAN ANDRES`**, sequence **`Sequence 12`** — not a new job project |
| preset | `presets/youtube/default/` + channel `presets/youtube/affan-afterhours/` | |
| lane gaps | step 4 grade: Premiere is ✅ in LANES.md but this machine runs **Premiere 25.0** and the scripted grade needs 26 (BRIEF § 6) — a cost for later, not now | steps 2, 3, 5, 6 ✅ |
| source | **59.94 fps** (60000/1001) · 1937.44 s = **32:17.4** | 1920×1080 |
| constraints | **STAGE 1 ONLY — the creator's explicit instruction: rough cut only. No animations, no motion graphics, no other passes.** | |
| started | 2026-09-16 | |

## Sources and the sync

| | |
|---|---|
| camera (picture + scratch audio) | `E:\Skool Recordings\5 Sept Batch\C1289.MP4` — 14.7 GB, 59.94 fps, PCM scratch at −61 dB RMS (sync reference only, never program audio) |
| mic (the voice) | `E:\Shorts\Abudance Wisdom Shorts Exports\Final Renders\Batch Batch\2026-09-16 05-41-09.mp4` — OBS screen recording carrying the HyperX at −26.8 dB RMS, both channels identical (a mono mic duplicated) |
| **working master** | **`raw/hot-coffee-synced.mp4`** — the camera video stream copied bit-for-bit + the HyperX audio at AAC 320k. This is what the pipeline reads. |
| measurement | `audio/sync/sync.json` · `workflows/sync-dual-audio.py` |

**The sync, measured not guessed:** the mic started **+27.4029 s after** the camera. Four GCC-PHAT
windows spread across 23 minutes agreed to within **0.2 ms** (peaks 42–74× the noise floor), and the
clock drift between the two devices came out at **+0.1 ppm = 0.01 frames over the whole take**, so a
constant delay holds sync end to end and no resampling was needed. A first attempt with ordinary
cross-correlation scattered ±50 ms; GCC-PHAT is what made it frame-exact (why: the tool's docstring).

**And the mux was VERIFIED, not assumed:** the finished `hot-coffee-synced.mp4` was re-measured
against the camera's own scratch track at 300 s, 900 s, 1500 s and 1850 s. Worst deviation
**0.19 ms = 0.011 frames**. Duration matches the camera exactly (1937.4355 s), the video stream is a
bit-for-bit copy, and the audio is AAC 320k.

**Intake deviation, stated on purpose:** the 14.7 GB camera original is **not** duplicated into
`raw/`. `hot-coffee-synced.mp4` already carries its video stream bit-for-bit, its scratch audio is
preserved as `audio/sync/camscratch-16k.wav`, and the original is untouched at its own path above.
Copying it would spend 14.7 GB on the same physical disk to guard against nothing the pipeline can
do. The OBS original IS copied, to `raw/originals/` (200 MB). Say the word and I will copy the camera
file too.

## Steps

| # | Step | Status | What it produced / why not |
|---|------|--------|----------------------------|
| 1 | Intake | **done** | `raw/hot-coffee-synced.mp4` (synced master) + `raw/originals/obs-mic-…mp4`; both sources untouched at their own paths |
| 2 | Rough cut | **EDL done · timeline needs one re-replay** | **32:17 → 13:12.9**, 256 segments, dead-air gate **PASSES**. A first replay of an earlier EDL verified perfectly on the timeline (258 V1 + 258 A1 clips, 0 gaps, 0 overlaps, nothing off the EDL by even a frame). Two later replays of the corrected EDL timed out client-side and silently appended, so the sequence must be cleared and replayed once more. |
| 3 | Audio polish | **measured, not applied** | `voice-gain.py`: kept speech **−21.8 LUFS**, true peak −0.6 dBFS, LRA 5.1 → **gain +5 dB** into the −6 dBFS limiter. Apply after the clean replay (a timeline rebuild discards clip effects). |
| 4 | Color grade | — | **stage 2+** |
| 5 | Graphics | — | **stage 2+ — explicitly out of scope this session** |
| 6 | SFX | — | **stage 2+ — explicitly out of scope this session** |
| 7 | Review | — | |
| 8 | Export | ✓ 2026-09-17 | Re-exported after the edge-bleed restore and finalized. `outputs/gta-san-andreas-hot-coffee.final.mp4` · 727.860467 s · 3.65 GB · H.264 Main@L4.2 39.8 Mbps + AAC 317 kbps, mp42 · true peak −0.6 dBFS, LRA 3.5 LU · copy in `~/Downloads`. **Four renders to get there** — see `lanes/premiere/lab-notes.md`: the Premiere ingest preset is Main@10.6 Mbps despite its name, the AME MooV preset wraps QuickTime with PCM audio, and `exportAsMediaDirect` workAreaType **1** (in-to-out) lands one frame short because the out point is exclusive — use **0** (entire sequence). The previous master was High@L5.2 25 Mbps; this is a higher-bitrate Main encode from the same software encoder, so no quality loss, but 1.3 GB larger. |

## Request coverage

- **"do the rough cut first… no animations, no motion graphics, none of that"** → steps 4–6 are
  deferred by instruction, not skipped for lack of a recipe. Recorded so a resumed session does not
  wander past stage 1.
- **"use the audio of my HyperX mic, not the camera"** → done at intake; the camera's own audio does
  not reach the timeline at all. Evidence: `audio/sync/sync.json`.
- **"make sure there is no repetitive wording / repeated sentences… I was doing multiple takes"** →
  the governing rule for step 2. `rough-cut` keeps the **LAST** take of any repeated line and never
  compares takes. This is the main thing to verify in the cut sheet.
- **"so that I can see what the actual duration is"** → the report states raw vs cut runtime.
- **work inside the bin `GTA SAN ANDRES` in the already-open project** → import and replay target.

## The cut, in numbers

| | |
|---|---|
| source | 32:17.4 · 2,624 transcribed words · speech from 0:33 to 32:00 |
| speech vs silence in the raw | 16.1 min speaking, 15.4 min silence |
| final cut | **13:12.9** · 256 segments · 2,191 words |
| removed | 439 words: 198 whole utterances (chapter titles read off the page, superseded takes), 184 repeated phrases, 57 hand-authored spans |
| script coverage | **88.3%** token match against `script.md`; all 12 remaining gaps explained (9 are number formatting, 3 were never recorded) |
| dead-air gate | **PASSES** (`transcript/dead-air-qa.json`) |

**Two fresh-eyes reviews ran (one tier below this session's model) and both are adjudicated.**
The mechanical reviewer measured all 29 flagged boundaries, cleared 28 and found two real defects,
both fixed: a clipped "game." (cut mid-word, extended to its measured decay) and a segment that kept
a second "accused" the next segment repeats. The flow reviewer's first pass reported ~20 duplications
that were **artifacts of my own cut-sheet rebuild, not the edit** — twice: once from copying a whole
transcript field into both halves of a split segment, and once from counting boundary-straddling words
in both neighbours. Rebuilt by word MIDPOINT; the only repeated token now left in the whole cut is the
legitimate "…to reach it. It made no difference."

Working files: `transcript/cuts.json` (the EDL) · `transcript/cut-sheet.md` (every segment) ·
`transcript/cut-prose.txt` (the cut as one readable script) · `transcript/script-gaps.md` (coverage) ·
`transcript/take-map.md` (where the retakes were) · `outputs/…transcript.json` (canonical, for captions later).

## NOT RECORDED — three script passages are missing from the footage

Verified absent from the raw transcript, so these are gaps in the shoot, not the edit:

1. **"A modder in the Netherlands and a company in New York, telling the world two incompatible stories about the same thirty seconds of footage."** (chapter 5, the beat that lands the conflict)
2. **"Cut content that you left in the files is shipped content."** (chapter 9, the third line of the three-part LOCKED / UNREACHABLE / CUT build)
3. **The entire closing handoff** — "If you want the other half of how Rockstar handles the things it doesn't talk about — the leak, the one a teenager pulled off from a hotel room with a Fire Stick — that video's on the channel." The video currently ends on "…still building around the hole he found."

## Flags to report

- **Shot at 59.94 fps, not the 23.976 the channel playbook specifies** (`presets/youtube/affan-afterhours/PLAYBOOK.md` § B). Not a problem for the cut; it does mean this video will not carry the 24p film cadence the documentary look was specced around. Worth a decision before the next shoot, not now.
- **`Sequence 12` is 60.00 fps but the footage is 59.94.** The sequence is empty, so this is free to fix and must be fixed before the replay, or every cut lands on a grid the footage does not sit on.
- The project is the creator's live `ABW6.prproj` with 102 sequences. Every write is scoped to the `GTA SAN ANDRES` bin and `Sequence 12`.

## Skipped, and why

- Nothing skipped yet. Steps 4–6 deferred by the creator's stage-1 instruction (above).

### Next
1. **The creator answers the two date errors** (HANDOFF.md § 1) - a two-word pickup each, or a
   ripple trim I can run in one command.
2. **The grade** is a manual step on Premiere 25.0 (HANDOFF.md § 2) - and on this channel it should
   go over V1 ONLY, because the reenactments are already graded by prompt.
3. **Three Forest blocks still need the creator's gameplay**: 08:55.89-09:06.98 (the Statue of
   Happiness), 10:09.73-10:20.79 (Oblivion), 11:15.74-11:28.07 (the GTA 6 close). Until they land,
   V1's face plays under those blocks, which reads fine but is not the plan.
4. Re-export after any of the above. The draft is
   `outputs/gta-san-andreas-hot-coffee-draft.mp4`, 1920x1080 @ 59.94, CBR 24 Mbps, from
   `lanes/premiere/premiere-templates/youtube-1080p5994-h264-cbr24.epr` (minted this run from the
   locked 2160p preset).

### Skipped, and why
- **Step 4, the grade**: Premiere 25.0 cannot run it (project format v45 donors need Premiere 26);
  recorded in the channel PLAYBOOK before this run started. Manual recipe in HANDOFF.md § 2.
- **The music pass**: never runs on this channel. The creator lays their own Epidemic tracks on A2.
