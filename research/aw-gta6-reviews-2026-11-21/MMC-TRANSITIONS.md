# Music Media (@musicmediaco) transition study (23 Nov 2026, "Streamers Rated GTA 6")

Method: three GTA 6 / GTA 5 Shorts downloaded whole (pace.sh, H.264), stills only (nothing played). Cuts found from per-frame difference, then every cut read frame by frame at the clip's native fps (contact sheets, frame numbers stamped in yellow). Numbers marked MEASURED come from the pixels (mean luma 0-255 and an edge-sharpness metric per frame on the clips' own frames). Anything marked FIT or START VALUE is my proposed implementation, not a measurement. Counts for the two non-iLVj Shorts are read from contact sheets by eye. Audio could not be listened to; it was read as 40 ms RMS and high-frequency ratio (weak evidence, see 4).

Files: `projects/gta6-reviews-compilation/overlays/mmc/` (videos) and `overlays/mmc/sheets/` (all sheets named below). API raw: `overlays/api/mmc-*.json`.

## 1. The three Shorts

| ID | Title | Views (23 Nov) | Length | Spec | Role |
|---|---|---|---|---|---|
| iLVjl8TT74Y | this is why GTA 6 took 13 years | 154,348 | 23.7 s | 1080x1920, 60 fps | closest to our video: face cam <-> GTA footage |
| vcWryhX1sI0 | GTA 6 was made for our generation | 104,226 | 14.5 s | 1080x1440 (3:4), 24 fps | brand-heavy (logo stingers, glitch) |
| -V7fzWgu3Fg | Goodbye GTA 5... | 1,119,742 | 57.4 s | 1080x1920, 23.976 fps | 16:9 clips letterboxed in the middle, hard cuts + dips |

Overview sheets: `sheets/iLVj_overview_a.png`, `iLVj_overview_b.png`, `vcWr_overview.png`, `V7fz_overview.png`.

## 2. Transition catalogue (frame counts at each Short's native fps)

### T1. Radial zoom-blur + white flash cut ("the MMC cut") — the signature: 9 of the 19 cuts in the two GTA-6-framed Shorts (6 of 8 in iLVj)
Seen 6 times in iLVj (2.27, 3.85, 5.50, 8.35, 10.92, 16.93 s, MEASURED below), 3 times in vcWr (239, 251, 303: pink-tinted variant, same idea at 24 fps, not measured the same way). Sheets: `iLVj_cut2.267.png`, `iLVj_cut_f231.png`, `iLVj_cut_f330.png`, `iLVj_cut_f501.png`, `iLVj_cut_f655.png`, `iLVj_cut_f1016.png`; pink variant `vcWr_cut_f239.png`, `vcWr_cut_f251.png`, `vcWr_cut_f303.png`.
Measured on the six iLVj instances (60 fps; n = the first frame of the NEW clip):
- n-2, n-1 (2 frames, 33 ms): OUTGOING clip under a heavy radial (zoom) blur centred on the frame centre. MEASURED sharpness falls to 0.17-0.45 of normal over the six instances (e.g. 33 -> 12 at 2.27 s, 36 -> 6 at 10.92 s). The outgoing clip is already at its punch-in scale (1.6-1.7x, see 4).
- n (the hard cut, hidden by the flash): INCOMING clip appears under the same radial blur (MEASURED sharpness 0.45-0.58 of normal) and a white exposure flash: MEASURED mean luma peaks at +32 to +111 above the incoming clip's own settled exposure (2.27 s: 189 vs 122 settled; 5.5 s: 187 vs 131; 10.92 s: 218 vs 169; 8.35 s: 180 vs 115), i.e. 45-57 % of the way to white (alpha = (peak - base) / (255 - base) = 0.50, 0.45, 0.57, 0.46). Faces blow out to near-white silhouettes.
- n .. n+4 (5 frames, 83 ms): MEASURED: sharpness holds near 0.5 for 5 frames and the picture is at full sharpness from frame n+5 (it looks like a smooth release in the sheets, the metric is flat then steps).
- n .. n+16: MEASURED, the flash decays linearly (about -4 luma per frame at 60 fps) over 16-20 frames (267-333 ms) to the new clip's own exposure, then holds flat (checked on 2.27, 5.5, 8.35, 10.92 s). No ease on the decay.
- Total: 2 frames build + 1 cut frame + 4 frames blur + a 16-frame exposure tail. At 60 fps the "heavy" part is 7 frames (117 ms); at 30 fps it is 1 + 1 + 2-3 frames, tail 8 frames.
- Captions sit on top of all of it, untouched, and keep running through the cut (the caption layer is separate).
- Recipe (START VALUES, tune by eye against the measurements above; the blur amount in Premiere units was NOT measured, only the resulting sharpness ratio): outgoing clip, last 2 frames: radial/zoom blur centred on the frame centre, strong enough that sharpness drops to ~0.3 of normal. Incoming clip, frames n .. n+4: the same blur at about half that strength (sharpness ~0.5 of normal), off at n+5. Plus a white overlay (or Exposure lift) layer: ~50 % white on frame n, linear to 0 over 16-20 frames at 60 fps (8-10 at 30 fps). Hard cut at n, no crossfade. Whether the incoming clip starts at 100 % scale was NOT measured (it looked unscaled in the sheets; the blur hides the first frames).
- Variant seen once (iLVj 3.85 s, `iLVj_cut_f231.png`): a 10-frame brightness build BEFORE the cut (luma 116 -> 176, 0.17 s) instead of the 2-frame build, then the same blur/cut/decay.

