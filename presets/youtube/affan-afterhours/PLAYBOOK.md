# affan-afterhours — PLAYBOOK (the repeatable procedure, every video)

The same phases, in order, for every Affan Afterhours video. The pipeline itself is the eight steps in `CLAUDE.md`;
this file is what sits around it for this channel. Job state lives in the job folder, never in chat:
`BRIEF.md` (pre-production) → `RUN.md` (from intake), each with a **"▶ STATUS: resume here"** block at the top.

**Starting any session on a job:** say "resume <job>". Claude reads the resume block and continues; nothing is re-derived.

## 0a. TWO FORMATS — pick in the BRIEF before anything else (2026-09-19)

The channel runs two formats and the **GTA 6 explainer is the default** (`README.md` § 1b): bright LED room,
animated hands, ≥ 17 visible changes/min, illustrated key-art **stills** (never videos), posters with one pink
keyword, game footage first and last, ≤ 30 credits. Its measured grammar and the motion-graphics modification live
in `projects/gta6-travis-scott-hired/STYLE.md`. The documentary format below (§ 0) is **paused** until a doc video
performs. Its palette and mannequin rule do not carry to an explainer — **but the overlay frame does**: stills at
85–90 and gameplay zoomed out over a dark grained colour matte (`README.md` § 1b). People in explainer graphics
are animated PNG cutouts of the real person; an explainer opens on the face.

## 0. What an episode of the DOCUMENTARY format is — measured on Hot Coffee (2026-09-18)

The creator's labelled hand-cut is the shot list. Export it as FCP XML, run
`python lanes/premiere/parse-fcpxml.py <timeline.xml> --json <out>`, and the colour blocks with their
word ranges are the plan (labels are XML-only; the effect stack is DOM-only — `lab-notes.md` 2026-09-18):

| label | means | share of runtime | median block | how the pipeline answers it |
|---|---|---|---|---|
| **Iris** | face on camera — never covered, never still | 38 % | 7 s | **the pipeline now applies this grammar** (`lanes/premiere/face-nests.py`, picks as data in `transcript/face-zooms.json`): the gradual zoom is a **RATE ≈ 1.6 %/s capped at 10 %** (a 1.4 s run gets ~4 %, not 10 % — they hand-fixed three short runs), plus a **tail push** (razor the last ~1 s, ramp to 118–126) on a landing clause. The creator's face grammar, in order: nest the jump-cuts → **cut zoom** (an instant +25 snap on the emphasis word inside the nest; +5/+10 in the doc format) → a **keyframed gradual zoom 100 → 110** on the nest itself. A replay that flattens the face destroys all three |
| **Violet** | reenactment wanted | 41 % | 9 s | **two Higgsfield angles** (three only over 12 s), placed at **96** on V3+ over a **V2 Color Matte + BCC Film Grain**, each with **Drop Shadow 80 % / 135° / 30 / 40** — the channel's overlay frame |
| **Mango** | motion graphic wanted | 16 % | 6.6 s | a house graphic at **100**; the creator carves Mango OUT of Violet wherever a line carries a name, date, title or number — plan those first |
| **Forest** | real gameplay | 5 % | 11 s | the creator's capture, radio off |
| **Lavender** | a real still the creator supplies | 3 % | 3–5 s | when the thing itself is the evidence, a screenshot beats a generation; they place and scale it |

Rhythm: **24 cuts/min, cold open 27/min, median clip 2.25 s** — dense edit points, calm picture (only
~11 perceptible scene changes/min; the rest are face jump cuts). Mean luma **0.22**, blacks at 21/255.
Music: the creator's own Epidemic bed on **A2**, 100 % coverage, −24 dB under the cold open, −3…−7 dB
in the body, cue points on the section turns. They also lay their own diegetic SFX (stamps, phone, beeps,
room tone): **read A2–A5 before planning any sound.** The full anatomy: `projects/gta-san-andreas-hot-coffee/POSTMORTEM.md`.

**Track layout the creator settled on:** V1 face nests + gameplay · **V2 Color Mattes only** · V3 graphics,
reenactments, stills · V4/V5 reenactment runs · V6/V7 alpha overlays · A1 voice · A2 their music ·
A3/A4/A5 SFX (A4/A5 carry their hand-placed diegetic sound) · A6 room-tone beds · A7 machine-hum layer.

