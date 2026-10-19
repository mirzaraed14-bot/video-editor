# BRIEF — cbum-last-show ("THE LAST SHOW")

## ▶ STATUS: resume here
Research DONE (Decisions 1-22, forks F1-F6). Paused on the creator: the right host recording (C1361 is a MrBeast talk) and the
sources (queued in the Onyx session's YouTube queue; download log in RUN.md). Rows below marked (open) were settled by [HOST] → see 18-22 and the forks.

## The creator's ask (2026-10-14, verbatim points)
1. "In some places I am directly looking at the monitor to read the script, so make sure that is masked with some sort of
   overlay." The host is only ever on screen while looking at the CAMERA; every reading span is cut or covered.
2. Friends on the last video (SAME NIGHT): after the first title it was good, "the intro part, the editing felt very
   immature and very amateurish". This one must have "that expensive, premium, polished look… like it's been made by 20
   people, like it was a whole damn project".
3. "Do thorough and heavy research before getting into the actual edit, so that you go into the edit with understanding
   and knowledge that you didn't have before."
4. Use the overlay storyboard and the effects catalog (FX codes) and the styles in it.
5. "Make this in Premiere, not in yourself": the whole edit lives on a Premiere timeline he can open and change.

## Request coverage (each row → its owner → its evidence at handoff)
| Requirement | Owner | Evidence |
|---|---|---|
| Reading spans never host-visible | eye-line pass → storyboard (mandatory overlay slots) or cut | a gate: no reading frame host-visible on the saved timeline |
| Premium intro, measurable | research → § Decisions → cold open built first | checkpoint preview + the decisions checklist ticked |
| Research before editing | 3 research agents + intro diagnosis | `research/*/FINDINGS.md` |
| FX catalog + storyboard | `brief/storyboard.json` + page | every beat carries an FX code |
| Built in Premiere | Premiere lane | the saved sequence |
| Script lock conditions 1-7 (with fallbacks) | rough cut / inserts | RUN.md: each condition's verdict by ear/eye |
| NEVER list: no daughters' frames · never caption Greg as "should have won" · Martin not a villain · no premiere date · the 28 Oct Instagram post as a TEXT CARD only (never voiced) · no PED/health speculation · not "only two men ever beat him" · not "robbed" | every step | daughters frame check on every used clip; caption audit |
| Bleep 3a + any other f-word | inserts + audio | bleep keys + tone, read back |
| Arena/broadcast music under 4a, 2b-2d, the Prague posing: ducked to -30 dB or replaced; hunt clean sources first | audio | levels read back |
| Every clip carries its date card; quotes subtitled from WhisperX, corrected by ear (IgA, names) | graphics | caption audit |
| Mid-roll markers ~6:40 and ~9:20 (after the cliffhangers) | timeline markers | markers read back |
| Ending: black → "Maybe. Maybe not." card → a 15-20 s end-screen tail | graphics | timeline |
| Music: he lays his own (ask once at the checkpoint) | — | — |

## What this video does better than the last one (CLAUDE.md learning loop #5)
SAME NIGHT's cold open measured: 65 % synthetic pictures, 3.4 picture changes and 5.3 SFX per 10 s, colour jump 13.7, four
one-off type treatments, an FX-12 space title. THE LAST SHOW's open targets: 0 % synthetic (all real footage, Chris's own
cinematography), ≤ 2.5 changes and ≤ 2.5 SFX per 10 s, colour jump ≤ 7 under ONE grade shared with the host, one type system
matched to his own trailer, a title in the film's palette, and a measured pass/fail against those numbers before it is shown.
Plus: the host is graded for the first time (the wall and neon no longer out-shine the face), and every reading span is hidden.

## Decisions (from research, each with its FX code or a new code)
Sources: `research/intro-diagnosis/FINDINGS.md` [DX], `research/opens-cinematic/FINDINGS.md` [STD = Chris's own trailer,
GN = the competitor CBUM: The Movie, CZ = Coffeezilla]. The face-led study [HOST] is still running: rows marked (open) wait for it.

**What made the last intro cheap, and the counter-rule (measured on SAME NIGHT) [DX]**
1. Real footage from frame 0; synthetic pictures (AI images, cut-out composites) ≤ 15 % of the cold open (was 65 %), never two
   in a row, never near a credibility line. No mirroring, no scenes that never happened, dates match their line.
