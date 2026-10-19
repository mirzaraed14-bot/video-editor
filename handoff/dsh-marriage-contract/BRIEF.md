# dsh-marriage-contract: Onyx sample Short for Digital Social Hour (Sean Kelly) (batch 3)

## ▶ STATUS: resume here
- **21:20: TOPAZ STOPPED (unresolved).** Iris 2x + FI took 28 min for segment 0 alone (89 of 1353 frames): the GPU is pinned at 100 % /
  7.9 GB by a WhisperX run of another session OUTSIDE the lock (`cbum-last-show`, pid 130275, since 19:01), so the whole base would take
  ~7 h and hold the GPU lock from five other agents. Both looks are built on the 1080 base (`base_hq` points at
  `outputs/dsh-marriage-contract.topaz-ok.mov`, absent). TO FINISH TOPAZ LATER: `bash projects/_onyx-batch2-2026-10/lock.sh gpu python
  workflows/topaz-iris.py projects/dsh-marriage-contract/outputs/dsh-marriage-contract.mp4 projects/dsh-marriage-contract/outputs/dsh-marriage-contract.topaz.mov
  --out-scale 2 --no-stab --segments 0,89,138,332,382,441,490,526,614,737,776,966,1067,1240,1253,1313`, check 1353 frames, rename to
  `.topaz-ok.mov`, then rebuild the pictures only (`yt_build.py … --skip overlay,mix`; `ig_build.py … --skip overlay,mix`) and re-export.
- **2026-10-14 20:25: CUT DONE, BUILDS QUEUED.** Source = Affan's full download (v1b); section `work/raw-orig/hsJ05oQk2Ag_section-47.88.mkv`
  (stream copy from the keyframe at 47.881167 s; container t = YouTube t − 47.810, A/V verified against the full file) → `raw/hsJ05oQk2Ag_section.mkv`
  (audio first_pts 0). Podcast clock = file t + 78.936 (cross-correlated, r 0.95-0.96 at 4 points). Transcribed ONCE on CPU (the GPU was
  saturated by an unlocked `cbum-last-show` WhisperX run + the queue). Speakers verified by wespeaker (Greg 0.69-0.85, Dave 0.72-0.85).
  **The cut: 45.15 s, 14 segments, 1353 f @ 29.97** (`work/cut/make_cuts.py`, pinned grafts measured on the video's own envelope +
  centroid; `transcript/words.json` edges fixed for the phantom "so" / "marriage," / the long "institution."); dropped vs the dry run:
  Greg's hesitation "Right? I—" before "I actually am pro-marriage" (the joint is hidden by a layout change); dead-air-qa PASS;
  audio-qa flags one joint "click" at 16.35 s = the sibilant end of "continues" next to a quiet onset (diffs = the hiss's own, raw max 0.16
  vs joint 0.12): a detector false positive, kept. Camera map: `work/cut/cutmap.py`.
  Specs written: `yt/build_spec.py` (17 shots, B/DOC/FIT 51 %, SPLIT 25 %, A 24 %; real inserts: the room x2, Census DOC, Maynard DOC,
  his book; stock: trap, bride, ring, divorce papers, judge) and `ig/build_spec.py` (square, word wide, seam 640 = the caption line,
  the hook split above the burned-in prompt, 9 cards, gates clean). Topaz (Iris 2x + FI, `--segments` at every joint and camera cut) queued
  on the GPU lock; YT v1 draft queued on the render lock (picture on the 1080 base until Topaz lands; then rebuild with `base_hq`).
