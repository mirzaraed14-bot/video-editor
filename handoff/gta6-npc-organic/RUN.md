# RUN — gta6-npc-organic (Affan Afterhours video 41: GTA 6 NPC reactions, KSI+ style)

## ▶ STATUS: WAITING ON THE RE-RECORD (2026-11-24 ~08:50 PKT). Affan: "no ill rerecord we're fcked"
- **Why:** his only voice on this take was the CAMERA'S BUILT-IN MIC (no DJI on the shoot: speech p95 −48.7 dBFS, floor −94.8, roomy), and
  OBS recorded desktop audio only (profile "Ig live": Simple output `RecTracks=1`; Mic/Aux on track 2). No voice rescue (no Enhance Speech, no A1 swap).
- **ABW11:** v1 "GTA 41 - NPC Reactions" stays EXACTLY as it is (placed 05:57, unsaved, untouched since). Do not write to it, do not delete it
  without his word.
- **He skipped the 10 s test ("No need", 24 Nov).** So the FIRST step on the new take, before any build work: `ffprobe` the new OBS file and confirm
  his mic (the HyperX) is in it ON ITS OWN TRACK and not silent while he talks. That is the only voice requirement: the camera's built-in mic is
  fine as the sync backup, never a reason to stop him. If the OBS mic track is missing or silent, tell him at once.
