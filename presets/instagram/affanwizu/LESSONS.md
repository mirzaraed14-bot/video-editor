# @affanwizu: lessons

Format: *lesson → change made → file*. Newest first. A lesson that repeats becomes a rule in
`deep-talks-style.md` / `roman-urdu.md` / `PLAYBOOK.md`.

## 2026-10-23: names come from his screenshots (ABW10 Seq 22)

- **When the reel shows screenshots, read them before writing a single name.** Seq 22's V5 carried 13 of them: the photo
  at 0–5 s settled "arslan ash" (Whisper: ارشلین ایش / "Arsalan Ash"), the event poster "IMMAF" (the English listener:
  "IMMF"), the fundraiser card "gohelpme.pk" and "7 lakh PKR". → PLAYBOOK habit: export the V2+ stills and read them first.
- **A slow spoken list is one item per line** ("registration / tickets / nutrition"): on one line, 2.3 s for 3 words reads
  as missing words to the gate, and it is also how the list is said.
- **Known false warning:** the English listener sometimes echoes its own prompt sentence ("video script nahi ki")
  mid-segment, which `echoes_prompt()` misses (Seq 20 + 22) → caption_qa warns "heard script". Warning only; fix the filter
  if it ever produces a FAIL.

## 2026-10-23: a reel that READS OUT comments (ABW10 Seq 20)

- **Read-out comments and imitated pitches are quoted speech:** every line gets its own pair of quotes (BELIEVE's
  `“aby yar mukao ya isko”` / `“jaldi jaldi karo”` / `“ghar chalo yar”`), not one pair spanning the lines. → applied; the rule
  is already in `roman-urdu.md` § quotes.
- **`caption_qa.py` counted a web address as one spoken word** ("AyanGFX.com" = 1.52 s of speech → FAIL HANGING). It is said
  "ayan G F X dot com". → `spoken_words()` counts an address by its parts (caps run = letters, each dot = "dot" + tld).
- **WhisperX on a 3-minute monologue dropped three stretches and looped once**; one batched hi + en re-decode of every gate
  flag (15 windows) resolved them all before a line was written. On CPU it took ~13 min while another job shared the CPU:
  for long reels, batch the windows once rather than re-decoding spot by spot.

## 2026-10-20: "bruv what are these shitty captions" (ABW10 Seq 12) — speed-changed clips + a late first cue

- **Every A1 clip was at 1.1x or 0.8x, and Premiere reports a speed-changed clip's `inPoint` DIVIDED by the speed**
  (the 0.8x clip read 250.04 s on a 215.7 s file; the real in point is 250.04 × 0.8 = 200.03 s). The rebuild pulled the wrong
  stretch of the take for all 15 clips: 9.4 s of speech instead of 33.6 s, so the reel got 10 captions of the wrong words.
  → `sequence_reference.py` reads `getSpeed()`, cuts at in × speed, plays the audio through `atempo` at the clip's speed, and
  ABORTS when a clip returns less audio than its timeline length. Same quirk logged in `lanes/premiere/lab-notes.md`.
- **Premiere lays an .srt's FIRST CUE at the drop point, not at 00:00.** v1 started with an empty `@0.00 |`, its first cue sat
  at 4.13 s, and every caption landed 4.13 s early. → the first line always starts at `@0.00` (their own rule: the first
  line shows from frame 0); `build.py` prints a ⚠ when the first cue is later than 0.
- **The picture rebuild gave each still ONE frame**, shifting every later frame (chin read y1330, true y1270).
  → stills are looped for their timeline length (`sequence_reference.py`).
- A gate that only checks LENGTH (GATE A) can't see a wrong in point: the audio was exactly 40.583 s and mostly the wrong
  words. What caught it was the creator's waveform vs my "9 s of speech". → when speech is under ~half the cut on a talking
  reel, treat the rebuild as suspect before captioning (now also enforced by the short-clip abort).

## 2026-10-11: a "captions" sequence on his own camera take can be ENGLISH (Seq 44)

