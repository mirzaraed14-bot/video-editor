# affan-afterhours — the channel preset (v0, 2026-09-16)

**The default for every Affan Afterhours video** (https://www.youtube.com/@AffanAfterhours): long-form YouTube
documentary, 16:9, the creator on camera, in the GTA niche. A job for this channel reads this folder before step 0:
`README.md` (the look, this file) · `PLAYBOOK.md` (the repeatable procedure) · `LESSONS.md` (what earlier jobs taught).

Built on three sources, each kept as its own file so it can be re-measured without touching this one:

| Source | What it gives this preset | Where |
|---|---|---|
| **Fern** (@fern-tv) | pacing numbers, scene vocabulary, the reenactment look, the dark finish | `presets/youtube/fern-inspired/` (measured 2026-09-15) |
| **The house craft** | motion graphics: scenes, cards, camera moves, glow, racked type, synced SFX, the QA + review loop | `presets/youtube/default/` (proven on `projects/marvels-wolverine-reviews/`) |
| **Volksgeist** (@Volksgeist, Philip D'Amico) | the on-camera host: framing, narration rhythm, how the face and the cutaways trade | NOT YET MEASURED — analyse with `presets/youtube/fern-inspired/reference/analyze.py`, then fill § 2 |

## 1. The three layers (the creator's direction, locked 2026-09-15)

A hybrid, not a replacement. Every beat gets whichever layer tells it best.

| Layer | Used for | Look |
|---|---|---|
| **1 · The face** | the spine: narration, opinion, the turns | dark cinematic background, face well lit, medium close-up to close-up, off-centre, shallow depth of field (shoot spec: `PLAYBOOK.md` § B) |
| **2 · Reenactments** (Higgsfield) | human moments: someone at a desk at 11:37 PM, an email being typed, a grandmother at a counter, a vote on the floor | faceless humanoid figures (smooth featureless heads, realistic bodies and clothes), moody rooms, one warm practical light, slow push-ins, 4–6 s per shot, silent (the edit adds sound). **Never a real person's likeness.** Mechanics: `workflows/higgsfield-reenactment.md` |
| **3 · Motion graphics** (the house craft) | facts shown, not told: numbers, dates, file names, quotes, documents with highlights, charts, diagrams, maps | the `youtube/default` craft **re-coloured to § 4's dark palette** so it sits next to the reenactments |
| **Real gameplay** | when the game itself is the evidence | recorded by the creator, radio and in-game music OFF |

**🔒 THE OVERLAY FRAME — the three-layer stack under every Higgsfield reenactment (read off the live
timeline, 2026-09-18).** Bottom to top:
1. **V1** — the face (or gameplay), scale 100.
2. **V2 — a Color Matte, dark red (≈ #3A0000 on the export), spanning the whole reenactment run,
   carrying BCC Film Grain.** V2 is reserved for these mattes; the creator laid one under all 30 runs.
3. **V3+ — the reenactment at Motion > Scale 96** (the creator typed 95 on four; same look), with
   **Drop Shadow: opacity 80 % (204/255), direction 135°, distance 30, softness 40.**

The 4 % inset lets the grained matte show on all four edges as a dark red frame with a shadow — that is
the channel's overlay look, built by the creator by hand. Kling renders 1928×1076 into 1920×1080, so
`setScaleToFrameSize()` produces exactly 96 — fit, add the shadow, lay the matte, and leave the edge.
**Motion graphics stay at 100 with no matte.** Never scale a reenactment up to fill, and never
normalise a clip the creator left at another value. (Cost the day it was broken: `LESSONS.md` ★.)

Where two layers fit one beat, plan both and let the creator pick at the style test.

## 1a. THREE STYLES, ONE FOLDER EACH (2026-09-21)

| style | folder | status |
|---|---|---|
| **face-cam explainer** — face + cut zooms + game footage, 1–3 posters, the 170k look | [`../affan-afterhours-facecam/`](../affan-afterhours-facecam/README.md) | **DEFAULT for the next videos** ("dieting down the editing", the creator 2026-09-21) |
| motion-graphics explainer — the face + 30–40 house graphics from colour labels | `projects/gta6-travis-scott-hired/STYLE.md` + this file § 1b | shipped once (Travis Scott, 2026-09-20); parked unless asked by name |
| documentary — dark cinematic, Higgsfield reenactments | this file § 1–2 | PAUSED (Hot Coffee, 237 views) |

A job reads ITS style folder plus this channel's PLAYBOOK/LESSONS/sfx.json; nothing from another style leaks in.

## 1b. THE CHANNEL HAS TWO FORMATS — and the explainer is the one that gets the views (2026-09-19)

| | **GTA 6 explainer** (the channel's engine) | **documentary** (Hot Coffee, an experiment) |
|---|---|---|
| top result | 167k · 34k · 16k · 13k · 10k views | 237 views |
| set | bright colour-LED room, animated hands, mic in frame | dark cinematic, one practical |
| pace | ≥ 17 visible changes/min, cold open ≥ 25, median shot ≤ 3 s | 10.7/min, median 4.5 s |
| luma | mean ≥ 0.33, 6 % dark frames | 0.22, 31 % dark |
| overlays | illustrated GTA key-art stills (Higgsfield STILLS, 2 cr), posters with ONE pink keyword, game footage | Higgsfield videos at 96 % over a matte, house graphics in ember/tan |
| cost | ≤ 30 credits | ~900 credits (~$50) |
| where it is written up | `projects/gta6-travis-scott-hired/STYLE.md` | § 1, § 2 above; `projects/gta-san-andreas-hot-coffee/POSTMORTEM.md` |

**The documentary format is PAUSED** by the creator until a doc video performs; the explainer format is the default
for the next videos, with the house motion graphics folded in **recoloured to the explainer palette** (navy panel,
white condensed caps, hot pink `#FF2E9A` keyword, Vice City neon) to explain mechanisms the posters can only state.
**The § 1 overlay frame is CHANNEL-WIDE — only the scale changes** (creator, 2026-09-19): in an explainer a
Higgsfield still sits at **85–90** and gameplay is **zoomed out**, both over a **dark colour matte with BCC Film
Grain** on the track below (dark red / dark blue / dark gold — never a light colour); motion graphics stay
full-frame. The mannequin rule and ember/tan do NOT carry over. **People in explainer graphics are PNG cutouts
of the real person, animated as puppets** (a manager's cutout travels to the artist's, the artist's to the label's).
**An explainer opens on the face.**

## 2. Numbers (the documentary format)

**Measured on the channel's own first episode (Hot Coffee, 12:08, 2026-09-18) — these replace the Fern proxies.**

| | measured | Fern proxy |
|---|---|---|
| edit points | **24.0 / min**, median clip 2.25 s, mean 2.50 s, longest 9.8 s | 16–22 / min |
| cold open (0–60 s) | **27 / min** | ~27 |
| perceptible scene changes | 10.7 / min (jump cuts on the face read as continuity) | — |
| face on camera | **38 %** of runtime, median block 7 s, longest 20 s | open |
| reenactment | **41 %**, median block 9 s, the cold open one 37.6 s block | — |
| motion graphic | **16 %**, median block 6.6 s | — |
| gameplay / stills | 5 % / 3 % | — |
| mean luma | **0.22** (median 0.25); blacks 21/255; 31 % of frames under 0.18; 2 % over 0.40 | 0.22–0.34 |
| longest held picture | 25 s @ 10:47 (empty hall → face) — one to watch | ≤ 8 s |
| punch-ins | **105 % for 1–3 s on the landing clause**, ~1 per face block; 110 % ≤ 0.6 s for one word | — |
| music | creator's Epidemic bed on A2, 100 % coverage, −24 dB under the cold open, −3…−7 dB body | — |

One warm accent (ember). The hand-cut with its colour labels IS the plan — `PLAYBOOK.md` § 0.

## 3. Text policy: cinematic first

- **No running captions and no kinetic word-pops by default.** This overrides `youtube/default`'s text-animation habit.
- On-screen text is only: the script's own `[ON SCREEN: …]` lines, the labels that live inside a graphic (dates, names,
  numbers, sources), date/place slugs and chapter cards.
- The creator calls any extra text at review (step 7), never the plan.
- **No text inside generated shots** (Higgsfield morphs it). Slugs are our own overlays.

## 4. Identity and palette

- Channel: **Affan Afterhours**. Logo: `assets/logos/` (pending from the creator). Brand kit: `brand-kit.md` (optional).
- Palette: Fern's programme palette (`fern-inspired/README.md` § 5): near-black `#030406`–`#140e0d`, warm browns, tan,
  off-white `#eeece9`, **one hot accent per video**. House graphics are recoloured to this, never to the default starter palette.
- End screen: the last 20 s keep the right side and bottom clear; the outro names the next video (Hot Coffee → "The GTA 6
  Leaker's Real Mistake Wasn't The Leak").

## 5. Sound

- **Background music is ON by default for this channel** (the pipeline's music pass is opt-in elsewhere; this preset opts
  in): a tense, pulsing suspense bed, flat level, from the creator's licensed library in `audio/music/`.
- **The licensed library is EPIDEMIC SOUND** (confirmed by the creator 2026-09-16). Music goes to
  `audio/music/`, sound effects to `assets/sfx/`. Epidemic ships an official MCP connector (launched
  Aug 2026, in Claude's connector directory; docs `developers.epidemicsound.com/docs/mcp`), connected
  the same way as Higgsfield — a claude.ai account connector, never `.mcp.json`
  ([[reference-higgsfield-connector]] explains why that route fails here). **The licence attaches to
  the creator's account, so anything used must be pulled under their own login.** Connected and
  verified 2026-09-16 via an **API key** in `.mcp.json` (the OAuth route fails — see
  [[reference-epidemic-sound-connector]]). **It downloads as well as searches**, WAV or MP3, so
  tracks land in `audio/music/` and effects in `assets/sfx/` and the normal pipeline takes over.
  Music comes with **separated stems**, and the no-drums stems usually sit better under narration
  than the full mix. Search by feel, not keyword: `moodSlugs` covers suspense / dark / sneaking /
  mysterious, and `taxonomySlugs` covers dark-ambient / crime-scene.
- SFX per `youtube/default/sfx.md`: risers into reveals, impacts on title and evidence cards, whooshes on scene changes;
  reenactment entrances count as entrances.

## 6. Locked vs draft

Locked: § 1 layers, § 3 text policy, § 5 music on. Draft until the first video ships: § 2 numbers (Volksgeist pending),
§ 4 logo and accent, the reenactment character design (approved at the style test). Changes come from `LESSONS.md`.
