# matg-targeting-is-dead: Onyx sample Short for Marketing Against the Grain (Kipp Bodnar, Kieran Flanagan) (batch 4)

## ▶ STATUS: resume here
- **2026-10-22 12:30: INTAKE DONE, TRANSCRIBING, RECEIPTS IN PROGRESS.** Source copied (original untouched) to
  `work/raw-orig/fIgLRgCC30s_full.mp4`; section `raw/fIgLRgCC30s_A.mkv` = episode 40.500 → 611.458 s (keyframe stream copy, audio FLAC
  from 0): **section t = episode t − 40.5**, checked: section frame 240 == episode 50.5 s (PSNR inf), audio xcorr offset 0.0 ms.
  WhisperX large-v3 running under `lock.sh gpu` (`work/transcribe.log`). YouTube look only today (Affan, 2026-10-22).
- Next: cut plan from the word-level transcript → polish-boundaries → splice → Topaz (background, GPU lock) → faces → spec → build → QA → final.

## The job
- Approved pick (Affan 2026-10-19/20, line by line): `projects/_onyx-batch4-2026-10/SEQUENCING.md` § 2 ★ A, "Why Beckham's $400K-a-day
  ad account doesn't use targeting". 9 lines, in order; trimming inside lines only. Guest Danny Yeung (co-founder, IM8, with David Beckham;
  CEO of Prenetics). Hosts Kieran Flanagan (glasses, painting behind) and Kipp Bodnar (white room, wooden beams). Remote recording: full-frame
  singles, a two-up and a three-up layout.
- Look: `presets/youtube-shorts/onyx-samples-youtube/` (Sean Ryan look) + README § 13 devices. Template: `projects/tftc-hospital-bill/`.
- Deliver: `outputs/matg-targeting-is-dead.sample-yt.final.mp4` + `X:\Claude Projects\Exports\matg-targeting-is-dead.yt.final.mp4` (MP4 H.264).

## GATE 5 (facts on screen)
- "Aryna" (the audio says "let's say Arena… world number one tennis player"): IM8's own parent announced on 2025-06-26 "World No. 1 Tennis
  Star Aryna Sabalenka Joins Prenetics' IM8 Health as Global Ambassador and Shareholder" (prenetics.gcs-web.com news release; also SI,
  Athletech News). Confirmed against the audio below before her name goes on screen.
- CAC numbers ($305 → $301 → $239) are DANNY'S SPOKEN NUMBERS. The Prenetics Q2 2025 release (SEC EX-99.1, 2025-09-12) does NOT print them
  (it prints a first-half CAC of $104): so the chart's source line credits Danny on the show, never the filing. CAC = "cost per customer".
- "$300,000-400,000 a day" = Kieran quoting what Danny told them off camera (spoken only / as said).

## Download log
| # | File | Source | Size | Why |
|---|---|---|---|---|
| v1 | `work/raw-orig/fIgLRgCC30s_full.mp4` | Affan's own download of the whole episode (`E:\Bullshit Folder\Henry\How-I-Grew-SnapYT.App.mp4`, copied, original untouched); YouTube fIgLRgCC30s, 1920x1080 24 fps, 31:25 | 365.5 MB | the source |
| v2 | `raw/fIgLRgCC30s_A.mkv` | LOCAL derivative of v1: stream copy 40.500 → 611.458 s | ≈ 115 MB | the raw clip the EDL cuts from |
