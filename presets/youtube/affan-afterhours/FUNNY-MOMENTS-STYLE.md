# FUNNY-MOMENTS-STYLE.md — "funny campaign moments" cut from GTA 6 play, in Affan's own Urdu-channel style

## ▶ STATUS: v1 written 2026-11-19, buildable. Read this block first.

| | |
|---|---|
| State | **v1, usable now.** Built from ONE finished video plus TWO of his real Premiere timelines. Not a three-video average: see § 0. |
| Gap 1 | **YouTube is flagged BLOCKED** (`projects/_onyx-batch2-2026-10/.locks/youtube.BLOCKED`, 2026-11-19 10:43). `yt-dlp` got `HTTP 403 Forbidden` on the video stream of `lgUUlX1DZpE` (not a sign-in page, not a 429). Videos 2 and 3 were NOT downloaded, so their finished pictures were never seen. The hub clears the flag after one spaced metadata probe; then `research/urdu-funny-style-2026-11-19/dl.sh` fetches the missing two (it skips what exists) and `vstats.py` / `pip_track.py` / `sheet.py` in the same folder re-measure them. |
| Gap 2 | **RE8 (`9CyIYSM1gO8`) has no timeline.** The only local project (`Re8 Finale.prproj`) is a one-clip wrapper around the finished 900 s export, and that mp4 is not on disk. For RE8 only the length (15:00), upload date (2023-07-20) and title are known. |
| Gap 3 | `Don't Scream` was measured from its timeline only (exact cuts, zooms, SFX, audio), never seen as a picture. `Backrooms` was seen as a picture, but its project is a trim pass (§ 0). |
| To refine | After the flag clears: look at Don't Scream and RE8 frames (captions? memes? PiP?), then re-check § 3 caption rule, § 6 meme rule, § 9 music rule. Then calibrate on his first English hour. |
| Evidence | `research/urdu-funny-style-2026-11-19/` : `prproj/` (read-only copies + decoded JSON + `analyze_timeline.py`), `src/6U5zDE2ypaA.mp4`, `frames/` (contact sheets and stills: hook, busiest 60 s, five payoff sheets, glitch moments, PiP punch test, outro, GTA HUD check), `meas/` (scene, loudness, PiP tracks). Nothing committed, nothing uploaded. |

**Which style wins:** for "funny moments" the Urdu videos win over `HUMOR.md` / `CREATOR-HAND.md` wherever they differ (his instruction: "the editing style is pretty much something that we can replicate"). Both values are recorded in § 12.

**Label key:** MEASURED = read from a timeline or a frame, with the video and timestamp. ESTIMATE = inferred, scaled, or one-source. Nothing here is an average over three videos.

---

## 0. The three videos and what we actually hold

