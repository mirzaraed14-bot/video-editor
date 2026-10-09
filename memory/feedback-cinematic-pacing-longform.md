---
name: feedback-cinematic-pacing-longform
description: "Affan 2026-10-08: Abundance Wisdom long-form is SLOW and cinematic; FX-12 title cards; every move eased in+out; builds finish >= 1 s before a cut; subtitles on third-party speech; subtle drift on his face shots"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 2af79f46-b1fb-47c3-827d-40eebd325de0
  modified: 2026-10-08T11:17:30.125Z
---

Affan on the SAME NIGHT cold open v1 (2026-10-08): "the pacing of this entire intro is a little bit fast… I want them to
really feel the music, feel the vibe… we're just blasting visuals left right and center"; the two cutouts at the very
first second arrived too fast; "the pacing of this entire video is a lot more slower". The pro card was wrong: he wanted it
UPRIGHT on a table with a light shining down on it and a gentle push, not a hard zoom. The title card style was wrong:
"you have the whole catalog… FX-12 the Tumbling Debris chapter, look at the card concept there".

**Why:** the VO lines are short, so per-word hits (slams, white flashes, fast slides, stamps) stack into a bombardment;
he wants each image to land and breathe under the music.

**How to apply:** entrances 0.8-1.5 s (fades, slow drifts, blur-to-sharp), soft cross-dissolves instead of flash cuts, slow
continuous camera moves (~1.00->1.06), at most one accent per beat, quiet type instead of stamps; generated props follow
his staging literally; title and chapter cards use the FX-12 concept (black hold, deep navy-crimson space, slow tumbling
props with depth of field, heavy gold Montserrat title with orange glow, letters assembling from huge blurred scale, drift
toward camera, fade to black). Built graphics render STEPPED at ~20 fps on the 60 fps timeline (his ask the same day:
"intentionally low FPS… gives off a nice cinematic look"; render.sh STEP_FPS=20, catalog FX-81); real footage stays smooth.
Pick every treatment from the FX catalog (research/effects-catalog/CATALOG.md) and name the
code.

Whole-video v1 review (2026-10-08, later): EVERY move eases in and out ("easy ease keyframes… they don't just suddenly stop": no linear, no one-sided ease-out on a move); a graphic's last build FINISHES with >= 1 s to read before cutting to him or the next graphic (hold the finished frame into his face time, or land the build earlier); name-intro freezes zoom slowly (<= 2.5 % over the whole beat); third parties speaking on screen get REAL subtitles; when his line names a moment, point at it (freeze + dim + arrow + label: "he ignored the handshake"); his face shot always carries a subtle eased drift (<= 3.5 %, never static). Lessons 10-17 in presets/youtube/abundance-wisdom/LESSONS.md.
Related: [[feedback-voice-first-mix]], [[reference-premium-doc-channels]], [[project-abundance-wisdom-longform]].
