# RUN — lisa-marie-mj (captions only)

▶ **STATUS: delivered BOTH ways (2026-09-21). Creator to pick one.**

1. **Editable (their preset works):** `outputs/seq22-captions.srt` imported and a **caption track
   created on Sequence 22**. Next: *Upgrade Captions To Graphics* → apply Gretaros / Gretaris Italic
   → drop **Revised Light pop** on all of them → colour the emphasis words from
   `caption-colours.md`. Premiere cannot read caption tracks back by script, so this one is
   unverified from my side.
2. **Rendered (colours baked, no preset):** `outputs/seq22-captions-static.mov` on V3.

**v2 changes:** punctuation stripped to `?` / `!` only · `sex` → **S*X** in pink · LISA MARIE pink ·
DAY TO DAY yellow · SOMEBODY (sleeping with) blue · WAKING UP yellow · KITCHEN pink ·
pop animation rebuilt from a frame-by-frame measurement of the creator's own export.
Live file: `outputs/seq22-captions-v2.mov` on V3 of Sequence 22.

| | |
|---|---|
| Channel / preset | Abundance Wisdom → `presets/youtube-shorts/abundance-wisdom/` |
| Creator's project | Premiere `ABW6.prproj` → **Sequence 22** (36.33 s, 1080×1920, 60 fps) |
| Scope | **Captions only.** The creator owns the cut, overlays, music, CapCut morph and the AE build. |
| Source of the cut | 19 audio clips: MJ & Lisa Marie *Primetime* 1995 (0–21.32 s) + Lisa Marie on *Oprah* 2010 (21.32–36.33 s) |

## What was done

1. **Rebuilt the sequence audio** from the two source files using the timeline's in/out points
   (`raw/seq22.mp4`, 36.332 s — matches the timeline to 1 ms).
2. **Transcribed once** with WhisperX (`WHISPERX_DEVICE=cpu`, because AE/Premiere/Topaz hold the GPU)
   → `transcript/words.json`, 146 words.
3. **Wrote the caption script** by hand from those words → `captions.txt`
   (3 words per caption, 4 where the delivery is fast, never 5; colour tags; `i:` = the interviewer).
4. **Built the plan** → `captions-plan.json` via `make_plan.py`, which checks every caption word
   against the transcript word by word and refuses to run on a mismatch. 49 captions, wall-to-wall.
5. **Rendered the caption layer** → `outputs/seq22-captions.mov` (1080×1920, 60 fps, black background,
   Gretaros, gradients, the "light pop" growth) with `build.py`.
6. **Placed it on V3 of Sequence 22** at 0.00–36.33 via the bridge (scripted import worked this run).
   **The project was NOT saved** — left for the creator.

## Next steps (creator)

- Review wording/colour; edits go in `captions.txt`, then
  `python presets/youtube-shorts/abundance-wisdom/make_plan.py projects/lisa-marie-mj` and
  `build.py render …` re-render in ~2.5 min.
- The .mov is the **black-background master**, same as a Premiere caption export — it can go
  straight to CapCut for the motion-blur pass (no Premiere export needed first).
- In Premiere the clip will cover the picture: set its blend mode to **Screen** to preview over the
  video, or ask for an alpha (ProRes 4444) version.

## Caption script as shipped

49 captions; italic for the interviewer's questions (0–9.56 s), upright for Michael and Lisa Marie.
Emphasis: red = intimate / sex / media / faking / speculated / BS · cyan = Michael, Lisa Marie,
studio, kitchen · magenta = love, together, Loved, care · yellow = 24 hours, career, center, real.
