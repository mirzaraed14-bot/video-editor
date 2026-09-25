# RUN — monetized-before-gta6 — "my GTA 6 channel got monetized before the game is out"

## ▶ STATUS: resume here (updated 2026-09-23)

**Channel:** AffanWiz → read `presets/youtube/affanwiz/` first. **Format:** long-form YouTube, 16:9 (horizontal,
auto-detected). **Lane:** Premiere, working in the CREATOR'S project `ABW8.prproj` (path: Premiere's Auto-Save
folder, `E:\Premiere Pro Exports\Adobe Premiere Pro Auto-Save\…\ABW8.prproj`; backup before our first write:
`premiere-backup/ABW8-before-rough-cut.prproj`). Their handover sequence **`Sequence 02` is never touched**.

**Scope so far:** rough cut (done) → the creator's own hand pass (face cut, nests, cut zooms, nested zooms, overlays
dropped on V1; sequence now **8:09.7**) → **overlays finished to the channel's OVERLAY FRAME** (done 2026-09-23).

**▶ Where it is (overlays DONE, project saved):** sequence `monetized-before-gta6 - rough cut`. All **36 overlay slots**
(35 screenshots + 1 gameplay clip) now read: **V1** = animated matte (`overlays/matte-affanwiz-5994.mp4`, in-point =
sequence time; the gameplay slot uses `matte-slot15-depth.mp4` with its shadow burned in), **V2** = the overlay
(`overlays/final-depth/ovd-<key>.png`, Scale 100, shadow baked; gameplay at Motion Scale 88.5). `place-overlays.py
verify`: 36/36 frame-exact on both tracks, V1 57 clips / 0 gaps, **the 21 untouched V1 clips (13 nests + face) identical**,
A1 voice untouched. Proof frames rendered in Premiere: `overlays/qa/proof-sheet.jpg`. Backup of the creator's edit
before any of this: `premiere-backup/rough-cut-creators-edit.xml`. Superseded imports sit in bin
`AffanWiz overlays/superseded builds (unused)`.
**Higgsfield:** 28 overlays enhanced (19 upscaled, 9 tiny ones re-rendered by `gpt_image_2_5`), 67.5 credits
(986.5 → 919); every job id in `overlays/higgsfield-jobs.json`, each result QA'd against its original (`overlays/qa/compare-*.jpg`).
**Flag for the creator:** the 2.5M badge crop includes a sliver of a thumbnail, which the re-render redrew; at 50 % width
it shows. Offer to crop it out.
NEXT: the creator's review, then steps 4/6–8 on their direction.

## How the cut is built (re-runnable)
1. `uv run transcript/build-cuts.py` — every keep as a word-index range, commented; PIN rows for boundaries
   WhisperX got wrong (measured by slice re-ASR + forced alignment + envelope). Writes `/tmp/video-editor/<job>/cuts.json`.
2. `RENDER=0 splice.sh` → `polish-boundaries.py` → `RENDER=0 splice.sh`.
3. `uv run transcript/fixes.py` (dead-air splits, flow-review kill, the '15th' tail, 9 mechanical-review edges) → `RENDER=0 splice.sh`.
4. `dead-air-qa.py` must pass (it does: 148 segments, 523.76 s). The persisted EDL is `transcript/cuts.json`.
5. `premiere-bridge.mjs replay` onto the active sequence → verify by readback → `audio-polish.py --apply`.

## Steps

| # | Step | Status | Notes |
|---|---|---|---|
| 1 | Intake | **done** | `raw/originals/` = copies of `C1292.MP4` (E:\Skool Recordings\5 Sept Batch, 9.6 GB, 1920×1080 59.94, 21:01) + the creator's Enhance-Speech voice `like-esv2-2p-bg-10p-music-10p.mp3` (Downloads\Music, 128 k MP3, 20:47). **Sync measured, not trusted:** `audio/sync/sync.json` → voice starts **+14.5519 s** into the camera, drift −13.9 ms over the take (−11.7 ppm, resampled), scatter ±0.1 ms. Premiere had it at +14.5667 (15 ms late at the head, 29 ms at the tail). Working raw: `raw/monetized-before-gta6-synced.mov` (camera video stream-copied + voice as PCM 48 k). |
| 2 | Rough cut | **done — on the timeline** | transcribed once (WhisperX, 3.5 min on the RTX 3060 Ti) → `transcript/words.json`. Kill rate is an outcome: 20:47 → 8:43.8. Corrections: `corrections.local.json` (school→Skool, real→reel). |
| 3 | Audio polish | **done** | +5 dB (−22.4 → −17 LUFS kept speech) + Hard Limiter −6 dBFS on all 148 A1 clips, read back |
| 4–8 | | waiting on the creator's direction | |

## Transcript facts found (for the graphics pass)
- Repeated-take scan on the final cut (3/4-gram repeats within 12 s): only deliberate parallels remain (PS5 callback, the 10k/34k/339 list, 'think how insane' pair) — no retakes.
- Flow review: killed 'So let me show you in order' (meta-signpost); kept 'this is the part where it gets crazy'.
- WhisperX misaligned the first word of 6 takes (Channel / And / I / I would / But / Oh, one more thing); the
  cut keeps the right audio (pinned), but `outputs/<job>.transcript.json` lacks those first words.
- The creator says the requirements double on **"January 1st"** once and **"January 31st"** twice — flag to them.
- On-screen references to add later: "You see that video? It's at 9.6 thousand views", "Right here, I can see it",
  "here I can see I got 10,000 / 34,000 / 339 views", the Monday monetization email ("This came in on Monday").

## Constraints
- Never touch `Sequence 02` or the creator's other sequences in ABW8.
- Everything built fresh for this job; nothing copied from earlier jobs.
