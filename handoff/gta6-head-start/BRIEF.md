# gta6-head-start · Affan Afterhours YouTube Short ("The Head Start", video 27's Short)

▶ STATUS: resume here (2026-11-06): **APPROVED BY HIM, FIRST DELIVERY, NO NOTES** -> `X:\Claude Projects\Exports\afterhours-gta6-head-start.final.mp4` (Version B, his button; 52.35 s). Full state, QA and the rebuild commands: RUN.md. **Cut from `work/cut/bursts.json`, never from WhisperX here:** WhisperX collapsed the restarts on the hook (40.80 vs 45.49), the Xbox line, the sprint line and "buy digital". The catalog pass below stands; the FX-70 ring on Nov 18 lived only in the ad-lib and went with it.

**Changes from the sequencing (said in the delivery note):** "Number one" opens on a giant pink 1 instead of a blank card; "retrain your thumbs" is the drawn controller, then sprint and handbrake are official footage (Lucia running, the sedan sliding) with a button chip, REPORTED · PREVIEW BUILD low; the reminder holds ~0.6 s after "days" under the card so it can be read; the receipt is cropped to the question and the two paragraphs (column-tight, so the whole phrase stays on screen). Captions: "THE ONES" (his s merges into "staring", both ASR passes write "one"), "MOVED TO X" (d elided, script says moved), "A BIG ONE".