### T2. Tinted-flash hard cut with a logo/overlay pop (no blur)
iLVj 9.93 s (f596, `iLVj_cut_f596.png`): hard cut, whole frame gets a magenta/pink colour grade (luma 114 -> 160), the GTA VI logo overlay is stamped over the new clip; the tint decays linearly over ~25 frames (0.4 s). vcWr 1.54 s (f37, `vcWr_cut_f37.png`): hard cut at 24 fps, GTA VI logo pops at ~2x scale and settles to 1.0 in 4 frames (ease-out), luma +40 on the cut frame decaying over 3 frames. Used when a logo appears with the new shot. Counted: 1 in iLVj, 4 in vcWr (37, 286, 317, 337: 317 and 337 are plain hard cuts with a white-out of 1-2 frames and a 4-12 frame fade, 286 a pink wash into a logo), 2 in -V7fz (green tint at 7.0 s and 16.9 s).

### T3. Dip through black (fast)
-V7fz, the GTA-world flythrough, every ~3.6 s from 28.8 s to 50 s (28.78, 32.82, 35.9, 39.3, 43.25, 46.84, 50.05 s), 7 times. Sheet `V7fz_push_f1037.png`. Pattern at 24 fps: the clip darkens over 2 frames (1036 -> 1038, black on the last), then the next clip fades in from black over ~10 frames (0.4 s) with a fast-then-slow (exponential) curve; frame-difference decays exponentially, not linearly. No blur. Mood-setting, not punchy; it suits wide establishing shots with no face.

### T4. Glitch / datamosh slice (2-3 frames)
-V7fz 3.17 s, 4.55 s, 11.6 s, 15.6 s (`V7fz_cut_f76.png`, `V7fz_cut_f109.png`, `V7fz_cut_f278.png`, `V7fz_cut_f374.png`), vcWr 11.29 s (`vcWr_cut_f271.png`). The two clips are cut into horizontal slices offset sideways with RGB speckle for 2-3 frames (at 24 fps: 83-125 ms), the new clip arrives sharp on frame 3-4; sometimes followed by a white wash (V7fz 15.6 s) or a dip to black (V7fz 11.6 s). 5 uses in the 58 s Short (3.17, 4.55, 11.6, 15.6 s and a red-flash glitch at 22.86 s, `V7fz_cut_f548.png`), 1 in the 15 s.

### T5. Whip / motion-blur dissolve (1-2 frames)
-V7fz 1.96 s (`V7fz_cut_f47.png`): one horizontally blurred frame at the cut, new clip arrives blurred and sharpens in about 6 frames. Used once.

### T6. Brand stinger (M logo)
vcWr 7.04 s (`vcWr_cut_f169.png`): zoom-blur frame -> 1 black frame -> logo scales 2.5x -> 1.0x in ~8 frames and sits 1.2 s -> logo scales back up 1.0 -> 3x over 2 frames into the next clip (`vcWr_cut_f202.png`). Channel branding only; do not copy.

### T7. Plain hard cut
iLVj 0.78 s (`iLVj_cut_f47.png`: no blur, no flash), most of -V7fz. In iLVj the Short opens on a hard cut, then every following cut is a styled one.

Not edits (do not mistake them): iLVj 6.25 s and 7.05 s are the creator's own phone-feed scroll inside a screen recording.

## 3. Counts, and THE one transition

| Short | Cuts | T1 radial+flash | T2 tinted flash/logo | T3 dip to black | T4 glitch | T5 whip | T6 stinger | T7 hard |
|---|---|---|---|---|---|---|---|---|
| iLVj (23.7 s) | 8 | 6 | 1 | 0 | 0 | 0 | 0 | 1 |
| vcWr (14.5 s) | 11 | 3 | 4 | 0 | 1 | 0 | 3 (169, 202, 295) | 0 |
| -V7fz (57.4 s) | ~19 | 0 | 2 | 8 (7 dips + end fade) | 5 | 1 | 0 | 3 |

(iLVj is exact. vcWr and -V7fz were read cut by cut from the sheets and classified by eye: +-1 on any cell, and a few -V7fz hard cuts may hide a short dissolve.) Across the two GTA 6 Shorts that mix faces and game footage (iLVj, vcWr), T1 is the single most frequent type (9 of 19 cuts); in iLVj, the Short most like ours, it is 6 of 8 cuts, i.e. the transition to apply clip-to-clip. The 1.1M-view Short (-V7fz) does NOT use it at all (it is a GTA 5 nostalgia montage of archive clips: hard cuts, glitches, dips), so MMC has no single house cut across all three; T1 is the house cut of the GTA 6 Shorts that cut between a face and game footage.

