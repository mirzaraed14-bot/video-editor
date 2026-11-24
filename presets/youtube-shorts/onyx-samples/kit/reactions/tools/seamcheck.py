"""seamcheck.py <job dir> [dump.json]: the seam check from the READBACK (dump.py / syndump.py format, no Premiere call): for every face clip on the face track
  layer top  = pos_y * H - anchor_y * h * scale                       must be <= seam - 2   (the UNCROPPED layer covers the seam: the hard cover bound)
  visible top = pos_y * H + (cropTop% * h / 100 - anchor_y * h) * scale   must be <= seam + 1   (Crop Top trims it to the seam; no black band under the line)
H = 1920 (frame), h = source height (1080), scale = Scale / 100. Exit 1 when any clip breaks either. The dump defaults to plan['dump'].
NOTE: REACTIONS-LEAN writes the bound with the cropTop term in it ('top = pos_y*H + (cropT*h/100 - ay*h)*scale <= seam - 2'); with the term the value is the visible top, which
the crop pins at the seam (1038) on EVERY correct clip, so that form can never pass. The cover bound is the layer top without the crop term (lunchtable's final: 1035.0 on clip 1)."""
import json, os, sys
if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"): print(__doc__); raise SystemExit(0)
J = sys.argv[1]; plan = json.load(open(os.path.join(J, "plan.json"), encoding="utf-8")); SEAM = plan.get("seam", 1038)
dump = sys.argv[2] if len(sys.argv) > 2 else os.path.join(J, plan.get("dump", "work/dump-layout.json"))
seq = next(s for s in json.load(open(dump, encoding="utf-8")) if s["name"] == plan["sequence"])
H, h = 1920.0, 1080.0; worst = (-1e9, None); n = 0; bad = []
for c in seq["v"][plan.get("face_track", 1)]["clips"]:
    m = c.get("m") or {}
    if "Position" not in m: continue
    sc = float(m.get("Scale", 100)) / 100.0; ay = (m.get("Anchor Point") or [0.5, 0.5])[1]; ct = float(m.get("Crop Top", 0))
    lay = m["Position"][1] * H - ay * h * sc; vis = m["Position"][1] * H + (ct * h / 100.0 - ay * h) * sc; n += 1
    if lay > worst[0]: worst = (lay, c["s"])
    if lay > SEAM - 2 or vis > SEAM + 1: bad.append((c["s"], round(lay, 1), round(vis, 1)))
print(f"seamcheck: {n} face clips, worst layer top y {worst[0]:.1f} at {worst[1]} (limit {SEAM - 2}), {len(bad)} over")
for b in bad[:5]: print("  over (t, layer top, visible top):", b)
sys.exit(1 if bad else 0)
