---
name: feedback-usage-budget
description: Affan 2026-10-15: six parallel build agents burned ~50 % of his Max 20x weekly plan in 3 hours and hit the limit; he's on paid usage credits he can't afford to exceed — budget every job, no agent swarms, fresh small sessions
metadata:
  type: feedback
---

2026-10-14 evening: six long-running build agents ran in parallel (3 resumed Opus agents carrying 500-600K tokens of history + 3 new
Fable agents that each loaded ~15 documents first), every tool step re-sending its whole context, plus image-heavy QA and a days-long
main session. ~50 % of the Max 20x weekly plan went in ~3 hours; all six were cut off by the weekly limit with only 1 of 12 samples final.
Affan, 2026-10-15: "I have bought usage credits but I cannot afford any more… we need to make sure we don't exceed our usage credits…
I'd rather wait… I really don't want to compromise on quality."

**Why:** usage is his money; a stalled swarm wastes it twice (spent + nothing shipped).

**How to apply:** estimate the cost of a job before starting and get his OK; one sample/task at a time, never several heavy agents in
parallel; cheap models (Sonnet/Haiku) for mechanical steps, Opus/Fable only for judgment; lean briefs (no 15-document preambles);
few image reads; start a FRESH session with a short resume file instead of continuing a days-long one; stop and report if a job runs over.
On credits (until a reset) pause rather than cut quality. Related: [[feedback-use-fable-allowance]], [[project-onyx-sample-shorts]].

- 2026-10-15 (Scott Clary FUBU Short): Affan capped ONE video at $10 of usage credits. Per-video cap: plan the build in few, batched turns; avoid full-size image reads and doc re-reads.
