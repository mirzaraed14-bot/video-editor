# moonshots-cathie-no-job: Onyx sample Short for Moonshots (Peter Diamandis) (batch 3)

## ▶ STATUS: resume here
- **2026-10-19: Affan's OWN MUSIC on both looks:** "Thelema", his file (copied to `audio/music/`, used as a voice-carved copy `*.voicecarve.wav`, -4 dB around 2.5 kHz), from 2.724 s, 14.5 LU under the voice (YT window-held, turn lift 1 dB; measured 13.8-14.5 LU under). New: yt v4 / ig ig5 (picture stream-copied from the drafts, mix-only). spec.json + build_spec.py now carry this bed (backups `*.bak-own-music`), `<look>/work/mix.wav` is the new mix (old: `mix.epidemic-bed.wav`): picture-only rebuilds keep his music. Script: `projects/_onyx-batch3-2026-10/own_music.py`.
- **2026-10-14 22:45: DRAFTS PASS, WAITING ON TOPAZ.** YT v2 (1080p base) measured: decode clean, 1442 f, captions = 132 words, caption
  line on the seam y 1092, payoff report 2.51 s before the turn / 3.29 s after → v3 merges the interview shot into the laptop shot (after-turn
  mean ≈ 3.6 s), last shot 5.33 s; Peter z0 1.35 so his "POWERED BY MOONSHOTS" shirt print sits under the captions; charts start with
  their shots; "90 PERCENT" spelled (no %); target_tp −2.0 (v1's AAC hit −1.2 dBTP). IG ig3: `ig_qa` RESULT PASS (−13.1 LUFS, −1.7 dBTP,
  132 words once, caption y 931 constant, 36 cues / 21 events, 4.4 events per 10 s, restate / slots / leaks PASS). Hook = a left-aligned
  neon in the black stage beside the host's head (the void has no bars and his close-up fills the top). Lip sync on the full file:
  Peter's close-up peaks at lag 0.000 s (r 0.26); Cathie's windows scatter −0.13…+0.20 s with no consistent side (gestures in the
  mouth box): in sync. p1 (720p caps) checked at full size in the YT frame: soft but readable, kept.
  **Topaz:** the GPU queue is slow (tftc's Topaz ran 70+ min on its first take while Affan's own Topaz app shares the 8 GB card).
  `work/topaz_guarded.sh` queues ours behind `lock.sh gpu` only when no topaz-iris.py python runs and the lock dir is absent (lock.sh's
  90-min stale takeover would otherwise start a second Topaz on a live card). When `outputs/<job>.topaz.mov` lands: full `yt_build`
  (picture re-renders with base_hq; check the log says `base: …topaz.mov`), DELETE `ig/work/window/` then `ig_build`, then QA + finals.
  Kit bug (reported, worked around): a `lower3` with `zone: "bottombar"` does not dip the credit (only the bar meter does) → lower3 in
  the top bar.
- **2026-10-14 20:15: CUT DONE, BUILDING.** Source = Affan's full file (v1b), cut to `raw/ZOhUSIaa2MA_A_0323.mkv` (t_file = t_ep − 323.533,
  Peter's close-up) + `raw/ZOhUSIaa2MA_B_0516.mkv` (t_ep − 516.1; her close-up, house wides at file 25.97-42.40 / 98.07+, Peter 84.53-88.03);
  audio xcorr 0.0 ms, frame-exact vs the full file. Framing: close-ups are tight (her face 29 % of 1080, Peter 25 %): 9:16 is fine;
  the burned-in "Build with Gemini XPRIZE" box (source y ≥ 975, bottom right) is kept out by z0 1.16 top-aligned. WhisperX large-v3 (CPU,
  the GPU queue was 40+ min) → `transcript/words.json` (fixed: "because" end 18.462 → 18.40, a phantom in the export). Cut =
  17 pinned segments, **48.07 s / 1442 f @ 30**, dead-air gate PASS, audio-qa clean, AMPLIFY_DB −2. Dropped vs the draft: "I think we're
  going to have an entrepreneurial explosion" (her early flip: without it the fear → evidence → "But this is a blessing in disguise"
  escalates), the median clause, "so you absolutely are right". Joints 60 133 194 319 369 418 680 686 752 835 916 931 959 1092 1180 1402,
  camera cuts 471 / 1132 (`work/joints.json`). Topaz (Iris 2x + FI per take) queued under `lock.sh gpu` → `outputs/<job>.topaz.mov`.
  YT: `yt/build_spec.py` (17 shots; draft picture rendered on the 1080p base); v1 = draft build queued under `lock.sh render`.
  IG: `ig/build_spec.py` (void, stack + dim, story meter, 2 chapters, compare, todo, titlecard, racked neon) + `ig/faces_clean.py`.
