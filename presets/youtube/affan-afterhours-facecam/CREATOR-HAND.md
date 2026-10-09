# CREATOR-HAND — what Affan's own shipped timelines actually contain (measured 2026-10-08)

**Why this file exists.** Everything else in this preset was measured off EXPORTS (two reference videos, one of which —
Fuel System, 170k — was cut by the creator's friend, `X:\Claude Projects\GTA 6\results-log.md` V4) or off one diff
(HUMOR.md, PC release). This file is read straight out of the creator's **own Premiere timelines** for the three
face-cam videos they shipped after the style was set, decoded clip by clip from a read-only copy of the project
(`research/afterhours-channel-audit/prproj/read-timeline.py` → `summarize.py` / `aggregate.py` / `grammar-stats.py`):

| video | uploaded | views | timeline | who cut what |
|---|---|---|---|---|
| GTA 6 Is Coming To PC Sooner Than Everyone Thinks (5:16) | 09-23 | 1.1k | `ABW6-FINAL-shipped.prproj` › Sequence 24 | Claude rough cut + overlays; creator did nests, zooms, slow-downs, memes, music |
| GTA 6 Collector's Box DISAPPOINTED Everyone (6:01) | 09-25 | 559 | `ABW8.prproj` › Sequence 05 | Claude rough cut (job `gta6-vice-city-sign`); **everything else is the creator's** |
| Everything Game Informer Just Revealed About GTA 6 (6:22) | 09-30 | 287 | `ABW8.prproj` › Sequence 16 | Claude rough cut, overlays, pops, music dropouts; creator did nests, zooms, music |

Where a number here disagrees with `README.md`, **this file wins** — it is the creator's hand, not a reference.
Per-clip evidence: `research/afterhours-channel-audit/prproj/*.summary.txt`, `agg-*.txt`, `grammar-stats.txt`.

---

## 1. The face motion system — exactly how they build it

**Two saved Motion presets, by name, on almost every face shot:**

| preset (their spelling) | what it is | applied to | count |
|---|---|---|---|
| **`110 GTA LF Zoom Preset`** | Scale 100 → 110, two linear keys at the clip's first and last frame | a **nest** of a face run (≈ 5–25 s) | 16 (GI) · 17 (PC) |
| **`105 GTA Lf Zoom Preset`** | Scale 100 → 105, same two keys | a **single** face clip or a short nest (≈ 2–6 s) | 6 (GI) · 5 (PC) |
| `LF 120 Zoom Preset` / `Lf 120 Zoom` | 100 → 120 | rare (10 uses project-wide) | — |

So the push is not a rate they set — it is "+10 % across the run" (long) or "+5 % across the clip" (short). Measured
rates fall out of that: **median 0.89 %/s (GI), 1.14 %/s (PC)**, range 0.4–2.6 %/s. Replicate it with the same two
keys (start/end of the item); don't invent a rate.

**Cut zooms = a razor cut + a STATIC Scale on that clip.** Not hold keyframes, not a ramp. The clip under the
emphasis word is razored out and its Motion > Scale typed in; the next clip goes back to 100 (or to the next rung).

| | PC Release | Collector's Box | Game Informer | README said |
|---|---|---|---|---|
| cut zooms on the face | 53 (10.1/min) | 48 (8.0/min) | 23 (3.6/min) | ~5/min |
| **median scale** | **130 %** | **136 %** | **121 %** | +25 % |
| p25 – p75 | 115 – 149 | 126 – 144 | 110 – 135 | 117 – 139 |
| extremes | 201 · 215 · 294 · 356 | 180 | 161 · 203 | +40–60 rare |
| hold (clip length) median | 1.3 s | 1.3 s | 1.6 s | ~1 s |
| hold p25 – p75 | 0.9 – 1.9 s | 1.0 – 2.1 s | 1.0 – 2.2 s | |
| inside a nest | 19 | 0 (no nests this video) | 15 | — |
| with a reposition | 2 | 1 | 4 | — |

- **Size bands they use:** ~110 (a nudge), **120–150 (the normal hit)**, 160–215 (a big hit), 280–360 (an
  extreme close-up, once or twice a video). A nudge of 103–105 also appears.
- **Reposition on big hits:** the 145–205 % zooms often move Position so the face is not centred (GI 1:31.9 at 203 %
  x 0.354; 5:26.6 at 149 % x 0.435; PC 0:24.5 at 294 %), or shift down (y 0.56–0.61) to keep the eyes in frame.
- **Zoom LADDERS:** consecutive clips stepping **110 → 120 → 130 → 140**, each rung 0.7–2 s, on a build-up line
  (PC 3:48.9–3:52 and 5:01.5–5:06). +10 per rung. Use on a list or an escalating sentence.
- **Two-level nesting:** cut zooms live INSIDE the nest (static scales on the sub-clips) and the nest carries the
  110 preset — so a zoom inside a pushing nest compounds (130 × 1.08 at that moment).
- **The STRETCH GAG (in all three videos):** Uniform Scale OFF, **Scale Width 248–928 %** with the height left at
  100 (or at the cut zoom's 147), held **0.4–1.5 s** on one word — the face smeared sideways as a comic beat. PC 2:10.8
  (928 %, "the PS3"), 4:11.7 (266, in a nest), 4:32.7 (248); CB 2:42.7 (544 on a 147 zoom); GI 3:57.8 (446), 4:21.8
  (443, 0.42 s). One to three per video, on a mocking word.
- **Collector's Box had no nests and no presets at all** — cut zooms straight on V1. The nest+preset system is the
  default (two of three videos), but the zooms are what they never skip.

## 2. Slow-downs are content-driven, not a quota

| | PC Release | Collector's Box | Game Informer |
|---|---|---|---|
| face slow-downs | **11, all exactly 0.8x** (0.65–2.7 s) | 0 | 0 |
| other speed changes | motion graphics conformed 0.988x (not creative) | the screen recording frozen at **0.1x** for 6 s under a zoomed crop (5:46) | none |

HUMOR.md's "budget around ten" came from PC Release, a joke-dense script. The rule that survives all three: **0.8x,
pitch kept, only on a joke landing or a claim dropping, never on a fact** — and **zero is fine** when the script has no
comic beat. Budget from the script's jokes, not from a quota. (The export-based slow-down detector reported 4 on Game
Informer; the timeline has none — trust the timeline.)

## 3. Overlays — three treatments in use

1. **Inset over a colour matte (current default, the creator's rule since 2026-09-30, said three times):** overlay
   ~85 % of frame, rounded corners, drop shadow, over an animated colour matte that differs per slot (GI: V3 matte +
   V4 overlay, 24 slots). PC Release used the same idea with one matte file (`overlay-matte.mp4` on V2) and the
   overlays on V3 with **Drop Shadow + a keyframed scale (slow push)**.
   **Read off the finished frames (visual catalogues 2026-10-08):** Game Informer's 24 insets are exactly 85 % with
   rounded corners, each matte coloured after its subject (green for animals, amber for Red Dead weather, red for
   robberies, violet for Vice City nights — hex per slot in `game-informer/visual-catalogue.md`). PC Release's insets
   are 85–95 % with square corners and a Premiere drop shadow and they SHRINK over the hold (95 → 87, 85 → 80) over a
   near-black matte with magenta/teal glows. **Neither video has a single full-frame insert** — a break from the hit
   run, where game footage was always full frame (see `../affan-afterhours/ERAS.md`).
2. **Screen-share segment with a face PiP (Collector's Box, new):** geometry read off the frames and the raw project:
   the PiP is ≈ 372 × 388 px flush in the corner, Scale 46 **with a rectangular crop mask, feather 10**, no border,
   no shadow, never zoomed itself; the screen recording is 2560 × 1440 laid at 100 % so the 1080 frame shows only the
   centre of the screen (no browser chrome), cursor visible. Each cut flips the face between full frame and the PiP
   while the recording keeps running; his face is on screen 96.7 % of that video. the OBS recording of their screen (browser,
   articles, a YouTube video) is the full picture and **the face cam sits on top at Motion Scale 46**, top-right
   (Position 0.864 : 0.164) or top-left (0.049 : 0.164). 31 % of that video's runtime. Inside it the screen recording
   itself gets cut zooms (scale 123–186, repositioned onto the detail) and the PiP clips keep their own jump cuts. Used
   when the creator is reading/browsing sources live.
3. **Raw found artefacts:** screenshots on V1/V2 at ~81–86 % with a 5 % push (CB 0:05.96: 81 → 86 over 2.3 s), a
   YouTube clip at 84 % (CB 2:43.6), a screenshot nested and blown up to **281 %** to punch into one detail (PC 0:09.1).

## 4. The creator's own comedy inserts (none of these is in the README)

| device | where | spec |
|---|---|---|
| **TV colour-bars glitch** | PC 1:01.80 · CB 1:07.95 · GTA shorts | `TV colour bars test card screen with sine tone in 4K.mp4`, **0.20 s on V1 with its own tone on A1**, as a hard "channel change" before a new section/segment |
| **Meme clip** | PC 0:00 (facepalm, 1.9 s, opens the video) · PC 2:15.15 (`house exploding #meme#`, 0.5 s) | full-frame on V1/V3, own audio, sub-second to ~2 s |
| **Vine boom** | CB ×5 (0:04.3, 1:53.1, 3:19.6, 3:48.1, 4:51.2) · shorts | `Vine boom sound effect.mp3` at **−11 to −15 dB clip gain**, on a punchline / an absurd fact, usually riding a big cut zoom |
| **Shake + bass hit** | CB 0:34.98 | Sapphire **S_Shake** (Amplitude 1, Frequency 73, Stillness 0.7) on a 133 % zoom clip + `Bass boosted sound effect.mp3` at −27 dB |
| **Awkward cricket** | PC ~3:56.6 | `Awkward Cricket Sound Effect.mp3`, −15 dB, 3.9 s, after a joke that "doesn't land" |
| **Swears cut, not bleeped** | CB ×5 | the word razored out of the voice; nothing over it (the Shorts censor with `*` in captions) |
| **Vine boom timing** | CB | lands in the breath right AFTER the key noun, not on it |
| **Lean-in → hard cut to a found clip** | CB | leans into the lens, then hard cut to a streamer's clip (TimTheTatman) |
| **SUBSCRIBE animation** | PC ×3 (8.4 s each) · Fuel ×2 · DIRTIEST ×5 | canned bottom-left, dropped mid-sentence, never cued; its sequences live in ABW8 (`SUBSCRIBE 04`) |
| **Fade from black** | CB 0:00 | Black Video, Opacity 100 → 0 over the first ~1 s |
| **Fade to black** | GI end | last nest Opacity 100 → 0 over its tail |

## 5. Sound — the creator's levels

- **Music = their own Epidemic picks, recurring across videos:** `ES_Loungin – Scientific` opens all three (the
  channel's cold-open bed), then `ES_First Born – Timothy Infinite`, `ES_Brooklyn – Dyalla`, `ES_Take a Ride –
  Scientific`. One track per section, 2–3 tracks per video.
- **Level is set by CLIP GAIN, not volume: −20 to −27 dB, typically −24.** The files measure ≈ −11 LUFS, so the bed
  sits ≈ −31 to −38 LUFS, i.e. **~14–18 LU under the voice** (masters measure −16.6 / −17.3 / −17.4 LUFS integrated,
  LRA 6–7 LU). They ride it by section: −20 under a cold open or a turn, −26/−27 under dense explanation.
- **Music OUT under cut zooms:** 23/23 on Game Informer (the creator's rule, 2026-09-30, `music-dropouts.py`); on the
  earlier two it was done by hand on part of the video (PC 25/53, CB 14/38 — CB's cold open has it on every zoom).
  Current rule: every cut zoom.
- **Overlay pops — the uncaptured correction:** Game Informer's 44 `es-pop-mouth-finger.wav` pops were placed at
  Volume −6 dB; the creator then added **Clip Gain −12 dB to 39 of them and −7 dB to the four rapid C02 pops** and
  added one more at 0:00. **Effective pop ≈ −18 dB** (−6 vol −12 gain). Place pops there from now on.
- **Meme SFX levels:** Vine boom −11…−15 dB gain, bass boost −27, cricket −15.
- **Voice:** the shipped A1 is the creator's Enhance Speech bounce (channel LESSONS 2026-09-20); masters land ≈ −17
  LUFS integrated.

## 6. Shape of the whole edit (timeline-measured)

| | PC Release | Collector's Box | Game Informer |
|---|---|---|---|
| runtime | 5:15.7 | 6:00.7 | 6:22.2 |
| edit points / min (all tracks, incl. inside nests) | 33.3 | 31.8 | 24.2 |
| first 60 s | 27 | 29 | 26 |
| face share | 73 % | 68 % full + 31 % as PiP | 73 % |
| face runs | 21 · median 10.0 s · max 24.5 s | 26 · median 4.4 s | 24 · median 10.8 s · max 29.9 s |
| first frame | a meme (facepalm) with the voice already running | fade from black into the face | an overlay (the Game Informer article) + a pop at 0.000 |
| last frame | face | face (a 129 % cut zoom) | face, fading to black |

**"Opens on the face" is no longer strict:** two of three open on an overlay/meme at frame 0 with the voice already
talking. What is constant: the voice starts at 0.000, and the video ENDS on the face.

## 7. Not GTA — rules from the other channels that must NOT be applied here

These live in the shared `memory/` and come from Abundance Wisdom / Onyx work. They contradict this channel:
- `feedback-no-same-camera-punch-ins` (Onyx) — GTA's signature IS the same-camera punch-in.
- `feedback-premium-sfx` ("never goofy/meme sounds") and `feedback-cinematic-pacing-longform` (slow, no bombardment) —
  AW documentary register. GTA uses Vine booms, crickets, colour-bar glitches, memes, 24–33 edits/min.
- `feedback-whooshes-too-loud` / `feedback-voice-first-mix` numbers — AW/Onyx mixes. GTA's own levels are § 5 (the
  principle "voice on top, SFX under it" does hold here too: see the pop correction).
- AW caption fonts (Gretaros, Ubuntu Light) — GTA Shorts captions are **Anton**.