- **Gate reference:** the PRE-RECORD GATE in `presets/youtube/affan-afterhours/REACTION-STYLE.md` § 13 (10 s test take; the OBS file has his
  mic (the HyperX) on its own track and not silent while he talks; the camera's built-in mic is only the sync backup; a clap on both). If he sends the test files, check them first.
- **What carries over to the new take (a rebuild should take ~1 h of machine time, not a day):**
  - the whole KSI+ build kit in this job: `work/` (cutbuild → edgefix → polish → build_plan, camfaces → move_plan, comp, whips, reelgain,
    edgecheck, the ▶-icon / splash / scroll / silence / popup guards) and `premiere/` (run.py windows, rebuild.py, finalize.py, place/moves/fx
    templates, readback + VERIFY + VERIFY2, offgrab, dialog-watch by PID);
  - the opener comp (`work/opener/opener.py`: procedural fire plate, the title wipe placed by measuring his cutout, ×2.2 push) and its SFX;
  - the cam box TOP-LEFT (his note: `work/box/make_box.py`, default left), pulse about its top-left corner;
  - the three fixes: no split-word cut edges (`work/polish.py`), streamer chat / sub counters blurred, whips grey after a B&W row;
  - the clerk-reel blur rule (if he reacts to `DgCjI63OH_r` again: blur the clerk from the gun turn until he's out of frame, Jason clear);
  - the reel mezzanines of THIS screen recording (`mezz/reels4-608x1080.mp4`, fill, audio, OBS-time) are reusable only if he re-reacts to
    the same OBS file; a new screen recording needs a new reel map (address bar segments, banner layout, boxes) — scripts as above;
  - the bridge lessons (lab-notes 2026-11-24): libx264 for anything Premiere imports, dialog-watch by PID around imports, waiters in the
    tool's background mode, read his active sequence after any interrupted window.
- **Sync on the new take:** if the OBS file carries his mic on its own track, `workflows/sync-dual-audio.py` (camera vs OBS mic) replaces the
  meter trick; a clap at the start of each camera file makes it frame-exact.
- Cost of this (v1) pass: $70.1 = 3.2 % of the week.

<details><summary>Status before the re-record decision (v1 delivery, 06:50–08:35)</summary>

**Superseded status:** resume here (2026-11-24 08:35 PKT): v1 PLACED + VERIFIED in ABW11; a FIXED build (incl. his 2 notes) is prepared and waits for HIS go
- **In Premiere now (v1, placed 05:55–05:57):** ABW11 › "GTA 41 - NPC Reactions", 17:38, every DEFAULT BUILD move on it
  (`premiere/VERIFY.md` + `premiere/VERIFY2.md` PASS against the plan of that moment; `premiere/readback.tsv` = the placed truth).
  **NOT SAVED** (crash net = Premiere auto-save + the re-runnable build below). His active sequence + playhead: untouched (checked 06:48).
- **Three defects in v1, found by the final review, FIXED in the prepared build only:**
  1. Audio cut edges: ~19 cuts of ≤ 0.16 s split words (e.g. "Oh, | shit", "He's | not in it") and a few cuts clip a word's tail
     ("whoa, whoa!" ~1:36, "What the heck?" ~4:47). Fix: `work/polish.py` (contiguous pieces butt on one boundary, gaps < 0.16 s
     closed, voiced edges moved to quiet on the camera's mic track or past the word); the 6 edges left sit inside laughs/room noise.
  2. R19 (the Bentley reel) shows the streamer's Twitch chat + "SUBS 30/100" counter: blurred (`mezz/reels4-608x1080.mp4`, which also
     blacks out a Windows taskbar preview card that popped over R05's letterbox for 0.9 s at OBS 257.4: the only one inside the cut).
  3. The whips after the two B&W rows flashed 5 colour frames: re-rendered grey (`mezz/whips-reel2.mp4`).
- **His notes on v1 (24 Nov, relayed by the research session):**
  - "where is audio, the OBS recording has my mic audio in it": it does not. The OBS file has ONE desktop-only track: −91 dB flat
    for 20–220 s while he talks the intro, and silent wherever no reel plays. His HyperX moved the OBS meter but was not routed to
    the recording. His voice on A1 is the CAMERA'S BUILT-IN MIC (Affan, 24 Nov: "there is no dji mic there ... thats just the camera mic"): 176 clips,
    unmuted, house chain (checked read-only 07:35); clean but very quiet and roomy (speech p95 −48.7 dBFS, floor p5 −94.8). Recording ask added to REACTION-STYLE § 13.
  - "my facecam should be on the left": DONE in the prepared build: box outer x20–366 y21–412 (`work/box/camframe_left.png`), V4
    position x193 y216.5, pulse about the box's top-LEFT corner, whips re-rendered with the box on the left
    (`premiere/proof_box_left.jpg`). The box never covers a reel (9:16 reels sit at x656–1264). Logged: REACTION-STYLE ★ + § 11 + § 14,
    channel LESSONS.
- **To swap the fixed build in (needs his go; the auto-mode check refused to run it unattended):**
  `python -I premiere/finalize.py` (waits for 160 s idle; imports reels4 + whips-reel2 + camframe_left.png; guarded clear of OUR sequence + re-place + moves
  by name; our sequence active ~1 min for the QE voice chain + B&W, then his restored by id; FX by name; readback + VERIFY + VERIFY2).
  Alternative: build it as "GTA 41 - NPC Reactions v2" beside v1 (not scripted yet).
- **C1499 sync is only BOUNDED (±0.25 s)**, see § Sync. Cost so far: **$63.7 = 2.9 % of the week** (session-cost.py, session 5f24084e, 06:50).
- After hand-off: no writes to his ABW11 without his go (hub, 06:55: "Hold"). Nothing written to ABW11 since 05:57; the 07:35 audio check was read-only.
- Prepared build = `work/plan.json` + `work/moves.json` + `mezz/reels4-608x1080.mp4` + `mezz/whips-reel2.mp4` + `work/box/camframe_left.png`; run `python -I premiere/finalize.py` on his go (his own words, in this session).


</details>

## Job
| | |
|---|---|
| Channel / # | Affan Afterhours · video 41 · format test: face-cam REACTION to Instagram reels of GTA 6 NPC interactions |
| Spec | `presets/youtube/affan-afterhours/REACTION-STYLE.md` ★ DEFAULT BUILD (KSI+, template `MgNMUQz5H5Q`, layout L1) |
| Lane | Premiere, his live project (ABW11 expected; checked at the window). He exports himself: the run ends at "placed + verified". |
| Sequence | "GTA 41 - NPC Reactions" (new, ours only) |
| Format | 16:9 long-form 1920×1080, 59.94 (camera rate) |
| Constraint | Content and order come from HIS recording; the 23 Nov TALK-LIST is NOT the sequence (none of its moments are in it). |

## Raws (copies; originals untouched)
| file | what | probe |
|---|---|---|
| `raw/C1498.MP4` | camera + its built-in mic (his voice), part 1 | 1920×1080 59.94, 1563.562 s, PCM s16be stereo 48k, TC 16:11:30:46 |
| `raw/C1499.MP4` | camera + its built-in mic, part 2 | 1920×1080 59.94, 638.638 s, TC 16:37:34:22 (starts ≈0.5 s after C1498 ends: continuous) |
| `raw/screen/obs-2026-11-24_00-33-22.mp4` | OBS screen (Chrome, instagram.com/reels) + desktop audio | 2560×1440 60, 2209.2 s, AAC stereo. Kept out of `raw/` top level so transcribe.sh skips it |

## Sync
- `sync-dual-audio.py` (both files vs OBS): offsets −526.5 s / −752.7 s with ±257/±321 ms scatter, peaks 3–6× → **false matches**
  (the two answers overlap each other; camera timecodes prove C1499 follows C1498).
- Why: OBS audio is reel sound only (digital silence while he talks); the camera track is his voice only (in-ear earphones, gated
  camera mic, gated/very quiet: noise floor ~−95 dB). A masked bleed test (OBS active & camera quiet) gave r = 0.03 at every lag: there is no shared sound.
- Picture light (face/glasses luma vs the reel), cursor-vs-arm motion, leakage GCC-PHAT and startle latency: all no signal.
- **C1498: OBS = cam − 18.63 s, frame-level.** Read off the OBS window's own Mic/Aux meter (his HyperX voice drawn on screen, OBS 5–101 s) against the DJI voice: onset fit −18.637 (peak 2.8× the next), level fit −18.623.
- **C1499: OBS = cam + 1577.50 s ± 0.25 s, bounded not measured.** No shared signal exists in its span. Camera creation-time gap 1597 ± 1 s → [1577.37, 1579.37]; the behavioural fit (1578.71) runs 0.7–2.1 s late on C1498 → low end. Reel clips cut from C1499 time are slippable; flagged in the delivery note.
- Camera gap: C1498 ends at OBS 1544.9, C1499 starts at OBS ~1577.5 (~33 s with no camera). All numbers: `work/sync.json`.

## Steps
| # | step | state |
|---|---|---|
| 1 | Intake + sync + ASR | done (sync: see § Sync; ASR large-v3 once, GPU) |
| 2 | Cut (dead air, fumbles, last take, whole lines, jokes kept) | done: `work/cutbuild.py` + `work/cut_overrides.json` (every manual drop with its reason) + `work/edgefix.py` → `work/plan.json`, `transcript/cuts.json` |
| 3 | Place: V1 cam (EDL replay) + reels on L1 (fill V2, reel V3, cam box V4/V5) | done, VERIFY PASS |
| 4 | Voice chain, clip audio −6 dB under voice, face moves, opener, whips | done, VERIFY2 PASS |
| 5 | Verify (offline frames, readback) | done |
| 6 | Deliver note + JOBS row + LESSONS/lab-notes | done (JOBS row = the hub's; lab-notes 2026-11-24) |

## Cost (session %)
- 06:00 delivery of v1: $50.6 = 2.3 %. 06:50 incl. the review fixes: $63.7 = 2.9 % (Opus 5.5 + Fable advisor calls).

## The cut (step 2)
- Auto first pass (`work/cutbuild.py`): a reel playing for the FIRST time (OBS audio or reel motion, address bar on a reel, Instagram's ▶
  pause icon NOT on screen, not an audio replay) = CLIP (L1, he reacts in the box); his voice otherwise = full cam; the rest is cut.
  Anti-flicker: cam < 1.5 s between clips → clip; clip < 2.0 s between cams → cam.
- Replays: detected from reel-AUDIO self-similarity (`work/reels/audloops.py`); the picture detector was fooled by static fixed-camera shots.
- Editorial drops + one forced layout: `work/cut_overrides.json` `_why` (first intro take, meta lines, Whisper hallucinations, fumbled
  unfinished stories, off-topic filler, the R25 repeat he skips, the clerk reel's second watch).
- Edge fix (`work/edgefix.py`): clip rows start on the first real reel frame (no black/loading, no Instagram splash), stay ≥ 1 s clear of a
  reel scroll, and carry no ▶ pause icon at either edge; a trimmed edge where he speaks becomes full-cam instead of being cut.
- Kept judgement calls (for his review): the intro keeps his Brian ambush story (first reel at ~1:10); the conspiracy tangent is cut to
  ~50 s; two rows (S087, S129) keep a ~0.3 s ▶ flash because he is mid-sentence; swears kept (KSI+ censors nothing; no drug or
  self-harm words in his speech).
- Reels in the cut (address-bar ids, his order): R05 DgDP0c3lxys, R06 DgBsDOPokWW, R12 DgAY0euJkFt, R13 Df5IBXcTC0I, R14 DgCY4r8xIG6,
  R16 DgA-KFIpZS_, R18 Df-JJucjM2g, R19 Df8PJtixgte, R20 DgDXb1IiTT2, R21 DgBTWeJOpJJ, R22 Df5ylOwM72N, R23 Df9zWRkiyKF, R24 DgCF7SXBDMm,
  R26 DgC3SaPIu5I, R27 Df-XoW9BHrw, clerk DgCjI63OH_r (first watch only, clerk blurred from the gun turn to out of frame, Jason clear).

## Mezzanines (all on OBS time: mezz t = OBS t)
- `mezz/reels-608x1080.mp4` 60 fps: the reel box cropped per Chrome-banner layout (banner: x948–1597 y205–1364; no banner OBS
  1143.5–1338.75: x932–1614 y150–1362) → 608×1080; clerk blur baked (OBS 2103.25–2109.3 and 2138.75–2145.9).
- `mezz/fill4-640x360.mp4` (V2 at Scale 300): cover-scaled, gblur 32, −10 % luma, soft vignette. `mezz/reel-audio.wav` (A2).
- Reel loudness: each reel to −25 LUFS (6 dB under the voice, which lands ~−19 LUFS: the take is −43.1 LUFS and the house gain caps at
  +24), peaks ≤ −6 dBFS (`work/reel_gains.json`).

## The timeline (track map, REACTION-STYLE § 11)
| track | what | how it was proven |
|---|---|---|
| V1 / A1 | his camera, 176 rows (EDL replay of `transcript/cuts.json`); A1 = house chain Amplify +24 dB → Hard Limiter −6 dBFS on every clip | readback frame-exact; chain values read back 176/176 |
| V1 Motion | face moves: anchor = position = his face (YuNet per row), ×1.30 jumps alternating across every in-cam cut (28), ×1.9 punch (1: "What the fuck?" at 1:19), eased ×1.0→×1.5 push-ins over 22 f, cubic ease-out (23, one per cam stretch ≥ 4 s; from ×1.06 after a jump), laugh creeps ×1.4→×2.0 over 150 f (2), B&W ×1.30 on his two loudest laughs (2, Black & White effect) | keys read back (count + end values) per row; `proof_moves.jpg` |
| V2 | blurred fill (`mezz/fill4-640x360.mp4` at Scale 300) | readback |
| V3 | the reel, 608×1080 centred (`mezz/reels-608x1080.mp4`, OBS-time) | readback; edges checked frame by frame (`work/edgecheck.txt`) |
| V4 | cam box: video-only subclip of the camera, Motion crop to head-and-shoulders (head per row), Scale ×(377/640), into x1561–1893 y28–405; 4 laugh pulses ×1.40 about the box's top-right (24 f ease-out, hold, 24 f back) | readback; pulse keys 51 per clip |
| V5 | the box frame PNG: 7 px white border, pink #FF2E9A zig trim + edge stripes, AFTERHOURS (Inter Black, sheared) on the bottom border; pulses with V4 | readback |
| V6 | the opener (0–8.44 s) + 40 cam→clip whips (13 f each: 5 f cam smear, swap, 8 f clip unsmear), pre-rendered from the same plan (`mezz/opener.mp4`, `mezz/whips-reel.mp4`) | readback positions; frames in `proof_moves.jpg` |
| A2 | reel audio, each reel at −25 LUFS (6 dB under his ~−19 LUFS voice), peaks ≤ −6 dBFS | levels read back |
| A3–A6 | opener SFX only (KSI+): explosion 1.0 s, a hit per title word (4.30 / 4.85 / 5.15 s), whoosh on the push 5.9 s (local Epidemic/library files copied to `mezz/sfx/`) | readback positions |
| markers | one per reel (its first row) | 16 |

## DEFAULTS TAKEN (REACTION-STYLE § 12, built until he answers) and his open questions
1. Music: **no bed** (exact KSI+). Open: GTA rule (11-21) says full SFX + Epidemic music: want a bed?
2. SFX: **opener only** (explosion + 3 word hits + push whoosh), nothing on whips/zooms/box. Open: add hits on the zooms?
3. Box trim: **white 7 px border + hot-pink zig trim + AFTERHOURS** (no logo file exists). Open: his own wordmark/logo?
4. Same-camera instant zooms: **followed KSI+** (×1.30 jumps + one ×1.9). Open: keep them, or his 10-07 "no punch-ins" rule?
5. Length: **17:38, cut tight to his reactions** (KSI+ runs 14–22 min; the channel's data likes 6–7 min). Open: a tighter cut?
6. Opener plate: **procedural fire** (no download, no Higgsfield credits). Open: a stock fire/explosion plate or Higgsfield (his credits)?
7. End sticker: **none**. Open: a "DO NOT SUBSCRIBE"-style line of his own?
8. B&W: **rare (2)**. Open: B&W on every jump zoom (KSI+'s newest habit)?
9. Censoring: **nothing needed**: no drug or self-harm words in his speech (large-v3) or in the kept reel audio (small.en, 250 segments).
   Swears kept (KSI+ censors nothing). The clerk reel: clerk + sparks blurred from the gun turn until he's out of frame, Jason clear.
- Title on the opener: **FUNNIEST / GTA 6 / NPCS** (his own words at 0:04): a placeholder for the real video title.
- Picture source: reels are OBS screen grabs (no source files; nothing downloaded). They carry Instagram's mute icon in the corner,
  the cursor at times, and creator captions; handles sit outside the crop. Open: download the 16 reels at source quality?
- Clerk reel: the kept part starts at the gun turn, so the clerk is blurred from its first frame; ~1.1 s of him taking the gun
  (unblurred) could be added before it for context.
- Two clips keep a ~0.3 s Instagram ▶ flash because he is mid-sentence there at **8:10** (S089, 21 frames) and **13:11** (S131, 16 frames).

## Deviations from the ★ DEFAULT BUILD (for his review)
- **First reel at ~1:08**, not ~0:11: the intro keeps his whole Brian-ambush story. One-cut fix: drop rows S010–S013 (the story) → first reel at ~0:35.
- **No motion blur** on the push-ins (Motion keys; Transform's shutter needs a QE effect per clip).
- **Zoom rate 1.8 scale changes/min** (+ 23 push-ins), one ×1.9 punch: lower than KSI+'s 2–6/min.
- Whips and the opener are **baked V6 clips**: stale if he re-trims around a cut (delete the V6 clip there).
- **Handles are outside the reel crop** (creators' captions are in): R05 @aurawelness_, R12 @leonidaclipz247, R16 @justmaliyahh,
  R19 @nytrsa, R23 @icemanisaac, R26 @beastbalagaming, clerk reel @arccreepy21 (read off the OBS frames at 300/700/1000/1300/1700/1900/2100 s;
  the other reels' handles were not legible in the sampled frames).
- **Voice:** the take is −43.1 LUFS; the house gain caps at +24 dB, so the −6 dBFS limiter catches up to ~13 dB on his shouts (voice-gain.py warned).
- The Onyx kit's `prep.sh` / `xplay2` were NOT used: there were no source clip files (reels watched in the browser) and no shared audio
  to sync, so the play map came from the OBS picture (address bar + reel-area motion + Instagram's ▶ icon) instead.
- Incidents: the bridge froze 16 min (my NVENC import modal, 04:40–04:56); our sequence sat active in his Premiere ~1 min (05:56) after a
  waiter died mid-window: restored by hand, playhead ticks identical. Both logged in lab-notes.
