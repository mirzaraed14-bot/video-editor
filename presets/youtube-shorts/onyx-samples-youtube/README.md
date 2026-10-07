# Onyx sample Shorts: THE YOUTUBE LOOK (B-roll storytelling)

> **AFFAN'S RULES, ALL VIDEOS (review 2, 2026-10-07; verbatim + per-video plan in
> `projects/_onyx-batch-2026-10/REVIEW-2026-10-07.md`). They override anything below that disagrees.**
> 1. Captions keep ONLY `!` `?` and quotation marks: no full stops, no commas, nothing else.
> 2. Caption base position is CONSTANT for the whole video, just under the lips where the face sits; it never moves on a cut
>    (frame the speaker shots consistently instead). The entrance animation is fine.
> 3. The caption entrance must look smooth: the Instagram look's rise tween renders at 60 fps (`ig_build.py` outputs 60/59.94). The
>    YouTube look keeps its measured stepped pop at the source rate (the reference design; MFM is "perfect").
> 4. No instant zoom-in (punch-in cut) on the same camera: one continuous keyframed push-in.
> 5. Transitions (whips) ONLY where the scene/camera/source changes, never between two shots of the same camera.
> 6. Every pop-up / motion graphic has an audible, crisp SFX (high-end minimal podcast vibe; Epidemic Sound).
> 7. Captions: white base + coloured emphasis words (not one colour for everything).
> 8. Never cut a word short at a joint. 9. The hook makes a STRANGER care: who this is and why the story matters to them.
> "Sean Ryan style/format" in Affan's words = `onyx-samples-youtube/` (this look's reference). MFM's sample is the benchmark: "perfect".

> **Platform decides the look (Affan, 2026-10-05).** Every sample is built for the prospect's PRIORITY platform:
> - **YouTube-first → this file**: maximal, full-bleed B-roll storytelling.
> - **Instagram-first → `presets/youtube-shorts/onyx-samples/`**: the minimal motion-graphics look (the MFM pilot).
> How to pick the platform: `presets/youtube-shorts/onyx-samples/PLAYBOOK.md` § 0.

The look of the sample Short Onyx makes for a podcast prospect whose priority is **YouTube Shorts**. Affan's brief,
2026-10-05: the pilot is *"a classic minimalistic Instagram style… if you're aiming for YouTube that's gonna be a
different style"*, with a reference to take apart *"each and every single frame"*.

**The reference:** Shawn Ryan Show, "Why Shawn Ryan Walked Away From His Dream Farm" (`KUMikP6a2eI`, 51 s, 1.03M views in
4 days). All 1,222 frames were logged, and the cuts, faces, blur and audio stems were measured:
`projects/_ref-yt-shorts-shawn-ryan-farm/analysis/` → **`STYLE-TEARDOWN.md`** (the synthesis), `FRAME-LOG.md` (every frame),
**`board/`** (1-layouts, 2-whip, 3-captions: look at these before building anything).

Procedure: [PLAYBOOK.md](PLAYBOOK.md). What jobs taught: [LESSONS.md](LESSONS.md).
Not Abundance Wisdom, and not the Instagram look: no cards, no window morphs, no Inter, no dark canvas.

Status: **v0, measured from the reference and not yet built.** The first YouTube-first job proves it. Log every change in LESSONS.md.

---

## 1. The idea in one line

**A told story, illustrated noun by noun.** The speaker is on screen only when HOW he says it matters (quotes, attitude,
reactions, the punchline). Everything he describes is SHOWN, full-screen, in real footage. One transition, one caption
system and one music bed hold it together, and the last line runs back into the first.

## 2. Delivery

