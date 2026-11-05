# Bolt Motivation: the upscale + grade look (research, 2026-11-05)

Affan's ask: "this channel I really like his Topaz, how he upscaled it. It looks very realistic, somewhere it looks very
pasty, but normally it looks very realistic ... frame by frame analysis on how he upscaled it and try to replicate that on our
shorts and also try to copy the color grading of him as well."

Channel: https://www.youtube.com/@BoltMotivationYT (2.2M subs). Seen in his Chrome, muted, paused frames at the 1080x1920
rendition, drawn 1:1 on a canvas. Nothing downloaded. YouTube's own re-encode sits on top of every frame here, so grain and the
finest texture read lower than in his master.

## Shorts studied
| Short | Source type | Upscale read |
|---|---|---|
| Z34LiwjhPzs Comedian / Letterman (92k) | 2000s doc + DV home video | The reference: real skin. Pores, wrinkles, blotches, stubble all there, no wax. Speculars clip. Faint halos. |
| b5rTExvwUMM Millionaire game show (140k) | SD TV 2000s, closest to La Toya | Clean, faintly painted: eyes + hair strong, forehead smooth. Black backdrop stays pure. |
| W3q6bLmMzIU NFL tricks team (5.2M) | modern HD | Crisp, pushed micro-contrast, punchy colour. |
| -Yg3qkLvK5s Viral judge clip (142k) | phone/news, very low res | The "pasty" one: no real upscale, plain soft enlargement, no invented detail. He leaves a hopeless source soft, or gives it a halftone/dot texture as a treatment. |

## Upscale read (what it IS, not which button)
The frames can't prove the Topaz model or sliders. They show what the result does:
1. Skin keeps high-frequency luminance texture. It is never smoothed, and that's the whole "realistic" impression.
2. Micro-contrast is pushed after the upscale (a clarity-like lift): wrinkles and pores read at phone size.
3. Specular highlights are allowed to clip; that wet, contrasty skin reads expensive.
4. No visible added film grain at 1080p (YouTube may eat a light one).
5. Eyes are the sharpest thing in frame, and no faces are re-invented.
6. A hopeless source is left soft rather than hallucinated. Soft beats fake.

## Grade, measured (median of 12 frames per Short, y 14-84 % of the frame, 8-bit RGB as served)
| Short | Luma p1 / p5 / p25 / p50 / p75 / p95 / p99 | Shadow RGB | Mid RGB | High RGB | Sat | Skin hue / sat / Y |
|---|---|---|---|---|---|---|
| Letterman | 16 23 42 82 127 201 253 | 35 32 29 | 102 87 89 | 210 196 197 | .29 | 18.9 / .33 / 116 |
| Game show | 3 7 15 47 99 171 255 | 19 19 23 | 116 91 83 | 207 208 198 | .32 | 20.3 / .44 / 112 |
| NFL | 3 16 50 98 148 232 255 | 26 31 47 | 108 96 98 | 215 201 185 | .37 | 23.3 / .44 / 128 |
| Sharks | 5 13 43 83 135 212 229 | 39 23 32 | 132 94 87 | 225 188 171 | .39 | 17.7 / .49 / 120 |
| She fainted | 9 23 73 119 157 212 253 | 35 24 40 | 114 106 145 | 192 197 221 | .54 | 16.2 / .44 / 120 |
| Mom kicked out | 0 9 39 76 122 213 255 | 32 24 28 | 89 94 102 | 208 198 202 | .36 | 24.2 / .45 / 104 |
| Judge | 22 41 74 114 163 220 251 | 39 33 27 | 105 96 82 | 213 190 176 | .22 | 24.4 / .45 / 105 |

Read: skin sits at Y 104-128 (bright mids, hue 16-24°, sat ~.44). Blacks are deep, p5 ~7-23. Highlights reach 250+. There's no one
LUT tint: neutral-to-cool shadows, warm skin, each source keeps its own colour. It's a contrast + clarity look, not a teal-orange wash.

## Layout seen (for reference, same family as ours)
Full-bleed always: a letterboxed band has a blurred twin filling the screen top and bottom, never black. Band edges carry a thin
white line with a soft glow. Captions sit mid-frame.
