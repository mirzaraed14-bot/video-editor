# wellness-manson-discipline: Onyx sample Short for Wellness + Wisdom (Josh Trent) (batch 3)

## ▶ STATUS: resume here
- **Better than its closest batch-2 sample (Vivian Tu, also a held belief reversed with a receipt):** YT = real receipts where she had
  0 of 16 real inserts and 3 stock actors (Goggins is his own site, the definition is Manson's own article line, marked), a MEASURED slow
  payoff (after the turn 7 shots at 4.0 s vs her 2.59 s) and an archival "then" device; IG = the void frame + line/dim captions instead of
  window + stack, 2 leaks instead of 5, a 10-word hero diet, the receipt in frame, the bars/zones carrying the meter and the returning name.
- **2026-10-14 21:05: BUILDING (source in: Affan's full download, v1b).** Done: section cut by stream copy at the 2728.309 s keyframe →
  `raw/jSj8VjpdfEI_004528-004941.mkv` (time zero normalised; **t_episode = t_file + 2728.229**, picture and sound both verified against the
  full file, in sync ≤ 1 frame); WhisperX ONCE (on CPU: the GPU was held 90 min by another job + Affan's Topaz); "Why?" is MANSON (his mouth,
  frames at 132.5-132.8 s), so one voice; cut = 16 segments, **44.67 s, 1071 f @ 23.976** (`transcript/cuts.json`, all pinned on the 10 ms
  envelope; a lip click at 217.175 avoided; the 0.83 s pause after "home gym" cut; dead-air gate PASS; joints clean); phantom word edges
  fixed in `transcript/words.json` (think / and / And). Camera cuts measured ON THE BASE: 195, 418, 611, 735, 828, 1070 (the section decode
  ran 2 frames late: `yt/cut_facts.json`). YT v1 built on the 1080p base (payoff: after the turn 7 shots at 4.02 s, last 3.67 s);
  v2 = fixes (s03 card above the seam, s09 ends before the 828 camera change, s12 face raised + the Josh frame 1070 frozen, hook max_w 900,
  shade on the bright plates, 7 spec cues: battery blips + thud, split whooshes, film shutters) waiting on `lock.sh render`. Topaz
  (Iris 2x + FI, 18 takes) queued on `lock.sh gpu`. IG spec written (`ig/build_spec.py`: void, line + dim, lower3 + again, Goggins
  ghost from his site, willpower bar meter, "−30 lbs" neon, B&W mood on NYC, 2 leaks, reticle "the nudge" on the shoes to the end).
- **(superseded) 2026-10-14 10:50: blocked on the source (v1), handed back.** Evidence: `work/raw-orig/` empty (all six
  batch-3 `raw-orig/` folders empty); `_onyx-batch2-2026-10/.locks/youtube.BLOCKED` still carries 06:25:41; `ytqueue.done` unchanged
  since 06:24; no yt-dlp process on the machine (08:11-10:50). Possible silent skip: with the flag up `lock.sh` exits 75 ("BLOCKED"),
  which `ytqueue.sh` doesn't grep for, so a run of `ytqueue-build.txt` after 06:25 would skip every item and still print "finished".
  This job never touches YouTube, the flag or the queue.
  **Ready (all logged below):** bed `audio/music/ES_Memories Of Old - Christoffer Moe Ditlevsen.wav` (Epidemic cc0efab9…, lift at
  21.3 s); B-roll `yt/assets/broll/y01, y05, y06, y07b, y09b, y10` (+ spares y07, y08, y09); DOC receipts `yt/assets/broll/c1-davidgoggins-hero.png`,
  `c2a-markmanson-habits-header.png`, `c2b-markmanson-habits-cue.png` (dry-run through `yt_picture.py`: they render, marks land);
  generators `yt/make_battery.py` (WILLPOWER type card) and `yt/make_archival.py` (NYC "memory" look); storyboards `yt/STORYBOARD.md`,
  `ig/STORYBOARD.md`; `yt/build_spec.py` (word/joint-anchored, reads `yt/cut_facts.json`). Draft cut (episode times, 15 segments, ≈ 43.6 s):
  `yt/STORYBOARD.md` + the RSS word stamps in scratch `wellness/rss_words.txt`.
  **Resume line (when v1 lands):** cross-correlate the file's audio with the RSS mp3 `_onyx-batch3-2026-10/wellness/scout/remine/ep821_A_4520-5100.mp3`
  → time zero (`raw/`) + mouth check → `lock.sh gpu` WhisperX ONCE → cuts.json (the 15 segments) → polish-boundaries → splice
  `AMPLIFY_DB=-2` → camera-cut scan ±2 frames of every joint → write `yt/cut_facts.json` (fps, frames, joints, camera cuts, chunks,
  shots, src_in, bed_in so 21.3 s of the bed lands on the turn) → `make_battery.py` / `make_archival.py` at the base fps → Topaz
  (`lock.sh gpu`) → `yt_faces.py` → `python yt/build_spec.py` → `yt_build.py` → IG spec (void if the set measures dark, else square) → QA.
  **Open for the main session:** the real-inserts gate plans at 3 of 8 (38 %, < 50 %): his home gym and shoes are private, so the gym,
  shoes, scale, grip and cocktail are literal stock nouns (no stock actor for a named person: Goggins is his own site).
- **2026-10-14 09:50: still no source** (flag up since 06:25, no yt-dlp running on the machine; nothing pulled for any batch-3 job). Meanwhile
  done: a dry run of the DOC receipts + battery + archival shots through `yt_picture.py` in a scratch mini-job (all render; DOC card
  params set from it: fg_y ~590-600, max_h 820, push 0.025 on the 7 s DOC), the 4K empty-home-gym and black-sock scale clips (y09b, y07b),
  `yt/build_spec.py` (word/joint-anchored; reads `yt/cut_facts.json` written on the transcript), `ig/STORYBOARD.md`.
- **2026-10-14 08:50 (build agent): PREP DONE, waiting for the source.** `work/raw-orig/` empty; the YouTube flag
  `_onyx-batch2-2026-10/.locks/youtube.BLOCKED` (06:25) is still up and no batch-3 section has landed yet: the main session owns the pull
  (`ytqueue-build.txt`, GAP 240 s); this job never touches YouTube. A background watcher waits for the file.
  Ready: the bed (Epidemic "Memories Of Old", m1), 7 Pexels clips (y01, y05-y10), the two DOC receipts cut to cards
  (`yt/assets/broll/c1-davidgoggins-hero.png`, `c2a-…-header.png`, `c2b-…-cue.png`), the battery type card generator
  (`yt/make_battery.py`, times set on the transcript), the archival-look generator (`yt/make_archival.py`, tested), the YT storyboard
  (`yt/STORYBOARD.md`). Pexels search pages now answer curl with 403: searched through headless Chrome instead (scratch `wellness/pexbrowse.mjs`).
  Next when the file lands: offset vs the RSS mp3 (`_onyx-batch3-2026-10/wellness/scout/remine/ep821_A_4520-5100.mp3`), time zero +
  mouth check, WhisperX ONCE (GPU lock), cuts.json from the draft in `yt/STORYBOARD.md`, polish-boundaries, splice (AMPLIFY_DB=-2),
  camera-cut scan ±2 frames of every joint, Topaz (GPU lock), faces, YT spec + build, IG spec + build, QA, one reviewer, finalize.
- **2026-10-14: APPROVED by Affan** ("these are a lot better, you can start your work now"): the ★ pick of `_onyx-batch3-2026-10/PICKS.md`
  round 2, **"Discipline isn't willpower (Mark Manson keeps his shoes in the gym)"**, ONE clip cut once, edited TWICE (YouTube look + Instagram look). Research, the exact cut table and the sequencing:
  `../_onyx-batch3-2026-10/wellness/research.md` § C2 / § E2. The bar: `../_onyx-batch3-2026-10/VIRAL-BAR.md`. Style upgrades for this batch:
  `../_onyx-batch3-2026-10/STYLE-RESEARCH.md` (§ F variety rule: this prospect's column). Kits upgraded 2026-10-14 (YT: DOC/marks/chart;
  IG: square/void frames, dim reveal, bar meter, ghost, chapter cards).
- Source section: pulled by the main session's YouTube queue into `work/raw-orig/` (YouTube is rate-sensitive on this IP: agents never pull).

## The Short
- **Title (written first):** "Discipline Isn't Willpower: Why Mark Manson Keeps His Shoes in the Gym" (a why + a reversal).
- **Hook / debt:** the belief said aloud ("most people assume a disciplined person is white-knuckling… like David Goggins") → debt: *then
  what IS discipline?* **Second loop:** "really what discipline is…" (the definition) → the receipts (NYC → −30 lbs; the shoes).
- **Button:** "…I couldn't put my shoes on to go anywhere until I walked into my gym." then cut (≤ 0.03 s).
- **Target length:** a belief-reversed mechanism + story = 25-45 s (AW § 4.5); the approved table runs ≈ 45-47 s before pause removal,
  so tightening is inside the approved beats only (drops listed in research § C2: "and it was basically like," goes, per PICKS' ellipsis).
- **Credit (GATE 5):** "Mark Manson · #1 New York Times bestselling author" (markmanson.net/media-kit: "a three-time #1 New York Times
  bestselling author", "sold over 20 million copies", "currently lives in Los Angeles"). Watermark / credit show name: **WELLNESS + WISDOM**.
- **Accent (IG):** the show's primary green **#3FB65F** (wellnessandwisdom.com Elementor globals: primary #3FB65F, secondary #34A8C6,
  read from the episode page saved by the research, `_onyx-batch3-2026-10/wellness/scout/shownotes_835.html`).

## Freshness check (the brief's ask: his own channels / website text, never YouTube or Instagram pages), 2026-10-14
- **The IDEA is a Manson staple, not fresh:** markmanson.net/self-discipline ("If Self-Discipline Feels Difficult, Then You're Doing It
  Wrong": willpower "works like a muscle… becomes fatigued and gives out"), markmanson.net/habits ("consciously creating and/or reorganizing
  the cues in our environment that trigger those habits"), and his own podcast ep 44 "5 Ways to Be Self-Disciplined Without Making
  Yourself Miserable" (markmanson.net/podcast/self-discipline, 2024-08-21: "setting up your environment for success"; David Goggins is
  listed under "Referenced in This Episode").
- **The PICTURES are fresh by search:** the shoes-in-the-home-gym story and "left New York after 8 years, lost 30 lbs" appear in none of his
  own written text (site search "shoes", "willpower"; the self-discipline + habits articles; the podcast ep 44 show notes; web search for
  both stories). The clip lives on those two receipts, which is why they carry the edit (research's fatal weakness: "design your
  environment" is known self-help).

## Decisions (advisor-checked, 2026-10-14)
- **No stock actor for David Goggins** (batch-3 ban): "everybody's like David Goggins" gets a REAL receipt, a DOC of davidgoggins.com
  with its own line highlighted ("…among the world's best ultra-endurance athletes"). The research's "ultra-runner grinding" stock is out.
- **The 5:30 / smoothie / six miles / cold plunge clause** (0:45:55-0:46:02) is NOT in the approved table and would push the cut past 45 s:
  dropped, and with it the alarm / ice-bath B-roll (literal-to-the-words beats the PICKS shot list). If the measured cut lands under ~41 s, a
  three-item version may come back inside beat 1's own sentence (trimming, not a new beat); decided on the transcript.
- **Receipts on purpose** (≥ 50 % real-inserts gate): the davidgoggins.com DOC, the markmanson.net/habits DOC (his own written definition
  of environment design, under beat 5), Manson's own media-kit photo with "The Subtle Art…" (the credential), real New York footage for the
  named city. Literal stock only for the generic nouns (a white-knuckle grip, a draining battery, a scale, a home gym, shoes by a rack).
  The honest real share is reported after the storyboard.
- **YT hero move = the slow payoff (D3):** after the turn ("really what discipline is…") mean shot ≥ 3.5 s, last shot ≥ 3 s. The shoes
  picture arrives ON the button line ("I started putting all my shoes in the gym"), then Manson's face holds ≥ 3 s through "…until I walked
  into my gym" (both locks met: the picture lands on the button, the face holds the payoff).
- **YT signature device = film / archival-feel inserts, adapted:** § F gave this column home-video inserts for "the original wound"; this clip
  has one past-tense beat, "I lived in New York City for eight years", so the NYC inserts get the archival treatment (grain, gate weave,
  faded warm print, soft vignette) as a memory, against clean present-day LA for the home gym and the shoes. The look marks "then" vs "now".
- **IG:** frame `void` only if the set measures dark on the pulled frames (else `square`); captions `line` + `reveal: "dim"` + `hero_gap 4`;
  hero cards = a lower-third that returns (`again`) + the receipts (a willpower bar meter draining "DAY 1 · DAY 2", "−30 LBS" as HIS words);
  the shoes-by-the-rack picture lands ON the button.
- **Josh's interjections** ("Yeah and", "Why?", the NYC riff) mean source camera cuts near the joints: scan ±2 frames of every joint for
  scene cuts before writing shots; every same-camera joint gets a cover (B-roll / DOC on the cut, or a shot boundary).

## Download log (batch approval 2026-10-14; each row written BEFORE its pull)
| # | File | Source | Size | Why |
|---|---|---|---|---|
| v1 | `work/raw-orig/jSj8VjpdfEI_<section>.mkv` | https://www.youtube.com/watch?v=jSj8VjpdfEI sections *0:45:35-0:49:30 (yt-dlp, best ≤ 2160p + audio) — **pulled by the main session** | SUPERSEDED: YouTube stayed bot-blocked; see v1b | the source of the cut (ep 821, 0:45:49-0:49:17) |
| v1b | `work/raw-orig/jSj8VjpdfEI_full.mp4` | Affan's own download of the WHOLE video, handed over 2026-10-14 evening (`E:\Bullshit Folder\Henry\Mark Manson_ How to Get Ahead of 95% of People.mp4`, copied, original untouched); 1080p H.264, the YouTube timeline | 1023 MB | the source of the cut (cut your section from it) |
| m0 | `work/music/preview-<id>.mp3` | Epidemic Sound low-quality previews (audiocdn.epidemicsound.com lqmp3) of 4-6 candidate beds (Open Seas · Ascent · Connection · Dissolving Patterns · Self Help · …) | ~1-3 MB each | music choice only (measured: drums, build, level curve) |
| m1 | `audio/music/ES_Memories Of Old - Christoffer Moe Ditlevsen.wav` | Epidemic Sound recording cc0efab9-55c1-406d-b3cb-3e459bb6c436 "Memories Of Old" (Christoffer Moe Ditlevsen; hopeful, sentimental, build; 90 bpm; 2:51; NO drum stem), MCP `DownloadRecording` WAV FULL; not in batch 2 or any other job's log (grep 08:30) | 49.2 MB (done 08:24, 170.7 s, 48 kHz st) | the bed for both looks: a quiet intro that lifts ≈ 18-24 s in (lands on the turn with bed_in ≈ 0), and its title is the archival device's "then" |
| p0 | `work/pexels/thumbs/<id>.jpg`, `work/pexels/*.json`, `work/pexels/sd/<id>.mp4` | Pexels search-result data (headless Chrome: curl now gets 403 from the search pages) + preview thumbnails (images.pexels.com, w=320) + the smallest SD rendition (videos.pexels.com) of ≤ 20 shortlisted clips, to check content frame by frame | thumbs ~30 KB, SD ~1-6 MB each | B-roll selection only |
| c1 | `work/captures/c1-davidgoggins-mobile.png` | https://davidgoggins.com/ (full-page still, 430 px mobile viewport @3x, local headless capture, `workflows/page-record.mjs --full`, cookie bar removed with --hide) | 3.8 MB, 1290x10683 (done 08:27) | DOC receipt for "everybody's like David Goggins" |
| c2 | `work/captures/c2-markmanson-habits-view.png`, `c2-markmanson-habits-top.png` | https://markmanson.net/habits (viewport stills at the line and at the header, 430 px @3x, local headless capture; exit modal removed) | ~1-2 MB each, 1290x2796 (done 08:31) | DOC receipt: his own written definition ("…reorganizing the cues in our environment…") under beat 5 |
| ph1 | `work/photos/ph1-manson-subtle-art.jpg` | https://markmanson.net/wp-content/uploads/2025/02/Mark-Manson_Subtle-Art_Oct-24.jpg (his media kit, "high-resolution" press photo) | 54 KB (1400x933, done 08:29) | the credential (#1 NYT bestselling author) as a real picture |
| ph3 | `work/photos/ph3-manson-two-books.jpg` | https://markmanson.net/wp-content/uploads/2025/02/Mark-Manson_Two-Books_Oct-24.jpg (media kit) — **pulled with ph1/ph2 at 08:29 before this row was written (logged late, my slip)** | 64 KB (1400x979) | spare credential picture |
| ph2 | `work/photos/ph2-manson-headshot-1.jpg` | https://markmanson.net/wp-content/uploads/2025/02/Mark-Manson_Headshot-1_Oct-24.jpg (media kit) | 66 KB (1400x1179, done 08:29) | spare: IG lower-third / ghost only if needed |
| y01 | `yt/assets/broll/y01-white-knuckle-grip.mp4` | Pexels, free licence: https://www.pexels.com/video/30254380/ → https://videos.pexels.com/video-files/30254380/12970113_1080_1920_50fps.mp4 (1080x1920@50) | 33.1 MB (done 08:40) | "white-knuckling through everything" (a hooded figure gripping a bar, B&W) |
| y05 | `yt/assets/broll/y05-nyc-night-street.mp4` | Pexels, free licence: https://www.pexels.com/video/19332989/ → https://videos.pexels.com/video-files/19332989/19332989-uhd_2160_3840_50fps.mp4 (2160x3840@50) | 24.3 MB (done 08:40) | "I lived in New York City for eight years" (archival treatment) |
| y06 | `yt/assets/broll/y06-nyc-cocktail-pour.mp4` | Pexels, free licence: https://www.pexels.com/video/27136436/ → https://videos.pexels.com/video-files/27136436/12082980_1080_1920_30fps.mp4 (1080x1920@30) | 33.9 MB (done 08:40) | "the only thing to do in New York City is just eat and drink" (archival treatment) |
| y07 | `yt/assets/broll/y07-scale-pov.mp4` | Pexels, free licence: https://www.pexels.com/video/6719385/ → https://videos.pexels.com/video-files/6719385/6719385-hd_1920_1080_24fps.mp4 (1920x1080@24) | 4.7 MB (done 08:40) | "I lost like 30 pounds" (POV feet on a bathroom scale, no face) |
| y08 | `yt/assets/broll/y08-la-palms.mp4` | Pexels, free licence: https://www.pexels.com/video/36904510/ → https://videos.pexels.com/video-files/36904510/15632826_2160_3840_30fps.mp4 (2160x3840@30) | 19.3 MB (done 08:40) | "at my place in LA" (present day, clean) |
| y09 | `yt/assets/broll/y09-home-gym-rack.mp4` | Pexels, free licence: https://www.pexels.com/video/4514294/ → https://videos.pexels.com/video-files/4514294/4514294-hd_1920_1080_24fps.mp4 (1920x1080@23.98) | 7.0 MB (done 08:40) | "I have a little home gym" (a home gym with a rack, present day) |
| y10 | `yt/assets/broll/y10-shoes-by-dumbbells.mp4` | Pexels, free licence: https://www.pexels.com/video/8026527/ → https://videos.pexels.com/video-files/8026527/8026527-uhd_4096_2160_25fps.mp4 (4096x2160@25) | 38.7 MB (done 08:40) | "I started putting all my shoes in the gym" (sneakers by the weights, the button picture) |
| y07b | `yt/assets/broll/y07b-scale-pov-black.mp4` | Pexels, free licence: https://www.pexels.com/video/6547792/ → https://videos.pexels.com/video-files/6547792/6547792-uhd_2160_3840_24fps.mp4 (2160x3840@23.98) | 19.9 MB (done 08:59) | replaces y07 (its readout says "90.9 kg" over cartoon socks): a POV foot in a black sock stepping on a black digital scale, native vertical 4K |
| y09b | `yt/assets/broll/y09b-home-gym-empty.mp4` | Pexels, free licence: https://www.pexels.com/video/8032667/ → https://videos.pexels.com/video-files/8032667/8032667-uhd_2160_4096_25fps.mp4 (2160x4096@25) | 23.9 MB (done 09:06) | "I have a little home gym at my place in LA and I wasn't using it enough": an empty bright home gym corner (dumbbells, mat, ball), native vertical 4K; y09 (1080p landscape, soft at 9:16) becomes the spare |
| y02 | `yt/assets/broll/y02-barbell-grip.mp4` | Pexels, free licence: https://www.pexels.com/video/5319754/ → https://videos.pexels.com/video-files/5319754/5319754-uhd_2160_3840_25fps.mp4 (2160x3840@25) | 22.6 MB (done 20:12) | "white-knuckling through everything": veined forearms gripping a barbell (a second insert so the 4.9 s set-up line gets two shots) |
