# hpp-brad-pitt-f1: Onyx sample Short for High Performance (batch 8, RESTRUCTURE mode)

## ▶ STATUS: resume here
- 2026-11-09 21:35 (main) **SIGNED OFF, checked from the Exports copies** (`X:\Claude Projects\Exports\hpp-brad-pitt-f1.yt.final.mp4` / `.ig.final.mp4`, proof sheets beside them): 54.0 s, 1350 f, 25 fps, -12.1 LUFS / -2.2 dBTP, decode clean, identical to outputs/. Fix round 1 verified frame by frame: the LOG scene draws in by 45.52 (after the sign leaves at 45.28 there are ~6 frames of the sign scene's faint background, 1-2 near empty, before the line work: flagged); the last David face starts on "someone" at 50.16 and runs 3.84 s; the IG hook has no burn (card holds to ~2.64, then the photo). IG burns now at 28.0, 37.24, 39.68: the last two sit 2.4 s apart around the poster (taste, flagged to Affan). Labels: David once (DIRECTOR DAVID AYER), Brad by the hook card; Jake's three words ("High performance is", cyan) carry no label: flagged. Full 2 fps sheets of both looks and all proof sheets viewed. Nothing left to build.
- 2026-11-09 ~20:00 (Sonnet builder): BOTH LOOKS DONE. `outputs/hpp-brad-pitt-f1.sample-yt.final.mp4` (= v5) and `.sample-ig.final.mp4` (= r1), 54.0 s, 1080x1920, 25 fps native, 1350 f, -12.1 LUFS / -2.2 dBTP each,
  copies `X:\Claude Projects\Exports\hpp-brad-pitt-f1.yt.final.mp4` / `.ig.final.mp4`, proof sheets in outputs/. cue_check PASS both (every cue -19.2..-23 dB, none weak on a phone). One Sonnet reviewer: no blockers.
  Rebuild: `python yt/build_spec.py`, `yt_build.py <job> vN`, `python work/yt_finish.py vN+1` (grade + sharpen + restore_panels); IG `bash ig/run.sh build.py` then `bash ig/run.sh sound.py r1 --mux`. Machine memory is tight: retry a step that dies on "Unable to allocate".
- Flags so far (for Affan / main): (1) beat 3's opening "high performance is" is JAKE's voice (the host started the sentence, David finishes it with "hours of preparation"): captions cyan / yellow, TRACK covers
  it, David's label lands on his first face frame ("putting the time in"); (2) beat 2: the source is the show's split screen under "On the straights ... dinner later", so that line is a B (TRACK) not a face;
  Brad's own "and" glued to "breather" stays ("... breather and you think ...") because there is no gap to cut it at; (3) beat 6 opens on "What Brad did" (his "And" glued to "what" is cut at the continuous voicing:
  slice ASR reads "What Brad did"); (4) hook photo enters on "in the car" (not "How it demanded"): the hook face would otherwise be 5 s bare.

