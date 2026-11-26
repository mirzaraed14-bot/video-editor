# REACTION-STYLE.md — face-cam REACTION / chill-talk videos, edited in the KSI+ style (@KSIplus)

## ▶ STATUS: v1 written 2026-11-23 from three KSI+ videos read frame by frame. Read this block first.

| | |
|---|---|
| State | **v1, buildable.** The WHAT below is measured. The Premiere HOW (§ 11) is mostly existing tools; three moves are NEW and get a scratch-sequence test before the first real job (§ 11, marked 🧪). |
| Scope | Affan Afterhours **face-cam reaction / talk videos** where he watches clips and reacts (first job: `gta6-npc-organic`, "reacting to GTA 6 NPC encounters"). Not scripted VO, not his play videos (`FUNNY-MOMENTS-STYLE.md`), not Onyx reactions. |
| His words (23 Nov) | *"another editing style which is going to be our secondary editing style for these reaction videos, or these funny chill reaction videos where I'm just talking ... I want the style to be exactly in this channel style ... executed when I give you the recording inside of Premiere Pro."* (FEEDBACK.md 2026-11-23) |
| Which style wins | For this format, **KSI+ wins over `CREATOR-HAND.md` / `HUMOR.md`** wherever they differ (memory `feedback-gta-own-style-only.md`, exception of 11-23). The few places KSI+ breaks a standing rule are in § 12 as his decisions; until he answers, build the § 12 DEFAULT. |
| Gaps | (1) ~~era check~~ done: the 3 Aug video matches (§ 0), the style is stable. (2) **Sound was read from loudness traces only, never heard** (silent rule): "no bed" and "SFX on the opener only" are INFERRED from the floor and the peaks. (3) The ending comes from ONE full upload (v2). (4) Four Premiere moves are untested (🧪 in § 11), and the Onyx kit's prep/placement runs here for the first time: **the first GTA reaction is the pilot.** |
| Evidence | `X:/Claude Projects/GTA 6/research/ksiplus-style-2026-11-23/`: `findings-<id>.md` per video (every number with its timestamp/frame), `frames/` (sheets, native bursts, `hub/` = the hub's own checks), `meas/` (scene, loudness, saturation), `ref/<id>/zoom.json` (background-tracked zoom steps). Tools: `strip.py`, `meas.sh`, `sat_track.py`, `inset_box.py`. |
| Thumbnails | **`REACTION-THUMBNAILS.md` (this folder, v1 24 Nov): the KSI+ thumbnail grammar and its builder. The thumbnail session builds only after watching this edit's cut (§ 10b there): at the raw-cut checkpoint, send it the camera↔screen offsets, the clip map and `cuts.json`.** |

**Label key:** MEASURED = read off frames / frame counts / meas files (timestamp given in the findings). INFERRED = reasoned. Px are at **1920×1080**; frame counts at **60 fps** unless said (his camera runs 59.94).

## ★ DEFAULT BUILD, job 1 (one value per move; the ranges below are the evidence, this is the build)
**Template video: `MgNMUQz5H5Q` (Street Interviews, 1080p60, layout L1).** Change a value only on his note.

| move | build exactly this |
|---|---|
| layout | **L1** for the whole video (gameplay is 16:9; reels go on the blurred fill) |
| cam box | outer **346×391** at **x20–366** (top-LEFT: his note 24 Nov, § 14; KSI+ itself is top-right x1554–1900), y21–412; **7 px white border, square corners, no shadow**; head-and-shoulders crop of the same camera; his trim + wordmark on the bottom border (§ 12 #3) |
| blurred fill | cover-scaled copy of the clip, blurred to no detail, −10 % luma, soft vignette lower right |
| cam → clip | **whip**: 5 f horizontal smear on the cam, swap, 8 f unsmear on the clip (≈0.22 s) |
| clip → cam | **hard cut** on his laugh / the punchline |
| jump zoom | **×1.30** held 1–3 s (most), **×1.9** for a punchline hit (≤ 1/min); ~3 per minute of runtime; out by a 1-frame step or a hard cut to wide |
| eased push-in | ×1.0 → **×1.5 over 22 f**, ease-out, then hold; motion blur mid-move; ~1 per cam segment ≥ 4 s |
| laugh creep | ×1.4 → **×2.0 over 150 f** on his biggest laughs, ends on a hard cut |
| B&W | **OFF** except ≤ 2 moments on the biggest laughs (a 5-f fade to grey, or a white flash into B&W). The newest video's habit (every jump zoom goes B&W, 1.5/min) is HIS call (§ 12 #8) |
| laugh pulse | ON: box ×1.40 about its top-LEFT corner (box on the left), 24 f ease-out / hold 2 s / 24 f back, ≤ 0.7 per minute, on hard laughs only |
| opener | cold open mid-sentence → fire plate behind him at ~1.0 s → title (the video's title in 2–3 words) builds with a 14-f left-to-right sliver wipe per word, Inter Black caps, black fill + thick coloured stroke (hot pink `#FF2E9A` / white / yellow), **him in front of the type**, a hit per word → whole composite pushes ×2.2 over ~150 f → hard cut to wide by ~8.5 s → first clip by ~11 s |
| graphics | no captions; 0–1 boxed caption; 0 stickers unless a beat clearly calls for one (max 2) |
| audio | his voice on the house chain; clip audio ~6 dB under him; **no music bed; SFX on the opener only** (§ 12 #1–2) |
| end | hard cut to his face; it ends on him; no outro card |

---

## 0. The videos read

| id | title | date | views | layout | what it gave |
|---|---|---|---|---|---|
| `MgNMUQz5H5Q` | Street Interviews That Went WAY Too Far.. | 13 Nov 2026 | 619K | **L1** | 1080p60 reference: inset geometry, whip, laugh pulse, title build, push-in ladder |
| `9TDEteLZ0uI` | When Live Performances Go Horribly Wrong | 20 Nov 2026 | 286K | **L1** | the WHOLE upload incl. the ending; zoom + B&W habit; stickers; mixed-aspect framing |
| `k0MqxOUbez4` | KSI Reacts To The Most Viewed Tiktoks In The World! | 29 Oct 2026 | 1.04M | **L2** | the split layout, the count pill, the zoom rate on a list video |
| `nTFTwdYYT2M` | Brutal Public Embarrassing Moments | 3 Aug 2026 | 617K | **L1** | ERA CHECK (first 6 min, hub's read): **no change across the Aug→Oct gap** — same explosion-behind-him opener, same stacked title with him in front, same box + laugh pulse, a B&W close-up; adds one rare gag (him cut out INTO a clip's scene, § 6) |

The channel is a two-layout system with ONE grammar. A video picks its layout from its clips: **L1** for mixed-aspect clips (street interviews, concerts, gameplay), **L2** for an all-vertical TikTok list.

## 1. The grammar on one card

| | KSI+ (MEASURED across the three) |
|---|---|
| open | cold open on his full-frame cam mid-sentence → a VFX plate behind him (~1 s) → a 2–3-line title builds word by word with HIM IN FRONT of the type → the whole composite pushes in ×2 → hard cut to a wide shot → he talks → first clip at 11–27 s (§ 5) |
| body | clip PLAYS (he reacts live in the cam box / cam half) → hard cut to his full-frame cam on the laugh/punchline → he talks 3–5 s → back into the next clip (§ 2–3, § 8) |
| clips | never paused, never zoomed into, never replayed, never slowed; source captions, watermarks and @handles left as they are |
| face cam | one fixed camera; every change of framing is an editor crop: instant jump zooms, eased push-ins with motion blur, slow creeps on big laughs, a few B&W moments (§ 4) |
| graphics | almost none: no speech captions, no lower thirds; a count pill on a ranked list (L2); 0–2 cut-out stickers per video; one boxed caption at most (§ 6) |
| audio | NO music bed; SFX only on the opener (and a sticker or flash); clip audio ~6 dB under his voice (§ 7) |
| end | no outro, no end card: ends on his face; one "DO NOT SUBSCRIBE"-type joke sticker in the last 3 s (§ 9) |

## 2. The two layouts (MEASURED)

### L1 — clip centred on a blurred fill, cam in a box top-right (Street Interviews, Live Performances)
- **Clip:** fit to full height 1080, centred on x960, never cropped. 9:16 → 608 px wide (x656–1264); ~4:3 → ~1440–1500 px wide, pillarboxed; 16:9 → fills the frame (the box sits on top of it).
- **Fill behind a narrow clip:** a cover-scaled duplicate of the SAME clip, blurred to no detail (5–30× smoother than the clip), luma 0–15 % under the clip (v1 darker, v2 not), a faint vignette toward the lower right. It carries the clip's colour.
- **Cam box:** right edge x≈1900 (≈20 px margin), top y≈21; outer **346–392 px wide** (18–20 % of the width; v1 346×391, v2 392×443), aspect w/h ≈ 0.885; **6–7 px white border, SQUARE corners, no shadow**; inside = a tight head-and-shoulders crop of the same camera (≈0.58 of the cam frame, head centred). Brand trim: a blue/white diagonal band along the bottom border + blue edge stripes, and the channel wordmark (~110 px wide) centred ON the bottom border. Present on every clip frame, from the first frame of the clip. Never moves except the laugh pulse.
- **Laugh pulse (v1 only, ~0.7/min):** the box grows ×1.40 (345→482 px wide) ANCHORED TOP-RIGHT, ease-out: 80 % of it in 6 frames, settled in 24 (widths every 3 f: 353, 433, 454, 466, 474, 478, 480, 482); holds ~2.1 s; shrinks back in ~24 f. On his hard laughs / lean-ins.
- **Share of runtime:** clip + box 65–73 %, full-frame cam 26–31 %, extras (pulse, split, raw clip) ≤ 3 %.
- Rare extras: a 1.7 s split (clip left, 12 px white divider, cam right); a 4.7 s raw source clip shown with no box (his own old video).

### L2 — vertical clip left, cyan divider, cam right (Most Viewed TikToks)
- **Clip panel:** full height, flush left, full-bleed and uncropped: a 9:16 clip = x0–604 (width follows the clip's aspect). No blur fill.
- **Divider:** a vertical line 12–13 px wide, full height, **cyan #2BD7FD**, one soft anti-aliased edge, no shadow.
- **Cam half:** everything right of the divider (≈x617–1920) = the camera at its full-frame scale, shifted so his head sits centred in the half (~+285 px). Jump zooms happen inside the half too.
- **Share:** L2 90.5 %, full-frame cam 9.5 % (the intro + gaps, median 2.6 s).
- **No L1 box in an L2 video**, and no whips (L2 switches are all hard cuts).

**For GTA:** NPC-encounter clips are mostly 16:9 gameplay with some vertical reels → **L1** (it takes every aspect). L2 only for an all-vertical ranked list.

## 3. Switching (MEASURED)

| switch | L1 | L2 |
|---|---|---|
| clip → full cam | **hard cut, 0 frames**, on the punchline / his laugh (loudness jumps +10…+15 dB at the cut: his laugh) | hard cut, 0 frames, at the clip's end |
| full cam → clip | **horizontal WHIP BLUR ≈0.2 s**: the cam smears sideways over ~5 f (60 fps), hard swap to the clip (itself smeared), unsmears over ~8 f; no slide, no scale; the box is there from the first clip frame | hard cut, 0 frames |
| clip → clip | hard cut; the box (and the fill) stay; the fill swaps with its clip | hard cut |

- The whip starts at the END of his line: his audio falls silent 0.1–0.4 s before it, and the clip's sound arrives ~0.1 s into the whip. No separate whoosh is visible in the loudness trace (INFERRED: none).
- Rates: cam↔clip switches 2.6–4.4 per minute each way.

## 4. The face cam (MEASURED)
Base framing: WIDE, upper body + room, lots of headroom (his own set: the same). One camera, all variety is crop:

| move | numbers | how often |
|---|---|---|
| **jump zoom** (instant, 1 frame) | two rungs: ×1.15–1.5 (medians ×1.14 / ×1.23 / ×1.30 per video) for most, and a BIG one ≈×1.9 from wide straight to a tight close-up (v1 23.23→23.25 s, f1394→f1395, hub-checked; v3 71.4 s ×1.5); held 1–4 s; out by another 1-frame step or a hard cut to wide | **2–6 per minute** |
| **eased push-in** | ×1.0–1.06 → ~×1.5 over **13–24 frames**, ease-OUT, then hold; v3 shows **motion blur peaking mid-move** | 1–2 per cam segment |
| **creep on a big laugh** | ×1.4 → ×2.0 (up to ×2.7 on a scream) over 2–3 s (50–180 f), sometimes with shake; ends on a hard cut | ~1 per 3 cam segments |
| **B&W moment** | v2 HABIT: jump zoom ×1.23–1.30 + saturation down to ~25 %, held 1–2.5 s, both back in 1 frame (~1.5/min). v1/v3: rare (1–3 per 14 min): a 5-f fade to grey, a white flash into B&W, a greyscale shrink on black | v2 1.5/min, else rare |

Not used on the face: colour flashes, tints, vignette, freeze, slow-mo, shake outside a creep.

## 5. The opening (MEASURED, frame-counted on v1 and v3; v2 a variant)
1. **0–1 s:** cold open on his full-frame cam, mid-sentence (v2 already punched in ~×1.34). No sting, no logo. v1/v3 add a whole-frame blur jolt or whiten flash of ~6 frames around 0.9–1.5 s.
2. **~1.0 s: a VFX plate BEHIND him**: fire/explosion rising from the bottom edge, filling the background in ~0.7 s, fading out over ~0.5 s (v1 f61–f188; v3 1.0–4.5 s with smoke). v2 swaps the background for a stage-light plate, then an explosion plate. An explosion sound rides it (+6…+13 dB).
3. **~2.7–6 s: the title builds**, 2–3 lines of very heavy caps, one word at a time: a left-to-right sliver wipe of 12–24 f per word (v1, v3) or a rise from below of ~4 f per word (v2). Colours: black fill with a thick green / yellow / red outer stroke per word (v1); yellow #F4CD1B with a black outline (v2); white with a teal + red glitch offset (v3). A white gloss sweep across one word (v1). **He is masked IN FRONT of the type** (letters pass behind his head and shoulders, clean hair/headphone edges). Each word lands with a hit (+14…+18 dB).
4. **The whole composite (him + plate + type) pushes in ×2–2.2**, fast for ~12 f then easing (v1 154 f, v3 ~55 f).
5. **Hard cut to a WIDE shot** at 5.4–9.2 s (title gone, or still on screen small and wiping out).
6. He talks to camera, then the first clip at **10.9 s (v1), 13.7 s (v3), 26.8 s (v2)**.

The title is the video's own title in a few words (WILDEST / STREET / INTERVIEWS; LIVE / FAILED / PERFORMANCE; MOST / VIEWED / TIKTOKS).

## 6. Graphics (MEASURED)
- **No speech captions. No lower thirds, chapter cards, arrows or emoji.** Source captions, watermarks and handles are left in the clips.
- **Count pill (L2 list videos):** top-left of the clip panel, ≈310×99 at (27, 21); black fill, round ends, pink inner stroke + cyan outer glow, the TikTok logo, a thin divider, the view count in white condensed bold. Hard on (no animation), 0.7 s before the clip, and the number RISES clip by clip up to #1 (121.5M → 653.2M). A ranked-list device only.
- **Cut-out stickers (v2, 2 per video):** a transparent PNG (a famous face cut out; a chrome "DO NOT SUBSCRIBE" with two red siren lights) rising from the bottom edge in ~4 f, held to the next cut or the end.
- **Him cut out INTO a clip's scene (Aug video, rare gag):** a keyed cutout of him composited inside the clip (sitting in a subway car, 4:30–4:35), full frame, 1–2 per video at most. Not in the default build; a candidate for a GTA beat (him "in" the game scene) on his OK.
- **One boxed caption at most** (v1 "LAUGHS IN 33 YEARS OLD"): white heavy geometric caps on a near-black rounded box, low-left, opening as a thin horizontal sliver over ~8 f, held ~3.5 s.
- **Censoring:** only a mosaic over a source handle (v2, once). No bleeps found (can't be judged silently).

## 7. Audio (MEASURED numbers, INFERRED reading)
- Integrated **−17.0 / −18.8 / −19.2 LUFS**, LRA 13–19 LU, true peak up to +1.1 dBFS (theirs; ours stays under −1).
- **No music bed** in any of the three: the floor drops to −50…−85 dB in his pauses.
- **SFX only on the opener** (the explosion, each title word, the push) plus a sticker or a white flash. No whooshes on the whips, no meme sounds, no risers under clips.
- **Clip audio sits ~6 dB under his voice** (v2 momentary medians: cam −22.9, clips −28.9 LUFS). When he talks over a running clip, the clip keeps playing under him.

## 8. Pacing (MEASURED)
- Clip runs: median 12 s (v1, v2), longest 48–56 s uncut when the clip is good; L2 blocks median 27 s.
- Full-cam talk between clips: median 3–5 s (v1 5.0, v2 3.05, v3 2.6), longest 15–26 s of free talk (a story).
- Cam↔clip switches 2.6–4.4/min each way + 2–6 jump zooms/min. The longest stretch with no layout change: 56 s (v1), 158 s (v3, jump zooms keep going inside it).
- Length: 14–22 min per upload (the 14-min sections read here).

## 9. The ending (v2, the only full upload read)
No outro, no end card, no music, no fade: a hard cut to his full-frame cam and it ends on him mid-gesture. A joke sticker ("DO NOT SUBSCRIBE", chrome, two red siren lights) rises from the bottom 3.2 s before the last frame. End-screen elements are added in YouTube Studio (INFERRED).

## 10. Copy vs adapt for Affan
- **Copy exactly:** layouts L1/L2 and their numbers, the switching, the zoom ladder, the opener's structure and timings, no captions, no bed, the clip level, the ending shape.
- **Adapt (it's KSI's brand, not ours):** the box trim and wordmark → his own (§ 12 #3); the title colours and font → the same weight and build, with Inter Black (`assets/fonts/`) and the channel's hot pink `#FF2E9A` as one stroke colour; the "DO NOT SUBSCRIBE" joke → his own line or nothing (never KSI's sticker art).
- **GTA sources:** clips from YouTube/IG keep their creators' captions/handles (KSI does), and streamer face cams stay visible with the name on them (memory `feedback-streamer-facecams-labelled.md`).

## 11. Premiere HOW (lane: `premiere-pro` skill + `lanes/premiere/lab-notes.md`)
**Recording + prep = the Onyx reaction kit's step 1, as a PILOT** (`presets/youtube-shorts/onyx-samples/kit/reactions/KIT.md`): OBS capture of the screen where the clip plays (with desktop audio) + the camera with the DJI mic → `prep.sh` (copy, `sync-dual-audio.py`, ONE large-v3 transcript, `xplay2.py` = where each SOURCE clip file plays on his timeline). The SOURCE clip files (not the OBS screen grab) go on the timeline, offset by the play map, so clips stay full quality. Clip downloads follow the YouTube rules (`pace.sh youtube`, short sections, H.264).
🧪 **The kit is unproven for this job:** its own "Pilot part 2" lists `prep.sh`, `xplay2` over a whole OBS file and `premo3.sh` live as untested; it is built for a 9:16 Short and takes ONE prospect Short, not ~15 clips from mixed sources. The first GTA reaction IS the pilot: run `sync-dual-audio.py` and the play map by hand first, check every clip's offset on the audio (a 1-frame-exact match), and log what broke in `lanes/premiere/lab-notes.md`.

**Track map (L1):** V1 camera (full-frame cam state) · V2 blurred fill per clip · V3 the clip · V4 the camera AGAIN as the box picture · V5 the box frame (alpha) · V6 opener / stickers / caption (alpha) · V7 adjustment layers (whips, B&W). A1 his voice (house chain) · A2 clip audio · A3 SFX.

| move | how | status |
|---|---|---|
| cut (clip runs, talk segments) | EDL replay of V1 + clip placement from the play map; clip runs and talk segments come from the cut (rough-cut rules: kill dead air, keep the last take) | ✅ V1 replay (`premiere-bridge.mjs replay`) · 🧪 placing ~15 source clips from the play map (the kit's by-name placement, never run on a 16:9 long-form) |
| voice chain | `lanes/premiere/audio-polish.py --apply` (measured gain → −6 dBFS limiter) | ✅ scripted |
| clip fit-to-height, centred | Motion Scale = 1080 / clip height × 100, Position centre | ✅ property writes (Onyx `applyo.py` pattern) |
| blurred fill | pre-rendered per clip with ffmpeg (cover scale + heavy blur + 0–15 % darken + soft vignette) and placed on V2: no live Gaussian Blur in Premiere | ✅ ffmpeg + placement (render the fill, never blur in-app) |
| cam box (V4 + V5) | V4 = the same camera clip at the same source time, Motion crop to the head crop + scale/position into the box; V5 = one alpha PNG/mov of the white 7 px border + his trim + wordmark (built with PIL, `place-graphics.py`) | ✅ pieces exist; the head-crop numbers come from one P2b-style measure (`p2b4_measure.py` pattern) |
| laugh pulse | Motion Scale ×1.40 about the box's outer TOP-LEFT corner (x20 y21) on V4 and V5 together: V5 anchor = position = the corner, V4 position keyed `TL + f·(P0 − TL)`; ease-out 24 f / hold ~2 s / 24 f back: baked keys | ✅ verified on GTA 41 (keys read back; top-right then, same math) |
| whip cam → clip | an adjustment layer on V7 spanning 5 f before + 8 f after the cut with Directional Blur (90°) keyed 0 → max → 0; fallback: render the 13 frames with ffmpeg from both shots and lay them on top | 🧪 new: test the adjustment-layer route on a scratch sequence first |
| jump zoom | razor + static scale, his own GTA cut-zoom grammar (`face-nests.py` CUT ZOOM = hold keys) | ✅ scripted |
| eased push-in ×1.5 / creep ×2 | the bridge `zoom` command (`ease: "quart"`, frames 13–24; creep: frames 120–180) on Transform Scale; motion blur = Transform's own shutter (un-tick "Use Composition's Shutter Angle", shutter 180°) | ✅ zoom scripted · 🧪 the shutter write is new: verify by a frame grab |
| B&W moment | Lumetri Saturation 0–25 on a razored piece (or a V7 adjustment layer) with the jump zoom | ✅ Lumetri add exists (`grade-layer`); the Saturation write is a new param: write + read back once |
| opener (plate + title + him in front + ×2 push) | ONE HyperFrames comp rendered as an opaque clip over V1 for 0–~9 s: his first seconds of camera + a background-removed copy of him (`npx hyperframes remove-background`, pinned 0.8.16) + the plate + the type build + the push; placed by `place-graphics.py` | 🧪 new: the cutout quality on headphones/hair is the risk; check full-res frames. Plate source = his call (§ 12 #6) |
| count pill (lists only) | alpha mov per number (HyperFrames), hard on | ✅ standard graphics build |
| sticker rise | alpha PNG/mov, 4-frame rise, `place-graphics.py` | ✅ |
| clip level | A2 clip audio ~6 dB under the voice (measure the voice first, memory `feedback-voice-first-mix.md`) | ✅ |
| frames for QC | offline grabs (`offgrab.py`) or the bridge `frame` command; never move his playhead or activate his sequence | ✅ |

He exports himself (memory `feedback-affan-exports-himself.md`): the run ends at "placed + verified".

## 12. Where KSI+ meets a standing rule: his decisions (build the DEFAULT until he answers)
1. **Music:** KSI+ has NO bed; the GTA 6 rule (11-21) is "full SFX + Epidemic music". DEFAULT: **no bed** (exact KSI+).
2. **SFX:** KSI+ only sounds the opener (+ a sticker); "SFX on every graphic" is the Onyx rule, and GTA graphics get premium SFX. DEFAULT: **opener + stickers only**, nothing on whips, zooms or the box.
3. **The box trim + wordmark:** KSI's blue trim + "KSI+" logo. DEFAULT: white 7 px border + a hot-pink `#FF2E9A` trim + "AFTERHOURS" in Inter Black italic on the bottom border (no logo file exists yet in `assets/logos/`).
4. **Instant same-camera zooms:** KSI+ does 2–6/min; his 10-07 rule says "no same-camera punch-ins" (it came from the Onyx podcast samples), while his own GTA edits already use razor + static zooms (median ~130 %). DEFAULT: **follow KSI+**; his call.
5. **Length:** KSI+ runs 14–22 min; the channel's data says 6–7 min beats 8+ for scripted videos. DEFAULT: **whatever his reactions earn, cut tight** (clip runs ≤ ~15 s unless the clip is strong, talk segments 3–5 s).
6. **The opener's VFX plate** (fire/explosion behind him): a stock plate or Higgsfield (credits only with his OK). DEFAULT: ask once at build time; never spend credits unasked.
7. **The joke end sticker:** his own line or none. DEFAULT: none.
8. **B&W on every jump zoom** (the newest KSI+ video's habit, 1.5/min) or rare B&W (the other two). DEFAULT: **rare** (≤ 2 per video).
9. **Censoring:** KSI+ censors nothing; his AW rule bleeps drug / self-harm / suicide words in audio and text ("ask once on the next", memory `feedback-censor-sensitive-words.md`), and the talk list has the Kurt Cobain clerk item. DEFAULT: **bleep those words** (mute + soft tone), ask him once.

**Standing rules that simply apply here (no conflict with KSI+):** no promo frames at any clip edge, checked frame by frame (`feedback-no-promo-frames.md`); no silence over 2 s inside a third-party clip, cut to ~1.2–1.5 s (`feedback-clip-pauses-max-2s.md`); same-scale jump cuts keep his head still (his camera is fixed, so only the deliberate zooms above change its size: `feedback-head-steady-across-cuts.md`); streamer face cams stay visible with the name on them; work in silence; never move his playhead or activate his sequence.

## 13. Recording ask (for him)
Record like the Onyx reactions: **OBS on the screen where the clip plays (desktop audio on) + the camera with the DJI mic**, started together; the clip links in `X:/Claude Projects/GTA 6/research/npc-organic-2026-11-23/TALK-LIST.md` order. Let a clip play while you react over it; to talk longer, pause it and look at the camera (that becomes a full-cam segment). Restart a line if you fumble: the last take is kept. **In OBS, record the mic too.** GTA 41's profile "Ig live" was in Simple output mode (`RecTracks=1`: track 1 only), with Desktop Audio on track 1 and Mic/Aux on track 2 only, so the meter moved but the file held desktop audio alone. Fix: Settings → Output → Output Mode **Advanced** → Recording → tick **Audio Tracks 1 and 2** (the mic lands on its own track). The quick alternative, ticking Track 1 on Mic/Aux in Advanced Audio Properties, mixes the mic into the desktop sound. Also **clap once on camera with the OBS window up at the start of each camera file** (sync; GTA 41 lesson, § 14).
**PRE-RECORD GATE (after GTA 41, which had to be re-recorded):** before the full take, record a 10-second test in OBS and on the camera while
talking, then CHECK THE FILES, not the meters: (1) `ffprobe` the OBS file shows his mic on its own audio track (track 2 when Advanced output
records tracks 1 + 2) and that track is not silent while he talks; (2) the voice is HIS MIC (the HyperX) in that OBS track: the camera's built-in
mic is only the sync backup (GTA 41's only voice was that built-in mic: speech p95 −48.7 dBFS, roomy, unusable as the main voice), never a
reason to stop him; (3) the clap shows on both.
Only then start the real take. The edit session runs this check on the test files if he sends them. **The thumbnail face is a frame of this camera (his call 24 Nov):** keep the mic off your mouth, and laugh toward the camera at least once (`REACTION-THUMBNAILS.md` § 10).

## 14. Lessons
- **2026-11-25, GTA 41 take 2 REJECTED → v2 (read before any reaction build):** `X:/Claude Projects/GTA 6/research/ksiplus-style-2026-11-25/FOUNDATION.md` (Fable study of 7 KSI+ uploads) overturns 10 claims of this file (its § 17): clips ARE frozen and punched into, text gets a yellow highlighter, sub-booms on whips, face zooms are 1-frame steps on fixed levels, the box crop is HC 1000. Layout is chosen BY REFERENT, never by the reel's play state. The applied spec: `projects/gta6-npc-organic/take2/v2/BUILD-PLAN.md`; lessons: `LESSONS.md` 2026-11-25. This file gets the v2 rewrite after his verdict on the pilot.

Log every review note of the first job here as *note → change → file*, and in `LESSONS.md`.
- **GTA 41, 24 Nov: "my facecam should be on the left".** → The cam box moves to the TOP-LEFT (outer x20–366, y21–412, border, trim
  and AFTERHOURS unchanged); the laugh pulse anchors on its top-left corner. A 9:16 reel sits at x656–1264, so the box never covers the
  reel, its captions or a streamer's own face cam (checked on GTA 41's frames). Files: ★ DEFAULT BUILD (cam box, laugh pulse), § 11,
  `projects/gta6-npc-organic/work/box/make_box.py` (`BOX_SIDE`, default left).
- **GTA 41, 24 Nov: "where is audio, I gave you the OBS recording, it has my mic audio in it".** → It did not: that OBS file carries one
  desktop-only track (−91 dB while he talks; his HyperX showed on the OBS meter but was not routed to the recording). The voice is the
  camera's BUILT-IN mic (there was no DJI on this shoot), clean but very quiet and roomy; he re-records. Recording ask + pre-record gate (§ 13): route Mic/Aux to the recorded track (or a second track), and clap once on camera with the OBS
  window up at the start of every camera file (sync). Files: § 13 below, `lanes/premiere/lab-notes.md` 2026-11-24.