- **2026-10-14 10:22: BLOCKED, NOT DONE: prep complete, waiting on `work/raw-orig/`** (YouTube `youtube.BLOCKED` since 06:25; no batch-3 job
  has its source). Handed back to the main session with this state. **RESUME, in order:** (1) intake: `ffprobe` start times, normalise
  time zero (`-af aresample=async=1:first_pts=0`, the download kept in `work/raw-orig/`), mouth-vs-voice check; (2) cross-correlate the
  video's audio with the podcast MP3 (scout clock = podcast − 110; expected file t = podcast − 86.3) and copy the dry-run cut below onto
  the file clock; (3) `transcribe.sh` (GPU lock; no HF token → no `--diarize`: speakers by `scratch dsh/tools/spk.py` wespeaker, refs
  in `scratch dsh/refs_pod.json`); (4) re-measure on the VIDEO audio: the three graft dips, the button end (fricative vs breath 288.43-288.52),
  "Here's"/"It's", spoken "gonna"; split the pauses polish missed (after "lose" ≈0.8 s, after "wife" ≈0.9 s, before "I actually" ≈1.4 s);
  fix phantom words in `words.json` (the grafts sit inside "so" and "marriage,": correct both edges, else captions show "so marriage" /
  "marriage marriage"); `dead-air-qa.py`; (5) layout scan (camera cuts, two-up, chyrons) → face keys; (6) splice → Topaz FI (GPU lock) →
  `yt/build_spec.py` → `ig/build_spec.py` → QA → Exports.
