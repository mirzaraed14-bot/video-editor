---
name: project-urdu-instagram-captions
description: "@affanwizu Urdu reels (Premiere, ABW6): goal is FULL autonomy, raw take in → finished reel out. Recipe measured off the shipped reel in presets/instagram/affanwizu/reel-recipe.md; yellow Ubuntu Light captions as an editable .srt"
metadata: 
  node_type: memory
  type: project
  originSessionId: 123ecc4f-c34e-484c-84b1-6417b858da1c
  modified: 2026-09-18T08:38:24.668Z
---

Started 2026-09-18. The user's Urdu talking-head reel page **@affanwizu** (Affan Baig, ~36.4k followers, shot in front of a "skool" neon sign). It started as **captions only** (Roman Urdu); since 2026-09-19 the scope is the whole edit (see GOAL below).

**Why:** caption-making is the repetitive part; choosing which bits to use is their creative edge.

**How to apply:** never cut, reorder, trim or reframe their reel. Everything lives in `presets/instagram/affanwizu/` (README → deep-talks-style.md, roman-urdu.md, PLAYBOOK.md, LESSONS.md, build.py), and CLAUDE.md's learning loop points there. Read PLAYBOOK.md before any reel.

State at 2026-09-18:
- **"Aesthetic deep talks" style is LOCKED**, measured off `E:\Shorts\Abudance Wisdom Shorts Exports\Final Renders\balcony.mov`: Ubuntu **Light** with a faux-italic 0.18 slant, 48 px, #FFD700, black shadow 3.75/4.25 px with 1 px blur, baseline y1178, lowercase, one line, holds until the next line. Glyph overlap is 0.81 against their frames; switch timing is a median 0.034 s from theirs. The proof image was shown to the user.
- **White style:** measured 2026-09-18 (Tahoma 48) → `white-style.md`. The creator prefers yellow for their reels.
- `transcribe.sh` now takes `--lang ur` (10 s chunks; the 30 s default dropped 10.7 s of Urdu speech). English is unchanged.
- The Roman Urdu text is written by Claude from `captions.draft.txt` into `captions.txt`, then goes to the user for spelling review before rendering.
- (2026-09-18 open questions are all settled: editable .srt captions, not a burn/layer; we propose the title; the white style is measured.)

**The creator edits these reels in PREMIERE PRO, not CapCut** (they said so, 2026-09-18). Their caption layers are Essential Graphics text, so the fastest source of truth for any style is the project itself: e.g. `oushi.mov` came from project **ABW6**, whose auto-saves live under `E:\Premiere Pro Exports\Adobe Premiere Pro Auto-Save\...` (gzip XML; the text layers' InstanceName = the caption, and the Source Text base64 blob names the font). Read that, or ask for an Essential Graphics screenshot, before pixel-measuring a render. From ABW6: white style = **Tahoma 48**; yellow = **Ubuntu-Light 48** (confirms the lock). White style now measured → `white-style.md`, `build.py --style white --y <baseline>`.
**First real test 2026-09-18:** ABW6 · Sequence 16 (Andrew Tate opinions), white style, alpha layer placed on V3; job `projects/seq16-urdu-reel/RUN.md` holds the resume block + 5 spelling flags awaiting the creator's review.

**GOAL (the user, 2026-09-19): full autonomy.** They want to hand over a raw file and get the finished reel with nothing touched by hand. Scope is no longer captions-only: the cut, frame stack, punch-ins, captions, title proposal and music placement are all ours. Every shipped reel gets a learning pass. The first shipped full edit was `ameer.mov` (ABW6 · Sequence 18, job `projects/dowry-beggars`); its measured recipe lives in `presets/instagram/affanwizu/reel-recipe.md`. Still manual: the song choice (theirs) and bringing captions in (scripted import broken → .srt drag).

Raw footage: `E:\Skool Recordings\<batch>\`, where Urdu reel takes are mixed with English GTA takes (C1253 = Urdu; C1269/C1263/C1287 = English). Forcing Urdu on English audio produces garbage.
Related: [[user-abundance-wisdom-editor]], [[feedback-long-term-self-improving]].