- **2026-10-14 11:35: BLOCKED, HANDED BACK (not done).** No source: `work/raw-orig/` empty, `youtube.BLOCKED` up since 06:25, no
  yt-dlp / ytqueue process, `ytqueue.done` unchanged since 06:24 (lock.sh fails fast while the flag exists, so the build queue never
  pulled; every batch-3 `raw-orig` is empty). Resume = the "Next when the file lands" sequence below. Open item: p1 (Pexels 7945811,
  "1080x1920") is really 720x1280: swap it or check it at full size before use. Cut draft ≈ 51 s on the CPU stamps: trim toward ≤ 48 s
  (candidates in `work/cut-draft.md`: the median clause, "the way they used to", "But you have to be realistic").
- **2026-10-14 09:12: PREP DONE, WAITING FOR THE SOURCE** (`work/raw-orig/` empty; `_onyx-batch2-2026-10/.locks/youtube.BLOCKED`
  since 06:25; the main session owns the pull, `../_onyx-batch3-2026-10/ytqueue-build.txt` line 5; this job never touches YouTube).
  Ready: GATE 5 confirmed on the BLS API (below); receipts captured + test-rendered in the YT kit (scratch `moon-b/rtest/`, sheet2.jpg:
  CS Monitor headline clipping slapping onto its page with "entry-level / jobs" highlighted · NY Fed recent-grads chart as a screen
  card with a red circle on 2022-26, where recent grads rose above all workers · a BLS line chart Jan 2024 → Aug 2026 landing on
  26.3 WEEKS); the bed (m1) downloaded + its sections measured; 4 Pexels clips (p1-p4); the cut drafted on the CPU stamps
  (`work/cut-draft.md`). Next when the file lands: normalise + A/V check per section → 1 fps sheet, scene cuts, her face size per shot
  (too wide for 9:16 → say so early) → WhisperX (GPU lock) → cuts.json → splice → Topaz FI (GPU lock) → YT build → IG build → QA → Exports.
- **2026-10-14: APPROVED by Affan** ("these are a lot better, you can start your work now"): the ★ pick of `_onyx-batch3-2026-10/PICKS.md`
  round 2, **"If you can't find a job, do this (Cathie Wood)"**, ONE clip cut once, edited TWICE (YouTube look + Instagram look). Research, the exact cut table and the sequencing:
  `../_onyx-batch3-2026-10/moonshots/research.md` § C2 / § E2. The bar: `../_onyx-batch3-2026-10/VIRAL-BAR.md`. Style upgrades for this batch:
  `../_onyx-batch3-2026-10/STYLE-RESEARCH.md` (§ F variety rule: this prospect's column). Kits upgraded 2026-10-14 (YT: DOC/marks/chart;
  IG: square/void frames, dim reveal, bar meter, ghost, chapter cards).
- Source section: pulled by the main session's YouTube queue into `work/raw-orig/` (YouTube is rate-sensitive on this IP: agents never pull).

