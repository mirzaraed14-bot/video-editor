# roofing-cash-you-hide: Onyx sample Short for Roofing Insights (Dmitry Lipinskiy) (batch 6)

## ▶ STATUS: resume here
- **≈22:55: the BUTTON IS DMITRY (the host), verified by VOICE** (`work/cut/spk.py`, wespeaker cosine vs single-camera centroids: button
  99.80-102.88 = Dmitry 0.78 / Justin −0.10; "you may still have assets…" before it = Justin 0.87; control Dmitry span 0.89). SEQUENCING
  and my content read both said "guest": the show's camera (on Dmitry) was right. YT v5 = the last five chunks in Dmitry's yellow
  (`--skip picture,mix`, captions only), re-faded and recopied (`…sample-yt.final.mp4` = Exports, md5 380406…); IG unchanged (no voice
  colours). The pension card stays as the closing image over his line.
- **2026-10-31 ≈22:45: FINALS DELIVERED, awaiting the main session / Affan's review.** `outputs/roofing-cash-you-hide.sample-yt.final.mp4`
  (= YT v4) and `.sample-ig.final.mp4` (= IG v6), copies `X:\Claude Projects\Exports
oofing-cash-you-hide.yt.final.mp4` / `.ig.final.mp4`
  (md5-identical), proof sheets `outputs/…sample-yt.proof-sheet.jpg` / `…sample-ig.proof-sheet.jpg` (+ Exports copies). Both: H.264
  1080x1920 23.976 fps, 797 f, 33.24 s (ends 0.09 s after "pension", a 70 ms audio fade on the tail), AAC 256k, −12.4 LUFS, peak −2.2;
  swishes −21 dB vs the voice beside each (`yt/cue_check.py`, `ig/cue_check.py` PASS subtle). After QA r1: IG v5 linear stage push (no
  near-static stage frames), the SALE PRICE drop clear of the bug; v6 the pension stage's axis label dropped (it crowded the caption).
  OPEN for Affan: the hook title "WHAT A BUYER / CHECKS FIRST" (buyer's side, no tax wording, his pick to change); "manufacturing" captioned
  as spoken (SEQUENCING guessed "manipulating"); the "like" in "If someone, like, never" stays in the audio (uncuttable); IG captions run
  under the hook (CLAUDE.md Rules) vs his War Dogs "no captions while the hook is up" (open since CrossExamined).
- **2026-10-31 ≈22:10: QA r1 (one sonnet reviewer, defects only; scratch `work/review/`) FIXED, finals rendering** (YT v4 = `yt_build.py
  ... v4`; IG = `bash ig/run.sh build.py` then `bash ig/run.sh sound.py --mux` → `outputs/…sample-ig.v4.mp4`). Then: a 60 ms audio fade
  on the last frames of each final (r1 #16: 87 ms of hiss after "pension" stopped hard), copies to outputs/…final + Exports, proof sheets.
  **Fixed:** (1 HIGH) row numerals 1-8 on the tax return (digits that are not his) → removed (`work/gfx.py`); (2) YT documents in the top
  200 px band → the return / P&L at y 243-1037 (scale 0.64 / 0.72), the split's rows fade out above the bottom 300 px band (LOWFADE);
  (3) IG documents under the ROOFING INSIGHTS bug → smaller, left of it; (6) "AND YOU'RE" / "MADE" chunks held 4-5 frames → re-chunked
  ("AND YOU'RE KEEPING" / "CASH", "WHAT YOU WOULD" / "HAVE MADE"); (10) IG stages froze (20 identical frames) → every stage object
  pushes in 5 %; (12) IG caption swaps left one blank frame → a new line is ~30 % up on its first frame; (16) the end fade.
  **Kept by design (reported, not defects of the rules):** Dmitry's payoff chunks wipe white → yellow (README § 5: another voice's
  emphasis chunks wipe white → colour); chunks pinned to joints lead by 0-2 frames (kit joint pin, as CrossExamined); head steps 16-18 px
  at two Justin joints (under the 25 px snap bar); real $100 bills in the cash B-roll carry their own printed numbers; head/cap tops in the
  top band on face shots (faces whole); IG light-leak burns wash the captions for 1-2 frames; 2-3 frame J-cuts where the source camera
  changes before the speaker does; SFX 14.7-22.8 dB under the voice peak by the reviewer's fit (cue_check: every cue -21 dB full band,
  the 19-23 band; the hook swish sits in Patrón's 14-16 peak range).
- **2026-10-31 ≈21:20: YT v2 + IG v1 rendering; then ONE sonnet reviewer, fixes, finals.** Cut DONE: `outputs/roofing-cash-you-hide.mp4`
  (797 f @ 23.976 = 33.24 s; 25 segments, all pinned; `work/cut/make_edl.py` → splice.sh with AMPLIFY_DB=10 (2 dB under the measured 12:
  limiter pressure); audio-qa: timeline exact, 24 joints clean, limiter transparent). RUN `python work/cut/patch_transcript.py` AFTER
  EVERY SPLICE. Verbatim faster-whisper on the cut (`work/cut/fw_cut_v2.txt`) reads every approved beat; plain pass drops the very
  first "You" (ASR start artifact: the same audio joined to its next piece reads "You own" both ways, `fw_join_r3.txt`).
- Cut findings: (1) **"manufacturing" is what he says** (large-v3 slice + join, with and without a neutral prompt: all "manufacturing");
  (2) "what ARE your tax returns say" (WhisperX, medium.en, small.en; large-v3 alone hears "do"); (3) "isn't THAT" kept per the beat
  (3 decodes "that", 3 "it": a tie); (4) WhisperX hid a stumble "and you're- and you're hiding- and you're keeping cash": the LAST take
  kept (raw 60.46), "hiding" out; (5) "If someone, like, never": the "like" runs inside the voicing of "someone" (no clean cut, both
  cut attempts still read "like"): kept in the audio, not captioned; (6) the tight pause pass protects fricatives (a first pass clipped
  the /s/ of "say", the /th/ of "thirty", the /sh/ of "showed": `make_edl.py` HF-share guard).
- YT: `yt/build_spec.py` (14 shots, 48 chunks, 13 swishes, head lock at the in-shot joints), `yt/cards.py` + `work/gfx.py` (7 built
  cards), `yt/sound.py` (3 slices). v1 → v2: bars + "30" out of the top 200 px band, flat chart inside the split panel's safe rows, every
  swish re-levelled to −21 dB vs the voice (v1 cue_check −16.8..−24.2). Head gate on v1 (`work/headgate.py`): no snaps (343's 110 px =
  YuNet noise on the cap: frames checked, `work/snap343.jpg`).
- IG: `ig/build.py` (CrossExamined kit, two tracked cams, the same objects), check frames `ig/work/check_sheet.jpg`; lips gap ≥ 26 px.
- Rules for this build (BUILDER-BRIEF + coordinator): NO Topaz, NO 60 fps: both looks render at the source's native **23.976 fps**
  (24000/1001) from the 1080p cut and the QA'd render is the final. GPU only for transcription, one job at a time under
  `bash projects/_onyx-batch2-2026-10/lock.sh gpu`. Captions run the whole video, under the hook too (CLAUDE.md Rules). One sonnet
  reviewer round. No YouTube requests (no B-roll needed from YouTube: no NEEDS-YOUTUBE.md). Work in silence.

## The job
- Show: **Roofing Insights** (Dmitry Lipinskiy; roofing / construction business interviews; ~15-person in-house media team; handoff:
  "YES on money, NO on need"). Approved pick (SEQUENCING.md "Roofing Insights v3"): **"Why the cash you hide from taxes is money you'll
  never sell your business for"** (VALUE; the viewer gets: a buyer pays on your tax returns, so every dollar you hid is a dollar you'll
  never sell for). Episode "He Owns 13 Companies But His Name Isn't on Any of Them" (YouTube 2Tz8VrU84QI, 1080p23.976, in-person
  studio kitchen set, 3 cameras: a wide two-shot, Dmitry's close-up, Justin's close-up).
