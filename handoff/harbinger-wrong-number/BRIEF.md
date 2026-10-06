# harbinger-wrong-number: Onyx sample Short for The Jordan Harbinger Show (guest Sean Wiswesser, ex-CIA)

## ▶ STATUS: resume here
- **2026-10-06 (later): FINAL = v6** — the lip-line captions now MOVE ON THE CUT: a chunk on screen across a cut takes each shot's own height (before, it kept one shot's height and sat on the other shot's mouth for a few frames; found by Pomp's r3 QA), and a chunk that would appear 1-2 frames before a cut appears on it. Kit `ig_capy.py` (moves/show/hide) + `ig_overlay.py`. Picture and sound untouched (audio null -91 dB vs the previous final), clean decode; final + ~/Downloads replaced.
- **2026-10-06: FINAL = v5, CAPTIONS MOVED UP UNDER THE LIPS** (Affan's review: "the distance between the captions and the lips needs to be shorter"). `kit/ig_capy.py` places every chunk just below the speaker's lower lip, per shot (per-shot lip line); picture, cards and sound unchanged from the earlier final. Clean decode, audio = picture; `outputs/harbinger-wrong-number.final.mp4` + ~/Downloads replaced.
- **2026-10-06: FINAL = v4** (`outputs/harbinger-wrong-number.final.mp4`, copy in ~/Downloads). 3 QA rounds (r1 joints/pan/lip + highlight kit bug; r2 Jordan cutaway, flag, aerial; r3 merged hook shot, aerial shade, ticks), r3 fixes verified on frames (49 cues, -13.0 LUFS / -1.8 dBTP, 47.1 s audio = picture, clean decode). Next: Affan's review, reaction video, delivery email draft (Affan sends).
- 2026-10-06: job opened (batch 1, `projects/_onyx-batch-2026-10/BATCH.md`). Research: `projects/_onyx-batch-2026-10/harbinger/research.md`.
- **Platform:** INSTAGRAM (@jordanharbinger: 993K followers, median 85.6K, paused since 16 Aug; YouTube Shorts: 0 in 60 days, 2 in 12 months at 1.7K/2.9K).
- **Moment (Claude's pick, batch mode):** The wrong-number call (`JC-tO9ZV-A0`): a US agent dials the Russian illegals' house by mistake, "can we go secure?"; the wife pauses, "I think you have the wrong number", hangs up; they never reported it: "They just want to live here." Set-up: Jordan's question about The Americans ("this kind of thing is real"). Names/code names stay OFF screen (garbled in the telling). Instagram freshness: unchecked.
- 2026-10-06: sections pulled and normalised to a common time zero (audio padded; downloads kept in work/raw-orig/), transcribed.
- 2026-10-06: Instagram study: @jordanharbinger's house style = a WHITE title box with black bold text in the top band, bold ALL-CAPS captions with one key word in green, the show's purple branding. Plan: title box "A US agent called / Russian spies by mistake", caps captions with green key words, Jordan for the set-up, Sean full or cropped inside his two-up box (the box spans x 994-1806, y 290-952 on the base: crops stay inside it), ONE full-screen graphic (the phone sheet: field office and residence rows side by side, made-up 555 numbers, no names), a call card "Field office · calling…" (what he thought he dialed), "Call ended". Source is 1080p webcam: Topaz Iris 2x (no stab) → outputs/harbinger-wrong-number.topaz.mov. Credit: "The Jordan Harbinger Show · Sean Wiswesser, ex-CIA".
- **rough cut DONE 47.1 s (outputs/harbinger-wrong-number.mp4; 24 segments; both reviews applied: 'What exactly is a Russian illegal?' and 'That's treason.' added, five mid-phrase holes closed, three stacked 'she's like' lines cut, eight boundary fixes). Next: style study → ig/spec.json → build → QA.**

## Download log (every file logged BEFORE it is pulled)
| # | File | Source URL | Section | Approx size | Status |
|---|---|---|---|---|---|
| r1 | `raw/JC-tO9ZV-A0_010418-010452.mkv` (best video ≤2160p + the original English audio) | https://www.youtube.com/watch?v=JC-tO9ZV-A0 | 1:04:18–1:04:52 (0.6 min) | ~20–60 MB | done 2026-10-06 (5 MB, 1920,1080,30/1, audio ?) |
| r2 | `raw/JC-tO9ZV-A0_011450-011848.mkv` (best video ≤2160p + the original English audio) | https://www.youtube.com/watch?v=JC-tO9ZV-A0 | 1:14:50–1:18:48 (4.0 min) | ~120–350 MB | done 2026-10-06 (42 MB, 1920,1080,30/1, audio ?) |
| b01 | `ig/assets/broll/b01-aerial-suburb.mp4` (Pexels, free licence) | https://www.pexels.com/video/31965012/ → https://videos.pexels.com/video-files/31965012/13620397_1080_1920_30fps.mp4 | whole clip (aerial suburban street: "they pretend to be American, kids and everything") | ~5–30 MB | done 2026-10-06 (8 MB, 1080,1920,30000/1001
 8.241567
) |
| b02 | `ig/assets/broll/b02-dialing-phone.mp4` (Pexels, free licence) | https://www.pexels.com/video/34835424/ → https://videos.pexels.com/video-files/34835424/14766099_1080_1920_30fps.mp4 | whole clip (a hand dialing an old phone: "He dialed the actual number") | ~5–30 MB | done 2026-10-06 (4 MB, 1080,1920,30/1
 6.933333
) |
| b03 | `ig/assets/broll/b03-woman-answers.mp4` (Pexels, free licence) | https://www.pexels.com/video/7119838/ → https://videos.pexels.com/video-files/7119838/7119838-hd_1080_2048_25fps.mp4 | whole clip (a woman answering a landline: "picks up the phone") | ~5–30 MB | done 2026-10-06 (10 MB, 1080,2048,25/1
| b04 | `ig/assets/broll/b04-suburb-spring.mp4` (Pexels, free licence) | https://www.pexels.com/video/36094983/ → https://videos.pexels.com/video-files/36094983/15307624_1080_1920_30fps.mp4 | whole clip (aerial suburban neighborhood: replaces b01, which read as an Australian street and carried a readable wordmark on a hoarding; QA r2) | ~5–20 MB | done 2026-10-06 (36 MB, 1080,1920,30/1
 20.333333
) |
| m1 | `ig/assets/audio/ES_Unfinished Stories - Lennon Hutton.wav` (music bed, WAV full mix) | Epidemic Sound recording 1419406f-2b2b-42cc-a51c-2d85994050dd ("Unfinished Stories", Lennon Hutton; ambient, mysterious, pulses, suspense; 65 bpm; 3:55) | whole track | ~40 MB | done 2026-10-06 (65 MB) |
 29.600000
) |
