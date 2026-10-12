---
name: feedback-no-c-drive-exports
description: "Affan 2026-10-12: never put videos on the C drive (no ~/Downloads export copies); everything for his business lives on the X drive, export copies go to X:\\Claude Projects\\Exports\\"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 4f6ff510-e01c-4ae4-a5c4-8388b194173e
  modified: 2026-10-12T13:51:16.215Z
---

Affan, 2026-10-12: "from now don't fill C drive with these videos; everything related to your business will be in X drive."
Export/deliverable copies go to **`X:\Claude Projects\Exports\`** (one folder, file names as before, e.g.
`<job>.yt.final.mp4`), never `C:\Users\affan\Downloads\`. Set `VE_EXPORT_DIR="X:/Claude Projects/Exports"` on every
`finalize.sh` run, and tell build agents the same in their brief. Downloads, renders, scratch and caches stay on X too
(job folders under `X:\Claude Projects\...`); keep large temp files out of `%TEMP%` on C where a tool lets you choose.

**Why:** C is his system drive; the X: NVMe is the workspace ([[project-workspace-on-nvme]]).

**How to apply:** any step that copies a deliverable "to Downloads" (CLAUDE.md step 8, the Onyx PLAYBOOK, AGENT-BRIEF) now
targets the X Exports folder instead. Batch-2's copies already in C:\Users\affan\Downloads (8 samples + older finals) are
duplicates of the job outputs; removing them is his call.
