# BRIEF — gta6-ign-missions (Affan Afterhours video 22)

## Walkthrough 1 — "Fixing Video Overlay Gaps" (Tella, recorded 2026-10-09 00:28, 2:00) → `brief/walkthrough-1/`
Files: `guide.mp4` (downloaded from the share link), `transcript.txt` (his narration, word-timed), `frames/`, `full-*.png`.

**Verdict:** "the video itself is pretty good… apart from that the video is pretty solid, I don't have any other complaints."

**The one note — every overlay edge leaves a stray frame of face:** at 00:00:03:20 (his playhead, 0:20 in the walkthrough)
the V1 cut sits one frame BEFORE g01's plate + overlay start, so one frame of his un-zoomed face flashes between the zoom
and the graphic ("this frame has to be filled out, otherwise it makes for a weird distortion… for literally one
millisecond you can see my face even though the viewer is not supposed to see my face"); "this is not the only time…
it's prevalent", "I need you to fix this in all of the overlays". He pushed some back by hand while recording. His
last-resort fill when media runs short: "a slow-mo a little bit… 99 or 98 percent so it's not visible".

**Resolved to:** the plan builder ended back-to-back graphics `0.02 s` early (exactly one frame at 59.94) and never
snapped graphic edges onto V1 cuts. Fixed AT THE SOURCE in `build-plan.py`: every graphic edge within a few frames of a
V1 cut lands ON the cut, and neighbours butt exactly (gap 0). Gate: no gap under 0.8 s between graphics and no face
sliver under 0.3 s at any graphic edge (checked on the plan and on the timeline readback).

**His own re-cut of Sequence 39 (kept as decisions, confirmed in chat 2026-10-09):** jump-cut tightening (~0.25 s at
0:18 and word-edge trims around 1:44–1:56), "Go together and it's his words." trimmed out of the date list (so Rob's
"2-for-1" note on g11 is dropped), and at ~2:57 a re-picked passage (two silent beats + "…are outside ready to bust
your") in place of "Robbing. Lots of robbing. Different types of robbing." His cut is now the source of truth:
`transcript/cuts.his.json` + `v1-cuts.his.json` (`transcript/his-cut.py`), canonical transcript re-derived through it.
