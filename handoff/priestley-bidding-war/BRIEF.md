# priestley-bidding-war: Onyx sample Short for Daniel Priestley (batch 3)

## ▶ STATUS: resume here
- **2026-10-19: Affan's OWN MUSIC on both looks:** M83 "Midnight City" (lyrics version: in-point 110 s = the 109-177 s stretch without singing), his file (copied to `audio/music/`, used as a voice-carved copy `*.voicecarve.wav`, -4 dB around 2.5 kHz), from 110.0 s, 14.5 LU under the voice (YT window-held, turn lift 1 dB; measured 13.8-14.5 LU under). New: yt v7 (from v5) / ig ig4 (picture stream-copied from the drafts, mix-only). spec.json + build_spec.py now carry this bed (backups `*.bak-own-music`), `<look>/work/mix.wav` is the new mix (old: `mix.epidemic-bed.wav`): picture-only rebuilds keep his music. Script: `projects/_onyx-batch3-2026-10/own_music.py`.
- **2026-10-14 22:45 PST: YT v6 = the pre-Topaz YouTube candidate (measured QA PASS, every reviewer finding verified fixed on frames:
  `yt/work/qa-f388-v6.jpg`, `qa-chart-v6.jpg`, `qa-misc-v6.jpg`); IG ig3 (the fixed spec) still queued on the shared render lock; Topaz
  RUNNING on the GPU lock since 22:36 (`work/topaz.log` prints at the end).** When `outputs/priestley-bidding-war.topaz.mov` lands:
  `python yt/build_spec.py && python ig/build_spec.py` (both pick up `base_hq` automatically), then ONE YT build and ONE IG build through
  `lock.sh render` (two orphaned waiters of mine, `yt_build … v5` and `ig_build … ig3`, are still polling that lock and will perform exactly
  those builds with whatever spec is current when they win; do not queue duplicates), measured QA (`uv run yt/work/qa.py <mp4>`,
  `kit/ig_qa.py <job> <mp4> --sheet`), then copy to `outputs/<job>.sample-yt.final.mp4` / `.sample-ig.final.mp4` and
  `X:\Claude Projects\Exports\priestley-bidding-war.yt.final.mp4` / `.ig.final.mp4`.
  - **Shared-machine note (for lab-notes):** `lock.sh` polls every 10 s with no queue; an agent that releases the lock and re-queues its
    next render re-takes it within a second, so a waiter can starve (my render waiters lost every hand-over for 70 min between 21:09 and
    22:20; the Topaz waiter waited 3 h behind the GPU lock, whose 90-min stale takeover also let two transcriptions keep running outside it).
    Killing my own orphaned waiters was refused by the permission classifier, so they stay queued and are used as the final builders.
