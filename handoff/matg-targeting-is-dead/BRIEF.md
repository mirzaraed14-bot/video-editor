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
| m1 | `yt/assets/audio/ES_Out There - Out To The World.wav` (+ its DRUMS stem, to subtract for a drumless bed) | Epidemic Sound recording a227905b-d133-4d32-92c3-ce285bc0b1f8 "Out There", Out To The World (dark ambient, suspense, pulses, 99 bpm, 2:47), `mcp__epidemic-sound__DownloadRecording` WAV FULL + DRUMS; not used by any earlier sample (grep of every BRIEF/spec 2026-10-22) | ≈ 30 + 30 MB | the bed (13.5 LU under the voice) |
| x1-x15 | `yt/assets/sfx/<name>.wav` | Epidemic Sound SFX, `DownloadSoundEffect` WAV, none used before in this repo (grep 2026-10-22): 073cf199 Whoosh Soft Airy · fe174b5e Whoosh Airy Tonal Cinematic 01 · 87214551 Whoosh Airy Medium Ghost Tonal · 89724499 Whoosh Airy Clean Short Crisp · 240e5b47 Boom Cinematic Hit Low · 41839644 Boom Cinematic Big Deep Reverberant · 2f0a40ab Boom Cinematic Deep Impact · d0ba83c3 Impact Low Deep Thuds · 6d82b75c Boom Low Hit · 3a908c02 Shutter Release Nikon F4 02 · c65951a5 Shutter Release Nikon F4 01 · 3e3e1af7 Paper Thick Turn Page · a836c16e Marker Writing Circle · da68334f Riser Reverse Build Up Tonal 01 · e73cb6c2 Trailer Swell Reverse 01 | ≈ 0.2-2 MB each | a fresh, varied set: every graphic gets its own sound |
| r1 | `yt/assets/broll/doc-im8-home.png` | https://im8health.com/ (IM8's own homepage, "co-founded with David Beckham"), `workflows/page-record.mjs` still, no login | ≈ 2-8 MB | the hook's receipt: whose ad account this is |
| r2 | `yt/assets/broll/doc-prenetics-q2.png` | Prenetics' own news release "Prenetics Announces Second Quarter 2025 Financial Results with IM8 on Track to Achieve $100M Annual Recurring Revenue by Year's End" (2025-09-12; prenetics.gcs-web.com / SEC EX-99.1), page-record still | ≈ 2-8 MB | "Q2, we spent $33 million…": the public Q2 report he cites (highlight = the headline only; the $ numbers stay his) |
| r3 | `yt/assets/broll/doc-sabalenka-im8.png` | Prenetics news release 2025-06-26 "World No. 1 Tennis Star Aryna Sabalenka Joins Prenetics' IM8 Health as Global Ambassador and Shareholder" (prenetics.gcs-web.com) and/or Sports Illustrated "Aryna Sabalenka Adds Her Muscle to IM8 as Ambassador & Shareholder" (si.com), page-record stills | ≈ 2-8 MB | "let's say Aryna, world number one tennis player" |
| r4 | `yt/assets/broll/doc-ads-manager-audience.png` | Jon Loomer, "Advantage+ Audience vs. Original Audiences" (jonloomer.com): his screenshots of Meta Ads Manager's audience controls (Age 18-65+, Gender), page-record still | ≈ 2-8 MB | "we don't have to target men and women, 18 to 65" (a red box on the age row) |
| r5 | `yt/assets/broll/doc-im8-ads-*.png` | ConvertFlow, "The $120M Meta Ads Strategy IM8 Uses" (convertflow.com/blog/im8-meta-ads-strategy): its screenshots of IM8's real Meta ads, page-record still (crops) | ≈ 2-8 MB | "you let your creatives do the targeting": the real creatives |
