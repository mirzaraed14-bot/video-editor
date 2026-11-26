# Two Hot Takes (Morgan Absher) sample: BRIEF

## ▶ BUILDER STATUS (Sonnet, 08:30): picture build running
- Raw fixed by main (07:30): cut re-run on the fixed raw (work/cut/run_cut.sh + retime.py), 16 pieces, 67.97 s + 8-frame dip = 68.23 s (planned 63.5 s: SEQUENCE counted word times, the measured speech edges and kept pauses add ~4.5 s).
- 4K base (work/raw-hq/tht-s5-hq.mkv) spliced frame-locked: yt/prep_hq.py -> yt/work/base_hq_ext.mp4 (MSE vs the 1080p cut 2.2 on 480x270).
- Shots follow DIRECTION § 0b (s04 SPLIT, s08 A Ashby, s10 A Morgan + her label, s10b SPLIT, s11 from "to check for murderers"). 13 drawn scenes done (yt/scenes.py), cue sounds made (yt/sfx_make.py), spec = yt/build_spec.py.
- Next: picture v1 -> grade tests per camera -> grade/sharpen -> overlay + mix -> QA -> finals. Rebuild: bash yt/run_all.sh <v> [picture|grade|overlay].

## ▶ STATUS 2026-11-26 ~07:00 PKT: APPROVED by Affan ("Yes, YouTube look" = SEQUENCE.md Option A, ~63.5 s, YouTube look only). Catalog pass + DIRECTION.md written by main; build next (Sonnet builder), then Opus QC.

