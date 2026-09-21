# BRIEF — gta6-travis-scott-hired (pre-production, 2026-09-19)
**"How Rockstar Actually Hired Travis Scott For GTA 6"** — Affan Afterhours, the channel's **GTA 6 explainer
format** (the one that gets the views), ~8 min, with the house motion graphics folded in to explain the mechanisms.
Thumbnail (creator's): `THEY DIDN'T CALL TRAVIS` + Travis / Future / Metro faces.

## ▶ STATUS: resume here (updated 2026-09-19)
**Done (foundations, no editing):** `script.md` verbatim (V15 FINAL) · `FACTS.md` (32 claims, primary-sourced; 4
items need the creator) · `STYLE.md` (the explainer format measured off three reference exports + the modifications)
· `SHOTS.md` (40 beats → face / still / motion graphic / game; 7 must-stills = 14 cr, 6 nice = 12 cr, 26 comps) ·
drop folders made.
**Landed 2026-09-19:** the Extended Look footage → `broll/gameplay/gta6-extended-look.mp4` (26:48, 1080p30) ·
three reference images → `assets/refs/` (the RHYNO single art with Travis composited into VI key art; Metro
Boomin's post of the Coquette teaser; the six-tile VI key-art grid) · the two unsourced quotes DECIDED as
unattributed posters (FACTS B2/B3) · likenesses DECIDED (§ 5, PNG cutouts).
**Waiting on the creator:** **the face recording (not yet shot)** · source photos for the cutouts →
`assets/cutouts/` · a screenshot of Travis's RHYNO post · one real "appears courtesy of" credit · the "eleven
days ago" count fixed to the record date · OK on the rewritten Martyn Ware line (FACTS H4).
**Next for Claude, in order (a FRESH session — say "resume gta6-travis-scott-hired"):** 1 read this block and
`STYLE.md` § 4 · 2 intake the face take + footage · 3 rough cut (`RENDER=0`, replay to Premiere) · 4 audio polish ·
5 graphics-plan from `SHOTS.md` (the 12 explaining scenes first, then the posters) → build in the pink/navy palette
→ place · 6 the 7 Tier-1 stills (nano_banana_pro, 2 cr each, gated on their still before anything else) → place ·
7 SFX → 8 the creator's review → export.

## 1. Creative direction (what differs from `presets/youtube/affan-afterhours/README.md`)
- **This is the explainer format, not the documentary.** Bright colour-LED room, animated hands, ≥ 17 visible
  changes/min, cold open ≥ 25/min, median shot ≤ 3 s, mean luma ≥ 0.33, face ≥ 60 % of runtime. Numbers and the
  grammar: `STYLE.md` § 1–2. **The Hot Coffee palette (ember/tan/near-black), the mannequin rule, the 96 % overlay
  frame and the slow pace do not apply here.**
- **Palette:** navy panel `#12102A` · white condensed caps · **one hot-pink keyword `#FF2E9A`** per card · Vice City
  neon backdrops · the wall's own LED colour. Fonts: the condensed grotesk the posters already use (Bebas/Oswald
  class) — pull the exact face from the creator's Premiere project before building.
- **Four creative assets only:** (1) the face recording — **the video opens on the face** · (2) **Higgsfield
  STILLS — no video** (nano_banana_pro, 2 cr; GTA key-art style, Vice City palette, a scene that literalises the
  line), placed at **scale 85–90 over a dark colour matte with BCC Film Grain** on the track below (dark red /
  dark blue / dark gold only) · (3) the house motion graphics, recoloured, **doing the heavy lifting** (the 12
  mechanism scenes in `STYLE.md` § 4.1) — **people are PNG cutouts of the real person, animated as puppets** (the
  manager's cutout moves to Travis's, Travis's to Rockstar's) · (4) GTA VI Extended Look footage here and there,
  **zoomed out over the same grained matte**, never fit-to-frame. Full detail: `STYLE.md` § 4b.
- **The modification the creator asked for:** *"that style but integrated with your motion graphics concept with a
  little bit more complexity … so that the concepts get better explained."* The format's posters state; this script
  has mechanisms (the chain, the clearance, points, rent vs own, ×34, the three clubs). Each mechanism is a short
  animated scene in the format's own colours — that is the whole difference. Everything else stays the channel.
