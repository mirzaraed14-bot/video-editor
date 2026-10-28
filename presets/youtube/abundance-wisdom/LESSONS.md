# Abundance Wisdom long-form: LESSONS

What the creator's reviews taught, oldest first. Format: *lesson → change made → file*. A lesson that repeats goes into
[`PLAYBOOK.md`](PLAYBOOK.md) (since 2026-10-26: the gist of the look + the procedure, a starting point and NEVER a style lock;
every video must be ≥ 5 % smoother, more premium and more expensive than the last).

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
18. **On a scripted shoot WhisperX hides the retakes; the cut followed it onto the wrong take (cbum-last-show, 2026-10-19).**
    A false start plus its retake comes back as ONE stretched word ("years." 8 s, "who" 1.5 s), or as the script's words
    painted over the wrong audio (a run with p < 0.4). Neither the take-map nor a stitched-joint re-ASR sees it, because
    Whisper collapses repeats inside one window. 20 hidden repeats survived a first pass.
    → Find the kept take with sub-span re-ASR split at the silences (two clusters of matching length = two takes; trust
      the speech bursts, not faster-whisper's word times, which run 0.3-1 s early).
    → Forced-align the LAST take's known text (`work/realign.py`), with hand pins where the aligner squeezes a slow word.
    → Then let the boundary tools run. A list read slowly ("2020… 2021…" at 1.1 s each) is NOT a false start; count the
      clusters. "Last take" means the last COMPLETE take: two restarts that broke off before the line's last word are false
      starts (decide with a forced-alignment fit of the full text, `fit_test.py`). Last gate: `cluster_sweep.py`, every
      segment's clusters re-heard alone, 0 repeats. → `projects/cbum-last-show/work/` (`slice_asr.py`, `joint_asr.py`, `realign.py`, `words_patch.py`,
      `rebuild.sh`).
19. **Host grade: the creator took the colour LUT and DECLINED the vignette (cbum-last-show, 2026-10-20).** The LUT pulls the
    violet wall to slate (saturation 0.68 → 0.42) with skin protected; without the vignette, corners/centre stays ~1.2. Don't
    re-add a vignette unasked. Apply the host LUT as a MASTER-CLIP effect on the host's source item: it never touches archive
    inserts and survives re-replays (Premiere 25 cannot script the LUT slot; the master clip is ~1 minute by hand).
    → `projects/cbum-last-show/grade/cbum-host-grade.cube`, `work/grade/host_grade.py`.
20. **THE LAST SHOW was rejected as "mid, a draft, not a documentary" (2026-10-21). The AW long-form rules, from his review**
    (`projects/cbum-last-show/review/critique-2026-10-21/CRITIQUE.md`):
    - **Bespoke visual per LINE.** A Higgsfield image, a screenshot (Instagram, results) or the named person. Never one archive
      clip stretched across several lines; every line naming a person shows that person; no unflattering shots.
    - **The FX catalog + motion graphics are the job.** The Nick Walker video is the floor.
    - **Host face:** NEST consecutive face cuts, ONE subtle zoom-in, no per-clip repositioning ("camera goes up"), no cut zooms.
    - **No freeze frames under his VO.**
    - **Opacity fades into and out of graphics and footage** (no pops), flash transitions where the energy turns.
    - **Level-match every insert to the voice, with short audio fades at joins, before his first watch.**
    - **SFX match the action** (a highlighter wipe = a highlighter sound).
    - **Subtitles on EVERY third-party clip.**
    - **Research numbers (changes/10 s, colour jump) are guards, never the target, and never override his standing look.**

## 2026-10-21 · THE LAST SHOW redo, cold open v2 ("the whole intro looks so much better… it's insane")
21. **He took the redo's cold open: VO from the first breath after the archive, a bespoke visual per line, no freezes, level-matched
    inserts.** What he praised is the method in lesson 20 executed; keep it.
22. **A collage is not premium.** The 0:25 beat (Samson Dauda on his raw Olympia LED backdrop + a low-res Nick Walker torso
    cut-out + a giant steel OPEN word + two mono tags) was "hideous… not refined, expensive at all". → ONE subject, graded into
    the film's world (warm monochrome, crushed blacks, the backdrop and watermarks falling into black under a soft oval), the
    stage light coming up on him, one quiet line of type (mono gold label + Instrument Serif italic). When a source is busy,
    grade it into the palette instead of stacking more elements on it. → `work/redo/co/build_co.py` co-07 v2 (`co-07-c.mp4`).