## The plan (both looks of ONE cut)
- **Title first:** "If you can't find a job, do this". Shape: QUESTION IN THE ROOM → the answer is the lesson (Victor's shape) with a held
  belief said aloud and reversed (Vivian's). Debt: "so what do I do?". Second loop: Peter's "or your company takes off". Button: "call option".
- **Hook (Peter, the host's question first, STYLE-RESEARCH D7):** "You just graduated school. Some bet you made wiped you out. You got to
  start again. What would you do today?" (exit before "Palmer?").
- **Target 42-48 s** (a question-in-the-room scene; D8 says 32-45 s by default: the payoff needs Peter's line + her odds).
- **YT hero move (§ F, adapted):** REAL RECEIPTS (D1) instead of the provisional "archival clips": the topic is a jobs market with public
  data, so the receipts are a dated jobs-data CHART (BLS duration of unemployment) + a headline on entry-level hiring (DOC + highlighter) +
  the NY Fed recent-grads page. Signature device: annotation mark(s) on a receipt (D2) + ONE story fx only if the words describe one.
- **IG (§ F):** frame `void` if the stage is dark, else `square` (the Moonshots LIVE stage has a lit purple LED wall: likely `square`);
  captions `stack` + `reveal: "dim"` + `hero_gap: 4.0`; hero card: a story meter in the bottom bar or a 90/10 card (decided on the cut:
  a single-fill meter reading "90 then 10" would mislead, so the 90/10 goes on a `compare` / `neon` if the meter has no honest number).
- **Accent (IG):** `#E3E50A`, the yellow of "LIVE" in the show's MOONSHOTS / LIVE stage logo (median RGB 227, 229, 10 sampled on the named
  Short `czkVVwV0Ucw` frame 12 s); moonshots.com uses `#FDEA00`. A LIGHT accent: chapter cards go deep-tone (kit rule).
- **Watermark (YT):** "MOONSHOTS" (the show's name only, README § 6).
- **Closest batch-2 sample:** Victor Antonio (same question-in-the-room shape). Measurable targets: real inserts > his 6 of 22; mean shot
  after the turn ≥ 3.5 s (his 1.99 s); a held last face ≥ 3 s (his 0.60 s).

## GATE 5 (on screen)
- Cathie Wood = **Founder, CEO & CIO, ARK Invest** (the show's notes; research § C2). Peter Diamandis = Moonshots host (show name only on YT).
- "Average unemployment six months, median three months" = HER line (about people coming out of school). **CONFIRMED on the BLS's own
  API (d1b, CPS, seasonally adjusted, ALL unemployed):** LNS13008275 average weeks unemployed **Aug 2026 = 26.3** (≈ 6.1 months; Jan 2024
  20.9 → Aug 2026 26.3; Sep 2026 = 24.8, released Oct 2), LNS13008276 median **Aug 2026 = 11.4** (≈ 2.6 months; Sep 2026 = 11.5). Oct 2025 has no
  value (the shutdown). Aug 2026 = the latest release when she spoke (2026-09-25). They round to her 6 / 3, so a chart may print them,
  labelled "ALL UNEMPLOYED · BLS" with the month (it is not a graduates-only statistic). FRED's fredgraph.csv timed out (d1/d2 not used).
- Recent graduates (22-27) vs all workers: NY Fed "Unemployment Rates for Recent College Graduates versus Other Groups", latest release
  Aug 6, 2026 (2026:Q2): recent grads ≈ 5.6 % (page highlights). CS Monitor (Jul 29 2026, Laurent Belsie): "by this past March, joblessness
  for this group stood at 5.6%, compared with 4.2% for all workers, according to… the Federal Reserve Bank of New York."
- "90 % of all startups fail, 10 % succeed" = HER claim: in quotes / attributed, never sourced to anyone else.
- "Call option" translated honestly: a small bet with a big upside (NOT "a free shot": the bet is not free).
- No "$0", no "no network" (Peter's "you didn't have your network" is not in the cut).

## Download log (batch approval 2026-10-14)
| # | File | Source | Size | Why |
|---|---|---|---|---|
| v1 | `work/raw-orig/ZOhUSIaa2MA_<section>.mkv` | https://www.youtube.com/watch?v=ZOhUSIaa2MA sections *0:05:35-0:06:05 + *0:08:45-0:10:25 (yt-dlp, best ≤ 2160p + audio) | SUPERSEDED: YouTube stayed bot-blocked; see v1b | the source of the cut (Peter's question 5:45 + her answer 8:54-10:16) |
| v1b | `work/raw-orig/ZOhUSIaa2MA_full.mp4` | Affan's own download of the WHOLE video, handed over 2026-10-14 evening (`E:\Bullshit Folder\Henry\We Gave $2M To The AI Startup That Could Help The Most People _ MOONSHOTS Live.mp4`, copied, original untouched); 1080p H.264, the YouTube timeline | 267 MB | the source of the cut (cut your section from it) |
| d1 | `work/receipts/fred-UEMPMEAN.csv` | https://fred.stlouisfed.org/graph/fredgraph.csv?id=UEMPMEAN (BLS CPS, average weeks unemployed, monthly; text) | ~10 KB | GATE 5 + the CHART data |
| d2 | `work/receipts/fred-UEMPMED.csv` | https://fred.stlouisfed.org/graph/fredgraph.csv?id=UEMPMED (BLS CPS, median weeks unemployed, monthly; text) | ~10 KB | GATE 5 + the CHART data |
| d1b | `work/receipts/bls-LNS13008275.json`, `bls-LNS13008276.json` | https://api.bls.gov/publicAPI/v1/timeseries/data/LNS13008275 and …/LNS13008276 (the BLS's own public API: the CPS series behind UEMPMEAN / UEMPMED; d1/d2 timed out on fredgraph.csv) | ~5-10 KB each | GATE 5 + the CHART data |
| d3 | `yt/assets/broll/r-csmonitor-entry-level.png` (+ `r-csmonitor-full.png`, the same page as a --full still for the byline/date) | page still (workflows/page-record.mjs --full, headless, no login) of https://www.csmonitor.com/Business/2026/0729/unemployment-youth-jobs-work-economy ("College grads face a global squeeze on entry-level jobs", Jul 29 2026) | ~2-8 MB | DOC receipt: "entry-level jobs are not filling up" |
| d4 | `yt/assets/broll/r-nyfed-college-labor.png` | page still (page-record.mjs --full) of https://www.newyorkfed.org/research/college-labor-market (2026:Q2 highlights: recent grads' unemployment ≈ 5.6 %) | ~2-8 MB | DOC receipt: "people coming out of school are unemployed" |
| d5 | `yt/assets/broll/r-carta-solo-founders.png` | page still (page-record.mjs --full) of https://carta.com/data/solo-founders-report/ (solo-founder share of new startups 23.7 % in 2019 → 36.3 % in H1 2025) | BLOCKED: a Cloudflare "verify you are human" page (no bypass; capture deleted, not used) | — |
| d6 | `work/receipts/moonshots-hl-cathie-wood.jpg` | https://moonshots.com/assets/hl-cathie-wood.jpg (the show's own event site, her highlight still from Moonshots LIVE) | ~0.1-1 MB | preview of her stage framing while YouTube is blocked; possible IG ghost / reference |
| d7 | `yt/assets/broll/r-axios-bloodbath.png` | page still (page-record.mjs, headless, no login) of https://www.axios.com/2025/05/28/ai-jobs-white-collar-unemployment-anthropic ("Behind the Curtain: A white-collar bloodbath", May 28 2025: AI could wipe out half of entry-level white-collar jobs, per Anthropic's CEO) | BLOCKED: Cloudflare "verify you are human" (no bypass; capture deleted, not used) | — |
| m1 | `audio/music/ES_All Gas, No Breaks (Instrumental Version) - Nbhd Nick.wav` | Epidemic Sound recording 4f2a02ae-b43e-41ba-a597-d0296cf75d82 "All Gas, No Breaks (Instrumental Version)", Nbhd Nick (trap beats; epic, hopeful; 146 bpm; 3:45), `mcp__epidemic-sound__DownloadRecording` WAV FULL | ~40-60 MB | the bed for both looks (drive + groove, Affan's 2026-10-14 swaps were drum-led instrumentals; not used in batch 2 or by another batch-3 job at the time of logging) |
| p0 | `work/pexels/thumbs/<id>.jpg` + `work/pexels/<query>.json` | Pexels search-result pages (www.pexels.com/search/videos) and their preview thumbnails (images.pexels.com, `w=500`), ≤ 12 per query: graduation caps · laptop at night · job interview · rejection email · rocket launch · lightbulbs | ~40-80 KB each, ≤ 100 files | B-roll selection only |
| p1 | `yt/assets/broll/p1-graduates-throw-caps.mp4` | Pexels (free licence): https://www.pexels.com/video/graduates-throwing-academic-cap-on-air-7945811/ → https://videos.pexels.com/video-files/7945811/7945811-hd_1080_1920_25fps.mp4 (native vertical 1080) | ~10-30 MB | "You just graduated school" |
| p2 | `yt/assets/broll/p2-interview-handshake.mp4` | Pexels: https://www.pexels.com/video/interviewer-shaking-hands-with-an-applicant-5438947/ → https://videos.pexels.com/video-files/5438947/5438947-uhd_2160_3840_25fps.mp4 | ~30-90 MB | "and keep interviewing" |
| p3 | `yt/assets/broll/p3-interview-office.mp4` | Pexels: https://www.pexels.com/video/man-and-woman-shaking-hands-in-office-12893616/ → https://videos.pexels.com/video-files/12893616/12893616-uhd_2160_3840_24fps.mp4 | ~30-90 MB | alternate for p2 |
| p4 | `yt/assets/broll/p4-founder-laptop-night.mp4` | Pexels: https://www.pexels.com/video/a-man-working-hard-at-home-5197243/ → https://videos.pexels.com/video-files/5197243/5197243-uhd_3840_2160_25fps.mp4 | ~30-90 MB | "start your own company with AI and no employees" (a company of one, at night) |
| p0b | `work/pexels/prev/<id>.mp4` | Pexels 640x360 preview files (videos.pexels.com) of 6 "stock market screen" candidates (38557069, 38859052, 39589976, 38736271, 38736274, 38168755): the search thumbnails now answer "Source is unreachable" | ~1-3 MB each | B-roll selection only ("some bet you made wiped you out") |
| p5 | `yt/assets/broll/p5-red-market-screen.mp4` | Pexels: https://www.pexels.com/video/dynamic-stock-market-analysis-in-dark-room-38859052/ → https://videos.pexels.com/video-files/38859052/16518461_3840_2160_50fps.mp4 | ~30-120 MB | "some bet you made wiped you out" (a market screen in the red) |
| p* | `yt/assets/broll/<id>-<noun>.mp4` | Pexels (free licence) clips, one row each added BEFORE its pull | | literal nouns only (caps and gowns, a laptop at night, an interview) |