## A. Pre-production (before any footage exists)

| # | Step | Output | Done when |
|---|---|---|---|
| A1 | Brief | `projects/<job>/BRIEF.md` from the template below | creative direction + checklist written, drop folders made (`raw/ broll/gameplay/ audio/music/ assets/`) |
| A2 | Script | `script.md`, verbatim as the creator wrote it | saved; `[ON SCREEN]` / `[LOOP]` tags kept |
| A3 | Fact-check | `FACTS.md`: one row per checkable claim → status (VERIFIED / PARTLY / WRONG / UNSOURCED) · what the sources say · source · suggested wording. **Method (learned on Hot Coffee, 2026-09-16):** first find the two or three load-bearing PRIMARY sources (a regulator's complaint or order, the official statements, a court opinion, a roll call, SEC filings, one deeply reported long-read), then check every claim against them; Wikipedia is a pointer, never the source. **Every exact date is checked against a primary record** (scripts inherit the news write-up's date, 1–3 days late). Spans ("within six weeks") are arithmetic, check them. Parallelise: split the claims into 2–3 research passes by phase of the story. | every flagged line has a source or a rewording; **nothing unsourced gets reenacted** |
| A4 | Shot list | `SHOTS.md`: beat → layer (face / reenactment / motion graphic / gameplay) → for reenactments the prompt + credit cost, **and a FACTS gate column per reenactment row** so an unsourced claim cannot be generated by accident; two tiers (must / nice) with a retake reserve so the creator decides on a number | the creator approves the list and the total credits |
| A5 | Style test | first video, or whenever the look changes: ~60 s cut with one of each scene type | the creator signs off the character design, fonts, palette |

## B. Shoot (the creator)

