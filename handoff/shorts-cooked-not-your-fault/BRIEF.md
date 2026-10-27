# shorts-cooked-not-your-fault: ORGANIC REEL for Affan's @affancuts page (ABW10 "Shorts cooked reel")

## ▶ STATUS: resume here
- **2026-10-27 ≈13:00 PKT: v2 PREPARED — "Shorts cooked reel v2"** (same bin; v1 "Shorts cooked reel" kept untouched: re-dumped,
  identical to its 12:05 state, and no export of the reel anywhere in Exports / E:\Shorts / Downloads, so he had not edited or
  exported it). Affan's review note (the only one for the reel): the SFX read "very very cheap … not expensive, premium, refined,
  subtle … loud in places". v2 changes ONLY A2/A4: cut, graphics, bed, captions, voice chain identical (cloned).
  **27 cues from a FRESH Epidemic set** (10 takes, none of the 591 earlier ids; `work/sfx2_fetch.py`): 22 soft airy swishes on the
  graphic entrances (7 takes rotated, never the same twice in a row), 3 light risers that END on the 487K / 600M / reprise gold-bar
  landings (2 takes), 2 soft high-passed impacts on the 487K and 600M landings (one take, the 600M a minor third lower). Out: every
  stab, crunch, sub, boom, deep whoosh. Every slice ≤ 18.5 dB tonal prominence, phone band checked (`work/sfx_measure.py`).
  **Levelled by loudness, not peak** (`work/sfx2_build.py` → `work/sfx2-gates.txt`): every swish / riser exactly 19.5 LU under his
  short-term loudness at its spot (gate 18), impacts 22.6-26.0 LU under (gate 12) with peaks 10.5 dB under the local voice peak
  (gate 10); spread over the class median: swish +1.7, riser +0.7, impact +1.7 LU (gate 3); no two cues sounding at once.
  Placed by `work/sfx_v2_place.py` (per-cue Volume, read back 27/27 within ±20 ms / ±0.1 dB). **`--verify` (plan_v2.json) 0 problems**,
  real end 83.8167 s, lip sync OK (worst 11.1 ms), proof `work/grabs-sheet.jpg` (v1's kept as `grabs-sheet-v1.jpg`). Active sequence
  restored to "MATG reaction" (what was active before the windows), ABW10 saved, premiere.lock released. He exports v2.
- **2026-10-27 ≈12:05 PKT: PREPARED IN ABW10** — sequence **"Shorts cooked reel"**, bin "Onyx batch 5 reactions (2026-10-27)",
  **REAL sequence end 83.8167 s (1:23.8; cap 1:30)**, 1080x1920 @ 60. V1 screen / V2 face (49 segments, razored to 56 pieces, 67
  layout edits, 0 leaks) / V4 15 MG layers / V5 captions + seam line; A1 voice with the house chain on all 49 clips (Amplify +10.0 dB
  into Hard Limiter −6 dBFS, read back), A2/A4 38 SFX (26 + 12), A3 the bed. **`apply.py --verify`: 0 problems.** Lip sync from the
  sequence: all 56 face pieces +2.8 ms off the sync line (`tools5/lipsync.py` worst 11.1 ms, OK). Proof sheet `work/grabs-sheet.jpg`
  (23 program-monitor grabs, GRAB_WAIT 12-18). ABW10 saved (safe_save) with "Joe Appointment - raw cut" active again (same id),
  premiere.lock released. **He exports himself** (never exportAsMediaDirect / Media Encoder). Nothing reviewed by him yet.
- Premiere-side fixes this run: (1) every camera in-point had landed 14-30 ms early (Premiere floors a subclip in-point to the
  camera's 59.94 frame, then to the 60 grid): V2 re-placed with `work/fix_v2.py` (requests chosen so the double floor lands on the
  nearest grid point), re-styled, `build_seq3 --verify` OK; (2) the reprise's landing hit ran 0.43 s past the picture (sequence end
  84.25): trimmed to V1 with a 0.12 s ramp, sequence end 83.8167.