I assumed Urdu (every earlier caption job on his C-/CAM- takes was an @affanwizu reel) and started the `--lang ur` pass;
he stopped it: *"its an english video"*. → PLAYBOOK § 1 already says to confirm the language: do it FIRST (listen to a
few seconds or let Whisper detect it) before any Urdu pass, and ask the style when the language is English. His pick
for that English vertical: the plain **white** style as an .srt track (`projects/seq44-short/RUN.md`).

## 2026-10-19: first ABW10 job (Sequence 09) — a loop at the very START, and the loop window

The Urdu pass looped the opening ("dekhne ke liye bhi difference hota hai, meri shuru mai" ×3, 0–7 s) and the 15-word loop
window missed it (a 7-word phrase repeated 3 times spans 14 words). → window 17 words in `transcript_check.py` and
`caption_qa.py`: catches it, the Seq 26 loop and the middle loop here, and stays quiet on Seq 42–51 and the four reference
reels (rhetorical repeats like "phir mene… phir mene…" sit further apart). The English listener had the real opening.
Also: a new project number holds other channels' work (ABW10 = Onyx reactions too) → check frame, tracks and language
before forcing `--lang ur`, and prefix the job with the project (`abw10-seq09-short`).

## 2026-10-13: the ending dropped a 4th time (Seq 51) → `transcript_check.py`

Seq 17, 20, 29 and now 51: WhisperX stops before the cut ends and squeezes the last sentence early (Seq 51: words end at
163.1 s, 4.7 s of speech after, "sunglasses mene promote kardi… mai khud pehnta hun" lost). The checks that caught it lived
in session scratch scripts. → `transcript_check.py` (preset) runs Gate B + the ending rule + loops + true silences in one
command and prints what the English listener heard in each bad window (on Seq 51 it printed the missing ending verbatim).
Also from Seq 51: two TIMELINE GAPS = two silences (27.05–35.88, 42.85–49.15) get explicit `@<sec> |` lines so no caption
hangs over a gap; "easy mode" (آسان موڈ) and "something in return" (heard "in it") restored.

## 2026-10-11: tool bug — the rebuilt cut had NO picture (Seq 47)

`sequence_reference.py` joined the V1 clips with the concat demuxer straight off the camera file. This camera's
`CAM_*_D.MP4` (4K HEVC 29.97) also carries a 1280×720 MJPEG thumbnail as a second video stream, and through the demuxer
the picture came out EMPTY: the reference was audio-only, so `chin-line.py` crashed (IndexError) and build.py would have
had no frame grid. → the picture is now built per clip from the main stream only (`-map 0:v:0`), each clip with its
own Scale/Position, then joined; the tool now refuses to finish if the result has no video stream. Regression check:
Seq 42 measures chin y991 vs y998 before (keyframe-exact framing now).

## 2026-10-11: "2 words per layer" (Seq 45) — one request so far, not yet a rule

The creator asked for Sequence 45 at 2 words per layer. Splitting each 5-word line on its own left 50 one-word scraps and 44
layers under 0.25 s (unreadable). What worked: time every word, then pair BY HAND on natural units across the old line
breaks; allow 3 words only for a verb chain said too fast to split ("kar rha hun" = 0.18 s) or to keep a negation with its
verb ("ni ayen ge"); never leave a layer under 0.2 s. Result: 153 layers, 98 × 2 / 35 × 3 / 20 × 1, median 0.45 s on screen.
If they ask for it again, it becomes a `--max-words 2` mode for this channel (with that pairing logic) and a PLAYBOOK rule.

## 2026-10-10: tool bug — captions snapped to a 0.1 s grid (Seq 31, 32, 41, 42)

