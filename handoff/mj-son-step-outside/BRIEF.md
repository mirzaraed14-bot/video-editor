# BRIEF: Why Michael Jackson's Son Had To Step Outside 💔 (Abundance Wisdom Short)

## ▶ STATUS: resume here
**2026-11-08 ~23:25: SEQUENCE COMPLETE FOR REVIEW, STOPPED for Affan's creative direction.** `MJ Son Step Outside - raw cut` (bin `MJ Son Step Outside`, ABW10.prproj, UNSAVED), 1080x1920 30 fps, 35.467 s: V1/A1 9 clips, V2 3 picture-only Lionsgate covers (A2-A4 empty), 6 markers. Read back = plan (every in-point equals the plan to the frame); A1 rebuilt from the read-back and re-transcribed = the table's words (plus the "like" below). His active sequence (Bieber) restored. No music, no captions, no graphics, no SFX, no CTA, nothing saved, nothing exported. State/resume: `RUN.md`.

## Final timeline (30 fps; read back from Premiere)
| Beat | Sequence tc | s | Source of the sound (file = what Premiere plays) | Picture |
|---|---|---|---|---|
| 1 | 00:00:00:00-00:00:04:15 | 4.50 | ABC 219.200-223.700 ("Tell us how it was ... role of your dad.") | ABC Prince panel (3-up), 484 % |
| 2 | 00:00:04:15-00:00:11:28 | 7.43 | KIIS file 122.934-130.367 (I never got to see ... very young.) | KIIS 1080p, 178 % |
| 3 | 00:00:11:28-00:00:19:29 | 8.03 | ABC 249.667-252.733 + 253.133-258.100 (pause after "makeup" tightened) | ABC panel 415 %; V2 00:00:13:07-00:00:14:16 (1.3 s) Prince on set laughing beside Jaafar (featurette 120.57-121.87), ends just before "makeup" |
| 4 | 00:00:19:29-00:00:23:09 | 3.33 | ABC 259.667-263.267 ("Jaafar just embodied him ... that moment") | V2 whole beat: Jaafar on stage (featurette 125.33-128.67); the ABC panel is hidden |
| 5 | 00:00:23:09-00:00:35:14 | 12.17 | ABC 263.567-269.167 + 269.433-272.500 + 272.633-275.867 ("And it was difficult ... get some air.") | ABC panel 415 %; V2 00:00:29:05-00:00:30:19 Jaafar in costume (featurette 108.65-110.12), saying "Jaafar" on screen and hiding the ABC dissolve; razor at 30:13 (270.70 s), then ABC full frame above the banner 349 % from about 30.63 s to the end (about 4.8 s); HARD CUT after "air" |
V1 clip edges: 0, 4.500, 11.933, 15.000, 19.967, 23.567 (the "And" opening B5 is the last word of B4's clip, at 23.30), 29.167, 30.433 (razor), 32.233, end 35.467. Markers: B1 0.000, B2 4.500, B3 11.933, B4 19.967, B5 23.300, HARD CUT 35.433.
**Premiere stores floor_seq(floor_src(requested in-point))** (a 29.97/23.976 source on a 30 fps sequence): the first placement landed every in-point 19-48 ms early, so it was deleted (my own sequence only) and rebuilt with each in-point requested at the first source frame boundary at/after the chosen 1/30 s boundary; the read-back now equals the plan. The KIIS window was re-encoded from a frame-aligned start (118.034 s; file `msso_kiis3_h264.mp4`, A/V start 0). Leftover in my bin: an unused first-pass `msso_kiis_h264.mp4` (this Premiere has no `deleteAsset`).
Edge levels at every cut (10 ms RMS): -45 to -60 dBFS at all joins except B1's in (-37, the /t/ burst of "tell" begins 5 ms after it) and the final piece's in (-36, 10 ms before "but").

Script: `research/instagram-beat-mining/IDEAS.md` § "MJ REPLACEMENT (8 Nov, evening)" (5 beats, about 37 s). Locked prediction: `research/instagram-beat-mining/RESULTS-TRACKER.md` (not edited here): 80K-2.5M, centre 200-500K. Biggest predicted failure: the proof is for the on-set picture (4M), not the quote (49K, 1.8K).

## The script (locked, exact words)
| # | Who | Exact words | Picture (table) |
|---|---|---|---|
| 1 | Linsey Davis, ABC News Live Prime | "Tell us how it was watching your cousin Jaafar transform into this role of your dad." | Prince's panel, banner out |
| 2 | Prince, 102.7 KIIS FM / JoJo Wright | "I never got to see my dad perform live. The closest I ever got was the Madison Square Garden, right before 9/11. And I was very young." | Prince, studio |
| 3 | Prince, ABC | "The first time that I saw him in person, in his hair and makeup, was really an emotional shock, because I had not seen my father in a long time." | on-set Prince, then ABC |
| 4 | Prince, ABC | "Jaafar just embodied him and brought him back in that moment." | Jaafar as Michael (adult, official Lionsgate) |
| 5 | Prince, ABC | "And it was difficult to maintain and keep composure, because I really just wanted to give him a hug in that moment. But I had to tell him, 'Jaafar, I'm proud of you. You're going to do great. But I need to take a little step outside and get some air.'" HARD CUT | Prince (ABC full frame from about 4:32) or the on-set shot |

## Hard rules
No minors on frame (checked on every placed span and every cover). No music bed (his job). Silence: nothing played, ffmpeg to files only. Premiere: `premiere.lock` for every window, NEW sequence only, never touch his sequences (the Bieber and rejected MJ sequences untouched), never save, never export, restore his active sequence. YouTube only through `lock.sh youtube`, plain yt-dlp, >= 60 s apart, no cookies/proxies/client switching. Prince is composed and smiling on camera in ABC: no effects to fake emotion.

## QUALITY GATE (Affan 8 Nov): real >= 720p, clean close audio, logged per beat
Resolution of the FILE and of the crop actually shown (a 9:16 window of a 16:9 source; scale is what is applied to the source pixels to fill 1080x1920):
| Beat | File (ffprobe) | 9:16 window used | Scale | Audio verdict |
|---|---|---|---|---|
| 1 | ABC `eOBq4qHOsxI`, 1280x720 H.264 Main 29.97 fps, AAC 44.1k | 223x397 px (Prince panel of a 3-up, x278-553, y105-508) | **484 %** | clean: no music, no bed; pauses fall to -59 dBFS at the cut, 5th-percentile floor -50 dBFS vs speech p90 -18 |
| 2 | KIIS `6mbkmGadUsk` local file, 1920x1080 H.264 23.976 fps, AAC 44.1k | 607x1080 px | 178 % | clean studio mic; floor -45 dBFS vs speech p90 -19; pauses -55 dBFS at the cut |
| 3 | ABC, same file | 260x463 px (Prince panel of a 2-up, x8-425, y71-542) | **415 %** | clean; floor -50 dBFS vs speech p90 -17 |
| 4 | ABC | 260x463 px (picture covered by Lionsgate 1080p) | 415 % (ABC picture hidden) | as 3 |
| 5 | ABC | 260x463 px until the layout dissolve ends (270.70 s), then full frame above the banner 309x550 px | 415 % then **349 %** | as 3; one faint steady line at 3680 Hz, -71 dBFS in the pauses (53 dB under speech): inaudible |
| covers | Lionsgate featurette `-KkNPUvFqco`, 1920x1080 H.264 23.976 fps | 607x1080 px | 178 % | picture only, audio removed (the featurette has music) |
**ABC is a real 720p upload but the Prince picture inside it is small (the panel, the banner out): every ABC shot is magnified 3.5-4.8x to fill 9:16. This is the one resolution risk of the build; no better source for these lines exists (the answer is only on ABC).** Audio method: WhisperX word spans, spectrograms of each line (`proof/spec/sheet.png`: speech formants only, no horizontal bed), pause floors. The first gap-SNR attempt was discarded: WhisperX gaps still hold word tails, so its "tonal peaks" (109-184 Hz) were the speakers' own pitch.

## Sources (downloaded 8 Nov 22:08-22:11 through `lock.sh youtube`, plain yt-dlp, 100 s apart, no bot check)
- `eOBq4qHOsxI` ABC News "Michael Jackson's son Prince reveals his takeaway watching 'Michael' film" (24 Apr 2026, 482 s, 1.6M views). Best H.264 offered is 720p (AV1/VP9 stop at 720p too). ABC: split screen, ABC banner across the bottom (y>=557 of 720). Layout by frame: 212-216 2-up; 218-226 3-up (Linsey | Prince | film); 228-270.6 2-up; dissolve 270.37-270.70; full frame Prince 270.70-276; Linsey + Prince 278+.
- KIIS: `E:\Bullshit Folder\Henry\Prince Jackson Opens Up_ Michael Jackson's Legacy, the Michael Movie _ Moments Fans Never Knew.mp4` (1080p, 27.8 min). Speaker confirmed by frame (lips move, studio, headphones).
- Lionsgate featurette `-KkNPUvFqco` (official "On the Set of Michael", 8 May 2026, 147 s, 1080p). Used for ALL picture-only covers. ET `VpFNXZfaCYc` (1080p, downloaded) is NOT used: same footage as the featurette in the later half, but with the ET logo and a music bed.
- Premiere-safe re-encodes in `h264/` (CRF 12 H.264 + AAC 256k): `msso_abc_h264.mp4`, `msso_lg_h264.mp4` same timeline as the source; `msso_kiis_h264.mp4` is the window starting at 118.000 of the KIIS file. A/V lag vs the raw audio: 0.00 ms (cross-correlation on 4 windows).

## Word check (WhisperX large-v3 + alignment, every line against the table)
All five lines match the table word for word, with these exceptions, reported not hidden:
- B2: Prince says "...Madison Square Garden, **uh** right before 9/11" (the table has no "uh"); also a false start "I uh I never" (cut: the clip starts at the second "I"). The "uh" is KEPT: no silent edge exists around it (garden/uh/right are continuous voiced sound at -22..-30 dBFS; the nearest dip is -35).
- B5: Prince says "I had to tell him **like** Jaafar, I'm proud of you" (the table has no "like"). KEPT: him/like/Jaafar are continuous, so a cut would be a stutter. The cut-out would have been a visible same-camera jump too.
- B5: the "And" that opens the beat is the last word of the B4 clip in the timeline (it sits 20 ms away from "moment" in the source); the beat 5 marker is placed on it.
- WhisperX spells Jaafar "to far" (B1), "Jafar" (B4), "your farm" (B5): mishearings of the same name; the real words are the table's.
- The table's ABC clock times are off: the question is 3:39.2-3:43.6 (not 3:36-3:43), beat 3 is 4:09.7-4:18.1, beats 4+5 are 4:19.7-4:35.9 (table 4:05-4:35). The words, not the clock, set the cuts.
- Speakers by frame: Linsey Davis (3-up panel, B1), Prince (all others). B1's picture is Prince's panel (listening), as the table says.
Pauses tightened (the standard AW tighten, pauses >= 0.13 s over the keep margins): 0.42 s after "And" in B5, 0.28 s after "makeup" in B3, 0.14 s in B5; the last line "but I need to take a little step outside and get some air" is NOT tightened (his hitches stay).

## Picture plan (deviations from the table, with reasons)
- B1 picture = the ABC Prince panel (per the table).
- **B3 follows the table's "on-set Prince, then ABC":** the featurette shot 120.45-122.54 (also ET 120.45-122.52; at about 2:00-2:02, not the brief's "about 2:08"): Prince laughing beside Jaafar in the sequin jacket, headset round his neck. It is the brief's "headset shot of Prince on set, sharing the frame with Jaafar", and the picture the 4M Short sells. Used 1.3 s (featurette 120.57-121.87), ending just before "makeup": he leans out of a static 9:16 crop after ~122.0. (The ET shot at 137.5-138.5 with a cap and headset is a different, 1 s shot, not used.)
- **B5's dissolve cover is Jaafar in costume** (featurette 108.65-110.12, the Billie Jean jacket close-up, adult), on screen exactly when Prince says "Jaafar"; it hides the ABC 2-up to full-frame dissolve (270.37-270.70) and the razor at 270.70.
- B4 picture = Jaafar as Michael on stage, featurette 125.33-128.63 (one 4.5 s shot, adult actor). No child actor anywhere.
- B5 = ABC panel, then full-frame Prince (above the banner) from about 30.63 s (after the cover lifts) to the end, about 4.8 s: the hard cut lands on him.
- Identification: the on-set man with long wavy hair and a headset (featurette 120.45-122.54) is Prince per the brief; no name card, and the featurette's own on-set interview of Prince (white MICHAEL tee, short hair, 134.47-136.51) looks different, so the basis is the brief plus his face and beard. **The unambiguous on-set Prince alternative is that interview shot, 134.47-136.51 of the featurette.** The Jaafar identification (sequin-jacket close-up and stage shots) rests on the featurette's own Jaafar-on-set sequence; all adult.