**THE ONE: T1, radial zoom-blur + white flash cut**, built exactly as in 2/T1 with a punch-in on the outgoing clip (section 4):
- Outgoing clip: final ~0.5 s push 1.0x -> ~1.6x (ease-in-out; measured on 2 shots, see 4), last 2 frames radial blur at full strength (sharpness ~0.3 of normal).
- n: hard cut; white flash ~50 % (measured 30-57 %); radial blur at about half strength for n .. n+4, off at n+5 (sharpness ratio measured, strength numbers are START VALUES).
- Flash decays linearly to 0 over 16-20 frames at 60 fps (267-333 ms; at 30 fps 8-10 frames).
- Timing at 30 fps: blur-in 1 frame, cut frame, 3 frames blur, 8-10 frame exposure tail.
- Place the cut on a word boundary / speech gap so the flash lands on the new beat (in iLVj the caption word changes within a few frames of every cut; not measured to the frame).

**Runner-up: T2, tinted-flash hard cut** (no blur, no scale): colour pop (use the AW accent, not pink) at +40-46 luma on the cut frame (MEASURED 114 -> 160 at iLVj 9.93 s), decaying over about 20 frames at 60 fps (measured -2.4 luma/frame from 160 to 131 over 12 frames, then slower), 10 at 30. Use it for back-to-back beats where a second radial blur in under a second would feel repetitive, or when a graphic/logo/number card lands with the new clip.

## 4. Pacing numbers

- Shot length: iLVj shots 0.78, 1.52, 1.55, 1.65, 2.85, 1.58, 0.99, 6.0, 6.8 s (mean 2.6 s, median 1.58 s; first ten seconds mean 1.4 s). vcWr: mean 1.2 s on 12 shots. -V7fz: mean 1.7 s in the first 23 s, then a fixed 3.6 s metronome for the world flythrough. A long hold (6 s) is a clip that has its own internal motion (jet ski with a dog, a gameplay moment), never a static head.
- Punch-in: MEASURED (scale estimated between frames) on only 2 of iLVj's 9 shots with a clean fit; a third (shot 2, a talking head) showed only ~1.04 drift and no punch, and the jet-ski/dog shot gave noise. So treat 'a punch before every cut' as a pattern seen on 2 clean shots plus the zoom-blur frames of the others, not a proven rule. iLVj shot 1 (Jason, 0.78 -> 2.27 s): 1.00 -> 1.06 drift over the first 0.5 s (~9 %/s), then a fast ramp 1.08 -> 1.63 between 0.55 s and 1.0 s (about +50 % in 0.5 s, peak ~+9 % per 6 frames), settle to 1.68 by the cut. iLVj shot 3 (a face): 1.02 drift, ramp 1.10 -> 1.51 in 0.3 s (frames 273-300), 1.60 by the cut. So on those two shots the cadence is: a punch of about +50 % lands (scale 1.5-1.7x) as the T1 blur begins, with a slow drift of 5-10 %/s before it. The next clip restarting at 1.0 is NOT measured.
- Zoom curve (FIT to the two clean shots, not measured on others) to implement per shot of length L: scale(t) = 1 + 0.07 * (t/0.6) for t < 0.6 s (drift), then from t_p = L - 0.55 s to L - 2 frames an ease-in-out from the drift value up to 1.65 (S-curve, smoothstep). Shots shorter than 1.0 s use the punch only.
- Face cams and game clips both get the punch; b-roll enters a face with T1 and leaves it with T1, always full-frame, never a picture-in-picture or a slide.
- Captions (noted only; ours stay AW style): MMC puts one word at a time dead centre on the frame, white with a green/yellow/cyan/magenta highlight on the active word, and the caption layer is not affected by transitions.
- SFX on cuts: weak evidence only. Frame-aligned 40 ms RMS shows the cut often falls in a level dip of the speech (e.g. -23 -> -41 dB at iLVj 2.27 s, -29 -> -35 dB at 16.93 s) and a high-frequency burst (3 kHz+ share rises from -15 to -1 dB) starting 0.1-0.2 s after the cut at 2.27 s and 16.93 s: consistent with a short whoosh placed ON the radial blur, quiet under the voice. Other cuts (e.g. 5.5 s) show no isolated transient. Treat as "one soft whoosh centred on the cut frame" and verify by ear in review.

## 5. Frame sheets (in `projects/gta6-reviews-compilation/overlays/mmc/sheets/`)
`iLVj_*` (12 files: overview a/b, each cut), `vcWr_*` (12 files), `V7fz_*` (14 files). Frame numbers are absolute frame indices of that Short at its native fps.