- Guest credit from the show's own burned-in lower third (hook_section ≈ 4-12 s, read on a full-size frame, `work/lowerthird.png`):
  **Justin Escajeda / Escajeda Holdings**; host **Dmitry Lipinskiy / Roofing Insights**.
- Sources (pulled by the main session): `source/2Tz8VrU84QI_0.00.30-0.01.30.mp4` (t0 = YouTube 0:00:30) and
  `source/2Tz8VrU84QI_0.43.30-0.48.00.mp4` (t0 = YouTube 0:43:30); both H.264 1920x1080 24000/1001, AAC, start_time 0 on both streams.
- Raw sections (frame-exact seeks on k x 1001/24000, x264 CRF 12, PCM; both streams start at 0, 815 / 2565 frames):
  `raw/hook_section.mkv` = source1 16.016-50.008 (**raw t = YouTube t − 46.016**), `raw/main_section.mkv` = source2 95.012-201.993
  (**raw t = YouTube t − 2705.012**).
- Camera map (scene cuts > 0.25): hook_section 0-2.25 show logo sting, 2.29-14.43 wide (burned-in lower thirds), 14.43-19.23 Dmitry,
  19.23-26.90 wide (a subscribe pill bottom-left), 26.90-31.74 Dmitry, 31.74- Justin. main_section 0-2.25 Justin, 2.25-13.72 Dmitry,
  13.72-33.24 Justin, 33.24-36.25 Dmitry, 36.25-57.22 Justin, **57.22-69.74 WIDE** (no usable face: covered by cards), 69.74-74.74
  Justin/other, 74.74-91.26 Dmitry, 91.26-99.73 Justin, **99.73-103.23 Dmitry (he says the button: verified by voice)**, 103.23- Justin.