`build.py` snaps every caption switch to the reference cut's frame rate. The long-sequence rebuild (Seq 31's
`rebuild2`, then `sequence_reference.py`) wrote its picture at 10 fps (it only fed `chin-line.py`), so every switch
landed on a 0.1 s grid: up to 50 ms off, 21 ms on average (the creator's own switches sit ~34 ms from the word).
→ `sequence_reference.py` now reads the sequence's own frame rate (`seq.timebase`) and writes the picture at it.
Seq 41 and 42 were rebuilt and re-sent; Seq 31 and 32 shipped on the 0.1 s grid (their captions.txt has since been
edited outside this job, so they were not regenerated without asking).

## 2026-10-06: the ending drop, third time (ABW8 · Sequence 29)

`words.json` stopped 6.6 s before the cut (25.9 vs 32.5 s) with 6.3 s of speech in the gap; "jo professional hai wo"
was pulled 6.7 s early and the seven seconds before it were gone. Three of the last six caption jobs (Seq 17, 20, 29)
had this exact failure; the § 2 rule (re-decode the last 6–10 s whenever the last word ends > 1 s early) fixed it
in one pass, and `caption_qa.py` would have failed the raw version. If it keeps repeating, automate the tail
re-decode inside `codeswitch_pass.py` instead of doing it by hand.

## 2026-10-04: Seq 25 + Seq 26 — the stand-in list grows, and a loop precedes a drop

- **Seq 25:** "especially pakistan mai" came back as خاص طور پر; the CONNECTOR warning found it on the first try.
- **Seq 26:** the Urdu pass LOOPED ("edit karta tha iske liye" ×3) and then dropped 5.6 s of speech; four English
  phrases were translated: "the reason … is because" → اس کی وجہ ہے کہ, "but" → لیکن, "no offense to editors, it's
  just that" → ایڈیٹروں کو کوئی فرق نہیں …, "and that's a fact" → اور یہ ایک حقیقت ہے.
  → `caption_qa.py` now warns on a LOOP (same three words 3+ times within 15 words: zero hits on the four reference
  reels) and knows وجہ / فرق نہیں / حقیقت as stand-ins. Loops came before missing speech on Seq 11 and Seq 26:
  whenever one fires, re-decode the loop plus the next few seconds wide.

## 2026-10-02: the misplaced ending repeated (ABW8 · Sequence 20)

Second reel in a row (after Seq 17) where WhisperX dropped the second-last sentence and placed the last one 3.5 s
early: `words.json` ended at 30.9 s, the cut at 34.8 s, and the tail measured −23.4 dB (speech). Caught by Gate B;
`caption_qa.py` would also have failed it (UNCAPTIONED after the last caption). A repeat → now a PLAYBOOK rule
(§ 2 Gate B: when the last word ends > 1 s before the sequence end, re-decode the final 6–10 s and time the
closing lines from it).

## 2026-10-01: learning pass on four finished reels (Khayal, balcony, BELIEVE, UNi; 211 lines)

The creator's brief: *"you translate the English bit into Urdu"*, *"learn how I do captions"*, *"some caption
layer is extended too long while the next speaking bit has started"*. All 211 of their lines are now ground truth
with frame-exact timing in [`reference/`](reference/README.md), pulled from the exports by `extract_captions.py`.

1. **The timing rule was never the problem.** On Khayal (= my Seq 15) they kept the switch time of all 52 lines
   they didn't reword, every one within a frame. On their own reels the switches sit within ±0.1 s of WhisperX's
   first-word start. → rule confirmed, nothing changed → `deep-talks-style.md` § Timing.
2. **"Hanging" captions are dropped speech.** Whisper drops a stretch, so the line before it holds over words it
   doesn't show: Seq 15 `aye age ni` held 5.1 s over four lines. Their own lines never carry more than 0.78 s of
   speech per word. → `caption_qa.py` measures speech with Silero (independent of Whisper) and FAILS a line over
   0.45 s × words + 0.6 s, and any speech with no caption (in a gap, before the first line, after the last).
   Zero false alarms on their 211 lines. On my shipped work it found Seq 15 `aye age ni`; Seq 11 "founder explains
   the science of perfumes in an entertaining way" (missing); Seq 17 "2 million followers", "she is the
   attraction, right? she is the marketing" and **the whole closing sentence**, which I had placed 3.7 s early.
3. **English: Whisper keeps his nouns (spelled phonetically) but TRANSLATES or DROPS his connector phrases.**
   doesn't mean → ایسا, it's just that → ایسی طرح (translated); most likely, but, as such (dropped). Quoted lines
   ("aby yar mukao ya isko") dropped whole; six `bohat` collapsed to three.
   → `codeswitch_pass.py`: a second listener with a code-switched prompt on every ≤10 s chunk. Measured: 19/34
   English test phrases kept in English vs 3/34 without a prompt. It also hallucinates (it pasted the prompt into
   BELIEVE and UNi and skipped 8 s of Khayal), so it is never the transcript, only a check: `caption_qa.py` warns
   on every English word it heard that the caption on screen doesn't show (leaked fragments filtered by p < 0.2 or
   impossible durations). It flags my Seq 15 "it's just that" / "choose", stays quiet on their reels.
