# fern-inspired — the long-form documentary preset (DRAFT v0, measured 2026-09-15)

**Opt-in by name only** ("edit this in the fern-inspired style"). The default stays `presets/youtube/default/`.

A style study of the channel **@fern-tv** (5M subscribers; narrated investigative documentaries), adapted
to a creator who stays ON CAMERA: the host is Fern's "interview" subject, and everything they describe
becomes a Fern-style scene. This is a study of pacing, structure and visual grammar — **no Fern asset,
logo, title artwork, character model or music is copied or shipped**; everything is rebuilt from scratch.

Reference set (analysis only, never placed in an edit): `reference/videos/` — The Truth About fern
(TlioXObelHU, 12:52), The Bank Heist of the Century (PSHQ_MuxxNw, 22:33), The $1 Billion McDonald's Box
(65hjeAq6Oq0, 29:16), Why everyone hates Lego now (dSgwNvydXhI, 30:01). Numbers: `reference/analysis/<id>/stats.json`,
contact sheets beside them (one frame / 5 s), measured by `reference/analyze.py`.

---

## 1. The measured numbers

| | Truth About fern | Bank Heist | McDonald's Box | Lego | **→ preset target** |
|---|---|---|---|---|---|
| visual changes / min (scene score > 0.3) | 24.6 | 15.3 | 19.3 | 19.7 | **16–22** |
| median shot | 1.2 s | 2.2 s | 1.8 s | 1.7 s | **~2 s** |
| shots over 8 s | 7 % | 12 % | 6 % | 7 % | **≤ 10 %** (a long hold is a camera move, never a still) |
| changes / min by quarter | 28·21·28·21 | 26·10·13·13 | 27·15·23·13 | 14·25·17·24 | **cold open ~27/min**, body 12–20 |
| mean luma | 0.27 | 0.22 | 0.34 | 0.66 | **dark: 0.22–0.34** (light only for "clean data/product" topics) |
| near-black pixel share | 48 % | 58 % | 39 % | 11 % | **40–55 %** |
| mean saturation | 0.45 | 0.44 | 0.43 | 0.22 | **moderate, one warm accent** |
| programme loudness | −18.9 | −15.6 | −18.9 | −14.7 LUFS | voice chain unchanged; music bed audible (see § 6) |

Scene score counts camera moves and flashes as well as hard cuts, so read "visual changes", not "edits".
The cold open always runs hot: every video's first quarter sits near 27 changes/min.

## 2. Structure (every video)

1. **Cold open (0:00 → ~1:15):** a dramatised scene mid-story (a 3D reenactment: 1970s office, a cash-counting
   room at 5:15 AM), with a **date / place slug** lower-left in small monospace caps
   (`SEPTEMBER 23, 2009 | 5:15 AM` / `VÄSTBERGA, SWEDEN`) or on a **yellow cut-paper tag** ("1970s / Fullerton, California").
2. **Credits woven over the cold open** in stamp-style small caps beside the action ("3D ANIMATION", "SOUND DESIGN & MIX").
3. **Title card ~1:15:** the story name HUGE in a distressed condensed face (red on near-black, grain), a small
   uppercase subtitle under it ("THE CRAZIEST BANK ROBBERY OF ALL TIME"), channel mark above.
4. **Body in chapters:** evidence (news broadcasts, CCTV, articles) → explanation (maps, diagrams, charts) → reenactment → expert on camera, repeating.
5. **Time jumps are labelled** on screen ("ONE MONTH EARLIER").

## 3. The scene vocabulary (what the frame can be)