## The Short and the point
Their Short: "Brad Pitt explains the feeling of driving an F1 car" (QDlNQg0ScaI, 29.5K views, 35 s, 720x1280 25 fps, uploaded 2026-10-02).
It opens mid-sentence on "prep, prep, prep, prep" with no setup, runs Brad's answer as one block, two F1 photos in the first 7 s, and ends on
the film line.
Ours (title: **Brad Pitt Drove A Real F1 Car. This Is What It Taught Him**): opens on the claim (total presence in a real F1 car), the
straights and the corners, David Ayer's definition of high performance, Brad's "do your laps", the film line, and ends on a usable lesson:
David on why a crew works harder for a leader who stays with them.
**The viewer gets:** what high performance is (hours of prep until it's muscle memory, then total presence under pressure), and why a crew
works faster for a leader who stays with them.

## Beats (`../_onyx-batch8-2026-11/SEQUENCING.md`, order exact, words exact; episode seconds, file = episode)
1. HOOK, Brad (~810-821): "The most amazing thing to me, when I was able to be in the car, was just how present I was. How it demanded my absolute presence."
2. Brad (~823-835): "On the straights you can have a little breather, you think about what you're gonna have dinner later. But most of the time you're just prepping for the next turning point, and then how you get out of that turn."
3. DAVID AYER (~767-779): "High performance is hours of preparation, putting the time in so that when pressure hits, you know you have the skills and you're not sitting there thinking about it. Things become muscle memory."
4. Brad (~803-810): "Prep, prep, prep, prep. Do your laps, do your laps, do your laps."
5. Brad (~835-845): "It was such an incredible experience for me that I've never quite had anything like it, other than certain moments on film when you're attacking a scene in the same way."
6. BUTTON, David Ayer (~547-578): "What Brad did to win the crew was just being with the crew. Not leaving the set. Being cold, wet, tired. He doesn't go back to base camp. He's just sitting there on a log, listening to music, and just being incredibly patient. And when someone does that, you want to work faster. You want to deliver for them."
Left out: the XTB ad read (10:02-10:39), "I love this f***er" (12:01), the vulnerability block (10:40-11:16).

## Teardown: their Short → ours (Affan's talking points)
| Axis | Their Short (35 s) | Ours (54 s) |
|---|---|---|
| Hook, first 3 s | "prep, prep, prep, prep, do your laps" mid-sentence over Brad's face, no title; a stranger doesn't know what he's prepping for | Brad's face on frame 1 saying the most amazing thing was how present the car made him, under a claim card BRAD PITT DROVE A REAL F1 CAR: a promise the Short then pays |
| Who / what / why by 5 s | Brad is never named; the F1 car only appears as stock photos with no context | named by the card in the first second; the real McLaren MCL60 he drove at COTA on screen by ~5 s |
| Captions | one or two lowercase words at a time, mid-chest | the show's seam captions from frame 1, Brad and David in their own colours |
| Pacing | one 35 s block, his pauses kept | every pause closed; a new picture every 2-4 s |
| Visuals per beat | two paddock photos, then 25 s of the same face crop | the real MCL60, a drawn COTA track where the next corner lights up before he reaches it, a pressure gauge, a lap counter on "do your laps", the race photo dissolving into the film, the base camp he never went back to, the log he sat on |
| Ending | stops on the film line, no lesson | a lesson in his director's words: stay with your crew and they'll work faster for you |
| Sound | the show's mix | the show's voices, soft swishes on graphic entrances only, no bed (Affan picks the song) |

## Catalog pass (CLAUDE.md rule 5), main, 2026-11-09
Read all of `research/effects-catalog/CATALOG.md` and looked at all 79 reference stills (two contact sheets, no strips).
- Used here: FX-29 Float Frame (the MCL60 and film stills on charcoal, never full-bleed), FX-24 Red Dash Map + FX-21 line style (the COTA
  track, the corner lighting up), FX-71 Funnel Count (LAP 1/2/3), FX-42 Kin Tag (David's label, kept low), FX-37 Ghost Dissolve (race photo
  into film still on "on film"), FX-21 Red Silhouette Set (the log scene nobody filmed).
- New to Onyx samples: the drawn track scene, the ghost dissolve, the line-drawn reconstruction. The last sample of its kind leaned on
  photos + counters (John Legend's family tree, Melanin's escalators).
- Not used: maps of places, headlines, charts (no document or number in the story), FX-13 depth type (killed on seated close-ups).

## Better than the last one of its kind
Every graphic is drawn from his words (a corner lights up on "turning point", a lap lands on each "laps"), the hook is a verified claim
shown with the real car, and the ending turns a celebrity anecdote into a lesson a viewer can use.

## Downloads (logged before pulling)
| File | Source | Size | Use |
|---|---|---|---|
| source/hpp-ep-jdZPl95OWHI.mp4 | YouTube jdZPl95OWHI, format 137+140 (pulled 2026-11-08 by the mining session) | 110 MB, 1920x1080 25 fps, 876 s | the episode |
| reference/short-QDlNQg0ScaI.mp4 | YouTube QDlNQg0ScaI (their permitted Short) | 5.1 MB, 720x1280 25 fps, 35 s | teardown only |
| assets/img/cand/* (several files) | Bing image search via workflows/img-candidates.py (curl; origins in cand/sources.txt): Brad Pitt McLaren MCL60 COTA test; Sonny Hayes F1 The Movie still; Heart of the Beast set | each < 5 MB | photo candidates; the picks are re-logged below with origin + size (2026-11-09 builder) |
| assets/data/cota_osm.json (+ cota_chain.json derived) | OpenStreetMap Overpass (maps.mail.ru mirror), highway=raceway ways named Turn 1-20 near COTA, ODbL | 56 KB | the TRACK card: COTA's real centre line, 5494 m (the Short's TRACK / LAP COUNTER scenes) |
| assets/img/pick/hook_mcl60.jpg | f1i.com/wp-content/uploads/2025/06/GuTTvCNWkAQov1Q-1-scaled.jpeg (Brad in the McLaren MCL60 cockpit at COTA, June 2025) | 2560x1707 | HOOK photo (the papaya car + McLaren crew in frame) |
| assets/img/pick/mcl60_track.jpg | motorone.gr/wp-content/uploads/2026/03/Brad-Pitt-McLaren-MCL60-copy.jpg (Brad standing by the papaya McLaren MCL60 on the COTA pit straight, the same test) | 1920x1280 | PHOTO 2, beat 5 (ghost dissolve start). assets/img/pick/mcl60_helmet.jpg (f1i.com ... GuTYAqSXkAA1iod, 1000x1220, helmet close-up) was a candidate, not used |
| assets/img/pick/sonny_film.jpg | images.lifestyleasia.com/.../12132814/f1-movie-ending-1600x900.jpg (press still of Brad as Sonny Hayes, F1 The Movie 2025) | 1600x900 | the film still, beat 5 (ghost dissolve) |
| assets/img/pick/hotb_poster.jpg | static0.srcdn.com/.../heart-of-the-beast-poster.jpg (official Heart of the Beast poster art, Brad Pitt) | 960x1440 | beat 6 opening (fallback named in DIRECTION: no real set photo of Brad found HQ; hotb5 = an unverified candid, not used) |

- More flags: (5) beat 3 label held ~1.6 s (his face shot is 1.6 s) not 2.5 s; (6) s18 David's last face shot is 4.36 s bare (limit ~4); (7) s11 photo 2 + film still is a 7.4 s B; (8) hook photo helmet carries APXGP/Shark Ninja branding (his film helmet worn in the real MCL60); (9) IG hook title "A REAL F1 CAR" touches Brad's hair edge; (10) no real Heart of the Beast set photo found: official poster art used (candid set photo unverified, not used); (11) COTA track = OpenStreetMap centre line (ODbL), drawn rotated.
