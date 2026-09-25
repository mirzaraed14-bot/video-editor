# RUN — gta6-pc-release

## ▶ STATUS: resume here (updated 2026-09-22, evening)

**The creator has redone V1 themselves** — their own cut zooms, nesting and rescaling. V1 = 126 clips, sequence
now **315.148 s** (was 316.65). **NEVER touch V1, and never reuse a cue time from before this point**: their trims
moved every block and cut the overlay count from 27 to 26. The cue map in `brief/blocks.json` and
`brief/v1-labels.json` was re-read from their current project at 16:55 and is the only valid one.
Backup of their work: `premiere-backup/ABW6-creators-work-1655.prproj`.

**DONE: the 7 motion graphics.** `make-motion-graphics.py` renders all seven from one config; placed by
`place-overlays.py --only 6,16,17,20,21,22,24`. All original type-and-gradient design, no logos or game art.
Look: Montserrat over a DIAGONAL magenta-to-teal wash — a drifting sine was tried first and swept the whole frame
onto one hue, rendering as a flat magenta field; a diagonal ramp keeps both poles in every frame.
V3 now holds 15 clips (7 graphics + the 8 the creator kept), all at 85 %.

**DONE: the Google images (all 4).** `assets/images/` — GTA 4 (official trailer frame) and GTA 5 (official
gameplay frame) for cue 10's two halves, Strauss Zelnick for cue 15, Mike York (his own channel) for cue 19.
Sourced from real footage rather than scraped thumbnails, so provenance is known and the frames are clean.
**The Zelnick frame's CNBC banner read "Q4 results", a DIFFERENT occasion from the Sept 17 shareholder meeting
the script cites — cropped off so the shot does not assert the wrong event.** The two game stills came back at
1280x720 and no higher source exists (the GTA 4 trailer is 2007 and tops out at 720p), so both went through
Higgsfield upscaling per the Blue rule and are now 3840x2160. The portraits were already full-res.

**DONE: SFX on the motion graphics (Epidemic Sound).** `assets/sfx/` + `place-sfx.py` — 15 events on **A3**:
a short swish as each graphic's first line starts to rise (0.10 s in, matching HOLD_START in the renderer) and a
soft UI click as the accent rule draws. mg3 carries the two CEO quotes so its second phase gets its own swish.
Entrances only; exits stay silent, per the channel rule.

**STILL TO DO:**
1. **Google images** for cues 10 (GTA 4 / the PC-date statement / GTA 5), 15 (shareholder meeting) and
   19 (a photo of Mike York) — real people, products and a document, so SOURCED not generated, then enhanced in
   Higgsfield if soft.
2. **The colour matte on V2**, which is still empty. Every overlay sits at 85 %, so the creator's face currently
   shows around them; they want "a really subtle animated one, nothing crazy".

Also unsourced: cue 1 (opening meme) and cue 8 (the movie-scene two-hander).



## 🔴 V1 IS DAMAGED — RESTORE IT BEFORE ANY OTHER WORK

The creator asked for the face nests and zooms removed so they could do the face motion themselves.
`unnest-faces.py --apply` removed all 25 nests and re-laid the 97 default clips, **but re-laying was wrong**:

- **8 of those clips carried an 80 % speed change — the creator's own slow motions** ("I've incorporated the slow
  motions already so you don't have to do any"). `overwriteClip` re-lays at 100 %, so those 8 came back at full
  speed and 12.93 s short.
- **V1 now has 30 gaps of a frame or more** (largest 600 ms), plus 22 one-frame rounding gaps from placement.
- One clip at 18.235 s was additionally mutated by a `setSpeed(0.8, ...)` probe that landed it at 20.370 s
  instead of the correct 20.921 s.

