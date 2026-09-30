# seq17-short — ABW8 · Sequence 17 (captions only)

▶ **STATUS: DONE — caption track delivered, waiting on the creator's review.**
Deliverable: `projects/seq17-short/seq17-short.srt` (169 cues, 0 → 180.20 s, track length 184.917 s).
Next: drag the .srt into ABW8 Sequence 17, apply the saved **"affanwizu yellow"** Track Style,
set the caption baseline to **y1137**. After the creator corrects any layers → learning pass into
`presets/instagram/affanwizu/LESSONS.md`.

## The job
- **Channel preset:** `presets/instagram/affanwizu/` (Roman Urdu captions ONLY; the creator owns the cut).
- **Source:** Premiere project **ABW8**, **Sequence 17** — read through the CEP bridge, not exported.
  74 V1 clips + 74 A1 clips, picture `X:\Recordings\PBZ\C1316.MP4` (3840×2160) at Scale 36,
  Position 0.525/0.5, no crops, V1 only. Music on A-track: `SL-esv2-2p-bg-10p-music-10p.mp3`.
- **Sequence end:** 184.917 s. **One timeline gap:** 175.433 → 178.700 (3.267 s).
- **Content:** brand-audit reel — SL Aesthetics Clinic (owner Shaista Lodhi), follower count vs views,
  influencer spend vs the founder as the marketing asset, organic-ness, script formation, views ≠ clients.

## What was produced
| Step | Output |
|---|---|
| Rebuild | `raw/seq17-cut.mp4` — 184.934 s, gaps preserved (black + silence), framing matched to the sequence |
| EDL | `transcript/cuts.json` — the 74 segments + the gap |
| Transcript | `transcript/words.json` — 634 words, WhisperX large-v3 CPU `--lang ur`, **+3 spans re-decoded and spliced** (backup: `words.json.prealign.bak`) |
| Baseline | `uv run workflows/chin-line.py` → median chin y1022 → caption baseline **y1137** |
| Lines | `captions.txt` — 169 lines, max 5 words each, word-index keyed, every line verified against its words |
| Delivery | `seq17-short.srt` — editable caption track, `--style yellow --y 1137 --dur 184.917` |

## Traps hit on this job (now gates in PLAYBOOK.md § 2)
1. **The first rebuild was 181.65 s, not 184.92** — a concat closed the 3.27 s timeline gap, which would
   have pulled every caption after 175 s early. Rebuilt with the gap inserted.
2. **WhisperX silently dropped 11 s of speech** in two spans that looked like pauses (8.5→15.0 and
   48.9→53.2). Both measured −27 dB, the same as normal speech; real silence measures −55 dB.
   Re-decoded wide and spliced back — they held the reel's core statistic and its pivot.
3. Language auto-detect said `hi` (p≈0.69) as always on this channel — `--lang ur` was forced.

## Constraints honoured
- Nothing in the creator's Premiere project was changed; the project was never saved by us.
- Captions ship as an **editable .srt**, never a rendered .mov.
