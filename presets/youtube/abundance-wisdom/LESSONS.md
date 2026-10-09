# Abundance Wisdom long-form: LESSONS

What the creator's reviews taught, newest first. Format: *lesson → change made → file*. A lesson that repeats becomes a
rule in this folder's README/PLAYBOOK (none yet: the look still lives in each job's BRIEF.md + storyboard).

## 2026-10-08 · SAME NIGHT (nick-martin-same-night), cold open v1 review

1. **The voice is the loudest thing in the mix.** His music clips sit at 0 dB (-15/-16 LUFS) over a voice that
   integrates at about -29 LUFS: on his timeline the music played 12-14 LU OVER him. → Music bed re-levelled 12 LU (the
   intro) / 14 LU (the rest) under the measured voice, swelling only in real voice gaps (titles, cards).
   → `projects/nick-martin-same-night/level-music.py`, `brief/music-levels.json`.
2. **SFX were far too loud.** I matched his Seq 24 camera flash (-6.6 dBFS) without measuring the voice under it.
   → SFX peaks ~7-8 dB under the voice PEAK (-15.5 dBFS): hits ≈ -23, whooshes ≈ -31, beds ≈ -34; fewer cues.
   → `projects/nick-martin-same-night/audio/sfx/make-cues.py`.
3. **A preview has to play the real mix.** v1 used a flat -9 dB music guess. → `preview.py` now reads every clip's
   Level (static or keyframed) live from Premiere and applies it in source time.
4. **The pacing is slow and cinematic, never a bombardment.** Fast cutout entrances, slams, white flashes and 700 px
   slides under short VO lines read as "boom boom boom". → entrances 0.8-1.5 s, soft dissolves, slow continuous camera,
   one accent per beat, quiet type instead of stamps. → `hf-graphics/make-comps.py` (cold open v2).
5. **Generated props follow his staging literally.** The pro card had to stand UPRIGHT on a table under a light from
   above, with a gentle push (v1 lay flat with a 1.34x zoom). → regenerated in Higgsfield, push 1.00 → 1.06.
6. **Title and chapter cards come from the catalog move he likes: FX-12 (Tumbling Debris Chapter).** v1's shafts-and-
   embers title was my own invention. → t01 rebuilt as FX-12 (black hold, navy-crimson space, tumbling medal / trophy /
   plate / dumbbell with depth of field, Montserrat ExtraBold gold title with orange glow, letters assembling from blur).
   Every treatment names its FX code (`research/effects-catalog/CATALOG.md`).

## 2026-10-08 · SAME NIGHT cold open v2 review ("better, not perfect")

7. **SFX must feel refined and premium, never goofy, and there can be MORE of them.** The "magic shimmer" on the Sandow
   lift read as goofy. → One cinematic palette for the whole video: reverse-cymbal swells into reveals, low reverberant
   thuds on them, soft airy whooshes on dissolves/entrances, an analog shutter on freezes, low booms; retired: magic/
   twinkle, UI glitch, electric sparks, keyboard typing, cartoon/meme anything. → `audio/sfx/fetch.py` (v3 picks),
   `audio/sfx/make-cues.py` (v3 sheet, 21 cues in the cold open).
8. **On a title card the type is the subject; props stay in shadow.** The FX-12 props were too bright and sat in the
   title band. → props at brightness .38-.5, more blur, lower opacity, kept out of the title band, a dark pool behind
   the type. → `hf-graphics/make-comps.py` t01 (v2.1).
9. **Don't iterate one section forever.** "I don't have all day just to correct this intro": apply the lessons and carry
   them through the whole video in one pass.

## 2026-10-08 · SAME NIGHT whole-video v1 review (the fix list)

10. **Every move eases in AND out (his "easy ease").** Linear drifts (title debris, the space push) and one-sided
    `sine.out` entrances read as things that start or stop dead, worse on the 20 fps stepped look. → house default
    `gsap.defaults({ease: 'sine.inOut'})`, `soft()` and `camera()` on `sine.inOut`, every `.out` on a move converted.
    Linear stays only on textures (the VHS scan band) and a progress bar. → `hf-graphics/tools/ease-pass.py`.
11. **A graphic's last build must FINISH with time to read before the cut.** Measured (every comp's last tween vs its cut,
    probed in the browser): ~20 comps landed < 0.6 s before cutting to him or to the next graphic. → when the host follows,
    the comp HOLDS its finished frame up to 1.5 s into that host time (`make-comps.py` HOLD, from `brief/room-after.json`);
    when another graphic follows, the last build lands earlier. Target: ≥ 1 s settled. → `hf-graphics/tools/hold-pass.py`.
12. **A name-intro freeze zooms SLOWLY.** c14 pushed 5 % in 1.5 s ("a very sharp zoom"); that whole stretch of the video is
    slower. → ≤ 2.5 % across the whole comp from frame 0, the darkening over 1.3 s, the comp held 1.5 s longer.
13. **Where a third party SPEAKS on screen, give them real subtitles.** → Montserrat 700, warm white, soft shadow, balanced
    lines in the clear band above the tag (the letterbox bar on a 2.39 shot), wording from his script's own transcription,
    timed to the clip's words, swears as a solid bar. → `hf-graphics/subs.py`, `transcript/map-inserts.py`.
14. **No trilling SFX ("sounds like a cricket").** The reverse-cymbal swells (cym-swell, cym-swell-short) and riser-eerie
    are narrow ~2.5 kHz tones broken into 10-30 bursts: crickets. → chirp-free risers (Epidemic rise-low / rise-air /
    rise-whoosh), same events, same levels. → `audio/sfx/cue-pass-v4.py`, `sfx-plan-v4.json`.
15. **When the line names a moment, POINT at it.** "He didn't shake Nick's hand": the walk freezes on Nick, everything else
    dims, an eased arrow finds him under HANDSHAKE IGNORED, and the walk resumes on "but…". → c27 v3 (`chapters2.py`).
16. **The face shot is never perfectly still.** → one eased Scale drift per on-camera run (push-in / pull-out alternating,
    ≤ 3.5 %, 0.35 %/s), keyed on his C1330 clips by name. → `host-zoom.py`.
17. **A one-frame flash of the face at a graphic's head was the RENDER, not the placement.** libx264 B-frames give the mp4
    an edit list that Premiere misreads at the clip head. → every graphic encodes with `-bf 0` (render.sh, both copies).
