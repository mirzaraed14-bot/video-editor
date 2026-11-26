---
name: feedback-av-sync-gate
description: "Lips, speech and captions must be in sync: the AW hub gate cross-correlates each third-party clip's audio against its source and checks every caption against the aligned word in the FINAL mix (Travis v7, 2026-11-25)"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 0ac70c57-b1cb-4865-b958-7d9d45bd812d
  modified: 2026-11-24T22:27:10.780Z
---

Affan's main complaint on Travis A2 v7 (Tella review, 2026-11-25, said 5 times) was "the lips, the actual speech and the
captions are not synced". Two causes were measured:
- ffmpeg input-seek (`-ss` before `-i`) on two stream files landed their audio 0.3-0.7 s late;
- captions timed from medium.en ASR plus the CapCut model's 6-frame lateness ran 0.6-1.0 s late.

The hub had passed v7 without any sync check.

**Why:** a reaction Short lives on the streamer's face saying the line. Audio or captions late by even a few tenths read as
broken, and he notices before anything else.

**How to apply:**
- **Builds:** cut every third-party clip's audio from a full decode (output-seek), never from input-seek. Time captions
  from wav2vec2-aligned word starts of the FINAL mix, minus the kit's 6-frame CapCut lateness.
- **The hub, every version:**
  - cross-correlate each clip's audio in the final against its source decoded from the claimed in-point (it must be
    within 1 frame);
  - require a caption sync table and fail any gap over 0.1 s, then re-measure the 3 worst captions itself;
  - word starts are measured twice, by wav2vec2 alignment and by the 10 ms energy rise in the voice stem. wav2vec2 alone
    is not ground truth: on Kai's "oh" it was 1.1 s late against the open mouth. A disagreement over 0.1 s is flagged and
    checked against the mouth by eye.
- The gate lives at the top of `presets/youtube-shorts/abundance-wisdom/HUB.md` (HUB DELIVERY GATE).

Related: [[feedback-fix-only-what-he-named]] (the whole Short gets the gate every version),
[[feedback-captions-just-below-lips]], [[feedback-cover-phone-reading]] (prove lip sync).