**THE FIX — restore the pre-nest project, which has the creator's exact state (labels, speeds, no nests):**
1. Premiere must be CLOSED (`premiere-up.sh` is macOS-only, so this is by hand on Windows, or `app.quit()` through
   the bridge with the creator's OK).
2. Copy `premiere-backup/ABW6-before-face-nests-1412.prproj` over the live project at
   `E:\Premiere Pro Exports\Adobe Premiere Pro Auto-Save\...\ABW6.prproj`.
3. Reopen, then replay the overlay work, which is all scripted and idempotent:
   `importall` (the scratch driver) -> `place-overlays.py --apply` -> mute A3.

**Caveat to state to the creator:** that backup is from 14:12. Anything changed ANYWHERE else in the project after
14:12 would be rolled back. `premiere-backup/ABW6-before-unnest-1541.prproj` holds the 15:41 state if it is needed.

**Lesson for `face-nests.py`: it has no undo, and un-nesting by re-laying from an EDL silently destroys per-clip
speed changes.** Never re-lay a timeline the creator has hand-edited; restore the file instead.


**Next action:** finish the overlay assets, then place all 27. **Face motion is DONE** (25 nests, 21 cut zooms,
ramps verified). Six overlay sources downloaded. Blocked only on two YouTube pulls that need a signed-in session
and on one creative call (see Flags).

**Done 2026-09-22 while the creator was away**
- **Step 5b face motion, complete.** `transcript/plan-face-zooms.py` -> `transcript/face-zooms.json`, applied with
  `lanes/premiere/face-nests.py --sequence "Sequence 24" --scratch-audio 3`. All **25 Iris runs nested**, **21 cut
  zooms** (100 -> 125 hold keys, 4.0 per minute of runtime), gradual ramp **100 -> 110 on the 7 nests >= 10 s** and
  **100 -> 105 on the other 18**, which is the creator's own rule from the walkthrough at 1:40. Read back: V1 = 80
  clips (25 nests + 55 overlay clips), A1 = 149 clips, **zero gaps**, both ending 316.6497 s.
  **A1 was ALREADY 149 before the pass** (confirmed against `premiere-backup/ABW6-before-face-nests-1412.prproj`) --
  the creator had split V1 without audio in three places. Nothing was lost.
- **Project backed up** to `premiere-backup/` before the first timeline change.
- **Seven overlay sources downloaded** into `broll/` (all 1080p H.264): RDR2 Official Gameplay, GTA V Official
  Gameplay, GTA Online hackers, both GTA 6 trailers, an IShowSpeed piece to camera, and Rockstar North responding
  to a GTA 6 question. **Two memes** into `assets/memes/`: a five-stages-of-grief meme (cue 3) and the burning-house
  meme (cue 13, the creator asked for "a house blowing up").
- **Three Higgsfield plates** in `assets/higgsfield/`, all ORIGINAL artwork with no text, logos or game art baked in
  (the type goes on top as our own graphic, per the Hot Coffee lesson): `plate-announcement` (cues 2 and 10),
  `plate-blurred-date` (cue 7), `plate-230million-2k` (cue 26). The first two are upscaling to 2k at 2 credits each.
  **`resolution: "2k"` on generate_image FAILS on this connector** — omit it, the server picks; failures cost nothing.
- **Cue 15 unblocked.** The creator supplied the real file (`GTA 6 (Grand Theft Auto 6) - Official Extended
  Gameplay.mp4`, 26:48, 1080p, matching the official runtime) -> `broll/GTA 6 Official Extended Gameplay.mp4`.
- **Text is baked into the Higgsfield plates at the creator's instruction** (2026-09-22): they overrode the
  keep-text-out recommendation. It WORKED -- "COMING TO PC 2028", "RUMOURED PC 2028" and "230 MILLION SOLD" all
  rendered sharp and correctly spelled. **Short strings are why**; the Hot Coffee failure was a long one. Artwork
  stays original throughout: no logos, no game key art, no characters, plain generic type.
- **All 21 assets imported** into the `GTA 6 PC Release` bin.
- **Cue 4 built to the creator's spec** (2026-09-22): six thin vertical panels across one 1920x1080 frame, each an
  ORIGINAL scene evoking that game's era and setting (no characters, no logos, no key art, no text), composited
  with ffmpeg at exactly 320 px each, left to right in release order ->
  `assets/higgsfield/collage-rockstar-history.png`.
- **Cue 4 LABELLED** after the creator's note that the panels "just look like random images". Each panel now
  carries the game's NAME and RELEASE YEAR set in Bebas Neue over a bottom gradient scrim, with a hairline rule
  and a panel divider -> `collage-rockstar-history-labelled.png`, built by `label-collage.py` (re-runnable).
  Titles are set as plain type rather than recreating each game's logo: the logos are distinctive brand designs,
  and plain type is also sharper and exactly placeable, which generated lettering is not. Swapped in at cue 4.
- **14 overlays PLACED on V3** at **85 % scale** by `place-overlays.py` (idempotent, one clip per bridge call).
  V3 now holds 15 clips. V1 (80) and A1 (149) untouched and still ending 316.6497.
- **A3 MUTED.** Placing the video overlays brought their own audio onto A3 (9 clips: the memes, the Rockstar and
  IShowSpeed clips, the gameplay). Muted rather than deleted so the creator can unmute and trim a meme's sound if
  they want it.

### ⚠ Step 5 is NOT finished -- two of the creator's explicit rules are still unmet
1. **The colour matte is NOT placed. V2 is empty.** The overlays sit at 85 % with the FACE showing around them,
   not the "cool animated looking colour matte" the walkthrough asks for at 8:34. V2 is free and reserved for it.
2. **No drop shadow yet.** `place-overlays.py` sets Motion > Scale only; the walkthrough wants a drop shadow on
   every overlay.
3. **13 cues still have no asset:** 7 motion graphics (6, 17, 18, 21, 22, 23, 25), the opening meme (1), the movie
   scene two-hander (9), and 3 image cues that need REAL sourcing, not generation -- GTA 4 / the PC-date statement
   / GTA 5 (11), the shareholder meeting (16), and a photo of Mike York (20). A placeholder was deliberately NOT
   put on cue 20: a console image where a person belongs would read as done and be wrong.
- **The creator's first `GTA 6 EXTENDED LOOK IS HERE!.mp4` (45 min) is NOT the official Extended Look**
  (which runs 26:49). It is a livestream reaction with a streamer's webcam, Twitch chat and an FPS counter burned
  into the picture. Unusable as clean source for cue 15.

**Old next action:** build the overlays. The creator labelled V1 and recorded a **12-minute walkthrough** explaining
every block; it is resolved into **[`BRIEF.md`](BRIEF.md)** — **27 overlay blocks, all placed exactly**, plus the
global rules. Nothing is waiting on an answer any more. One gap remains: the GTA 6 Extended Look is still not
downloaded (YouTube age-gates it) and cue 15 needs it.

**The creator has hand-edited V1 since the replay: 152 clips, and the timeline is now 5:16.65, not the 5:51
that was laid down — they cut ~34 s. NEVER re-replay the EDL, and never quote a position off the old cut.**

All 27 overlay blocks are placed exactly: the labels were read out of the `.prproj` (`asl.clip.label.name` on the VideoClip), joined to the words under each clip by source time. Reader kept at `brief/readlabels.py`.

| | | |
|---|---|---|
| format | long-form YouTube, **the FACE-CAM style** | `presets/youtube/affan-afterhours-facecam/` (measured 2026-09-21) + channel `presets/youtube/affan-afterhours/` |
| lane | Premiere 2025 (25.0.0 build 61) | the creator's LIVE project `ABW6.prproj`, bin **`GTA 6 PC Release`**, sequence **`Sequence 24`** (1920x1080, timebase 4237833600 = 59.94). Sequence 23 is a DIFFERENT short — never touched |
| subject | **GTA 6 on PC: why 2028 is wrong, and the call is November 2027** | written script saved at `script.md`; the creator warned they restructured sentences while reading, so the transcript is the truth for WORDING and `script.md` for STRUCTURE |
| camera | `E:\Skool Recordings\5 Sept Batch\C1295.MP4` · 1920x1080 · 59.94 · 977.98 s | 7.1 GB, never copied — the synced master carries its video bit-for-bit |
| voice | OBS capture `…\Batch Batch\2026-09-22 07-39-59.mp4` · 60.000 fps · 958.32 s · **−16.9 LUFS** | copied to `raw/originals/`; its picture is the teleprompter script |
| lane gaps | step 4 grade: Premiere 25.0 cannot run the scripted grade — this style needs none · step 8 is the creator's | from LANES.md + lab-notes |
| constraints | none | |
| started | 2026-09-22 | |

## Steps

| # | Step | Status | What it produced / why not |
|---|------|--------|----------------------------|
| 1 | Intake | **done** | `raw/gta6-pc-release-synced.mov` = the camera's video **stream-copied bit-for-bit** + the OBS voice delayed 578,160 samples (**+12.045 s**), PCM 48k, 977.98 s. **The camera's own audio is DEAD** (flat −93 dB, constant −80.8 dB peak, zero speech modulation), so `sync-dual-audio.py` cannot work here and returned an impossible +323.9 s. Synced instead with the new **`workflows/sync-by-motion.py`** (picture motion against the voice envelope): +12.045 s, no drift, 20 windows. Verified three ways — lips closed at −133 ms and opening at 0; strongest post-mux windows +0.010 / −0.037 / −0.016 s; and the **clap slate at the head of the take** (hands meet on the frame the clap sounds, 16.718 s and 18.189 s). Record: `audio/sync/sync.json` |
| 2 | Rough cut | **done** | WhisperX large-v3 once → `transcript/words.json` (1359 words, speech 13.28 → 965.37 s). `take-map.py` found 23 take groups / 31 superseded takes. **141 segments · 351.1 s (5.85 min) from 16.3 min of raw** — 8.7 min of it was silence. EDL `transcript/cuts.json`, canonical `outputs/gta6-pc-release.transcript.json` (1097 words). Boundary polish run; **11 boundaries hand-corrected against the measured envelope + slice re-ASR** because the OBS mic is noise-gated (see Flags). Fresh-eyes pass run on both dimensions. Replayed onto Sequence 24: **141/141 clips on V1 and A1, zero gaps, every in/out within one frame** |
| 3 | Audio polish | **not run — the creator's** | Channel rule: they run Enhance Speech v2 themselves on a voice bounce. Nothing to push anyway — the kept speech measures **−16.6 LUFS integrated, LRA 9.5**, so `voice-gain.py` calls for **+0 dB**. True peak is 0.0 dBFS, so a **−6 dBFS limiter is still wanted** before export. **A re-replay discards clip effects**, so this runs after the labelling pass, not before |
| 4 | Color grade | **skipped** | none in this style — the LED room is the look (facecam PLAYBOOK § per-step) |
| 5 | Overlays | **in progress** | Labels done by the creator and read exactly out of the `.prproj`; their 12-min Tella walkthrough ingested into **[`BRIEF.md`](BRIEF.md)** — **27 overlay blocks** (8 Rose, 7 Mango, 5 Violet, 4 Blue, 3 Tan) over 25 default Iris blocks, plus the global rules (no overlay fills the frame, colour matte visible behind, drop shadow on every one, 1080p floor, **slow motions already done, add none**). Default Iris blocks: cut zooms inside the nest + a slow zoom on the nest, 100→110 when the nest is long, 100→105 when short. Guide: `brief/raw/editing-guide.mp4`, narration split from playback by differencing the program monitor (557 s directing / 122 s playback) |
| 6 | SFX | — | |
| 7 | Review | — | |
| 8 | Export | — | the creator's |

## Measured against the style's definition of done

| | rough cut now | `presets/youtube/affan-afterhours-facecam/` target |
|---|---|---|
| cuts per minute | **24.1** (141 clips / 5.85 min) | 20-25 visible changes/min *including* overlays and zooms — already there on the cut alone |
| pace | **187 words/min** | 200+ |
| first minute | 18 cuts, **0.71x** the body's 25.4/min | cold open 1.5-2.5x the body |
| deliberate pauses over 1 s | 0 (three between 0.67 and 0.95 s, pinned) | 2-3 per video |

The cold open is the one number under target, and it closes at step 5, not here: the style reaches it with the
first minute's overlays at twice the body density plus a game montage inside the first 10 s. Nothing to re-cut.

## Request coverage
- **"sync the OBS screen recording audio with the actual camera footage"** → step 1. Evidence: `audio/sync/sync.json`, the clap-slate frames, the post-mux re-measure.
- **"the camera audio is very quiet, you'll have to increase the volume"** → answered and closed: the camera track is not quiet, it is **dead**, and the OBS voice needs **no gain at all** (−16.6 LUFS measured on the kept speech). Nothing was pushed.
- **"just the rough cut so I can label where the game footage and Higgsfield images go"** → step 2 ends at the replay. **No overlays, no graphics, no zooms, nothing above V1.**
- **"here's the script, some sentences I might have restructured"** → saved verbatim to `script.md` and used for section structure; every wording difference resolved from the transcript, not the script.
- **the separate bin "GTA 6 PC Release"** → used. The synced master was imported into it alongside the creator's own `C1295.MP4` and OBS file; nothing else in the project was touched.

## Flags to report
- **The script's biggest argument was never said on camera.** The intro promises "one thing about GTA 6 that completely kills the biggest excuse of making PC players wait" — the script's *THE EXCUSE THAT JUST DIED* section (GTA 6 ships without Online; Zelnick's "no recurrent consumer spending" quote). It is **absent from the raw take entirely**; the take goes "Hackers, right?" → "That's not the main reason." → straight into Mike York. **No edit can deliver it — it needs a pickup line**, or the promise comes out of the intro. Confirmed independently by the fresh-eyes flow review.
- **"Even the CEO is saying that it's not true"** (the CEO section's button) has a loose antecedent, because the connecting line — the script's *"you don't call PC more and more important and then make it wait two years. That's not how that works."* — was fluffed on camera ("It's not how that... you see, understand what I'm saying? Huh?") and is unusable. Kept as the section's only payoff; a pickup line would fix it properly.
- Three smaller scripted lines were never recorded: the *case against me* point two (GTA 5 really did take 19 months), the four-point recap just before the November 2027 reveal, and the closing callback *"Rockstar's betting on 'twice.'"*
- **The camera is not recording audio at all** (C1295 and C1296 flat at −93 dB; C1297 −77 dB). Not quiet — dead. Worth fixing at the shoot. The clap slate on this take made the sync exact, so keep doing it.
- **The OBS mic is noise-gated**, so quiet frames are digital zero and the local floor reads −140 dB. Every "floor + 12 dB" hot-cut check therefore fires on almost every joint (69 of 139 on the first pass, all but five of them silence). Boundaries on this footage must be judged in **absolute dB against the segment's own speech level**. Eleven real defects were found and fixed that way.
- **The fresh-eyes mechanical pass raised three more clipped heads; all three are false positives.** It read segments 11, 18 and 104 ("First," / "the biggest excuse…" / "Fit your uncle…") as opening after their first word, from quiet pre-onset ramps at −67 to −84 dB and from whisper word-starts measured on wide windows. Settled by extracting **exactly the kept span** and transcribing that: each one already contains its first word in full. **That is the decisive test on this footage** — a pre-onset ramp 65 dB under the vowel is the gate opening, not a fricative, and a word-start read off a wide ASR window carries padding. No EDL change.
- **Three pauses are deliberately retained** and will show up in any dead-air gate: "Oh, shit… 2028." (0.84 s), "GTA 5 came out on PS3… right?" (0.67 s), and "November 2027 is… when the PC version of GTA 6 will be released." (0.95 s). All three are pinned (`no_refine`).
- Two stutters were left in because the audio gives no clean boundary to cut on: "about seven, about seven months" and "that takes… that takes labour".
- Profanity kept as spoken, for the creator to bleep or keep: "roast the shit out of me" (~2:53 on the cut) and "Oh, shit. 2028." (~1:41).
- Sequence 24 was **60.00 fps** against 59.94 footage (the same trap as Sequence 20); set to 59.94 while it was still empty, timebase read back `4237833600`.

## Skipped, and why
- Step 3 audio polish: the creator's Enhance Speech pass, and a re-replay would discard clip effects anyway.
- Step 4 grade: not part of this style.
- Background music: not asked for.