4. **Their spelling, counted on their own typing** (→ the 🔒 table in `roman-urdu.md`, `caption_qa.py --fix`):
   joined `aapko aapke aapne isme jisme iska usne` (split forms: 0), `or` never `aur`, `kia` for what/did, `lye`,
   `chahye`, `hazar`, `lac`, digits for every number, curly apostrophes in English contractions, quotes around
   quoted speech (one pair per line) and around a weighted English word (`aap “destined” hain`).
5. **Phrasing:** median 4 words (BELIEVE 3), max 6, a line on screen a median 0.9 s. They break at the breath even
   when it strands `aap` at a line end.
6. **Builder bug fixed:** a last line keyed by `@<sec>` past the transcript's end got an end time BEFORE its start
   (Seq 17 v2). It now holds to the end of the cut, as all four reference reels do → `build.py`.

**Seq 17 re-delivered as v2** with all of the above (176 cues; v1 kept as `seq17-short.v1.srt`).

## 2026-09-30: WhisperX drops speech silently (ABW8 · Sequence 17, 169 lines)

Two lessons, both now hard gates in `PLAYBOOK.md` § 2:

1. **A concat rebuild closes the sequence's gaps.** Seq 17's 74 clips sum to 181.65 s but the sequence
   runs 184.92 s — one 3.27 s gap at 175.4 s. The first rebuild concatenated the clips and came out
   181.65 s, which would have pulled every caption after 175 s three seconds early. Fix: insert
   `color=black` + `anullsrc` per gap, then check the rebuild's duration against the sequence end.
   → GATE A.
2. **A "pause" in `words.json` can be dropped dialogue — measure it, don't trust it.** Two gaps
   (8.5→15.0 s and 48.9→53.2 s, 11 s total) read −27 dB mean, the same as the take's speech; real
   silence in the same file reads −55 dB. WhisperX had simply dropped them, with no warning. The
   recovered lines carried the reel's core statistic ("follower count hai 350,000 … jo views hain,
   in mai difference bohat zyada hai") and its pivot ("she already has two million followers — for
   the last eight reels ni aye"). A caption pass that trusted the first transcript would have shipped
   a reel missing its argument. → GATE B.
   - **Re-decode WIDE spans.** A 3.4 s slice of 45.6–49.0 invented "2 million followers ke liye aakhri
     aath reel"; the 42.0–58.5 slice around it read the same audio correctly. Short windows hallucinate.
   - The main pass had also **mis-placed** words: "aap agar yahan reels pe jayen…" sat at 45.8 s in the
     first transcript and at 50.0 s in the clean re-decode. When a span is re-decoded, replace the whole
     window, never just the empty part.

**ASR fixes this job** (context repair, per `roman-urdu.md`): `pachpan se` → **bachpan se**,
`پیچھ` → **page**, `سٹرونگس` → **strongest**, `ایسیل ایسٹھیٹکس لینک` → **SL Aesthetics Clinic**,
`شاہستہ لوڈی` → **Shaista Lodhi**, `وچیز نوٹ بینگ یوٹلائز` → **which is not being utilized**,
`دیکھ رہو نا` → **dekh rahe ho na**, and a restored `se` in "sab se strongest point".

## 2026-09-29: the creator's caption corrections (ABW8 · Sequence 15, 68 lines)

**52 of 68 lines (76 %) shipped verbatim.** Every edit found was one of three kinds:

1. **A NEGATION MUST NEVER BE SPLIT FROM ITS VERB.** I wrote `aye age ni` / `barh pa rahe`; they made the
   second line `nai barh pa rahe`. A caption that ends on `ni`/`nai` and continues the verb on the next line
   reads as two broken halves. → keep `ni + verb` in ONE line, even at the cost of a 6-word line → `roman-urdu.md`.