| # | Scene type | Look | Our build route |
|---|---|---|---|
| S1 | **Reenactment** | stylised-realistic 3D people and rooms, single warm practical light, deep shadows, shallow DOF, slow dolly/push | ⚠ NOT buildable in HyperFrames at Fern quality — see § 7 (AI-video or 3D artist) |
| S2 | **Archival evidence** | real news broadcast, CCTV, press photo, soft / low-res, film grain | real sourced footage (§ 7), framed full-frame with grain + a small source credit lower-left |
| S3 | **Dark map** | desaturated teal-green street/satellite map, darkened; dashed route line drawing on; small boxed label chips ("CASH DEPOT"); slow push toward the target | ✅ buildable (vector map data rendered to the tint; satellite needs a map provider key, § 7) |
| S4 | **Neon line diagram** | monochrome glowing LINE icons + arrows + labels on a flat tinted field (yellow-on-deep-red, white-on-black); process flows, org charts, molecules, patterns that zoom | ✅ buildable (the house glow pass, re-coloured) |
| S5 | **Document / web capture** | real article or product page on light background, key word highlighted (yellow marker, or red block on a headline word), slow scroll + push | ✅ buildable (the capture tools + highlight) |
| S6 | **Clean data chart** | minimal Apple-like bars/lines, blue + grey on off-white, thin axis, title top-left | ✅ buildable |
| S7 | **Person on camera ("interview")** | framed off-centre with lead room, warm practical lights, shallow DOF, dark background; **yellow cut-paper name tag** lower-left, slightly rotated; book/product cover pops beside them | ✅ graphics buildable — **the look of the shot itself is the creator's lighting and set** (§ 7) |
| S8 | **Title / chapter card** | distressed condensed display type, red or off-white on near-black, heavy grain, small caps subtitle | ✅ buildable (font licence, § 7) |
| S9 | **Brand sting** | short glitch/scan-line reveal of a wordmark on deep blue with circuit lines | ✅ buildable with OUR mark, never theirs |

## 4. Type system (to be font-matched and licensed, § 7)

- **Display:** distressed/rough condensed heavy grotesk, all caps, red `#d8342c`-family on near-black.
- **Slugs & credits:** monospace or stencil small caps, wide tracking, off-white, lower-left.
- **Labels on maps/diagrams:** small uppercase sans in a hairline box.
- **Tags:** bold condensed sans on a yellow (`~#e8b84a`) paper shape, slight rotation, hard shadow.
- **Charts / documents:** clean neutral sans (Inter-like), sentence case.

## 5. Colour & finish

- Programme palette (sampled): near-black `#030406`–`#140e0d`, warm browns `#4b372d` `#643e2c`, tan `#a98c77`,
  off-white `#eeece9`, one hot accent per story (red `#5b0803`→`#d8342c`, orange `#ea7550`, amber `#bd824a`).
- **Every chapter owns one field colour** (deep red process chapter, teal-green maps, black org chart).
- Finish: film grain on everything, soft vignette, crushed-but-not-clipped blacks, warm highlights.
  For the on-camera host this is a GRADE (warm, lifted-shadow teal-orange, lower saturation than the default Autumn look).

## 6. Motion & sound

- Camera is always moving: slow push-ins (≈1.00 → 1.08 over the shot), slow lateral dollies on 3D/maps; hard cuts between scenes.
- Diagram elements draw on / pop in sequence with the narration; maps drop label chips then draw the route.
- Music: continuous low, tense cinematic score under the voice (programme LRA only 2.4–4 LU: the bed is steady,
  not dynamic), risers into reveals, whooshes on scene changes, impacts on title/evidence reveals.

## 6b. How Fern makes it (their own account, "The Truth About fern", `reference/analysis-truth-about-fern.txt`)

- A team of ~60 staff and freelancers: journalists write the script under two editors-in-chief plus a fact-check,
  then cutters, 2D and 3D animators, musicians and sound designers build it; scenes are built in **Blender**, reviewed in Frame.io.
- **Art directors are involved during scripting "to make sure interviews are filmed in a certain way"** — the on-camera
  look is planned, not graded in afterwards (the NEEDS.md § 5 point).
- Named influences: Lemmino (3D), Nerdwriter, Kurzgesagt, Vox, CGP Grey, Veritasium. Their 3D thumbnail style came from Lemmino.
- Stated stance: "our animations are made by humans" (an on-screen disclaimer in the cold open) — they do not use AI for
  creative work. Using AI video for S1 reenactments here is OUR production choice, not part of their look; say so on screen if you use it.

## 7. What the build needs that it cannot make by itself

See `NEEDS.md`.
