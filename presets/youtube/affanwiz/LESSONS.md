# affanwiz — LESSONS (append-only; the channel's learning log)

One entry per lesson: **what was learned → what changed → where**. Newest at the bottom. A lesson that repeats
becomes a README number or a PLAYBOOK rule (say so in the entry). Written after every creator review and whenever
a job teaches something.

## 2026-09-23 · channel set up, monetized-before-gta6

- **AffanWiz is its own channel** (English personal brand promoting the creator's Skool community), separate from
  Affan Afterhours and from the Urdu `@affanwizu` reels. → its own preset folder, `presets/youtube/affanwiz/`.
- **The handover is a Premiere sequence with a pre-enhanced voice on A1.** → PLAYBOOK § Intake.
- **No script is supplied for the rough cut** (the creator said to go without one) → cut from the transcript alone.

## 2026-09-23 · rough cut, monetized-before-gta6

- **WhisperX word STARTS ran ~250–400 ms late after long pauses on this setup** (Enhance-Speech voice, near-silent
  room): 5 kept lines lost their first syllable ("I normally", "I got 10,000", "And this happened", "I don't even
  know", "I'll give you") because polish-boundaries only searches 250 ms before the claimed start, then grafts.
  → every IN after a ≥ 0.65 s pause gets an envelope check before replay (job `transcript/fixes.py`); tool fix
  suggested for `polish-boundaries.py`.
- **Merged/compressed words hid whole phrases**: "all it took" sat 1.1 s after where WhisperX put it and the cut
  dropped it. → slice re-ASR of every pinned or ⚠ boundary is not optional on this channel's footage.
- **The creator talks in retakes and restarts** (last take always wins, they re-stated "one more thing", "I would
  100%", "the good thing about longs"); ~58 % of the take was cut. → expect heavy retake grafting on every job.

## 2026-09-23 · overlays, monetized-before-gta6

- **The creator's overlay direction is now the channel's frame** (reference image supplied): no overlay fills the
  screen, tiny ones at 50 % width, Higgsfield-enhanced, animated matte under, drop shadow on each. → README § 1a (locked).
- **Higgsfield's upscaler invents text on tiny crops** (an 81×42 view-count badge came back with made-up lettering
  over the eye icon). A prompted `gpt_image_2_5` edit with the exact text spelled out is faithful. → README § 1a.
- **Spell out every glyph in the prompt, including emoji**: "screaming face" produced 😱 where the original was 😭.
  Compare every generated overlay with its original before it ships. → PLAYBOOK § Overlays.
- **The upscaler rejects images wider than ~2:1** and some portrait jobs at 4k (2k worked). Pad wide strips to 16:9
  with their own edge colour, then crop back. → PLAYBOOK § Overlays.
- **Premiere's Drop Shadow is invisible on a dark matte** (100 % opacity darkened it ~12 %). Shadows are baked into
  the overlay PNG; a video overlay's shadow is burned into its matte segment. → README § 1a.
- Spend on job 1: 67.5 Higgsfield credits for 28 enhanced overlays (incl. retries and one false "nsfw" flag).

## 2026-09-28 · rough cut, charlie-best-youtuber

- **The rough cut goes on the creator's own handover sequence, not a new one.** Job 1 replayed onto a new sequence;
  the creator objected on job 2. → PLAYBOOK § Intake item 5 (clear the handover sequence, replay onto it; the
  project backup is the safety net).
- **The creator doesn't want to approve steps one by one.** A project-local allow list (`.claude/settings.local.json`:
  Bash, Edit, Write, premiere-pro tools) lets the pipeline run unattended when auto mode's check is down.
- **Sync is measured every job: Sequence 12's voice sat 68 ms (4 frames) late** against the camera (job 1: 15 ms). The
  creator lines the Enhance-Speech mp3 up by eye; `sync-dual-audio.py` fixes it at intake. → PLAYBOOK § Intake item 3.
- **polish-boundaries overshoots tight cuts into the NEXT, killed word, and the mechanical reviewer missed all 13**
  (e.g. "...like a human. But" kept 321 ms of "But"). → after polish, run a LEAK SWEEP: any killed raw word
  overlapping a kept clip by > 60 ms gets its OUT moved to the energy dip before it (job `transcript/fixes.py`,
  `review/leak-fixes.json`), then re-ASR the tails. WhisperX starts can be early too, so confirm leaks on the envelope.

## 2026-09-28 · music drop-outs, charlie-best-youtuber

- **The music drops out wherever the creator punches in** ("when it gets zoomed in the music also gets pulled out… it
  feels like this is an important part"). Their punch-ins are static Scale 127 on V1. Sequence 12: 37 punch-ins →
  34 drops (adjacent ones merged), 58.8 s of music removed, every edge within 0.3 ms of the punch-in's.
  → PLAYBOOK § Per step, Music row (becomes a README look rule if it repeats on the next video).
- **Razoring through QE is clean**: `qe.project.getActiveSequence().getAudioTrackAt(n).razor(tc)` at the SEQUENCE
  fps (Sequence 12 = 60) splits the clip, and the right-hand piece keeps its level and the right source offset. Lift the
  piece with `trackItem.remove(false,false)`. Hard cuts only; fades are offered, not assumed.

## 2026-10-04 · the creator ports the Game Informer style (Affan Afterhours) to this channel

- **"We're picking up this editing style from my other channel for our next video"** (YouTube `EsnIehnZUhs`). It was
  our own job `gta6-hurricanes`, so the spec came from two sources that agree: the live ABW8 · Sequence 16 (read-only;
  identical to the published master but for one pop) and the master `Weather GTA.mov` through the five style tools.
  → `STYLE.md` (self-contained copy, numbers), README § 1 rewritten, § 1a partly superseded, PLAYBOOK rows 4–7.
- **YouTube blocks yt-dlp here without cookies** ("Sign in to confirm you're not a bot"). The creator's OWN video is
  already on disk: check `E:\Shorts\Abudance Wisdom Shorts Exports\Final Renders\` (match on duration; oEmbed gives the
  title without signing in) before reaching for a download. Their Chrome is the fallback they named.
- **The timeline beats the measurement on zooms and speed.** `style-report.py` saw 11 zoom steps and 4 "slowed
  stretches"; the timeline holds 22 cut zooms (14 inside nests) and every clip at 100 %. Read the live project when it
  exists; the tools are for exports without one. (`slowmo-scan.py` also crashed on a cp1252 console: fixed in place.)
- **Cut zooms sort into two families by what they land on**: emphasis 103–135 % on the claim, the punch 139–203 %
  re-centred on the joke and the self-roast. → STYLE § 2.
- **The drop-out tool had to learn nests**: in this style 14 of 22 cut zooms sit inside nests and every face run has
  a keyframed push, which a V1-only `getValue()` scan would miss or misread. → `lanes/premiere/music-dropouts.py`
  (static scale > 100 on V1 + inside nests, pushes excluded), proven read-only: exactly the 22 reference ranges on
  Sequence 16, 35 punch-ins on Sequence 12, all already silent.
- **Correction:** the Volume Level 0.1778 on every clip is **0 dB** in the DOM's encoding (v = 10^((dB−15)/20)), not
  −15 dB as job 2's notes said. Levels were never changed; only the label was wrong.

## 2026-10-04 · job 3, kick-fake-viewers (CA-003, ABW8 · Sequence 27): rough cut + assets from the script

- **The creator's joint spec is now the channel's: ~2 frames of silence out, ~1 in** (`POLISH_TAIL_MS=33
  POLISH_LEAD_MS=17`). At that tightness every edge matters: the mechanical review found 7 clipped words (a missing
  "thirty", "four thousand" without "four hundred channels", the 'f' of "For"/"First", the 's' of "views"), 9 mouth clicks
  followed by dead air at INs, and 6 fragments of killed words riding on edges. → PLAYBOOK § 2; keep the exhaustive
  exact-span review on every job at this tightness.
- **Split on the envelope, not on transcript gaps.** Splitting at every WhisperX gap ≥ 0.40 s cut a phrase in two
  ("He didn't say I | buy bots", a 15 ms overlap that aborted splice) and dropped speech WhisperX never placed
  ("masters | like"). `quiet_run()` in the job's build-cuts.py: split only where the audio is quiet ≥ 0.40 s.
- **The per-burst pass earns its keep on this channel too:** 6 hidden retakes ("dropped dropped", a second "and to be
  clear", "Bots can / Bots can", "Kick / Kick's", "or not or", "you guys" misplaced by 2 s). → PLAYBOOK § 2.
- **The creator films the script out of order and with life in between**: a phone call mid-take, a pickup line said
  30 s late ("Bots can be sent to you by anyone" → moved back to its script place), no cold open / close in the take.
  Read the whole raw before authoring; say what is missing.
- **Script → assets is a repeatable step** (PLAYBOOK § Assets). What worked: their Chrome to find + verify (signed in to
  X, so X search with date filters finds the clips the research cites); yt-dlp for X (no login) and YouTube via the
  `mweb` client (360p only); headless 2x page captures, or a 1.7x-zoomed full-size capture in their Chrome when bot-
  blocked. What failed: Reddit (blocked), X search for 2023 posts (empty), ppc.land (ad gate), Chrome tabs freezing on
  `scrollIntoView` after a CSS zoom (open a fresh tab), screenshots saved at the PREVIEW scale (never pass `scale` with
  `save_to_disk`), a CDN ".png" that was a JPEG (Premiere's File Import Failure modal blocked the bridge).
- **Transcribe every quoted clip before placing it**: the Adin clip held the quote at 6–12 s, a slur at 23.6 s, and
  offensive chat on screen; the script's second Adin quote was not in it at all. → `assets/SOURCES.md` columns.
- **A "let it play" clip gets its own gap**: replayed with a 16.9 s hole after "Listen to exactly what he says.", the
  clip on V2/A2 (never A1: audio-polish processes every A1 clip). `review/tools/replay-gap.py`.

## 2026-10-13 · the channel moves to the IGN-missions style (STYLE.md v2) — Sequence 27 restyled

- **"Replicate that style exactly for the AffanWiz channel"** (Afterhours video 22, 8:17). It was our own job
  (`gta6-ign-missions`, Sequence 39), so the spec came off the creator's FINAL timeline (read live, read-only) + the
  published master through the style tools + every graphic sampled entering/settled/leaving → `STYLE.md` v2, the v1 Game
  Informer port kept as `STYLE-v1-game-informer.md`. What changed vs v1: **graphics = full-frame "IGN dossier" plates +
  alpha overlays** (blurred footage plate, warm-white Inter type, pink underline that draws, refined UI diagrams), not inset
  cards over gradient mattes; b-roll insets sit over their OWN blur; **premium SFX** (soft whoosh, pen line, glassy ticks,
  chimes) instead of pops; **no face push** (no nests), cut zooms median 135 %; music beds on their own track, out under
  every zoom.
- **Reuse the reference job's tools, re-anchored**: build-plan (word-anchored beats, edges on V1 cuts, neighbours butt),
  build-comps (same HEAD/helpers at 60 fps), build-plates, place-gfx, place-sfx, place-music, face-pass, active-window —
  copied into `projects/kick-fake-viewers/` and pointed at Sequence 27 (60.00 fps, not 59.94). Gotchas found adapting:
  the face planner snapped to clip STARTS only, so a zoom ran 3 frames into the Adin gap (snap to ends too); a section of
  advice outran a 160 s song (add a turn, the bed resumes in sync).
- **This script is proof-heavy**: 24 graphics at 3.7/min, face 53 % (reference 62 %); the first 30 s was all graphics
  until three short beats were handed back to the face (longest face-less run 12 s).
- **The "my theory" graphics name nobody and show no recognisable streamer** (the phone's feed is a blurred Kick Browse
  thumbnail): the theory must not read as an accusation.
- **The legal list goes on screen when the take misses it**: the reported-drops meter says "reported" (he never says it).
- **A plate is blurred, not anonymous: check every plate for readable text.** At σ≈26 and ×0.38, big type still reads: the
  N3on-chapter plate under the dot room (KM@15, his channel page) carried a legible business email. Change → g03 re-sourced
  to KM@140 (N3on on camera), placed as `g03-plate-v2.mp4`; the check = a contact sheet of `compositions/_bg/*.jpg` before
  placing. → `projects/kick-fake-viewers/build-plan.py`.

## 2026-10-22 · CA-007 "I Ranked Every Streamer's Content Machine" (ABW10 › "CA-007 Streamer Tier List") — STYLE v2, + the first "1 % better" pass
- **A spine graphic carries a list video**: the TIER BOARD (S/A/B/C/F, the thumbnail's layout) appears at every verdict as
  a compact SIDE board on the face (right third, x 1450–1850, dark glass card), the newest entry dropping in, and fills the
  whole frame once for the spoken recap. → `projects/streamer-content-machines/hf-graphics/gfx/build-comps-B.py`.
- **Side cards keep the face on screen while information lands** (chapter tags top-left for the five archetypes, the
  census / Expedia / clipper-math / recipe cards on the right): a proof-dense script got 25 full-frame graphics (3.5/min)
  + 17 side overlays, face 50 % (the script's density; the reference was 62 %, CA-003 53 %). The no-stray-frame gate skips
  side overlays (they never cut the face). → `build-plan.py` (region 'side'), `review/gate-frames.py`.
- **A fresh, wide SFX set per job** (the 2026-10-21 variety note): 53 Epidemic files in 12 classes, every one ≤ 20 dB tonal
  prominence, takes rotated in time order (none twice in a row) → 157 cues over 42 distinct files. Real bells/chimes all
  fail the prominence rule (21–86 dB): the "chime" class is soft timpani. → `sfx/LIBRARY.md`, `build-plan.py` § SFX.
- **The take, not the script, sets the numbers**: on-screen numbers follow his words; live pages had moved (xQc TikTok 48 vs
  his 47, Adin 5.8M vs 6M, Speed's best Short 30M vs 28M), so captures are cropped/dimmed where their own number competes.
- **WhisperX merges repeated lines on a heavy-retake take**: rebuild the words per energy burst (faster-whisper per burst,
  wav2vec2-aligned per burst, numerals keep faster-whisper) and measure every cut edge on the envelope; a spectral check
  catches clipped fricatives ("five" played as "ive"). → `projects/streamer-content-machines/review/tools/`, `transcript/build-cuts.py`.
- **ABW10's 59.94 sequences display DROP-FRAME**: QE razors need DF timecode (lab-notes 2026-10-22).

## 2026-10-23 · CA-007 review (Tella walkthrough) — four must-fixes ("otherwise I literally cannot upload this")
- **Lips out of sync at 1:24, 1:56, 2:50, 3:22, 3:49, 4:59, 5:50** → my 2026-10-22 stray-razor "heal" (`.end =`) SLIPPED 50 V1
  pieces (−3 … −240 frames); no gate compared V1 with A1. Change → V1 rebuilt from HIS A1 with a video-only subclip, zoom edges
  pre-split (no QE razor), `work/sync_audit.py` = 0 off; the audit is now a gate after every V1 write (PLAYBOOK + lab-notes).
- **"Whenever I'm looking down reading off the phone … cover the whole thing"** → head-pitch measurement (`review/tools/look_down.py`),
  covers on every ≥ 60 % reading clip (37 → 0 s visible), the archetype titles full-frame, side cards that sat on reading lines
  made full-frame. Face share falls to ~34 % (his ask). → PLAYBOOK rule.
- **"SFX very cheap … recycling one sound effect … I need variety, crisp, expensive"** (v1 had 42 files, but 44 near-identical
  ticks/thuds dominated) → a new premium set (`sfx2/`, 77 takes in 16 classes), 157 → 110 cues (a pen per underline and a click
  per list row were the tick-fest: `THIN` in `build-plan.py`), no take more than 3 times or twice within 60 s, and a class that
  runs dry BORROWS a sibling class's take (`FALLBACK`) instead of repeating: 69 different files. → PLAYBOOK rule.
- **Head-pitch 40–60 % ≠ reading**: the 12 such clips on CA-007 were all camera-facing looks/gestures; real reading = head
  tipped fully down (compare against a ≥ 60 % frame, `review/frames/ref-reading.jpg`). Eyeball them; don't cover by number.
- **"A clean animation each minute prompting them to join the Skool community"** → CTA side cards + a full plug card. → PLAYBOOK
  (the channel's CTA exception). Once the reading covers took the face away, 3:00–5:00 had NO face window: that minute's CTA rides
  INSIDE a full-frame comp as a chip (same template, scaled .85, top-left above the comp's own rows), never skipped; a fourth CTA
  inside 70 s at the end was retired instead. Every CTA line is his words (his ask + the plug in the take), none invented.
- He cut two lines himself ("$40 per 100,000"; "CaseOh is also"): his A1 became the EDL (`work/edl_from_a1.py`); his hand wins.

## 2026-10-27 · CA-009 "Speed Bought the iPhone Duo. 20 Clippers Got Nothing." (ABW10 › "CA-009 iPhone Duo Clip Angles") — built with CA-007's fixes in from the start
- **Reading in SUNGLASSES is a head TURN, not a head drop.** Pitch never held on this take; the scripted lines (cold-open numbers, "212,000
  views", "Mistake number one", the Oct 1 list) are all head-turned to his left (yaw proxy ≥ 0.27 on ≥ 50 % of a segment), the improvised
  lines sit at yaw ≈ 0. Measured over the whole RAW before cutting (`projects/iphone-duo-clip-angle/review/tools/pose_raw.py`, calibrated by
  eye on `review/pose-bins.jpg`), mapped onto the cut (`reading.py`), and asserted in the plan + on the live V2 (`reading_gate.py`): 0 s
  visible from the first draft. → PLAYBOOK rule 2 now has a yaw half; measure BOTH every job.
- **Lip sync by construction, not by repair:** replay linked A/V by name, then re-lay V1 from a video-only subclip pre-split at every zoom
  edge (`work/rebuild_v1.py`): 0 frames off on 206 pieces, no QE razor, no `.end =` anywhere. → the default V1 build for this channel.
- **The take was improvised AROUND a written script** (CA-009 in creator-shorts/; START-HERE said "no script"): the script is the capture
  shopping list and the fact sheet, the take decides the cut and the copy. The number was CA-009, not CA-008 (that is Zack D. Films).
- **On-screen numbers vs live data:** his "23 Shorts, 20 under 5K" is ~100 / 80 today; "212K" is a 61 s HORIZONTAL long-form (now 330K);
  "crops, flips, speeding it up…" is not YouTube's list (theirs: "minor technical edits", "VO descriptions of what's happening on screen");
  "requirements doubled" applies to NEW YPP entrants from Feb 1 2027. Shown as his words, credits quote the real source, all flagged.
- **A real thumbnail never carries a typed label it does not match** (review r1: the 1,200-view card used a Short titled "…Hits 62 MILLION
  Subscribers…"): pin a real lookalike title, or use a typed card with no real thumbnail.
- **HyperFrames renders serve gfx/ as the root:** relative `assets/…` in a comp under compositions/ 404s in the RENDER (fonts + images fall
  back silently) while the probe passes. A junction gfx/assets → compositions/assets fixes it; check a frame from every RENDER, never only the
  probe. MBLUR_SS=8 is refused at 59.94 (> 240 fps capture cap): SS=4 max. One render is capture-bound (CPU 5 %): 3 parallel slots.
- **The edit-review loop earned its keep:** 3 rounds, 11 + 4 + 1 verified defects (edge strips under a tilted wall, same-slot swaps,
  arrowheads 16° off a curve, underlines drawing at 2.5× the spec, a 0.43 s hold on the plug card's last row, a cursor fleck on a crop).
- **Music:** his four STYLE § 4 beds + ONE new bed (Grizzy, hopeful, the solution section), level-matched by measured LUFS (−9.8 source →
  −25, same −34.8 as his beds), out under every zoom; laid as pre-cut pieces (no QE razor).

## 2026-11-02 · CA-009's verdict read off his finished ABW10 sequence (read-only), at the start of CA-010
- **He kept the whole graphics language** (V3 37 = all 36 graphics + the chip), **81 of 84 SFX**, the beds (50 pieces), and replaced A1 with his
  own Enhance-Speech bounce (`CA-009iPhoneDuoClipAngles-esv2-16p-bg-10p-music-10p.mp3`). → the STYLE v2 build + CA-007 fixes are the right default.
- **He cut 1.6 % more** (7:25.8 → 7:18.6; V1 206 → 197). Affan Afterhours GTA 24 the same week: −1.8 %. → tighten word edges / mid-line pauses
  ~2 % on the first draft; check every joint by re-transcribing the cut audio (`projects/viral-clip-method/review/tools/joint_asr.py`).
- **The recording folder is not the channel**: CA-009 arrived from `X:\Recordings\Onyx\`, CA-010 from `X:\Recordings\Afterhours\` (and was briefed
  as a GTA edit). Transcribe first, match the take against `creator-shorts/CA-NNN-*`, then pick the preset.

## 2026-11-02 · CA-010 rough cut: the fresh-eyes second pass found what word timings hide
- **WhisperX alignment hides real stumbles.** It squeezes words to 20 ms or stretches them over pauses, so "uh"s, "I- I", "in the- in one",
  "that- that doesn't ha-" sit inside kept spans, and a killed word filed after the edge escapes the leak sweep. The joint ASR alone missed them.
  On CA-010 the Sonnet mechanical reviewer found **43** with an unaligned-voiced-run scan on the 10 ms envelope plus a whole-segment ASR.
  The flow reviewer found 5 more retakes and stumbles. Net: 13:20 → 12:41 (−4.9 %), well past his usual −1.6 %.
  → For every take of his: run the envelope scan of each kept segment for voiced runs no aligned word covers (tools:
  `projects/viral-clip-method/review/fresh-eyes/`), then re-hear every changed joint.
- **Every fix is written as a raw-time edit, not a word index**: REMOVE (a, b), EARLIER_IN, ADD, in a pass after the word edges
  (`projects/viral-clip-method/transcript/build-cuts.py` § FRESH-EYES MECHANICAL PASS). Word-index pins cannot express a sound no word covers.
- **The disfluency-prompted ASR invents "uh" at joins** (the "through my, uh, faceless" case). Before cutting a real word, re-hear with
  `PROMPT=""` (`review/tools/hear_cut.py` now reads it). Whisper also silently drops swear words ("bullshit") in a whole-cut pass.
- **Flow findings vs the channel rule:** kept his "small little recap" / "short and sweet" remarks and "number one" with no "two". These are
  improvised bits (PLAYBOOK § 2); they were offered to him as optional trims, not cut.

## 2026-11-03 · CA-010 draft (viral-clip-method): what the build taught
- **His own Shorts as plates need cleaning, twice over.**
  - A centre 16:9 crop of a 1080x1920 AW Short shows the burned-in captions through a σ≈26 blur. Take the band ABOVE the captions.
  - The Shorts fade through black between shots (8–16 frames), so a straight plate "breathes" to black. Drop every frame whose
    black-referenced luma is < 60 % or > 150 % of the Short's median, ± 4 frames.
  - Tool: `projects/viral-clip-method/assets/video/make_clean.py`, plates via `hf-graphics/gfx/build-plates.py` (SRC = the clean files).
  - The letterbox-edge lines that move per shot are accepted texture.
- **Snap graphic edges to the ZOOM razors too**, not only to the EDL cuts. `review/gate-frames.py` caught 3 slivers 14–20 frames off a
  zoom edge. `build-plan.py` now reads `transcript/face-pass.json` razors into its CUTS.
- **A rule-4 CTA cadence needs the plan to check the gaps**, not only target times: two gaps of 86 s and 103 s slipped through because the
  face windows near the targets were taken. Fix: move a card into the nearest ≥ 3.6 s window, or add one there.
- **Labels vs quotes (round-1 ruling):** labels inside graphics may condense or address the viewer. Quote marks only ever wrap his
  EXACT words.
- **Readable lines rise on their clause start, never on their last word** (g04/g11/g48: lines visible 0.3 s). Titles rise on the
  word that says them, not at frame 0 (g08/g14 were 0.9–1.1 s early).
- **Tooling:** `workflows/graphics-qa.py` needs `PYTHONUTF8=1` on Windows when the plan carries curly quotes. Renders before a comp's
  `gfx/assets/` existed fell back to system fonts while the probe looked fine: always check one frame out of the RENDER.
- **Usage:** 3 Sonnet builders + 6 Sonnet review passes (3 rounds) built and converged 64 overlays + 46 plates. The builders reused CA-009's
  helper code only.
- **Shared ABW10:** the Onyx batch also uses `projects/_onyx-batch2-2026-10/.locks/premiere.lock`. Take it too around saves.
- **A new music bed is checked for vocals BEFORE it is laid.** Read the Epidemic `vocal type` tag through the connector
  (`SearchSimilarToRecording` / search results carry `tags`); a bed must say "no vocals".
  - Twice in one job a vocal take nearly went under his voice: the vocal Grizzy (the instrumental is "Grizzy (Instrumental Version)"),
    then "Pacific Coast Cruisin", tagged "vocal presence".
  - CA-010 ships 'fresh perspectives' (no vocals) as the sixth bed. His five beds hold 722 s, so a video longer than ~12 min needs one more bed.

## 2026-11-03 · CA-010 after the hand-off: his edits + the head-steady lock (viral-clip-method)
- **His edits after the 15:08 hand-off are data** (read back by name at 17:15, before any write):
  - Two V1 trims, both rippled through every track: the tail of "…if you are building a short channel, there might have be(en)…" (raw
    324.2–329.9, −0.52 s) and "…transferred into another niche." (raw 566.1–568.0, −0.57 s). Lesson → a line that trails off into a
    half-word or a restated clause gets its tail cut in the rough cut, not left for him. File: the next job's `build-cuts.py` KEEP rows.
  - He replaced A1 with his own **Enhance Speech v2** export of the timeline (one mp3, razored once). So our audio chain on A1 is
    temporary on this channel. The replacement sits a constant 40–50 ms behind the picture as ffmpeg decodes it (cause unknown:
    not the MP3 padding, which ffmpeg strips); report it, never fix his A1.
  - Tools that assume A1 = camera audio (`work/sync_audit.py`) report "all out of sync" on his A1. Prove sync by cross-correlating
    his A1 against the camera audio instead.
- **The head-steady lock on a 1080p long-form = STATIC Scale + Position per V1 piece** (`projects/viral-clip-method/work/head_steady.py`):
  - The eyes are matched across every visible same-scale jump cut by least squares, with a pull back to his framing. Razors inside
    one take share a transform; joints under a full-frame graphic are free.
  - **One base scale per run between graphics** (100–108 %, the smallest that locks the run): a graphic hides the change, so a run with
    no jump keeps 100 %. A 1080p source never goes past ~111 %.
  - **His cut zooms must still read:** each zoom stays ≥ 1.15× (here ≥ 1.20×) the base beside it, so a run next to a 125 % zoom is
    capped near 104 %. That cap is what leaves most of the remaining jumps.
  - **A head TURN is not a lean:** an eye-gap change beyond ±12 % matches position only. Without that, six turned pieces went to 120 %.
  - **Side cards:** the reframe moved his head toward s02/s03 (45 → −28 px). Holding the card-side EAR's on-screen x (not freezing the
    piece) kept every card within 6 px of its draft clearance and kept more jumps locked.
  - **One take on both sides of a cut zoom keeps ONE framing** (a transform-equality tie, not a head match). The first apply solved
    each side toward its other neighbour and gave 20 of 33 such pairs different framings: a new shift at the cut back from the zoom.
  - CA-010: before, 6 of 51 visible jumps within dy ≤ 12 / dx ≤ 20 px / size ≤ 5 %; after, 35 of 51 (median dy 22 → 2–3 px).
  - He moves a lot inside a piece (median 24 px up/down, 44 px sideways over 2 s), so a static lock can match one side of a piece
    perfectly but not always both.
  - Next time, consider this at the face pass: build it from the start, and shoot tighter (or in 4K) for the headroom.

## 2026-11-03 · CA-010 UPLOADED: what he changed before posting (viral-clip-method)
Read back by name on ABW10 › "CA-010 Viral Clip Method" after he said he uploaded (read only, no writes): every clip's start/end/in on
V1–V3 and A1–A4, V1 Motion vs the head-steady plan, V2/V3 Motion, opacity, enable flags, track mutes, every SFX and bed level.
- **Clip times and V1 framing are unchanged since my 17:43 save.** The 17:43 snapshot held times and framing only, so for levels the
  check is against the 15:03 gate. He posted the head-steady lock as built: 320 V1 pieces at the plan's static framing
  (`work/head_steady.py --verify` 0 mismatches), with the 16 joints that still move left as they were.
  Lesson → a static per-piece head lock is acceptable to him on a long-form. Next job, build it at the face pass instead of after the
  hand-off. File: `presets/youtube/affanwiz/PLAYBOOK.md` (face pass), the next job's face pass.
- **One change after the 15:03 gate that the 17:15 read-back missed** (that diff compared clip times, not levels; when he made it,
  before or after 17:43, is unknown): **he raised the cold-open bed.** Loungin's first piece (0–9.3 s, under the g01 opening graphic) went from −20 to −10.5 dB clip level (+9.5 dB).
  The rest of the opening section stays at −20, and every other bed keeps its level. My 15:03 gate had checked it at −20.
  Lesson → on AffanWiz the music under the opening graphic sits ~10 dB above the body bed: the open is scored to hit, then the bed
  drops under his voice. This is one instance, so it stays a lesson until CA-011 repeats it.
  File: `work/place_music.py` SECTIONS (a separate first piece for the opening graphic) on the next job.
- **Everything else shipped as delivered:** all 46 plates and 64 overlays (side cards and Skool CTAs included), all 109 SFX at our
  levels and his 5 beds + 'fresh perspectives' at theirs. His whole hand on CA-010 was the two trims (−1.07 s), his Enhance Speech A1,
  and that +9.5 dB on the open.

## 2026-11-05 · CA-011 "Kai Cenat Accidentally Showed His TikTok Money" (kai-tiktok-money): pre-production
- **His brief for this one, voice:** "1 % better", "steal something from other channels", "whenever I'm looking on the screen, that's where you will be placing overlays". → `projects/kai-tiktok-money/BRIEF.md`; the channel's stolen-move log starts at `research/longform-style-radar.md`.
- **Reading without sunglasses is cleanly two-state on yaw:** humps at y ≈ 0.1 (lens) and y ≈ 0.4 (the screen, frame right), threshold y ≥ 0.27, checked by eye against scripted vs improvised lines (eyes visible). Most reading pauses die in the cut: raw 49 % turned, cut 26 %. Copy the tools from this job, and remove CA-010's `39 < t < 1006` window from `pose_bins.py` / `yaw_runs.py` first: it hid the cold open from the calibration sheet.
- **WhisperX squeezed a whole sentence** ("And according to reports, he made about another $7,000 in that one stream") into 3 s at prob ~0, while the real speech sits in three bursts 16 s later. `review/tools/burst_spans.py` flags these from coverage alone, with no ASR, so a loaded box only re-transcribes the bad bursts.
- **On a shared 8 GB GPU with Topaz running, WhisperX starved for 20+ min; CPU finished in about 20.** Check `projects/_onyx-batch2-2026-10/.locks/gpu.lock` first and go straight to `WHISPERX_DEVICE=cpu` when it's held.
- **Intake is a real copy, never a hard link:** a `chmod` on the link cleared the read-only flag on his original (restored, contents unchanged).
- **Silent frames of any YouTube video:** storyboard sprites from a `robots.txt` tab (no player, no ad, no sound). Method in `research/longform-style-radar.md`.
- **His sequencing answer on CA-011, 2026-11-05: "Yes, use defaults".** So: the Money Map gets built; "help other people out who can't afford your service" ends on "help other people out"; the Studio numbers go in type over his Short plates; 2 Sonnet cut reviewers + Sonnet builders + up to 3 Sonnet review rounds approved. → `projects/kai-tiktok-money/review/SEQUENCING.md`, `transcript/keep-rows.txt`.
- **CA-011 fresh-eyes pass, 2026-11-06:** the Sonnet mechanical reviewer found 20 more hidden stumbles on a READ take (a false start per ~15 s, e.g. "$25,000" said twice, "now there are" twice), so a read take hides as many as an improvised one. It also proposed one wrong fix: a burst after "a" was the vowel of "skill" after the /k/ closure. → Energy-only findings at a stop consonant get a re-hear before they are applied. File: `review/fresh-eyes/mechanical-report.md`, `transcript/remove-rows.txt`.
- **The cut fell to 5:04 from 10:37:** reading pauses die, so a read take cuts far harder than a talked one. Reading was 81.8 s of it. Face stays ~52 % with covers only where he reads plus the evidence beats.
- **Head yaw alone misses glances where the eyes move more than the head (CA-011, 2026-11-06).** With the yaw number at 0.00 s visible, an iris measure (MediaPipe iris landmarks at 10 fps, `projects/kai-tiktok-money/review/tools/gaze_raw.py` + `gaze_report.py`) still found four real glances the viewer could see, 1.4 s in all, while it cleared most of the turned-head frames as eye contact. It separates cleanly on this take: reading gx median 0.756 (5th pct 0.669), camera median 0.461 (99th pct 0.546), threshold 0.60. Run it on every read take after placement, 4 minutes on CPU. Change: four short beats on his own words (g11a, g12b, g12c, g12d), edges on razors already there.
- **Keep spare SFX takes before adding beats.** The rotation (at most 3 uses per file, 60 s apart) ran out of whooshes at four more beats, so new entrances use paper and tab clicks. That also fits "whooshes are texture".
- **CA-011 build, 2026-11-06:** a first pass of QA + full frames caught what the reviewers would have spent a round on: side-card fades cut at 22 % on their last frame, and camera pushes carrying copy to y20–y40. Check the end position under the push, not the layout position. **g11's closing build finished 0.04 s before its cut** because it was timed to its last word; a build goes as early as it must to hold about 0.4 s. **A line up 0.7 s before its word (g12) is the frame-0 rule misread:** frame 0 needs SOMETHING moving, a rule will do, and the line rises on its word. A sliced credit with " · " wraps with a dangling dot: one fact per line. Date a credit only when the source agrees with itself.