- **Background:** dark, 2–3 m behind you so it falls off; one small warm practical (lamp, monitor glow) for depth. No bright walls, no pink/neon washes.
- **Light:** ONE soft key 45° to the side, slightly above eye line; let the far side of the face fall into shadow; optional faint rim light.
- **Framing:** medium close-up to close-up, off-centre with the space on the side you look toward, eyes on the upper third, camera at eye level. A second tighter angle is a bonus.
- **Camera:** 50–85 mm, f/1.8–2.8, 1080p or 4K, **23.976 fps at 1/50 shutter**, fixed focus / exposure / white balance.
- **Audio — DUAL SYSTEM, and the camera's own mic stays ON.** The voice is the HyperX mic, recorded through OBS (so it arrives as a screen-recording video, not a wav); the camera's internal audio is the **scratch track**, never used in the cut but never disabled either, because it is the sync reference. Hand over BOTH files. Intake extracts the mic track, cross-correlates it against the camera scratch to find the offset, checks the offset again at the end of the take for clock drift (two devices, two clocks), and muxes the mic onto the camera picture without re-encoding it. That synced file is the raw the pipeline reads; both originals stay untouched in `raw/`. **Record the OBS side as ONE continuous take** even if the camera stops and restarts, so every camera file syncs against one master. In OBS, keep the mic on its own track (Settings → Output → Recording, separate audio tracks) — a mic already mixed with desktop audio cannot be unmixed.
- **Performance:** read in short sections; a fluffed line is simply repeated (the edit keeps the last take).
- **🔒 THE EYE-LINE MARKER (the creator's own convention, 2026-09-16).** The script is on a monitor **to the creator's left**: they deliver to the lens and **turn their head left to read**. That turn is a deliberate marker for the edit — **eye contact means no overlay**, a head turn means the frame is free for graphics and cutaways. `uv run workflows/eye-line.py <base-cut> --out projects/<job>/transcript/eye-line.json` measures it and the graphics plan treats the camera segments as no-go. Shoot it consistently: turn the HEAD, not just the eyes (the measurement reads head yaw from face landmarks; a pure eye flick is not visible to it), and **open every take with a 3 s look at the lens then 3 s reading the monitor** — that labelled pair calibrates the split exactly (`--calib-camera 0:00-0:03 --calib-read 0:04-0:07`) instead of it being inferred.
- **Gameplay:** record with radio and in-game music OFF (Content ID). Never show explicit content. The game is only used where it is the evidence.

## C. Post (the pipeline, with this channel's deviations)

| Step | As `CLAUDE.md`, plus |
|---|---|
| 1 Intake | BRIEF's resume block becomes RUN.md's; RUN.md names `presets/youtube/affan-afterhours/` as the preset |
| 2 Rough cut | **The creator's pacing (measured on their hand pass, 2026-09-19, LESSONS.md):** keep a pause up to **0.9 s** between a setup and its punch (the ≥ 0.65 s dead-air split is for hesitation only); **tighten lists** (parallel items, yes/yes/yes runs) to the joint minimum; graft only a real false start, never a self-correction that carries rhythm; between a clean earlier delivery and a hitched later one keep the clean one; cut restated numbers, cold-opening connectives and a second quote stacked on a first; KEEP an aside that tells the viewer something new about the subject. Joint air (~150 ms) is right as the polish sets it. The creator re-cuts and colour-labels the timeline after the rough cut: **Iris face · Mango motion graphic · Brown real footage/real images (Google/Instagram, enhanced in Higgsfield) · Violet Higgsfield still**; their labels are the graphics plan |
| 3 Audio | **the EXPLAINER finishes its voice OUTSIDE Premiere** (measured on the shipped Travis cut, LESSONS 2026-09-20): the creator bounces the edited voice and runs it through **Adobe Enhance Speech v2** (0 % background / 17 % music), then drops ONE file back on A1 — every per-clip Amplify/limiter is discarded with the old clips. So: apply the measured gain chain for monitoring, **bake any mute (a bleep) BEFORE the bounce**, hand them the bounce, and ask for WAV or ≥ 256 kbps back (they shipped a 128 kbps MP3 as the master voice). Doc format: unchanged |
| 4 Grade | Premiere 25.0 cannot run the scripted grade (v45 templates): manual recipe in the Premiere lane notes, or update to Premiere 26 |
| 5 Graphics | three layers. Reenactments are planned as full-screen cells in `graphics-plan.json` and generated per `workflows/higgsfield-reenactment.md` (approved SHOTS.md only); house graphics recoloured to the dark palette; **no captions, no text animations** (README § 3) |
| 5b Receipts | **a cited source that exists on video is PLAYED, not drawn** (`clip-insert` cell): razor the face nest, Color Matte on V1, the clip on V2 scaled with a Drop Shadow, a text credit on V3 across its span, the voice out on A1 and the clip's own audio in, the music bed silent for the whole insert, everything after it rippled. The insert point comes from a WORD BOUNDARY in the canonical transcript. A slot whose artifact cannot be sourced is never handed back empty: offer the nearest equivalent artifact in the same beat |
| 6 SFX | unchanged; reenactment entrances are events. **The first sound of the video starts at 0.000**, not at the first graphic's in |
| Music | **ON** (README § 5). Explainer, as shipped: **one Epidemic track per SECTION** (4 across 7:39), 0 dB clip gain, ~91 % coverage, and **a 1.5–5 s silence just BEFORE each section turn or big graphic** (and under any clip insert) — a bed that breathes, not one flat bed. It rides the first free track ABOVE the SFX (A7 on the Travis cut); **A2 is not reserved — read every audio track before planning sound** |
| 7 Review | the creator watches and calls taste. **Then phase D, always** |
| 8 Export | on the creator's go; `finalize.sh` |

## D. Learn (after every review, unasked)

1. Read what the creator changed on the timeline: `place-graphics.py --diff`, `place-sfx.py --diff`, the V1 cut diff, and what they said in chat.
2. Append each finding to `LESSONS.md` as **lesson → change made → file**. A lesson that repeats across jobs becomes a number in `README.md` or a rule in this playbook; a one-off stays a lesson.
3. Update the resume block, the memory index, and (for tool bugs) the lane's `lab-notes.md`.

## E. BRIEF.md template

```
# BRIEF — <job> (pre-production, <date>)
One line: what the video is and which channel.

## ▶ STATUS: resume here (updated <date>)
**Done** · **Waiting on the creator** · **Next for Claude, in order**

## 1. Creative direction   (anything that differs from presets/youtube/affan-afterhours/README.md)
## 2. The story            (the claims to verify → FACTS.md)
## 3. What the creator supplies, and where it goes   (footage raw/, gameplay broll/gameplay/, music audio/music/, logo assets/, credit budget)
## 4. What Claude does, in order
## 5. Risks               (monetization, copyright, AI disclosure, tool gaps on this machine)
```
