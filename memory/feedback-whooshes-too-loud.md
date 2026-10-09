---
name: feedback-whooshes-too-loud
description: "Affan found the whoosh SFX too loud on the Onyx samples (2026-10-08): whooshes go 10 dB under the kit level that shipped on Chris Do"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 4f6ff510-e01c-4ae4-a5c4-8388b194173e
  modified: 2026-10-07T23:32:55.063Z
---

Affan, 2026-10-08, after reviewing the Onyx samples: "turn down the whoosh sound effect by 10db its too loud in each of these videos".
Chris Do's whooshes (hook `whoosh-light` at gain +6.8 dB, split `whoosh-air` at +7.0, i.e. 2–6 dB under the voice peak) were
lowered by exactly 10 dB (to −3.2 / −3.0) in `projects/thefutur-nonprofit-15k/yt/build_spec.py` (`WHOOSH_TRIM`).

**Why:** a whoosh is a transition texture, not a graphic's sound; at near-voice level it reads as cheap/loud. This is different
from [[feedback-sfx-on-every-graphic]], which is about pops/ticks/hits on pop-up graphics being audible — that rule still stands.

**How to apply:** default whoosh levels on short-form samples ≈ 10 dB below the Chris Do yt4 level (YouTube look: the `cue()`
gain minus 10 dB; Instagram look: whoosh kinds `title`/`whoosh` 10 dB under the kit's ES table). Keep a whoosh audible in a voice
gap rather than masking a word, but never at voice level. Pops, clicks and hits are NOT whooshes and keep their audible level.
