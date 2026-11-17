# RUN: mj-fired-his-father ("Michael Jackson FIRED His Father"), Abundance Wisdom Short, movie <-> real format: RAW CUT (STOP 1) in Affan's ABW11

## ▶ STATUS: resume here
- **18 Nov 2026 ~00:25 PKT (machine clock): everything is built OFFLINE; the Premiere window has NOT run yet** (kit in `premiere/`, mezzanines in `seq_src/`, proof in `proof/`). Next: `python -I premiere/run_window.py --run` (takes `premiere.lock`, refuses unless he has been idle >= 150 s), then `--readback` is built in, then `python -I premiere/verify_readback.py` -> `premiere/READBACK.md`.
- **Sequence to be created:** "Michael Jackson FIRED His Father - raw cut" in bin "Michael Jackson FIRED His Father" (ABW11.prproj, a clone of his "Sequence 02", 1080x1920 @60). 19 V1/A1 clips, 1 V2 cover, 10 markers, **38.30 s** (36.23 s without the optional B7b + B7c). Not saved, not exported (he does both).
- **The plan:** `research/aw-mj-2026-11-17/format/SEQUENCE.md` v1.2 "V1 - movie -> real" (8 beats, his OK 18 Nov: "thsi is good build the raw in premire"). Evidence + format: `research/aw-mj-2026-11-17/format/`. Hub: local_3ae3a4cf (AW hub); research session `aw-mj-beats`.

## What is built (all numbers from `premiere/plan.json`, `place_rows.json`)
| beat | side | source (in -> out, measured) | timeline |
|---|---|---|---|
| 1 | MOVIE "THE MOVIE (2026)" | FILM 142.325-143.640 / 148.340-149.270 / 151.120-152.270 / 154.205-154.830 | 0.00-4.08 |
| 2 | REAL "THE REAL MICHAEL · 1979" | 1979 special 72.645-78.185, **V2 cover** (held Michael frame 72.50) over the special's Joe cutaway 72.517-74.567 | 4.08-9.65 |
| 3 | MOVIE | FILM 195.065-201.550 as three clips butted on the shot changes 197.333 / 200.033 | 9.65-16.15 |
| 4 | REAL card | type on black, 3.2 s, silent (placeholder, SFX at STOP 2), no year | 16.15-19.35 |
| 5 | MOVIE "KATHERINE (THE MOVIE)" | FILM 215.320-216.190 / 224.560-225.900 / 227.720-229.055 | 19.35-22.93 |
| 6 | REAL "THE REAL JOE · CNN, 2013" | Piers 217.884-222.201 (question) + 224.290-228.074 (Joe) | 22.93-31.03 |
| 7 | MOVIE | FILM 288.517-289.600 (approved) + OPTIONAL 297.733-298.183 / 301.067-302.683 | 31.03-34.18 |
| 8 | REAL "THE REAL MICHAEL · 1979" | 1979 special 84.033-85.550 (mixing-desk B-roll) + 85.550-88.150 (Michael on camera), hard cut on "yes" | 34.18-38.30 |

