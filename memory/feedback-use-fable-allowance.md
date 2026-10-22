---
name: feedback-use-fable-allowance
description: "Affan 2026-10-21: NO Fable agents; agents run on Opus only when the task needs it, Sonnet/Haiku otherwise; check with the advisor which model a task needs"
metadata:
  type: feedback
---

**Rule (Affan, 2026-10-21, MJ siblings short):** "don't use agents of fable, use opus only, and use advisor as well to see if a
task actually requires opus, don't just use opus for everything" + "you can use agents but of opus and other models".
This REPLACES the 2026-10-14 note that said to delegate to Fable's separate weekly pool.

**Why:** his call on the usage pools (the Fable pool is no longer to be spent on agents).

**How to apply:** before launching any subagent, ask the advisor (or decide explicitly) which model the task needs and pass
`model` explicitly: `opus` only for judgment-heavy work (creative choices, adjudicating evidence), `sonnet` for mechanical
work against stated criteria (running a template's scripts, scanning sheets against rules), `haiku` for pure command runs.
Small leftovers stay in the main session (an agent's startup can cost more than the work). Gate agent output at judgment
points (e.g. captions: the agent writes captions.txt + the mishear table, the main session reviews, then renders).
Related: [[feedback-usage-budget]].
