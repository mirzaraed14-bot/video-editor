# Shorts style radar: what other channels do that ours doesn't

Affan, 2026-11-05 (Herjavec H1 review): "go through different types of channels and pick out what we can integrate into our own style and
make it unique ... I really want to improve our shorts every single day by 1%." Add a dated section per pass. What each Short actually took goes in
`presets/youtube-shorts/scott-clary/UPGRADES.md`.

Method: his Chrome, player muted, paused, frames drawn on a canvas and `getImageData` for the numbers (memory `feedback-bolt-motivation-look`). Nothing downloaded,
no audio. 16 frames per Short: frames only show layout, grade and text, so cut rate and sound are NOT read here.

## Pass 1, 2026-11-05
Luma percentiles and mean HSV saturation over the sampled frames, y 14-84 % of the frame. YouTube's re-encode sits on top.
| Short | Type | Views | Upload | p5 | p50 | p95 | p99 | Sat |
|---|---|---|---|---|---|---|---|---|
| Hormozi, "Dumb People or Dumb Systems?" (wfCHrGKaESw) | business, live room | 176K | 1080p | 1 | 44 | 237 | 254 | .38 |
| Cleo Abram, "You're Dead. What Next?" (3Bc2UXVk5ug) | explainer, 3D graphics | 1.1M | **2160x3840** | 11 | 57 | 199 | 234 | .43 |
| Modern Wisdom, "Why WWII Was So Traumatic" (DI6Vf3ybTdQ) | podcast, face only | 307K | 1080p | 10 | 72 | 225 | 255 | .27 |
| Johnny Harris, "Google Docs to its limit" (fkoyGkCfwi4) | podcast, two faces | 339K | 1080p | 13 | 41 | 179 | 254 | .41 |
| DOAC, Mark Cuban (eLh-KTuJ1u4) | podcast + bespoke MG | 63K | 1080p | 0 | 46 | 220 | 255 | .47 |
| MrBeast, "What's Inside My Briefcase?" (CEJXqm2eiJ0) | action | 127M | 1440x2560 | 13 | 108 | 205 | 232 | .40 |
| **OURS, H1 check 1, face shots** | podcast | | 1080p | **39** | 118 | **175** | **193** | .36 |
| **OURS, H1 with POP grade + sharpen** (`workflows/grade-picture.py`) | | | | 3 | 100 | 203 | 248 | .37 |

**The read:** "bland" is measurable. Our blacks sat at 39 where every reference sits at 0-13, and our whites stopped at 193 where they reach 232-255. Saturation was not the gap: Modern Wisdom is at .27 and looks rich, because it has real
blacks. A per-channel S-curve turned Robert orange (hue 28, sat .59) so the contrast goes on luma only; his skin measures hue 25, sat .37 after the grade (Bolt: 16-24, ~.44).

### What each one does that we don't
- **DOAC / Cuban:** every graphic is a bespoke full-frame WORLD for that one line: a newspaper "CUBAN TO BUY MAVERICKS" with a halftone cutout of him and jersey puzzle pieces, a subway-map chart, trading cards, a whiteboard stat in a staged office. Our receipts are one layout, a photo on a blurred plate. White title box under the captions, name in it.
- **Hormozi:** opens on a two-camera stack, speaker on top, the other person below, the hook in a RED box on the seam, captions under it, a credential lower-third at 4 s. Layout rotates: full, stack, wide.
- **Modern Wisdom:** 307K with zero graphics, on a rich grade and two focal lengths. White title box under the captions.
- **Johnny Harris:** captions on a coloured highlight bar. Cuts to the listener and to a wide of the room. A full-colour end plate.
- **Cleo Abram:** native 4K upload. A hand reaching into the lens in frame 1. Numbered neon stages ("1. AUTOLYSIS") so the viewer sees progress; a circular lens mask for "looking inside".
- **MrBeast:** no text at all, something moving in every frame. Not transferable to a seated podcast beyond "never a still frame".

Upload size: the two biggest in this set upload above 1080p. **Hypothesis, not measured:** a 2160x3840 master gets a better encode on YouTube. Test it on one Short.

### Effects catalog pass (CATALOG.md + all 137 stills, 2026-11-05)
On Scott Shorts so far: DOC cards on a blurred plate, FIT clips, whips, hook card, captions, a few counters. **Never used on this channel and fitting a seated podcast:**
FX-13 Depth-Sandwich Type · FX-71 Funnel Count · FX-22 Red Isolate Photo (colour as story) · FX-55 Red Pen Underline / D2 marks on a photo · FX-44 Halftone Push · FX-16 Portal Zoom · FX-18 Karaoke Leader Quote · FX-27 Red Word Quote · FX-37 Ghost Dissolve · FX-11 Rival Colour Split · FX-23 Pointer Tag · FX-41 Year Ghost · FX-78 Cinema Vignette Montage · FX-25 Exhibit Grid · FX-19 Concrete Sticker Board.
Overused, rest them: the same photo card with a tilt and a whip into it, on every receipt.

## Pass 2, 2026-11-09 (AffanWiz Short 4 `stop-remaking-viral-shorts`): Shorts ABOUT Shorts, the niche's current top
Method: YouTube search HTML fetched same-origin from a robots.txt tab in his Chrome, Shorts filter (`sp=EgIQCQ%253D%253D`), then each Short's
three auto-frames (`i.ytimg.com/vi/<id>/hq1|hq2|hq3.jpg`, 25/50/75 %) + its vertical cover, laid out in the tab. No player, no sound.
A Short's storyboard sprite is only 48x27 (useless); the hq1-3 frames are the silent read for Shorts.
| Short | Views | Length | What it does |
|---|---|---|---|
| KeeanSocial "5 Second Trick to get WAY MORE Views on YouTube Shorts" (`tT1JRa28iL0`, 2022) | 10M | 7 s | bright close talking head, a physical YouTube play-button prop in frame 1, one-word yellow captions |
| vidIQ "How to Get More YouTube Shorts Views in 2026" (`p2O2HP0vKV0`) | 3.8M | 8 s | talking head + phone prop, **green "+ VIEWS"-style growth callouts**, a neon play mark behind him |
| SpactYT "Will Your SHORT Go Viral? (Algorithm explained)" (`kOZ_NM7w7Ac`) | 816K | 12 s | faceless: **green arrows on black ("viral loop"), a rising views line with tier labels**, FULL VIDEO BELOW |
| Topic search "stop copying viral shorts" | | | nothing above 61K; the "YouTube cut reach for reposts" explainers sit at 53-886 views: the news angle is saturated and weak |

**The read:**
- The niche's hits are ONE idea in 7-12 s. Ours is 44 s, so every beat needs its own picture: one scene per beat, not one card per Short.
- **Green is the niche's growth colour** (vidIQ, SpactYT): his green call for Short 4 fits the category.
- A rising graph or bar is the shared payoff picture. Ours draws its 100x bar to scale and breaks the frame instead of a generic arrow.
- The receipt-news angle ("YouTube cut reach") is dead on its own, so Short 4 leads with the call-out ("complete noob") and puts the receipt in the middle.
