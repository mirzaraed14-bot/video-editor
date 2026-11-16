---
name: reference-doac-kit
description: "Scott's own-talk Reels in the DOAC look are built by projects/_client-scott-clary/_doac-kit (one command per stage, 30 fps check + 60 fps Chronos final); proven byte-identical on the Tuesday job"
metadata:
  node_type: memory
  type: reference
  originSessionId: a2e01e38-3d39-4672-82d2-fa1b6fa3dd35
  modified: 2026-11-15T23:50:49.559Z
---

`projects/_client-scott-clary/_doac-kit/` (README.md there) is the Tuesday DOAC-look pipeline as a reusable kit:
`new_job.py <name> --spans spans.json --hls <master url>` then `run_job.py --job <dir> all`.
Stages: fetch (Scott's own flightcast HLS, stream copy) → audio → asr (WhisperX GPU under lock.sh gpu) → spec (spans snapped to the words, auto-chunked captions, card detection) → shots (head lock) → vaudio (−14 LUFS static chain) → build30 (shadow ON) → qa30 → plain30/qashadow → proof30 → plate → chronos (Topaz 2x per take) → build60 → qa60 → deliver (X:\Claude Projects\Exports).

**Proof:** run on the Tuesday inputs (`_doac-selftest`) it reproduces the delivered `doac.check30.shadow.mp4` byte for byte, plus the audio, QA and timing logs identically (2026-11-16).
**Why it exists:** Affan's overnight brief 2026-11-16 (a second Scott own-talk Reel with nobody to ask) — see [[feedback-scott-ig-minimal-format]]. The look and the shadow are his picks, not a standing rule for other strands.
**How to apply:** use the kit for any new Scott own-talk Reel; a decision it makes alone is logged at the top of the job's RUN.md.
