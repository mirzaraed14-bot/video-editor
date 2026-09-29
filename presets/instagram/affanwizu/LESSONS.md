# @affanwizu: lessons

Format: *lesson → change made → file*. Newest first. A lesson that repeats becomes a rule in
`deep-talks-style.md` / `roman-urdu.md` / `PLAYBOOK.md`.

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
