# tfts-we-need-to-talk: Onyx sample Short for Think Fast Talk Smart (Matt Abrahams) (batch 6)

## ▶ STATUS: resume here
- **2026-10-31 18:30: DELIVERED, both looks, 29.97 fps, awaiting Affan's review.** Affan 18:30 (via the main session): no 60 fps and no
  Topaz for these samples ("30 fps is good enough for prospecting"), so the QA'd checks ARE the finals; the queued Topaz/Chronos jobs
  were cancelled (`work/finals.sh` kept, unused).
  - YT: `outputs/tfts-we-need-to-talk.sample-yt.final.mp4` (= `…sample-yt.v10.mp4`) = `X:\Claude Projects\Exports\tfts-we-need-to-talk.yt.final.mp4`
    (md5 93483ea6…), proof `outputs/…sample-yt.proof-sheet.jpg`.
  - IG: `outputs/tfts-we-need-to-talk.sample-ig.final.mp4` (= `…sample-ig.check30.mp4`) = `X:\Claude Projects\Exports\tfts-we-need-to-talk.ig.final.mp4`
    (md5 a93b1385…, re-delivered ~19:10), proof `outputs/…sample-ig.proof-sheet.jpg`. **IG fix (coordinator, CLAUDE.md Rules:
    "Captions run the whole short-form video ... never suppress them under a hook"):** captions now run from frame 0 (one ~4-word
    line, whole, subtle rise, on the same constant line); the hook's camera card moved down under the caption line (title 70-330,
    captions on 522, card 590-1010) and the hook now CUTS to the full-window cam at 3.20 s (a growing card carried his face up
    through the caption line), so its growth swish is gone (11 cues). The previous IG = `outputs/…sample-ig.v-uncaptioned-open.mp4`
    (md5 d8609a7c…). The YT final is unchanged.
  - Both: 1080x1920 H.264 29.97 fps, 947 frames, 31.60 s, AAC 48 k, -12.1 LUFS, peak -2.2 dBFS, decode clean; 12 soft swishes each
    18-22 dB under the voice; no music bed.
  - Final gate (after the 18:30 delivery, re-delivered 18:55): eye steps across every in-shot joint on the delivered frames
    (`work/eye_gate.py`). Fixed: the 0.10 s pause cut at 7.47 dropped (a 37 px snap; the cut is now 947 f); YT s05 top untracked
    (the tracker put a 48 px snap where the source moves ~10 px); IG camera pinned PER TAKE at both edges (one anchor per shot left
    31-50 px). Left, judged by guide-line pairs (`work/look/gate_pairs.jpg`): YT 506/588 and IG 378/588 read 43-58 px on the EYE
    midpoint, but they are head TURNS between takes; the head's height, size and outline hold (Patron LESSONS: judge on the head, not
    the eyes, when the head turns).
