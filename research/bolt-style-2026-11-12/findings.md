# AW house style: Bolt Motivation vs our "MJ son step outside" (2026-11-12)

Affan, 2026-11-12: "copy Bolt Motivation's style aesthetic, it's pretty much very very close to my style, but I really
like the editing style of the Prince Jackson / Jaafar Jackson short you made, it was really close to Bolt Motivation ... I
just really want to continue that aesthetic. I like the Topaz, the head tracks, everything about it."

The measurements came from a Sonnet subagent (its scripts `a1..a13`, `common.py`, sheets and `data/*.json` are here). The
subagent was not allowed to write this file, so this synthesis was written by the Opus session.

## THE DECISION
**The house style is the "MJ son step outside" build exactly as shipped** (`projects/mj-son-step-outside/`, delivered
11-09). That is the Short he named, and its zoom, transitions, captions, grade and head lock are his own earlier rulings.

Where Bolt measures differently, Bolt does NOT override it. The differences are listed for him below ("his call"), and
nothing from them is built unless he says so. His caption, CTA, label and censor rulings are untouched.

## The template: our build's parameters (port these; file:line from the subagent's read)
Paths are under `projects/mj-son-step-outside/` unless stated.

- **Frame:** 1080x1920, 60 fps; the shots come from the locked read-back (`build/make_timeline.py` ←
  `premiere/final_readback.tsv`). Original sources only, never mezzanines.
- **Topaz (Stage B):** `build/topaz_son.py` + `workflows/topaz-iris.py`.
  - One segment per shot, so interpolation never crosses a cut.
  - Chronos `tvai_fi=model=chr-2:slowmo=1:rdt=0.01` to 60 fps (topaz-iris.py:41).
  - Iris `tvai_up=model=iris-3:scale=4:preblur=0.14:noise=0.14:details=0.73:halo=0.2:blur=0.42:compression=0.84`
    after a 1/4 downscale (topaz-iris.py:40; his numbers, :7-9).
  - Soft panels add Proteus `prob-4 … details=0.6:blur=0.6` (topaz_son.py:13-14).
  - Stabiliser OFF on face shots. ProRes 422 HQ per segment. GPU lock per segment.
  - Check every output for the watermark.
- **Head lock:** `build/stage_a.py` + `build/smooth_track.py`.
  - Nose track, Gaussian sigma 2 frames (smooth_track.py:13); a jump over 200 px is held at the last clean value (:23).
  - That Short locked x only, because its panel clamp blocked y. A full x+y lock is the default where nothing blocks it.
  - One layer spans the same camera across a jump cut.
- **Zoom:** `build/finish.py` + `zoom_layers.json`.
  - One push-in per shot change; `zoom_curve 'table'`; `CURVE = [0,.35,.46,.53,.58,.62,.66,.70,.75,.82,1.0]`
    (finish.py:50, PCHIP); depth by block length (finish.py:81-91):

    | Block length | Depth (z1) |
    |---|---|
    | ≤ 1.4 s | .86 |
    | < 1.5 s | .82 |
    | ≤ 2.5 s | .78 |
    | < 3 s | .77 |
    | ≤ 5 s | .75 |
    | longer | .67 |

  - Shots > 2.5 s use `long_curve` (start burst 38 %, end burst 20 %, drift 42 %; finish.py:125-132).
  - Shutter blur on the zoom. Pivot at the nose on face shots.
  - This is his "transition zoom" (memory `feedback-aw-transition-zoom`).
- **Transitions** (finish.py:159-176):
  - purple = BCC brightness dip −90 (−0.333/+0.267 s);
  - cyan = Gaussian 50 → 0 over 0.7 s;
  - green = +30 swell;
  - hard cuts where the same camera continues.
  That Short used 5 cyan, 5 purple, 1 green and 2 hard; the end is a hard cut.
- **Grade: his AW After Effects look, `grade_mode 'ae'`, layer 43** (PRE sharpen bands, looks, POST LUT, saturation key,
  Sharpen 40, vignette; finish.py:293-310).
  - Per-section temperature, tint, sat and pre-sharp are in `timeline.json`.
  - Check skin with `build/skin_png.py`: not orange, not grey.
  - **This is NOT the Bolt grade.** The Bolt grade (La Toya trial, `grade_mode 'bolt'`) is still waiting on his verdict.
