---
name: feedback-shutdown-after-overnight-job
description: Affan 2026-10-13: when he hands over an overnight Premiere job and goes to bed, finish it, save the project, quit Premiere cleanly, then shut the PC down (normal shutdown, 5-min delay, never forced)
metadata:
  type: feedback
---

Affan, 2026-10-13 (handing over 4 reaction videos before bed): "once the videos are done completely edited inside of Premiere I want you
to save the project and shut the computer down… so that my computer is not running for hours and hours for no reason."

**Why:** the PC otherwise idles all night after the work is done.

**How to apply:** at the end of such a job: `app.project.save()` and read it back; quit Premiere cleanly (nothing left with a "save
changes?" prompt); check no other Claude session or agent is mid-job on this machine (lock files under `lanes/premiere/ACTIVE-WINDOW.lock`,
`projects/_onyx-batch2-2026-10/.locks/`, running agents) and wait for them rather than cut them off; then `shutdown /s /t 300` (a normal,
cancellable shutdown: `shutdown /a`), never `/f`. Only when he asked for it for that job; say in the final message that it is happening.