## 2026-10-21 · THE LAST SHOW redo, his second review ("a lot better than our previous one, but there are a few mistakes")
Notes resolved in `projects/cbum-last-show/review/critique-2026-10-21-redo/NOTES.md`.
23. **After a recovery, the damaged copy must not be where he can open it.** He reviewed the DAMAGED sequence (its tab was still open),
    so half his notes (flashing frames, "no captions", vlog under the trailer audio, "stretching to 29 minutes") were the damage.
    → close a damaged sequence's tab the moment it is replaced; delete it only with his OK, after an FCP XML backup; the handoff names
    the sequence by name AND id.
24. **SFX variety is the quality bar ("2/10… that Vegas whoosh so many times").** 125 of 296 cues were two air samples (one whoosh 70×).
    → every class is a POOL of distinct Epidemic takes rotated with no back-to-back repeats; air sounds are thinned (a hit or stroke
    within 0.25 s carries the moment; ≥ 1.2 s between air cues); whooshes stay 10 dB under the hits. `work/redo/sfx/build_sfx.py`.
25. **Never a mock-up of a real person's account.** co-02/c3-post used an invented avatar and an invented caption ("you have to search
    Instagram… this is his profile picture"). → fetch the real thing: the profile header and grid (instagram.com/<user>), the post's
    image + exact caption + likes from its public embed (`/p/<code>/embed/captioned/`), news articles for the shortcode. Rebuild it
    faithfully; animate only what the line needs (the follower count, a highlighter).
26. **Pointers on people are TRACKED and rest on the body.** Static circles slid off the men as the handheld camera drifted ~250 px.
    → template-match each man through the shot (`work/redo/ch4/track_4a.py`), circle on the shoulder, line up to the name, the label
    moving with him. Identities by a primary source in the shot itself: a bib must be LEGIBLE in that shot (then matched to the
    official sheet); otherwise a reference photo of the candidate must match. A name inferred by elimination is not proof (lesson 31).
27. **An insert that ends mid-syllable needs a breath, not a butt join ("too abrupt, destroys the immersion").** 4e's picture cut kept
    90 ms of Chris's NEXT word, then the host. → find the true word end, fade there, open a ~0.4 s breath (`ripple_breath.py`), fill it
    with the speaker's own room tone at the measured level (`fix_4e_joint.py`), and hold the last picture frame through the breath into
    the next graphic.
28. **A cover never opens on black.** c4-martin-olympia faded up from an empty dark frame ("cheap"). → hold the previous shot's last
    frame and dissolve straight into the card.
29. **No sub-1 s covers.** A 0.37 s pre-roll of the next insert over his face read as a random flash. → a cover is a real shot (≥ 1 s)
    or nothing; the eye-line gate's ±0.25 s padding can flag a cut's last frames as "reading" — check those frames before covering.
30. **A push-in on a still portrait is "pretty silly".** → hold archive portraits plainly (c1-1c-push removed).
31. **Name only the men you can prove ("thats not shaun brh", same day).** The left man's bib was never legible; he was named Clarida by
    elimination, and Clarida turned out to be a bald Black athlete. → bib legible in the shot or a matching reference photo, else no
    tag; send him the evidence (bib crops + reference photo) with every identity fix (`work/redo/ch4/id-evidence.jpg`).
32. **Subscribe alerts, on his ask (THE LAST SHOW, 2026-10-21): "little… fit the aesthetic… not too often".** → about 3 in an
    11-minute film, 3 s each, lower-left in the film's own tag language, only on calm host-face windows with nothing else on screen,
    never in the cold open, the end screen, near a mid-roll or after a heavy moment; one soft refined sound each.
    `projects/cbum-last-show/work/redo/cta/build_cta.py`.

