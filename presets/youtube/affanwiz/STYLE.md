# affanwiz — THE EDITING STYLE v2: the IGN-missions style (adopted 2026-10-13)

**The creator, 2026-10-13:** *"analyze my @affanafterhours channel's this video frame by frame… I want to replicate that
style exactly for the affanwiz channel."* The reference is **"GTA 6 Just Got A Whole Lot More Interesting…"** (Affan
Afterhours video 22, 8:17, thumbnail "MISSIONS ARE JUST SIDEQUESTS"), built in this repo as job
`projects/gta6-ign-missions/` on ABW8 · **Sequence 39** and finished + exported by the creator: master
`E:\Shorts\Abudance Wisdom Shorts Exports\Final Renders\GTA IGN.mov` (496.0 s, 1080p59.94). Same room, same face, same
mic as this channel, so the face grammar carries over 1:1. Supersedes v1 (`STYLE-v1-game-informer.md`).

Evidence: the final Sequence 39 read live and read-only (`reference/ign-missions/seq39-*.json`), the master measured with
the style tools (`reference/ign-missions/report.md`, `probe/`, `zoom.json`), every graphic sampled entering / settled /
leaving (`reference/ign-missions/sheet-gfx-0..2.jpg`, `sheet-broll-zooms.jpg`), and the job's own design system
(`projects/gta6-ign-missions/brief/graphics-design.md`) and builders (`hf-graphics/gfx/`). Self-contained on purpose.

## 1. The shape (measured on the master)
| | measured | rule |
|---|---|---|
| visible changes | **24.3 / min** (hard cuts 11.4, zoom steps 5.9, reframes 7.7) | ~24 a minute |
| face on screen | **62 %**, 28 runs, median 6.8 s, longest 38.8 s | ~60–65 % |
| graphic runs | **27 = 3.3 / min**, median **6.2 s** (2.1–11.6), longest without the face 23.6 s | ~3–3.5 a minute, 4–8 s |
| cut zooms | **56 on V1 = 6.8 / min** (49 measured steps), median **135 %** (p25 130, p75 140), range 110–250, hold median **1.27 s** (0.9–1.75); 21 repositioned on the face | § 2 |
| gradual push on the face | **none** (no nests, no 100→110 keys: −0.02 %/s) | none |
| speed | one creator-added **0.8x** run (3 clips, 2:53.5–2:57.9, a joke) | 0–2 per video, on a joke, pitch kept |
| speech | 200.9 words/min, 5 pauses ≥ 1 s | cut tight |
| transitions | hard cuts only | |
| captions / grade | none / none (the lit room is the look) | |
| loudness | **−17.1 LUFS** integrated, LRA 4.2, peak −3.9 dBFS | |

## 2. The face (V1, the creator's grammar — `affan-afterhours-facecam/CREATOR-HAND.md` § 1)
- **Cut zoom** = a razor + a STATIC Motion Scale on the piece under the emphasis line, then straight back to 100.
  Bands: ~110 (nudge), **120–150 (the normal hit, most at 130–140)**, 160–250 (a big hit, Position moved so the eyes stay
  in frame), one **extreme close-up ~250 %** on the biggest reaction. Ladders +10 per rung on an escalating line.
- **Stretch gag**: Uniform Scale OFF, Scale Width 250–930 %, 0.4–1.5 s, on one mocking word, 1–2 per video.
- **No push, no nests.** Graphic and b-roll edges land ON a V1 cut, never a frame early (`memory: no stray frames`).
- **Music out under every cut zoom** (`lanes/premiere/music-dropouts.py`).