| | |
|---|---|
| Canvas | 1080×1920, **rendered at the base's own frame rate** (`hyperframes render --fps 24000/1001` for a 23.976 source, `30` for 30). The Instagram pilot's 24 → 30 mapping cost a whole QA round. |
| Length | 35–55 s (the reference runs 51 s) |
| Finish | Fully automatic MP4, on the chat-only route (HyperFrames + ffmpeg + a numpy frame pass for the whips). |
| Loudness | **Master −12 LUFS integrated** (the reference: −12.1, LRA 5.7), true peak ≤ −1 dBTP (the reference hits +0.2; don't copy that). Voice ≈ −12.5 LUFS; music bed ≈ 13–14 LU under the voice. |
| Safe zone | Captions, hook title and watermark all sit between 55 % and 77 % of the height, clear of YouTube's bottom text and its right-hand buttons. Keep text inside x 60 → 960. |

## 3. Shots: three types, and the rules for choosing

| Shot | Picture | Use it for | Length |
|---|---|---|---|
| **A** (speaker) | Full-bleed 9:16 crop of whoever is talking. Face median 29 % of frame height (16–44 %). Two framings, medium and tight, swapped for variety (a sarcastic line gets the tight one). | Quotes, attitude, reactions, the punchline: anything where HOW it's said is the content. | 1.3–4.6 s |
| **B** (B-roll) | Full-bleed real footage of the thing being named. | Every noun, place, object and event. A pop-culture comparison gets the real reference (*"they communicate through electricity"* → *Stranger Things*). | 0.8–2.7 s in the set-up; a whole sentence (4–5 s) in the payoff |
| **SPLIT** | Speaker on top (56–57 % of the height), B-roll below, hard seam, no divider line. The bottom panel floats ±9–24 px (a ~1.25 s bob); the top keeps pushing in (up to +27 % over 2.3 s). The caption sits on the seam. | A line where both the face and the noun matter (a reaction to a thing, a guest's comparison). | 2–4 s |

**Rhythm rules (measured):**
- **Share of runtime: B-roll ≈ 50–55 %, SPLIT ≈ 10–15 %, speaker ≈ 35 %.** The face is on screen less than half the time.
- **Fast set-up, slow payoff.** Mean shot 2.7 s, but ~2 s per shot over the first ~45 % (12 shots in 23 s), then ~4 s per shot
  to the end (7 shots in 28 s). In the slow half, the captions keep the rhythm (a new chunk every ~0.66 s).
- **Open on the speaker for under a second, then B-roll** (the reference cuts to the farm at 0.67 s).
- **B-roll arrives early: 0.3–1.9 s before its noun is spoken.** The cut lands on a caption change, 1–5 frames before the phrase.
- **Literal beats clever.** "Old farmhouse" = an old farmhouse; "slave quarters" = a real sign that says Slave Quarters. Test: with the
  sound off, could a viewer name the noun from the picture alone?
- **A B-roll event can be a beat**: the kitchen light dies exactly on "And she's like". Trim B-roll so its own events land on words.
- **End on the speaker** (the punchline face), and cut on the last word (§ 9).

## 4. The one transition: a whip-slide with mirrored edges

Every shot change uses it (19 of 19 in the reference). There are no plain cuts, flashes, zooms or glitches.
Frame by frame on `board/2-whip.jpg`. Numbers are at 1080 px width, per frame at the base rate:

| Frame | What happens |
|---|---|
| out −2 | The outgoing shot moves ~1 % of the width (12 px) in the travel direction, with a light horizontal blur (~6 px). |
| out −1 | It moves ~5 % (55 px); the blur builds (~62 px). |
| **cut** | The incoming shot sits **~43 % of the width off rest** (≈ 460 px), on the side it comes from. The uncovered strip is a **mirrored copy** of the incoming frame, and the whole frame is smeared horizontally (≈ 345 px). |
| +1 → +8 | The offset **roughly halves every frame**: 460 → 260 → 118 → 52 → 24 → 12 → 5 → 2 → 0. The smear shrinks more slowly (345 → 214 → 110 → 55 → 29 → 16 → 8 → 4). The picture is sharp by frame +5 to +7; the move is done in ~9 frames (~0.35–0.4 s). |

- **Direction:** follow the incoming B-roll's own camera move when it has one; otherwise alternate. A SPLIT slides in as one unit.
- **Captions, the watermark and the hook title stay on top, sharp and still.** A sticker belongs to the picture and whips with it.
- **Silent.** No whoosh (confirmed on the separated music/SFX stem).
- **Built: `workflows/whip-slide.py`** (2026-10-05), a frame pass on the PICTURE track before the overlays go on:
  `uv run workflows/whip-slide.py IN.mp4 CUTS.json OUT.mp4`, with CUTS.json = `{"cuts": [{"frame": 48, "dir": "left"}, ...]}`. Its defaults
  are FITTED to the reference's cleanest cuts (f120, f314) with the footage's own motion removed; the frame log's "+414" at f80 was an eyeball
  estimate (the fit reads ≈ +465). Test board: `projects/mfm-nursery-rhymes/yt/work/whip-test/whip-test-board.jpg`. **Do NOT use HyperFrames' built-in `whip-pan` transition**: in 0.8.16 it
  crossfades two blurred frames and clamps the edges, which looks nothing like this (read in `shaderTransitionWorker.js`, 2026-10-05).

## 5. Captions: one system, and colour = who is speaking

| | |
|---|---|
| Font | Ultra-condensed heavy sans, ALL CAPS: **Anton** (Google Fonts, OFL) is the closest match; Impact is the fallback. Tight tracking. Calibrate the width against `board/3-captions.jpg` on the first build (the reference may be squeezed horizontally). |
| Size and place | One line, cap height ≈ 80–92 px (≈ 4.5 % of the height), centred. **Placed JUST BELOW THE SPEAKER'S LIPS, per shot** (Affan, 2026-10-06: the eyes must not travel between mouth and text): `onyx-samples/kit/ig_capy.py --dir yt` sets each chunk's glyph centre from the measured mouth, kept ≥ 20 px above the watermark (glyph centre ≤ `watermark_y` − 90; lower the watermark with `watermark_y` when the lips sit low, Rollo 1295); B-roll and screen-capture insets use the median face-shot height (an inset face counts only if it fills ≥ 0.3 of the inset: a post photo or avatar does not). A boxes-only faces.json from an older job: add `faces_lm` (a fresh `yt_faces.py` scan) and the mouth line is taken as a fraction of the box. The reference's fixed y ≈ 1070 (55.7 %) is the fallback. In a SPLIT it sits exactly on the seam. |
| Look | Off-white fill `#FCF7F7`, **3–4 px black outline**, a soft black drop shadow down and to the right. No pill or box. |
| Chunks | **1–5 words (mean ≈ 2.9), ≤ 19 characters**, ~0.7 s each. Never blank; each chunk hard-replaces the last (no exit animation). Chunks break at phrase and speaker boundaries, and the payoff noun ends its chunk ("THERE'S A CEMETERY" / "ON IT"). |
| Timing | Each chunk appears **3–4 frames (0.12–0.18 s) BEFORE its first word**. Shot cuts land on chunk changes. |
| Entrance | **A horizontal-only stretch pop over 5 frames**: width × 0.76–0.83 (blurred) → 0.89–0.97 (blurred) → 1.05–1.08 → 1.02–1.04 → 1.00. The height never changes. |
| Emphasis wipe | On **~35–45 % of chunks**: the payoff chunk of a clause (set-up chunks stay plain; in the opening never two wiped chunks in a row). One **linear, constant-speed, left-to-right wipe across the WHOLE chunk** (not word by word), with a soft edge about one letter wide (≈ 55–60 px). It starts on the chunk's 2nd–3rd frame and finishes **~82–86 % of the way through the chunk's screen time**, then holds. |
| Colour = voice | The main speaker narrating: **white → red** wipe (a red sheen: `#E70A24` at top and bottom → `#F34E5D` in the middle). Anyone else gets their own colour: **purple-magenta** (his wife quoted), **yellow** (`#F5DC0B` → `#F9E60D` → `#F0B90B`, the guest), **cyan** (`#46FEF6` → `#DCFEFA`, the realtor quoted). Another voice's plain chunks are SOLID in their colour, and their emphasis chunks wipe white → colour. The colour switches exactly at the quote boundary. |
| Profanity | Starred on screen ("SH\*T") and muted in the audio (YouTube monetisation). |

## 6. Overlays

- **Hook title (0 → ~3.2 s):** two centred lines at 69–77 % of the height, under the captions. Line 1 is small white ("SHAWN ALMOST BUYS");
  line 2 is big, in an **orange → yellow gradient** ("A HAUNTED FARM"). Heavy geometric sans (**Montserrat Black**, Google Fonts). It slides in
  from the left over ~0.46 s (fast deceleration, blurred while moving), holds ~1.8 s, slides out to the left over ~0.88 s (accelerating) and
  is gone by 3.2 s. **It names the premise in plain words** (≤ 6 words, who + what) and never repeats the captions.
- **Watermark:** the show's name (e.g. "THE SHAWN RYAN SHOW"), italic condensed caps, white at ~30–40 % opacity, ~40 px cap height, ~414 px
  wide, centred at y ≈ 1160 (60.4 % of the height, about 25 px under the captions). On every frame, static, never blurred. On an Onyx sample this
  is the PROSPECT's show name: it shows the sample was built for them. (Still no Onyx branding and no CTA.)
- **One sticker, at most:** on the biggest reaction beat (the reference: *"I was like, oh"*). A flat red "!" (`#C90506` → `#9A0204`), tilted
  ~24°, ~24 % of the frame height, beside the head. It **rises from BEHIND the speaker** (it needs a matte of him: `npx hyperframes
  remove-background` on that shot), eases into place, grows with the push-in, and leaves with the whip. It is the only shot with a designed sound (§ 8).

## 7. Motion and effects

- **Nothing is ever static.** Every speaker shot pushes in continuously: **8–14 % per second**, anchored on the face, with the crop following
  the head (a sub-second opening shot can run ~24 %/s). A still or slow B-roll shot gets 7–12 %/s. Moving B-roll keeps its own camera move at
  normal speed (handheld judder stays in).
- **One story effect per video, at most,** when the words describe something visual. The reference: after "the lights start flickering", the
  final speaker shot **flickers** (its brightness toggles between two levels ~15 % apart, in 1–4-frame runs, 51 times in 4.3 s) under steady
  captions. Same idea for a shake on "earthquake" or a glitch on "it glitched". Never decorative.

## 8. Sound

| | |
|---|---|
| Music bed | **Continuous from the first frame to the last, ≈ 13.6 LU under the voice** (bed ≈ −26 LUFS against a voice at −12.3). Mood-matched to the story (eerie for a haunting; tension or curiosity for a business story). Tonal, with **no drums or beat** competing with speech (the reference's drum stem sits at −67 LUFS). It has a sub "boom" every ~6.9 s, but **the cuts follow the words, not the music**: only 5 of the reference's 18 cuts sit within 0.3 s of a boom. It **intensifies at the story's turn** (the reference: from ~28 s of 51) and is **cut mid-bar on the last frame**, not faded. Source: Epidemic Sound (the creator's licence), with the no-drums stem or `vocals:false`, and `EditRecording` to fit the runtime. |
| Transitions | **Silent.** |
| SFX | **Almost none.** The reference has exactly one designed sound: a bright rising chime (up to ~8 kHz) on the sticker. An on-screen event (a light snapping on) may get its own literal sound. The energy comes from the bed and the pacing, not from effects. |
| Master | −12 LUFS integrated, true peak ≤ −1 dBTP. |

This is the opposite of the Instagram pilot (SFX only, no bed), which Affan found too thin on sound. See § 11, question 1.

## 9. Ending and loop

No outro, end card, CTA or fade. The last chunk finishes its wipe and holds; the video ends **≤ 0.1 s after the last word**, with the music cut
mid-bar. **The out-point is chosen so the last line runs straight into the first** ("…nobody can seem to figure it out." → "We went and we
looked at this farm"), so the replay reads as one continuous thought. Check it at the cut stage: read the last line, then the first, aloud.

## 10. B-roll sourcing (the hard part of this look)

Every noun needs real footage, sourced in this order:
1. **The show's own footage:** their past episodes and Shorts often hold the exact clip (a guest's photo, a product, a place).
2. **Real footage of the named thing** from its official source: a company's, brand's, studio's or newsroom's own channel, via yt-dlp (forced
   H.264, repo rule). A clip from **another creator's** own video stays ≤ 3 s and is flagged in BRIEF.md (a flag, never a refusal).
3. **Free stock** (Pexels, Pixabay: commercial use, no attribution needed) for generic places, objects and actions: aerials, houses, offices,
   money, crowds.
4. **Pop-culture comparisons:** the official trailer or clip from the studio's channel, ≤ 2 s.
5. **Higgsfield generation** only when nothing real exists: never for a real person, the credit cost approved by Affan first, and logged in BRIEF.md.

Prefer 4K or vertical sources: a 1080p 16:9 clip cropped to 9:16 is blown up 1.8×. Every clip is checked at full size after the crop and
enhanced if soft (the HQ rule), and logged with its source in BRIEF.md.

## 11. Questions for Affan (resolve on the first YouTube job)

1. ~~Sound~~ **DECIDED 2026-10-05: copy the reference** (Affan): a mood bed under the voice the whole way, silent whips, one sound on the
   sticker. No whooshes.
2. ~~Third-party clips~~ **DECIDED 2026-10-05: short borrowed clips are OK** (Affan): official brand footage first; a trailer or another
   creator's clip (2–3 s) only where nothing else shows the thing.
3. **Caption colour for the host:** red as in the reference, or the show's own accent colour?
4. **Hook title** on every YouTube sample, or only when the premise isn't clear from the first line?

## 12. The two looks side by side

| | Instagram look (`onyx-samples/`) | YouTube look (this file) |
|---|---|---|
| Canvas | Minimal dark canvas, the speaker inside cards | Always full-bleed picture |
| Visuals | Motion graphics: numbers, logos, grids | Real B-roll for every noun, pop-culture clips |
| Shots | FULL / CARD / GRAPHIC / SPLIT, joined by window morphs | A / B / SPLIT, joined by one whip-slide |
| Captions | Inter, sentence case, the active word in the show's accent | Anton-like ALL CAPS, stretch pop, a colour wipe on payoff chunks, colour = speaker |
| Hook | The first line | A 3 s hook title naming the premise |
| Sound | SFX only, no bed | A continuous mood bed ~13.6 LU under the voice, one SFX, silent transitions |
| Loudness | −16.6 LUFS | −12 LUFS |
| Ending | Cut on the payoff card | Cut on the last word; the loop runs into the first line |