## 2026-10-26 · BOTH VERSIONS (paris-jackson-both-versions), the cold-open pacing + look review
33. **Intentional pauses are RARE and never on his face ("you went overboard… not with every damn cut").** I took "restore the pauses
    on the lines Part A marks slow" as a pause between every sentence of those blocks plus a 0.4 s breath at every host↔clip joint,
    stretched into his silent frames: in those frames he turns back to READ the script, so every pause showed him reading. → The face
    cam stays TIGHT, always. A deliberate pause only where it is felt to be necessary (a handful per film: the script's explicit
    holds), and it sits under an OVERLAY, never on his face. Joints get their short audio fades, not host-side breaths.
    `projects/paris-jackson-both-versions/work/pacing.py` (now: Part A's two explicit holds only).
34. **Every reading span is under an overlay, never his face in the centre (same review; the AffanWiz rule, memory
    feedback-cover-phone-reading, now explicitly for AW long-form).** → measure head pitch AND yaw on the final cut
    (`work/look_down.py`, `workflows/eye-line.py`) and lay a full-frame graphic over every reading run before he sees it; his face
    shows only where he looks into the lens.

## 2026-10-27 · BOTH VERSIONS review 1 (his notes + his own edits on the sequence)
35. **He cut every pause himself, including the script's designed holds.** Ten ripple cuts (15 s): three in the cold-open Alvarez clip,
    six short host gaps, and BOTH 1 s holds Part A asked for. → No designed silent holds in an AW film unless he asks; read his
    timeline edits (`work/review1/diff.py`: map the old timeline to the new by source time) before touching anything, and keep them.
36. **No silence over 2 s inside a third-party clip ("they cannot be more than two seconds, otherwise it just gets uncomfortable").** →
    measure every speech-free stretch from word timings, check it on the source level, and cut it to 1.2-2.0 s with a sync-safe ripple
    across all tracks (QE extract on a proven clone first), plus a 2-frame crossfade on the new joint; crying counts as content
    but is still capped at 2 s. `projects/paris-jackson-both-versions/work/review1/extract_gaps.py`.
37. **Censor every word about drugs, self-harm, suicide, in the audio AND the captions (and redact it in designed type).** → the
    film's bleep (mute + soft tone), caption "[bleep]", list reported so he can restore one; host lines included.
    `work/review1/censor.py`.
38. **A score with an arc, never one flat bed: "mellow, emotional, sad at the beginning… a little intense where it builds… mellow again
    approaching the end".** → map the chapters' feeling, pick one measured track per section (intensity curve, percussion share,
    1-4 kHz energy, key), crossfade between sections, duck 6 dB under archive clips, pull fully out under the script's list.
    `work/review1/score.py` + `music_measure.py`.
39. **A reveal that lands ~1 s before a hard cut reads as "cut before it finishes".** The build agents met "settled ≥ 1 s before the cut"
    and it was not enough. → a graphic's last reveal settles ≥ 1.8 s before its cut; measure it on the render
    (`work/review1/mg_cutoffs.py`), and fix late comps with a time remap of their own timeline (`work/review1/remap_comps.py`).
40. **Cutaways from other moments of an interview under someone's words look out of sync ("janky… all over the place").** → when a span
    of picture can't be shown (undated photos), use the film's audio-only word card, never other talking footage.
41. **Check every clip edge frame by frame for promo / transition frames** (Jay Shetty's "WATCH NOW · Netflix · Spotify" end card,
    ET's white flash, a blur into a red-carpet photo). → trim, or hold the last clean frame when the word is still running.
42. **SFX were too loud after a phone-audibility lift.** → no phone lift on a long-form; cap each class against the voice (booms -12,
    thuds -13, hits -15, strokes/paper -19, swishes -21 dB).

## 2026-10-28 · BOTH VERSIONS review 2 ("very close to upload material")
43. **A word card whose exit starts before its last word is lit reads as "the animation doesn't finish… it transfers to my camera…
    it looks like I interrupted" (2f, Oprah).** The audio-only card builder faded every card at a fixed `dur − 0.7 s`, so on a 1.8 s
    card the last word lit inside the fade and the cut followed 0.13 s later; 1c and the review-1 Willow card had the same flaw. →
    the exit is keyed off the LAST REVEAL (fully lit, held, then out), never off the comp's end; a gate reads every placed comp's own
    timeline against its cut (`projects/paris-jackson-both-versions/work/review2/reveal_check.py`), because the motion check skipped the
    word cards. Into his face: hold, then dissolve (≥ 1.5 s of face left); if his face window is too short for that, her line hangs over
    his VO into the next scene (and anything that fades in after the card gets black under it, or his face flashes through the fade).
    He approved that handoff on 2f ("keep it: her line holds over my voice into Chapter 3").
44. **The paper / writing / scribble textures still read loud after review 1's caps ("tone it down three, four decibels").** → those
    classes sit 3.5 dB under review 1 (strokes / paper ≈ −22.5 dB vs the voice); applied RELATIVE to the live level, by name, so his
    hand-set levels stay (he had pulled one page-turn 15 dB himself). It also answers the phone-band question: quieter wins.
45. **The film ends on a fade to black, not a hard cut** (his ask; Part A had "HARD CUT on 'hi, daddy'"). → the last frame held under
    a slow push (the next words start 0.2 s later, so no more footage), a black solid eased 0 → 100 % over 1.6 s, then the end black.
46. **A viewer must know who is talking and who they mean: "I didn't know he was Ozzy Osbourne's son."** Jack was never named, and 5d
    ("when my dad passed") is HIM speaking, not Paris. → every third-party speaker gets a name at first sight; when a speaker refers to
    someone famous, a small callout stems from the speaker's head (measured off the ear, clear of his hands) to a REAL photo + name +
    relation + dates, in the lower-third type, with the lower-third whoosh.
47. **His own edits this round: the score runs under the cold open too** (he laid the score's opening under 0-30.8 s and started Ch1's
    section 2.6 s later), and the tabloid page-turn went −15 dB by hand. → AW long-forms: music from frame 0.
