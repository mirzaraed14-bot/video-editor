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

- **2026-11-02, said again (Onyx batch 6, after 23 % of the week went on day one):** "use Opus where is needed… you don't have to use
  opus for everything… otherwise use sonnet". The batch-6 builders all ran on Opus, which was the mistake. **Builders default to SONNET**
  (cutting, kit scripts, renders, placing, QA against the brief); Opus only for the judgment pieces: the sequencing/teardown of a sample,
  creative calls a reviewer can't settle, adjudicating conflicting evidence. Where a Sonnet builder is unsure, it hands the question
  back to main, and main uses the **advisor** rather than spawning an Opus agent.