2. **They restore the connective I trimmed at a line head**: `aap under perform` → `islye aap under perform`;
   `to aap excel` → `usme to aap excel`. When a line starts mid-clause, keep the connective that ties it back.
3. **Real words beat ASR guesses**: `ragre yar` → `ragre jarhe ho`, `fail hua tha` → `fail hojata tha`,
   `aap is ke liye` → `aap us ke liye`, `aap apni` → `aap apne lye`, `aap destined hain` → `destined`.

**Spellings confirmed by their own typing:** `islye`, `lye`, `jarhe` (ja rahe), `hojata`, `usme`, and `nai`
alongside `ni` — they did NOT change any of my `ni` spellings, so both stay valid; `ni` remains the default.

**Reading a learning pass out of the project file (method note):** Premiere stores caption text in a binary
Source Text blob; ExtendScript `getValue()` returns nothing usable and a live read of >~40 clips truncates.
The route that works: gunzip the .prproj, attribute every `AE.ADBE Text` layer to its clip `<Start>` (objects
are serialised flat, so an `ObjectRef` belongs to the nearest preceding `ObjectID`), then match by TIME against
the delivered lines. **Caveat: sequences in the same project share timeline positions, so a match must also
beat a text-similarity check** — 6 lines stayed unresolved because Sequence 10/11 captions sit at the same seconds.

## 2026-09-19: learning pass on the SHIPPED reel (Sequence 18 → `ameer.mov`)

The creator's goal: raw file in, finished reel out, nothing touched by hand. Everything they did by hand this time
is now written down in [`reel-recipe.md`](reel-recipe.md), so it can be automated next time:
- **Cut:** a median −169 ms on every tail and +69 ms on heads. Take choices all stood. → `POLISH_TAIL_MS=20 POLISH_LEAD_MS=15`
  (new env overrides in `polish-boundaries.py`) → `PLAYBOOK.md` § 0.
- **Frame stack Claude didn't build:** V2 Black Video (36 %, fade to 100 % over the last ~1 s), V3 Adjustment Layer
  with Crop Top 17 / Bottom 16 (the letterbox), V1 Position x 0.578 (face ~50 px right of centre, not centred). → recipe.
- **3 punch-ins** (Scale 157 / 170 / 155) on the insult, a one-word payoff and the closing punchline. → recipe.
- **Captions:** 21/23 lines verbatim; 2 fixes ("logon **ko**", "haan"→"**kaam**"); upright, not italic; no caption
  over the one-word punch-in. → `roman-urdu.md`, `deep-talks-style.md`.
- **Title:** an ironic quote of the target (`“Aap apni khushi se deden”`), Ubuntu Light 48 gold. → recipe.
- **Music:** a song's instrumental under the whole reel, ~6.6 dB under the voice; mix −16.7 LUFS. → recipe.
- **Process:** the mechanical re-ASR said "ko" was inaudible and the creator put it back. **ASR is not the authority on
  short particles (ko/ke/ka/na).** Restore them when the Urdu grammar needs them, and flag them. → `roman-urdu.md`.

## 2026-09-19: first FULL edit (ABW6 · Sequence 18 → dowry-beggars)

- **The creator's trim pass (27.4 → 24.4 s) = the cut should be TIGHTER.** They took 0.1–0.3 s off almost every
  head and tail. Their edges land ON the word (0–35 ms from the sound, one tail 110 ms early), where the house
  polish leaves decay + 70 ms. They also dropped the opening "agar" (the reel now opens on "aap jahez
  maangte hain") and the drawn-out "aur" at the head of "…dusre ki di hui cheez". → one job so far, so it stays a
  lesson. If the next trim repeats it, it becomes a preset number (tail pad ~0, drop a leading connective) → `PLAYBOOK.md` § 0.
- **After a creator trim, rebuild captions from the TIMELINE, never the old EDL:** read V1/A1 source ranges,
  re-map the raw words, re-check each clip's kept audio by slice ASR (it found an "are" the first pass
  missed), and verify every line against its words (an index drift of 1 showed up and was fixed).

- **The creator's pick for their reels is the YELLOW deep-talks style** (they overrode the white choice on
  Sequence 16). → default `--style yellow` for this channel unless told → `PLAYBOOK.md`.