2. Cut-outs only as editorial portraits: one identical B&W treatment for everyone on a plain field.
3. Cadence: median shot ≥ 4 s for graphics (montage beats excepted, see 10), ≤ 2.5 picture changes and ≤ 2.5 SFX per 10 s.
4. One grade, ≤ 2 colour worlds, colour jump between neighbouring pictures ≤ 7, one grain over every source.
5. One type system (the chapter kit), no glows, gradient fills or RGB splits on type.
6. No interpolated slow-mo on moving bodies: real speed + a freeze, or the broadcast's own replay.
7. Build the cold open from the chapters' kit; measure it (`research/intro-diagnosis/measure.py`, `density.py`) against the
   chapters before it is shown.

**The look, matched to Chris's own film [STD]**
8. (open) 2.39:1 band (1920×804 picture, 138 px bars) across the archive; archive at its own shape inside the band, black at
   the sides, no borders/templates. Host shots: decide with [HOST].
9. Event footage (Olympia, Prague) regraded to one low-key look (median luma ~32/255, teal shadows, amber skin, whites ≤ 240);
   his own vlog/home footage left as it is.
10. Section changes cut to BLACK, never a dissolve. Montage beats median 1.3-1.6 s; host sections ≥ 2.5 s.
11. Type: two typefaces (+ the subtitle font). Date/place cards = his trailer's tagline spec: bold caps, white on black,
    ~3.3-4 % of frame height, wide tracking, fade in, hold 1.2-2 s, fade out over 6-8 frames, starting on a line boundary.
12. Title "THE LAST SHOW": heavy condensed, light grey, ~21 % of frame height, held ≥ 3.5 s (the script said 2 s), in the
    video's own palette; no gold glow, no debris space (lesson 6's FX-12 noted: the creator picked it, the data says it read
    cheap; to discuss at the checkpoint).
13. Sound: ≤ 1 impact per 10 s, impacts on the end of a black gap, a rising build into the title ~3 LU over the body,
    true peak ≤ -1 dBTP.
14. "Six in a row": a 6-win flash, 4 frames per win [STD].
15. Screenshots / headlines: a push-in, then a #E2B209 highlighter wipe [STD].
16. Subtitles only on third-party or rough audio [CZ] (lesson 13 already).
17. No watermarks, stock globes or soft stills [GN].

**The face-led openings [HOST] (`research/opens-host/FINDINGS.md`; Patrick's newest unmeasured, bot check)**
18. VO by 0.25 s; open 60-85 s to the end of the title; archive ≥ 70 % of the open; ≤ 3 designed text events in the open.
19. Median shot 2.5-3.5 s in the open; stills joined by 1-1.5 s dissolves, footage by hard cuts.
20. One graded look over archive AND host; host raw measures saturation 0.60 / corners 1.24 of centre (the green wall and neon
    out-shine the face) → grade the host: wall and neon down, a vignette, saturation ≤ 0.46, whites ≤ 0.80.
21. One 0.3-1.0 s silence with the bed out right before the pivot line; impacts only on structural moments (pivot, title).
22. Mix -14 to -16 LUFS integrated, LRA ≤ 5 LU, bed 12-14 LU under the voice (lesson 1).

**Forks, with my default (the creator can overrule any of them at the checkpoint)**
- F1 framing: archive in the 2.39 band (Chris's own film), the host full-frame 16:9, so "then" and "now" read apart by shape.
  The cold open (0a → 0b → 0c, all archive) is one framing throughout.
- F2 title: keep "THE LAST SHOW", restyled to his trailer's title (heavy condensed light grey on black, 5-6 s incl. build,
  then ≥ 1.5 s to black), NOT the FX-12 debris space (that look sat in the intro viewers called amateur).
- F3 host before the title: the script's 8-line host paragraph plays as VO over archive, with the face on screen only for
  the pivot ("Most of them have the order wrong… It was stopping.") and only on camera-looking takes.
- F4 cards: near-black cards with dust and a #E2B209 highlighter, not the 90 % gold matte.
- F5 SFX: quiet but present cues on graphics, ≤ 2 low impacts in the open (pivot, title).
- F6 music: he lays his own (asked once at the checkpoint).

**Edit points the research corrected**
- 0c: the trailer's own "PERFECTION" card shows on "die": end the trailer picture at 61.94 s and finish "die" over our black;
  start at ≥ 50.13 s.
- 5c: start at the trailer's own cut, 31.99 s (0:31 is mid-sentence).
