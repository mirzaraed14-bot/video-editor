# seq22-short — ABW8 · Sequence 22 (captions only)

▶ **STATUS: DONE — caption track delivered 2026-10-01, waiting on the creator's review.**
Deliverable: `projects/seq22-short/seq22-short.srt` (183 cues, 0 → 173.317 s). `caption_qa.py` PASSES.
Next: drag the .srt into Sequence 22, apply **"affanwizu yellow"**, baseline **y1121**. After the creator corrects
any layers → learning pass into `presets/instagram/affanwizu/LESSONS.md`.

**Flagged for the creator:**
- 9.5 s **"ahmar azam" / "the CEO of trifit"**: spelling of the name and the company is a guess from the audio.
- 77.8 s **"on meta ads"**: could be "on my ads" (both listeners split). Meta fits the Ads Library context.
- 171.7 s **"or apne [?] ke pese / zaya na karen"**: one word every decode hears as "meshwar"/"make sure".
  Left OUT of the caption (shows "or apne pese"); add it if you want it.

## The job
- Source: Premiere project **ABW8**, **Sequence 22**, read through the CEP bridge. 58 V1 clips of
  `X:\Recordings\PBZ\C1318.MP4` (1920×1080 at Scale 100, Position 0.5/0.5 → the 1080-wide centre band at y420–1500)
  + 58 A1 clips from a SEPARATE audio recording `E:\Shorts\...\Batch Batch\2026-10-01 16-53-36.mp4`.
- Sequence end 173.317 s, no timeline gaps. Rebuild `raw/seq22-short-cut.mp4` = 173.334 s (Gate A ✓).
- Content: Pakistani social-media agencies are mostly scams; how to vet one (proof, Meta Ads Library, spend
  flexing in the bio), the creator's own numbers as proof, hire out of need not out of want.

## Pipeline (per PLAYBOOK.md, first job on the 2026-10-01 gates)
| Step | Result |
|---|---|
| Transcript | WhisperX large-v3 CPU `--lang ur`, 739 words, no pause > 1.5 s (Gate B ✓), no long words |
| English listener | `codeswitch_pass.py` → `transcript/codeswitch.json`; recovered **"not out of want"** (138.1 s), which the Urdu pass dropped |
| Re-decodes | 5 spans (name, spam, follower numbers, "out of need", the ending), ur + en + hi |
| Baseline | chin median y1006 → **y1121** |
| Lines | 183, max 5 words, creator spelling (aapko/unhone/inki/or/kia/lye/chahye, digits), quotes on quoted speech |
| QA | `caption_qa.py` PASS: 0 FAIL; warnings reviewed (ایسا at 146 s is a real "esa"; "so much → so many" is a self-correction, final kept) |
