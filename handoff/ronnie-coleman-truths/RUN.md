# RUN — ronnie-coleman-truths (ABW9.aep comps 61–64: Ronnie Coleman + Kevin Levrone "12 Brutal Truths")

## ▶ STATUS: resume here
**2026-10-12: 4th FUCHSIA block — letterbox on 2.383–5.033** (Ronnie on the treadmill, was Dark Green): band y502–1485
→ mask y504–1481, twin 232 % @ 47 %, lines at y504 / y1481 (`letterbox/plan65b.json`, `letterbox65b.jsx`, log
`letterbox65b.txt`, proof `letterbox65b-proof.jpg`: twin covers 100 %). The template's cleanup now touches only the
blocks in its plan, so the first 3 stayed as built (comp now 8 lines + 4 twins). Its own undo "Letterbox glow lines
(Claude)" (one). ABW9 NOT saved. The +30 transition after this block (5.033) stays.
**2026-10-12: CAPTION LAYER ON COMP 65** (his ask after the clean): `ron2caps_clean.mp4` imported (#1516, next to
seek 2_clean), his comp 60 precomp duplicated as **`ron2caps.mp4 Comp 1`** (inner layer re-sourced: 50 %, Deep Glow 0.55
Unmult, Bevel Alpha 2.4, 2× Drop Shadow 12 px) and his comp 60 caption LAYER copied onto comp 65 as L1 (Sharpen 80,
Turbulent Displace 4/100 with his Evolution keys), 0–58.4 s, enabled (`captions/capcut/place_caption65.jsx`, log `.txt`).
Undo "Caption layer ron2caps (Claude)". ABW9 NOT saved. FLAGGED: his saved caption layer (identical in comps 47 and 60)
keys Evolution 0 → 9197.8 at 50.967 s (180°/s) → 6139 at 52.517 s, so on a 58 s short the wiggle runs ~11× faster
backwards for 1.5 s and then STOPS for the last ~6 s. Copied as is; the fix would be one key at the end at 180°/s.
**2026-10-12: CAPCUT CAPTION RETURN CLEANED** — `Caption Exports/ron2caps.mp4` (his CapCut return of the Sequence 46
captions, 2160×3840, 60 fps, 3504 frames) → `ron2caps_clean.mp4` (same size / rate / frame count / 58.421 s): 770 frames
repaired = 30 static frames (5, 119, 239 … every 2 s, 38–44 % of the frame) + 740 faint 1-frame specks ≤ 2.5 %
(`captions/capcut/clean.log`). Checked on 16 frames (`captions/capcut/verify_clean.py`): caption pixels (Y > 60) move
≤ 4 levels (re-encode), the lifted black field 42–46 % → ≤ 0.3 %. NOT in ABW9 yet (no caption export is used by
comp 65), so nothing re-pointed: import `ron2caps_clean.mp4`, not `ron2caps.mp4`.
**2026-10-12: LETTERBOX LOOK on the 3 FUCHSIA blocks of ABW8 Linked Comp 65** (7.533–8.767, 8.767–10.25, 51.967–53.5:
the Kevin posing inserts), built the way his comp 60 does it (read off `letterbox/comp60_deep.json`): mask on the
picture band (feather 0) → twin underneath with the same mask, scaled to fill (199 / 227 / 236 %) at 47 % → two copies
of his own comp 60 glow line ("White Solid 1 Comp 1", Deep Glow 0.55 + Bevel Alpha + 2× Drop Shadow) centred on the mask
edges, placed above his grade, below the zooms. Read back (`letterbox/letterbox65.txt`) and proven on a rebuild
(`letterbox/letterbox65-proof.jpg`: twin covers 100 % of the frame, no black inside the band). Undo "Letterbox glow
lines (Claude)" TWICE (the first run stopped on its read-back after block 1; the second cleaned that up and built all
3). ABW9 NOT saved. Note: relabelling these 3 to fuchsia does not touch the transitions already built; a re-run of the
transition pass WOULD drop the ones after them (fuchsia = no transition).
**2026-10-12: TRANSITION PASS on ABW8 Linked Comp 65** from his labels (fresh dump `transitions/labels_comp65.tsv`):
18 transitions = 11 Dark Green (+30), 4 Cyan (Gaussian Blur), 2 Purple (−90 dip), 1 Peach (Exposure Blur), 1 Pink (white
flash at 15.667). No transition after 10.25–14.317 and 56.667–57.467 (Aqua); last block ignored. Every value read back
(`transitions/transitions65.txt`). Stack, re-dumped: transitions 1–18 → zooms 19–39 → his grade (Adjustment Layer 33)
40–42 → footage 43–63. Undo "Abundance Wisdom transition pass (Claude)". ABW9 NOT saved. The zoom pass below is still the earlier step.
**2026-10-12: ZOOM PASS (BlurMoCurves) on ABW8 Linked Comp 65** (his Topaz render `ronnie_stab_chr2_iris3.mov` of
Sequence 46, 21 blocks, 3 yellow = pull out: 7.53–10.25 s and 51.97–53.50 s): 21 `Adjustment Layer 29` zooms with
S_BlurMoCurves, 11 face pivots, every Z read back as planned; a fresh dump shows exactly one zoom per block, all above the
footage (no caption layer in the comp yet, so the zooms sit on top). Preview `zoom/zoom-preview.jpg` checked block by
block; black bands on blocks 2, 4, 5, 18 are his own framing of those inserts. Undo "Abundance Wisdom zoom pass
(Claude)". ABW9 NOT saved. Next on the creator: relabel for transitions (then the transition pass).
**2026-10-11: CAPTIONS on ABW8 Sequence 46 — 91 captions, max 3 words, imported as a caption track
(`importFiles true | createCaptionTrack true`, targeted by name; Sequence 47 stayed the active one, and the creator was in
an export/codec dialog, so it was NOT window-grabbed). ABW8 NOT saved.** Styling per `captions/caption-colours.md`
(Gretaros; Gretaris Italic on Kevin's lines; 26 of 91 coloured).
Earlier the same day: HEAD LOCK applied on ABW8 Linked Comp 61–64 (below). ABW9 NOT saved.

## Captions (`captions/`)
`sequence-captions.py read` (Sequence 46: the short is 0–58.40 s; the clips parked after the gap at 67.75 s are not it)
→ reference trimmed to 58.4 s (full read in `brief/parked/`) → `transcribe.sh` (224 words) → `captions.txt` →
`make_plan.py --hang 0.8` → `make_srt.py … seq46-captions` → `sequence-captions.py import`.
- Speaker from the A1 source of each clip: upright = Ronnie (Shannon Sharpe interview), italic (`i:`) = Kevin Levrone
  (A1 15.67–18.93, 20.23–23.35, 36.53–38.93, 40.52–53.48, 56.67–58.40).
- Colours: red = losses / booze / regret, blue = Kevin, green = winning, yellow = emphasis.
- **Transcript fix:** WhisperX heard "We're in this show" at 35.68 s; two beam-5 re-decodes (with and without a prompt)
  both hear **"…this is what I'm doing to win these shows"**. Fixed in `transcript/words.json` (words 138–141, tagged
  `fix`); the untouched WhisperX file is `transcript/words.whisperx.json`.
- Not changed, for the creator's ear: 38.4 s "go ahead and **try it**" (beam 5 hears just "try").

## Letterbox (`letterbox/`)
`deep_dump60.jsx`/`deep_dump65.jsx` → `comp60_deep.json` (his look) + `comp65_deep.json` → `plan_band.py` (band measured on
every 2nd frame of his render; mask = band edge inside 95 % of frames; twin = fill scale × 1.10; lines at edge − 537) →
`plan65.json` → `letterbox.jsx.tmpl` → `letterbox65.jsx` (log `letterbox65.txt`) → `proof.py` → `letterbox65-proof.jpg`.

## Transitions (`transitions/`)
`dump65_labels.jsx` → `labels_comp65.tsv` → `transition_pass.py` → `transitions65.jsx` (log `transitions65.txt`) →
`dump65_after.jsx` → `after_comp65.tsv`.

## Zoom (`zoom/`)
`dump65.jsx` → `srcmap_comp65.tsv` → `zoom_pass.py` → `zoom-preview.jpg` → `zoom.jsx` (log `zoom.txt`) →
`dump65_after.jsx` → `after_comp65.tsv`.

## Head lock (`headlock/`)
read_comps6164.jsx → `ae_comps6164.txt` (32 layers; sources "GOAT Bodybuilder, 8x Mr Olympia Ronnie Coleman Chest
Workout…" 23.976 fps and "12 Brutal Truths For Men From The Uncrowned King of Bodybuilding" 25 fps, all 184–197 %) →
`live6164.txt` → `head_track.py` (0 missed) → `track_sheet.jpg` (dot on Ronnie / Kevin / the bearded host in comp 64 L3)
→ `headlock6164.jsx` → `headlock6164.txt` (32/32 keyed) → `headlock_read.json` → `headlock_proof.jpg`.
Biggest travel: comp 64 L1 (Ronnie wiping his eyes with a tissue) x −45..+305 comp px, at the top of the earlier range
(306 on comp 41); his face stays inside the crop (x 382–732 unlocked), so it is locked whole.