- **2026-10-14 20:10 PST: GATE PASSED, BOTH LOOKS BUILDING.** YT v1 rendered and measured (`yt/work/qa.py`: clean decode, 873 f,
  −12.1 LUFS / −1.8 dBTP, 47 chunks only ! ? quotes, every spoken number captioned, the white line rows 1089–1094 on both splits);
  **v2 queued** (`yt/work/build-v2.log`) with the v1 fixes below; **IG ig1 queued** (`ig/work/build-ig1.log`); both wait on the shared render
  lock (six agents). Topaz is queued behind another agent's GPU lock (held since 19:15) and lands as `outputs/priestley-bidding-war.topaz.mov`:
  re-run both builds with `base_hq` then (the specs pick it up automatically). Next: QA v2 + ig1 (sheets, ig_qa PASS, cue list), one
  fresh-eyes reviewer (sonnet), fix, the Topaz rebuild, finals → `X:\Claude Projects\Exports\`.
  - **Fresh-eyes reviewer (sonnet) on YT v4, 21:20 → adjudicated, fixes in v6 (chart re-rendered to 154 f):** 0 HIGH. MED: the source's
    2-frame zoom step at f388 showed uncovered (the whip's out −2 frame blurs only 6 px) → s09 ends ON the step, the split starts there (the
    step frame = the whip's fully smeared cut frame, the EDL joint f390 sits in its +2 settle). MED: captions on the chart's baseline / the
    bars' bottoms → the chart box raised to y 380–900, push 1 %/s. MED: the "+$100M IN 24 HOURS" chip had 0.3 s → the chart holds 1 s into
    "He said" (to f738, the "15 YEARS" chunk change; the joint f714 sits under B-roll), chip from +116. MED: split 2's white line vanished
    into the men's white curtain → the panel re-cropped (cy 0.60, z 1.2); the clock gets a shade under the captions. MED (GATE 5): a legible
    "us bank" rooftop logo under "sold his company" and a "Vakıf" sign + a flag on the skyline → both clips re-cropped (aerial cx 0.45 cy 0.6
    z 1.15; skyline cx 0.55 / 0.66), checked on full frames; the same crops in the IG spec. LOW: the sticker's edge clipped by the frame
    → [240, 380], s09 push 0.06. LOW: the chart footer's "2026" → kept as the citation's date ("Daniel Priestley on YouTube, July 2026").
    LOW: the third split's cue "missing" → it is in the spec (the brief's list was stale). LOW: the poster frame mid-slide and the last
    whip → by design. Clean: 107/107 caption words, no stray frames at any cut, the seam at 1089–1094 throughout, the counts land within
    0.15 s of the spoken numbers, no stock face as the friend.
  - **Fresh-eyes reviewer (sonnet) on IG ig2, 21:00 → adjudicated, fixes in v4 / ig3:** HIGH: the "matched cut" at 32.16 s is a visible
    same-camera jump (confirmed on the base: frames 803 → 804 go from hands apart to hands clasped, the face ×1.09: the agency's own JUMP
    CUT hidden with a punch-in, not a zoom step; v1–v3 tried to match the crop; impossible) → YT: the button ends on a SPLIT at 804
    (Daniel on the white line, the day-lapse below, `allow_fast_payoff` reasoned); IG: a 1.2 s day-lapse insert at 804, then a fresh A shot.
    MED: the $4.2M neon's label stood alone 1.3 s, the value landed 0.4 s before the end, the lead overlapped the hair, "an hour" low-contrast
    on the bright set → a dark-glass LIST widget ("By the hour": $100M ÷ 24 h → = $4.2M an hour), rows landing on "24 hours" / "make".
    MED: the credit's "Sell a Business, 2026" (a shortened title) → "Daniel Priestley · YouTube". MED: the lower-third to 7.42 s (by design:
    the top-bar share; the brief's 5.9 was stale). MED "15 YEARS" behind the head repeats the caption → KEPT: the behind-the-speaker type IS
    the spoken word by design (STYLE-RESEARCH E10, Chris Williamson); not a card. LOW: the neon's lead2/tail2 re-printed the spoken line →
    "the day before / their own number". LOW: dim captions on the bright curtain and clock face → `grade.shade` on i09 / i12. LOW: the
    reticles framed curtain (the square crop holds one buyer whole, the other at the edge) → both reticles DROPPED. LOW: the green "$100"
    hero → KEPT (the gain colour, like Vivian's "million"; white base + coloured emphasis).
  - **v1 → v2 fixes (measured):** (1) the matched "cut" at f804 matched the SIZE (YuNet ±20 px) but jumped ~60 px sideways: the kit fits
    the crop path as a line per shot and the two fits disagreed at the boundary (the punch-in also shifts the face +22 px in the source) →
    `work/matched_cut.py` derives `yt/work/faces.cut.json` / `ig/work/faces.cut.json` (s15b's box track = s15a's fit continued, corrected
    by the residual × the step 1.0855; landmarks untouched) and the specs read those. (2) The kit's note "cuts 1–3 frames off a chunk
    change": every FREE cut moved onto its chunk change (27→29 became 15: the first B-roll now at 0.60 s, README § 3; 191→188, 236→233,
    283→280, 324→321, 362→364, 510→507); f94 and f804 are baked steps and stay. (3) The count chunks made plain ("220", "240" like
    "140…200"). (4) The sticker centred beside the head ([300, 430]) so the matte reveals it rising from behind his shoulder.
  - **The tape (STEP 1, read 19:16):** the story is on tape and better than the premise. 8:36–9:16 of `WqhKesG91hY`: "I have a friend of
    mine who sold his company for $240 million. And what's crazy is that 24 hours before selling the business for $240 million, they thought
    the price was $140 million. It came up a hundred million in the last 24 hours. It's insane. [Now, what he said happened is he said that]
    two buyers absolutely wanted this particular business. They had a strategic reason to acquire it, and they didn't want anyone else having
    it. And at the last minute, it went 140, 160, 180, 200, 220, 240. [It went from 140 to 240. The thing he said to me,] he said, it took me
    15 years to build a $140 million business, and it took 24 hours to make the next $100 million. [And the reason that he made the next $100
    million is because of the bidding war.]" VIRAL-BAR: A ✓ (the mechanism shown: two buyers who didn't want the other to have it, the price
    climbing in steps), B ✓ money/business, C ✓ (the $240M/$140M contradiction opens it, "24 hours to make the next $100 million" closes it),
    D ✓ a told story with six numbers, E ✓ a how. **Button = "the next $100 million"** (a number, AW rule 8), NOT the last line "…because
    of the bidding war" (an "and that's why" summary, ENGINE § 5) and not "$240" (the 15-years line comes after it on tape; no reordering).
    Dropped: the framing "what he said happened is he said that" (1.9 s), "It went from $140 to $240" (a repeat), "The thing he said to me"
    (the second "he said" keeps the quote attributed). The mechanism line "the key is not to have a buyer but to have a bidding war" (8:24)
    precedes the story on tape and is not used (reordering). Target 35–45 s → **34.92 s** (a story shape: 25–45 s).
  - **Transcript fixes (measured, `transcript/words.json` patched):** WhisperX collapsed "140, 160, 180, 200" into 0.5 s and stamped "It came
    up a" as fiction (p 0.00); per-burst re-ASR + the 10 ms envelope (`work/scan/`) gave the real times: 140 541.60-542.43, 160 542.56-543.04,
    180 543.43-544.11, 200 544.39-544.95, $220 545.24-545.75, $240 545.82-546.40; "$140 million. It came up a hundred million" is continuous
    speech (526.28 → 528.94). There is NO 3.2 s pause in the count: the beats are 0.1–0.4 s and kept as the rhythm.
  - **The cut (`transcript/cuts.json`, pinned):** 516.04→531.64 · 533.52→546.48 · 549.64→556.00 (873 f @ 25, joints f390 / f714). Lip
    sync verified on bilabial closures (price / particular / business / buyers): the picture leads the sound by 1–2 frames, the normal lip
    lead; both streams start at 0 (a full download, not a section). `raw/` = the whole file; the cut reads the full timeline directly.
    Audio chain measured 0 dB (the source is hot; limiter pressure flagged by audio-qa, kept: the kits re-master to −12 / −13 LUFS).
  - **Source picture facts that drive both builds:** one camera; the agency's baked punch-in steps at cut f94, f324, f388, f551, f804
    (face height ×1.083 at f804, measured) and its own stock insert on f582–f714 (the whole count-up has no face). Every step lands on a cut
    to B-roll / a card; f804 is a matched "cut" (s15b z0 = 1.288 / 1.083, the push continued) so the button is one continuous 6.4 s shot.
  - **YT look (`yt/STORYBOARD.md`, `yt/build_spec.py`):** hero move = type cards ($240,000,000 counting up; the same card re-rolling 2→1
    into $140,000,000) + a glossy render on "strategic reason to acquire it"; signature device = the chart receipt (`g-chart.mp4`, six bars
    landing ON each spoken number, +$100M IN 24 HOURS chip); the sticker rises on "It's insane" (matte `yt/assets/daniel-insane-matte.mov`);
    two splits with the white line; hook "FROM $140M TO $240M / IN 24 HOURS"; the friend's quote in yellow. Shares B 51 / SPLIT 13 / A 35;
    after the turn (23.36 s) mean 5.8 s, last shot 6.4 s. **Better than batch 2's closest (MrBeast, real artefacts):** the receipt is
    word-synced bar by bar; no stock actor anywhere (the friend stays unseen); the baked punch-ins of a produced source handled without a
    single same-camera jump; the slow payoff measured (5.8 s vs 2.66).
  - **IG look (`ig/build_spec.py`):** frame SQUARE, stack + dim reveal, hero_gap 4; top-bar lower-third that returns on the button; the
    racked $240,000,000 → $140,000,000 neon; the bottom-bar story meter THE PRICE moving through the six spoken prices; reticles on the two
    buyers; "15 YEARS" behind his head; a computed "$4.2M an hour" neon ($100M ÷ 24 h, labelled as his numbers) on the button; 2 leaks.
    Accent #BE4046 (the show's brick red #A8393E lifted one step for the black window). **Better than batch 2's closest (Vivian IG):** no
    leak tic (2, on real changes), heroes rationed, every card adds a number the captions don't say, the bars carry content ≥ 25 %.
- 2026-10-14 19:00 PST: STEP 1 (the tape gate) started: the whole 22:13 video transcribed ONCE (WhisperX large-v3 + alignment, GPU lock)
  from its audio track copied to `work/full-asr/raw/` → `work/full-asr/transcript/words.json` = `transcript/words.json` (episode time = file
  time, the full file has no offset).
  - Picture scan (`work/scan/sheet-480-720.jpg`, `scdet-500-680.txt`): one camera on Daniel at a desk, bright garden behind; the agency
    edit bakes in stock B-roll (boardroom 8:30–8:35, auction hands 9:01–9:06), cream quote cards (9:28–9:34, 9:44–9:50, 10:14–10:19),
    red label boxes (9:42, 10:00–10:06), a whiteboard inset 10:19–10:44, a chat card 11:07–11:12, AND punch-in zoom steps inside his
    takes (8:39.8, 8:49.0, 8:51.6, 8:52.8, 8:59.96, 9:13.2, 9:18.4, 9:20.0, 10:47.6, 10:55.2). Each baked zoom step is a same-camera
    jump: hide it under B-roll / a full-window card, or split the A shot on it with matched z0 (a "cut", no whip).
  - GATE 5 (his own site, `work/gate5/danielpriestley-home.html`, 2026-10-14): "co-founder of Dent Global and ScoreApp", "built and sold
    multiple successful multi-million dollar businesses", "bestselling author", "the most returned guest on Diary of a CEO". Kicker options
    from these only. The friend's deal is HIS ACCOUNT (unnamed): numbers on screen are labelled as his telling.
  - Accent (measured on the show's own graphics, label box 9:42 and the "04" chapter numeral): **#A8393E** (brick red); the cards are
    cream #F4F0E2.
  - Music lead candidate (not yet downloaded): Epidemic "Luxx" (Out To The World, ambient · dark · suspense, 96 bpm, 3:47; drums stem
    17.6 LU under the full mix on the previews, so it is tonal) — new to the batch; alternates "Unknown Phenomenon", "Tracker".
- **2026-10-14: APPROVED by Affan** ("these are a lot better, you can start your work now"): the ★ pick of `_onyx-batch3-2026-10/PICKS.md`
  round 2, **"How a $140M offer became a $240M sale in one day"**, ONE clip cut once, edited TWICE (YouTube look + Instagram look). Research, the exact cut table and the sequencing:
  `../_onyx-batch3-2026-10/priestley/research.md` § C2 / § E2. The bar: `../_onyx-batch3-2026-10/VIRAL-BAR.md`. Style upgrades for this batch:
  `../_onyx-batch3-2026-10/STYLE-RESEARCH.md` (§ F variety rule: this prospect's column). Kits upgraded 2026-10-14 (YT: DOC/marks/chart;
  IG: square/void frames, dim reveal, bar meter, ghost, chapter cards).
- Source section: pulled by the main session's YouTube queue into `work/raw-orig/` (YouTube is rate-sensitive on this IP: agents never pull).

## Download log (batch approval 2026-10-14)
| # | File | Source | Size | Why |
|---|---|---|---|---|
| v1 | `work/raw-orig/WqhKesG91hY_<section>.mkv` | https://www.youtube.com/watch?v=WqhKesG91hY sections *0:08:15-0:11:25 (yt-dlp, best ≤ 2160p + audio) | SUPERSEDED: YouTube stayed bot-blocked; see v1b | the source of the cut (premise only until this pull is read on tape) |
| v1b | `work/raw-orig/WqhKesG91hY_full.mp4` | Affan's own download of the WHOLE video, handed over 2026-10-14 evening (`E:\Bullshit Folder\Henry\Sell a Business Someone Will Fight to Buy - My Playbook in 22 Minutes.mp4`, copied, original untouched); 1080p H.264, the YouTube timeline | 326 MB | the source of the cut (cut your section from it) |
| m1 | `yt/assets/audio/ES_Luxx - Out To The World.wav` (WAV, FULL mix; the INSTRUMENTS stem as a fallback if the drums read on the bed) | Epidemic Sound recording `0005db4e-ce08-463f-b43c-b32539837dc5` "Luxx", Out To The World (ambient · dark · suspense, 96 bpm, 3:47), `mcp__epidemic-sound__DownloadRecording`; previews `work/music/preview-luxx*.mp3` (drums stem 17.6 LU under the full) | ~40-70 MB | the music bed of both looks (new to the batch; batch 2 used DOX, She Knows, Thelema, There Is Still Time) |
| y02 | `yt/assets/broll/y02-office-aerial.mp4` | Pexels, free licence: https://www.pexels.com/video/13175373/ (best rendition, see `work/pexels/dl.txt`) | ~20-90 MB | "sold his company" (a company = its tower, literal) |
| y05 | `yt/assets/broll/y05-contract-signing.mp4` | Pexels: https://www.pexels.com/video/8439245/ | ~10-60 MB | "before selling the business" (the signing) |
| y07 | `yt/assets/broll/y07-cash-stacks.mp4` | Pexels: https://www.pexels.com/video/6266432/ | ~20-80 MB | SPLIT bottom, "it came up a hundred million" |
| y08 | `yt/assets/broll/y08-skyline-day-timelapse.mp4` | Pexels: https://www.pexels.com/video/27817643/ | ~40-150 MB | "in the last 24 hours" (a day passing) |
| y10 | `yt/assets/broll/y10-two-buyers-table.mp4` | Pexels: https://www.pexels.com/video/8426050/ | ~20-80 MB | SPLIT bottom, "two buyers" (generic nouns; nobody named) |
| y11 | `yt/assets/broll/y11-render-network.mp4` | Pexels: https://www.pexels.com/video/35063152/ (native 1080x1920 3D render) | ~10-40 MB | "a strategic reason to acquire it" (abstract noun → a glossy render, STYLE-RESEARCH D5) |
| y13 | `yt/assets/broll/y13-clock-second-hand.mp4` | Pexels: https://www.pexels.com/video/39488470/ | ~20-80 MB | "at the last minute" |
| y14 | `yt/assets/broll/y14-auction-hands.mp4` | Pexels: https://www.pexels.com/video/37639454/ | ~20-80 MB | IG look, the count-up window picture: hands raised at an auction ("it went 140, 160…" = bidding, literal) |
| p0 | `work/pexels/thumbs/<id>.jpg` | Pexels search-result pages (`https://www.pexels.com/search/videos/?q=…`, read with curl) and their preview thumbnails (images.pexels.com) | ≤ 120 KB each, ≤ 80 files | B-roll selection only |
| y14 (REJECTED) | `yt/assets/broll/y14-auction-hands.mp4` | pulled, then checked at full size: a concert crowd with one raised hand, not an auction — not used (kept in the folder, logged) | 28.9 MB | — |
