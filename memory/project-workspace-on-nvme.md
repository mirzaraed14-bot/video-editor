---
name: project-workspace-on-nvme
description: "Since 2026-09-26 the whole workspace lives on the X: NVMe (X:\\Claude Projects); E:\\Claude Projects is retired and becomes a junction to X: via move-to-nvme.cmd"
metadata:
  type: project
---

On 2026-09-26 the user copied `E:\Claude Projects` (115 GB, 31.8k files) to the new NVMe at **`X:\Claude Projects`**
and asked to operate from there, because E: is nearly full (822 GB used, 132 GB free). Verified complete with a
list-only robocopy: every file matches; X: has the live git repo (commit `64e6724`, ahead of E:).

**Why:** E: was running out of space; the user wants no duplicate data and no disturbance to the workflow.

**How to apply:**
- Open Claude Code at `X:\Claude Projects\video-editor-client\video-editor` (memory is linked there via
  `C:\Users\affan\.claude\projects\X--Claude-Projects-video-editor-client-video-editor\memory`). The Content
  Engine is `X:\Claude Projects\Abundance Wisdom\`.
- **Old paths still matter:** Premiere projects ABW8 (127 files) and ABW6 (372 files) link media under
  `E:\Claude Projects\...` (overlays, Hot Coffee / Travis Scott graphics, `GTA 6\screenshots`), and old jobs'
  `placement.json` files carry E: source paths. The fix is not relinking: **`X:\Claude Projects\move-to-nvme.cmd`**
  renames `E:\Claude Projects` to `Claude Projects OLD delete-later` and creates a junction `E:\Claude Projects →
  X:\Claude Projects`, so every old path resolves to the NVMe copy. Run it with Premiere and every Claude window
  closed (an open session's working directory blocks the rename). Delete the OLD folder by hand after a few
  clean days. Until it runs, don't delete E:\Claude Projects.
- `.mcp.json`, the Abundance Wisdom scripts (`head_track`, `plan_placement`, `zoom_center`: repo-relative now)
  and `apply_headlock.py` (AE report next to the jsx) no longer hard-code E:. Media outside the workspace
  (`E:\Shorts`, `E:\Bullshit Folder`, `E:\Skool Recordings`, `E:\Premiere Pro Exports`) was NOT moved and is
  where most of E:'s 822 GB actually sits. Related: [[project-abundance-shorts-automation]].
