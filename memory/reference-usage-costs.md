---
name: reference-usage-costs
description: "Measured 2026-10-22: Max 20x weekly cap ≈ $2,150–2,450 of API-priced usage (1 % ≈ $22), Fable cap ≈ $630; per-job cost of every job type as % of a week; the requested 7-stream weekly load is 1.5–4.5x the cap"
metadata:
  node_type: memory
  type: reference
  originSessionId: 6c53394f-576a-44da-bd21-303d5d14e3eb
  modified: 2026-10-22T01:59:53.130Z
---

Measured 2026-10-22 from the session transcripts (~/.claude/projects/*/*.jsonl, usage per message × API prices,
cache write = 2x input for the 1-hour TTL), calibrated against the meter:
- Week of 10-12: the limit hit on 10-14 ~17:00 UTC at ≈ $2,420 cumulative. Week of 10-19: 53 % on 10-21 19:00 UTC at ≈ $1,140.
  → **weekly all-models cap ≈ $2,150–2,450, 1 % ≈ $22.** The week resets Monday 02:00 UTC.
- Fable has its own weekly cap: 44 % at ≈ $278 → it fills at ≈ $630 (one Fable-heavy session on 10-21 spent $222).
- Where the cost goes (since 10-05): cache writes 55 %, cache reads 38 %, output 7 %. **Cost = context size × turns,** not work done.

Per job, % of the weekly cap (lean = fresh session, no subagents; typical = how it actually ran):
- Onyx sample: lean ≈ 1.5–2 % (Scott Clary Shorts, CLIENT-SHORT-RECIPE, ~$35 each) · typical ≈ 8 % (batch 1 in the hub session, ~$175 each).
- Onyx per YES (prospect), measured from the build-agent transcripts: both looks (YT + IG from one shared cut) as batch 2
  ran it, one build agent per prospect ≈ $90–120 (≈ 5 %) plus ≈ $6 research; batch 3 ≈ $190–250 per prospect (9–11 %) and
  stalled. One look in a fresh lean session (Scott Clary recipe) ≈ 1.6 %. Dropping the 2nd look alone saves less than half
  (the pick, cut, transcript and captions are shared); one look AND a lean fresh session cut it to about a third.
- Onyx reaction (≤ 3:00, prepared in Premiere): ≈ 0.8 % lean ($89 for 5, 10-19, one session) · ≈ 2–3 % the batch-2 way
  (separate rough-cut + graphics agents, $40–65 each).
- Week with one look per yes, everything lean: other streams ≈ 79 %, so about 1 yes a day fits (≈ 2.4 % per yes incl. the
  reaction); 4 yeses a day ≈ 146 % (asked 2026-10-22).
- ABW short: ≈ 1 % as an assist pass on his Premiere/AE edit (captions, transitions, head-track) · ≈ 4–6 % built fully in code (Katherine).
- AW long-form: 15–30 % (cbum-last-show ≥ $620 across 3 sessions, with a rejected version).
- GTA long-form: ≈ 5 % (plain) to 13 % (video 22, IGN style, $286 in one day).
- AffanWiz English video: ≈ 2 % (rough cut) to 13 % (full IGN-style build).
- Onyx outreach + logs: ≈ 1 % a day. Urdu captions: ≈ 0.5 % per job.
- Anti-patterns measured: the Onyx hub session (one session, 10-02 → 10-21) cost ≈ $3,580 = 1.5 weekly caps; the 10-14
  six-agent swarm ≈ $1,370 in one day with 1 of 12 samples shipped.

Affan asked 2026-10-22 whether this fits one week: 2 AW long-forms, 28 Onyx samples + 28 reactions, 14 ABW shorts,
3 English, 3 GTA, daily outreach, daily captions for 2 Urdu brands. Answer: no — ≈ 1.4x the cap at the leanest measured
costs, 3–4.5x at typical costs; the 28 samples alone are 0.4–2.2 caps. Related: [[feedback-usage-budget]],
[[feedback-use-fable-allowance]], [[project-onyx-sample-shorts]].

The weekly schedule built from these numbers: projects/_weekly-plan/SCHEDULE.md (2026-10-22, draft for his OK).
