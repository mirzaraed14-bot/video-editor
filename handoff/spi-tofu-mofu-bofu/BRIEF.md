# spi-tofu-mofu-bofu: Onyx sample Short for Smart Passive Income (Pat Flynn) (batch 6, ENHANCE mode)

## ▶ STATUS: resume here
- **2026-11-02 ≈17:05: FINALS DELIVERED (v3), awaiting main / Affan's review.** Finals (md5-identical copies): `outputs/spi-tofu-mofu-bofu.
  sample-yt.final.mp4` = Exports `spi-tofu-mofu-bofu.yt.final.mp4` (118.1 MiB, md5 4a82a96f) and `…sample-ig.final.mp4` = Exports
  `.ig.final.mp4` (67.5 MiB, md5 22a06115); phone copy Exports `spi-tofu-mofu-bofu.yt.phone.mp4` (26.8 MiB); proof sheets in outputs +
  Exports. Both: H.264 1080x1920 30 fps, 1920 f = 64.00 s, AAC 256k; **YT −14.0 LUFS / −1.7 dBTP, IG −14.0 LUFS / −2.2 dBTP** (theirs
  −15.4 LUFS); voice constant (static chain), YT bed 8 LU under, 30 cues at −19/−20 dB vs the voice (cue_check). Finalize = `python
  work/finalize.py <yt render> <ig render>` (70 ms tail fade, atomic copies, YT phone copy at 3.3 Mb/s). One sonnet QA round (r1, below),
  HIGH/MED fixed and self-verified on frames (`work/review/v3_fixes.jpg`); no second round (main's lean mode, 16:58).
  OPEN for Affan: the sponsor read of their paid ManyChat integration is out (ManyChat stays named + shown); watermark PAT FLYNN vs SMART
  PASSIVE INCOME (main chose PAT FLYNN); the YT credential tag is fully legible ~1.9 s (6.33-9.08 s, the kit's animated tag); the 4 low
  "L" whooshes are quiet in the phone band (−22..−25 dB) by design (weight under the hero moves).
- **2026-11-02 ≈16:50: v3 building (QA r1 fixes + main's loudness call); then finals.** v1 (15:58) self-checked → v2 (16:20: AUTOMATE
  stage dark glass, the TOFU word steps aside under the big ManyChat mark, the IG's first light-leak moved out of the hook, every SFX cue
  trimmed to −20 dB (S/M) / −19 dB (L) vs the voice beside it) → **QA r1** (one sonnet reviewer, defects only, `work/review/r1/`):
  FIXED in v3: (HIGH) IG empty window frames on the first frame of three float cards (471, 636, 1651) → cards open ~40 % in; (HIGH) YT
  "BOTTOM" micro-label past x 1020 on the broken-path MG → TOP/BOTTOM labels dropped; (MED) YT head jump at the split → face cut 1470 →
  a whip (a layout change), A → A stays a plain cut; (MED) a 36 px head step at the joint 566 inside his face → "who will benefit from
  that" is now the same theater later, FILLED with people (s08b, src 8.0 s; contrast with "nobody's listening"); (MED, IG) a 26 px step at
  joint 255 → the IG creator card enters ON 255 (the IG credential runs 6.33-8.5 s); (LOW) the phone bezel and the pour dots touched the
  top 200 px → moved down; (LOW-MED) his lip touched the caption on "For what?" (zoom 1.08 → 1.05) and in s22 (eye line 0.32 → 0.285).
  KEPT by design: the PAT FLYNN watermark on every frame at y 1185 (the look's rule; main's call 1); the bed averages 8 LU under the voice
  and only exceeds it inside pauses (400 ms windows); the YT joint 255 steps 18 px sideways (under the 25 px precedent, Roofing r1); IG
  red hero words wash out during the 3 light-leak burns (by the look's design, ~8 frames each).
- **Main's loudness call (16:45): master both looks to −14.0 LUFS integrated, true peak ≤ −1.5 dBTP** (theirs measures −15.4 LUFS: ours
  must never play quieter), one static gain into the limiter, every relative level kept (voice constant, bed ≈ 8 LU under, SFX offsets);
  the −6 dBFS peak rule is about keeping the voice constant (the cut's static chain), not a master ceiling.
- **2026-11-02 ≈15:45: cut LOCKED, MGs rendering, YT + IG builds next.** Cut `outputs/spi-tofu-mofu-bofu.mp4` = 1920 f @ 30 = 64.00 s
  (`work/cut/make_edl.py` → splice.sh, AMPLIFY 0 dB measured; 31 segments; audio-qa: timeline exact, 30 joints clean; two −10/−11 dB
  "ambience" dips at pauses over a −45 dB room tone, accepted). Verbatim faster-whisper large-v3 on the cut, prompt + plain
  (`work/cut/fw_cut_v8.txt`): every word as sequenced; the plain long decode alone hears "robot and And nobody" (every short decode,
  medium.en and small.en hear ONE "and": a decoder artifact). RUN `python work/cut/patch_transcript.py` AFTER EVERY SPLICE ("But" added,
  "the no" → "but no"). Fixes found on the way: "is- is the creator" (start 10.600), his false start "Not if-" (cut), "You shouldn't scale
  everything." restored (without it ASR heard "SKILLS"), the inhale 72.83-73.31 forced out, their gate's digital silence kept off joints.
- YT: `yt/build_spec.py` (25 shots, 115 chunks, 29 cues, head lock [255, 566, 1651], A z0 1.16 / eye line 0.32: lips ~70 px over the
  caption top), MGs `work/gfx.py` + `work/mg.py` (13 states of ONE funnel; params `work/mg.params.json` written by build_spec),
  SFX `yt/sound.py` (12 fresh takes), bed `yt/assets/audio/bed-laundry-list.wav` (offset so its own ending lands on the last frame).
  Run: `bash work/run.sh work/mg.py work/mg.params.json [names] --variant yt|panel|ig` (OpenCV via uv), `python yt/build_spec.py`,
  `python presets/.../kit/yt_build.py projects/spi-tofu-mofu-bofu v1` (under the GPU lock).
- IG: `ig/build.py` (the Roofing IG kit helpers + SPI plan; MGs as stage clips `ig/assets/mg-*-ig.mp4`), `bash work/run.sh ig/build.py`.
- ManyChat: their site answered a Cloudflare bot check (no capture; nothing touched) and Bing via curl is junk, so the REAL wordmark is
  keyed from their own Short (raw 52.9-54.9 s, white on his shirt) → `assets/manychat-wordmark.png`; the comment → DM flow is a built
  skeleton UI (no invented copy). His "post" on the phone = a frame of this video (`work/img/post.png`, cut frame 1530).
- Rules: 30 fps native, NO Topaz; GPU jobs under `bash projects/_onyx-batch2-2026-10/lock.sh gpu`; no YouTube; silence; voice peaks −6 dBFS.

## The job
- Show: **Smart Passive Income / Pat Flynn** (tracker row "Smart Passive Income (Pat Flynn)", channel @patflynn, 485K, replied Yes
  2026-10-13; PICKS.md: Pat sold SPI to Liz Wilcox, so on screen he is the FOUNDER, never "owner"/"CEO").
- Their Short: "Do you know about TOFU, BOFU and MOFU?" (`gLydjgO_q6s`, 124.33 s, 1080x1920 30 fps H.264, AAC 44.1 k), 1.7K views.
  A native vertical selfie: Pat close to his phone (plants + bookshelves behind), handheld, ~35 jump cuts. It is a **paid ManyChat
  integration** ("that's where a tool like ManyChat can really save your butt", "official Meta business partner", "Check out ManyChat.
  Thanks, ManyChat.").
- **Burned-in text, every frame scanned** (`work/textscan.py` → `work/textscan.json`: near-white low-saturation pixels per frame, per
  sixth of the height): exactly TWO overlays: the white **TOFU / MOFU / BOFU** stack **f44-f223 (1.467-7.467 s)**, over his whole face,
  ending on their jump cut at f224; and the white **"Manychat"** wordmark **f1572-f1656 (52.40-55.20 s)**, low (y ≈ 1280-1600). Every other
  white run (38-43, 50-51, 68.6, 85.4, 117 s; peaks 400-850 px at 1/16 size) is in the bottom sixth = the print on his T-shirt (checked
  on a full-size frame, `work/sheets/shirt_38.jpg`). 1 fps sheets: `work/sheets/ref_1fps_0..3.jpg`.
  → No face shot or SPLIT top may show raw 1.467-7.467 or 52.40-55.20 in either look: both spans are covered by our own graphics.
- Their own hard cuts inside spans we keep (ydif > 30): raw 62.27-62.33, 85.15-85.30 (inside the button: a shot edge sits on it).
- Their audio: −15.4 LUFS, LRA 4.3; no music bed (pauses are digital silence or a −45..−55 dB room tone with a steady 118 Hz hum).

## Teardown: their Short → ours (Affan's talking points)
| | Theirs (gLydjgO_q6s) | Ours | Better because |
|---|---|---|---|
| Hook, first 3 s | "Question, have you ever heard of TOFU, MOFU, and BOFU?" over his face; from 1.5 s a static white TOFU / MOFU / BOFU stack covers his face for 6 s | First word on frame 0 ("Have you ever…"; "Question," cut), his face for 0.87 s with the captions only (claim only), then from "TOFU" a drawn funnel whose three tiers drop in on each acronym | The odd words become a picture the viewer understands in 3 s, and the face is never buried under text |
| Stranger by 5 s: who / what / why | Who: nothing on screen. What: the acronyms, defined only by voice | What: the funnel labelled TOP / MIDDLE / BOTTOM OF FUNNEL by ~6 s. Who: only the PAT FLYNN watermark inside 5 s; his credential (FOUNDER OF / SMART PASSIVE INCOME) lands low on his face at 6.3 s, legible from ~7.1 s (main's call 3: no credential under the hook). Why: "nobody's listening" / the missing middle by ~25 s | What and why are on screen; who arrives on his first clean face after the hook |
| Captions | None (two burned labels only) | Word-synced captions, white + coloured emphasis, ! ? only, one constant line | Most Shorts are watched muted |
| Pacing | 2:04; 44 pauses ≥ 0.3 s = 23.7 s of silence; false starts ("is- is", "an an", "really really", "Not if-"); an ad-revenue aside; a "focus on content / DMs" detour | 64.0 s; every pause cut YouTube-tight; stumbles and asides out; the same point in the same words | Half the length, same lesson |
| Visuals per beat | One handheld selfie for 124 s + 2 text labels | ~13 states of ONE built funnel (built, top only, bottom only, middle pulled + red ring, people pouring and leaking, path broken, glue back, the real ManyChat mark in it, comment → DM on a phone, automated replies, AUTOMATE everything struck, complete) + 6 real clips (a creator's camera, packing an order, a man screaming, the theater full and empty, a robot); face never > 4 s bare | Every idea is shown, not just said |
| Ending / button | Sponsor read ("Check out ManyChat. Thanks, ManyChat.") + "I hope this was helpful" | Ends on the move: "Automate the middle, the glue, the connector between the people who are finding you to what you then have to offer", over the completed funnel; loops into "Have you ever heard of TOFU…" | The viewer leaves with the one thing to do |
| Sound | Phone audio, −15.4 LUFS, gated silences (digital silence in its pauses), no music | Voice held constant (static chain, peaks limited at −6 dBFS in the cut), master −14 LUFS (louder than theirs); YT: a lo-fi bed 8 LU under the voice; 30 soft cues from 12 fresh Epidemic takes, each sized to its move, −19/−20 dB under the voice | Polished, consistent, never quieter than theirs |

## Sequencing (sent to main 2026-11-02 ≈14:25; all words verbatim, raw seconds of `raw/spi-tofu.mkv`; one speaker: Pat)
1. **HOOK** (0.40-4.55) "Have you ever heard of TOFU, MOFU, and BOFU?" ("Question," cut)
2. **WHAT IT IS** (4.68-7.95) "These are acronyms for top of funnel, middle of funnel, and bottom of funnel."
3. **TOFU = the creator** (10.32-17.76) "The creator will usually start top of funnel. You're creating content, you're building an audience.
   For what? You don't know necessarily what the product or service is." ("And what a lot of creators and entrepreneurs do is- is" and
   "right?" cut; the ad-revenue / "business plan for a creator" aside 18.0-25.4 cut)
4. **BOFU = the entrepreneur** (26.04 + 27.02-27.66, 33.32-42.82) "But an entrepreneur, they're usually starting at the bottom of the
   funnel. Here's the thing that I can serve you with. Now I need to find the people who will benefit from that. And you're screaming at
   the top of your lungs and nobody's listening. And that's a big problem." (the stumbled first "an" and "one who thinks of solutions
   … digital or physical" cut)
5. **THE MISSING MIDDLE** (43.18-50.10) "But what's also a problem is if you have top of funnel and bottom of funnel, but no middle of funnel.
   The MOFU." ("right?" cut)
6. **THE LEAK** (54.64-62.06) "A lot of people will get a lot of audience, and then you're not following through. You're not connecting
   with those people. There's no way to get them from the top to the bottom." ("that's where a tool like ManyChat can really really save
   your butt because" and the first "a lot" cut; ManyChat is named in beat 7)
7. **THE FIX** (62.36-77.12, then 111.82-114.34) "What you need is the glue in the middle. And that glue in the middle could be something like
   ManyChat to help you build those systems so that when people come from the top, maybe you're asking them to leave a comment, or
   they're DMing you already, and you can have these systems in place, this automation to follow up with them. The fortune is in the
   follow-up. … When I implemented that in my business, it changed everything." (the misspoken "on a DM" and "as I say" cut)
8. **NOT EVERYTHING** (77.92-80.04, then 100.60-105.12) "And I'm not telling you to automate your entire business. … A person who scales
   everything just creates a robot, and nobody wants that anymore." (re-ordered up; "When you automate that middle part… one-on-one basis"
   and "You shouldn't scale everything" cut)
9. **BUTTON = the move** (80.98-86.40) "Automate the middle, the glue, the connector between the people who are finding you to what you then
   have to offer." Loop: "…what you then have to offer." → "Have you ever heard of TOFU, MOFU, and BOFU?"
- **Out:** the sponsor outro ("Check out ManyChat. Thanks, ManyChat. And I hope this was helpful."), "official Meta business partner", the
  closing question "how are you getting people who find you to find out what you need?". ManyChat stays NAMED and SHOWN as the tool
  (beat 7), the sponsor read goes (OPEN for Affan: it is their paid integration).
- **Length:** ≈ 60-63 s after the tight pause pass (target band 45-70).
- **Per beat, YT look (Sean Ryan B-roll, Anton captions, white seam line) / IG look (neon window, Mark Brazil type):**
  1 YT: his face for 0.87 s, captions only (claim only), then the FUNNEL MG on "TOFU": three dark glass tiers drop in, one per acronym.
    IG: his face in the window, captions only, then the funnel stage. (SHIPPED v3; the plan sent at 14:25 had the credential here: main's
    call 3 moved it to beat 3, low, on his face at 6.3 s.)
  2 YT/IG: the same funnel; each tag expands to TOP / MIDDLE / BOTTOM OF FUNNEL on his words (this shot also hides their burned stack).
  3 YT: his face → a creator filming on a phone (real stock) → people (dots) pour into the TOP tier → his face on "For what?" → the funnel
    with the bottom tier an empty outline + "?" on "what the product or service is". IG: cam, then the stage (top full, bottom "?").
  4 YT: the funnel with only the BOTTOM tier lit (a product box) → his face → a man shouting into a megaphone (stock) → empty seats on
    "nobody's listening" → his face on "that's a big problem". IG: stage (product tier), cam, stage (empty seats in the window).
  5 YT (hero): top + bottom tiers lit, the MIDDLE pulled out, a red marker ring + "MOFU" on the gap. IG: stage, the gap, red "the MOFU".
  6 YT: dots pour in the top (covers their "Manychat" burn) and fall out through the gap; split with his face on "not connecting"; a path
    from top to bottom broken at the gap. IG: the same leak on the stage.
  7 YT: the middle tier slides back in, glowing (the glue) → ManyChat itself on "something like ManyChat" (its logo / its own page) → a
    phone: a post gets a comment, an automatic DM answers it, the thread follows up → his face on "The fortune is in the follow-up" and
    "it changed everything". IG: comment → DM cards on the stage, the ManyChat mark, cam.
  8 YT: his face → a robot on "creates a robot" (real stock) → back to him. IG: cam, stage.
  9 YT: his face on "Automate the middle", then the COMPLETED funnel (TOP content → MIDDLE AUTOMATE → BOTTOM your offer) with the dots
    flowing all the way down, landing on "offer" (the closing image). IG: the same as the last stage, red "Automate the middle".
- **Sound:** no music bed (as Roofing r1; their Short has none): flip it if Affan wants one (a bed would sit ≈ 8 dB under the voice).

## Main's calls on the sequencing (2026-11-02 ≈14:35; Affan can override, main forwards)
1. Watermark / tag = **"PAT FLYNN"** (the Short lives on @patflynn; the hook tag is their channel).
2. Sponsor: dropping the outro read is fine; ManyChat stays named AND shown in the body as the tool (keeps the integration's value).
3. **Credential NOT under the 0-3 s hook** (feedback-hook-claim-only: "too much text at the beginning"): the low FOUNDER / SMART PASSIVE
   INCOME card comes in after the hook, on beat 3 (his first clean face after their burned stack, "The creator will usually start…"), low.
4. **Music: the YT look gets the preset's continuous soft bed** (lo-fi / mellow instrumental, no vocals, Epidemic), ≈ 8 dB under the voice
   and audible the whole way; the IG look per the neon-window preset (no bed). Track logged below.

## Decisions (with reasons)
- **Credential:** "FOUNDER OF" / "SMART PASSIVE INCOME" low under the captions on beat 3 (main's call 3); watermark = "PAT FLYNN" (main's
  call 1). Frame 0 = his face + the captions only; from "TOFU" the funnel IS the hook picture.
- **On-screen facts:** no numbers anywhere (he says none): no follower counts, no prices, no conversion rates. The funnel labels are his
  words (TOP / MIDDLE / BOTTOM OF FUNNEL, TOFU / MOFU / BOFU); the DM thread is a generic built chat, no invented brand, no fake metrics.
- **Same-camera joints:** handheld selfie, every joint is a jump cut: A shots at z0 ≈ 1.15 with the kit's head lock (eyes), and the bad
  joints covered by graphics; their hard cut at raw 85.15-85.30 becomes a shot edge.
- **Loudness:** voice peaks at −6 dBFS (limiter ceiling), integrated ≈ −15 LUFS (≈ theirs), measured and reported.
- 30 fps native, no Topaz (Affan 2026-10-31).

## Catalog pass (2026-11-02; CATALOG.md FX-01..81 read in full; all 137 stills of `research/effects-catalog/shots/` LOOKED AT on labelled
## sheets `work/catalog/singles_1-4.jpg` (79 singles) + `strips_1-5.jpg` (58 four-frame strips), every tile read)
- **Fits this story** (an abstract business model, no documents, no numbers, one speaker on a selfie):
  - **FX-73 Chart Reprise Push-In**: ONE funnel object built once and returned on every beat in a new state (top only / bottom only /
    middle missing / leaking / glued / complete), pushing in on the part that matters.
  - **FX-69 Lone Yellow Bar** logic: the tiers grey, the ONE tier the line is about in the accent.
  - **FX-70 Ring and Benchmark** + **FX-55 Red Pen Underline**: one hand-drawn red ring on the missing middle ("The MOFU").
  - **FX-23 Pointer Tag**: small tags pinned to the tiers (TOFU / MOFU / BOFU → TOP / MIDDLE / BOTTOM OF FUNNEL).
  - **FX-25 Exhibit Grid**: the funnel on a dark perspective grid floor (depth without a fake studio).
  - **FX-29 Float Frame**: stock B-roll that is 720p plays as a float frame over its own blurred plate, never blown up.
  - **FX-57 Propped Phone Call** idea: the comment → DM automation shown on a phone object, not as flat text.
  - **FX-79 Flash-Forward Echo**: the closing funnel = the hook's funnel, now complete (the loop).
  - **FX-42 Kin Tag**: the credential beside/below his face on frame 0.
- **Not used yet on this channel/batch:** a single diagram object carried through 7 states (Roofing carried a document through 4); a
  particle flow (people as dots) pouring, leaking and flowing through it.
- **Leaned on by the last ones, avoided here:** Roofing's tax-return document + blurred rows (FX-33/35), CrossExamined's FX-41 Year Ghost,
  Pollak's FX-27 quote card + FX-28 dossier, Pincus's read-along highlighters (FX-34).

## What this one does better than the last ones (rule 5; Roofing r1 / CrossExamined / TCO, 2026-10-31 → 11-02)
1. **Enhances their exact Short** (the new mode): the before/after is the pitch, so every row of the teardown above is a visible win.
2. **One concept object explains the whole lesson**: a funnel that changes state with each beat, so the viewer SEES the missing middle and
   the fix, not only hears it (Roofing told its story in documents; this one in a diagram that moves).
3. **More MGs than any sample so far** (≈ 15 graphics in ≈ 62 s), face never > 4 s bare, and a varied soft SFX set sized per move.
4. Voice at the new −6 dBFS peak standard (REACTIONS-V2 note 2) from the first build.

## Sources (logged as they are added)
| Use | File | From |
|---|---|---|
| "you're building an audience": a camera recording a creator (vertical; src_in 0.5) | yt/assets/broll/b-creator-41289.mp4 (1080x1920 23.976) | Mixkit 41289 "YouTuber recording himself" (free licence) |
| "Here's the thing that I can serve you with": hands taping up an order box (vertical; src_in 0.4) | b-pack-42137.mp4 (1080x1920) | Mixkit 42137 "Hands of two people sealing a package with tape" |
| "screaming at the top of your lungs": a man screaming (4K → 9:16, no upscale; src_in 1.7) | b-scream-42242.mp4 (3840x2160) | Mixkit 42242 "Man screaming desperately" |
| "and nobody's listening": an empty theater (720p float frame; its empty first seconds) | b-theater-21829.mp4 (1280x720) | Mixkit 21829 "People filling an empty theater" |
| "A person who scales everything just creates a robot": a humanoid robot face (720p float frame; src 0-3.7 s, before a passer-by enters) | b-robot-20961.mp4 (1280x720) | Mixkit 20961 "Robot with moving eyes" |
| the REAL ManyChat wordmark (white, keyed: median of 60 frames, min-channel + saturation matte) | assets/manychat-wordmark.png (928x174) | their own Short, raw 52.9-54.9 s (the burned-in "Manychat" over his shirt) |
| his "post" on the phone | work/img/post.png | a frame of this cut (frame 1530, eyes open) |
| the funnel MGs (13 states), YT 1080x1920 / split panels 1080x828 / IG 1044x1044 | yt/assets/broll/mg-*.mp4, ig/assets/mg-*-ig.mp4 | built: work/gfx.py + work/mg.py (Anton, IBM Plex Mono; params from yt/build_spec.py) |
| the bed (YT only) | yt/assets/audio/bed-laundry-list.wav | Epidemic "Laundry List" (Dylan Sitts), EditRecording 66.28 s, offset 2.28 s so its ending lands on the last frame |
| SFX (12 takes) | yt/sfx/*.wav (slices of assets/sfx/epidemic/spi-*.wav) | Epidemic (download log x1-x13; spi-s-card1 dropped: 97 % above 6 kHz) |

## Download log (logged BEFORE each pull)
| # | File | Source | Size | Why |
|---|---|---|---|---|
| r0 | `reference/gLydjgO_q6s.mp4` | main session (YouTube gLydjgO_q6s, 1080x1920 30 fps H.264) | 56 MB | their Short = the source (not pulled by me) |
| m-list | `work/img/mk_<tag>.html` (listing pages: vlogger, influencer, megaphone, empty-theater, empty-chairs, robot, robotic-arm, package, product, delivery) | mixkit.co/free-stock-video/<tag>/ | ≈ 0.2 MB each | find clip ids for the B-roll beats |
| m-thumb | `work/img/mixkit/<id>-thumb.jpg` (720p thumbnails: 41289 41272 42323 34486 42242 21829 42130 42137 49042 20961 47257 49040 49041) | assets.mixkit.co/videos/<id>/<id>-thumb-720-1.jpg | ≈ 50-100 KB each | first look at the candidates |
| m-prev (not pulled: thumbnails were enough) | `work/img/mixkit/<id>-360.mp4` (360p previews of the candidates) | assets.mixkit.co/videos/<id>/<id>-360.mp4 (Mixkit free licence) | ≈ 1-3 MB each | pick each B-roll shot by eye (frame sheets, no playback) |
| m1 | `yt/assets/broll/b-creator-41289.mp4` (vertical 1080x1920) | assets.mixkit.co/videos/41289/41289-1080.mp4 (Mixkit free licence; 2160 = 403) | 68.8 MB | "You're creating content": a camera recording a creator (his image on its screen) |
| m2 | `yt/assets/broll/b-pack-42137.mp4` (vertical 1080x1920) | assets.mixkit.co/videos/42137/42137-1080.mp4 | 50.6 MB | "Here's the thing that I can serve you with": hands taping up an order box (no face) |
| m3 | `yt/assets/broll/b-scream-42242.mp4` (3840x2160) | assets.mixkit.co/videos/42242/42242-2160.mp4 | 29.8 MB | "screaming at the top of your lungs": a man screaming (the 4K file crops to 9:16 with no upscale) |
| m4 | `yt/assets/broll/b-theater-21829.mp4` (1280x720) | assets.mixkit.co/videos/21829/21829-720.mp4 (1080 = 403) | 4.2 MB | "nobody's listening": an empty theater (its empty first seconds; a FIT float frame, never blown up) |
| m5 | `yt/assets/broll/b-robot-20961.mp4` (1280x720) | assets.mixkit.co/videos/20961/20961-720.mp4 (1080 = 403) | 3.8 MB | "just creates a robot": a humanoid robot face (FIT float frame) |
| c1 | `yt/assets/broll/doc-manychat-home.png` (a still of the page's first screen, 1440x900 at scale 2) | https://manychat.com/ (headless Chrome, `workflows/page-record.mjs`, the capture gate: the real tool he names) | ≈ 1-3 MB | "something like ManyChat": the real product as a DOC receipt (screen look) + its wordmark cropped for the funnel's middle tier | **RESULT: Cloudflare's bot check answered (no CAPTCHA touched), the still was deleted; nothing used.**
| i1 | `work/img/mc/<tag>_NN.*` + `_sheet.jpg` (Bing via curl, `workflows/img-candidates.py`): `logo` "ManyChat logo" x8, `ui` "ManyChat Instagram comment automation flow builder" x8, `dm` "ManyChat comment to DM automation Instagram" x8 | bing.com image search → each result's full-size URL | ≈ 0.1-2 MB each | the real ManyChat mark + its real product UI for "something like ManyChat" |
| x1-x13 | `assets/sfx/epidemic/spi-*.wav` (repo library; MANIFEST rows added) | Epidemic Sound SFX, `DownloadSoundEffect` WAV: 0c248d3f "Swooshes, Swish, Swing, Twirl, Short, Close" · 863f9a1a "Games, Misc, Playing Cards, Hand, Slide On Table" · 3952fb9f "Games, Misc, Playing Card, Slide On Table" · a5da9fbb "Paper, Friction, Envelope, Slide" · 86c26fdb "Marker Pen, Draw Line On Cardboard Sheet 02" · 0495c3a2 "Swooshes, Whoosh, Short, Mid Freq, Dry 02" · fc2ead45 "Swooshes, Swish, Short, Harsh, Dry 02" · 4794588c "Swooshes, Swish, Short, Hard Plastic, Dry 01" · 76a3ff39 "Swooshes, Swish, Short, Hard Plastic, Dry 02" · 91b5b50b "Paper, Friction, Sheet, Large, Laminated, Movement, Slide 01" · dd6d2d57 "Low 02 (Swooshes, Whoosh)" · b2bc02f7 "Low 03 (Swooshes, Whoosh)" · 98b31330 "Low 04 (Swooshes, Whoosh)" | ≈ 0.1-0.5 MB each | a fresh varied soft set, one cue per graphic entrance, sized S / M / L |
| b1 | `yt/assets/audio/bed-laundry-list.wav` (an Epidemic EditRecording fitted to the cut, ~64.5 s) | Epidemic Sound recording 44647473 "Laundry List" (Dylan Sitts; lo-fi hip hop, laid back, relaxing, 80 bpm, no vocals; not used by any earlier job), `EditRecording` + download WAV | ≈ 11 MB | the YT look's continuous soft bed, ≈ 8 dB under the voice (main's call 4) |