- Prospect: Two Hot Takes, host Morgan Absher, 1.03M subs (API 11-24), @TwoHotTakes, Reddit-story reaction show.
- Yes 2026-11-24 21:07 UTC: "Totally fine as long as you tag two hot takes on whatever platforms you're posting on."
  **CONDITION: tag @TwoHotTakes on every platform** (the upload, not the video; the show's name is the on-screen watermark).
- Permitted Short (the one we enhance): "Something weird happened at a party last night - Me (23F) with my boyfriend (28M) of 1.5 years",
  `zB7i3tNVjHQ`, posted 2026-11-10 23:45 UTC, 2:21, 52,323 views / 2,014 likes / 46 comments (API, 2026-11-26).
- Its follow-up Short: "UPDATE: Something weird happened at a party ...", `qDwRNaquIB0`, 2026-11-11, 1:05, 24,341 views / 1,010 likes / 14 comments.
- Parent episode: "Rage Bait! Reddit Stories Ft. Ashby || Two Hot Takes Podcast", `gDA2zhH5fhA`, 2026-11-05, 1:51:38, 696,498 views;
  Story 5 at 1:23:01-1:34:41 (index in its description). Reddit source: r/BestofRedditorUpdates 1wl6i9f (reddit.com refuses our fetches;
  the story text comes from Morgan reading it on the episode).
- Owner of the job's run state: `RUN.md` (this folder).

## Downloads (logged BEFORE each pull; all through `projects/_onyx-batch2-2026-10/pace.sh youtube`, one stream, 180 s apart)
| # | File | Source | Size | Why |
|---|---|---|---|---|
| d1 | `reference/zB7i3tNVjHQ.mp4` | YouTube Short zB7i3tNVjHQ, H.264 | (after pull) | the permitted Short: transcript, frames, audio, teardown |
| d2 | `reference/qDwRNaquIB0.mp4` | YouTube Short qDwRNaquIB0, H.264 | (after pull) | the update Short: the story's payoff, their own follow-up |
| d3 | `work/raw-orig/gDA2zhH5fhA_s5.mp4` | episode gDA2zhH5fhA, section 1:22:50-1:35:00, H.264 <= 1080p | (after pull) | the whole story 5 segment: the full read, every reaction, hook candidates |
| d4 | `work/formats-gDA2zhH5fhA.txt` | `yt-dlp -F` probe of episode gDA2zhH5fhA (no media) | text | YES: 2160p VP9/AV1 (DASH needs the n-challenge, which failed; HLS itag 625 VP9 2160p works) |
| d5 | `reference/zB7i3tNVjHQ.1080.mp4` | YouTube Short zB7i3tNVjHQ, H.264 1080x1920 (`height<=1920`) | 35.2 MB, 29.97 fps, 1.87 Mbps (pulled 07:04) | the permitted Short at full size for Affan's reaction (REACTIONS-LEAN prep `<their-short>`); d1 is 480p |
| d6 | `work/raw-hq/gDA2zhH5fhA_hq.mkv` (855 MB, VP9 3840x2160, video only) -> `work/raw-hq/tht-s5-hq.mkv` (1.36 GB H.264 crf 14 + raw's audio, raw's clock, K=736 frames) | episode gDA2zhH5fhA, section *1:23:20-1:30:40, HLS itag 625 | pulled 07:34, encoded 07:53 | the picture base (`base_hq`) for the 9:16 crops; cut + audio stay on raw/ |

## API calls (Onyx key `Abundance Wisdom/Onyx YT API Key.txt`, via a scratch door that never prints it; 1 unit each)
- 2026-11-26: playlistItems UU uploads (50 items), videos.list (7 ids).

## Platform pick (PLAYBOOK § 0), measured 2026-11-26
| | YouTube Shorts (@TwoHotTakes) | Instagram Reels (@twohottakes) |
|---|---|---|
| Audience | 1.03M subs | 483K followers (1,152 posts; Morgan's own handle is @morgsyabsher) |
| Posts, last 30 days | 14 | 14 (the same clips, cross-posted) |
| Median views, last 30 days | 30,070 (2.9 % of subs) | ~687K (142 % of followers; 5 newest still ramping) |
| THIS story | `zB7i3tNVjHQ` 52,323 views, 2,014 likes, 46 comments (2:21) | `DflHeXNydXy` **1.9M views**, 49.3K likes, 952 comments, 2,043 shares (2:21, 11-10) |
| Its update | `qDwRNaquIB0` 24,341 (1:05) | `DfnGPIJImmj` ~491K (11-11; page read: the UPDATE, 17.8K likes / 81 comments / 428 shares) |
| Best recent | "$1M or… REDDIT EDITION" 376,952 (69 s) | "I stalked my wife for 3 years…" De0Ff5eSLog 5.1M, 231K likes, 51.9K shares (2:11) |
IG read by a Sonnet agent through `pace.sh instagram` (11 loads) + 2 loads by main (13, no block); all numbers in `research/ig-twohottakes-2026-11-26.md`; reel dates decoded from shortcodes (one checked on the page).
Their IG format: 9:16 stacked split, Morgan on top, the guest below, a red-bordered Reddit title card (verbatim post title) on the seam, no burned-in captions seen.
**Same content, 36x the views on Instagram.** Instagram is by far the stronger feed (§ 0 rule 2); their YouTube Shorts are the weak side.

## Viewer comments (API, top by relevance)
- Short: "He's cheating and an idiot beyond idiots" (502 likes), "He's a damn liar" (234), "If your legs were asleep, wouldn't you [go] back to where you were sitting before, not a new spot?" (130; the API text has no "go"), "Update?" (15), "I actually missed that she left that same bathroom he was in until their reaction".
- Update: "Glad she broke up with him" (47), "my problem is with the friends who are still willing to hang out with him" (47), "can someone give me the part 1??".
- So the first Short ends unresolved, and viewers of each half ask for the other half.

## Other tellings of this post (YouTube API, 3 searches, 45 results, `research/yt-search-*.json`)
Only three, all faceless TTS: ScrollTrolls HQ `Skr9gihf3rw` 1,249 views (35 s), reddit doggo `Be9_aIZdQao` 626 (4:08), Void Archive `wEwQns4D72o` 437 (28 s). THT's is the only real telling.
Uploads list (50, with every Short's numbers): `research/uploads-50.json` + `research/v2.json`.

## Catalog pass (CLAUDE.md rule 5), 2026-11-26 ~07:00 PKT (main, Opus)
Read all of `research/effects-catalog/CATALOG.md` (FX-01..FX-81) and looked at all four contact sheets (`_catalog_sheet_1..4.jpg`, every reference still).
- **Fit this video** (a private Reddit story: nothing was filmed, so the B-roll has to be drawn, and the story is about who was where):
  FX-21 Red Silhouette Set (ONE drawn world: couch, stairs, bathroom; the girl is the one red figure, him a white outline),
  FX-23 Pointer Tag (BOYFRIEND, 28 / THE GIRL / LEGS ASLEEP? / HIM / HER), FX-79 Flash-Forward Echo (the bathroom door and the curtain
  in the hook come back at their real point; the dossier returns for the DD line; the couch returns for "ex-boyfriend"),
  FX-28 Dossier Readout (HIS STORY: didn't know / really drunk / designated driver), FX-55 Red Pen Underline (DESIGNATED DRIVER),
  FX-70 ring (his hands on her hips), FX-80 Black-Beat Ident (the dip before the update), FX-30 Whisper Card (UPDATE),
  FX-71 Funnel Count (2 MONTHS on the last word), FX-42 Kin Tag (Morgan, Ashby).
- **Not used before on this channel:** all of them (first Two Hot Takes sample). New to Onyx samples: FX-23 pointer tags, FX-30 whisper
  card, FX-79 echoes inside one drawn world.
- **What the last samples leaned on:** Rise Above (11-12): FX-28 dossier, FX-21 cells, FX-71 clock, FX-27 last-words card. Barbell Logic
  (11-23): plain cards, a red ring, an FX-28 readout (its drawn lifter was dropped at build). Not used here: maps, newsprint, documents
  (the post itself is only its title, rebuilt as the hook card), CRT frames, charts (no numbers in the story but "two months").
- **Better than the last one of its kind (≥ 1 %):** one continuous drawn world whose characters keep their colour and tags from the
  couch to the shower to the last frame ("BOYFRIEND" becomes "EX-BOYFRIEND"), so a sound-off viewer follows who is where; the answer
  inside the Short (their story needed two Shorts); their own best line moved to second 0.
- Direction for the builder: `DIRECTION.md` (this folder).