- **Tested on scratch (10:20):** DOC receipts render readable: Census front = `doc-census-p4.png` crop `[0.0745, 0.7298, 0.345, 0.8472]`
  (6 lines, ≈ 55 px type), w 860, push 0.05, highlights `[t, 0.0866, 0.7657, 0.2258, 0.0141]` ("$19.2 billion. Custodial mothers") and
  `[t, 0.0866, 0.7815, 0.1509, 0.0141]` ("received $16.2 billion"), back = `doc-census-cover.png`; Maynard front = `doc-maynard-quote.png`
  crop `[0.0595, 0.3533, 0.9405, 0.4567]`, w 860, push 0.03, **focus [0.5, 0.42]** (the default focus on the right-hand highlight pushed the
  card's left edge out of frame), highlights `[t, 0.675, 0.408, 0.2268, 0.0193]` ("the law steps in") + `[t, 0.0732, 0.432, 0.8196, 0.0193]`,
  back = `doc-maynard-top.png` (scratch `dsh/doctest/yt/work/doc-sheet3.jpg`). IG chapter card: flat `#3DB8FC` under white captions is
  2.2:1 → `bg` `#0A2A40` + `color` `#3DB8FC` (white 14.8:1, accent 6.7:1). Bed: `yt_mix` holds the bed per 3 s window, so either start
  `bed_in` in the loud body (≥ 14.5 s) or land the track's 98-112 s break on the turn on purpose (bed_in ≈ 98 − turn_t) and check the curve.
- **2026-10-14 ≈08:40: PREP DONE, WAITING FOR THE SOURCE** (`work/raw-orig/` empty; YouTube `youtube.BLOCKED` since 06:25, the main session
  owns the pull: `../_onyx-batch3-2026-10/ytqueue-build.txt` line 3). Done: GATE 5 (below), the two DOC receipts captured, accent sampled,
  bed downloaded, both storyboards drafted (below, timings estimated from the podcast reading). Next when the file lands: normalise time
  zero + picture/sound check → layout scan (camera cuts, two-up spans, burned-in chyrons) → `transcribe.sh --diarize` (GPU lock) →
  speaker check (embedding) → cuts.json → splice (`AMPLIFY_DB=-2`) → Topaz FI (GPU lock) → YT build → IG build → QA → Exports.
- **09:55: still waiting (YouTube block since 06:25).** Since 08:40: B-roll b01-b08 in `yt/assets/broll/` (gavel, judge, ring exchange,
  divorce papers + ring, bride walking the aisle, a mousetrap still); a SCOUT WhisperX transcript of the podcast audio (scratch
  `dsh/podscout/`, podcast clock − 110 s: NOT the canonical, that comes from the video) gives the draft cut ≈ 44 s: Greg's prompt ·
  Dave "When you use the word trap … at that point?" · Greg "It certainly is a voluntary act … what they don't know is | what they're
  gonna lose after the marriage continues" · "they have a wife … in family court" · "85 to 90% … paid by men" (DROPPING "Overwhelmingly,
  men pay child support": same claim twice; the number is the receipt) · Dave "You know what? You're right. Here's the problem, though,
  coach (WhisperX large-v3 hears "Here's", medium "It's": check on tape) … horrible legal system, | That isn't an argument against
  marriage" · "it becomes a contract … then the government." · Greg "Correct. And I've never said … I actually am pro-marriage."
  Voices verified by speaker embedding on the podcast audio (wespeaker: Dave 0.66-0.86 on his lines, Greg 0.81-0.87 on his).
  Diarization: no HF token on this machine → speakers by wespeaker embeddings (`scratch dsh/tools/spk.py`), not `--diarize`.
- **2026-10-14: APPROVED by Affan** ("these are a lot better, you can start your work now"): the ★ pick of `_onyx-batch3-2026-10/PICKS.md`
  round 2, **"Marriage Isn't The Trap For Men. The Contract Is."**, ONE clip cut once, edited TWICE (YouTube look + Instagram look). Research, the exact cut table and the sequencing:
  `../_onyx-batch3-2026-10/dsh/research.md` § C2 / § E2. The bar: `../_onyx-batch3-2026-10/VIRAL-BAR.md`. Style upgrades for this batch:
  `../_onyx-batch3-2026-10/STYLE-RESEARCH.md` (§ F variety rule: this prospect's column). Kits upgraded 2026-10-14 (YT: DOC/marks/chart;
  IG: square/void frames, dim reveal, bar meter, ghost, chapter cards).
- Source section: pulled by the main session's YouTube queue into `work/raw-orig/` (YouTube is rate-sensitive on this IP: agents never pull).

## Platform
Permission email named a YouTube Short, but DSH's audience is far stronger on Instagram: @seanmikekelly ≈ 11.9M followers, reels median
16.7K (last 12) vs YouTube Shorts median 55 (last 12), 1.29M subs (STYLE-RESEARCH § C). Both looks are built (batch rule); the IG one is the
one that matters most for this prospect.

## GATE 5 (on screen)
- **"85 to 90% of all child support dollars are paid by men"** = HIS claim (captions, his voice). The receipt shows the Census's own
  printed figures, never "Census: 85-90 % paid by men": US Census Bureau, *Custodial Parents and Their Child Support: 2022* (P60-285, Aug
  2025, the newest edition), p. 4: "custodial parents only received $19.2 billion. Custodial mothers received $16.2 billion … custodial
  fathers received $3.0 billion" (Figure 4 draws the same bars). That is ≈ 84 % to mothers (my arithmetic, not printed); the 2017 edition
  (P60-269) gave $16.1B of $18.6B ≈ 87 %. The Census counts by the CUSTODIAL parent's sex ("received by mothers"), so the card says
  received, not paid by men.
- The dropped "less than 15% of women are payees" stays out (garble).
- **"It becomes a contract between three individuals… the government"** (Dave's line): receipt = *Maynard v. Hill*, 125 U.S. 190 (1888),
  U.S. Supreme Court, via Cornell LII: "Other contracts may be modified, restricted, or enlarged, or entirely released upon the consent of the
  parties. Not so with marriage. The relation once formed, the law steps in and holds the parties to various obligations and liabilities."
- **Credits:** Coach Greg Adams = "author of Free Agent Lifestyle" (his own course page coach-gregadams.teachable.com/p/conquer1: "author of the
  books Free Agent Lifestyle and DeEvolution"; Dave on tape: "I've read both of your books", podcast 6:17). Dave = no surname on tape (none
  invented); "married, two kids" from his own words in the same exchange ("If my wife decides to divorce me… known this woman since I was 17…
  we have two children", podcast 6:48-6:58).
- Show: "Digital Social Hour" (watermark / credit: the show's name only).

## Variety column (STYLE-RESEARCH § F) and why
- **YT hero move = the belief said aloud in the room opens, the challenger's question follows within ~3 s** (D7 adapted: the approved order
  opens on Greg reading his prompt to camera, and reordering is not allowed, so Dave's in-room question is beat 2, not beat 1).
- **YT device = the sticker** ("!" rising from behind the speaker) on the biggest reaction: planned on Greg's "I actually am pro-marriage"
  (the reversal is the clip's biggest beat; it doubles as the stamp the research says the ending needs), settled ≥ 0.5 s before the end cut.
  Re-check on the footage: if the room reacts audibly somewhere, that moment wins.
- **IG frame `square`, caption mode `word` (wide caps)**, accent `#3DB8FC` (the show's sky blue, sampled from its RSS cover art).
- **IG hero card = YOU + SPOUSE + GOVERNMENT** (a horizontal `route`, three nodes landing on "you" / "your spouse" / "the government"), NOT the
  ghost: nobody real is named in the clip, so a ghost would be a stand-in (and the cut-out model is human segmentation). The card prints its own
  words (PARTY 1/2/3…) so the restate gate passes.

## The cut (podcast clock, dry-run 2026-10-14 10:05 on the podcast audio: scratch `dsh/podscout/`, 11 segments, 47.2 s before pause trims)
Map to the video: file t = podcast t − 31.3 − 55 (verify by cross-correlating the video's audio with the podcast MP3 first).
| # | podcast in → out | words | notes |
|---|---|---|---|
| 1 | 119.03 → 121.94 | "Marriage is a financial trap for men." | graft after "Okay, so": cut in the measured −35 dB dip 118.99-119.05 (pinned) |
| 2 | 127.27 → 128.73 | "When you use the word trap," | |
| 3 | 129.76 → 136.20 | "Is there somebody … walking into it? Isn't it kind of voluntary at that point?" | keep "at that point?" (the question's falling tune ends there) |
| 4 | 136.50 → 138.07 | "It certainly is a voluntary act." | |
| 5 | 141.85 → 145.81 | "They don't know what they're gonna lose after the marriage continues." | enter after the 0.78 s pause (drops "Unfortunately, I think for men, what they don't know is": the know|what joint has no gap); split the 0.8 s pause after "lose" |
| 6 | 181.92 → 186.56 | "They have a wife, then they find out who the new wife is in family court." | split the 0.9 s pause after "wife" |
| 7 | 215.955 → 220.03 | "85 to 90% of all child support dollars are paid by men." | graft in the −53 dB dip after "support." (pinned); "Overwhelmingly, men pay child support." dropped (the same claim twice) |
| 8 | 232.57 → 240.05 | "You know what? You're right. Here's the problem, though, coach. Everything you said has everything to do with a horrible legal system," | THE TURN; check "Here's"/"It's" on tape |
| 9 | 243.22 → 246.46 | "That isn't an argument against marriage." | ends before "or" (246.48) |
| 10 | 257.150 → 262.96 | "It becomes a contract between three individuals. It's you, your spouse, then the government." | graft in the dip after "marriage," (pinned) |
| 11 | 283.51 → ≈288.45 | "Correct. And I've never said marriage was a bad institution. I actually am pro-marriage." | the button: end on the measured decay of "-marriage" (fricative vs breath at 288.43-288.52: check centroid); "institution." flagged long-span 1.39 s: check for a repeat/pause |

## Storyboards (draft, timings estimated from the podcast reading; re-timed on the word-level transcript)
Cut ≈ 50 s, 8 beats (research § C2), YT clock ≈ podcast − 31.3 s; file clock = YouTube − 55 s.
| t (est) | Beat / words | YT look | IG look (square) |
|---|---|---|---|
| 0.0-2.8 | Greg (to camera): "Marriage is a financial trap for men." | A Greg ≤ 0.7 s, hook card "ANTI-MARRIAGE COACH / VS A MARRIED DAD" (+ whoosh + thud); B a trap snapping | hook top bar (kicker DIGITAL SOCIAL HOUR · 1 VS 10); `behind` "TRAP?" behind Greg once |
| 2.8-11.6 | Dave: "When you use the word trap … walking into it? Isn't it kind of voluntary?" | A Dave (the question in the room) → B ring exchange → B couple walking the aisle → Dave | lower3 Dave (top bar) "Dave · married, two kids" |
| 11.6-17.7 | Greg: "It certainly is a voluntary act. What they don't know is what they're gonna lose after the marriage continues." | A Greg → B ring set down on papers | lower3 Greg (top bar) "Coach Greg Adams · author, Free Agent Lifestyle" |
| 17.7-22.6 | Greg: "They have a wife, then they find out who the new wife is in family court." | B wedding → B judge + gavel (female judge) | B in the window (gavel) |
| 22.6-30.4 | Greg: "Overwhelmingly, men pay child support. 85 to 90% … paid by men." | A Greg → **DOC Census P60-285** p. 4, highlight "Custodial mothers received $16.2 billion" | neon "$19.2B" (child support paid, 2022) → re-roll "$16.2B" (to mothers) · US Census |
| 30.4-41.4 | Dave: "You know what? You're right. It's a problem though, Coach … horrible legal system. That isn't an argument against marriage." (THE TURN) | SPLIT Dave / Greg on the white line, slower shots (≥ 3.5 s) | chapter card on the cut (the turn) |
| 41.4-47.3 | Dave: "It becomes a contract between three individuals. It's you, your spouse, then the government." | **DOC Maynard v. Hill** highlight "the law steps in…" → SPLIT | **route: PARTY 1 · PARTY 2 · PARTY 3 (the State)** |
| 47.3-52.3 | Greg: "Correct, and I've never said marriage was a bad institution. I actually am pro-marriage." (button) | A Greg held, **sticker** on "pro-marriage", cut ≤ 0.03 s after | lower3 Greg returns (`again`) |
Loop check: "…I actually am pro-marriage." → "Marriage is a financial trap for men." (reads as one argument).

IG card plan, prototyped 2026-10-14 08:45 on the kit-demo picture (scratch `dsh/igtest/proto-sheet*.jpg`): hook in the top bar (kicker
"Digital Social Hour · 1 vs 10", "Anti-marriage coach / vs a *married* dad"); `behind` heavy caps once on the hook; lower3 Dave and lower3 Greg
parked in the TOP bar (Greg's returns on the button); B-roll in the window for ring / gavel; a reticle "THE JUDGE" on the judge; a racked neon
"Child support received, 2022 · $19.2B" re-rolling to "$16.2B · received by custodial mothers" (US Census Bureau · P60-285); a chapter card in
`#3DB8FC` on the cut to Dave's pushback; the HERO = a dark-glass list widget "The marriage contract" building 01 You / 02 Your spouse /
03 The State on the spoken words, closing on a stamp (the horizontal route read too small at 980 px; the word scene spent the face). The
restate gate passed on all of them in the prototype.

## Download log (batch approval 2026-10-14)
| # | File | Source | Size | Why |
|---|---|---|---|---|
| v1 | `work/raw-orig/hsJ05oQk2Ag_<section>.mkv` | https://www.youtube.com/watch?v=hsJ05oQk2Ag sections *0:00:55-0:04:50 (yt-dlp, best ≤ 2160p + audio) | SUPERSEDED: YouTube stayed bot-blocked; see v1b | the source of the cut (the 1 vs 10 debate, YouTube ≈ 1:27-4:17) |
| v1b | `work/raw-orig/hsJ05oQk2Ag_full.mp4` | Affan's own download of the WHOLE video, handed over 2026-10-14 evening (`E:\Bullshit Folder\Henry\1 Anti-Marriage Alpha Male vs 10 Feminists (HEATED DEBATE).mp4`, copied, original untouched); 1080p H.264, the YouTube timeline | 3638 MB | the source of the cut (cut your section from it) |
| d1 | `work/receipts/census-p60-269.pdf` | https://www.census.gov/content/dam/Census/library/publications/2020/demo/p60-269.pdf (US Census Bureau, "Custodial Mothers and Fathers and Their Child Support: 2017", P60-269, May 2020; public domain) | 379,439 B (done) | GATE 5 for "85 to 90% of all child support dollars are paid by men" + the DOC receipt |
| d2 | `work/receipts/census-p60-285.pdf` | https://www.census.gov/content/dam/Census/library/publications/2025/demo/p60-285.pdf (US Census Bureau, "Custodial Parents and Their Child Support: 2022", P60-285, Aug 2025; the newest edition per census.gov/topics/families/child-support.html) | 411,335 B (done; the www2 host, the first URL answered an HTML page) | the same check on the newest data; page renders `yt/assets/broll/doc-census-p4.png` (p. 4, 300 dpi) and `doc-census-cover.png` (p. 1) made locally (pymupdf) |
| d3 | ~~`doc-nrs122.png`~~ NOT PULLED | https://www.leg.state.nv.us/nrs/nrs-122.html answered a Cloudflare block page; https://leginfo.legislature.ca.gov (CA Family Code § 300) a "verify you are human" check: both abandoned (never bypassed) | — | — |
| d3b | `yt/assets/broll/doc-maynard-quote.png`, `doc-maynard-top.png` (local headless viewport stills, 560 css px at 3x) | https://www.law.cornell.edu/supremecourt/text/125/190 (Cornell LII: *Maynard v. Hill*, 125 U.S. 190 (1888)) | 532,138 + 322,195 B (done) | DOC receipt for "it becomes a contract between three individuals… the government" (a first full-page still `doc-maynard.png` mis-tiled at 58K px tall: deleted) |
| d4 | `work/receipts/dsh-cover.jpg` | https://image.simplecastcdn.com/images/96a10b54-3566-4ae1-87fd-fd8bff7bd182/715b32cf-a932-44ce-be6a-786731c62380/3000x3000/whatsapp_image_2026_03_18_at_125501_pm.jpg (the podcast's own RSS cover art) | 135,077 B (done) | the show's accent colour (no YouTube): sky blue `#3DB8FC` (median of the sky) |
| m1 | `audio/music/ES_Campaign - Dylan Sitts.wav` | Epidemic Sound recording e7d120ea-eabe-4e58-b3ed-dc8cf1958f38 "Campaign", Dylan Sitts (beats / hip hop / trap; dark, restless; 137 bpm; 2:34), `mcp__epidemic-sound__DownloadRecording` WAV FULL; not in batch 2 nor in any batch-3 job log (grep 08:35: Moonshots = All Gas No Breaks, Wellness = Memories Of Old) | 44,397,498 B (done; 154.2 s, 48 kHz st; quiet intro 0-14 s, beat 14-98 s, break 98-112 s, beat 112-146 s) | the bed for both looks: a drum-led dark instrumental (Affan's 2026-10-14 swaps on batch 2 were all drum-led hip-hop instrumentals) for a debate |
| p0 | `scratchpad/dsh/pex/thumbs/<id>.jpg` | Pexels search-result preview thumbnails (images.pexels.com, w=320) for "mouse trap", "bear trap", "wedding rings", "gavel", "writing a check" (+ more searches as logged here) | ~20-60 KB each | B-roll selection only |
| t0 | (tooling) `pymupdf` via `uv run --with pymupdf` (PyPI, uv cache) | https://pypi.org/project/PyMuPDF/ | 18.9 MiB | render the Census PDF pages + find the line boxes (no poppler on this machine) |
| b01 | `yt/assets/broll/b-judge-gavel-6101348.mp4` | Pexels, free licence: https://www.pexels.com/video/6101348/ → https://videos.pexels.com/video-files/6101348/6101348-uhd_2160_4096_30fps.mp4 | ~20-60 MB | "family court" (a gavel strikes) |
| b02 | `yt/assets/broll/b-woman-judge-gavel-6101694.mp4` | Pexels, free licence: https://www.pexels.com/video/6101694/ → https://videos.pexels.com/video-files/6101694/6101694-uhd_2160_4096_30fps.mp4 | ~30-80 MB | "who the new wife is in family court" (a judge, not a named person) |
| b03 | `yt/assets/broll/b-ring-exchange-38359910.mp4` | Pexels, free licence: https://www.pexels.com/video/38359910/ → https://videos.pexels.com/video-files/38359910/16289444_1080_1920_60fps.mp4 | ~5-20 MB | "somebody who's getting married" |
| b04 | `yt/assets/broll/b-ring-on-finger-9431543.mp4` | Pexels, free licence: https://www.pexels.com/video/9431543/ → https://videos.pexels.com/video-files/9431543/9431543-uhd_2160_3840_24fps.mp4 | ~20-60 MB | alternate for b03 |
| b05 | `yt/assets/broll/b-divorce-papers-ring-7841583.mp4` | Pexels, free licence: https://www.pexels.com/video/7841583/ → https://videos.pexels.com/video-files/7841583/7841583-hd_1080_1920_30fps.mp4 | ~5-15 MB | "what they're gonna lose after the marriage" (divorce papers + a wedding ring, vertical) |
| b06 | `yt/assets/broll/b-courtroom-gavel-34536748.mp4` | Pexels, free licence: https://www.pexels.com/video/34536748/ → https://videos.pexels.com/video-files/34536748/14633439_2160_3840_50fps.mp4 | ~15-40 MB | "family court" (a gavel strikes in a courtroom), alternate for b01 |
| b07 | `yt/assets/broll/b-mousetrap-633881.jpg` | Pexels photo, free licence: https://www.pexels.com/photo/633881/ → https://images.pexels.com/photos/633881/mouse-trap-cheese-device-trap-633881.jpeg (5873x3921) | ~2-6 MB | "a financial trap for men" (a wooden mousetrap with cheese: the literal noun; Pexels has no mousetrap video) |
| b08 | `yt/assets/broll/b-bride-walks-aisle-14268100.mp4` | Pexels, free licence: https://www.pexels.com/video/14268100/ → https://videos.pexels.com/video-files/14268100/14268100-hd_1080_1920_24fps.mp4 | ~3-10 MB | "walking into it?" (a bride walks away down the aisle toward the altar; no face) |
| d5 | `yt/assets/broll/doc-goodreads-fal.png (local headless still)` | https://www.goodreads.com/book/show/45441164 (Goodreads: Greg Adams, *Free Agent Lifestyle: Men's Guide To Peace, Quiet and Freedom*, 2019) | ~1-3 MB | his own book as the receipt under "And I've never said marriage was a bad institution" (SPLIT bottom) |
| d6 | ~~`b-fal-cover.jpg`~~ deleted: 321 x 500, too soft (HQ rule); replaced by `b-goodreads-fal-card.png` = a LOCAL composite of d5 (the page crop as a card on its own blurred, darkened plate, so the captions on the seam sit on dark) | | https://m.media-amazon.com/images/S/compressed.photo.goodreads.com/books/1556831803i/45441164.jpg (the cover of Greg Adams' *Free Agent Lifestyle*, as Goodreads serves it) | ~0.1-0.5 MB | the SPLIT bottom under "And I've never said marriage was a bad institution" (the white Goodreads page put white captions on white) |
