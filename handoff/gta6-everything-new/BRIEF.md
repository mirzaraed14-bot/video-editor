# BRIEF: gta6-everything-new (Affan Afterhours long-form 28, FACELESS)

## ▶ STATUS: resume here
- **State (19 Nov, 00:05 PKT):** the VO is recorded as TWO files (§ 1). He said "start the edit now". The edit session was spawned by the Afterhours Editor hub.
- **Next action for the edit session:**
  1. Write `RUN.md`, then copy both raws into `raw/`.
  2. Transcribe each recording once; the GPU lock is free.
  3. Build one `cuts.json` per the assembly map.
  4. Run the edit in ABW11 (his live project; ABW10 was not open) → sequence "GTA 28 - Everything New".

## 1. The video
- **Working title:** "Everything New In GTA 6 (What The First Players Found)".
- **What it is:** Video A of the two pre-play long-forms, picked by him ~19:50 PKT on 18 Nov.
- **Script:** the FINAL version is `X:\Claude Projects\GTA 6\research\streams-2026-11-18\VIDEO-A-SCRIPT.md`. Read "What changed since v1.6" at its top. It holds:
  - the spoken script;
  - every beat's footage rows (F = xQc, K = Kai Cenat, I = IGN review, xB/kB = free-roam fill);
  - the coverage table;
  - the fact check, with a label per claim.