## CATALOG PASS (2026-11-08, CLAUDE.md learning loop 5: `research/effects-catalog/CATALOG.md` read in full; all 137 reference stills looked at on `projects/mj-showed-his-mother/proof/catalog_0.jpg` + `catalog_1.jpg`; the shots folder is unchanged since 8 Oct). HELD for his direction: nothing below is built in this pass, and the brief says the words carry the emotion, so no effect is used to fake it.
- **Fits this Short:** FX-40 Slow-Burn Portrait (a tight face held with no text while the frame creeps in: the last 4.8 s on Prince's full frame, "need to take a little step outside and get some air"); FX-80 Black-Beat Ident (the hard cut after "air" read as a dip to black); FX-57 Propped Phone Call (a remote interview is never full-screen: the ABC panel is already that); FX-37 Ghost Dissolve (Prince's face ghosting into Jaafar between B3 and B4: the dissolve the story is about); FX-79 Flash-Forward Echo (the on-set shot returns).
- **Not used on this channel lately:** a one-voice Short with no card and no archive; FX-40's held portrait and FX-37's slow ghost.
- **The last build leaned on:** designed cards and montage (MJ Victory Tour). This one deliberately has none.

## Sequence plan
`RUN.md` carries the timeline; `edl.json` + `premiere/place.jsx` rebuild it from scratch (delete the sequence by hand first: `premiere/run_window.py` refuses if the name exists).
