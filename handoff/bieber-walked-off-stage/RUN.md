# RUN: bieber-walked-off-stage (Abundance Wisdom Short "Why Justin Bieber Walked Off His Own Stage 💔")

## ▶ STATUS: resume here
**2026-11-08 ~22:40: HIS TELLA 1 IS IN (BRIEF.md "TELLA 1"); THE SEQUENCE IS HIS NOW.** He re-cut `Bieber Walked Off - raw cut` before recording (37.671 s, V1 20 + V2 8 + A1 25, no V3). Snapshot: `premiere/his_v1_readback.json`. **My rebuild scripts (`delete_seq.jsx`, `create_seq.jsx`, `place.jsx`, `fixin.jsx`) must NEVER be run on it again: they would destroy his edit.** Anything new goes on a copy (a `... v2` sequence) or on tracks above his, after reading his state again.
- What his video asks (10 items, BRIEF.md): better Oslo quality or letterbox/zoom-out, a Higgsfield-enhanced freeze frame (B2a), an earlier-performance video overlay from the same concert (B2b), a young-Justin overlay (B4) re-used slowed/warped in B5, name+relation cards, two Pattie/Jeremy stills + one Justin-and-mother still (B6), mellow pacing. Flags for him: the crowd on frame vs the minors rule, "her husband", Higgsfield credits.
- History: first build 17:55 (B2 an empty slot, YouTube bot check 16:59), flag cleared 19:26, B2 filled 19:50 (Inside Edition audio + the 8.2M Short's picture), Oslo swapped to the Short; his re-cut happened after that (~22:00-22:15).
- 23:20: sourcing after his Tella 1 (BRIEF.md "SOURCING AFTER TELLA 1"): no better Oslo source than the Short exists on YouTube, no same-concert earlier performance found (only the Senkveld TV studio set, same day), freeze-frame candidates exported to `research/stills/`, young-Justin and Pattie/Jeremy stills not searched yet. Nothing placed in Premiere; his sequence untouched.
- 23:30: he answered "Show crowd" (Oslo crowd stays visible in the zoom-out, no blur; BRIEF.md). Web search for the Pattie/Jeremy/Justin stills found no usable file (agency photos only). Still open: Higgsfield credits OK for the freeze frame, Senkveld as B2b ("earlier the same day") or skip, which young-Justin pool, how the stills get sourced. Nothing placed in Premiere.
- 23:55: he said not to extract stills from video: found NRK P3's CC BY-NC-SA Flickr photos of the same concert (1920x1080), enhanced three in Higgsfield (6 credits, balance 886.75): `research/stills/nrk-p3-same-concert/` (BRIEF.md "B2 STILLS FROM THE SAME CONCERT"). Nothing placed in Premiere; his sequence untouched.
- 2026-11-09: he chose B (facing) for B2a. B6 stills searched in the browser: candidates A (Justin 18 + Pattie, AMAs 2012) and B (Jeremy + adult Justin) in `research/stills/b6-parents/`, a clean Pattie-with-Jeremy photo does not exist without minors. Nothing enhanced or placed.
- 2026-11-09: "Yes, two stills": B6 = A (Justin 18 + Pattie) and B (Jeremy), both enhanced (4 credits, balance 882.75), files in `research/stills/b6-parents/`. Still open: B2b (Senkveld / stand-in C / skip), the young-Justin overlay for B4/B5. Nothing placed in Premiere.
- 2026-11-09 ~01:35: **`Bieber Walked Off - raw cut v2` built** (clone of his cut + V4 + 3 stills + 3 name cards, BRIEF.md "V2 OVERLAY SEQUENCE"); his own sequence untouched and identical to the snapshot; previous active sequence restored; nothing saved or exported. Still open: B2b, the young-Justin overlay (B4/B5), his sign-off on this v2.
- 2026-11-09 ~02:10: B2b = stand-in still C (his pick), laid on V3 of v2 at 4.14-7.95 (letterbox on blurred fill); v2 = his 53 clips unchanged + 7 overlay clips (readback `premiere/v2_readback2.json`). Still open: the young-Justin overlay for B4/B5 and its slowed re-use in B5, his sign-off.
- 2026-11-09 ~03:10: "Yes, Confident": young-Justin overlays laid on V3 of v2 (B4 15.62-18.22 at 1x, B5 18.22-21.76 same shot at 50 %); v2 = his 53 clips unchanged + 9 overlay clips (readback `premiere/v2_readback3.json`). All ten asks of his Tella are now either in v2 or flagged; open: his review of v2, the B5 warped-edge look, the zoom-out of B1b/B3a, the Higgsfield video upscale decision.
- 2026-11-09 ~03:30: "Yes, zoom out": B1b and B3a zoomed out on v2 to his own values (Motion only; readback `premiere/v2_readback4.json`). v2 vs his cut = 9 overlay clips + those two Motion values. Open: his review of v2, the B5 warped-edge look, the Higgsfield video upscale decision for the Confident overlay.
- The old build scripts stay in `premiere/` for reference; `readback.jsx` / `restore_active.jsx` are read-only and safe.

## Lessons from this build (also in `lanes/premiere/lab-notes.md` 2026-11-08)
1. **`audioTrack.overwriteClip(item, t)` on an A/V item also drops its VIDEO on V1.** Order that works (verified twice): the audio-only twin goes right BEFORE its hold, after the preceding AV row (the hold then overwrites the stray video; the twin placed before the preceding AV row loses its head to that row's 0.2 s over-trim; placed after the hold it replaces the hold).
2. **A 6 s hold item overwrites 6 s**: the over-trim ate the next V1 clip's head in the first attempt. Place the next clip after it.
3. **Placed in-points land 4-52 ms early.** After placing, set `clip.inPoint = Time` exactly (`fixin.jsx`): it moves only the source in-point, start/end stay.
4. `project.deleteSequence(seq)` works on my own sequence; `clone()` / `setSettings` leave the NEW sequence active: restore the previous one at the end.
5. wav2vec2 forced alignment cannot time numerals ("19", "21"). Isolated faster-whisper DTW (`premiere/fw_words.py`) can, but is ~0.2 s early on noisy audio; RMS gaps (`premiere/gaps.py`) are the ground truth.
6. `dl.sh` matched an OLD bot-check line in a re-used download log and printed STOPPED after a successful download: it now greps only `tail -n 15` of the log.

## Sources (originals in `src/`, H.264 mezzanines for Premiere in `seq_src/`)
| id | what | file | res / fps | used for |
|---|---|---|---|---|
| `Uz2-nYKCFIo` | *Seasons* "The Dark Season", Justin Bieber's official channel, 14:49 | `src/Uz2-nYKCFIo.mp4` | **1920x1080 H.264, 23.976 fps**, 2.3 Mbps (best H.264 offered; 4K only as VP9, skipped as instructed) | B4-B7 (`seq_src/seasons_140_300.mov`, window from 140.014875) |
| `-raBuLTeArQ` | "Justin Bieber leaves/walks the stage in rage after yelling at his fans", Spontaneous Story, the 8.2M Short, 0:30 | `src/-raBuLTeArQ.mp4` | **720x1280 H.264, 30 fps** (the full vertical phone frame, no captions, no watermark); the phone video itself, so the best Oslo source found | B1, B3 (`seq_src/short_full.mov`); its picture 22.55-29.40 under B2 |
| `jaDjwOE-k0o` | Inside Edition, "Justin Bieber Apologizes For Storming off Stage: 'It's Been a Rough Week'", 0:50 | `src/jaDjwOE-k0o.mp4` | **1280x720 H.264, 29.97 fps** (the picture is the same ~420 px phone strip with a burned-in "Guys nevermind!" subtitle 2.5-5 s and the IE bug); the anchor line is a **voice-over at 6.03-12.52 s**, no anchor on camera | B2 audio only |
| `eCX64yPx8sw` | WSJ 0:37 (AP/Newsflare phone video) | `src/eCX64yPx8sw.mp4` | 1280x720, ~420 px strip | used in the first build (B1, B3), replaced by the Short; its mezzanine `seq_src/wsj_full.mov` stays in the bin unused |
- **B2 is a hybrid mezzanine**: `seq_src/b2_hybrid.mov` = the Short's picture 22.55-29.40 (found by frame matching: Short time = Inside Edition time + 16.65 s, stable 6.2-10 s) + Inside Edition's audio 5.90-12.75. The picture is the same phone video as under the anchor line in the Inside Edition upload, only sharper.

## Verification
- WhisperX large-v3 on every downloaded file (`asr/seasons`, `asr/wsj`, `asr/ie`, `asr/short`), then on the rebuilt timeline (`asr/timeline`): B4 "He's making some wrong decisions, but I never really believed that that person that the whole world hated so much was who he is." ✓; B5 "When he turned 18, it started bubbling a little bit. 19 [to], what was it, 21? That was probably that dark period." ✓ (the re-ASR does not hear the short "to"); B6 "His mother was a child when she raised him, and she was in a very conflicted relationship with his dad. And so there was chronic stress." ✓; B7 "I never had that security in a family. I never had that consistency." ✓. Isolated faster-whisper re-listen of the timeline audio: B1 "Nevermind, I'm done. I'm not doing a[the] show." ✓; **B2 "It's a complete meltdown from Justin Bieber. He stormed off the stage after performing just one song." ✓ word for word**; B3 "What are you doing? Stop it. Hey,[the onset of "I'm" split by the ASR] I'm trying to wipe the floor. Give me a second." ✓.
- Speakers: name cards at 144 s (Scooter, "manager"), 184 s and 192 s (Allison Kaye, "management"), 281 s (Dr. Daniel Amen, "Justin's brain health doctor"); Justin in the pink hoodie at 241-246 s (frames, mouth moving). A mouth-motion vs audio correlation (`premiere/lipsync.py`) proved nothing either way: identification rests on the cards and the frames. The B2 voice is Inside Edition's own anchor VO (not on camera).
- Picture: every Seasons row sits inside one shot (`proof/emu/edges.jpg`); YuNet sweep of every frame of every Oslo and B2 row (`proof/emu/*_faces.json`, `flagged3/4.jpg`): only Bieber, bodyguards and the stage person (adults); no audience in any window.

## Placed plan (tl seconds; read back from Premiere, 0 mismatches)
| id | tl | what | source in-out (source clock) | Motion | words |
|---|---|---|---|---|---|
| B1a | 0.000-0.934 | AV the 8.2M Short `-raBuLTeArQ` 720x1280 | src 19.620-20.554 | scale 408.511, pos 1.3624,1.3617 | Justin: Never mind. I am done. |
| B1b1 | 0.934-1.335 | AV the 8.2M Short `-raBuLTeArQ` 720x1280 | src 20.554-20.955 | scale 369.231, pos 1.0265,1.0769 | I'm not doing (audio continuous with B1a) |
| B1b2 | 1.335-1.568 | AV the 8.2M Short `-raBuLTeArQ` 720x1280 | src 20.955-21.188 | scale 376.471, pos 0.4529,1.0588 | the show. (audio continuous with B1b1) |
| B2 | 1.568-8.208 | AV B2 hybrid: Short picture + Inside Edition `jaDjwOE-k0o` audio | src 5.985-12.625 | scale 150.0, pos 0.5,0.5 | Inside Edition anchor (voice-over): It's a complete meltdown from Justin Bieber. He stormed off the stage after performing just one song. |
| B3a | 8.208-9.343 | AV the 8.2M Short `-raBuLTeArQ` 720x1280 | src 4.030-5.165 | scale 342.857, pos 1.0952,1.1429 | What are you doing? Stop it. |
| B3b1 | 9.343-9.810 | AV the 8.2M Short `-raBuLTeArQ` 720x1280 | src 13.745-14.212 | scale 342.857, pos 0.3492,1.0714 | I'm trying to wipe the |
| B3b2 | 9.810-11.278 | AV the 8.2M Short `-raBuLTeArQ` 720x1280 | src 14.212-15.680 | scale 342.857, pos 0.6667,1.0714 | floor. Give me a second. (audio continuous with B3b1) |
| B4a | 11.278-13.180 | AV *Seasons* `Uz2-nYKCFIo` 1080p23.976 | src 191.680-193.582 | scale 177.778, pos 0.821,0.5 | Allison Kaye: He's making some wrong decisions, but |
| B4b | 13.180-17.317 | AV *Seasons* `Uz2-nYKCFIo` 1080p23.976 | src 194.040-198.178 | scale 177.778, pos 0.821,0.5 | I never really believed that that person that the whole world hated so much was who he is. |
| B5a | 17.317-19.486 | AV *Seasons* `Uz2-nYKCFIo` 1080p23.976 | src 149.140-151.309 | scale 177.778, pos 1.2901,0.5 | Scooter Braun: When he turned 18, it started bubbling a little bit (picture: TMZ b-roll, left panel) |
| B5b | 19.486-20.921 | AV *Seasons* `Uz2-nYKCFIo` 1080p23.976 | src 152.260-153.695 | scale 177.778, pos 1.2901,0.5 | to, what was it, 21? (19 kept, see RUN.md) (picture: TMZ b-roll) |
| B5c | 20.921-22.322 | AV *Seasons* `Uz2-nYKCFIo` 1080p23.976 | src 153.695-155.096 | scale 177.778, pos 0.3025,0.5 | That was probably that dark period. (Scooter on camera; audio continuous with B5b) |
| B6a | 22.322-23.423 | AV *Seasons* `Uz2-nYKCFIo` 1080p23.976 | src 279.865-280.966 | scale 177.778, pos 0.9543,0.5 | Dr. Amen: His mother |
| B6b | 23.423-24.291 | AV *Seasons* `Uz2-nYKCFIo` 1080p23.976 | src 281.160-282.027 | scale 177.778, pos 0.9543,0.5 | was a child |
| B6c | 24.291-25.259 | AV *Seasons* `Uz2-nYKCFIo` 1080p23.976 | src 282.510-283.478 | scale 177.778, pos 0.9543,0.5 | when |
| B6d | 25.259-26.193 | AV *Seasons* `Uz2-nYKCFIo` 1080p23.976 | src 283.810-284.744 | scale 177.778, pos 0.9543,0.5 | she raised him. |
| B6e-V | 26.193-31.198 | V Dr. Amen freeze (284.867) | src 284.867-284.867 | scale 177.778, pos 0.9543,0.5 | HOLD on Dr. Amen (the episode shows child Justin here: minors rule) |
| B6e-A | 26.193-31.198 | A *Seasons* `Uz2-nYKCFIo` 1080p23.976 | src 285.190-290.195 | scale -, pos -,- | And she was in a very conflicted relationship with his dad. |
| B6f | 31.198-33.800 | AV *Seasons* `Uz2-nYKCFIo` 1080p23.976 | src 290.690-293.293 | scale 177.778, pos 0.9543,0.5 | And so there was chronic |
| B6g | 33.800-34.368 | AV *Seasons* `Uz2-nYKCFIo` 1080p23.976 | src 293.520-294.087 | scale 177.778, pos 0.9543,0.5 | stress. |
| B7a | 34.368-35.502 | AV *Seasons* `Uz2-nYKCFIo` 1080p23.976 | src 241.090-242.225 | scale 177.778, pos 0.263,0.5 | Justin: I never had that |
| B7b | 35.502-37.704 | AV *Seasons* `Uz2-nYKCFIo` 1080p23.976 | src 242.630-244.832 | scale 177.778, pos 0.263,0.5 | security in a family. I never had that |
| B7c | 37.704-38.739 | AV *Seasons* `Uz2-nYKCFIo` 1080p23.976 | src 245.090-246.124 | scale 177.778, pos 0.263,0.5 | consistency. HARD CUT |

V3: `He was 21 in Oslo.` card 20.387-22.322 (`seq_src/card-he-was-21-in-oslo.png`). Markers: B1 0.000, B2 1.568, B3 8.208, B4 11.278, B5 17.317, CARD 20.387, B6 22.322, B7 34.368.
