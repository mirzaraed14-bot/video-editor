# spi-link-in-bio: Onyx sample Short for Smart Passive Income (Pat Flynn) (batch 3)

## ▶ STATUS: resume here
- **2026-10-14 19:15 (build agent, Fable): BUILDING, phase A (the cut).** Source landed (v1b): the section `raw/ZVEfS6yAIcc_2814-3122.mkv` = the full
  video's keyframe 1694.593 s (28:14.6) → 1882.881 s, video stream-copied, audio FLAC padded to time zero; both streams start together
  (0.033 s mkv offset, no A/V gap: `ffprobe` start_time equal; mouth check on the transcript next). **t_file = t_video − 1694.593 s.** Layouts
  (`work/frames/sheet.jpg`): Pat single (red SUPERFANS shirt, plants) 0-30 s, Brock single (sweater, bright blue-white set) 36-170 s, a wide
  two-shot ≈ 174-186 s; the episode cuts between the singles (camera cuts = the joint/scene grid for both looks).
  WhisperX queued behind the Priestley agent's full-episode ASR on the GPU lock (RAM is at 0.3 GB free: no CPU run). Meanwhile DONE: the bed
  (m1), the accent, the DOC receipt (d1, the "over 800k followers" paragraph at page y 0.3798-0.3981, Manychat line at y ≥ 0.466 excluded by
  the crop), 4 Pexels clips (b01-b04), the mock-funnel generator `yt/make_mock_ui.py` (profile · audience · comments · inbox · names, fictional,
  no ManyChat). NEXT: words.json → `transcript/cuts.json` from the approved table → polish-boundaries → splice (full render, chat-only) →
  dead-air gate → camera-cut scan ±2 frames of every joint → Topaz (Iris 2x + FI, `--segments`, GPU lock) → faces → `yt/build_spec.py` →
  `yt_build.py` → `ig/build_spec.py` → `ig_build.py` → QA → one Sonnet reviewer → finalize to `X:\Claude Projects\Exports\`.
- **2026-10-14: APPROVED by Affan** ("these are a lot better, you can start your work now"): the ★ pick of `_onyx-batch3-2026-10/PICKS.md`
  round 2, **"How to turn your followers into money (stop saying 'link in bio')"**, ONE clip cut once, edited TWICE (YouTube look + Instagram look). Research, the exact cut table and the sequencing:
  `../_onyx-batch3-2026-10/spi/research.md` § C2 / § E2. The bar: `../_onyx-batch3-2026-10/VIRAL-BAR.md`. Style upgrades for this batch:
  `../_onyx-batch3-2026-10/STYLE-RESEARCH.md` (§ F variety rule: this prospect's column). Kits upgraded 2026-10-14 (YT: DOC/marks/chart;
  IG: square/void frames, dim reveal, bar meter, ghost, chapter cards).
- Source section: Affan's own download of the whole video (v1b); agents never touch YouTube.

## The Short
- **Title (written first):** "How to turn your followers into money (stop saying 'link in bio')" (a how + a reversal of the habit everyone has).
- **Hook / debt:** Pat's question in full ("what is the best way for a person who now has a following, how might they then convert those
  followers into dollars?") → debt: *so what do I say instead of "link in bio"?* **Second loop** at beat 7 ("you don't know who they are"),
  closed by the names list.
- **Button:** "…so I can go manually follow up with the other seven" → cut ≤ 0.03 s after "seven".
- **Sequencing (approved, § E2 TOP 1; trimming inside it only):** 1 Pat's question → 2 "I don't care if you go viral, I care if you are putting
  food on the table, paying your bills" → 3 "the tried and true way… has been click the link in my bio" → 4 "half your audience… not interested…
  the half that is interested… told… go somewhere else" → 5 "if instead you use Direct Message Automation… comment the word blank and I will send
  you blank" → 6 "hundreds of comments… instantly sent… right to their inbox" → 7 "when someone clicks the link in your bio, you don't know who
  they are" → 8 "I can literally see the names… of the 10 people who clicked, only 3 purchased. So I can go manually follow up with the other
  seven". Target 40-46 s (a question in the room + a mechanism: AW § 4.5).
- **Credit (GATE 5):** "Brock Johnson · Instagram coach · 800K+ followers" (SPI 911 show notes: "He now has over 800k followers, personally
  consults with Meta and Instagram staff"; the DOC receipt d1 shows that sentence). Watermark / show name: **SMART PASSIVE INCOME**.
- **GATE 5 on screen:** "10 clicked · 3 purchased · 7 to follow up" = Brock's ILLUSTRATION: the names card is labelled EXAMPLE and prints no
  result; "for the last 20 years" stays in his voice (captions), never in a graphic; no ManyChat name or UI anywhere; no real account (handle
  "yourbrand", first names only).
- **Accent (IG):** the show's green **#00B050** (dominant saturated colour of the SPI cover art, d2; the secondary is #30C070).
- **Variety (STYLE-RESEARCH § F, SPI column):** YT hero move = evidence shots of a real funnel (self-made diegetic receipts: the profile's bio
  link, the audience split, the comment flood, the DM inbox, the 10-names list) + the real DOC of the show's own page; signature device =
  annotation boxes (blue `marks` on the bio link, a red circle on the 7). IG: frame `window`, captions `line` + dim reveal + hero diet, hero
  card = chapter cards (#1 LINK IN BIO · #2 COMMENT "GUIDE" · #3 FOLLOW UP) and the 10-names list (3 BOUGHT, 7 FOLLOW UP).
- **Freshness (unchecked: YouTube blocked; Affan approved the pick anyway):** their 2.1M Short "Stop letting your social media traffic go to
  waste" is probably the link-in-bio passage. Ours differs in two beats their title cannot carry: it OPENS on Pat's question (the host asking
  the viewer's own question, so the answer is framed as "how to make money from a following", not "stop wasting traffic") and it ENDS on the
  follow-up step (the names list: who bought, who to chase), which is the usable takeaway; the middle (link in bio leaks → comment the word)
  is the shared mechanism.
- **Better than the closest batch-2 sample (MrBeast / Creator Science, the real-artefact one):** zero stock actors and ≥ 50 % self-made
  diegetic receipts of the thing itself (a funnel you can see), a real DOC of the show's own page with the credential highlighted, the host's
  question as the opening beat, annotation marks on the receipts, a measured slow payoff (after-turn mean ≥ 3.5 s, last shot ≥ 3 s), and the
  hook carrying a whoosh + hit pair.

## Download log (batch approval 2026-10-14)
| # | File | Source | Size | Why |
|---|---|---|---|---|
| v1 | `work/raw-orig/ZVEfS6yAIcc_<section>.mkv` | https://www.youtube.com/watch?v=ZVEfS6yAIcc sections *0:28:00-0:31:30 (yt-dlp, best ≤ 2160p + audio) | SUPERSEDED: YouTube stayed bot-blocked; see v1b | the source of the cut (SPI 911, video ≈ audio + 0:55 (audio ≈ 27:40-29:55)) |
| v1b | `work/raw-orig/ZVEfS6yAIcc_full.mp4` | Affan's own download of the WHOLE video, handed over 2026-10-14 evening (`E:\Bullshit Folder\Henry\Instagram Expert Explains How to Grow from Zero Followers in 2026.mp4`, copied, original untouched); 1080p H.264, the YouTube timeline | 523 MB | the source of the cut (cut your section from it) |
| p0 | `work/pex/*.json` + `work/pex/thumbs/<id>.jpg` | Pexels video search pages (headless Chrome, `work/tools/pexbrowse.mjs`, the wellness agent's helper) for "family dinner table", "paying bills", "cash money hands", "scrolling phone", "thumb tapping phone", "typing message phone"; preview thumbnails from images.pexels.com | ~20-60 KB each, ≤ 80 files | B-roll selection only |
| d1 | `yt/assets/broll/doc-spi911-full.png` | https://www.smartpassiveincome.com/session911 (the show's own SPI 911 show-notes page, full-page still via `workflows/page-record.mjs --full`, 1280 css px at 2x) | ~2-8 MB | DOC receipt: who is answering (Brock Johnson, "interviews he's hosted with the heads of Instagram"); GATE 5 for the kicker |
| d2 | `work/receipts/spi-cover.jpg` | the SPI podcast's own RSS cover art (`<itunes:image>` of https://rss.art19.com/smart-passive-income-podcast, already saved in `../_onyx-batch3-2026-10/spi/meta/rss_art19.xml`) | ~0.3-2 MB | the show's accent colour for the Instagram look (no YouTube) |
| m1 | `audio/music/ES_Fragment - Lennon Hutton.wav` | Epidemic Sound recording 23a7aedb-ca72-4784-9176-f0b69b18397d "Fragment" (Lennon Hutton / Martin Landh; minimalism, mysterious, pulses, 105 bpm, 3:02; stems INSTRUMENTS / BASS / MELODY only = no drums), `mcp__epidemic-sound__DownloadRecording` WAV FULL | ~30-35 MB | the bed for both looks (tonal, no drums; not used in batch 2: those were There Is Still Time, DOX, Spring, Thelema / She Knows) |
| b01 | `yt/assets/broll/b-plate-to-table-3198244.mp4` | Pexels, free licence: https://www.pexels.com/video/3198244/ → https://videos.pexels.com/video-files/3198244/3198244-hd_1080_1920_25fps.mp4 (native vertical 1080) | ~10-30 MB | "putting food on the table" (a plate carried to a family table; a stranger as a literal noun, no named person) |
| b02 | `yt/assets/broll/b-past-due-bills-7924459.mp4` | Pexels, free licence: https://www.pexels.com/video/7924459/ → https://videos.pexels.com/video-files/7924459/7924459-uhd_2160_3840_25fps.mp4 | ~20-60 MB | "paying your bills" (paper bills stamped PAST DUE in a man's hands) |
| b03 | `yt/assets/broll/b-counting-dollars-6266251.mp4` | Pexels, free licence: https://www.pexels.com/video/6266251/ → https://videos.pexels.com/video-files/6266251/6266251-uhd_2160_3840_25fps.mp4 | ~20-60 MB | "convert those followers into dollars" (hands counting $100 bills) |
| b04 | `yt/assets/broll/b-scrolling-phone-17512949.mp4` | Pexels, free licence: https://www.pexels.com/video/17512949/ → https://videos.pexels.com/video-files/17512949/… (best mp4 from the search JSON) | ~20-60 MB | "they're not interested… they're just going to scroll" (a hand scrolling a phone gallery; checked for real UI / names at full size before use) |
