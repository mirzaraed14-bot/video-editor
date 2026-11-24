"""p2b4_measure.py <job dir> (fix round 3, needs cv2: PYTHONPATH=X:/Claude Projects/.pylib-cv2 python): YuNet head box on the camera frames at both ends of EVERY face clip (V2 of work/dump-syn.json = one clip per kept segment),
median of 5 frames each end. Writes work/p2b4-det.json {clip index: {s, e, i, o, A, B}} (camera px 1920x1080: cx, cy, w, h, mouth)."""
import json, os, subprocess, sys
import cv2, numpy as np
REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "..", "..", ".."))
J = sys.argv[1] if len(sys.argv) > 1 else "."; SJ = json.load(open(os.path.join(J, "seq.json"), encoding="utf-8"))
det = cv2.FaceDetectorYN.create(os.path.join(REPO, "assets", "models", "face_detection_yunet_2023mar.onnx"), "", (960, 540), 0.6)
seq = next(s for s in json.load(open(os.path.join(J, "work", "dump-syn.json"), encoding="utf-8")) if s["name"] == SJ["sequence"])
fc = seq["v"][1]["clips"]; CAM = SJ["cameras"][0]["path"].replace("\\", "/"); FPS = float(os.environ.get("CAM_FPS", "59.94"))
def frames(t, n):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{max(t,0):.4f}", "-i", CAM, "-frames:v", str(n), "-vf", "scale=960:540", "-f", "rawvideo", "-pix_fmt", "bgr24", "-"], capture_output=True).stdout
    k = len(raw) // (960 * 540 * 3); return [np.frombuffer(raw[j * 960 * 540 * 3:(j + 1) * 960 * 540 * 3], np.uint8).reshape(540, 960, 3) for j in range(k)]
def one(img):
    _, d = det.detect(img)
    if d is None or not len(d): return None
    r = max(d, key=lambda q: q[2] * q[3])
    return dict(cx=(r[0] + r[2] / 2) * 2, cy=(r[1] + r[3] / 2) * 2, w=r[2] * 2, h=r[3] * 2, mouth=(r[11] + r[13]) / 2 * 2)
def med(ds):
    ds = [x for x in ds if x]
    return {k: float(np.median([x[k] for x in ds])) for k in ds[0]} if ds else None
out = {}
for k, c in enumerate(fc):
    d = c["o"] - c["i"]; nf = min(5, max(2, int(d * FPS) // 3))
    A = med([one(x) for x in frames(c["i"], nf)]); B = med([one(x) for x in frames(c["o"] - nf / FPS - 0.01, nf)])
    out[str(k)] = dict(s=c["s"], e=c["e"], i=c["i"], o=c["o"], A=A, B=B)
    print(k, f"{c['s']:.3f}", "A", A and [round(A[q]) for q in ("cx", "cy", "h")], "B", B and [round(B[q]) for q in ("cx", "cy", "h")], flush=True)
json.dump(out, open(os.path.join(J, "work", "p2b4-det.json"), "w"), indent=0)
