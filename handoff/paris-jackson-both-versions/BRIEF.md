# BOTH VERSIONS (Paris Jackson) · Abundance Wisdom long-form · BRIEF

## ▶ STATUS: resume here (2026-10-26)
- **Stage:** pre-production, checkpoint 1 (this brief) sent to Affan. **No edit has started; nothing is written to Premiere.**
- **Done:** raw copied (`raw/C1397.MP4`, 14:51, 1920×1080 59.94, PCM 48 k); host transcribed once (`transcript/words.json`);
  source windows transcribed (`transcript/windows/*.json`, quotes located by `work/find_quotes.py` → `work/quote-map.json`);
  minor-frame sweep of every cited local range (`work/sweep/sheet-*.jpg`); grade references measured (`work/grade/`);
  catalog pass (all 81 entries + 137 stills, sheets in `work/catalog-pass/`).
- **Project: ABW10.** All 16 sources in hand and checked (§ 6); locks 1–8 all resolved by measurement (§ 4).
- **Waiting on Affan:** the open answers in § 7 (the Ch1 pickup first).
- **Next after his answers:** step 2 rough cut (LESSONS 18 retake method), then the cold open on the timeline (checkpoint 2).

## 0. The job
| | |
|---|---|
| Locked script | [`brief/PARIS-LONGFORM.md`](brief/PARIS-LONGFORM.md) (🔒 FINAL 22 Oct) + [`brief/PARIS-LONGFORM-SOURCES.md`](brief/PARIS-LONGFORM-SOURCES.md). Part B: "If anything can't be done exactly as written, stop and report it." |
| Raw | `X:\Recordings\Abundance Wisdom\C1397.MP4` → copied to `raw/C1397.MP4` (original untouched). Scripted shoot: retakes hidden by WhisperX, so LESSONS 18. |
| Format | Long-form 16:9. Host 1920×1080 **59.94 fps** (B3 says "24 or 30 fps, match Affan's host footage": the host is 59.94, see § 7). |
| Lane | Premiere (`.setup-complete` lane=premiere). Premiere is up with **ABW10.prproj** open (read-only ping, 2026-10-26). |
| Preset | [`presets/youtube/abundance-wisdom/PLAYBOOK.md`](../../presets/youtube/abundance-wisdom/PLAYBOOK.md) + `LESSONS.md` (gist, never a lock). |
| Publish | within 7 days of the script lock. |

## 1. Rules for this film (where Part B meets the standing rules)
- **No AI imagery at all** ("No actors. No AI." is said on camera). No Higgsfield, no generated stills. Designed motion graphics only.
  **No stock footage either** (FX-48 stand-ins are out): everything on screen is her, the people who were there, real archive,
  or a designed graphic.
- **No minors on frame.** Paris before Apr 2016 is audio only (1c, 2f). No childhood photos of any of the three kids, anywhere,
  thumbnail included. Every archive frame, cover and graphic is checked (sweep below).
- **"Suicide"** is never on-screen text anywhere and never spoken in the first 30 s. 2013 headlines are out (they carry the word);
  no 911 audio, no method detail, no Utah facility named or pictured, the ECT never dated.
- **Real evidence only** (LESSONS 25): every screenshot, headline, post, album cover is fetched from the real source and rebuilt
  faithfully; nothing invented for her "two pages".
- **Export:** he exports himself (never `exportAsMediaDirect`, no phone copies). B6's render path is a question (§ 7).
- **Loudness:** B4 (−14 LUFS integrated, ≤ −1 dBTP) reached with the STATIC chain (measured gain into a limiter), never dynamic
  loudnorm; every source level-matched; 2–4 frame dialogue crossfades.
- **Music:** one sparse sad piano bed (Epidemic) ~−30 dB under host lines only, pulled fully under 0a–0d, 1c, 3a, 3c, 4b, 6a, 6f,
  none after "Happiest Day of My Life" (last two minutes dry).