- **Whisper's Urdu mode TRANSLATES English speech into Urdu** ("especially around women etc" came out as
  "khaas taur pe … esi tarah"). The creator mixes ~10 % English into every reel. → every unclear or
  suspiciously formal Urdu line gets an `en` re-decode before captions are written → `PLAYBOOK.md` § 4.
- **The creator wants ≤ 15 min per reel.** The foundation (styles, tooling) cost the first two jobs; the
  full-edit path is now scripted end to end (`PLAYBOOK.md` § 0, `cut_reference.py`).
- **Premiere's scripted import stays broken across restarts** on this machine (see `lanes/premiere/lab-notes.md`
  2026-09-18); replay (no import: the raw is already a project item) works, the caption layer is dragged in by hand.
- **Urdu files on Windows:** `polish-boundaries.py` opened words.json as cp1252 and crashed → fixed to UTF-8.

## 2026-09-18: first real reel (ABW6 · Sequence 16) + the white style

- **The creator edits in PREMIERE, and the project is the source of truth for a style.** Pixel-fitting
  the white font took ~30 min and landed on the wrong family; ABW6's text layers named it (Tahoma 48)
  in one grep. → read the `.prproj` (gzip XML, `AE.ADBE Text` components: InstanceName = the caption,
  the Source Text blob names the font) BEFORE measuring renders → `README.md`, `white-style.md`.
- **The caption height is per reel**, not a constant (y1072 → y1398 across 11 reels); a median
  chin + 115 px predicts it (5 of 11 within 12 px). → `build.py --y`, measured with `chin-line.py` → `white-style.md` § Placement.
- **Deliverable on this lane = a transparent ProRes layer on the top empty video track** of the
  creator's own sequence (native text needs a .mogrt, which the scripting API can't make). → `README.md`.
- **Whisper's Urdu pass drops code-switched English**: "aurton ke baare mai" vanished, "opinions achay lage"
  became garbage. A second pass over just the unclear snippets with `language=en` recovered them. → `PLAYBOOK.md` § 4.
- **A gap in the creator's cut gets no caption** (Sequence 16: 35.7 → 39.2 s is empty): an empty
  `@<sec> |` line ends the previous caption there → `build.py`.
- **With After Effects/Premiere/Topaz open, the 8 GB GPU is full and WhisperX crawls** (20+ min for 41 s);
  `WHISPERX_DEVICE=cpu` did it in ~90 s. → `PLAYBOOK.md` § 2.

## 2026-09-18: preset built from `balcony.mov` (no creator review yet)

- **The italic is FAKE:** the creator's editor slants Ubuntu **Light** about 10°. It is not the true
  Ubuntu Italic font, whose glyphs are wider ("kaha" is 6 px wider). → `FONT_FILE = Ubuntu-Light.ttf`,
  `SHEAR = 0.18`; glyph overlap vs the reference went from 0.42 to 0.81 → `build.py`.
- **Kerning matters at this size:** PIL's basic layout ignores Ubuntu's GPOS kerning (k-a, k-e, l-a).
  → glyphs are placed by hand from fontTools kerning (+0.02 IoU, and fixes visible drift in long lines) → `build.py`.
- **Whisper drops speech in long Urdu chunks:** at the default 30 s window, 10.7 s of a 44 s reel
  vanished (one 29 s VAD chunk, decoding stopped at 18.7 s). → `--lang ur` uses 10 s chunks, and every
  word landed → `transcribe.sh`.
- **Timing rule is "switch on the first word":** the creator's 43 switches sit a median 0.034 s from
  the start of the phrase's first word (p90 0.12 s). → no lead/lag offsets → `build.py`.
- **The creator's Roman Urdu is inconsistent** (`ni`/`nahi`/`nai`, `mujy`/`mujhy`). → majority spelling
  is the default, and the review sheet is where they correct it → `roman-urdu.md`.
- **Whisper Urdu mishears:** teacher→ٹیٹر, bezti→ویسٹی/بیشتی, balcony→بیلگنی, mentally→پینتیلی, and it
  heard "agar" where the creator captioned "magar". → context repair when writing captions.txt, with
  unsure words flagged to the creator → `PLAYBOOK.md` § 4.
