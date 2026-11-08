# RUN: mj-victory-tour (AW Short, "Why Michael Jackson Gave Away $5 MILLION 💔")

## ▶ STATUS: resume here
**2026-11-08 ~19:50: SEQUENCE COMPLETE FOR REVIEW: beats 1-6 + both placeholder cards, 35.53 s, read back, STOPPED for Affan's creative direction.** Nothing saved, nothing exported, nothing committed. His active sequence (`MJ Showed His Mother - raw cut`) restored after every window. No music, no graphics beyond the two plain placeholder cards, no captions, SFX or CTA.
- Sequence: `Why MJ Gave Away 5 Million - raw cut` (bin `MJ Victory Tour`, ABW10.prproj, unsaved), 1080x1920 **30 fps**: V1/A1 17 clips butt-joined (razor stub at 12.60), V2 1 picture-only cover (beat 4, Michael centred), V3 2 text cards, 6 markers (card/caption notes in the comments). Read-back = `premiere/readback.tsv`: times and in-points equal the plan (in-points on the 1/30 grid, up to 27 ms early on the 50 fps source), A1 empty 22.77-24.77, A2-A4 empty.
- Audio proof (`win/asr_readback.py`, A1 rebuilt from the read-back): B1, B3 = table; B2 = table (ASR "turntour" for "current tour"); B5 = the real words; B6 = "I'd like to say this is our last and final tour and I think this is our farewell tour."; B4 "Thank you." is Whisper hallucinating on digital silence in the rebuilt wav (no audio in the sequence there).
- Beat 6 history: the Dodger download was refused 17:01 by the shared flag (no request sent), the flag was cleared by the parent session at 19:26 after one metadata probe, then ONE file downloaded through `lock.sh youtube` (no bot check). The dl.log line "STOPPED" at 19:27 is a stale grep hit on the appended earlier log, not a block.
- Transcribed alone in `scratch-dodger/` and merged into `transcript/words.json` (backup `words.json.before-dodger`); beats 1-5 EDL and placement rows verified IDENTICAL to what was in Premiere before beat 6 was appended.
- Rebuild from scratch: `premiere/run_window.py` (beats 1-5 + cards) then `premiere/run_append.py` (beat 6), after deleting the sequence by hand (run_window refuses if the name exists).
- Dialog watcher (still running, owned by this session, left up for the Bieber builder: stop it only if nobody else needs it): started 17:15 (log `logs/dialog-watch.out`); a `Link Media` dialog was already open in Premiere before my first window (lock free, not mine), left open for him.

## Sequence plan (beats, real in/outs)
| Beat | tl | Source | Source in-out | Words (heard) |
|---|---|---|---|---|
| 1 | 0.00-6.63 | `report` (83mtSOK4heY) | 6.167-9.467 + 10.067-13.400 | "putting the $120 price tag out of reach of many people. There were charges of greed leveled at the Jacksons and their entourage." |
| 2 | 6.63-17.30 | `press` (dCL3xxZDUu4), last take | 89.167-92.600, 93.067-95.767, 96.367-99.633, 100.300-101.567 | "The other day I got a letter from a fan in Texas named LaDonna Jones. She'd been saving her money from odd jobs to buy tickets, but with the current tour system, she'd have to buy four tickets, and she couldn't afford that." |
| 3 | 17.30-22.77 | `press` | 123.600-124.633, 124.900-127.133, 127.367-128.900, 129.200-129.867 | "I want you to know that I've decided to donate all my money I make from the performance to charity." Card 1 on V3 19.77-22.77 |
| 4 | 22.77-24.77 | picture only: `brothers` 60.4-62.4 (V2) | | silent. Card 2 on V3 22.77-24.77 |
| 5 | 24.77-30.57 | `brothers` (g32yuPdw03w) | 100.300-103.333, 109.667-112.433 | "Everybody's writing saying that it's Michael leaving the Jacksons ... Michael would never leave, because we're blood. We're family." |
| 6 | 30.57-35.53 | `dodger` (olrx34snPI4) | 46.68-47.55, 48.52-50.75, 51.76-52.13, 54.56-56.06 | "I'd like to say this is our last and final tour. And I think this is our farewell tour." HARD CUT |

## Sources (kept as downloaded in `src/`; Premiere-safe re-encodes in `h264/`, same timeline)
| Beat | Key | File | Spec | Note |
|---|---|---|---|---|
| 1 | `report` | `src/83mtSOK4heY.mp4` (MJ 80s Archive, 45 s, uploaded 2026-08-03) | 1440x1080 H.264 30 fps (the best H.264 offered; no larger format exists) | no network logo; baked 16:9 letterbox (content 1440x808); uploader watermark "M380sArchive©" bottom-right |
| 2-3 | `press` | `src/dCL3xxZDUu4.mp4` ("The Jacksons - Victory Tour Press conference (July 5, 1984)", MJ Live & Rare Videos, 176 s) | 1440x1080 H.264 30 fps (best offered) | from 121.13 s a second camera with a faint "gettyimages" watermark + clip id "1B011428_004" bottom-left (all of beat 3) |
| 4-5 | `brothers` | `src/g32yuPdw03w.mp4` ("The Jacksons Discuss Michael Jackson's Solo Success & Victory Tour", MJ 80s Archive, 166 s) | 1472x1080 H.264 30 fps (best offered), VHS tracking tears, baked border 56/32 px | lower third MARLON \| RANDY \| JACKIE at ~36-40 s; the same report is narrated 1984 ("awaiting release of their new album, Victory ... tour this summer") |
| 6 | `dodger` | `src/olrx34snPI4.mp4` (TRUQue TV, 92 s) | 1920x1046 H.264 50 fps (best H.264 offered), baked border ~10 px top/bottom | one continuous wide stage shot over 44-60 s; crowd noise ~8 dB under his voice |
No AV1/VP9 was kept; the 1440x1080/1472x1080 H.264 are the top format YouTube lists for these uploads (info.json read: AV1/VP9 stop at the same 1080p). The yt-dlp mp4s were re-encoded before import (the sibling's File Import Failure kills the bridge): no import failure occurred.

## Download timing (disclosure)
`g32yuPdw03w` (brothers) was requested at 16:59:37, after the Bieber session's bot check at 16:59 and before the flag existed on disk; it completed normally. The fourth id was then refused by `lock.sh` (exit 75) with no request sent.

## Local drives checked first (E:\Bullshit Folder)
No Victory Tour / Dodger / 1984 footage. The only candidate by name, `Henry/Michael Jackson _ The Jacksons _ 60fps.mp4` (1080p60, 17 min), is the 2001 Madison Square Garden 30th-anniversary concert (`proof/local60/sheet.jpg`): not usable. No sibling job holds the Dodger farewell either.

## Frame checks (the ACTUAL 9:16 crops at 3 fps, `proof/crops_a_0.jpg`, `proof/crops_a_1.jpg`; `win/cropsheet.py`)
No minors in any placed span (ticket hands and the arrival crowd are adults; podium and brothers are adults; beat 4 picture is Michael and a brother). Ladonna Jones: name only, no picture. The wider source frames show other bystanders, so any pan or reframe of beat 1 needs a fresh check.

## Hard rules
No picture of Ladonna Jones, no minors on frame, no card claiming "the brothers didn't know", no music, silence, premiere.lock per window, new sequence only, no save, no export.
