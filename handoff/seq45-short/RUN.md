# seq45-short — ABW8 · Sequence 45 (captions only)

▶ **STATUS: v2 = 2 WORDS PER LAYER (the creator's request, 2026-10-11), waiting on their review.**
Deliverable: `projects/seq45-short/seq45-short.srt` (153 layers: 98 two-word, 35 three-word, 20 one-word; none under 0.2 s;
60 fps grid). `caption_qa.py` PASSES. The 5-word version is kept as `captions.5w.txt` / `seq45-short.5w.srt`.
How the pairs were made: every word timed from the transcript (re-decodes for the repaired spans), then paired BY HAND on
natural units; 3 words only where a verb chain is said too fast to split ("kar rha hun" = 0.18 s) or a negation would
be cut from its verb ("ni ayen ge", "aapko ni lagta").
Next: drag the .srt into ABW8 Sequence 45, apply **"affanwizu yellow"**, baseline **y1208**.

**Flagged for the creator:** 0.0 s "irfan junejo ki najaiz aulad" (name spelling); 9.2 s "isi chaske mai" (every decoder
hears ششکے / शष्के; read as "chaske"); 6.6 s "faltu ka bhaaripan" (heard بھاری پناہ; the English pass says "unnecessary weight").

## The job
- 32 V1 + 32 A1 clips of `X:\Recordings\PBZ\C1344.MP4` (Scale 85, Position x 0.299), 71.017 s, no gaps, 60 fps
  (`sequence_reference.py`, Gate A ✓). Chin y1093 → baseline **y1208**.
- Content: cinematic-reel creators over-produce (drone shots, a camera angle per line, one reel a week); "this video" was
  made in half an hour with Claude; Mr Beast's 3 months vs Andrew Tate's podcast clips; find your winner and do it every day;
  "time is important… on to the next one".

## What the checks caught
- Transcript complete (no gaps with speech, no loop, ending intact).
- **Translated English:** "time is important" (Urdu pass: وقت اہم ہے), "but" (لیکن).
- **Misheard by the Urdu pass, fixed from re-decodes:** 34.7–37 s "usko views milte hain / sahi hai magar / wo bol rha tha
  ke"; 56.2–58 s "aap mujy dekh lo na / mai kyun ni FX / itne karta".