## 3. The graphics: "the IGN dossier" (V2 plate + V3 overlay, both full-frame at Motion 100)
**Plate (V2)**: the relevant footage, heavily defocused (Gaussian σ≈26 on a half-res copy), brightness ×0.38, saturation
0.85, a slow 1.00→1.04 push over the hold. Sharp footage = showing; blurred footage + type = telling.
**B-roll (V2, no V3 above)**: the same blurred copy as backdrop + the SHARP footage at **85 % inset (1632×918), 22 px
rounded corners, soft shadow (black 45 %, +18 px y, blur 18)**, its own 1.00→1.03 push. (Not the v1 gradient mattes.)
**Overlay (V3)**: an alpha ProRes 4444 HyperFrames comp, transparent over its plate. The look:
- **Type**: Inter (Medium/SemiBold/Bold), warm white `#F4F1EA`, soft text shadow; Anton only for big compare headers.
- **Quote card**: pink open-quote glyph, the quote in Inter Bold sentence case left-aligned in the upper-left third,
  the ONE load-bearing phrase gets a **hot-pink `#FF3E9A` underline that draws left→right**; a credit line under it in
  tiny letter-spaced caps at ~60 % white (`ROB NELSON · ROCKSTAR NORTH · TO IGN, 7 OCT 2026`). A strike-through turns a
  word grey and the corrected word pink.
- **Accents**: one at a time — GTA-yellow `#F5C518` = a marker / where you are, hot pink = the point / a loss.
- **UI pieces** (flat, 1.5–2 px strokes, generous spacing): a minimal dark phone with message bubbles + read receipt +
  typing dots; a "mission line" (thin rail, yellow M markers, pink segments, tags); a numbered 2-column list; a
  2-column compare with an Anton header each side and a divider; a flow diagram that draws node by node (icons in
  circles, curved edges, labels + tiny caps sublabels, pink for the bad branch); a value meter (yellow bar, pink loss
  label); a checklist with ticks (the joke item struck through); a dotted map; an app tile with a gradient icon; a real
  headline capture inset with a pink highlight sweep under the headline.
- **Motion**: elements rise ~14 px + fade + blur-to-sharp over ~10 frames, ease-out, staggered 3–4 frames; nothing
  bounces or pops; highlights draw in ~12 frames; whole graphics hard-cut in and out.

## 4. The sound
| layer | what | level (clip gain → target peak) |
|---|---|---|
| A1 voice | Amplify (measured) + Hard Limiter −6 dBFS (0.94) | kept speech → −17 LUFS |
| SFX (A2/A3) | **premium palette, never meme sounds on graphics**: `whoosh-soft-airy` on a whole-graphic entrance · `pen-line` when an underline/highlight draws · `ui-tick-glassy` per list item / marker · `ui-tick-dull` on a b-roll entrance · `soft-confirm-chime` on a completed state · `msg-chime-calm` on a phone message · `paper-slide` on a headline capture · `latch-lock` on a lock · `riser-clean` into the payoff · `whoosh-soft-impacts` on a big flip | whoosh −12 dB (−20 dBFS) · pen −15…−19 (−22) · ticks glassy ≈−1…−3 (−18…−20) · tick dull −6…−10 (−20) · chimes −5 (−18) · msg +4.7 (−12) · paper −15 (−18) · latch −16…−18 |
| music (A4) | the creator's Epidemic beds, one per section, a ~0.45 s silence before each turn: **Loungin – Scientific** (−20, cold open; −23 for the payoff/outro) · **First Born – Timothy Infinite** (−24) · **Take a Ride – Scientific** (−25, from its 10.3 s entrance) · **Brooklyn – Dyalla** (−24) | static clip gain, no keys, OUT under every cut zoom |
Files: `projects/gta6-ign-missions/sfx/` (Epidemic downloads).

## 5. Definition of done (a draft in this style)
~24 visible changes/min; face ~60–65 %; graphics ~3.3/min of 4–8 s; cut zooms ~6–7/min at 130–140 % (one extreme, 1–2
stretch gags); every graphic = plate + overlay with its premium SFX; b-roll inset over its own blur; music beds under
the voice, out under every zoom; no gap or face sliver at any graphic edge; end cold on the face.