- **Captions:**
  - `captions.txt` (≤ 3 words, about 1 in 3 coloured, no commas or full stops, `i:` italic) → `make_plan.py` →
    `render_caps.py` (trial engine `projects/aw-code-trial-parents/render/cap_render.py`, Gretaros 48);
  - ink y 1040-1079 (`caption_shift -10`; his under-the-lips ruling);
  - pop 100 → 105 → 112 % (`cap_pop.py:11-16`) plus the CapCut-style smear (`captions/capcut_pass.py`, DELAY 6 frames).
- **Cards and CTA:** lower thirds at y0 1262; CTA `mid` × 2, centre y 1392, no end screen.
- **Mix** (`build/mix.py`):
  - dialogue level-matched to −20 dB with 15 ms equal-power joints;
  - swishes (`cm_softs/brush/clean/wind`) on overlay entrances only at −21 dB, cards at −24 dB, CTA at −17 dB under the
    local voice peak;
  - no music;
  - one static gain to −14.0 LUFS, limiter −1.6 dBTP.
- **Export:** H.264 .mov 1080x1920 60 fps, PCM.
- **Letterbox** (available): band [370, 1470], twin scale 1.98, opacity .33 (finish.py:207-225).

## Bolt vs ours, measured (6 downloaded Bolt Shorts + ours; tables in `tables.md`, newest Shorts in `chrome-newest.md`)
| Dimension | Bolt | Ours (MJ son) | Read |
|---|---|---|---|
| Cadence | 4.1 cuts / 10 s, median shot 1.9 s | 3.7 / 10 s, median 2.35 s | close |
| Transitions | 119 of 119 hard cuts | 11 of 13 dressed (dips, blur, swell) | different on purpose (his AE transitions) |
| Edit push-in | linear 1.5-5 %/s (central ~2.5), 3-7 % per shot, no ease; ~5-10 % of shots static. **Rests on 3 clean Shorts; in two others about half the shots pull out** | his transition-zoom table: strong start, drift, end burst, ~16-49 % per shot | different on purpose (his ruling) |
| Captions | 3 words, a change every 1.0-1.2 s, mid-frame (ink y 941-977), white + glow, key word coloured on ~31 % | 2 words, a change every 0.62 s, y 1040-1079, coloured on 33 % | position is his ruling; pace differs |
| Caption entrance | ~2-frame blur blend, centre fixed. My Chrome strip suggested ~10 % growth over ~6 frames: **unresolved** | 3-4 frame smear + 100→112 % pop | his CapCut pass owns this |
| Layout | full-bleed; a 4:5 box (y 284-1634) on a blurred twin for wide or phone shots; **stacked two-panel splits for comparisons** (newest Shorts) | full-bleed; letterbox available; white-line splits | compatible |
| Reaction cutaways | host/judge/crowd reactions every few seconds | as the sources allow | an editorial habit worth copying where footage exists |
| Head lock | none (one jump moved the head 55 px) | x-lock (2 jumps still moved 27-83 px because of the clamp) | ours is the better one |
| Texture | Laplacian 12-344, noise 1.7-8.6 | 37.6 / 2.9 | inside Bolt's range |
| Skin hue | 10-17° here (16-24° in the 11-05 study) | 6° on ONE Short | not a rule: different people, one Short; never push dark skin |
| Audio | **not measured** (the downloads have no audio) | −14.0 LUFS, −1.6 dBTP, swishes −21 dB | none |
| Logo | white bolt low-centre | none | Bolt's brand, not copied |

## His call (offered, not built)
1. Hard cuts only (drop the dips and blurs), as Bolt does.
2. Bolt's slow linear push (~2.5 %/s, 3-7 % per shot) instead of his transition-zoom table.
3. Captions at 3 words per ~1 s (Bolt's pace) instead of ~2 words per 0.6 s.
4. Bolt's grade instead of his AE grade (the La Toya trial).
5. Stacked two-panel splits on comparison beats, and reaction cutaways, where the footage exists. **ADOPTED by Affan on
   2026-11-12 ("Add splits + cutaways")**: AW README § 13. These are sequencing moves and never change a locked cut.

## Corrections to what I said earlier today
- "Bolt's camera moves hard": wrong. That was one host shot whose motion came from the footage. Bolt's measured EDIT
  push is slow and linear.
- "Bolt's grade replaces the AE grade": wrong. The liked Short shipped with his AE grade (`grade_mode 'ae'`).