- Deliver: `outputs/roofing-cash-you-hide.sample-yt.final.mp4` / `.sample-ig.final.mp4`, copies
  `X:\Claude Projects\Exports\roofing-cash-you-hide.yt.final.mp4` / `.ig.final.mp4`, a proof sheet each.

## The beats (followed exactly; found by their WORDS; raw seconds from WhisperX, edges to be measured on the envelope)
1. HOOK (Dmitry, re-ordered): "You own 13 companies." (hook 16.75-17.91; the earlier "you bought 13 companies," dropped per the beat)
   … "So when someone calls you to buy their business, [because now you're known for it in the area,] what are you looking for?"
   (main 3.04-6.11 + 8.19-8.91; the beat's "…" = the bracketed words out; "Are you looking for revenue, people, brand?" after it out)
2. (Justin) "what are your tax returns say?" (18.52-19.88) … "You always get the story like," (26.16-27.20, the LAST of the two
   takes) … "my taxes say this, but I've done this much in cash." (28.36-32.31; "you know," before it out)
3. (Dmitry) "But isn't that because people try not to pay tax?" (33.19-36.33; the camera cuts to Dmitry at 33.242) / (Justin) "100
   percent. But here's the problem." (37.77-39.57; "And yeah, right. Like" before it out; the repeat "Here's the problem, though." out)
4. (Justin) "If you have been [manufacturing] your tax returns" (49.35-51.94; "for the last X amount of years" out) … "and you're baking
   personal costs into your profit and loss statements," (54.38-58.40) … "And you're keeping cash," (59.48-61.56) … "you've probably
   already spent what you would have made on the sale" (63.48-66.16; each "you know what I mean?" out; cut before "over the years
   because your valuation's gonna be dog shit")
5. (Dmitry) "If someone never showed profit, what does it really mean?" (86.62-91.05; "Explain that one more time." out)
6. BUTTON (Justin) "Who's going to buy that?" (93.42-94.36, the LAST of the two takes) … (DMITRY, by voice) "if you did not show profit
   for 30 years, that was your pension" (99.81-102.81; "essentially" dropped). The sequencing called it the guest's; the voice check says
   the host sums it up (he cuts in on "But" with no gap, and the show's camera is on him): yellow captions.
Loop: "…that was your pension." → "You own 13 companies." (the stakes, then the man who buys them).

## Decisions (with reasons)
- **Facts on screen (GATE 5, a tax / money claim):** only his words. The only numerals on screen are **13** (companies, the host's),
  **100 percent** (captions only) and **30 years**. No figures on any tax return, P&L or price tag (not even "$0" for "never showed
  profit": a line that stays flat says it without a number). No advice card of our own; nothing that reads as "evade taxes"; the hook
  title is the BUYER's side.
- **"manufacturing" vs "manipulating"**: captioned as the models hear it on a verbatim pass with and without a neutral prompt (neither
  word in the prompt); flagged here if they disagree.
- **Captions: colour = voice.** Justin (the answer, main voice) white → red wipe on payoff chunks; Dmitry (the host's questions) yellow.
- **No music bed; SFX = soft Patrón-family swishes only**, one per graphic entrance, sized to the move; cuts back to a face, text swaps,
  stamps and marks silent (memory feedback-premium-sfx SUPERHERO + UNDER HIS MUSIC). A fresh Epidemic set, rejected by title first,
  then tonal p90 ≤ ~13.
- 23.976 fps native, no Topaz (Affan 18:30).

## Catalog pass (2026-10-31; CATALOG.md FX-01..81 read in full; all 137 stills of `research/effects-catalog/shots/` LOOKED AT on labelled
## tiled sheets: 79 singles at 427 px in 4 sheets, 58 strips at 1500 px wide in 6 sheets, every tile read)
- **Fits this story** (a buyer's due-diligence lesson told in documents, two spoken numbers, no public receipt):
  - **FX-33 Dust Void Drop**: the business's TAX RETURN isolated on a dark dusty field, dealt on "tax returns" (the one object).
  - **FX-35 Blur-Isolate Row**: the return's figures are BLURRED bars (no numerals) with the ONE line that matters, PROFIT, sharp.
  - **FX-55 Red Pen Underline**: one red mark per document: the red pen working over the return on "manufacturing your tax returns".
  - **FX-69 Lone Yellow Bar**: "my taxes say this" vs "this much in cash" as two plain bars, one accent (no numbers, his "this").
  - **FX-72 Win-Prob Lifeline**: the PROFIT line drawn across the years and staying flat on "never showed profit" (no axis numbers).
  - **FX-71 Funnel Count**: "30" / YEARS on the button (his number; the hook's "13" stays in the captions: frame 0 carries the hook title).
  - **FX-79 Flash-Forward Echo**: the same tax return returns on the button, its flat profit line now labelled YOUR PENSION.
  - **FX-42 Kin Tag** (YT `tags` / IG credit): Justin Escajeda / Escajeda Holdings beside his face on his first answer.
- **Not used yet on this kind of video**: FX-35 (a blurred-figures document so no number is invented), FX-72 as a flat line that never
  rises (the absence drawn).
- **Leaned on by the last ones, avoided here:** CrossExamined's FX-41 Year Ghost + inflating tag, Pollak's FX-27 quote card + FX-28
  dossier, Pincus's five read-along highlighters (FX-34), TCO's drawn backyard.

## What this one does better than the last ones (rule 5; CrossExamined / TCO / BP Money YT+IG, 2026-10-31)
1. **Two voices, cut as a real interview**: the host's questions in yellow on his own camera, the guest's answers in red on his, the
   whip only where the camera changes, so the Short plays as a conversation, not a monologue with cards.
2. **The document IS the argument and carries zero invented figures**: the return's numbers are blurred bars (FX-35), only the PROFIT
   line is sharp, and that line is what the story bends (edited, squeezed by personal costs, flat for 30 years).
3. **Only his figures**: 13 (captions) and 30 YEARS (FX-71 on the button); every amount field on screen is a blurred bar.
4. IG: the 10-31 Mark Brazil type (small sans label over big bold sans, key words on a red box) with the return carried through the
   stage beats, as on CrossExamined, plus a two-camera conversation inside the window (each cam its own tracker).

## Sources (yt/assets/broll; the IG reads the same files)
| Use | File | From |
|---|---|---|
| "So when someone calls you to buy their business" — a man on a desk phone (FIT float frame: 720p, never blown up; src_in 4.0) | b-phone-23073.mp4 (1280x720 25 fps) | Mixkit 23073 (free licence; 1080 answers 403) |
| "And you're keeping cash" — hands counting a wad of $100 bills (no face; src_in 1.0) | b-cash-18296.mp4 (1920x1080 24 fps) | Mixkit 18296 (free licence) |
| the tax return, the P&L, the bars, the SALE PRICE tag, the PROFIT line | mg-ret / mg-bars / mg-edit / mg-pnl / mg-sale / mg-flat / mg-pension.mp4 | built: `yt/cards.py` + `work/gfx.py` (LibreBaskerville, IBM Plex Mono, Anton) |
| Swishes | assets/sfx/epidemic/rf-deep-drawer, rf-low, rf-wind-soft04 (sliced by `yt/sound.py`; rf-lowmid-thick tonal 15.0 and rf-cloth-fast04 15 % above 6 kHz: pulled, NOT used) | Epidemic (Download log x1-x5) |

## Download log (logged BEFORE each pull)
| # | File | Source | Size | Why |
|---|---|---|---|---|
| v1 | `source/2Tz8VrU84QI_0.00.30-0.01.30.mp4`, `source/2Tz8VrU84QI_0.43.30-0.48.00.mp4` | main session (YouTube 2Tz8VrU84QI, 1080p23.976 H.264) | 14 MB / 49 MB | the source (not pulled by me) |
| m-list | `work/img/mk_<tag>.html` (listing pages: phone-call, money, cash; phone-ringing + counting-money came back empty) — logged after the pull (missed before it) | mixkit.co/free-stock-video/<tag>/ | ≈ 0.2 MB each | find faceless phone + cash clip ids |
| m-prev | `work/img/mixkit/<id>-360.mp4` (previews: 23073 100880 309 18296 18304 23524) | assets.mixkit.co/videos/<id>/<id>-360.mp4 (Mixkit free licence) | ≈ 1-3 MB each | pick a faceless 'someone calls you' phone shot and a 'keeping cash' hands-and-bills shot |
| m1-m2 | `yt/assets/broll/b-phone-23073.mp4` (720p: its 1080 answers 403), `yt/assets/broll/b-cash-18296.mp4` (1080p) | assets.mixkit.co/videos/<id>/<id>-<720/1080>.mp4 (Mixkit free licence) | ≈ 5-25 MB each | 'someone calls you to buy their business' (a man on a desk phone) and 'you're keeping cash' (hands counting a wad of bills, no face) |
| x1-x5 | `assets/sfx/epidemic/rf-*.wav` (repo library) | Epidemic Sound SFX, `DownloadSoundEffect` WAV, none used before (MANIFEST + every BRIEF / sound script grepped 2026-10-31; today's builders took cx-*, tco-*, ph-*, pi-*, dc-*, bp's 287d8894 e8991406 1c9e4e2b 5a77c212, Drinkin' Bros 460b3ae4): 8de00d12 "Swooshes, Whoosh, Short, Deep Drawer, Dry" · 171dc5c9 "Swooshes, Whoosh, Low" · f10a8c2a "Swooshes, Whoosh, Organic, Wind, Soft, Normal 04" · 98cc6869 "Swooshes, Whoosh, Short, Low Mid, Thick, Dry" · 4e9f7218 "Cloth, Movement, Fast 04" | ≈ 0.2-0.6 MB each | the Patrón-family soft swishes, one per graphic entrance, sized to the move |