- **Cut 83.82 s (1:23.8; cap 1:30, target ≤ 1:28)**, 49 segments, pins rounds 1-3 measured (`work/pins1-3.json`; round 3 cut an
  aborted restart "…episodes, you just have to" inside the "all of your episodes" segment). **All 48 joints proven on Whisper large-v3
  (GPU, `work/jointcheck.txt`, 09:35)**: no clipped or stray word. Lip sync proven on the synthetic dump (47/47 face clips within one
  frame, GCC-PHAT, `work/sync_proof.py`; re-run on the real dump in step 4).
- **Format:** his reaction toolkit as a reel (screen = Scott's channel as the proof on top, camera below, seam line, Bebas captions on
  it with one gold emphasis word, face-only beats under black bars, zooms + gold rings on the page's numbers, MG stages for the
  lesson, SFX, a subtle bed). Why: the proof IS the screen, and it is the look of his own Onyx reel.
- **Look M:** hero = FX-69 honest-scale gold bar (487K vs 18 slivers + our 10K), reprised at the payoff; COOKED ghost + a big hook on
  frame 0; era pill; Popular-sort still card; the 20-tile episode grid; 600M vs 50M bars. Cormorant Italic 600, "focus" entrance.
  15 MG layers (`overlays/mg/*.mov`, every one frame-complete), 117 caption chunks (`overlays/captions.mov`), `mgx.py --check`
  0 errors / 0 warnings + stage_check 0, `apply.py --layout-check` 0 leaks. 5 face-only beats (16.3 s, 19 %), no face span > 4 s bare.
- **Audio:** voice +10 dB into −6 dBFS (−18.6 LUFS); bed "A Mistake (Instrumental Version)" (Particle House, never used) at −21.9 dB
  from 6.224 s (≈13 LU under); 38 SFX cues from 7 job slices (`audio/sfx/`), none shared with J or K, ≤ 26 % each, never 3 at once.
- **Number mismatches (graphics = the screen; captions = his words):** "around 1000 / 900-1000" → the page shows 493-1K (graphic:
  "493 TO 1K VIEWS"); "Scott's second most popular upload" → #2 of the SHORTS tab's Popular sort (595K is #1); "two months old" → not
  on screen (no number in any graphic); ASR "Damon John" → Daymond John; 600M / 50M / "two weeks" are his own claims (shown as said);
  10K and 487K match the page (487K was 378K on 10-24).
- **Taste calls:** hook line 2 = "it's actually not your fault" (22.49), not the later hedge "it might actually be not your fault";
  "like" kept in "averaging like around 1000" (20 ms gap); "and also" kept; "clips" in "qualify as clips" is swallowed (caption keeps it).

## Inputs
- OBS (good mic, 2560x1440 60p, 291.0 s): `raw/2026-10-26 20-15-52.mp4`, a COPY of
  `E:\Shorts\Abudance Wisdom Shorts Exports\Final Renders\Batch Batch\2026-10-26 20-15-52.mp4`.
- Camera `X:\Recordings\Onyx\C1407.MP4` (390.9 s, 1080p 59.94): camera = OBS + 92.497 s, 0 ppm
  (`../_onyx-batch5-2026-10/reactions/sync/sync-C1407-20-15-52.json`).