- **Budget:** ≤ 26 Higgsfield credits on stills (balance ~127), **plus enhance passes** for any soft web-sourced
  picture (STYLE § 4b.6): `upscale_image` is a flat per-image cost that can only be preflighted on a real
  uploaded image (`get_cost=true`) — preflight the first one, state the number, and get the creator's OK before
  spending. Zero video generations. The previous video cost ~$50 and
  sits at 237 views; this format's top video sits at 167k. Cheap is the brief.

## 2. The story — what has to be true (→ `FACTS.md`)
The casting-call thesis rests on: Stromberg is Travis's manager (✓) · Travis is signed to Epic/Sony (✓) · a
clearance is the label's permission and "appears courtesy of" is its receipt (✓) · Future's $250k verse via Megan
Thee Stallion (✓) · Guy-Manuel co-produced Modern Jam in 2023 (✓, "with Travis") · producer points come from the
artist's royalty (✓) · Cripps's "each scene" quote (✓, **name him**) · RHYNO "live at the J.O.H." / the Jack of
Hearts / Boobie Ike (✓) · 34 songs, Atlantic = Warner (✓, **say Atlantic**), Weaver's "two years" (✓, **he is the
President**) · ten-year one-off game licences (✓) · **Martyn Ware: $7,500 PER WRITER × 3, not one $7,500 split in
half** (fix) · GTA IV 54 songs, Bowie, Black Sabbath (✓) · Moloko out of GTA V on 15 Sep 2026 (✓, re-count "eleven
days"). **Two quotes are unsourced by me and gated** (B2, B3).

## 3. What the creator supplies, and where it goes
| what | where | notes |
|---|---|---|
| the face take (camera file + OBS mic track) | `raw/` | dual-system as in PLAYBOOK § B; **the explainer set** (LED wall, chair, mic in frame), animated hands, jump-cut-friendly |
| GTA VI Extended Look — **LANDED** as `broll/gameplay/gta6-extended-look.mp4` (26:48, 1920×1080, 30 fps, copied from `E:\Bullshit Folder\Simone\`) | `broll/gameplay/` | placed zoomed out over the grained matte; the Jack of Hearts if it appears; it carries Rockstar's own audio — mute it under the voice |
| source photos of the people for the PNG cutouts (Travis, Stromberg, Future, Metro, Ware, Weaver, Cripps) + the Rockstar mark | `assets/cutouts/` | backgrounds removed by the pipeline (`media-use` remove-background / Higgsfield `remove_background`); Rockstar / label press shots are the safest sources |
| screenshots: Travis's RHYNO post; one real "appears courtesy of" credit; the interview behind B2/B3 | `assets/` | the receipts shown, never re-typed |
| the music bed (their Epidemic pick) | `audio/music/` | upbeat, as the format uses; they lay it on A2 |
| the thumbnail | — | theirs |

## 4. What Claude does, in order
See the STATUS block. The graphics plan comes from `SHOTS.md` rows 1–40; the stills from its Tier 1 (then Tier 2
only if the cut wants picture); every still gated on its FACTS row and on its own 2-credit still before placement.
The edit runs the eight steps of `CLAUDE.md` on the Premiere lane; `RUN.md` is opened at intake.

## 5. Risks
- **Likenesses — DECIDED by the creator (2026-09-19):** the motion graphics use **PNG cutouts of the real people**
  as animated puppets (Travis, Stromberg, Future, Metro, Ware, Weaver, Cripps, the Rockstar mark). The Higgsfield
  stills stay **scenes**, not likenesses, and the mannequin rule was Hot Coffee's choice, not the channel's.
  Rights: prefer Rockstar / label press shots and the artists' own promo images for the cutouts; a photo of a
  named person in an explainer is standard YouTube practice, but keep the sources noted in `assets/cutouts/`.
- **The four words.** On screen, censored, never spoken — as the script says. Keep the censor block opaque.
- **Monetisation.** Licensed music never in the cut; the bed is the creator's Epidemic pick; game footage is
  Rockstar's published Extended Look.
- **Tool gaps on this machine.** Premiere 25.0 can't run the scripted grade (manual recipe in lane notes);
  `exportAsFinalCutProXML` hangs on very large sequences (DOM readback is the fallback); `place-sfx.py` must be
  followed by an all-tracks audit (lab-notes 2026-09-17/18).
- **Date-stamped lines.** "eleven days ago", "two days" — re-count on the recording day.
