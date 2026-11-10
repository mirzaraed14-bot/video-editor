# Abundance Wisdom: the hub session

The hub is the one main session that runs Affan's AW Shorts. It starts the build sessions, relays their reports to him,
checks every delivery, and saves his rules. Build how-to lives elsewhere: start a build at [SESSION-START.md](SESSION-START.md),
the look in [README.md](README.md), lessons in [LESSONS.md](LESSONS.md). Ideas and locked briefs come from the Cowork engine
files in `X:\Claude Projects\Abundance Wisdom\` (ENGINE, RESULTS, the newest HANDOFF), or from the Instagram method
(`research/instagram-beat-mining/`).

## ▶ STATUS: resume here (2026-11-10, written before a /compact)

**Nothing is running from the hub.** Every linked session was idle at the last status. Weekly usage: 76 % on 7 Nov, reset
Monday ~02:00 UTC (07:00 Pakistan time). The advisor is Fable 5.2 since 10 Nov (his `/advisor fable`, live after the compact).

**10 Nov strategy research (after Bieber and Son flopped):** `research/aw-strategy-2026-11-10.md`.
- Nothing broke: the 18-29 Oct MJ death-lane run was a hot streak, and it ended. Every other Short since early October (MJ or
  not) opened at 3-80K on day one, September's band, with viewers holding (stayed 68-78%).
- YouTube's 1 Oct "original content" Shorts change is a live risk (clip peers fell, narrated ones grew). Our feed columns show
  no sign of it: misses aged 5-13 days still get 79-94% of views from the Shorts feed.
- Make first: the oxygen chamber as a CLIP (OXYGEN-CHAMBER-CUT.md; card vs reusing Burnt Hair's line to settle). Narration is
  his opt-in experiment. Second: the Whitney/Bobbi clip (locked brief, grief lane).
- No verified birthday-shape story on another celebrity found yet.
- Waiting on him: clip or narrated for the chamber.

**Waiting on Affan:**
| Job | Session | What it needs from him |
|---|---|---|
| Jermaine Jealous (MJ's brother mocked his skin) | `local_0729b59b-cdba-451e-a976-e7b98a4410f4` | his direction on the 47.15 s raw cut in ABW10 (title + one word "out"/"up front" were also open) |
| Why MJ Gave Away 5 Million (Victory Tour) | `local_59aa922f-cf80-4fde-9047-81d1b48d98f8` | his creative direction on the 35.53 s sequence in ABW10 |
| Why Justin Bieber Walked Off His Own Stage | `local_12157f61-18f2-4fa8-a97b-dac32e70ace2` | the title pick; he already exported "Justin Final YT" |
| La Toya Betrayed | `local_d3f748df-e06e-4089-9b46-7c54053bd766` | his verdict on the Bolt Motivation look (decides the look for the rest) |
| Instagram method | `local_fd5de818-0d1c-43c9-98f2-673ea76852df` | view numbers once each Short's curve is flat (RESULTS-TRACKER.md); the method is unproven on YouTube until 4-6 flat rows |

**Finished on his side (his own "Final YT" export exists):** Harry Diana, Owen Hart Wife, La Toya Betrayed, Ronaldo Retires,
Bieber, Son Step Outside ("Jafaar"), and very likely What MJ Showed His Mother ("Burn"). Their sessions:
Harry `local_1836bd12-b423-40a8-9d24-caa48e312e5b` · Owen `local_dab7588d-f5fb-4c94-83f5-0b85a02aa394` ·
Ronaldo `local_40fe9e55-20a9-4f3c-937e-e429cb4a9ba9` · Mother `local_6dae492a-d521-4d43-9ca6-b6a0d7e2d839` ·
Son `local_60e694a4-3f6d-4d05-bd46-451642f9f0b7`.

**Older asks, NOT re-checked since 5 Nov** (read that job's RUN.md before acting; they may be done or dropped): Conrad's full
Topaz pass (`local_a9997639-1d78-42d0-b4d6-5d8f1a97c07e`); labels to the bottom on Patrick (`local_5e58eaf8-5db4-4d8d-87e4-c8a621b17b23`)
and Kane (`local_b76e56a5-15a2-4a68-a211-2effd951afca`); a dark backing behind Matt's label on MJ Outthink
(`local_9ba083d7-8d14-47e2-934a-d8599e2072dc`); reviews of Paris Shock Therapy (`local_028af0ae-f7b7-414b-9540-09cc14ff9bc1`)
and Katherine (`local_da5a006a-36b0-4117-aa32-ff0ceadb2381`). A third end-screen concept only if he asks.

The per-Short history is in memory `project-abundance-shorts-automation`; each job's own state is its `projects/<job>/RUN.md`.

## How the hub works
- **A pasted locked brief = a new Short = its own session.** Offer it with a title alone; he has picked "New session" every
  time. Then send the brief verbatim plus the standing-rule conflicts. If he asks in words for a subsession, start it directly.
  Over Remote Control the offer card can't be shown, so ask in text or start it when he has asked.
- **Workstreams are linked subsessions of the hub** (his ask, 2026-11-07: "everything is in one main session"). The daily
  Instagram idea work runs on Code, not Cowork ([memory: project-instagram-beat-mining]).
- **Relay in one or two plain lines with the session link**: what happened, what is checked and what isn't, what he must do.
  He dictates by voice and is often on his phone.
- **A child's note is a report, not proof.** Check every delivery yourself before calling it done: `ffprobe` (1080x1920,
  fps, duration) and `cmp` the `X:\Claude Projects\Exports` copy against Final Renders.
- **Find deliveries by title.** The newest files in Final Renders are often his own Premiere exports (`Chop.mov`, `Push.mov`,
  `box37.mov`, `prince1.mov`: pcm_s16le plus a timecode stream), not ours. Ours are named after the title, with earlier
  versions kept as `(vN).mov`. His `<word> Final YT.mov` means he exported his final.
- **Notes arrive cut at 400 characters.** For detail, read the job's `RUN.md` STATUS block; `list_events` often returns
  almost nothing.
- **Phone copy, only when he asks** (he's outside and wants to review): two-pass libx264 3700k, maxrate 6000k, AAC 128k,
  `+faststart` gave 24 MiB for a 54 s Short. Write `<title> (phone).mp4` to the job's `outputs/`, check the size and loudness,
  send it with SendUserFile, and delete it once he has reviewed.
- **Before a new workstream, read usage** (`get_usage`) and say the cost. Lean mode: no new agents without his OK.
- **Quote his words when forwarding an approval** ("Yes to all") to a session, and say what it does not cover.

## Rules the hub enforces (owners in memory)
Subscribe CTA on every AW Short, end screen OFF (README § 12) · no minors on frame · source audio only, no music on code builds ·
censor drug/self-harm words (ask per Short) · labels low, captions just under the lips · never save or export his Premiere
projects · work in silence · no C: exports, copies to `X:\Claude Projects\Exports` · YouTube: one plain request when he says
"download them yourself", never a bypass · no Fable agents · never kill another session's processes · the shared Premiere lock.