- **Grade:** warm, high-contrast, measured against the recent MJ-family Shorts (§ 5); THE LAST SHOW host LUT is only a start.
- **Captions:** every clip, AW subtitle style (clean, small, no animation), "[bleep]" in 1b; lower third (FX-42 family) on each new
  speaker's first appearance; small year card top-left on every clip; VERSION ONE | HER VERSION card at the top of Ch2–5, Ch6 HER
  VERSION only.
- **Premiere:** work by sequence name AND id; `lanes/premiere/ACTIVE-WINDOW.lock` for any active-sequence action; FCP XML backup
  before batch changes; never an A/V item on an audio-only track. Work in silence (no players, ffmpeg to files / `-f null`), and the
  silence rule goes in every agent brief. Agents: no Fable; Opus only where judgment needs it.

## 2. Catalog pass (CLAUDE.md learning loop #5, done 2026-10-26)
**Method.** Read all 81 entries of `research/effects-catalog/CATALOG.md` in full (`catalog.json` what / job / build, not the
truncated table). Looked at all 137 reference stills (80 key frames + 57 four-frame strips) frame by frame on 40 contact sheets,
two moves per sheet with each strip laid out 2×2 (`work/catalog-pass/sheet01-40.jpg`).

### 2a. What THE LAST SHOW leaned on (measured, not remembered)
Counted from the built placements (`projects/cbum-last-show/work/redo/*/placement.json`, 99 graphics, 47 codes):
FX-39 source tag 21 · FX-29 float frame 18 · FX-42 kin tag 18 · FX-41 year ghost 15 · FX-37 ghost dissolve 12 · FX-18 karaoke
quote 12 · FX-78 cinema vignette 12 · FX-04 era tag 11 · FX-24 red dash map 9 · FX-71 funnel count 9 · FX-81 stepped 20 fps 8 ·
FX-34 read-along highlighter 6 · FX-79 flash-forward echo 5 · FX-45 liner-note highlight 5 · FX-14 painted sky 5.
**This film cuts those back or evolves them:** FX-29 ≤ 6 (clips mostly play full-frame here), FX-41 only at the chapter year
jumps (≤ 6), FX-18 replaced by quieter quote type, FX-37 kept for the one bookend it earns (11 → 28). FX-39 / FX-42 / FX-04 are
REQUIRED by B3 (source + year on every clip, a lower third per new speaker), so they are redesigned as ONE new mark (§ 2c), not
dropped.

### 2b. Never used on this channel (checked against THE LAST SHOW's placements and SAME NIGHT's built comps)
FX-05 · 06 · 07 · 09 · 10 · 15 · 17 · 19 · 20 · 21 · 22 · 25 · 26 · 38 · 44 · 50 · 51 · 52 · 53 · 58 · 60 · 61 · 67 · 74 · 77
(FX-03 / 56 / 59 / 63 / 68 were only ever listed as suggestions, never built). **Going into this film (≥ 2 required):**
- **FX-61 Earth Dateline Flyover**: Ch1 opens on a real aerial of Holmby Hills with the plain two-line dateline
  "Holmby Hills, Los Angeles / June 25th, 2009" in the sky band (real satellite imagery, a slow glide; no people).
- **FX-26 Inverted Newsprint**: "the tragic little girl… the rich kid who went off the rails…" (cold open) and "the tabloid years"
  (Ch4): REAL headlines, in negative, steep 3D tilt, shallow focus, the key word turning red. Text crops only (no photos of her as a
  minor), nothing from 2013.
- **FX-22 Red Isolate Photo**: Ch1 "the memorial. Staples Center": a real wide of the arena drains to B&W while the stage stays in
  deep red with a small label. Wide only, no identifiable child.
- **FX-21 line-drawing set, objects only**: the six-noun teaser (memorial mic, Utah outline, a bite guard, a butterfly…) and "it
  wasn't on the program" (the Staples stage, an empty mic picked out in red). Honest reconstruction, NO people / silhouettes.
- **FX-67 Highlighter Clipping**: Ch5 estate ruling, the real Good Morning America text in cut strips, "$625,000 … returned"
  in the highlighter block, source line on the strip.
