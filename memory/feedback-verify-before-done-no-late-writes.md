---
name: feedback-verify-before-done-no-late-writes
description: Check delivered files BEFORE saying done (he exports within minutes); after a ready hand-off, no writes to his sequence without his go
metadata:
  type: feedback
---
Affan acts on a "done" message within minutes: on GTA 29 (20 Nov 2026) the first dialogue pass was reported done at 02:30
before the delivered clips were checked; by 02:41 he had fixed levels himself and started his export, and our corrected pass
(02:48) raced the export and never reached the upload. The posted video kept the first pass's faults (a streamer's own shout,
a clipped word). He called it "you still made some mistakes which I cleaned up".

**Why:** a "done" that is followed by fixes wastes his clean-up and can ship the faults; a late write can also stack on his own
hand fixes (Audio Gain is invisible to our readback).

**How to apply:** run the delivered-file checks (unprompted transcription vs the expected words, loudness vs his VO, the
streamer's voice absent) BEFORE the done message. After a ready hand-off, tell him what changed and get his go before any
further write to his sequence; read his Audio Gain from the autosave XML first. Related: [[feedback-gta-dialogue-real-audio]],
[[feedback-dont-disturb-his-premiere]], [[feedback-creators-hand-is-not-a-bug]].
