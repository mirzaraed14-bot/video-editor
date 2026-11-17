# BRIEF — Rise Above thumbnail gift (fentanyl & meth / arm episode)

## ▶ STATUS: resume here
- 2026-11-17 23:35 PKT (10:35 PST): **DONE, waiting on Affan's look.** Final: `outputs/riseabove-fentanyl-arm-thumb-mw-gold.png` (1280x720, 710 KB),
  copy at `X:/Claude Projects/Exports/riseabove-fentanyl-arm.thumbnail.png`; feed proof next to Kevin's: `outputs/feed-proof-vs-current.png`.
- Thursday 11-19 text for Affan to send (no price in it, see memory "no price to silent prospects"):
  "Hey Kevin, made you a thumbnail for the Tara Jane episode (My Arm Nearly Rotted Off). Run it in YouTube's Test & compare against yours and see which one wins."
- If Affan wants a change: edit `build/compose.py` params (`python -I build/compose.py <out> gold=E2A93A l1=... name=...`), re-run
  `build/feed_proof.py`, re-copy to Exports. Brighter gold E2A93A and darker B8862B were tried (`frames/gold_compare.png`).
- Nothing sent to Kevin. No paid credits. Premiere untouched. Nothing committed.

## What was built (2026-11-17)
- Frame: **57:01.75** of the episode (arm chapter 54:00-60:00), wide-eyed, lips parted, looking screen-left toward the text, so no
  mirroring. Chosen from a 1 fps face scan of 52:30-63:00 (`frames/faces_*.jpg`) then quarter-second full-res picks scored for
  sharpness (`frames/cand_sheet.jpg`, this one s224, among the sharpest). Face 305 px hairline-to-chin in the 1080p source, scaled
  1.2x Lanczos + light unsharp (366 px, MW ~395; 1.3x was tried, 1.2x kept: crisper face, MW proportions, her tattooed
  shoulder in frame for "MY ARM", `frames/scale_compare.png`); contrast x1.08, no other grade. Real frame only, no AI face work.
- Cutout: `hyperframes remove-background` (local matting, mask only) -> `frames/cut_3421_75.png`; hair edges checked at 100%
  on the new background. Plants and boom arm gone, her mic kept at the bottom as in MW. Review caught a 5-8 px band of
  leaf on the jaw edge kept by the matte: `compose.py` § 2a now drops leaf-coloured pixels in three source boxes (3,081 px).
- Layout measured off the MW reference: Anton (C:\Windows\Fonts) cap 147 px, pitch 158, left x65; gold rule + name cap 52;
  12 px gold border with 30 px inner radius, her hair and shoulder pop over it; gold halo around her silhouette; warm near-black
  background lifted behind her head. Colours: accent gold **#C8922C** (Affan: "deep gold"), background #120D08 -> #4A3618, type white.
- Text: **MY ARM / NEARLY / ROTTED.** (gold on ROTTED.), Kevin's own title words, literally true ("nearly"). Name line
  **TARA JANE WILLIAMS** as Kevin's description names her. Show mark = Kevin's real RISE ABOVE wordmark lifted from the
  episode's intro card (0:17.5), never M|W. Bottom-right left clear for the 1:16:23 badge.
- Re-read at delivery (2026-11-17 ~23:31 PKT / 10:31 PST): still 12K at ~21 h (yt-dlp: 12,736). Upload 2026-11-16 13:00 PST.

## Why
Onyx Influence gift for Kevin Lanning (Rise Above, 137K). Kevin posted our free death-row-guard Short (~15K, ~7x his other Shorts that day),
asked the price, Affan quoted $1,500/month, Kevin went quiet. Affan texts this thumbnail on **Thursday 11-19** as a second reason to follow up.
Affan on Kevin's current thumbnails: "horrendous".

## The episode
- **"I Shot Fentanyl & Meth Until My Arm Nearly Rotted Off"**, https://www.youtube.com/watch?v=FEBFdP5PiuI, 1:16:23.
- Read off the Videos tab (Chrome, text only) 2026-11-17 ~23:13 PKT: **12K views at ~21 h** (newest long-form).
- Comparison: median of the 29 other long-forms on the tab (1 day to ~5 weeks old) = **26K**; the last-2-weeks median = **20K**.
  At 21 h it is too young to call under-median. Re-read its views at delivery.
- Kevin's current thumbnail (feed grab from Affan): `reference/kevin-current-thumb-feed.png` (red "FENTANYL", her on the left, spoon + syringe).

## Format: Affan's pick (2026-11-17), replaces the 10-contender step
Affan's words: "this format of modern wisdom but the blue white color combo we exchange that for like deep gold and white combo so everything
that is blue we will turn it into goldish color like dark gold and text will be white and we will pick a moment from the actual episode of
like the freeze frame of this particular girl that he is interviewing and come as close as this modern wisdom thumbnail but for that
particular episode". Earlier the same evening: "get inspired from big podcasts like chris williamson and doac and others".
- Reference: `reference/mw-alex-oconnor-format.png` (Modern Wisdom, "WHY GOD IS HARD TO FIND." / Alex O'Connor).
- The MW anatomy: rounded accent border on the frame edge; dark background with an accent glow behind the guest; three lines of heavy
  condensed white caps on the left (Anton-like), ONE word in the accent colour, a full stop; a thin accent rule, then the guest's name in
  small white caps; the guest big on the right, head touching the top, mic in the foreground; the show mark top right.
- Colour swap: bright teal → saturated bright gold (border, accent word, rule); dark teal background → near-black warm brown; type white.

## Rules in force
- Real frames of the episode only. No AI-generated or AI-upscaled face; a soft frame gets Lanczos (+ light unsharp) only.
- Text 3-4 plain words, in the episode's own story terms, literally true ("nearly rotted off" is not "rotted off").
- Rise Above's mark in the logo slot, never M|W. Bottom-right kept clear for the duration badge.
- 1280x720, under 2 MB, copy in `X:\Claude Projects\Exports\`. Shown at feed size next to Kevin's current one before done.
- Work in silence (no playback), every opened tab closed, downloads only via `lock.sh youtube`, H.264.
