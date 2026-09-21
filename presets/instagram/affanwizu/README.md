# @affanwizu: Urdu talking-head reels (captions only)

Affan Baig's Urdu Instagram page (~36.4k followers, 2026-09-18): talking-head reels shot in front of
the "skool" neon sign. **Scope is captions and nothing else.** The creator picks, orders and trims the
clips, builds the frame, writes the title, and hands over a finished cut. We add Roman Urdu captions
(Urdu written in English letters) that look exactly like theirs.

> **Why so narrow:** the creator grew this page by hand and keeps creative control of the selection.
> Never cut, reorder, trim, reframe or re-grade their reel, and don't add music or SFX. Captions are the whole job.

## The two styles

| Style | Status | Look |
|---|---|---|
| **Aesthetic deep talks** | 🔒 LOCKED, measured off `balcony.mov` | [`deep-talks-style.md`](deep-talks-style.md): black 9:16 canvas, footage in a 1080×1300 window, yellow Ubuntu Light faux-italic, lowercase, one line |
| **White** (second style) | ✅ measured 2026-09-18 (font read from the creator's Premiere project ABW6) | [`white-style.md`](white-style.md): Tahoma 48, white, soft black shadow, mixed case with ALL-CAPS emphasis lines, `?` kept. `build.py --style white` |

**Both styles:** the creator edits in **Premiere Pro**. Captions ship as an **editable caption track**
(`build.py --srt`, dragged onto the sequence; styled by the saved Track Style), so the creator fixes spellings
themselves: see `deep-talks-style.md` § Premiere caption track. `--alpha` (a rendered layer) is the fallback.
The baseline is per reel (`--y`; chin + ~115 px). **Default style for this channel: yellow.**

## Files

- [`reel-recipe.md`](reel-recipe.md): **the whole finished reel** (frame stack, punch-ins, title, music, export), read off the creator's own shipped reel
- [`deep-talks-style.md`](deep-talks-style.md): the locked look, timing and phrasing (WHAT)
- [`roman-urdu.md`](roman-urdu.md): the creator's spelling, learned from their own captions
- [`PLAYBOOK.md`](PLAYBOOK.md): the per-reel procedure (HOW)
- [`LESSONS.md`](LESSONS.md): what each job taught
- [`build.py`](build.py): `--prep` drafts the phrasing, then a burn or a transparent layer

Reference export: `E:\Shorts\Abudance Wisdom Shorts Exports\Final Renders\balcony.mov` (1080×1920,
60 fps, 44 s, 43 caption lines). Raw takes live in `E:\Skool Recordings\<batch>\`, mixed with English
GTA takes, so check which language a clip is in before transcribing.
