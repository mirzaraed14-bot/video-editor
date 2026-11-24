"""applyx.py <plan.json> <apply.py flags...>: run the shared apply.py with mgx6's geom.face_motion patch loaded first (face-only beats
framed on the MOUTH: face_x = [x, mouth_y]), so --layout writes exactly the framing the stills and the reviewer saw."""
import os, runpy, sys
HERE = os.path.dirname(os.path.abspath(__file__))
TOOLS = HERE
sys.path.insert(0, HERE); sys.path.insert(0, TOOLS)
import json
import mgx6   # noqa: E402,F401  (patches geom.face_motion)
plan = json.load(open(sys.argv[1], encoding="utf-8"))
if plan.get("mouth_y"): mgx6.MOUTH_Y = float(plan["mouth_y"])
# the effective face scale (face_motion raises it so the window stays covered when the mouth sits low): written into a sibling plan so
# apply.py --layout and --verify read the SAME number (idempotent: face_motion(eff) == face_motion(nominal))
for f in plan["face"]:
    if isinstance(f.get("face_x"), list): f["scale"] = mgx6.face_motion(f.get("scale", 150), f["face_x"])["scale"]
eff = os.path.join(os.path.dirname(os.path.abspath(sys.argv[1])), "plan.eff.json")
json.dump(plan, open(eff, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
sys.argv = [os.path.join(TOOLS, "apply.py"), eff] + sys.argv[2:]
runpy.run_path(os.path.join(TOOLS, "apply.py"), run_name="__main__")