| id | title | uploaded | length | what is on disk | what it gives |
|---|---|---|---|---|---|
| `6U5zDE2ypaA` **Backrooms** | Brown Boys Get Stuck In The Backrooms | 2024-01-14 | 13:11.75, 1920x1080 60 fps | the finished video (downloaded) + `back.prproj` (sequence "Escape The Backrooms Game Footage", 791.75 s = the upload's length) | the finished PICTURE and audio mix; the timeline is only a TRIM PASS (see below) |
| `lgUUlX1DZpE` **Don't Scream** | You Scream You Get KISSED By Her | 2023-10-31 | 6:25.07 | `Don't scream.prproj` (sequence "2023-10-28 02-26-18", 385.07 s = the upload's length). **No video.** | exact cuts, zooms, SFX, audio edits of a real edit |
| `9CyIYSM1gO8` **RE8** | Horror Game GIVING Off HUM TV Drama Vibes, Resident Evil 8 Final Part | 2023-07-20 | 15:00 | stub only | length only |

**Honest reading of the two projects:**
- `Don't scream.prproj` is a REAL edit: one video track (152 clips), two audio tracks, one SFX track. Source is a single OBS recording `Don't Scream.mp4` with his face cam already baked into the corner of the picture. No text, no graphics, no music, no transitions, no Lumetri anywhere in the project. It was saved on upload day and its runtime matches the upload. This is the best evidence in the pack.
- `back.prproj` is a TRIM PASS, not the finished edit. It has zero effects and no graphics, yet the export has a title card at 0:00, captions, a CCTV meme, VHS gags and face-cam punch-ins. Its two source files ("Escape The Backrooms Game Footage", "Backrooms 2nd Recording Game Footage_1") were already-finished clips. So its 5.4 cuts/min is a FLOOR, not the video's cut rate. Where that captioned/punched layer was built was NOT found: the time-boxed search (AE Projects, After Effects auto-save, a CapCut drafts folder, Jan 2024 files on E:) was stopped before it finished and the CapCut folder listing never printed, so treat the search as INCOMPLETE, not as "nothing exists". Everything about captions, memes, glitches and PiP punches below is read off the export's FRAMES.
- The raw sources the projects point at (`E:\Recordings\...`, `E:\VODS\...`, `F:\sfx\...`) no longer exist on this PC: no raw footage survives, only the projects and the one downloaded export.

---

## 1. Layout — game full frame, face as a corner PiP

**Rule 1.1 (MEASURED, Backrooms):** the game fills the frame; his face cam is a hard-edged rectangle **flush in the TOP-RIGHT corner**. No border, no shadow, no rounded corners, no mask: the edge profile at 0:20, 1:00, 1:30, 2:30, 4:10 is a single sharp step.

| state | size at 1920x1080 | where seen |
|---|---|---|
| Recording 1, start | **576 x 324 px = 30.0 % x 30.0 %** | Backrooms 0:20, 1:00, 1:30, 2:30, 4:10 (left x=1344, bottom y=324) |
| Recording 1, later | 499 x 281 px = 26.0 % | Backrooms 5:30 to 10:30 (x=1421, y=281): the cam was resized between 4:10 and 5:30 |
| Recording 2 | about 588 x 340 px = 30.6 % x 31.5 % | Backrooms 10:39 to end (480p tracker, ESTIMATE) |

**Build value (ESTIMATE, rounded from the above):** face PiP = **Scale 30 % of a 1920x1080 camera clip, flush top-right**: size 576x324, Position (1632, 162) px. Use it as the same size for the whole video; do not copy the 26 % drift.

**Where the face cam lives in the English build:** in Urdu OBS recordings the cam was baked into the game picture. His English hour has the game (PS5 4K WebM) and the face (Sony + DJI) as SEPARATE files, so the PiP is a layer (V2). That is better: the face can be punched on its own (§ 4a).

**Risk, not measured:** a GTA 6 HUD may put cash, wanted stars or the clock in the top-right. In the only GTA 6 gameplay frames available (Extended Look, `E:\Bullshit Folder\Simone\...`) the visible HUD is an interaction prompt list at mid-right (x about 0.88, y about 0.40-0.50), which a 30 % PiP (y < 0.30) does not touch, but no HUD frame with the minimap/cash corner was available. Check it on the first hour (open question 2).
**Hub check, 2026-11-19 (CONFIRMED on xQc's launch stream, `projects/gta6-everything-new/verify/frames/F14-xqc-6h53m08-stash.png`):**
- The GTA 6 cash display (cash + bank, two lines) sits in the TOP-RIGHT, at about x 0.91-0.98 and y 0.02-0.09. A 30 % top-right PiP covers it.
- The minimap is bottom-left, and button prompts are bottom-right.
- So for funny moments the PiP can stay top-right (his style). On What If clips, where cash before and after is the evidence, the PiP moves, or the cash is shown with it off. Affan decides on hour 1.

---

## 2. Premiere track map (1920x1080, 59.94 fps sequence)

| track | content | notes |
|---|---|---|
| V1 | the PS5 game | Premiere cannot open the PS5 4K VP9 WebM: use the `hour_desk.py --mezzanine` HEVC file, Scale to fit 1920x1080 |
| V2 | his face (Sony camera), PiP | Scale 30, Position (1632, 162) px, hard rectangle. Time-aligned by `clap_sync` offset |
| V3 | inserts: TV colour bars, video memes, black gap | cuts only, no transitions (MEASURED: zero transition items in both projects) |
| V4 | optional: pop-words / captions | OFF by default (open question 1) |
| A1 | his voice (DJI mic as camera audio) | |
| A2 | game audio (PS5 file, game only) | |
| A3 | SFX | whoosh, colour-bars tone |

**Nesting (ESTIMATE, matches his CREATOR-HAND habit):** nest V1 + V2 per moment ("M01", "M02", ...) so a whole-frame punch (§ 4b) is a razor + static Scale on the nest piece. A PiP-only punch (§ 4a) is a razor + static Scale on V2 inside the nest or before nesting. In Don't Scream (MEASURED) everything is on one V1 with the cam baked in; that is the same thing as a nest.

---

## 3. The cut

### 3.1 Rhythm — Don't Scream (the exact timeline)
- **MEASURED (Don't Scream, whole video):** 152 clips in 385.07 s = **23.5 cuts/min**. Clip length median **1.92 s** (p25 1.19, p75 3.29, max 11.80). 30 clips under 1 s (20 %), 8 under 0.6 s, 20 over 5 s (13 %).
- **MEASURED:** clips starting in each minute `[37, 22, 24, 15, 21, 19, 14*]` (*the last bucket is only 25 s long: 14 clips in 25 s is about 34/min, so the video ENDS dense). **The first 60 s carries 36 edit points**; minutes 2-6 run 15-24/min.
- **MEASURED (Backrooms):** the trim pass is 5.4 cuts/min (floor); scene-detection on the export gives 18.3 hits/min (upper bound: game camera motion and caption changes also trigger it). Neither is "the" rate. Use Don't Scream's 23.5/min.
- **Agrees with the English hand:** CREATOR-HAND says 24.1-33.3 edit points/min.

### 3.2 What is kept and how it is joined (Don't Scream)
- **MEASURED:** **385 s kept out of a 2,442 s source span = 15.8 %** (source 0:54 to 41:36).
- **MEASURED, chronological only:** **0 of 149** source jumps go backward. Moments run in the order they were played. Do the same.
- **MEASURED:** 118 of 149 joins are forward jump cuts that drop a median **4.9 s** of source (largest 263 s); only 31 of 149 (21 %) are "razor splits" of continuous footage (the zoom is carved out of a running take).
- **MEASURED, moment size:** clusters of source separated by a skip over 20 s = **27 moments** (4.4 per kept minute), median **8.9 s** kept each (p25 4.8, p75 19.2, max 56.2). With skip over 8 s: 48 moments, median 6.9 s.
- **MEASURED, no slow cuts to black or fades:** no transitions in either project: hard cuts only.

### 3.3 Setup, payoff, exit (Don't Scream)
*Label: every number below is MEASURED off the timeline, but "the zoomed clip marks the payoff" is an ESTIMATE used as a proxy (the picture and voice were not seen). Treat setup/payoff/exit as the shape of his zoom placement, not a verified joke structure.*
- **Setup:** the clip before a payoff zoom has median length 2.38 s (p25 1.35, p75 5.89); inside a moment the first zoom arrives **4.1 s (skip>8 s clusters) to 6.1 s (skip>20 s clusters)** after the moment starts. The setup runs at 100 % scale.
- **Payoff:** a zoomed clip, median hold **1.25 s** (p25 0.88, p75 1.87, min 0.50, max 3.00). 25 of 40 are razor splits of the running take; 15 land on a jump cut (median skip 3.0 s).
- **Exit:** the tail after the LAST zoom in a moment has **median 0.0 s** (p25 0.0, p75 2.4-4.0 s). The moment ends on the zoomed clip, then the next jump cut. Total after the payoff starts: about **1.2 s (median) to 3 s**.
- **Following clip length** after a zoom: median 2.45 s (same as the 2.25 s of non-zoom clips).
- **ESTIMATE, fit to `hour_desk.py` (S9 suggests setup 5-18 s, end 1.5-3 s after payoff, 10-20 s total):** for this style, shrink the window: **setup 4-6 s, payoff clip 1-2 s, end on the zoom (0-2 s tail), total 6-10 s typical, 19 s only for a build-up, 56 s cap**.

### 3.4 Inside a moment
- **ESTIMATE:** where his voice or the game leaves a dead gap over about 1 s inside the setup, jump-cut forward (the median forward skip is 4.9 s).
- **MEASURED (Don't Scream, 4:08.10-4:10.20):** audio track A1 has NO clip for 2.10 s under a 145 % corner zoom while A2 keeps playing: the only audio removal in the timeline. Which track is the mic cannot be read from the project. ESTIMATE: it is a censor by cut (matches CREATOR-HAND "swears cut, not bleeped"). Backrooms export (MEASURED, 0:10 sheet): swears are censored in the captions with `*` and `$` ("ye b*tch a$$ hai").

---

## 4. Zoom rules (razor + STATIC scale, never a ramp)

**MEASURED (Don't Scream):** 41 Motion clips out of 152 clips (27 %) = 40 zooms + 1 stretch gag, **6.4 per minute**, **14.6 % of runtime zoomed**. All static (Scale + Position typed on the razored clip); one keyframed exception (§ 4d). Zoomed clips are shorter than plain clips (1.25 s vs 2.25 s median). Consecutive zoomed clips are rare: 31 single zooms, 2 doubles, 2 triples.

The 40 zooms are two different moves:

### 4a. Corner punch (geometry MEASURED, 29 of 40 = 73 %) — whole picture scaled around the TOP-RIGHT corner
*Label: the Scale / Position numbers are read from the timeline. That the top-right corner holds his face cam in Don't Scream, and that these punches land on HIS reactions, is an ESTIMATE carried over from Backrooms' layout (Don't Scream's picture was not seen).*
- **Scale 121-173, median 146** (bands: 2 at 100-125, 15 at 126-150, 12 at 151-173). Hold median **1.20 s**.
- **Anchor: the top-right corner.** Position = **(1920 x (1 - 0.5 S), 1080 x 0.5 S)** with S = Scale/100 (checked: 29 of 40 land within 0.05 of this). Examples: Scale 146 gives Position (518, 788); Scale 130 gives (672, 702). The view window becomes the top-right 1/S of the frame, so the PiP face grows to 0.30 x S of the frame width (Scale 146 gives 44 %) and the game is cropped to its top-right.
- Use it on a reaction beat where the game picture can be cropped for a second.

### 4b. Centred punch (geometry MEASURED, 11 of 40 = 28 %) — scale around the middle of the picture, not the corner
*Label: the numbers are measured. What each one points at (a scare, a face, a prop) was never seen: ESTIMATE that these are game moments, since they are not aimed at the corner.*
- **Scale 120-348, median 194.** Hold median **1.87 s** (longer than the corner punch).
- Centre anchor (Position 960, 540) on 5 of them; offset anchors on the rest (e.g. Position 0.5:0.40 at Scale 247).
- **All six zooms over 173 are this type:** 199 (1:12.31), 207 (1:31.61), 194 (2:22.94), 247 (2:29.88), 210 (3:49.76), 348 (1:04.93, hold 3.00 s). The biggest moments of the video.
- **Build default (ESTIMATE, decided here so nobody has to guess):** use it at about the measured density (11 in 6:25 = 1.7/min, so about **10-12 in a 7-minute video**), but ONLY on a candidate whose S11 payoff time is a GAME event (a big frame change or game audio transient, not just his voice), at Scale **195-210 centred, hold 1.5-2 s**; the single biggest game moment of the hour may go to 250-350 for up to 3 s. His voice beats get § 4a or § 4c instead. Revisit once Don't Scream's frames are measured.
- **Agrees with CREATOR-HAND bands** (120-150 normal, 160-215 big, 280-360 extreme once or twice a video).

### 4c. Face punch, PiP layer only (MEASURED on the Backrooms export, but built outside the timeline)
- The face cam grows **alone**: at 0:03.8 / 0:04.0 / 0:04.4 the lobby UI behind it is unchanged in size and place (lower-left region mean abs diff 1.0 against 0:02; the caption text accounts for the rest) while the PiP goes 30 % (0:03.4) to 40 % (0:03.6) to 50 % (0:03.8-0:04.4) to 40 % (0:05.0) (left edge 1344 to 1154 to 960 to 1154 px).
- **Peak size = exactly 50 % of the frame width (960 x 540, flush top-right)**, measured median 0.50 (max 0.60) in recording 1, 0.51 in recording 2.
- **Ladder: 30 % to 40 % to 50 % in two steps about 0.2 s apart** (sampled at 5 fps: ESTIMATE for the step timing), held median **1.8 s** (0.4-3.6 s), then back down in the same two steps.
- **Frequency:** 37 events in 10:39 of recording 1 = **3.5 per minute**; 6 events in 2:33 of recording 2 = 2.4 per minute (holds median 0.6 s).
- **Build values (ESTIMATE):** V2 Scale 30 / 40 / 50 with Position (1632,162) / (1536,216) / (1440,270). Use it when the game moment must stay readable behind his reaction; use § 4a when the game can be cropped.
- **Observation, NOT a rule (one export, small numbers):** 8 of 22 loudness peaks had a PiP punch within -1.5 / +2.5 s against a chance level of about 31 %, i.e. no better than chance, and the loudest game scare (5:59, -3.8 LUFS momentary) was left un-punched with the game carrying it. So in Backrooms the PiP punches follow his talking beats. Whether Don't Scream's centred game punches (§ 4b) sit on scares was never seen (no frames): UNVERIFIED until its picture is measured.

### 4d. The opening snap (MEASURED, Don't Scream 0:00-0:03.02)
The first clip is the only keyframed one, a Transform effect with **Motion Blur on**: Scale 100 to **165 in 0.083 s (5 frames at 60 fps)**, a slow drift 165 to 170 over 1.94 s (0.083-2.02 s), then a second snap 170 to **190 between 2.02 and 2.10 s**, and 190 holds for the last 0.92 s of the 3.02 s clip; position follows the same top-right corner anchor. Plus a 0.27 s whoosh on frame 0. The cut after it comes at 3.02 s. Use as the opening of the video (§ 8).

### 4e. Stretch gag (MEASURED, Don't Scream 2:52.02-2:52.57)
Uniform Scale OFF, **Scale Width 448, Scale Height 143**, Position (-0.967 : 0.694) normalised, **0.55 s**, between two 143 % corner zooms (a run of three). One in 6:25. **Agrees exactly with CREATOR-HAND** (Scale Width 248-928, 0.4-1.5 s, 1-3 per video, often on a 147 zoom). Keep: 1-2 in the hour video, on a mocking word.

### 4f. Zoom density by position (MEASURED, Don't Scream)
First 45 s: **10 zooms = 13.3/min**. 45-120 s: 4 = 3.2/min. 120-385 s: 27 = 6.1/min. **Open dense, then settle at about 6/min.**

### 4g. Never (MEASURED)
No drifting push-in on any clip, no 110/105 nest preset, no zoom ladders on the whole picture (the only ladder is the PiP's 30-40-50). Static scales only.

---

## 5. Slow motion, speed ramps, freeze frames

- **Slow-mo: NONE. MEASURED (Don't Scream):** no clip on any track has a speed other than 100 %. **MEASURED (Backrooms timeline):** one whoosh SFX at 110 %, no video clip speed change. Inside the Backrooms export's pre-finished sources slow-mo is UNMEASURED.
- **Speed ramps: none.** **Freeze frames: none verified.** `freezedetect` on the Backrooms export fired 0.3-1.8 s hits at 3:53-3:57 and 4:51-4:54; the frames are a static dark game screen, a Discord window, and a VHS "EJECT" blue screen: none is an edited freeze.
- **Conflict with `HUMOR.md`** (0.8x on the joke landing): **Urdu wins for funny moments: no slow-mo.** HUMOR's 0.8x stays only in his English commentary videos.

---

## 6. Meme inserts, glitches, graphics

**Timeline level (MEASURED, both projects): no meme video, image meme or graphic clip on any track.** What exists is below.

| device | where | spec |
|---|---|---|
| **TV colour bars + tone, full frame** | Don't Scream 2:59.61 (0.083 s = 5 frames); Backrooms 1:52.77 (0.10 s) and 13:11.65 (0.10 s, the last frame before black) | source file `TV colour bars test card screen with sine tone in 4K.mp4` (in at 6.39 s and 3.8 s), cut straight onto V1 with its own audio. **Same file as his English edits** (CREATOR-HAND: 0.20 s). Use **0.08-0.10 s** as a "channel change" at a section turn: about **1 per 3-6 minutes**, plus the last frame (Backrooms ends on it, then a single black frame). |
| **Face cam full screen** | Backrooms 0:42.10 (about 0.4 s) | hard cutaway to the face (no PiP) mid-moment. ESTIMATE: 1 per 10 min. |
| **Video meme, full frame** | Backrooms 0:05.0-0:05.5 (CCTV lightning clip with a date stamp, black and white), about 0.5 s hard in, dissolve out | baked into the export (built outside the trim project). ESTIMATE: 1-2 per 10 min, only where a line names the thing ("is that thunder and lightning?"). |
| **VHS "EJECT" blue screen** | Backrooms about 3:57 | a camcorder gag, about 1 s. |
| **Black gap** | none | (the Don't Scream "off-screen" Position clip was the stretch gag, § 4e) |
| **Title card** | Backrooms 0:00 (about 0.4 s, "MAP ONE / ESCAPE THE BACKROOMS", white serif, cyan and red offset outline) | Don't Scream has none. English build: only if the hour has a named map/mission; otherwise skip. |

**Image memes: none seen** in the Backrooms sheets (overview, hook, busiest 60 s, five payoff sheets).

---

## 7. Sound effects, meme audio, levels

### 7.1 What is in the timelines (MEASURED)
| video | sfx | at | file | clip gain |
|---|---|---|---|---|
| Don't Scream | whoosh 0.27 s | 0:00.00 (frame 0, with the opening snap) | `FREE Transition Sounds Effects! ｜ Swoosh, Swish, Whoosh.mp3` (in 30.76 s) | 0 dB |
| Don't Scream | whoosh 0.53 s | 0:41.31 | same file (in 28.21 s) | **-7.0 dB** |
| Don't Scream | colour-bars tone 0.083 s | 2:59.61 | the colour-bars file's own audio | 0 dB |
| Backrooms | colour-bars tone 0.10 s | 1:52.77 | colour-bars file | **+12.2 dB** (neighbouring game clip +4.5) |
| Backrooms | whoosh 0.15 s at **1.1x speed** | 10:39.40 (the source switch to recording 2; it is also the loudest moment of the video) | `10 Free Cinematic Whoosh Sound Effects.mp3` (in 38.37 s) | **-7.9 dB** |
| Backrooms | colour-bars tone | 13:11.65 (end) | colour-bars file | 0 dB |

- **SFX density: 3 in 385 s (0.5/min), 3 in 791 s (0.23/min).** Whoosh at the opening and at a section/recording change; colour bars at a "channel change"; the whoosh sits **-7 to -8 dB** under its clip level.
- **No Vine boom, bruh, bass-boost, cricket or any meme audio in either TIMELINE.** (Inside the Backrooms export's baked sources: UNMEASURED, you cannot name a sound without hearing it.)
- **Other audio edits (MEASURED):** Don't Scream: one game/voice clip at **-5 dB** (3:30.16, track A1), the 2.10 s A1 gap (§ 3.4). Backrooms: the game-footage audio clips are at **-4 dB** (44 of 50 gain-edited clips; others -3.4 to -3.7, +4.5, +12.2, -10).
- **Export loudness (MEASURED, Backrooms export):** integrated **-15.4 LUFS**, LRA 12.2 LU, true peak -0.8 dBFS; momentary median -19.9, p90 -12.2, max -3.0 (the 10:38 scare). 16 % of the time above -14 LUFS. It is HOT and wide: the scares are loud on purpose. The English master chain wins (`rough-cut` static chain, -17 LUFS pre-limiter, -6 dBFS limiter); keep the shape (quiet talk, loud scares) but not the -0.8 dBTP.

### 7.1b Game audio against his voice — a GAP, with the nearest existing number
- **Not measured for the Urdu videos:** only the finished mix of Backrooms was available (one stereo track), and Don't Scream's two OBS audio tracks sit untouched on A1/A2 with no volume edits (one clip -5 dB). Their voice-to-game balance cannot be read.
- **In the English build the two are separate files** (PS5 file = game audio only, camera/DJI = voice), so the balance must be set. The only existing number is the Shorts "Kai" style (`projects/gta6-launch/tools/styles/kai.json`, audio block): voice target -17 LUFS, limiter -6 dBFS, **game bed 10 dB under the voice**, mix target -13 LUFS, true peak max -1.5. **ESTIMATE for this video: game 10 dB under his voice while he speaks, back up in the gaps and on game events**; verify on hour 1. Voice first check (LAUNCH-MODE.md STATUS): the DualSense mic may have put his voice into the PS5 track.

### 7.2 Where the SFX come from (rule)
1. **Epidemic Sound first** (his library; connector in `.mcp.json`): search whoosh / swish / transition for the whoosh; a short test-tone or "TV static / beep" for the colour-bars tone if he does not want the ripped file.
2. **Risk for his call: three sound files in these videos are YouTube rips, not Epidemic:**
   - `F:\sfx\FREE Transition Sounds Effects! ｜ Swoosh, Swish, Whoosh.mp3` (a YouTube "free" compilation: the licence of its parts is unchecked);
   - `F:\sfx\10 Free Cinematic Whoosh Sound Effects.mp3` (same);
   - `F:\sfx\TV colour bars test card screen with sine tone in 4K.mp4` (a test-card clip from YouTube: low risk but not cleared; it is already in his English edits).
   - `F:\sfx\TV Noise - Green Screen Animation.mp4` is in the Backrooms project's media pool but is NOT on the timeline.
   `F:` is not mounted on this PC today. Mark these as a risk and, for a monetised English channel, replace with Epidemic equivalents unless he says otherwise.
3. **Meme audio (vine boom, bass-boost, awkward cricket):** he uses them in English edits (CREATOR-HAND § 4, clip gain -11 to -15 dB, -27, -15) but **none appears in the measured Urdu timelines.** Default for funny moments (Urdu wins): none. Any meme clip audio would be a copyrighted-clip risk: his call (open question 3).
4. **CONFLICT recorded, not settled here:** `memory/feedback-gta6-gameplay-first.md` (his 19 Nov rule, made on the faceless "Everything New In GTA 6" video) says GTA 6 videos get **full SFX plus an Epidemic music bed**. The Urdu timelines have 3 SFX and no bed. The spec default follows the Urdu style because he named it for this format, but the 19 Nov rule may be meant to cover every GTA 6 video: open question 3.

---

## 8. The hook (first 15 s) and the ending

### 8.1 Don't Scream, 0:00-0:15 shot by shot (MEASURED)
| t | clip | what |
|---|---|---|
| 0:00.00-0:03.02 | 3.02 s | **snap zoom on the face corner** 100 to 165 in 5 frames, drift, 170 to 190 in 5 frames, motion blur; **whoosh 0.27 s on frame 0** |
| 0:03.02-0:04.70 | 1.69 s | plain |
| 0:04.70-0:05.29 | 0.58 s | plain |
| 0:05.29-0:06.31 | 1.02 s | plain |
| 0:06.31-0:07.97 | 1.67 s | plain |
| 0:07.97-0:10.43 | 2.45 s | plain |
| 0:10.43-0:11.16 | 0.73 s | zoom 133 |
| 0:11.16-0:12.81 | 1.65 s | plain |
| 0:12.81-0:13.96 | 1.15 s | zoom 128 |
| 0:13.96-0:18.08 | 4.12 s | plain |

10 clips in 15 s. The video **starts mid-play (source 0:54, the first 54 s of the raw are dropped)** with no title, no talking-intro, and voice from 0.000 (agrees with CREATOR-HAND: voice from 0.000).

### 8.2 Backrooms, 0:00-0:15 (MEASURED, export frames)
Title card (about 0.4 s) then the lobby with big word-pop captions (the PiP punches to 50 % on "turb-", "TURBULANCE"), a 0.5 s CCTV meme at 0:05, then gameplay with captions. No whoosh, no colour bars in the first 112 s: the first take runs **112.77 s uncut** (timeline, MEASURED) before the first colour bars.

### 8.3 Rule for the English hour (ESTIMATE from 8.1)
Open on the **strongest payoff of the hour**, not on a title: the first clip is a 3 s snap-zoom on the face corner (Scale 100 to 165 in 5 frames, then to 190), motion blur on, whoosh on frame 0, voice from 0.000, then plain cuts about every 1.5 s for 15 s with 1-2 face punches (133, 128). Then the chronological run.

### 8.4 Ending (MEASURED)
- **Don't Scream:** the last clip (6:23.87-6:25.07, 1.2 s) is a corner face punch at 135 %: a cold end on the face. **Agrees with CREATOR-HAND** (ends on the face, a cut zoom).
- **Backrooms:** no outro or end card: the video runs out in the last game scare, then **0.10 s of colour bars and one black frame**.
- **Rule:** end cold on a face punch (135) with no outro graphic; the colour-bars flash on the last frame is optional (ESTIMATE).

---

## 9. Music

- **MEASURED (timeline level):** neither project has a music track; Don't Scream is voice + game audio + 2 whooshes + 1 tone, Backrooms the same. **Default: no music bed in funny moments.**
- **UNMEASURED:** whether the Backrooms export's baked sources carry music (cannot be named without hearing; no spectral test run).
- **Conflict with CREATOR-HAND § 5** (Epidemic bed -20 to -27 dB, out under every cut zoom): **Urdu wins for funny moments: no bed.** The "music out under zooms" rule is moot with no bed.
- **Second conflict (his 19 Nov rule):** `feedback-gta6-gameplay-first.md` says GTA 6 videos carry an Epidemic music bed. If he wants it here, use the CREATOR-HAND bed numbers (clip gain -20 to -27, about 15 LU under voice, out under zooms). Open question 3.

---

## 10. Text on screen and captions

**Evidence is 1 video, two looks (Backrooms), plus a timeline with none (Don't Scream). The default is NONE.**
- **Don't Scream: no text of any kind in the project** (MEASURED). Whether the finished upload has burned-in text is UNMEASURED (video not seen).
- **Backrooms export (MEASURED, frames 0:03-0:35, 11:00-12:59):** two caption looks:
  - **Recording 1 (0:00 to 10:38):** big bold rounded words, white or orange fill with a thick **purple / blue / orange outline** and a drop shadow, lowercase and ALL CAPS mixed, centre-low (y about 0.45-0.9), word-by-word pops ("BOIS!", "TURBULANCE", "chicken dinner kara do", "ALT+F4"); Roman Urdu with English words, swears censored with `*` / `$`.
  - **Recording 2 (10:39 to end):** small white ALL CAPS Roman Urdu at the very bottom, a few words at a time; one special caption "OHHH SHIT" at about 11:05 with an RGB-split glitch outline.
  - Frequency of captions per minute was NOT counted (no OCR available); they are on most spoken lines in both stretches.
- **Why this matters:** Roman Urdu captions served an Urdu-speaking audience. English funny moments are in English.
- **Spec default (ESTIMATE): ship NO captions** (EDITOR.md: none on long-form; YouTube CC). Optional **pop-word** for the top 3-6 payoff words per video (white fill, thick coloured outline, centre-low, 0.5-1 s, a small pop in, hard out). Not measured as a count. Ask him (open question 1).

---

## 11. Target length, moment count, build recipe

### 11.1 Targets (ESTIMATE, scaled from one video)
- **Don't Scream:** 6:25 from 41:36 of source = 15.8 % kept, 27 moments (4.4 per kept minute), 8.9 s median.
- **English hour (60 min raw):** the same 15.8 % would give 9.5 min and about 41 moments. His English long-forms do best at **6-7 minutes** (EDITOR § 3, results-log: 6-7 min beats 8+). So **target 6:30-7:30, about 28-33 moments** (4.4/min x 7). Never pad: if the hour has fewer than about 25 real payoffs, ship a shorter video (5:00) rather than weaker moments. Backrooms (13:11) and RE8 (15:00) are the long outliers; do not copy their length.

### 11.2 Recipe, one hour in
1. Run `projects/gta6-launch/tools/hour_desk.py <H01 drop folder> --hour 1 --mezzanine` (candidates, `CANDIDATES.md`, the 4K HEVC mezzanine for Premiere, clap-synced camera offsets).
2. Take the top candidates by score until about 30; reject any where the payoff is only his voice with nothing in the game or on his face. Use each candidate's **S11 payoff time**.
3. Window each: setup **4-6 s** before the payoff, payoff clip 1-2 s, end on the payoff zoom (0-2 s tail), total **6-10 s** (cap 19 s for a build-up, 56 s absolute). Drop the spoken "clip that".
4. Sequence them **in play order (chronological, no backward cut)**; inside a moment jump-cut forward over dead gaps (> 1 s).
5. Layers: V1 game, V2 face PiP (30 %, top-right flush), nest per moment.
6. Punches: his voice/face payoff gets a **4a corner punch (Scale 125-170, median 146, 1.2 s)** or the **4c PiP ladder (30/40/50)**; a candidate whose S11 payoff is a GAME event gets a **4b centred punch (195-210, 1.5-2 s)**; the biggest game moment once at 250-350 for up to 3 s. **Density about 6 per minute in the steady state, 13 per minute in the opening 45 s.** One stretch gag, on a mocking word.
7. Opening: § 8.3. Ending: § 8.4.
8. SFX: whoosh on frame 0 and at 1-2 recording/section changes (-7 dB under the clip), colour bars 0.10 s at 1-2 section turns plus optionally the last frame. Nothing else by default.
9. Audio: voice A1 and game A2, static chain per `rough-cut`; one clip trimmed 4-5 dB where the game scare clips; swears cut out of the voice, not bleeped.
10. No music, no captions (default), no overlays, no slow-mo, no grade, hard cuts only. He exports himself (`memory/feedback-affan-exports-himself.md`).

---

## 12. Urdu style vs `HUMOR.md` / `CREATOR-HAND.md` / `EDITOR.md`

| topic | Urdu videos (MEASURED unless marked) | English hand | wins for funny moments |
|---|---|---|---|
| cut zoom = razor + static Scale | yes, 41 in 152 clips, never a ramp | yes, razor + static (CREATOR-HAND § 1) | **AGREE** |
| zoom size | face punch median **146** (121-173); game punch median 194, extremes 207-348 | median 121-136; 120-150 normal, 160-215 big, 280-360 extreme | **Urdu** (146 / 194) |
| zoom hold | 1.20 s (face), 1.87 s (game) | 1.3-1.6 s | **AGREE** (1.2 s) |
| stretch gag | 1 in 6:25: Width 448, Height 143, 0.55 s | Width 248-928, 0.4-1.5 s, 1-3 per video | **AGREE** |
| zoom ladders | none on the picture; a PiP ladder 30-40-50 | 110-120-130-140 on a build | Urdu (no picture ladder) |
| keyframed push-in / nest presets (110/105 GTA LF Zoom Preset) | **none** (one opening snap clip only) | on almost every face run | **Urdu: none** |
| slow motion | **none** (0 clips) | 0.8x on the joke landing, 0-11 per video | **Urdu: none** |
| cuts per minute | 23.5 (first minute 36) | 24-33 | **AGREE** |
| face on screen | PiP in the corner all the time (30 %) | full-frame face about 73 %, PiP only on screen-share | **Urdu** (PiP, GTA game is the picture) |
| overlays | none | inset 85 % over colour matte, pops -18 dB | **Urdu: none** |
| SFX | 3 per video: whoosh (-7 dB), colour bars | pop on every overlay; Vine boom, bass, cricket | **Urdu: sparse**; both agree on colour bars |
| TV colour bars | 0.083-0.10 s | 0.20 s on V1 with tone | **AGREE on the device; use 0.10 s** |
| music | **none** (timeline) | Epidemic bed -20 to -27 dB, out under zooms | **Urdu: none** |
| captions | Backrooms yes (Roman Urdu); Don't Scream none in project | none on long-form; Anton on Shorts | open question 1 (default none) |
| swears | cut from audio; `*` in captions | razored out, not bleeped | **AGREE** |
| open | voice from 0.000, snap-zoom + whoosh on frame 0 | voice from 0.000 | **AGREE** (add the snap) |
| end | cold, on a 135 face punch (Don't Scream) | cold on the face, or fade to black | **AGREE** |
| transitions | hard cuts only | hard cuts | **AGREE** |
| master loudness | export -15.4 LUFS, TP -0.8 | -17 LUFS static chain | **English chain** |
| length | 6:25 / 13:11 / 15:00 | 5-7 min | 6:30-7:30 |

## 13. What the English channel already does differently
- Face is the main picture (73 % full-frame) with nested push-in presets (110/105 GTA LF Zoom Preset) and a 0.8x slow-down on the joke; the funny-moments video keeps the GAME as the picture, the face as a corner PiP and no slow-mo.
- Inset-over-matte overlays, a pop SFX on every overlay (about -18 dB), meme layer (Vine boom, bass hit, cricket), Epidemic music bed with dropouts under zooms: none of these appear in the two measured Urdu timelines.
- Long-forms carry the "N DAYS" subscribe-countdown CTA (EDITOR § 6, his ask): neither Urdu timeline has a CTA graphic. Keep the English CTA rule only if he wants it on this format (not decided here).
- Shorts captions are Anton and swears are `*`; long-form captions none.
- He exports himself, in his own ABW10/11 Premiere project: prepare the sequence, never `exportAsMediaDirect`.

## 13b. Reconciled with `LAUNCH-MODE.md` (the same recordings)
- **Lane:** LAUNCH-MODE STATUS makes funny campaign moments the **RAW lane, no OK step**, one of up to three Premiere sequences per hour, "cut in his old Urdu funny-gaming style". This file is that style.
- **PiP conflict, both recorded:** LAUNCH-MODE § 6 points long-forms at CREATOR-HAND § 3 (his English screen + PiP: Scale 46 with a rectangular crop mask, feather 10, about 372 x 388 px, top-right at Position 0.864:0.164 or top-left). The Urdu PiP is an uncropped 16:9 rectangle at 30 % (576 x 324), hard edge, top-right. **Urdu wins for this format** (§ 1); the English crop-mask PiP stays for screen-share segments.
- **Story spoilers:** LAUNCH-MODE § 5 bans story cutscenes and plot reveals in Shorts (open world, systems, reactions and the loading screen are in). "Campaign moments" can hit story missions. **Default (ESTIMATE): apply the same ban to this video** (no story cutscene footage, no plot reveals; gameplay and reaction moments only) and flag any candidate that contains a cutscene. It is not stated for long-form: open it if a good moment needs one.
- **Censoring:** Shorts use `projects/gta6-launch/tools/censor.py` and `qa_wordlists.json` (a mute list; LAUNCH-MODE warns ambiguous words like "weed" and "drugs" mute ordinary talk, tune after hour 1). For this Premiere sequence the Urdu way is the measured one: the word is cut out of the voice track (§ 3.4), nothing bleeped.
- **Intake:** `hour_desk.py` handles copy, probe, clap sync, voice-only WhisperX, scan proxy, `--mezzanine`; the PS5 VP9 WebM does not open in Premiere ("unverified" per LAUNCH-MODE), so use the mezzanine. Camera files in recording order; a gap in camera coverage means no PiP there.
- **No Urdu-style text/captions/CTA layer exists in the launch tools for long-form;** the Shorts caption layer (Bebas Neue, kai.json) is a different format.

## 14. Open questions for Affan (3)
1. **Captions / pop-words on the English funny-moments video?** Default in this spec is none (EDITOR.md long-form, and Don't Scream's project has no text). The Backrooms export has Roman Urdu word-pop captions. Yes (which look), or none?
2. **Is a 30 % top-right face PiP right once you see the GTA 6 HUD?** Check hour one: if cash, wanted stars or the clock sit top-right, which corner moves the PiP to?
3. **Sound for funny moments: the measured Urdu way (3 SFX per video, a whoosh at -7 dB and colour bars, no music) or your 19 Nov GTA 6 rule (full Epidemic SFX plus a music bed)? And any meme audio (Vine boom etc.)?** The spec defaults to the Urdu way. Meme clip audio is a copyrighted-clip risk, and three SFX files in these videos are YouTube rips (§ 7.2): replace them with Epidemic ones?
