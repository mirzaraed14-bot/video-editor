# roofing-cash-you-hide: Onyx sample Short for Roofing Insights (Dmitry Lipinskiy) (batch 6)

## ▶ STATUS: resume here
- **2026-10-31 ≈20:45: BRIEF written (beats found by their words, catalog pass done); the cut is next.** Raw sections cut and
  transcribed (WhisperX large-v3 under `lock.sh gpu`, `work/transcribe.log`); words dumped in `work/cut/words_dump.txt`.
- Rules for this build (BUILDER-BRIEF + coordinator): NO Topaz, NO 60 fps: both looks render at the source's native **23.976 fps**
  (24000/1001) from the 1080p cut and the QA'd render is the final. GPU only for transcription, one job at a time under
  `bash projects/_onyx-batch2-2026-10/lock.sh gpu`. Captions run the whole video, under the hook too (CLAUDE.md Rules). One sonnet
  reviewer round. No YouTube requests (B-roll needs go to NEEDS-YOUTUBE.md). Work in silence.

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
  Justin/other, 74.74-91.26 Dmitry, 91.26-99.73 Justin, **99.73-103.23 Dmitry (a listening shot while JUSTIN says the button)**, 103.23- Justin.
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
6. BUTTON (Justin) "Who's going to buy that?" (93.42-94.36, the LAST of the two takes) … "if you did not show profit for 30 years,
   that was your pension" (99.81-102.81; "essentially" dropped). Speaker: Justin, although the show's camera is on Dmitry there: his
   speech runs on with no gap from "…sell in lump sums. But" (on Justin's camera), so it is the same voice; caption colour follows him.
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
  - **FX-71 Funnel Count**: "13" / COMPANIES on the hook line (his number) and "30" / YEARS on the button (his number).
  - **FX-79 Flash-Forward Echo**: the same tax return returns on the button, its flat profit line now labelled YOUR PENSION.
  - **FX-42 Kin Tag** (YT `tags` / IG credit): Justin Escajeda / Escajeda Holdings beside his face on his first answer.
- **Not used yet on this kind of video**: FX-35 (a blurred-figures document so no number is invented), FX-72 as a flat line that never
  rises (the absence drawn), FX-71 used twice as bookends (13 → 30).
- **Leaned on by the last ones, avoided here:** CrossExamined's FX-41 Year Ghost + inflating tag, Pollak's FX-27 quote card + FX-28
  dossier, Pincus's five read-along highlighters (FX-34), TCO's drawn backyard.

## What this one does better than the last ones (rule 5; CrossExamined / TCO / BP Money YT+IG, 2026-10-31)
1. **Two voices, cut as a real interview**: the host's questions in yellow on his own camera, the guest's answers in red on his, the
   whip only where the camera changes, so the Short plays as a conversation, not a monologue with cards.
2. **The document IS the argument and carries zero invented figures**: the return's numbers are blurred bars (FX-35), only the PROFIT
   line is sharp, and that line is what the story bends (edited, squeezed by personal costs, flat for 30 years).
3. **Bookended numbers**: the only two figures (13 companies, 30 years) land as the same FX-71 lockup at the top and the bottom.
4. IG: the 10-31 Mark Brazil type (small sans label over big bold sans, key words on a red box) with the return carried through the
   stage beats, as on CrossExamined, plus a two-camera conversation inside the window (each cam its own tracker).

## Sources (to be filled as they are pulled)
| Use | File | From |
|---|---|---|

## Download log (logged BEFORE each pull)
| # | File | Source | Size | Why |
|---|---|---|---|---|
| v1 | `source/2Tz8VrU84QI_0.00.30-0.01.30.mp4`, `source/2Tz8VrU84QI_0.43.30-0.48.00.mp4` | main session (YouTube 2Tz8VrU84QI, 1080p23.976 H.264) | 14 MB / 49 MB | the source (not pulled by me) |
