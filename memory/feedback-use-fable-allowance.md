---
name: feedback-use-fable-allowance
description: "Affan 2026-10-21: NO Fable agents; agents run on Opus only when the task needs it, Sonnet/Haiku otherwise; check with the advisor which model a task needs. 2026-11-10: Fable 5.2 IS the advisor and that's wanted; hubs stay Opus, edit sub-sessions default to Sonnet once the BRIEF locks the creative calls"
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
- **2026-11-10: Fable 5.2 is the advisor now, and that's wanted.** Affan: "I really want to use fable 5.2 as advisor for basically
  everything." `advisorModel` in ~/.claude/settings.json is `fable` (it was `opus` until 11-10, so all advice before that date came
  from Opus). Keep calling the advisor as usual; the NO-Fable rule above is about agents, not the advisor. A session that existed
  before 11-10 keeps its Opus advisor until he runs `/advisor fable` and then `/compact`. Fable usage also counts toward the
  all-models weekly limit (Anthropic help article; the Fable meter is only a cap on the Fable share), so the no-Fable-agents rule
  still matters. Related: [[feedback-usage-budget]].
- **2026-11-10: the roles (Affan).** "Fable is the head, opus is gonna be used where it's needed according to Fable, sonnet …
  according to Fable as well." Fable = the advisor in every session, consulted at each decision point, including which model a job
  needs. Opus = judgment, where the advisor says it's needed. Sonnet = the head of execution. In practice:
  - The main hub sessions (one per channel) stay on Opus: they talk with Affan, make the creative calls (sequencing, picks) and
    write the BRIEF.
  - A sub-session started for an edit gets its `model` passed explicitly. **Sonnet by default** once the creative calls are locked
    in its BRIEF (sequencing OK'd); Opus only when the job itself still needs creative judgment (a new format, picks, sequencing not
    yet approved). Ask the advisor before starting it, and name the model and the reason in the hand-off.
  - Agents inside any session follow the rules above: Sonnet builders, Haiku for pure command runs, Opus only for judgment.
  - **Reviewers never go below Sonnet** (Affan 2026-11-10, "keep Sonnet"): a Sonnet edit session's rough-cut second pass and
    edit-review reviewers/skeptics stay on Sonnet, not Haiku. Written into CLAUDE.md step 2 and edit-review § Token efficiency.
  - Found 11-10: most edit sub-sessions had been started on Opus (AW Shorts, English, Onyx samples); only the Scott Clary hub was
    starting Sonnet ones.