- Transcript: `transcript/words.json` (WhisperX large-v3 of the OBS audio, from `_onyx-batch5-2026-10/reactions/obs-20-15-52/`).
- **Camera pre-roll (camera 0-95 s, before OBS started) = earlier REHEARSAL takes of the same hook and Scott lines** on the bad
  camera mic, no screen recorded ("If you have a podcast / but your short form is absolute… / it's actually not your fault ×2 / So
  this is Scott [Clary] ×3 / working with him for two weeks / a thousand-ish / 10,000 / … the second most popular"). The OBS takes
  come after them, so the OBS takes ARE the last takes: the pre-roll is not used. Evidence (faster-whisper medium.en, CPU, +45 dB):
  `work/cam-pre.txt`.

## What the screen shows (OBS time; the screen is the truth for every graphic number)
- 0-7 OBS UI; **7-35.5 his SCRIPT in Notepad ("Onyx Reels 1" + "Onyx Reel 2" notes about other clients)**; 35.5-38 the alt-tab
  switcher. **The screen is NEVER shown before OBS 38.3**: the hook runs face-only.
- 38-40.5 Scott's channel header: **Scott D. Clary - Success Story Podcast ✓, @scottdclary · 480K subscribers · 1.9K videos**.
- 40.5-77.7 the Shorts tab (Latest), scrolled: our first upload **"Daymond John's $1B Jersey Marketing Tactic" 10K views**, our
  second **"Daymond John Almost LOST $250M" 487K views**; neighbours 1.1K, 373, 203, 731, 493, 977 views.
- 77.75-81.5 **Shorts sorted by Popular: #1 Matt Gutman 595K, #2 "Daymond John Almost LOST $250M" 487K**, #3 298K, #4 258K.
- 82-107.5 Latest again (static from 90.25); 107.5-129 the Videos tab (newest long-forms 42K 5d / 67K 6d / 86K 10d: **no Daymond
  John episode and no date for it on screen**); 129-287 the Shorts grid scrolled down to the OLDER Shorts, static 133.75-287.

## Number check (his words vs the screen)
| He says | Screen | Graphics show |
|---|---|---|
| "averaging like around 1000 views" | neighbours 203 / 373 / 493 / 731 / 977 / 1.1K (Latest) | the real tile counts, never a "1,000 average" |
| "the first video … did 10,000 views" | "Daymond John's $1B Jersey Marketing Tactic" 10K views | 10K ✓ |
| "second upload 487 000 views" | "Daymond John Almost LOST $250M" 487K views | 487K ✓ (it was 378K on 10-24) |
| "Scott's second most popular upload" | #2 on the **Shorts** tab's Popular sort (595K is #1) | "#2 most popular SHORT" (the screen ranks Shorts only) |
| "this podcast of Daymond John … is two months old" | not on screen (the Videos tab shows no date for it) | **UNVERIFIED: no number in any graphic** (the caption keeps his words) |
| "Damon John" (ASR) | Daymond John | corrections.local.json: damon → Daymond |
| 600M (his own), 50M (his advice) | not screen claims | his own figures, as he says them |
| "we've been working with him for two weeks" | not on screen | his own claim about his own engagement (the era pill "SCOTT CLARY · week 2", like 600M); a claim about SCOTT'S channel that the screen does not show ("two months old") gets no number |

## Catalog pass, section M (copied verbatim from `_onyx-batch5-2026-10/reactions/CATALOG-PASS.md`, 2026-10-27)
### M · Reel for @affancuts (obs-20-15-52)
Not a reaction: no channel card, no showcase. Assumes the OBS-top / camera-bottom split with Scott's channel on screen. Raw 8.6-284.9 s must reach 90 s, so only surviving beats:
- FX-41 Year Ghost: "your short form is absolutely cooked" @11. 75 %-wide ghost "COOKED" on the first frame. `title_card` (new config).
- FX-04 Era Tag: "This is Scott Clary… two weeks" @37-40. Persistent pill "SCOTT CLARY · WEEK 2". `chip` (new config).
- FX-66 Trading Card Wall: "five, six max… 20 shorts" @161-176. 20 tiles, 5-6 turn gold. New kind `grid` (his claim, no data).
- FX-73 Chart Reprise: "you just need the right clipper" @276. The chart returns as one gold bar, slow push. Hero kind reused.
New: FX-66 `grid`, FX-69/68 `bars` (FX-73 reuses it); FX-41 and FX-04 are configs of `title_card` and `chip`. Last five leaned on cards on the OBS panel, never a chart.
**Hero:** the lone gold bar (FX-69). Scott's channel as a linear bar chart: ~1,000-view uploads are slivers (@59-63), the first upload 10,000 (@70), then one gold 487,000 (@76, "second most popular"). FX-68 pins the buried Damon John episode ("two months old" @94, "buried" @104) at that bar. New kind `bars`. Read the count off the page (in L he says 486K).
**Accent:** Cormorant Italic, wght 600 (installed, variable).
**Better than I:** every number is read off the page and said by him, on an honest scale (1K is invisible), where I drew a structure he taught.

## Format chosen: his REACTION toolkit, as a reel (stated, not asked)
Screen on top showing Scott's channel, his camera below, the white seam line, white Bebas Neue captions on the line, face-only beats
under black bars on his emphasis points, zooms into the screen where he points at numbers, motion graphics with crisp SFX, a subtle
bed. Why: the proof IS Scott's channel on screen (every number is read off the page), the reel is him talking to camera, and it is
the look his @affancuts audience knows from his Onyx reel (wade-reel.mp4). Differences from a reaction: no channel card, no showcase,
no sample plays; the hook is face-only from frame 0 (the screen shows his script until OBS 38.3).

## The cut (keep.json → author3 → splice/polish → measured pins → jointcheck)
- gap 0.30 s (YouTube-tight). Kept, in order: hook "cooked"; "it's actually not your fault"; this is Scott Clary, two weeks; averaging
  like around 1000; the first upload did 10,000; second upload 487,000; it's Scott's second most popular upload (LAST take); this
  podcast of Daymond John is two months old; this podcast was buried; so it was never about Scott or how he was interviewing; it was
  actually the clips, right? the clipper (LAST take); the right moments are not being extracted properly (LAST take); only a select
  moments from every podcast that qualify as clips, five six max; upload a full episode, forcefully extract 20 shorts (LAST take), no
  idea if they go viral, wasting money; and also what a lot of podcasters do (LAST take): hire cheap clippers or cheap editors who will
  charge a couple of bucks for clips to mass produce; you actually lose money in the long run; so it's much better that you get a
  better clipper; Scott trusted me, 600 million on my own; for you: at least someone who has done 50 million views by themselves,
  someone who knows how to clip properly and has that eye for virality; PAYOFF: the viral moments are still buried in all of your
  episodes, so you just need to find the right clipper to pull them out.
- Out (budget / tangents): "if you're one of those people… not getting any views", "take a look at this… explain by an example", the
  whole-content-management aside, "boom boom boom… 900 to 1000 range", "it's sitting at 10,000 right now", "keep in mind", "the Shark
  Tank shark", "not something I capitalized on… brand new episode", "maybe Scott's not asking the right questions", "not the job of
  the podcast host… editing himself", "the whole conversation is up there on longs", faceless content, "everyone can edit these
  days", "you're running your podcast completely fine", "or do it yourself", "and actually upload it".
- Pins: `work/pins1.json`, every one measured (falign = forced alignment, endtest = Whisper on the candidate edge, dip = quietest
  5 ms). Polish had clipped the end of "views" (77.49 vs 77.54) and the S of "Scott" (222.86 vs 222.70), and re-joined "moments from"
  to "every podcast" (putting "any part from" back): all fixed at measured points.

## Taste calls (his to overrule)
- "clips" in "that qualify as clips" is swallowed (no Whisper pass hears it); the caption keeps his word.
- Hook line 2 = "it's actually not your fault" (22.49, the line the brief quotes). His later "it might actually be not your fault"
  (27.48) reads as a softer hedge, not a retake of a flubbed line; to swap: keep.json entry 2 → [47, 53].
- "like" stays in "averaging like around 1000 views" (a 20 ms gap: cutting it would clip a word).
- "and also" stays in "and also what a lot of podcasters do" (continuous voice into "also").

## The look (column M; build_plan.py docstring)
- Hero: FX-69 the lone gold bar on an HONEST linear scale (18 other tiles read off the page, 203 to 5.9K, + our first upload 10K are
  slivers; our second, 487K, one gold bar), pinned "the Daymond John episode / our 2nd upload · an old episode", "buried" stamped;
  FX-73 reprise at the end ("the right clipper", slow push). Then FX-41 ghost "COOKED" + a big two-line hook visible on frame 0,
  FX-04 era pill "SCOTT CLARY · week 2" through the proof, FX-66 the episode grid (20 tiles → 6 gold "5 or 6, max"; 20 forced shorts
  → "?" → 14 fall away "wasted money"), the screen's own Popular sort as a still card (#2 ringed), a second honest bar pair
  600M (him) vs 50M+ (the minimum).
- Screen proof: the channel header (480K subscribers) → the Latest grid with gold underlines on nine tiles' counts ("493 TO 1K VIEWS")
  → push + gold ring on "Daymond John's $1B Jersey Marketing Tactic" (count-up 10K) → push + ring on "Daymond John Almost LOST $250M"
  (count-up 487K, its 1.1K / 373 neighbours in frame) → the Popular sort still (OBS 81.0). Every lesson beat after that is a graphite
  STAGE over the panel (the static page never sits legible behind "it's the clipper").
- Accent face Cormorant Italic wght 600; entrance "focus" (new); captions white Bebas with ONE gold emphasis word per chunk where it
  carries (cooked, fault, 10K, 487K, buried, clipper, 600, 50 …), one constant position on the seam line.
- New kinds live job-local in `mgx.py` (overlays.py patched at import: the shared toolkit is untouched while the J-L builder runs it).
- **Better than his last reel (wade-reel.mp4):** every number is the screen's own, first ringed on the page, then put on an honest
  scale where 1K is invisible next to 487K; the hook is on frame 0 in big type; the lesson is staged as motion graphics instead of a
  static page behind his face.
- Reading check: head yaw/pitch over the cut (`work/headpose.py`, `work/read-sheet.jpg`): sustained turns to the screen only at
  5-25.5 s (him looking at the Scott numbers he points at); after that only 0.4-1.0 s nods with eye contact. No reading span: no cover needed.

## Audio
- Voice: house chain +10 dB into the −6 dBFS limiter (his talk −27.5 LUFS on the cut → −18.6 LUFS after the chain, 0.96 % of samples over
  the limiter threshold), `plan.voice_gain = 10` (apply --window → lanes/premiere/audio-polish.py).
- Bed: Epidemic "A Mistake (Instrumental Version)" by Particle House (303ac447-13b2-3e88-b37c-7877610c0f77, never used before: checked
  every BRIEF + every job's audio folder, `work/beds-used.txt`), from its sustained entrance 6.224 s (workflows/music-onset.py), flat
  at −21.9 dB = ≈13 LU under the voice (bed −9.7 LUFS over the used span), 2 s tail fade (apply.py). `work/music.json`.
- SFX (job slices `audio/sfx/`, `plan.sfx_dir`; measured by `work/sfx_measure.py`: tonal prominence > 1 kHz ≤ 17.6 dB, phone band
  checked, hits high-passed at 90 Hz, trimmed to the transient): m-stab (Epidemic 69deff59 "Cinematic Hit, Stab, Filter Tail", new),
  m-crunch (91c686bc "Stinger, Impact, Crunch Hit", new), m-impact (crunch + the new sub dive b1928b73 at −9 dB, max −1.0 dBFS),
  m-accent (7ef84c54 "Stinger, Impact, Reverb, Pitch Down", new, high-passed 140 Hz: replaced the kit's cd3-hit-bright, which J
  (Brad) uses for its push landings), m-rise (kit mc-riser-short, cut to end ON its crest), whoosh-m-res (4659952a "Whoosh, Resonant, Low Passed",
  new), whoosh-m-clean (kit cd3-whoosh-clean). Rejected by the tonal test: "Riser, Cinematic Reverse Glass 01" (52 dB), "Metal,
  Impact, Clean Ping" (44 dB), "Stinger, Hihat Hit" (22.9), "Metal Kick" (24.9). J-L checked 2026-10-27 ≈09:10: J's slices
  (sfx-spec.json) and K's (k-*) share no file or Epidemic id with M once cd3-hit-bright was swapped out; L had no sfx yet. 38 cues, none over 26 % of the total, never three at once (A2 + A4).

## Premiere run (when the gate opens; coordinator note 2026-10-27 06:40)
- Another session ("AffanWiz video edit") works in ABW10 on its own bin + sequence "CA-009 iPhone Duo Clip Angles": never touch them.
- EVERY QE / active-sequence / playhead operation goes through `lanes/premiere/ACTIVE-WINDOW.lock` (build_seq3 --create, apply --razor,
  --window, grabs, the final restore); switch with openSequence(id) and prove the target with two reads; address every other write
  BY NAME; restore the previously active sequence by id; check ACTIVE-WINDOW.lock is free before saving.
- The run, from the job folder (`T3=../_onyx-batch3-2026-10/reactions/tools3`, `T=../_onyx-batch-2026-10/reactions/tools`, every
  python with PYTHONUTF8=1; `work/pp_locked.py` = one step under ACTIVE-WINDOW.lock with the active sequence read before and
  reopened after, proven; apply.py's own steps take the lock themselves):
  0. gate: REACTIONS-RUN ▶ STATUS = all three PREPARED and no `_onyx-batch2-2026-10/.locks/premiere.lock`; then
     `mkdir ../_onyx-batch2-2026-10/.locks/premiere.lock` + an `owner` file ("shorts-cooked-not-your-fault reel builder <time>");
     `node ../../lanes/premiere/premiere-bridge.mjs ping`; the template "Onyx reaction template (empty)" must exist (else
     `$T3/mk_template.py`); NEVER touch "CA-009 iPhone Duo Clip Angles" or its bin.
  1. `python $T3/build_seq3.py seq.json --import` (bin "Onyx batch 5 reactions (2026-10-27)", OBS + C1407 + "C1407 (video only)")
  2. `python work/pp_locked.py python $T3/build_seq3.py seq.json --create` → "Shorts cooked reel"
  3. `python work/pp_locked.py python $T3/build_seq3.py seq.json --place` then `--style` then `--verify` (OK expected)
  4. `python $T/dump.py work/dump-real.json "Shorts cooked reel"` → `python work/dumpdiff.py work/dump-real.json` (0 expected) →
     `python work/sync_proof.py work/dump-real.json` (IN SYNC expected)
  5. `python $T/apply.py plan.json --razor` → `python $T/dump.py work/dump-layout.json "Shorts cooked reel"` → `python build_plan.py` →
     facex (`uv run --with opencv-python-headless --with numpy python $T/facex.py plan.json`) → `python mgx.py plan.json --check`
     (re-render with `--mg --only <id>` only if a graphic moved) → `python $T/apply.py plan.json --layout-check` → `--layout`
  6. `python $T/apply.py plan.json --window` (tracks + the house chain +10 dB into −6 dBFS) → `--overlays` (captions, 15 MG movs,
     38 SFX from audio/sfx, the bed) → `--verify` (0 problems) → `python work/sync_proof.py` on a fresh dump
  7. `python $T/apply.py plan.json --grab-only 0.3 4.3 7.5 10.6 14.0 17.8 20.2 23.0 26.5 28.5 31.5 33.5 42.9 46.6 50.0 53.5 59.5 62.0 67.5
     71.8 75.0 80.5 83.6` → `python $T3/grabsheet.py .` → `work/grabs-sheet.jpg`
  8. `python work/pp_locked.py --restore-by-name "Joe Appointment - raw cut"`, then save ABW10 only when ACTIVE-WINDOW.lock is free
     (apply.safe_save), `rm -rf ../_onyx-batch2-2026-10/.locks/premiere.lock`; BRIEF ▶ STATUS = PREPARED; REACTIONS-RUN row M.

## Download log
| # | File | Source | Size | Why |
|---|---|---|---|---|
| d1 | `audio/ES_A Mistake (Instrumental Version) - Particle House.wav` | Epidemic recording 303ac447-13b2-3e88-b37c-7877610c0f77 (WAV, full) | 63 MB | the bed (never used before) |
| d2 | `audio/sfx-src/69deff59-stab-tail.wav` | Epidemic SFX 69deff59-6c11-4578-a17d-3dd5e98d9663 | 1.2 MB | m-stab |
| d3 | `audio/sfx-src/91c686bc-crunch-hit.wav` | Epidemic SFX 91c686bc-8525-418e-ad3d-1888150afa20 | 0.6 MB | m-crunch |
| d4 | `audio/sfx-src/4659952a-whoosh-resonant.wav` | Epidemic SFX 4659952a-860b-4398-ae54-5a7084edd1fa | 0.6 MB | whoosh-m-res |
| d5 | `audio/sfx-src/b1928b73-sub-dive.wav` | Epidemic SFX b1928b73-0446-4560-888c-3443c05eef7b | 1.4 MB | the sub under m-impact |
| d6 | `audio/sfx-src/e53d5089-rise-glass.wav` | Epidemic SFX e53d5089-0d6e-4076-831c-049892baacd8 | 1.4 MB | rejected (tonal 52 dB) |
| d7 | `audio/sfx-src/67324cf9-ping-clean.wav` | Epidemic SFX 67324cf9-d1f2-4feb-bce1-f4bc486d8e4e | 1.2 MB | rejected (tonal 44 dB) |
| d8 | `audio/sfx-src/7ef84c54-stinger-pitchdown.wav` | Epidemic SFX 7ef84c54-2c4b-477e-8a54-b0852ac8128a | 0.7 MB | m-accent |
| d9 | `audio/sfx-src/730c0291-hihat-stinger.wav`, `1372ef9b-metal-kick.wav` | Epidemic SFX 730c0291…, 1372ef9b… | 1.1 MB | rejected (tonal) |