## Decisions (each measured; evidence in `analysis/`, `proof/`)
1. **Every edge is a MEASURED acoustic edge, not the SEQUENCE.md aligner time.** The sequence's in/outs are word-aligner times; `analysis/edges.py` ran the real `polish-boundaries.py`, then I read the 5-20 ms envelopes at each edge and overrode the tool where it swallowed a neighbouring sound. Overrides: B1b out 149.27 (a 100 ms bump at 149.29-149.39 follows "dad."), B1c in 151.12, B5a out 216.19, B5b out 225.90 (before the shot change 225.933), B5c in 227.72, B6a in 217.90 / out 222.20, **B6b in 224.30 (the polish clipped the onset of "I'm") / out 228.06 (the aligner puts "with." 0.25 s late: the real end of "with" is ~227.96 and "I came out" starts 228.10; the gap is 40 ms)**, B7b in 297.74, B7c in 301.08, B8 in 84.04 (quiet gap 83.96-84.10, a -20 dB sound ends at 83.93), **B8b out 88.15 (the final /s/ of "yes." runs to 88.13 in the 3-8 kHz band; the next sound starts 88.16)**. Aligner offsets seen: Piers/Joe +0.25 s late (after 227), 1979 "Well," 0.18 s early, "Michael," 0.24 s late.
2. **Beat 7's SEQUENCE.md outs were short:** "that?" runs to 289.54 (sequence 289.34) and "family." to 302.56 (sequence 302.18, which would cut the last word). Re-timed to include them.
3. **Joe's "Well," (223.09) and the 0.9 s pause before "I'm glad" are cut** (the approved in is 224.41). Say if he wants "Well," back.
4. **B1c keeps a 0.1 s lead-in before "How"** (Whisper small.en heard "I mean,", medium.en "And"): there is no gap before "How" to cut on (the envelope runs -24 -> -15 dB without a dip). Trim 3-4 frames to drop it.
5. **Beat 2 cover = a freeze** of Michael's last frame before the special's Joe cutaway (the cutaway is 72.517-74.567 on the 60 fps grid; the interviewer's question runs under it). Remove V2 to see the special as aired.
6. **Beat 8 opens on the special's mixing-desk B-roll** (83.52-85.55, a hand on a console) under "Well, he feels that he was strict."; Michael is on camera only from 85.55 ("I'm glad he said it"). Kept as aired; the label is on from the beat start.
7. **Piers (beat 6) is a TIGHT crop (295 %, window y 140-791) to keep the black bars and the CNN lower third / bug off frame.** It is an SD source blown up 2.95x: soft. STOP 2 chooses Topaz or a blurred-fill letterbox. B6a's audio leads Piers's shot by 4 frames, so those 4 frames are a HOLD of his first frame (no flash of the previous Joe shot).
8. **Levels:** `analysis/levels.py`: kept audio of each CLIP -> -17 LUFS, capped at -1 dBFS sample peak. Film dialogue swings 8 LU inside one scene. Beat LUFS before gain: B1 -19.4, B2 -20.5, B3 -23.6 (B3a -20.1, B3b -28.4, B3c -23.0), B5 -27.6, B6 -28.8 (Piers -29.1, Joe -28.2: **+12.1 / +11.2 dB**), B7 -25.2, B8 -19.4. Capped by peak: B3a (+0.6, -19.5 LUFS after), B7a (+7.2), B7c (+5.8).
9. **Framing = one static Motion per clip** (face-centred fill-height, YuNet face centres). B5a is the one weak clip: Joe leans across the frame (face x 860 -> 1480 in 0.9 s) so the window cannot hold the face (head lock at STOP 2).
10. **Silent ASR (small.en, each span alone between 1 s of silence) reads every span as its own utterance** with no neighbour words (`raw/gapped.small.en.txt`); small.en misreads three words ("You're"->"Yeah, I'm", "paper"->"it", "whoop"->"put"), the large-model aligner has them right.
11. **Frame check (placed spans, as framed): no minors on any frame, no logos / channel bugs** (1979 "THE LAST DAYS OF MICHAEL JACKSON" + abc bugs and the CNN lower third sit outside the windows): `proof/framed_sheet_*.jpg`. Film copy is Lionsgate picture + audio (Content ID).

## Open items for Affan (also in the report)
- **Hear the Piers audio** (-28.5 LUFS, +12 dB review gain; September's Bashir notes rated Joe's 2013 Piers audio as slurred). I could not listen (silence rule); the ASR reads both lines word for word.
- **The film beats use Lionsgate audio (Content ID).**
- Nothing is captioned, graded, zoomed, SFX'd or musicked yet (STOP 2 after his review). No music bed (his job).

## Hard rules kept
Premiere only inside `premiere.lock`; a NEW sequence only (clone of "Sequence 02"); his active sequence + playhead restored and compared before/after; no save, no export; no audio/video played; no downloads; ASR = CPU small.en/medium.en under the shared `.asr-lock` (free RAM checked), never large-v3.
