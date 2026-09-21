# BRIEF — gta-san-andreas-hot-coffee (pre-production, 2026-09-15)

**Affan Afterhours** (https://www.youtube.com/@AffanAfterhours), the first video in the channel's documentary format.
It's a **hybrid of three layers**: the host on camera (Volksgeist-style), **Higgsfield reenactments** (Fern-style
faceless 3D figures), and **the house motion graphics** from the Wolverine edit (scenes, cards, camera moves, glow,
racked type, synced SFX). Each beat gets whichever layer tells it best. The old style isn't replaced; it's one of
the three layers. The edit pipeline hasn't started; this is the plan for it. It becomes `RUN.md` at intake.

## ▶ STATUS: resume here (updated 2026-09-16)

**Done**
- Script delivered by the creator → `script.md` (verbatim).
- Higgsfield connected (claude.ai connector). **The reenactment pipeline is tested and approved as the route** (§ 7). Balance 340 credits.
- Drop folders created: `raw/`, `broll/gameplay/`, `audio/music/`, `assets/`.
- Channel preset created (2026-09-16): `presets/youtube/affan-afterhours/` (README = look, PLAYBOOK = procedure, LESSONS = log). This job runs on it.
- **Fact-check → [`FACTS.md`](FACTS.md) COMPLETE** (2026-09-16): 38 claims against primary sources (the FTC complaint and consent order, the ESRB releases and testimony, the House roll call, Judge Kram's decertification opinion, Take-Two's SEC filings, Parkin's Eurogamer piece with the internal emails). 17 verified · 17 partly · 3 wrong · 1 unsourced sentence. The must-change list is in its resume block; every row has a proposed wording.
- **Shot list → [`SHOTS.md`](SHOTS.md) draft v1, reconciled with FACTS** (2026-09-16): every beat assigned a layer, 20 reenactments in two tiers with prompts and credit cost (Tier A 14 shots ≈ 170 credits with retakes, 13 if R20 is cut; A + B ≈ 240), gameplay list, archival list, a resolved fact gate on every row.

**Waiting on the creator**
- Face footage → `raw/` **plus the OBS screen recording that carries the HyperX mic** (dual-system audio: the camera's internal audio is the scratch/sync track only, and intake syncs the two — mechanics in PLAYBOOK § B) · gameplay (SHOTS § 4) → `broll/gameplay/` · music → `audio/music/` · logo → `assets/`.
- **The eye-line marker is READY, not yet proven on real footage.** The creator delivers to the lens and turns their head left to read the monitor; `workflows/eye-line.py` measures that turn so overlays only land on reading segments. Written and unit-tested on synthetic head poses 2026-09-16 (8° separates at 2.6 SD, 20° at ~8 SD, roll-invariant); **the first real take is its validation** — run it, read the separation figure, and check the contact sheet before it gates a single graphic.
- **Decisions:** reenactment tier (SHOTS § 1) · OK per archival download (SHOTS § 5) · the FACTS rewordings in their own voice · fonts and the accent colour (SHOTS § 7) · Volksgeist download OK.

**Next for Claude, in order**
1. When the creator's rewrite lands: save it as `script.md` (keep the original as `script-v1.md`), re-check the changed lines against FACTS, update the SHOTS rows that quote them.
2. Analyse @Volksgeist (download OK needed) → fill the channel preset's § 2 numbers (face share of runtime, host cut rhythm).
3. On the tier decision: generate the approved reenactments per `workflows/higgsfield-reenactment.md` into `broll/reenact/`, log the spend; cut the ~60 s style test (PLAYBOOK A5).
4. After footage lands: `edit-video` pipeline (rough cut → audio → grade → graphics + reenactments → SFX + music → review → export).

---

## 1. Creative direction (locked unless you change it)

| | Direction |
|---|---|
| Format | long-form YouTube documentary, 16:9. Scripted, chaptered, cold open. Cinematic first. |
| Look references | **Fern** (`presets/youtube/fern-inspired/`, measured) for reenactments, pacing, maps and the dark finish · **Volksgeist** (@Volksgeist, to be analysed) for the on-camera host and narration style · **our own Wolverine edit** (`projects/marvels-wolverine-reviews/`) for the motion-graphics craft |
| Layer 1: you on camera | dark, cinematic, face well lit, close shots (spec in § 3). Your face is the spine; the other two layers cut away from it and back. |
| Layer 2: Higgsfield reenactments | for **people, places and moments**. **Faceless humanoid figures** (smooth, featureless heads, realistic bodies and clothes, moody rooms, one warm practical light): a character reference image → image-to-video, or its Blender 3D scene builder. Our own character design, never Fern's models, and **never a real person's likeness** (no generated Houser or Clinton faces). |
| Layer 3: motion graphics | for **information, evidence and numbers**, with the same craft as the Wolverine video, **re-coloured to the dark cinematic palette** so it sits next to the reenactments: documents with highlights, dates, file names, counters, charts, quotes, diagrams, maps. |
| Who gets which beat | Higgsfield when a **human moment** is told (someone at a desk at 11:37 PM, an email being typed, a grandmother at a counter, a vote on the floor). Motion graphics when a **fact is shown** (21.5 M vs < 3,000, 355–21, the file-name list, the quotes, the settlement breakdown, the dates). **Real gameplay** when the game itself is the evidence (San Andreas, the GTA IV statue, the Warm Coffee achievement). Where both fit, I plan both options and you pick at the 60 s test. |
| Captions and on-screen text | **held off.** No running captions and no kinetic word-pops by default. Only your script's own `[ON SCREEN]` lines plus the labels that live inside a graphic (dates, names, numbers). You call any extra text at review, once the video exists. |
| Sound | tense, pulsing suspense score under the voice, steady level; risers into reveals, impacts on title and evidence, whooshes on scene changes |
| Pace | cold open ~27 visual changes/min, body 12–20/min, median shot ~2 s, no still image held over 8 s |

## 2. The story (what I research and fact-check before scripting)

Quick correction up front: San Andreas **came out in October 2004**; the **scandal hit in summer 2005**, when a modder
unlocked the hidden, cut minigame ("Hot Coffee") on PC and it turned out to be on the PS2 disc too. The ESRB changed
the rating from **M to AO (Adults Only)** in July 2005. Stores pulled the game, Rockstar reissued an M-rated edition,
and then came an FTC investigation, political attacks and a class-action lawsuit.

To verify with sources before anything goes on screen:
- **The money:** returns, the reissue, the lower forecast, the settlement amounts.
- **Rockstar's first public line** (blaming modders/hackers) vs what was actually on the disc.
- **"Higher-ups told staff to stay quiet":** this needs a real source (reporting, a book, court documents) before we
  reenact it. A reenactment of an unsourced claim is the thing that gets a documentary channel called out.

## 3. Shoot spec (your face footage) — canonical copy: `presets/youtube/affan-afterhours/PLAYBOOK.md` § B

- **Background:** dark, 2–3 m behind you so it falls off. One small warm practical (lamp, monitor glow, a neon
  strip turned down) gives depth. No bright walls or pink/neon washes.
- **Light:** ONE soft key light 45° to the side, slightly above eye line. Let the other side of your face fall into
  shadow (a black cloth on that side deepens it). Optional faint rim or back light to separate you from the dark.
- **Framing:** medium close-up (chest up) to close-up, **off-centre** with the space on the side you're looking toward,
  eyes on the upper third, camera at eye level. A second, tighter angle is a bonus for cutting.
- **Camera:** 50–85 mm lens, f/1.8–2.8 for a blurry background, 1080p or 4K. **23.976 fps at 1/50 shutter** for the
  film look (first 24 fps job on this system: I verify the timeline maths on the test). Fixed focus, exposure and white balance.
- **Audio:** your best mic, close, in a quiet room (the voice chain handles the level).
- **Performance:** read the script in short sections; when you fluff a line, just repeat it (the edit keeps the last take).

## 4. What you supply, and where it goes

Put everything under `projects/gta-san-andreas-hot-coffee/` (this folder):

| # | What | Where | Notes |
|---|---|---|---|
| 1 | **Volksgeist link** (+ 2–3 favourite videos from it or Fern, with timestamps of moments you love) | tell me in chat | I download (with your OK) and measure it the way I measured Fern |
| 2 | **Script or rough outline** (or say "research it and draft it") | `script.md` | mark beats: `[REENACT: …]` `[MAP: …]` `[DIAGRAM: …]` `[DOC: …]` `[ARCHIVE: …]` |
| 3 | **Face footage** | `raw/` (or leave it wherever; intake copies it) | shot per § 3 |
| 4 | **Gameplay** you record: San Andreas (the world, CJ, the girlfriend's house door) · **GTA IV: the Statue of Happiness from the harbour** (a slow boat or heli pass) · the Warm Coffee achievement pop if you can get it | `broll/gameplay/` | **turn off radio and music in the game settings** (licensed songs trigger Content ID). Never show the explicit minigame itself. The statue must be real gameplay: it's the evidence, and a generated Clinton-like face is off the table. |
| 5 | **Archival links** (news reports, ESRB statement, hearings, articles) | links in chat or `sources.md` | I download each with your OK, trim it and credit it on screen |
| 6 | **Music** 2–4 tense suspense tracks | `audio/music/` | **Answered 2026-09-16: Epidemic Sound.** Official MCP connector exists — connect it the Higgsfield way (claude.ai → Settings → Connectors), then SFX land in `assets/sfx/` and music in `audio/music/`. Files on disk are what the pipeline reads. |
| 7 | **Channel identity:** logo (PNG/SVG) and a colour if you have one (the name is Affan Afterhours) | `assets/` or `brand-kit.md` | for the title card and the brand sting. The close points at "The GTA 6 Leaker's Real Mistake Wasn't The Leak": make it the end-screen video. |
| 8 | **Higgsfield budget** for this video | tell me | reenactment shots cost ~6–7.5 credits per 5 s test; ~15–25 shots ≈ 100–190 credits of your 349.5. Nothing generated without your yes. |
| 9 | **Sign-offs:** the faceless character design, fonts, the ~60 s style test | review in chat | this locks the look for every video after this one |

## 5. What I do (in this order once we start)

1. Analyse Volksgeist, merge it with Fern into **your channel preset** (a GTA documentary look, used every video).
2. Research Hot Coffee → a sourced timeline → a script outline with scene tags (you rewrite it in your own voice).
3. Design the faceless character + 1–2 reenactment test shots in Higgsfield (priced before generating), and test the Blender scene builder.
4. Build the ~60 s style test: cold open slug, reenactment, dark map, doc highlight, name tag, title card.
5. After your shoot: the full pipeline (rough cut → audio → grade → graphics/reenactments → SFX + music → your review → export).

## 6. Risks to know about

- **Monetization:** the topic is sexual content. Talk about it plainly, but show nothing explicit (silhouettes, blur,
  cut away). Keep the title and thumbnail clean.
- **Copyright:** Take-Two is aggressive. Use short gameplay clips that support commentary, no game music, no leaked assets.
- **AI disclosure:** if a reenactment looks realistic, tick YouTube's "altered or synthetic content" box and label
  reenactments "DRAMATISATION" on screen. Faceless figures also keep real people's likenesses out of it.
- **Colour grade on this machine:** Premiere 25.0 can't run the scripted grade (the templates are Premiere 26). Either
  update to Premiere 26 (projects saved in 26 won't reopen in 25; finish ABW6 first) or I give you the manual grade steps.

## 7. Reenactment pipeline (tested 2026-09-15, approved route) — owner of the mechanics: `workflows/higgsfield-reenactment.md`

Test shot: Wildenborg at the desk, 11:37 PM. Files in `broll/reenact-tests/`:
`blender-test-01-still.png` (blockout) → `blender-test-02-polished.png` → `reenact-test-03-kling.mp4`.

| Step | Tool | Cost | Notes |
|---|---|---|---|
| 1. Blockout still | Higgsfield 3D Jutsu (Blender 5.2 worker, built in bpy) | 0 credits | sets the room, pose and camera. ~3 min per 1080p still, so **stills only**, never animation. Catalog import only (no people or monitors), so figures come from primitives. Project: "Affan Afterhours - Hot Coffee reenactment test" |
| 2. Polish | `generate_image` nano_banana_pro 2k, blockout as `image_references` | 2 credits | keeps the composition and makes it a Fern-like 3D-film still |
| 3. Animate | `generate_video` kling3_0 pro, sound off, 5 s, `start_image` = step-2 job | 7.5 credits | ~2.5 min. Outputs 1928×1076 at 24 fps: scale to frame in Premiere |

**≈ 9.5 credits per shot → ~20 shots ≈ 190 credits + retakes.**

Prompt rules learned from the test:
- **No text in generated shots.** The image model added a clock and its digits morphed in the video. Dates, times and places are our own slug graphics.
- **Period-correct screens:** prompt Windows XP / 2005 hardware (the test drifted to a Windows 7 look).
- **Keep faces hidden:** "back of head to camera, head angle locked". The test head drifted toward profile by 4 s.
- Faceless figures only, never a real person's likeness.

## 8. Fact-check list for `script.md` (to verify with sources before the edit)

- "Twenty-one and a half million discs… it was on all of them": copies sold in 2005 vs later; reissued discs didn't have the content.
- "Found to have violated federal law" (FTC, June 2006): check whether the consent order includes an admission.
- "A judge threw the class out altogether": check the class-action record.
- Take-Two cancelling "Snow" and the stated or unstated reason.
- "Internally, Rockstar's PR team are told not to respond" and "Sam Houser finds out by reading a message board": need sources before they're reenacted.
- The GTA 6 close ("every asset… has to actually be deleted", "an entire process"): the disclosure rule is documented, Rockstar's internal GTA 6 process isn't, so frame it as the rule's consequence.
- Also confirm: the 355–21 House vote date, the Kolbe and Donovan email dates, $1.3 M / < $30 K / $860 K settlement figures, the Oblivion re-rating year, and the Dan Houser quote year.