## The ask (2026-11-05, verbatim)
"this is the short version You will be making this in the Scott Clary Youtube style and ask ... that particular session for some updates because I have updated its style set and everything and start again like a new session for this"
Session brief on top: fresh job, 9:16 1080x1920 even though the raw is horizontal; his own video, so the Scott STYLE and not the Scott identity (no branding, no watermark, no CTA); sequencing as text before any editing; code-built MP4 at native 59.94 into `X:\Claude Projects\Exports\`; nothing on C:, no phone encode; lean usage, no new agents without asking, builders Sonnet, never Fable; work in silence; ask before Higgsfield credits; don't edit shared kit files without saying so.

## Source
- Raw: `X:\Recordings\Afterhours\C1448.MP4` (copied, original untouched): 1920x1080 h264 59.94p, PCM stereo 48 kHz (the camera carries the voice on this shoot, both channels -25.6 dB mean, -3.3 dB peak), 177.18 s, recorded 2026-11-05 22:14. Room = Skool neon, red mic, leather chair; he reads off a screen to his side.
- Script: `X:\Claude Projects\GTA 6\video27-SHORT-head-start.md` ("The Head Start", 5 Nov). Long-form sibling: `video27-before-you-play-SCRIPT.md` (C1447, its own live session; don't touch `projects/c1447-provisional`).
- **Channel: Affan Afterhours (GTA)**, confirmed by the words and the script's home.
- **Post window (his script): Sat 7 to Mon 9 Nov, up before the pre-load opens** (Xbox 12am GMT on the 10th = Monday evening in the US).

## What he actually said vs the script
- Adds two on-lens asides to the USB beat: "a big one, obviously." and "That is if you value your time." (the script's self-named weakest beat now carries his comedy).
- "happens after launch" (script: "a month after launch").
- "Set a timer for 29 days" (script: "set this" + phone to the lens). **The phone-to-lens shot was NOT filmed.** A phone only shows at ~16-33 s, silent, while he prepares.
- **Ad-lib after the payoff, not in the script:** "And also, you don't have to buy the Ultimate Edition right now. You can buy the Standard Edition right now, wait for 18th because the reviews are going to come out and you can decide if it's even worth it to spend the extra 10, 20 dollars. That's something no one's talking about." (He restarts "because the reviews are starting" once; the last take is used.)
- Facts on the ad-lib (his own long-form fact table): Standard owners can buy the Ultimate upgrade any time = CONFIRMED (Rockstar Support); reviews on the 18th = REPORTED only ("reportedly"), he says it flat; prices Standard $79.99 / Ultimate $99.99 (CONFIRMED, his 26 Oct notes) = a $20 gap, he says "10, 20 dollars".

## Eye line (raw clock, Otsu +0.254, separation 2.92 SD = reliable, 40 % on the lens)
He looks at the lens exactly on the hook, the asides, the punch lines and the whole ad-lib; every fact is read. So the Short's rhythm is given: **facts under full-frame graphics, face on the punches.**
- camera: 5.25-6.75, 9.5-14.75, 31-32.25, 34.25-38.5, 39.5-48.75, 49.75-53.5, 56.25-58, 68-69.25, 75.25-77.5, 84.75-86, 90.75-93, 98.75-100.75, 114.25-118.25, 139.25-144, 146-165.25, 166.5-167.5, 170.25-172
- reading: 6.75-9.5, 14.75-31, 32.25-34.25, 38.5-39.5, 48.75-49.75, 53.5-56.25, 58-68, 69.25-75.25, 77.5-84.75, 86-90.75, 93-98.75, 100.75-114.25, 118.25-139.25, 144-146, 165.25-166.5, 167.5-170.25

## Style updates (from the Herjavec session + the files, 2026-11-05; H1 v2 approved as a whole only, no verdict on any single move)
POP grade + stronger sharpen on every render (`uv run workflows/grade-picture.py <job>`, then `python workflows/sharpen-picture.py <job> --mask 0.55 --sharp 0.40`, then `yt_build.py <job> <ver> --skip picture,overlay`; cards named mg-* are excluded). Drift 2.5 %/s on every face shot on top of the pops. YouTube-tight: every quiet run ≥ 0.08 s (10 ms RMS < -42 dBFS) cut to 0.07 s, also on the face; breaths (< -35 dBFS, ≥ 0.18 s) only strictly inside a piece; PROTECT spans for fast numerals; rerun the verbatim ASR after tightening. head_track on, head_lock only where the head jumps (`smooth_through()`, H1 `yt/build_spec.py` lines 160-174). Captions from frame 1 on the seam (y 1092), hook card BELOW them (y 1340 / 1436), one key word coloured. Pop keys `[[f0,1],[max(f0+2, word-4),1],[min(word+6, f1-1),1.10],[f1,1.10]]` (settle 1.08 on him, hair top ≥ ~160 px). Mix -12 LUFS, TP -2.0. Templates: `projects/_client-scott-clary/herjavec-500m-billion/yt/{build_spec.py,sound.py}`, `work/v2_build.sh`; 59.94 keys from `projects/gta6-all-fit-inside/yt/build_spec.py`.

## Catalog pass (CLAUDE.md § learning loop; all of CATALOG.md read, all 137 stills in `shots/` viewed on labelled sheets, 2026-11-05)
**The last video of this kind** (`gta6-all-fit-inside`, 4 Nov) leaned on: pink-swept DOC receipts, stacked storage bars, cam-top splits, count-ups, one map pin. **Rest here:** the sweep (a mark by hand instead), storage bars, count-ups, map pins.

**Moves that fit this video:**
| Move | Where | Why it fits |
|---|---|---|
| **Numbered stages** (Cleo Abram, UPGRADES queue) | a 1 · 2 · 3 · 4 strip through the list | it IS a list; visible progress is the cure for his pre-mortem's "checklist feel" |
| **FX-11 Rival Colour Split** | PS5 vs Xbox on "know your minute" | two brands, two times, his script's own console-war comment bait; PS blue vs Xbox green is the ONE place the palette opens |
| **FX-55 Red Pen Underline** | exactly one phrase on Rockstar's support page | the receipt is the turn; a hand mark replaces last time's sweep |
| **Running prop** (the hook's own bar) | stuck at 3 % at 0 s, fills on "while you sleep" | a small physical image that pays off; closest ref FX-73 Chart Reprise |
| **FX-41 Year Ghost, as a number** | a giant "29" on "set a timer for 29 days" | the one number the viewer must keep |
| **FX-33 Dust Void Drop** | the USB drive alone on black | one artifact, one sentence |
| **FX-70 Ring and Benchmark** | one stroke around Nov 18 | same grammar as the underline |

**Not used on this channel's Shorts yet:** Numbered stages, FX-11, FX-55 (hand-drawn), the running prop, FX-41.
**The new moves committed for this Short (≥ 2, rule 5 + UPGRADES.md):** (1) Numbered stages, (2) FX-11 Rival Colour Split, (3) the running bar. (FX-55 and FX-41 are extra; drop either if its check clip fails.) Each is a drawn MG with its own kill switch.

**Looked at and rejected:** FX-16 Portal Zoom through the phone (no phone shot, and the phone is the last beat, so there is no scene to travel into); FX-53 HUD Host Inset (over evidence he is READING, so the inset would show him reading); FX-13 Depth type (killed on seated close-ups, UPGRADES § Killed; head far over 35 % of the width); FX-08 Black Table Tiles and FX-54 Dark Headline Card (nothing to show in tiles; the support page itself is the stronger receipt); the map, CRT and archive families (no fit).

**What this one does better than the last (rule 5):** the POP grade and the tight-cut pass the last GTA Short did not have; a prop that pays off instead of a stat stack; progress visible on screen; the reading spans decide the shots from the start.

## Pick test + Bombas (Scott ENGINE; scored honestly; his pick stands; nothing written to Scott's files)
- Pick test **1 / 3**: (a) held belief ½ ("free month", "you must pre-load / buy Ultimate") · (b) famous face speaks it 0 (his own channel) · (c) a cost or reversal ½ ("free" that auto-renews).
- Bombas **6 / 11 = worse** (no B1, no B4, structural for a solo explainer): B2 ½ (money comes late) · B3 ✓ "free" reversed · B5 ½ · B6 ½ (drawn bar at frame 1, no real event) · B7 ✓ PS5 / Xbox / GTA / Rockstar · B8 ½ (his two asides) · B9 ✓ the bar, the 29-day timer · B10 ½ (one subject, a list) · B11 ½.

## Prediction (his script, 5 Nov, mirrored verbatim, do not edit)
- **YT Shorts 5K–150K, IG 10K–200K, TikTok 5K–120K.**
- **Biggest risk:** reads as utility.
- **Pre-mortem 5K:** checklist feel; the hook's split not clear by frame 1; monotone.
- **Pre-mortem 500K:** everyone has stared at a download bar; the Xbox console war; the payoff flips "free".

## Assets
- On disk: official footage `projects/gta6-pc-release/broll/`, `E:\Bullshit Folder\Henry\Grand Theft Auto VI Launch Trailer.mkv` (2160p30), smoothed clips `projects/gta6-all-fit-inside/yt/assets/broll/`, `projects/gta6-world-stops/assets/captures/preload.png`.
- NOT on disk (searched E:\Bullshit Folder, G:\My Drive\Range, GTA 6\screenshots, earlier jobs): PS5 settings / Game Library screens, a DualSense close-up, the GTA+ support capture, a download bar. Plan: page captures with `workflows/page-record.mjs --full` (Rockstar Support, PlayStation Support), drawn MGs with `workflows/mg-cards.py`. Send capture paths to the C1447 session if captured first (its job is now `gta6-complete-guide`; 2026-11-06 it has fetched nothing, reports his answer that no PS5 settings recordings exist, and is building menu-path graphics with no fake console screenshot, so the toggles here stay drawn too). Its countdown cards read 13 DAYS for its 6 Nov upload; this Short has no launch countdown, so that doesn't touch it.
- **Rockstar captures to reuse (2026-11-06, from the C1447 session; COPY out, never edit that folder):** `X:\Claude Projects\video-editor-client\video-editor\projects\gta6-complete-guide\assets\captures\`, 1920 wide at 2x, a .txt of the page text beside each PNG: `01-rockstar-gta-plus` (the auto-renew line), `02-rockstar-preorder-faq`, `03-rockstar-newswire-preload`, `04-rockstar-preload-faq` (Rest Mode / Sleep), `05-rockstar-editions` (Standard / Ultimate). Each still shows the viewport around its phrase; a different crop = `review/capture-page.mjs <url> <out.png> "<phrase>"` in that job folder. Still to capture if needed: the PlayStation Support Rest Mode page. Check each at full size before use.
- Sourced stills checked at full size; Higgsfield only with his OK.

## Sources used (official only)
| Use | File | From |
|---|---|---|
| "The ones playing" | EXT 755.0 s | GTA 6 Official Extended Gameplay (Rockstar) |
| Sprint | EXT 560.95 s at 0.8x, interpolated | same |
| Handbrake | EXT 923.7 s, interpolated | same |
| Night plates | EXT 1546.8 / 1547.4 s | same |
| "After launch" | Launch Trailer 81.5 s, the NOVEMBER 19, 2026 end card, cropped to the date | Rockstar, 15 Oct |
| Box covers (delete, USB cards) | `projects/gta6-all-fit-inside/yt/assets/covers/` | Rockstar cover art |
| Receipt | `projects/gta6-complete-guide/assets/captures/01-rockstar-gta-plus.png` (the C1447 session's capture, 2026-11-06) | Rockstar Support, GTA+ pre-order article |
| Drawn, never faked as captures | bar, toggles, delete prompt, USB, controller, phone | mg_head.py |
