---
name: feedback-scott-ig-minimal-format
description: "Scott's own value talk on IG: never INVENT a look (the 11-14 invented one was 'horrendous'); a code-built COPY of a real reel he picked is OK: DOAC Katt Williams reel (DfnZX5ITrrx) = black canvas, rounded square window, EB Garamond 1-3 word captions, white/gold, SUCCESS STORY tag"
metadata:
  node_type: memory
  type: feedback
  originSessionId: add63d7d-24db-42f2-9307-dfe9e5325e88
  modified: 2026-11-15T01:50:00.000Z
---

Affan, 2026-11-14 (Scott D. Clary channel):
- **YouTube Shorts** go up on Instagram in the SAME YouTube format. There is no separate IG variant; the PBD urine-prank Short was the first.
- **Scott's own talk on Instagram** is a strand for his personal stories, motivation, and business or value advice, in a super-minimal look. His original description:
  - black bars and the footage, no zooms;
  - one clean caption font fading up;
  - ONE big handwritten calligraphy word under the 3-word line.

**2026-11-14 verdict on the first code-built attempt** ("How's your Tuesday looking?", job `hows-your-tuesday`; Claude wrote the look numbers into the BRIEF and a Sonnet session built them): **"horrendous ... this was a very bad job"**. His new split of the work:
- **Affan edits the look himself in Premiere.** For each post, Claude puts the RAW cut into his Premiere: the approved spans as separate trimmable clips, CUTS ONLY. No captions, script words, graphics, reframe, grade or audio processing.
- **Claude's job is to FIND minimalistic styles on Instagram that we can copy:** real Reels and accounts, with numbers, and what exactly makes each look work.

**Why:** a look invented from a written description (fonts, sizes and fades chosen by Claude) came out badly. The minimal look only works when copied from real proven examples, and finished by his own hand.

**How to apply:**
- **Never INVENT a look for this strand** (fonts, sizes and fades chosen from a description). **A code-built COPY of a real reel he picked is allowed** (his later word, below): measure the reel frame by frame, build from those numbers, show test stills against the reference BEFORE any full render. When he wants to edit it himself instead, hand over the raw cuts-only sequence (an importable XML exists for Tuesday).
- Still follow sequencing → his OK → build ([[feedback-sequencing-before-edit]]), the Premiere quiet rules ([[feedback-dont-disturb-his-premiere]]) and [[feedback-affan-exports-himself]].
- This is NOT the neon-window IG look ([[feedback-instagram-neon-window]]).
- Research lives in `projects/_client-scott-clary/research/ig-scott-value/`. Related: [[project-scott-clary-shorts-guarantee]], [[feedback-max-effort-every-asset]].

**Affan's chosen inspo (2026-11-14):** the DOAC Reel https://www.instagram.com/reel/DfnZX5ITrrx/ (Katt Williams, "this reel is good inspo").
- **The look:** a black field with big bars; the footage in a centred, near-square ROUNDED window; ONE gold serif word at a time, low in the picture; B-roll inside the same window; a tiny brand tag.
- **Where it lives:** `research/ig-scott-value/style-search/STYLE-REFERENCES.md` and `COPY-SHEET-DfnZX5ITrrx.md`.
- **Not liked:** Dan Koe's faceless text style and Scott's own looks were offered and not picked.
- **Later the same day:** he said "copy this style and make the tuesday video in this style", so a code-built COPY of a real, measured reel is allowed again (an invented look is not). To the build session he added **"put the podcast's watermark as well like DOAC"**: the tag stays ON, with the podcast's name ("SUCCESS STORY") in DOAC's tag form (sharp white ~65 % box, bold black caps, bottom-left inside the window, left x98 / bottom y1423). Step-1 test stills and the measured numbers: `projects/_client-scott-clary/hows-your-tuesday/test-doac/` and that job's BRIEF.md.
- **He approved the Step 1 stills ("our looks good") and added: do not write the title card's words twice** ("hows your tuesday looking don't write it twice"): no caption while Scott's own title card is up. The DOAC-style 30 fps check was then built and delivered (`X:\Claude Projects\Exports\scottclary-ig-hows-your-tuesday.doac.check30.mp4`, -14.0 LUFS, 58 chunks, EB Garamond 450 / 73 px / -5 %, tag "SUCCESS STORY" on every frame). This supersedes "Never code-build" above for the strand: a code-built COPY of his chosen reel is what he asked for.
- **2026-11-15: he chose "Add shadow"** (the answer to "Keep the defaults: EB Garamond, no caption shadow, one-line tag?"). The soft caption shadow (opacity 0.75: the caption drawn 3 px lower, blur 9, black under the text, `doac_frames.shadow_alpha`) was chosen for the Tuesday check only: delivered, awaiting his review IN MOTION (he picked it from stills; the halo cuts on and off per chunk). Not a standing rule for the strand yet. The font and the one-line tag "SUCCESS STORY" stay. Delivered beside the plain check, which he may prefer once he sees motion: `X:\Claude Projects\Exports\scottclary-ig-hows-your-tuesday.doac.check30.shadow.mp4` (audio bit-identical to the plain one). Rebuild: `python work/doac_build.py --shadow 0.75` in the job folder.