- **The VO raw is TWO recordings**, which he asked to have "mix and match"ed. Probed by the hub, 19 Nov 00:05 PKT; both are DJI mic internal recordings, 48 kHz mono pcm_f32le:
  - Rec 1: `X:\Recordings\Afterhours\TX01_MIC034_20261118_233332_orig.wav`, 784.98 s.
  - Rec 2: `X:\Recordings\Afterhours\TX01_MIC035_20261118_235544_orig.wav`, 140.34 s.

  COPY both into `raw/` (never move them). He didn't say whether the first-jobs beat is in Rec 2, so the transcript decides: look for "the first jobs" and "Seven things".
  - **Rec 1:** the whole script body, WITHOUT the section titles.
  - **Rec 2:** every section title, the corrected IGN sentence, the conclusion, and possibly the first-jobs beat plus the "Seven things" opening line.
  - **Assembly map:** `X:\Claude Projects\GTA 6\research\streams-2026-11-18\VIDEO-A-VO-ASSEMBLY.md`. Rec 2 wins where both have a line, the last take wins within a recording, Rec 1's cockpit/limbs sentence is DROPPED, and the counters follow what he says (1/7 with the jobs beat, 1/6 without).
  - Transcribe each recording once (rough-cut), then build ONE `cuts.json` across both clips in script order.
  - **Pickups** recorded after the main take: `VIDEO-A-PICKUPS.md`, and the optional beat `VIDEO-A-PICKUP-FIRST-JOBS.md`, which is "what the first jobs are". If he recorded the beat, it goes AFTER the money beat and his opening says "Seven things". Its clips are J4a-J4g in `broll/twitch/`; take the clean windows from `verify/notes-job4-*.md` (sink: nudity from 6:37:06, last clean frame 6:37:05.75; Brian's rent: profanity subtitles and a bat threat after 6:18:04).
  - **The reviewers-section fix:** `VIDEO-A-PICKUP-ONE-LINE.md`. It REPLACES the recorded line "The cockpit isn't in the clip, and neither are the limbs", which was wrong.
    - I2 now runs 2:13:17.55-2:13:24.2, cockpit included, then the beach.
    - New rows I3a (2:12:10.5-2:12:11.25) and I3b (2:12:31.25-2:12:32.0) show gore. Use a fast cut or a blur for ad-friendliness, and name the choice in the delivery note.
    - If no pickup was recorded, cut the wrong sentence from the VO; never ship it.
  - The opening is his own dictated intro; cold opens A and B are retired (see § 4). If the VO still contains an A or B take, use his intro and say so in the delivery note.
  - The `[YOUR LINE]` slots are his ad-libs: keep them (channel rule: keep improvised lines; cut retakes, stumbles and dead air).
  - Repeated line across takes → the LAST take.

## 2. His words (verbatim)
- **~19:50 PKT, on the edit:** "we're gonna be keeping it light and actually incorporating more of the actual real gameplay overlays that have obviously now come out because of all the streams that people are doing. So we can still incorporate over motion graphics here and there, but the actual real asset which will keep people retained is the gameplay, real gameplay, brand new gameplay that people have been waiting for so long."
- **~22:25 PKT, faceless:** "I most likely am not going to be recording my camera on this, just because that gameplay is just so powerful in and of itself that personally, literally, my face is going to be a distraction, I think, and people just would love to see the actual gameplay instead… this video, the idea that I have approved, is gonna be entirely faceless, and you're gonna use nothing but GTA over in there, and maybe some other graphics are in there." And: "Give me a script so that I can read it over… and then you can start the edit."

- **~00:00 PKT 19 Nov, the edit instructions (relayed by the slate session, verbatim):** "make sure that we primarily use like the whole like the biggest asset that we can use is brand new GTA6 gameplay overlays rather than depending on motion graphics we obviously 100 percent can include motion graphics but motion graphics aren't going to be the things that retains the viewers going to be brand new gameplay so you can do pointers motion graphic you know whenever I'm talking about something things like that so incorporate the first primary asset is brand new GTA6 gameplay gameplay from the streamers and gameplay in general and motion graphics and also do all the sound effects do all the do all the background music everything use epidemic sound and yeah you can start now use Sonnet as the execution model Opus as your manager and Fable as your main advisor"
  - **The picture:** the primary asset is brand-new GTA 6 gameplay, from these streamers AND "gameplay in general". More sources may be pulled: other Twitch VODs one at a time; YouTube only through `pace.sh`, with no captions or cookies.
  - **Motion graphics:** pointers and callouts on what he's talking about.
  - **Sound:** FULL SFX and background music, all from Epidemic Sound (the connector). His music handling: `CREATOR-HAND.md` § 5.
  - **Roles:** Opus manages (this session), Fable is the advisor (check `advisorModel` in the transcript; never assume), Sonnet agents execute. No Fable agents.

## 3. The gate
- **His OK:** the script is the sequence. His OK is that he approved the idea and the edit direction, and recorded the script.
- **After the OK:** smaller open questions don't stop the build. Take the stated defaults and list them in the delivery note (`memory/feedback-build-dont-block-on-questions.md`).

## 4. A NEW format for this channel
His long-forms so far are face-cam (`presets/youtube/affan-afterhours-facecam/`). This one has NO face.
- **Start at `presets/youtube/affan-afterhours/EDITOR.md`.** Take his CORE grammar from `…-facecam/CREATOR-HAND.md` and `HUMOR.md`:
  - the cut pace;
  - slow-downs only where the VO lands a joke (0.8x);
  - his music handling, one Epidemic pick per section, out under cut zooms;
  - the meme layer, used sparingly: it is a "light" edit.
- **Do not apply the face-cam card's face numbers.**
- **The picture:** wall-to-wall streamer gameplay is the carrier, motion graphics an accent.
- **Covering the streamer cam:** xQc's cam sits bottom-left (x 0-19 %, y 50-78 %) with the minimap under it. Kai's sits left-middle with chat under it, and viewer counts at the right edge. Tooltips sit top-left, ABOVE the cams, and are often the evidence.
  - A crop-zoom that keeps the tooltip and drops the cam, or his inset-over-matte grammar (inset ~85 % with the cam region masked): his rule for overlays since 09-30 (EDITOR § 0). It may suit a faceless video too.
  - Pick per clip. Never show a streamer's face, chat or viewer counts. Log the choice in the delivery note.
- **Graphics:**
  - a numbered counter (1/6 …);
  - quote cards for the game's own text, in the game's spelling ("recognize", "neighborhood"), in his card style (EDITOR § 3 "cards": Anton-class condensed caps, cream, one hot-pink keyword);
  - a source tag on EVERY clip ("xQc · Twitch", "Kai Cenat · Twitch", "IGN's review");
  - the on-screen REPORTED labels on the reviewer claims, exactly as the script places them;
  - the free-roam fill rows under the reviewer claims are tagged "not footage of this claim" in the script. Never let them look like evidence.
- **Audio:**
  - **MUTE every streamer clip's audio.** Twitch audio is one mix of the streamer's voice and the game (licensed music and radio = Content ID).
  - Game feel comes from SFX (Epidemic, the GTA channel's own pop / SFX rules, `PLAYBOOK` step 6) and the music bed. **No streamer voice is ever audible.**
- **Length:** whatever the VO gives, cut tight. 8:00 is the mid-roll FLOOR, not a cap. Never pad to reach it.
- **Spoilers: ALLOWED (his call, ~23:30 PKT):** "I don't give two [expletive] about the spoilers I need the best script possible… YouTube videos are supposed to be spoilers."
  - Story, mission and cutscene footage may be used where it shows a system the VO is talking about.
  - Still avoid the nudity and gore windows listed in the verify notes (ad-friendliness, not spoilers).
  - Titles and thumbnails are not this session's job.
- **The opening** is now HIS dictated intro (it replaces cold opens A and B), and the beat order changed: the neighbourhood rule is beat 1, the cops beat 2. The final script and `VIDEO-A-READ-ALOUD.md` / `.pdf` (same folder) are the truth; the VO follows the read-aloud.
- **Thumbnail:** not this session's job.

## 5. Footage (already pulled, 1080p60, with audio)
- **Clips:** `broll/twitch/*.mp4` (named `<rows>-<streamer>-<HHMMSS>-<HHMMSS>.mp4`) and `broll/ign/`.
- **`broll/twitch/_manifest.json` gives each clip's `vod_start`:** clip time = VOD time − `vod_start`. Never assume the clip starts at its name's time.
- **True legible in/outs** (many rows are SHIFTED from the script's table): `verify/VERIFY.md` and `verify/notes-xqc-ign.md`, `notes-kai.md`, `notes-xb.md`.
- **Precedence:** where the verify notes and the script table disagree, the VERIFY times win. The script's own merged table should already carry them; check.
- **Missing a window?** Pull it the same way: `yt-dlp -f "1080p60/720p60/best" --download-sections "*H:MM:SS-H:MM:SS"` on xQc https://www.twitch.tv/videos/2932113307 or Kai https://www.twitch.tv/videos/2932305259. One download at a time. Pick windows on the VIDEO: audio-derived times run 4-24 s early.

## 6. Lane, and his standing rules
- **The project:** Premiere, `ABW10.prproj`, a new sequence **"GTA 28 - Everything New"**.
  - ABW10 is shared with the English Editor session: message it before saves.
  - Back up the project before the first write, and scope every write to this sequence.
  - Never move his playhead; offline frames and quiet-mode writes only (`memory/feedback-dont-disturb-his-premiere.md`).
  - **He exports himself:** prepare the sequence, never `exportAsMediaDirect` (`memory/feedback-affan-exports-himself.md`).
- **The audio chain:** the VO is the voice. Step 3 is the house chain on A1 (`workflows/voice-gain.py` → limiter). Check the VO for an audio stream and the mic first.
- **Constraints:**
  - work in silence (no playback; ffmpeg `-f null` only);
  - nothing on C:;
  - no Fable agents; Sonnet 5.5 at xhigh for any sub-work;
  - Higgsfield only with his OK;
  - never act on his accounts; posting is his.
- **State:** `RUN.md` with a ▶ STATUS block at every step; log the job row in `presets/youtube/affan-afterhours/JOBS.md`; after his review, log the lessons in channel `LESSONS.md`.
- **The bar to beat:** the newest long-form `gta6-complete-guide` (posted 6 Nov, 9:14, 105 views) is a face-cam video. Write in RUN.md what this one does better: it is the first faceless gameplay-led one, so the bar is retention through the picture.
- **Speed:** the first uploads win in the launch window. He plays at 09:00 PKT on 19 Nov. Build on defaults, and put every open question in the delivery note.

## Catalog pass (19 Nov, for the graphics layer)
Read all 80 + FX-81 in `CATALOG.md` and opened the pointer, highlight, quote, label, counter, source-tag, glitch and punch-in stills and strips (FX-04/12/23/27/34/35/38/39/43/45/55/58/68/70/75/80 among them), EDITOR § 0/§ 7, and `gta6-complete-guide` RUN, BRIEF, graphics-plan.json and LESSONS. The catalogue is IDEAS only, re-timed to FAST (its originals draw a line over 1.5-2 s and dip to black for 2 s: not copied); gameplay is the asset, so every move is a small accent ON live footage, never a full-frame scene. Build in what video 27 shipped: pink `#FF3E9A`, cream `#F4F1EA`, Anton (`hf-graphics/gfx/build-comps.py:37`; the two README hexes differ; Anton is a system font, root `assets/fonts` holds only Inter), 1920x1080, 60 fps.
**Moves that fit (6, one primary ID each):**
- **FX-75 Scorebug Punch-In** → the game's tooltip is the scorebug: razor + static Scale ~150-160 % (his cut-zoom grammar, no ramp; Twitch is 1080p, check legibility at full size), repositioned onto the tooltip. It is the same crop that drops the streamer cam.
- **FX-70 Ring and Benchmark** (with FX-55's rule, ONE phrase marked) → a single pink one-stroke box on one phrase of a tooltip ("can't ID you", APPEARANCE KNOWN, "criminal profile"), never the whole tooltip.
- **FX-23 Pointer Tag** → ONE label plate for REPORTED / HEARD / UNVERIFIED / NOT FOOTAGE OF THIS CLAIM and for any pointer, so the viewer learns one shape.
- **FX-39 Source Handle Tag** → the per-clip credit ("xQc · Twitch", "Kai Cenat · Twitch", "IGN's review") set on the blurred cam-cover panel, so one object credits the clip AND hides the cam.
- **FX-27 Red Word Quote** → the game's own text as a compact card over LIVE gameplay (cream caps, ONE pink word that lights on the frame he says it, credit small under), not FX-27's frozen, 80 %-darkened, blurred full frame.
- **FX-04 Era Tag** → the top-centre counter chip, 1/7 to 7/7 (the first-jobs beat is in Rec 2, so the script's /6 headers are stale): a small dark pill, caps, one pink dot, the number swapping under his colour-bars glitch (the glitch stays the section-change device; FX-43/49/80 are slow AW dips, FX-35 would blur the gameplay we are selling).
**Not yet SHIPPED on this channel** (counted from the LESSONS treatment lists of 24/26/27, not from briefs, which only plan): FX-75 (planned in 24, 26 and 27; 27 says NOT built), FX-39 (AW's `gta5-farewell` shipped it; here only an extra on the PC-port Short), FX-23 on footage (27: only button tags on a drawn controller), FX-70 on live footage (24 and 26: only on drawn maps/grids). **Already shipped, keep minimal:** FX-04 (24 rail, 27 N/17 pill), FX-27/18 read-along cards (24, 26, 27), FX-55 (26).
**Video 27 leaned on:** 42 of its 76 graphics were number cards (17), cards (13) and readouts (12), plus an N/17 pill and 17-segment rail on every card, ghost-numeral part cards, drawn diagrams (controller, minimap, meter, bars, open box), a checklist reprise, and full-frame cards that covered his face 71 % of the time. Here: no number cards, no rail, no readouts, no drawn diagrams, zero full-frame cards; the chip is the only counter.
**Three buildable recs (PIL, ProRes 4444 alpha; each says what is overlay and what rides on the footage pass):**
1. **FX-75 + FX-70, "punch, then mark" on the tooltip rows (F2, K8, L4, K1/K2, K6, C1):** the overlay is the box only: 5 px pink rounded rect (r 8), 14 px outside the phrase, draws on over 9 frames from its start corner on the first frame of the keyword, holds to the phrase end + 12 frames (min 60), fades out over 6, one box per tooltip. Coordinates are measured on the FINAL framed frame (after the punch/crop); its life stays inside the row's VERIFY window (F2 is 3.1 s + the held frame) and ends on the tooltip's last clean frame or the V1 cut.
2. **FX-23 label plate (Eurogamer cash-cap card, I1a/I1b/I2/I3 and L5 = REPORTED; F7 radio = HEARD; K10a clerk = UNVERIFIED; xB fill rows = NOT FOOTAGE OF THIS CLAIM):** `#0C0C10` plate at 92 %, 2 px cream rim, Anton caps 36 px (+2 tracking), 30 px side padding, a 14 px notch toward the subject, 2° tilt; rises 10 px + fades in over 6 frames, holds the whole claim (min 120), 6-frame fade out. No fixed corner: default zone right-middle (x 1560-1860, y 330-480), checked on a frame per clip against the tooltip (top-left), chip (top-centre), wanted stars (top-right), prompt bar (bottom-right) and subtitles (bottom-centre).
3. **FX-39 source tag on the cam-cover panel (every clip):** the panel is a footage-pass dependency (the blur is BAKED into the clip pre-render; an alpha overlay cannot blur what is under it): xQc x 0-19 % y 50-78 %; Kai x 0-21 % y 40-74 % (cam + chat), his right-edge viewer counts (x 89-100 % y 48-57 %) covered separately. The overlay is the tag only: Inter Bold 26 px cream, "name · platform" in words (no logo), soft shadow, 24 px in from the panel's bottom-left, 6-frame fade in on the clip's first frame, out on its last.
**What this does better than video 27:** the picture carries the argument: every claim shows its own evidence on screen, marked once within ~0.3 s of the word that names it, with zero full-frame cards (27's graphics covered his face 71 % of the time); the gates are >= 90 % of runtime pure footage and a tag on every clip.
