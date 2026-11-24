# KINDS7: batch-7 graphic kinds + entrance signatures

Module `tools7/kinds7.py` (patched in at import over mgx6 -> mgx -> overlays; nothing on disk changes for anyone else).
CLI = mgx6's, via the wrapper `tools7/mgx7.py`:

    PYTHONUTF8=1 python projects/_onyx-batch7-2026-11/reactions/tools7/mgx7.py <job>/plan.json [--captions] [--mg] [--only id,id] [--check] [--still t ...]
    bash projects/_onyx-batch7-2026-11/reactions/sem.sh python .../mgx7.py <job>/plan.json --mg      # heavy renders go through sem.sh

`--still t ...` also writes one full-size `work/still-<t>.png` per time. Plan conventions: `plan["box"]` = `[0,227,1080,1038]` (top panel);
times `t0`/`t1` are sequence seconds; keys named `*_at` / `at` are **seconds after t0** unless the key says `t_abs`.
Output: `overlays/mg/<id>.mov`, 1080x1920, 60 fps, ProRes 4444 + alpha, exactly (t1-t0) long.
Suggested SFX per kind: `kinds7.suggest_cues(g)` (symbolic names `paper-slide`, `wood-tap-a/b`, `air-pass`, `marker-stroke`); `O.default_sfx` returns them as `cues`.

## Entrances (plan["entrance"] or g["entrance"])
`tilt` (0.42 s) | `slab` (0.46) | `foldx` (0.48) | `swing` (0.46) | `shutter` (0.40), exactly as NEW-KINDS.md. Exit = the same animation backwards, 30 % faster.
5 premultiplied sub-frames of motion blur on every transition frame. Work on every sprite kind (label, title_card, chip, channel_card, stat, steps,
checklist, compare, lower_third, hook_title, rows_blur, quadrant, scorecard) and on teaser, teaser2, still_card, era, source_tag, low_title
(their HOLD frame is transformed as one layer; their own entrance never shows). `riseup` = an internal default (play_card/portal when the entrance is not one of the five).
NOT applied to screen-locked marks (ring, select, spotlight, cursor, loupe, timecode, scrub, hl_sweep): a tilt or swing would move them off their target, so they keep their own fade. Others (comments, wave_cut, episode_bar, audience, filler_strip, bars, grid, stage_*) keep their own motion.
Slab and foldx slide the card's printed content inside its silhouette (the flattened sprite's RGB is shifted, alpha kept), so a card's 2 px border shifts a few px during the first 0.3 s.

## play_card (opaque ProRes over the panel; their Short or our sample plays)
Keys: `file`, `src_t0` (file seconds at t0), `muted` (info for the audio builder: audio from the file on A2, OBS muted), `handle` ("@andrewgoldheretics": THEIR Short, red YT glyph tag
docked 14 px left of the card's bottom-left) | `tag` (OUR sample pill, e.g. "OUR EDIT · YOUTUBE LOOK") + optional `tag2` (small line under the pill),
`push` (0.03, whole beat, ease in-out sine), `panel` ([0,227,1080,1038]), `entrance`.
Card 416x739 (panel height - 72), r 22, 2 px white keyline 70 %, 36 px shadow; backdrop = same file cover-scaled, blur 40, x0.45, crossfades in over 0.2 s;
the card rises 60 px with the signature. **No exit** (cut on a V1 edit). The backdrop crossfade shows whatever is under the panel for 0.2 s: keep the Claude app out of that view.
`{"id":"pc1","kind":"play_card","t0":12.0,"t1":22.5,"file":"X:/.../heretics.mp4","src_t0":3.0,"handle":"@andrewgoldheretics","muted":true}`

## portal (A -> B inside the panel, then B plays)
One graphic = A playing, the 0.5 s crossing at `at`, B playing. Keys: `a_file` + (`a_src_t0` plays A from there | `a_t` = a held still), `a_handle`/`a_tag`/`a_tag2`;
`b_file`, `b_t` (B's file seconds at the crossing; B plays on from there), `b_tag`/`b_handle`; `at` (s after t0), `push`, `enter` (default true: A enters like a play_card; needs at >= 0.5),
`entrance`. A 1.0 -> 1.9, B 1.35 -> 1.0, 7-copy radial zoom blur 0 -> 24 px, gold 2 px ring at 0.2 s. Audio for B = `b_file` from `b_t` at t0+at.
`{"id":"pt","kind":"portal","t0":20,"t1":27,"a_file":"X:/.../heretics.mp4","a_src_t0":10,"a_handle":"@andrewgoldheretics","b_file":"X:/Exports/x.yt.final.mp4","b_t":1.0,"b_tag":"OUR EDIT · YOUTUBE LOOK","at":3.0}`

## scorecard (THEIRS vs OURS)
Keys: `rows` (1-5) = `[[t_abs, "HOOK", theirs, ours], ...]` where theirs/ours = text or `{"count":135,"suffix":" s"}` (counts up, OURS gold, THEIRS white), `low` (true: y 1150-1600, w 960), `w`,
`x`,`y`, `recap` (t_abs: rows not yet shown appear together at that moment, OURS with no 0.18 s offset; a graphic that starts at `recap` shows all rows at once),
`stage` (mgx stage backdrop), `entrance`. Fails loudly if the rows do not fit or the card leaves y 200-1620.
`{"id":"sc","kind":"scorecard","t0":28,"t1":36,"rows":[[29,"HOOK","a vague title","the money line first"],[30.2,"LENGTH",{"count":135,"suffix":" s"},{"count":41,"suffix":" s"}]],"stage":{"in":0.3,"out":0.3}}`

## hl_sweep (read-along highlighter on a real page)
Keys: `box` (plan.boxes name or literal source px [x0,y0,x1,y1] of the OBS frame, follows the view per frame), `box2` (second line), `at` (0.3), `at2`, `dur` (0.45), `dim` (0.40), `strength` (0.42), `panel`.
Gold #F2C14E marker (0.9 x line height, r 3) sweeps left -> right; the swept part of each line stays lit while the rest of the panel dims to 60 %.
**Deviation:** an alpha overlay is composited normal-blend (not multiply) and cannot turn grey page text white; the line keeps the page's own brightness, everything else dims. Set the clip's blend mode to Multiply in Premiere for a true multiply marker.
`{"id":"hl1","kind":"hl_sweep","t0":42,"t1":46,"box":"title","box2":"subs","at":0.3}`

## inset_cam (his live face over a full-window screen beat)
Keys: `cam` (camera file), `cam_offset` (cam t = OBS t + offset, from the sync JSON `offset_s`), `face_x` `[x, mouth_y]` in camera px (the same pair facex6m / plan face[] carry; eyes = mouth_y - `eye_dy`, default 160),
`crop_h` (900 camera px shown in the inset; eyes land at 38 % of the inset height), `cam_size` ([1920,1080]), `rect` ([744,1190,300,400]). OBS time comes from the screen track's clips (`O.seq_pieces`), so cuts inside the graphic are followed (one camera seek per piece).
300x400, r 28, 2 px keyline 80 %, 30 px shadow; in: scale 0.92 -> 1 + fade 0.28 s; out: reverse 0.2 s.
`{"id":"ic","kind":"inset_cam","t0":47,"t1":55,"cam":"X:/Recordings/Onyx/C1455.MP4","cam_offset":72.14,"face_x":[1160,570]}`