- *Option, only with his OK (it changes the channel's subtitle style):* **FX-58 speaker-coded subtitles, AW-quiet version**: in the
  clips where an interviewer asks (1a, 1d, 2c, 2e, 3a, 6a) the question in grey with a leading dash, her answer in white. Not counted
  toward the new moves.

### 2c. Moves that fit, chapter by chapter (one designed visual per host LINE; clips play their own picture)
| Chapter | Host lines → treatment (FX) |
|---|---|
| **Cold open** 0a–0d | **FX-78** mood grade only here (warm-dark, oval, crushed blacks) so the archive reads as memory; **FX-47 Eyelid Vignette** on 0d: the oval closes on "knock you out…" and lands on black exactly at "weeks." (Part A's cut to black); **FX-79** 0d returns in Ch6 (6a, same source) in its natural grade. New source/year mark (below) on each clip. |
| Cold-open host | "everyone else has told her story…" → **FX-26** three real headlines; "wrote her life story twice… once as the victim… not as the victim" → the **VERSION ONE \| HER VERSION** device introduced (two fields, grey \| warm white, built from **FX-11**'s split, no faces); six nouns → **FX-21** line objects, one per noun, one red accent; "her, or the people who were there, on camera, with the date" → **FX-28** source ledger (real outlets + dates typing in); title **BOTH VERSIONS**: two type layers (grey, white) slightly out of register that slide into one (new, FX-12 family retired for this film). |
| **Ch1** Someone's got to say something | **FX-61** dateline flyover; "Paris is eleven…" ages only, on black (**FX-71**, quiet); hospital → real 2009 press photo of the building, adults only (**FX-08** tile); "the memorial. Staples Center. 20,000" → **FX-22**; "It wasn't on the program" → **FX-21** stage + red mic; 1c → black + word-by-word white caption (B3), optional adult Michael at 30 %; "the brave little girl" → **FX-26** 2009 headline text crop; "when Alex Cooper asked her" → the real CHD episode art (**FX-33** drop). |
| **Ch2** Crash course | VERSION ONE \| HER VERSION card; "79 years old" → real adult Katherine photo + count; **the life line** introduced (**FX-72**: one thin line, 1998 → 2026, her ages under it), "before he even died" pins a point before 2009; 2f → card "OPRAH'S NEXT CHAPTER · 2012 · AGE 14" on black, audio only; "one year later" → the line pins 2013. |
| **Ch3** Fifteen | "June 2013. Paris is fifteen" → **FX-30** whisper date on black (no headlines, no hospital images, no music); 3a with FX-58 subs; split card + RTT; "In 2017 she told Rolling Stone" → the real Feb 2017 cover (she was 18) as a tile; Utah → **FX-24** LA → Utah state outline only (no school, no facility); "Almost two years… by twenty" → line advances (**FX-73** reprise push-in). |
| **Ch4** Sirens | "the tabloid years… wild child" → **FX-26**; "a song called Sirens" → real album tracklist, "Sirens" lit (**FX-45** evolved into the **FX-67** strip look); "January 2020. Twenty-one, and sober" → **FX-73** push into the JAN 2020 pin. |
| **Ch5** No one's business | "You've seen the comments" → real public comments only if they can be fetched, else his words as quiet type (no mock-ups); 5a/5b vertical video in a designed phone-float (**FX-57** without a filmed plate); estate → **FX-67** GMA clipping + TODAY court B-roll + card; "a movie about him" → real poster + her real statement (**FX-34**). |
| **Ch6** The happiest day | HER VERSION only; 6a–6c natural grade (**FX-79** pay-off of 0d); "the album is called Happiest Day of My Life" → the real cover, held (**FX-33**), then the 1 s silent hold on his face; "At eleven… At twenty-eight" → the life line's two ends (11, 28) light together (**FX-73**), **FX-37** used once here; hard cut on "hi, daddy." → 3 s black → end screen. |
| **Every clip** | ONE new top-left mark replacing FX-39 + FX-04: `2013 · 60 MINUTES` in mono caps, year in the film's accent, 4 s fade then it settles to 60 % (B3 year cards). Lower thirds: FX-42 stack, name / relation, new type pairing. |

**Ruled out for this film:** FX-48 stand-ins and any stock (no actors); FX-43 tape morph and FX-44 halftone (both are childhood
photos); FX-40 push-in on a still portrait (LESSONS 30); FX-76 freeze & talk (no freezes under VO); FX-11's AI chrome heads; FX-17
loupe letter (it would invent her pages); FX-50 her music videos (rights); FX-60 tape deck on the audio-only beats (B3 says black +
caption; only with his OK).

### 2d. A new move from outside research (PLAYBOOK § 1.3): NOT DONE YET, announced
YouTube is blocked (`youtube.BLOCKED` since 2026-10-24 13:58), so no new reference video can be pulled and stilled. Candidate
FX-82 **Dual-Grade Split**: the same shot shown twice side by side, cool and desaturated left (the world's version), warm right (hers),
the seam drifting across as the host turns the line. It becomes FX-82 with a reference still once a reference can be fetched.

## 3. Beats THE LAST SHOW by… (≥ 5 % smoother, more premium, more expensive; every item checkable)
Baselines are THE LAST SHOW's own measurements (`work/redo/REPORT-19.md`, `REPORT-REVIEW-2.md`).
| # | Item | THE LAST SHOW | This film | Check |
|---|---|---|---|---|
| 1 | Dialogue joints with a crossfade | ≥ 20 ms fades at joints | **100 %** of insert↔host joints and of trims inside a source carry a 2–4 frame (33–67 ms) crossfade (B4); host-internal joints keep the measured 15 ms equal-power join (CLAUDE.md splice lock), 2 frames only where room tone gives the handle, so no word onset is clipped | readback sweep of every A-track joint + word-onset check |
| 2 | Chopped insert→host words reaching his first watch | 3 (fixed after review 2) | **0**: word-level joint sweep runs BEFORE his first watch | forced-aligned word ends vs clip ends |
| 3 | Source loudness match | cold open spread 0.1 LU; mix −21.3 LUFS | every insert within **±1 LU** of the host; mix **−14.0 ± 0.5 LUFS, TP ≤ −1.0 dBTP** | offline mixdown replicating the Premiere mix (`preview.py` pattern) |
| 4 | SFX variety | 101 distinct takes of 213 cues (47 %) | **≥ 60 %** distinct, no back-to-back repeat in a class | `build_sfx` report |
| 5 | Air-sound share | 65 of 213 (31 %) | **≤ 25 %** | same report |
| 6 | Phone-band audibility | not checked | **100 %** of cues pass `cue_check.py` | checker output |
| 7 | Archive grade | host LUT only; archive graded by eye | host AND every source inside the measured MJ-Shorts band (§ 5) | per-source frame stats script |
| 8 | Built graphic settle time | target ≥ 1 s, not reported per graphic | **every** graphic settled ≥ 1.0 s before its cut; minimum reported | browser probe of each comp's last tween |
| 9 | Mock-ups at first watch | 2 (avatar, post) | **0**: every document has its fetched URL in the plan | plan audit |
| 10 | Moves new to the channel | – | **≥ 4** (FX-61, FX-26, FX-22, FX-21, FX-67) | placement `fx` |
| 11 | Heaviest repeats | FX-29 ×18, FX-41 ×15 | FX-29 ≤ 6, FX-41 ≤ 6 | placement `fx` |
| 12 | Continuity device | none recurring | the life line returns in every chapter (Ch2–Ch6) | storyboard |
| 13 | Review-1 defect classes | sub-1 s cover, black-open cover, portrait push, freezes | **0** of each before his first watch | `verify` sweep |

## 4. Lock conditions (Part A): status at checkpoint 1
"By ear" = WhisperX word timings + wav2vec2 forced alignment of the candidate wordings (`work/fit_test.py`); never playback.
| # | Condition | Finding | Option used |
|---|---|---|---|
| 1 | No minors on frame | Swept every local cited range at 1 fps (`work/sweep/`): Telegraph 0a, 60 Minutes 0b/1a/2b/3a, all CHD ranges, Zane Lowe 6e/6f, Jack Osbourne 2d/5c/5d, her IG video 5a/5b: adults only (Alvarez, the courtroom, Katherine, Liz Hayes, adult Paris, the hosts). Flag: the 60 Minutes set has framed photos behind Katherine, fully out of focus and unidentifiable. Two local files found to be childhood footage ("I Love My Daddy So Much", a Jacksonology interview) are out, copies deleted. | ✅ local sources. **Downloads (swept 2026-10-26):** ECT, Shetty, septum, biopic used ranges: adult only. **TODAY estate 0:03–0:04 is a photo of Michael with Paris as a CHILD**, inside Part A's 0:02–0:13 B-roll range → the B-roll is 0:05–0:11 only (her walking into court). **Red Table Talk 1:41–1:48: ET cut in four undated Instagram photos of her** under her 3b audio; undated = can't be proven 2016+, so never shown (§ 7). Memorial and Oprah are kept in the job as WAV only (no picture of her as a child exists in the job). |
| 2 | 1b swear | Heard cleanly: "So I was like, **fuck** it, we ball." (CHD local 23:36.48–23:36.64, p 0.97). Note: Part A's "It happened on stage" is not said; she says "Oh, it kind of just happened in the moment… Yeah, but on stage, it was like they looked…" | Bleep the F-word only, keep "we ball"; caption "[bleep] it, we ball"; captions follow her real words |
| 3 | 3b Red Table Talk wording | Not clean. Two ASR passes hear "people would tell me to kill myself every day" but at very low word confidence (would 0.02, tell 0.05, to 0.00); forced alignment of four wordings (people would tell / people would totally tell / totally tell / people told) all fit poorly and alike (0.55–0.62), under ET's music bed. Local RTT file 1:47.8–1:50.6. Voice = Paris (voiceprint 0.80). | **Fallback as written: cut 3b at "…a lot of pressure. It was really hard."** (local 1:35.7–1:48.7). Consequence: the host's next line ("People telling a young girl to kill herself. Every day.") then states it in his voice (§ 7) |
| 4 | 4a heroin pre-line (CHD 37:44) | Not clean. ASR hears "we were trying on heroin" at low confidence; forced alignment of five wordings (trying on / strung out on / on / tripping on / trying) all fit poorly and alike (0.39–0.47): the four words sit in 0.6 s. | **Fallback: skip the pre-line**; 4a = the 42:05 engagement line only (where she clearly says "strung out on drugs") |
| 5 | 5b birthday line | The line is in **her own Instagram video of 29 Aug 2023** at 0:05.9–0:15.6 (the video Access Hollywood and the fan compilation both re-broadcast). The AH upload can't be fetched (YouTube blocked). | Proposed: use her original, card "PARIS'S INSTAGRAM · 29 AUG 2023" (needs his OK, it substitutes the named upload) |
| 6 | 5f biopic line is her own voice | **It is her voice**: voiceprint vs Paris (CHD) 0.65, vs Paris (Jack Osbourne) 0.57, vs the TODAY reporter 0.29 (reporter vs reporter 0.78, Paris vs Paris 0.76). Picture = her Instagram video (1:51–2:01). Her words: "The film panders to a very specific section of my dad's fandom that still lives in the fantasy. It's not real, but it's sold to you as real." (local 1:51.2–2:01.0; Part A's wording differs, captions follow hers) | **Keep 5f** (it stays #2 in the trim order) |
| 7 | Butterfly not the Sep 5 Short's ending | The Sep 5 YouTube final in Final Renders, **`Honor final YT FInal.mov`** (14:32, with audio, 36.0 s), ends: "…So I'm not going to like publicly do something on Instagram and I'll find my own private way to honor it." No butterfly anywhere in it (ASR `work/lock7/honor-final-asr.txt`, frames `work/lock7/`). The 13:21 video-only draft `parih.mp4` ends the same. `daddy.mov` (9 Sep) and `Paris Life.mov` (19 Oct) don't use it either. | **Keep 6f (butterfly) as the ending**; he confirms the published Short is this file |
| 8 | ET/TODAY packages: Paris's seconds only | Measured by words + voiceprint: ECT 0d 0:27.1–0:33.4, 6a 0:08.6–0:39.7 (Jay + Paris; ET narrator starts 0:40.3), 6b 0:55.5–1:00.1, 6c 1:07.5–1:17.1; RTT 1:35.7–1:48.7; septum 0:01.6–0:35.9; biopic 5e 0:23.4–0:26.9, 5f 1:51.2–2:01.0; estate B-roll picture only. Every reporter / narrator second is outside these spans | ✅ reporter muted everywhere; picture limits in row 1 |

## 4b. Host recording vs Part A (from the transcript + re-ASR + fit tests of the doubtful spans)
- **Missing line:** Ch1's cliffhanger **"Two versions. Remember that. Because the next part, nobody saw."** is not in the raw: after
  "Paris didn't tell it like that" (262.2 s) there are 9 s of room tone (−63 dB) and then "Version one". **His call (2026-10-26): cut it, go
  without it.** Ch1 ends on 1d; the L3 loop is still planted by 1d itself and named at the top of Ch2–5.
- **"June 25th, 2009"**: "2009" is not heard (two ASR passes; the aligner can squeeze it into the gap either way, 0.85 vs 0.84). The FX-61
  dateline shows "June 25th, 2009" on screen, so the year still lands.
- **"It was his fans"**: he most likely says "her fans" (ASR), the middle word is swallowed (aligner 0.00 for his / her / the). Part A
  means Michael's fans.
- "January 2020. Twenty-one, and sober": ✅ said as written (re-ASR "January 2020, 21 and sober").
- Small wording drift, kept (it's his read): "everyone else had told her story", "she finally describes it", "You think the hardest
  part is over". At 836 s he reads 6e's line ("She started crying in the studio"): not host text, cut.
- Retakes: many lines have 2–4 takes (e.g. "A friend on her floor" ×3, "People telling her to kill herself again" ×4); the LAST complete
  take is kept (LESSONS 18 method, cluster sweep to 0 repeats).
- **Runtime estimate:** ≈ 6 min host + ≈ 10.5–11 min clips ≈ 16:30–17:30 before trims. If it runs past 16:30, Part A's trim order applies.

## 5. Grade reference (measured 2026-10-26, `work/grade/`)
12 frames per Short, measured INSIDE the active picture only (the black surround and the white window lines cropped per frame,
caption pixels > 0.92 luma masked); means of luma · p95–p5 contrast · black p2 · saturation · R−B warmth.
| source | luma | contrast | p2 | sat | R−B |
|---|---|---|---|---|---|
| MJ Kids Saw (24 Oct) | 0.298 | 0.529 | 0.065 | 0.493 | 0.129 |
| Daddy Final YT (25 Oct) | 0.297 | 0.525 | 0.067 | 0.485 | 0.127 |
| MJ Sib Final YT (22 Oct) | 0.283 | 0.531 | 0.065 | 0.571 | 0.216 |
| Paris Life (19 Oct) | 0.273 | 0.525 | 0.035 | 0.606 | 0.217 |
| Died Final YT (21 Oct, red-washed outlier) | 0.242 | 0.393 | 0.042 | 0.702 | 0.312 |
| **HOST raw C1397** (full frame) | 0.226 | 0.487 | **0.002** | **0.726** | 0.215 |
Target band for this film: luma 0.27–0.30, contrast ≈ 0.52–0.53, black floor p2 0.035–0.065 (rich, not crushed to zero),
saturation 0.49–0.61, R−B warmth 0.13–0.22. The host is darker, crushed to zero and over-saturated (the hot-pink wall): the grade
lifts the floor and mids, pulls the wall's saturation, keeps the warmth, skin protected. Every archive source is graded into the same
band and checked by the same script.

## 7. Open questions for Affan (checkpoint 1), highest stakes first
1. ~~Premiere project~~ → **ABW10** (his answer, 2026-10-26).
2. ~~Ch1 cliffhanger not recorded~~ → **cut; go without it** (his answer, 2026-10-26). Ch1 ends on 1d's "…not through the eyes of the victim."
3. **5a/5b from her original Instagram video** instead of the TMZ / Access Hollywood packages: OK?
4. **"Suicide" in captions:** spoken in 3a (the interviewer: "It is reported that she tried to commit suicide") and in 6a (Jay: "…a
   particular suicide attempt?"). B5 says caption every clip; B7 says the word is never on screen. (a) the caption drops that word only
   ("…she tried to commit —. Is that true?") ← my pick; (b) no caption on that one sentence.
5. **5a swear:** her original says "people lose their **fucking** minds" (Part A writes "lose [it]"): bleep it like 1b, caption "[bleep]"?
   (She also says "they **tell** me", not "told": captions follow what she says.)
6. **"his fans" / "her fans"** (end of Ch4): keep his read, or pick up "his fans"?
7. **Silent beats:** B1.6 ("someone speaking at every moment") vs Part A's 2 s silent TITLE CARD and the cut to black after 0d's "weeks.":
   allow both as silent beats (my pick), or lay the title over speech?
8. **Export:** B6 asks for a render to `E:\Shorts\Abudance Wisdom Shorts Exports\Final Renders\Paris Long-form.mp4`. Standing rule: you
   export. Render that file myself, or will you export from Premiere?
9. **Subscribe alerts:** THE LAST SHOW had 3 (your ask); Part A is silent. Same 3 small alerts, or none on this film?
10. **FX-58 option:** interviewer questions in grey, her answers in white (changes the channel subtitle style): yes / no?
11. **Red Table Talk picture (3b):** ET cut four undated Instagram photos of her into the middle of her 3b audio
    (RTT 1:41–1:48). They can't be proven 2016+, so they never go on screen. Replace those 7 s with (a) the Red Table Talk
    two-shot / Willow listening shots from the same package (how ET itself cuts away) ← my pick, or (b) a designed card over her voice?
12. **Lock 3 fell back** (the "kill myself every day" words aren't clean), so 3b now ends on "It was really hard." Your next line,
    "People telling a young girl to kill herself. Every day.", then says it first, in your voice. Keep it as is (my pick), or listen to
    RTT 1:47.8–1:50.6 yourself and overrule the fallback?
13. **ET's censor emoji in 6c:** ET bleeped a word in "that's not [bleep] gonna work for me" and burned a cartoon angry-face "&$!#%"
    over her face for ~1 s. (a) cut away to the On Purpose wide shot for that second, keeping her audio and the bleep ← my pick;
    (b) leave it as ET aired it.

**Decided by the brief unless you say otherwise:** sequence 59.94 fps (B3: "match Affan's host footage"); no Topaz or any AI
processing ("No AI"), plain light sharpen + grain on the 2009–2013 SD sources; the 620×348 Telegraph clip sits as an inset at
≤ 115 % (never blown up full-frame).
**FYI:** the "skool" neon sign is in frame behind you throughout; the grade keeps it unless you say. The Telegraph's own burned-in lower
third reads "Michael Jackson's bodyguard" (local 0:05–0:08, right up to the in-point) while Part A's card says "director of logistics":
the picture starts after their bar clears so the two never show together.
**Downloads:** all checked on arrival (ffprobe, the 1 fps minor sweep, burned-in chyron / caption scan), 2026-10-26.

## 6. Sources (B2): what is here, what he downloads
Local copies in `broll/` (B2 names; originals untouched). In/out by words (WhisperX + wav2vec2), offsets vs the brief's YouTube
times measured per quote in `work/quote-map.json` (+0.1 to +9.8 s: the brief's times are approximate; the words win).
| B2 | ID | Local source | Clips | Status |
|---|---|---|---|---|
| 01 Telegraph | D0Acz0JmPd0 | `E:\Bullshit Folder\Henry\Michael-Jackson-Paris-SnapYT.App.mp4` (via mj-kids job), **620×348** 25 fps | 0a | ✅ 0:07.99–0:42.18; lawyer's question 0:11–0:19 to drop. SD: inset at ≤ 115 % (B3), never full-frame |
| 02 60 Minutes AU | jAGbux3rOjE | `E:\Bullshit Folder\Drake\…60 Minutes Australia.mp4`, 1080p 29.97 | 0b 1a 2b 3a | ✅ all four found |
| 03 Call Her Daddy | jR8-dzLECUE | `E:\Bullshit Folder\KIDS\Paris Jackson- Love, Loss, & Listening to Your Intuition.mp4`, 1080p 23.976, 71:53 | 0c 1b 1d 2a 2c 2e 4a 4b 4d 6d | ✅ all found |
| 06 Jack Osbourne | -kXLpqK0MaM | `E:\Bullshit Folder\Henry\Paris Jackson On Grief, Music _ Growing Up In The Spotlight.mp4` | 2d 5c 5d | ✅ |
| 15 Zane Lowe | jtFZfXDODnA | `E:\Bullshit Folder\Henry\…Zane Lowe Interview.mp4`, 1080p 23.976 | 6e 6f | ✅ |
| 11/12 TMZ + Access Hollywood | 2sp3lUsvwyk / V9IIkf5sd74 | **her ORIGINAL Instagram video**, 29 Aug 2023 (`E:\Bullshit Folder\Henry\Paris Jackson about her father's birthday.mp4`, 1080×1920) | 5a 5b | ⚠ substitution to approve: same words, no TV hosts to mute, better picture |
| 04 ET ECT | Qg9AG0nM58M | IDM 2026-10-26, 1080p H.264 | 0d 6a 6b 6c | ✅ 0d 0:27.1–0:33.4 · 6a 0:08.6–0:39.7 · 6b 0:55.5–1:00.1 · 6c 1:07.5–1:17.1. ET bleeped a word in 6c ("that's not [bleep] gonna work for me") and burned an angry-emoji "&$!#%" over her face at ~1:16 (§ 7) |
| 09 Shetty Short | FTdLn-4PgKo | IDM, 1080×1920 vertical | 3c | ✅ 0:02.8 "What was the experience like…" → 0:47.6 "…if you want to get out." Captions are burned into the picture: shown as a face crop above them |
| 08 ET Red Table Talk | pfADUCKKF0c | IDM, 1080p | 3b | ✅ 1:35.7–1:48.7 (lock 3 fallback). ET b-roll of undated Instagram photos at 1:41–1:48 (§ 7) |
| 10 ET Septum | o6fj3_t5Z5Y | IDM, 1080p (her TikTok inside ET's frame) | 4c | ✅ 0:01.6–0:35.9; spaghetti demo 0:18–0:22 skipped (Part A); ET censor emoji at ~0:32 over "and I'm just, [bleep] I don't know", trimmed out (filler inside the range) |
| 14 TODAY Biopic | sSS7K6vjnHY | IDM, 1080p | 5e 5f | ✅ 5e 0:23.4–0:26.9 · 5f 1:51.2–2:01.0 (her voice, lock 6). TODAY's lower bar "FAMILY FEUD OVER MICHAEL JACKSON FILM" is cropped out |
| 13 TODAY Estate | NNplDzFq_oo | IDM, 1080p | court B-roll | ✅ picture 0:05–0:11 only (0:03–0:04 is a childhood photo). Lower bar cropped |
| 07 ABC Oprah | kVbchWeM1tA | IDM → kept as `07_ABC_Oprah_2012_AUDIOONLY.wav` | 2f | ✅ "I think I'm doing all right." 0:26.9–0:28.3, between the narrator's words (0.7 s / 0.5 s gaps) |
| 05 Memorial | (his full CBS2 feed) | `E:\Bullshit Folder\Henry\Michael Jackson Memorial Service 1958-2009 (4K).mp4` → `05_Memorial_2009_AUDIOONLY_9490-9575.wav` | 1c | ✅ 2:38:40.5–2:39:04.4: "I just wanted to say…" · Janet "Speak up, sweetheart, speak up" · "Ever since I was born, Daddy has been the best father you could ever imagine. And I just wanted to say I love him so much." |
| ~~11/12/12b~~ TMZ, Access Hollywood, fan comp | | not downloaded | | replaced by her original Instagram video (pending his OK) |
All 16 sources are in hand (2026-10-26): every file H.264, ffprobed, minor-swept, chyron-scanned. No burned-in "suicide" text in any used range (ECT's intro card "ELECTROCONVULSIVE THERAPY" sits in the excluded 0:04–0:08).