- Flags for Affan: (1) [RESOLVED ~19:10: the IG opening line is now captioned from frame 0]; (2) lip sync
  measured ambiguous (my correlation -3/-4 frames incl. the natural lead, the reviewer's 0 to +2): not shifted; (3) Stan's tag says
  STANFORD NEGOTIATION LECTURER (Stanford lists him as a Lecturer; the episode: "teaches a very popular Stanford negotiation course"),
  never "professor"; (4) "kind of" kept and Matt's "Well," kept (trims either jumped Stan's head or made "one" read "when");
  (5) the OPENER 2 move labels (ADMIT IT'S HARD … LET HIM PICK WHEN) are our labels of his five moves, not his words.
- **Incident (for the report):** at ≈17:15 `yt_build.py v1` (fps_out 30 on a 29.97 base) started a Topaz Chronos pass on its own,
  outside `lock.sh` and inside the GPU-off window; killed within ~1 min (pids 64700/2564). Fixed at the source: the check spec now
  sets `fps_out` = the base rate (`--30`), so no Topaz runs for a check.
- Levels: 12 soft swishes per look (the DEFENSIVE stamp is silent: SUPERHERO rule), `under` set per slice so each sits 18-22 dB
  under the voice beside it (`yt/cue_check.py`, subtle bands LOUD > -18 / LOST < -25; most read "weak on a phone" < -20 in
  300 Hz-6 kHz, the subtle mode's known trade-off). Mix -12 LUFS, TP <= -2.
- **Lip sync (measured, not shifted):** mouth-motion vs voice-envelope cross-correlation on the raw section (`work/cut/sync_check.py`)
  peaks at -3 / -4 frames (Matt r 0.39, Stan r 0.24; the reframe span is flat), i.e. the mouth moves ~100 ms before the sound
  changes; part of that is the natural visual lead of speech (~1-2 frames). The show's own camera cuts also sit ~75-95 ms before its
  audio dropouts (10.675/10.75, 13.645/13.73, 39.175/39.27). Left at 0: the evidence is ambiguous and a wrong shift is worse. FLAG
  for the reviewer and Affan: if the voice reads late, it is a 2-3 frame audio advance on `raw/` (re-splice, everything re-times).
- `workflows/graphics-qa.py` does NOT apply (long-form 16:9 only, refuses other frame sizes): skipped on record; the kit's own
  checks (payoff report, cue_check, caption word-count asserts) + the reviewer replace it.
- IG: no captions while the hook title is up (0-3.25 s, neon-window LESSONS 2026-10-23), so the role-play's first line ("Let's say
  that I come to you, Matt, and we've had some tension in our relationship") plays uncaptioned under the title. FLAG for Affan.
- "99%" re-timed in words.json: WhisperX 15.745 -> 15.55 (5 ms envelope dip at 15.52-15.54, faster-whisper 15.48).

## QA round 1 (one sonnet fresh-eyes reviewer, defects only, on YT v6 + IG check30; scratch `work/qa-r1/`) -> fixed in YT v7 / IG check30 r2
1. HIGH: the end kept "S-o" of the next sentence (its /s/ at 44.665, centroid 5-6 kHz; WhisperX stamped "it." to 44.92 over it) ->
   the button now ends at 44.655 in the -45 dB dip after "it" (words.json "it." end 44.63). The prompted faster-whisper pass HAD
   heard "so": a prompted "so" at an edge is not always a hallucination.
2. MED: Stan's head dropped 50-60 px at the in-two-up joint 643 (the "kind of" trim) -> "kind of" kept (one fewer joint; captions
   "TO KIND OF"); the cut stays 31.498 s / 944 f (+0.275 s here, -0.297 s at the end).
3. MED: his studio mic (x >= 1290 in his single cam) half in the s03 top, and the two-up's mic stand (x 905-960) as an edge sliver
   -> s03 top z0 1.90, s04/s05 top z0 2.05 (fy_out 0.33): both out of frame.
4. LOW-MED: OPENER 2 read as an empty box for ~3 s before its first row -> the header strip carries "THE SAME TALK, REFRAMED" until
   row 1 lands.
5. LOW-MED: a mic-stand edge at the OPENER 1 card's left -> Matt's crop starts at x 600 (was 560).
6. LOW: the watermark over Matt's hair in the face split + the enlarged OPENER 1 card touching it at the end -> the face split's
   Matt panel z0 1.70 / fy_out 0.42 (head top under the watermark), the cards push 0.8 %/s (OPENER 1) and 0.6 %/s (the reprise).
7. LOW (IG): the show bug on Stan's hair in the face split -> that top panel frames him 20 px lower.
8. LOW (YT): the tag's text reached x 965 and the stamp x 1011 -> tag x 190 / dx 40, stamp 28 px left.
9. LOW (YT): six captions show 4.6-6.3 frames early after a pause: the kit's never-blank chain (a chunk holds until the next): kept.
10. LOW (IG): a line was only ~15 % up at its word (block start = word - 0.03 + a 0.12 s fade) -> block start = word - 0.10,
   clamped to any picture cut in between.
11. LOW (IG): the opening line uncaptioned under the hook title: a flagged decision (STATUS), kept.
- Reviewer's lip-sync read: in sync, 0 to +2 frames (no shift), against my -3/-4 correlation; both low confidence; no shift made.

## The cut (measured; `work/cut/make_edl.py`, re-ASR `work/cut/fw_slices.py` WITH and WITHOUT the filler prompt)
- Dropped: Matt's "I- I'm, uh," before "concerned" (reads "Concerned. I'm taken aback." both ways); Stan's "Right." before
  "You're defensive" (14.035 reads clean both ways); Stan's "um" after "Matt," (19.60-20.05); the approved trim "but we're both
  teachers of communication. And so I'd like to try to do that," (joint "doing it, | but I want you", both cuts in troughs);
  "kind of" (reads "but I want you to work with me on it" both ways). There is no "Yeah." before "How do you feel now?" (room tone).
- KEPT: Matt's "Well," before "one": every trim tried (39.50 / 39.53 / 39.56) makes "one" read as "when". Captions: "WELL ONE".
- Pauses: decay-to-onset at 6 places cut to ~0.10 s (breaths inside them too); "curious, | and two" (0.12 s) and "willing to |
  roll" (no quiet frame) left as spoken. End on "on it." at 44.952 (the "So" that follows starts 44.98; the prompted pass hears
  "so" from the release, the plain pass does not; energy dips to -36 dB before the cut).

