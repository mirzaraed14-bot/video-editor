# tftc-hospital-bill: Onyx sample Short for TFTC (Marty Bent) (batch 3)

## ▶ STATUS: resume here
- **2026-10-19: Affan's OWN MUSIC on both looks:** Seekae "Test & Recognise" (Flume re-work, slowed; vocals almost throughout: in-point 313 s = the vocal-free full-level outro), his file (copied to `audio/music/`, used as a voice-carved copy `*.voicecarve.wav`, -4 dB around 2.5 kHz), from 313.0 s, 14.5 LU under the voice (YT window-held, turn lift 1 dB; measured 13.8-14.5 LU under). New: yt v2 / ig v4 (picture stream-copied from the drafts, mix-only). spec.json + build_spec.py now carry this bed (backups `*.bak-own-music`), `<look>/work/mix.wav` is the new mix (old: `mix.epidemic-bed.wav`): picture-only rebuilds keep his music. Script: `projects/_onyx-batch3-2026-10/own_music.py`.
- **2026-10-14 22:40 (build agent): TOPAZ STOPPED, both looks ship on the 1080p base.** `topaz-iris.py` (Iris 2x + FI, 8 takes) held the GPU lock
  from 21:18 and finished ONE 114-frame take in 73 min (the GPU was saturated by Affan's own Topaz Video AI session plus other agents' jobs);
  the remaining 800 frames would have taken the night while two other agents' Topaz runs queued behind it. Killed (my process only), the stale
  lock entry removed, the lock passed to Priestley's run at 22:36. **Unresolved:** re-run `python workflows/topaz-iris.py outputs/tftc-hospital-bill.mp4
  outputs/tftc-hospital-bill.topaz.mov --out-scale 2 --no-stab --segments 0,114,342,398,496,506,662,767` under `lock.sh gpu` when the GPU is free
  (both specs already point `base_hq` at that file and skip it while it is missing), then rebuild both looks (the pictures only).
  IG v2 (`outputs/…sample-ig.v2.mp4`): ig_qa **RESULT: PASS** (−13.1 LUFS, −1.6 dBTP, 34 cues / 23 events, 6.0 per 10 s, top bar 33 %); one
  defect by eye: the compare's "Insured" column reached Marty's hairline → v3 (380 px wide, `--skip picture`) queued on the render lock.
- **2026-10-14 22:15 (build agent): IG v1 built and measured, IG v2 queued; YT v1 queued on the render lock (other agents' builds re-take it
  within seconds of each release: 1 h of queueing so far); Topaz running since 21:18 (GPU lock).** IG v1 (`outputs/…sample-ig.v1.mp4`):
  ig_qa PASS on decode / loudness (−13.1 LUFS, −1.7 dBTP) / 107 words once / punctuation / caption y 1070 constant inside the window / 29
  cues on 20 events / slots / 2 leaks; top bar 30 %; **FAIL restate** (the racked "$5,000" neon printed "charged… bag") and an 8 s stretch
  from 28 s with one event in the last window. Also seen on the sheet: the caption read "80?" (WhisperX's question mark on Andy's
  statement) → fixed at the source: words.json token "80." + `reapply-corrections.sh` (both looks inherit). **v2 changes** (`ig/build_spec.py`):
  neon lead/tail "what the hospital billed him / one liter of saline"; Marty's lower-third return moved onto the button (34.0-36.8, top
  bar); a HUD reticle on the dollar bills (29.9-33.7, "cash, up front"); the −50% neon replaced by a `compare` (Insured · Full price vs
  Paying cash · −50%, "his experience", the right column on "50%", the winner lights after it).
- **2026-10-14 21:05 (build agent): THE CUT IS FINAL (`outputs/tftc-hospital-bill.mp4`, 913 frames @ 24 = 38.17 s, 8 segments, AMPLIFY_DB
  measured 2); Topaz (Iris 2x + FI, GPU lock), the IG build (v1) and the YT build (v1) are running.** What happened since 19:35:
  - **The research's "YouTube ≈ RSS + 13 s" was wrong by minutes**: the first sections (14:40-18:10, 50:40-52:10) transcribed (CPU, the GPU lock
    was held ~1 h by other jobs' ASR + Affan's own Topaz) to RSS 12:57-16:27 / 45:25-46:55. Measured: YouTube = RSS **+163 s at 15 min, +316 s at
    46 min**. Re-cut (v3 rows): `raw/LjT9OUGZ1q4_A.mkv` = 18:20-21:00, `_B.mkv` = 55:40-58:00; transcribed on CPU (`work/transcribe-cpu2.log`).
  - **Speakers verified on the VOICE** (`work/speakers.py`, wespeaker, CPU; `work/speaker-spans.json`): Andy = the BALD guest (glass office, AirPods),
    Marty = the BOOKSHELF host (SHURE mic). Every beat's voice matches the face on screen; the research's attribution holds (hook, $8, 80, finger =
    Andy 0.81-0.96; the question + the cash button = Marty 0.90 / 0.73).
  - **Three WhisperX stamps were fiction, fixed by measurement** (10 ms RMS strips + slice ASR; `work/words.json.bak-prepatch` = the untouched
    original): "80" (stamped 58.80-58.85, really 58.86-59.17), "poor" (end 52.06 → 51.07), and the whole "for a bag… saline solution" run was
    force-aligned 3-5 s early onto "$5,000" — the tape says "for a bag, a thousand milliliter bag of saline solution" at 37.77-42.29 (a RESTART),
    re-stamped as its 10 real words. **The graft** follows the mid-thought-restart rule: take 1 through "for a bag," (38.76) + take 2 from "of
    saline solution" (40.04) = the approved "charged $5,000 for a bag… of saline". Kept: "80." alone (crisp; "Yeah, 80, 80 are very clear"
    dropped); "they immediately think that you are poor" + "and treat you completely differently" (the bridge into "Not only that"); the 0.63 s
    pause after "IV" (the joke's timing). Pinned by hand: seg 3 in = 54.75 (the source cuts to Marty at 54.708: 2 stray Andy frames otherwise).
  - QA on the base: `audio-qa` joints clean, limiter transparent; dead-air gate PASS; `work/base-layout.json`: every face switch lands ON a joint
    (joints 114, 342, 398, 496, 506, 662, 767); lip sync checked by eye on 6 plosives (`work/frames/mouth-check.jpg`: lips closed one frame
    before each burst, both speakers); the correlation tool (`work/scripts/lipsync.py`) is inconclusive on these faces (≈0 at lag 0, noisy peaks).
  - Cut transcript: 107 words incl. two slivers the captions absorb ("and" at 0.00, the [g] of take-2's "bag" at 14.25). Chunks in `yt/build_spec.py`.
  - **Kit lesson (faces):** `yt_faces.py`'s largest-face rule picked a 593 px false "face" on the door handle / wood panel at the right
    edge of Andy's shots (x 1445-1965) over his real 471 px face; every speaker shot now carries `face_x 0.5` (both looks): Andy cx 911,
    44 % face height; Marty cx 1047, 39 %. Both specs snap every shot edge within 6 frames onto a rough-cut joint (`f()` / `Fj()`), so the
    cuts ARE the joints (the graft at 342 sat 2 frames inside Andy's A shot before).
- **2026-10-14 19:35 (build agent): ASSETS IN, TRANSCRIPTION QUEUED.** Sections cut from Affan's full file (`raw/LjT9OUGZ1q4_A.mkv` 14:40-18:10,
  `_B.mkv` 50:40-52:10, keyframe-aligned stream copies, audio padded to 0; video starts 0.075 / 0.069 s after the audio, which `splice.sh`
  `video_offset` handles). `transcribe.sh` is queued under `lock.sh gpu` (`work/transcribe.log`; the lock was held by Priestley's then SPI's ASR).
  Source layout measured (`work/base-layout-raw.json`): Andy full-frame (bookshelf) / Marty full-frame (bald, glass office) / a TWO-UP with an X post and
  both faces as 385 x 260 boxes (no usable face: "80" and the finger beat are B-roll). Speaker identity to be verified on the VOICE
  (`work/speakers.py`), not the camera. Receipts captured (Goodbill $26,667 headline, ACEP 99281-99285 list, STAT cash-price sentence:
  `yt/assets/broll/doc-*.png`, boxes in `yt/receipt-boxes.json`, the STAT split-bottom card `card-stat-cash.png`); bed Mindscape (from 0 s);
  7 Pexels clips checked on a contact sheet (`work/frames/broll-sheet.jpg`: hands / objects only, no stock actor as a named person).
  Storyboard: `yt/STORYBOARD.md`. Spec builders written against word anchors: `yt/build_spec.py`, `ig/build_spec.py`; the cut plan:
  `work/cut_plan.py`. **Next:** transcript → `cut_plan.py` → polish-boundaries → `RENDER=0` splice → dead-air QA → render splice → Topaz
  (Iris 2x + FI, GPU lock) → `yt_faces.py` (yt + ig) → both builds → QA.
- **Better than batch 2 (plan):** vs Vivian (the closest: a money reversal, one speaker's story): the receipts are REAL pages, not stock
  (0 stock actors as named people, 3 real receipts + the show's own question beat), the chart lands on the spoken number with its source
  printed, the host's question is a beat on his face, 32 s instead of 44, the payoff holds ≥ 3 s on a split with the receipt.
- **2026-10-14: APPROVED by Affan** ("these are a lot better, you can start your work now"): the ★ pick of `_onyx-batch3-2026-10/PICKS.md`
  round 2, **"Your hospital bill is probably wrong. Here's what to say."**, ONE clip cut once, edited TWICE (YouTube look + Instagram look). Research, the exact cut table and the sequencing:
  `../_onyx-batch3-2026-10/tftc/research.md` § C2 / § E2. The bar: `../_onyx-batch3-2026-10/VIRAL-BAR.md`. Style upgrades for this batch:
  `../_onyx-batch3-2026-10/STYLE-RESEARCH.md` (§ F variety rule: this prospect's column). Kits upgraded 2026-10-14 (YT: DOC/marks/chart;
  IG: square/void frames, dim reveal, bar meter, ghost, chapter cards).
- Source section: pulled by the main session's YouTube queue into `work/raw-orig/` (YouTube is rate-sensitive on this IP: agents never pull).

## Download log (batch approval 2026-10-14)
| # | File | Source | Size | Why |
|---|---|---|---|---|
| v1 | `work/raw-orig/LjT9OUGZ1q4_<section>.mkv` | https://www.youtube.com/watch?v=LjT9OUGZ1q4 sections *0:14:40-0:18:10 + *0:50:40-0:52:00 (yt-dlp, best ≤ 2160p + audio) | SUPERSEDED: YouTube stayed bot-blocked; see v1b | the source of the cut (#681 RSS 0:15:00-0:17:28 + 0:51:06; YouTube ≈ 13 s longer, padded) |
| v1b | `work/raw-orig/LjT9OUGZ1q4_full.mp4` | Affan's own download of the WHOLE video, handed over 2026-10-14 evening (`E:\Bullshit Folder\Henry\Healthy People Are Ditching Healthcare Insurance and KEEPING COVERAGE (Here's How).mp4`, copied, original untouched); 1080p H.264, the YouTube timeline | 642 MB | the source of the cut (cut your section from it) |
| v2 | `work/sections/wrong-offset/LjT9OUGZ1q4_A.mkv`, `_B.mkv` | LOCAL derivatives of v1b (no download): stream copies 14:40-18:10 and 50:40-52:10, cut on the research's "YouTube ≈ RSS + 13 s" assumption. **WRONG SECTIONS:** transcribed (CPU) and found to hold RSS 12:57-16:27 and 45:25-46:55: the YouTube timeline runs **+163 s** vs the RSS at 15 min and **+316 s** at 46 min (the YouTube cut adds material the RSS lacks). Kept for the record with their words.json | 32 + 14 MB | superseded by v3 |
| v3 | `raw/LjT9OUGZ1q4_A.mkv`, `raw/LjT9OUGZ1q4_B.mkv` | LOCAL derivatives of v1b: keyframe-aligned stream copies ≈ 18:20 → 21:00 (the hook at ≈ 18:46, the question ≈ 19:22, the finger ≈ 20:03) and ≈ 55:40 → 58:00 (the cash button ≈ 56:23), audio padded to time zero | ≈ 25 + 22 MB | the two raw clips the EDL cuts from |
| m1 | `yt/assets/audio/ES_Mindscape - Lennon Hutton.wav` | Epidemic Sound recording 3c... → **4cb08b97-fa28-4f38-9b9c-3e71a2d98b5f "Mindscape"**, Lennon Hutton (dark, electronic, pulses, suspense; 108 bpm; 3:05; stems INSTRUMENTS / BASS / MELODY, no drum stem), `mcp__epidemic-sound__DownloadRecording` WAV FULL; not used in batch 2 (DOX, There Is Still Time, Thelema, She Knows) nor by another batch-3 job (grep 2026-10-14: All Gas No Breaks, Memories Of Old, Campaign, Type E) | pending | the bed for both looks (YT 13.6 LU under the voice, IG 13) |
| r1 | `yt/assets/broll/doc-goodbill-saline.png` | https://www.goodbill.com/hospital-price-of-saline (Goodbill's analysis of published hospital price files: a liter of saline listed at $26,667.03 at a Florida hospital, $6,837.65 Oklahoma, $1,031 Virginia), `workflows/page-record.mjs --full` still, no login | pending | DOC receipt under "I got charged $5,000 for a bag of saline": the real price files, not just his bill |
| r2 | `yt/assets/broll/doc-acep-ed-levels.png` | ACEP, "2023 AMA CPT documentation guideline changes for ED E/M codes 99281-99285" (acep.org newsroom, 2023-04-15) or the ACEP MDM grid PDF (acep.org/siteassets/.../acep-mdm-grid-june-2023.pdf): the five ED visit levels 99281 → 99285 (high MDM), `page-record.mjs --full` still | pending | DOC receipt + the annotation circle on level 5 under "there's five codes… the fours or the fives… critical life threatening" |
| r3 | `yt/assets/broll/doc-stat-cash.png` | https://www.statnews.com/2022/02/03/hospitals-cash-prices-for-services-offer-a-new-look-at-health-care-pricing/ (STAT, First Opinion, Jackson Williams, 2022-02-03: from hospital price disclosures, "the cash prices reported by hospitals is lower than the highest insurer-negotiated price 87% of the time; lower than most major insurers' negotiated prices 55% of the time"), `page-record.mjs --full` still | 3840x10880, done 19:33 | DOC receipt under Marty's button "the price gets cut by at least 50 %… half the time" (the receipt: lower than most insurers' rates 55 % of the time; his "50 %" stays his claim). Tried and BLOCKED first (nothing usable kept): Fierce Healthcare (403), PubMed 37011313 (403 to headless Chrome), carey.jhu.edu + axios.com + broad.msu.edu (Cloudflare / hCaptcha pages, never solved), trillianthealth.com (DNS) |
| r2b | (not captured) | ACEP MDM grid PDF | — | not needed: the ACEP newsroom page (r2) carries the 99281-99285 list |
| b01 | `yt/assets/broll/b01-iv-drip-pump.mp4` | Pexels (free licence) video 34263157 "hospital IV drip connected to infusion pump" https://www.pexels.com/video/34263157/ → the 2160x3840@29.97 file link in `work/pexels/saline_bag_portrait.json` | ≈ 30-60 MB | "they put me on an IV" |
| b02 | `yt/assets/broll/b02-saline-bag.mp4` | Pexels video 27128457 "close-up of an IV drip in a hospital setting" (an IV bag with its label) https://www.pexels.com/video/27128457/ → 1080x1920@60 (native vertical) | ≈ 10-30 MB | "I can buy that off of Amazon for $8 / the hospital can buy it for $2" (the bag itself) and the CHART's plate |
| b03 | `yt/assets/broll/b03-ambulance-911.mp4` | Pexels video 6520225 "video of a blue ambulance" (DIAL 911 side) https://www.pexels.com/video/6520225/ → 2160x3840@23.98 | ≈ 20-40 MB | "I've seen somebody go into the ER" |
| b04 | `yt/assets/broll/b04-hands-receipts-calculator.mp4` | Pexels video 7710751 "a woman putting notes on the receipt" (hands, a calculator, receipts) https://www.pexels.com/video/7710751/ → 2160x4096@25 | ≈ 30-60 MB | "80" (bills with errors), hands only |
| b05 | `yt/assets/broll/b05-cash-hands.mp4` | Pexels video 6624829 "person holding money" (hands exchanging US dollar bills) https://www.pexels.com/video/6624829/ → 2160x3840@29.97 | ≈ 20-40 MB | "you tell them you're paying in cash" |
| b06 | `yt/assets/broll/b06-pharmacy-counter.mp4` | Pexels video 8657615 "elderly woman buying a medicine" (paying at a pharmacy counter; a generic noun, not a named person) https://www.pexels.com/video/8657615/ → 2160x4096@25 | ≈ 30-60 MB | reserve for the cash beat (a counter, a card/cash hand-over) |
| b07 | `yt/assets/broll/b07-paramedic-hand-bandage.mp4` | Pexels video 6520252 "paramedic applying bandage on man's arm" (a hand injury bandaged in an ambulance; same shoot as b03) https://www.pexels.com/video/6520252/ → 2160x3840@23.98 | ≈ 30-50 MB | "go into the ER with a broken finger" |
| p0 | `work/pexels/thumbs/<id>.jpg` | Pexels search-result thumbnails (images.pexels.com w=320), ≤ 20 per search for ~12 searches (iv drip, saline bag, hospital bill, emergency room, finger splint, paying cash, broken finger, hand bandage, injured finger, finger cast, bandaged hand, emergency entrance) | ≈ 20-40 KB each | B-roll selection only |
