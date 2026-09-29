# RUN — charlie-best-youtuber — "why Charlie (penguinz0) is the best YouTuber, not MrBeast"

## ▶ STATUS: resume here (updated 2026-09-28)

**Channel:** AffanWiz → read `presets/youtube/affanwiz/` first (README · PLAYBOOK · LESSONS). **Format:** long-form
YouTube, 16:9 (horizontal, auto-detected). **Lane:** Premiere, the CREATOR'S project `ABW8.prproj`
(`E:\Premiere Pro Exports\Adobe Premiere Pro Auto-Save\…\ABW8.prproj`; backup before our first write:
`premiere-backup/ABW8-before-rough-cut.prproj`). The cut goes ONTO **`Sequence 12`** itself (creator, 2026-09-28): clear it, replay onto it.

**Scope: the ROUGH CUT** (creator, 2026-09-28: "do a rough cut on sequence 12 in premiere project abw8").
Handover = the channel pattern: V1 `C1311.MP4` (`E:\Skool Recordings\5 Sept Batch`, 8.05 GB, 1920×1080 59.94,
17:38; source in 63.4167 s, seq 0 → 994.63) + A1 the creator's Enhance-Speech voice
`where-esv2-2p-bg-10p-music-10p.mp3` (Downloads\Music, 16:35, seq 0 → 994.7).

**Where it is: ROUGH CUT DONE, ON SEQUENCE 12, VOICE CHAIN ON, SAVED (2026-09-28).** ABW8 · `Sequence 12` (60 fps
timebase, the creator's handover) was cleared and the EDL replayed onto it: **157 clips on V1+A1, 8:25.6** (from
16:35), `diff-edl` exact match, 0 gaps. A1: +4 dB (kept speech −21.4 → −17 LUFS) + Hard Limiter −6 dBFS, 157 verified.
Media = `raw/charlie-best-youtuber-synced.mov` on X: (bin `AffanWiz - charlie-best-youtuber`). The empty
`charlie-best-youtuber - rough cut` sequence I first made was deleted. Reviews applied: flow (3 echoes + 1 filler,
in build-cuts.py), mechanical (6 edges), a main-session LEAK SWEEP (13 OUTs that ran into a killed word, e.g.
"…like a human. But"), dead-air gate green. Creator's hand pass done by the creator (final cut + music bed on A2, 2026-09-28). **MUSIC DROP-OUTS DONE, SAVED
(2026-09-28):** the music is lifted under every punch-in (V1 Scale 127): 37 punch-ins → 34 drops, 58.8 s, A2 4 → 37
clips, every edge within 0.3 ms, levels −15 dB kept, V1 + A1 identical before/after. Undo: `music/A2-before-dropouts.json`
+ `premiere-backup/ABW8-before-music-dropouts.prproj`; tool `music/dropouts.jsx.tmpl`. Hard cuts; 1–2 frame fades
offered if they click. NEXT: overlays to README § 1a on the creator's word.

**How the cut is built (re-runnable):** `uv run transcript/build-cuts.py` (every keep commented; 2 PIN rows) →
`RENDER=0 splice.sh` → `polish-boundaries.py` → `uv run --with numpy --with scipy python transcript/fixes.py`
(dead-air splits + review fixes; `--scan` lists late-start candidates) → `RENDER=0 splice.sh` → `dead-air-qa.py`.
Corrections: `corrections.local.json` (Claw→Claude, goal→GOAT).

## Steps

| # | Step | Status | Notes |
|---|---|---|---|
| 1 | Intake | **done** | originals copied to `raw/originals/` (C1311.MP4 8.05 GB, the mp3 15.9 MB). **Sync measured, not trusted** (`audio/sync/sync.json`): voice starts **+63.3490 s** into the camera, drift −8.7 ms over the take (−9.3 ppm, resampled), scatter ±0.1 ms. **Premiere had it at +63.4167: 68 ms (4 frames) late.** Working raw: `raw/charlie-best-youtuber-synced.mov` (camera video stream-copied + voice as PCM 48 k, 17:38). |
| 2 | Rough cut | **done — on Sequence 12** | transcribed once (WhisperX, 4.5 min) → `transcript/words.json`; gap speech checked by slice re-ASR (aborted fragments only). | LESSONS: every IN after a ≥ 0.65 s pause gets an envelope check (polish-boundaries' 250 ms onset window is still unfixed); slice re-ASR every pinned/⚠ boundary |
| 3 | Audio polish | **done** | +4 dB + Hard Limiter −6 dBFS on all 157 A1 clips, read back |
| 4–8 | | creator's hand pass, then their direction | |

## Constraints
- Never touch any OTHER sequence in ABW8. The empty `charlie-best-youtuber - rough cut` sequence I created gets deleted at the replay.
- The session runs in ask-each-action mode for this job (auto mode's server-side check was failing, 2026-09-28).