## The job
- Show: **Think Fast Talk Smart** (Matt Abrahams, Stanford GSB), 200K. Tone (handoff 2026-10-31): polished, professional (Stanford).
  Their Short named in the permission email: "Why Most People Are Not Good Communicators".
- Approved pick: `projects/_onyx-batch6-2026-10/SEQUENCING.md` § "Think Fast Talk Smart v3", the **Alternate**: Stan Christensen's
  role-play on Matt (ep 294 "Ask & You Shall Receive: Questions For Better Negotiations"). Affan approved the swap from the Voss pick
  ("I want the video, none of that audio with png BS": Voss's ep 228 upload is static art, no faces).
- Source: YouTube 63Sv85jlYWg (1080p 29.97, H.264), window 0:08:00-0:16:00 = `source/63Sv85jlYWg_0.08.00-0.16.00.mp4` (main session's
  pull). The role-play sits at source 249.4-292.8 s (= YouTube 0:12:09-0:12:53; RSS cues 0:10:52-0:11:32, so YouTube runs ≈ +77 s).
  Section cut: `raw/tfts294_roleplay.mkv` = source frames 7448-8825 (t 248.515-294.494, 1378 f @ 30000/1001, x264 CRF 12 + PCM 48 k).
  Duplicate-frame check (YDIF on a face crop): 2.5 % near-zero steps, a true 30p camera (no 25-in-30 repeats).
- Both looks from ONE cut: YouTube (Sean Ryan look, `presets/youtube-shorts/onyx-samples-youtube/`) + Instagram (neon window,
  `presets/instagram/neon-window/`, newest kit = the Pincus `ig/`).
- Deliver: `outputs/tfts-we-need-to-talk.sample-yt.final.mp4` / `.sample-ig.final.mp4`, copies
  `X:\Claude Projects\Exports\tfts-we-need-to-talk.yt.final.mp4` / `.ig.final.mp4`, a proof sheet each.

## Who is who (verified, never by caption)
- **Stan Christensen = the man in the DENIM shirt with BLUE rectangular glasses** (guest). Lip check: his mouth moves through his
  role-play lines (source 253-255 s, `work/scout/lips_denim.jpg`).
- **Matt Abrahams = the WHITE-HAIRED man in the light-blue shirt, rimless glasses** (host). Lip check: his mouth opens on "Concerned"
  at 259.4 and his hands rise on "taken aback" (`work/scout/lips_grey.jpg`).
- The program feed follows the voice: Stan single 249.18-259.19, Matt single 259.19-262.16, Stan single 262.16-278.18, **native
  TWO-UP (Stan left, Matt right) 278.18-287.69**, Matt single 287.69+ (scdet, source seconds).

## The beats (followed exactly; found by their WORDS; nothing added, nothing re-ordered)
1. HOOK (Stan): "Let's say that I come to you, Matt, and we've had some tension in our relationship, and I say, Matt, I'd like to
   bring up something very difficult with you today. How does that make you feel?"
2. (Matt): "Concerned. I'm taken aback." (WhisperX hears "I'm concerned": to settle by ear-proxy; captions follow what is SPOKEN)
3. (Stan): "You're defensive. Exactly. And that's 99% of people. Now let's just change the frame a little bit."
4. (Stan, the reframed opener): "Matt, look, there's something I've been meaning to bring up with you. I've had a hard time bringing it
   up. I've sought counsel from some of my friends on how to do it, and I'm feeling ambivalent about doing it, [TRIM: but we're both
   teachers of communication and so I'd like to try to do that,] but I want you to work with me on it."
5. (Stan): "Would now be a good time to do that, or should we just set up a formal meeting? How do you feel now?"
6. BUTTON (Matt): "One, I'm curious and two, much more willing to roll up my sleeves and work with you on it."
- Spoken extras that are NOT in the approved text, trimmed if separable: "Right." before "You're defensive", "kind of" in "kind of
  work with me", "Yeah." before "How do you feel now?", "Well," before "one". Attributed by voice before any decision.

## GATE 5 (facts on screen)
- **Stan's title:** the episode says "a professional negotiator who has both practiced and taught negotiation for his entire career,
  and he teaches a very popular Stanford negotiation course" (tfts-294.txt 0:00:21-0:00:29). Stanford's own course listing
  (explorecourses.stanford.edu/instructor/stanc) lists him as a **Lecturer** (CEE 151 / 251 Negotiation, School of Engineering).
  → **Never "PROFESSOR".** Tag = **"TEACHES NEGOTIATION AT STANFORD / STAN CHRISTENSEN"** (the episode's own words).
- **Matt's title:** "I teach Strategic Communication at Stanford Graduate School of Business" (tfts-294.txt 0:00:11) → tag
  "HOST / MATT ABRAHAMS" (or "STANFORD GSB LECTURER"; the handoff confirms GSB lecturer).
- **"99% of people" is Stan's claim**: on screen only as his quoted words (a quote card with quote marks), never as a stat, chart or
  dot grid.
- The hook card names the premise in plain words and claims nothing Stan doesn't: "HOW TO OPEN / A HARD CONVERSATION".

## Decisions (with reasons)
- **The spine = the two-face exchange.** Every turn cuts between the two men on the turn (the exchange is the visual; onyx-samples
  LESSONS "an exchange beats a monologue"). The native two-up (Stan's ask + Matt listening, 278.18-287.69) becomes a stacked FACE
  SPLIT (Stan top, Matt below, white line, captions on the seam): both faces live while "Would now be a good time…" lands.
- **The visual idea = BEFORE / AFTER of the same face** (the hero move, FX-11 Rival Colour Split re-used as a time split): on the
  button, Matt's live "I'm curious" sits under a replay of his own "taken aback" face from beat 2 (muted, labelled OPENER 1 / OPENER 2).
  Two real faces of one man, honestly labelled as a replay; no borrowed listener plate pretending to be simultaneous.
- **The usable move is SHOWN**: the reframe's five moves build as a list beside Stan while he speaks them (FX-09 Demand Tree rows):
  ADMIT IT'S HARD / SAY YOU ASKED FOR ADVICE / SAY HOW YOU FEEL / ASK FOR HIS HELP / LET HIM PICK WHEN. Labels, not his sentences
  (no card restating the captions).
- **No music bed; SFX = soft Patrón-style swishes only**, one per graphic entrance, sized to the move, cuts back to a face silent
  (memory feedback-premium-sfx SUPERHERO + UNDER HIS MUSIC; batch-6 sibling Still Here made the same call). A bed is a mix-only rebuild.
- **No stock actor stands in for Stan or Matt** (README § 10). The only stock: hands rolling up sleeves (no face) on the button's
  metaphor, ≤ 2.5 s, if it reads.
- **No third-party film/TV footage. No YouTube requests from me** (NEEDS-YOUTUBE.md lists anything that would want YouTube).

## Catalog pass (2026-10-31; CATALOG.md FX-01..81 read in full; all 137 stills of `research/effects-catalog/shots/` LOOKED AT on
## 9 labelled tiled sheets, `work/catalog/singles_1-4.jpg` (79 singles at 480x270) + `strips_1-5.jpg` (58 strips at 1200 px))
- **Fits this video** (a live role-play in the room: two faces, one claim, one reframe, one reaction that flips):
  - **FX-11 Rival Colour Split** → the before/after: two colour fields, cold for OPENER 1 (taken aback), warm for OPENER 2 (curious),
    the same man in both. The hero move.
  - **FX-23 Pointer Tag** → a name tag beside each man the first time he is on screen (Stan at the hook, Matt on his first reaction).
  - **FX-18 Karaoke Leader Quote** → "99% OF PEOPLE" as Stan's own quote, beside his head, oversized quote marks (his claim stays his).
  - **FX-09 Demand Tree** → the reframe's five moves branching off a spine, one row per spoken move.
  - **FX-58 Speaker-Coded Subs** → the YT caption colour per voice (Stan white/red wipe, Matt yellow): the stranger always knows who talks.
  - **FX-73 Chart Reprise Push-In** (as a REPRISE, not a chart): beat 2's "taken aback" face returns at the button inside the split.
  - **FX-16 Portal Zoom** (light) → "change the frame": a thin white frame draws around Stan and the shot pushes through it into the
    reframed opener (a literal frame on the word "frame").
- **Not used before on an Onyx/Scott sample:** FX-11 as a before/after, FX-09 rows, FX-18, FX-16.
- **Leaned on recently, avoided here:** read-along highlighters / web DOCs (Pincus x5), stat charts (Patrón, MATG), FX-27 Red Word Quote
  + FX-79 echo + FX-28 dossier + FX-40 portrait (the batch-6 sibling Still Here's hero set: the batch variety rule).

## What this one does better than the last ones (rule 5; vs Pincus YT/IG 2026-10-31, MATG 2026-10-23, Chris Do 2026-10-25)
1. **The proof is a FACE, not a document**: the payoff shows the same man reacting twice (taken aback → curious), side by side. No
   earlier sample put a before/after of one face on screen; MATG flipped a chart, Pincus highlighted pages.
2. **Two people, both always named and coloured**: two pointer tags and two caption colours from the first second (MATG's three-person
   call had one tag; Chris Do had one speaker).
3. **The viewer leaves with the move**: the five-part opener builds on screen as it is spoken, screenshot-able (Rich Roll's rules list
   was a static card; this one grows with the words).

## Download log (logged BEFORE each pull)
| # | File | Source | Size | Why |
|---|---|---|---|---|
| v1 | `source/63Sv85jlYWg_0.08.00-0.16.00.mp4` | main session (YouTube 63Sv85jlYWg, window 0:08:00-0:16:00, 1080p 29.97 H.264 + AAC) | 114.4 MB | the source (not pulled by me) |
| v2 | `raw/tfts294_roleplay.mkv` | LOCAL derivative of v1 (frames 7448-8825) | ≈ 60 MB | the section the EDL cuts from |
| x1-x6 | `audio/sfx-src/<id8>.wav` | Epidemic Sound SFX (`DownloadSoundEffect`, WAV), the soft swish family only (SUPERHERO rule): 8f1a6bfe Swooshes, Swish, Low, Cloth Movement, Variations · 38a49746 Cloth, Flap, Single Flap, Soft · e435dfaf Whoosh, Soft, Long 01 · 9e39ef94 Swooshes, Whoosh, Airy, Light 01 · 6cbce22f Swooshes, Whoosh, Airy, Long 04 · e62847da Whoosh, Soft, Short 02. None is in the Pincus or Patrón kits (the last two Onyx/Scott sets); each slice tonal-checked (≤ ~13) before use | ≈ 0.2-0.6 MB each | one soft swish per graphic entrance, rotated, sized to the move |
