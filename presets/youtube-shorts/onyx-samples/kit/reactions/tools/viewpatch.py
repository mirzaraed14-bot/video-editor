"""viewpatch.py (fix shift 2026-11-09): per-view panel BOX and a source-px left crop, for the tools that import it (mgxo.py, applyo.py, claudecheck_o.py).

  views_named[v]["box"]           [x0, y0, x1, y1]  this view's panel on the 1080x1920 frame (default plan["box"]): the layer is cropped to it (beat 5's shorter player panel, R3)
  views_named[v]["crop_left_src"] source px: a Premiere Crop Left of at least that x on the OBS clip, scale/position unchanged (no YouTube guide sidebar beside the player)
Patches: geom.view_motion (crop + box), overlays.src_to_frame (marks / sweeps / tags follow the view's own box), and the leak test (applyo wraps apply.leak_problems)."""
import os, sys
TOOLS = os.path.dirname(os.path.abspath(__file__))
if TOOLS not in sys.path: sys.path.insert(0, TOOLS)
import geom as G          # noqa: E402
import overlays as O      # noqa: E402

_vm = G.view_motion


def view_motion(v):
    box = v.get("box"); saved = G.BOX
    if box: G.BOX = tuple(box)
    try: m = _vm(v)
    finally: G.BOX = saved
    cl = v.get("crop_left_src")
    if cl: m["crop"]["L"] = max(m["crop"]["L"], round(cl / G.SW * 100, 3))
    return m


def src_to_frame(view, x, y):
    s = G.BASE * view["z"]; B = view.get("box") or G.BOX
    return (B[0] + B[2]) / 2 + (x - view["cx"]) * s, (B[1] + B[3]) / 2 + (y - view["cy"]) * s


G.view_motion = view_motion
O.src_to_frame = src_to_frame
