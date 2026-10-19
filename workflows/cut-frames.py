"""cut-frames.py: snap head-lock joints to the frame where the picture REALLY cuts (scene score peak within +-4 frames).
Joints computed from the EDL can sit 1-2 frames off the cut after frame snapping; head lock then matches the wrong frames
across the jump (Serhant calendar, 2026-10-19: joint 53 was really 55).

  python workflows/cut-frames.py BASE.mp4 work/cut/joints30.txt > work/cut/joints_measured.txt
"""
import re, subprocess, sys
base, jf = sys.argv[1], sys.argv[2]
out = subprocess.run(["ffmpeg", "-hide_banner", "-v", "error", "-i", base, "-an", "-vf",
                      "scale=320:-2,select='gte(scene,0)',metadata=print:key=lavfi.scene_score:file=-", "-f", "null", "-"],
                     capture_output=True, text=True).stdout
sc = [float(m) for m in re.findall(r"lavfi.scene_score=([0-9.]+)", out)]
J = [int(x) for x in open(jf).read().split(",") if x.strip()]
res = [0] + [max(range(max(1, j - 4), min(len(sc), j + 5)), key=lambda i: sc[i]) for j in J if j > 0]
print(",".join(map(str, res)))
print("moved:", [(j, k) for j, k in zip(J[1:], res[1:]) if j != k], file=sys.stderr)
