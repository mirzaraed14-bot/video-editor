"""mouth.py: YuNet face box + landmarks of Affan on the reaction camera. mouth_at(cam, t) -> (face_cx, mouth_y, eye_y, chin_y) in camera px
(1920x1080), or None. Detections centred left of MIN_X are the leather chair (facex6.py)."""
import os, subprocess
import cv2, numpy as np
REPO = r"X:\Claude Projects\video-editor-client\video-editor"
_det = cv2.FaceDetectorYN.create(os.path.join(REPO, "assets", "models", "face_detection_yunet_2023mar.onnx"), "", (960, 540), 0.6)
MIN_X = 820.0
def mouth_at(cam, t):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{t:.3f}", "-i", cam, "-frames:v", "1", "-vf", "scale=960:540", "-f", "rawvideo", "-pix_fmt", "bgr24", "-"], capture_output=True).stdout
    if len(raw) != 960 * 540 * 3: return None
    _, d = _det.detect(np.frombuffer(raw, np.uint8).reshape(540, 960, 3))
    if d is None: return None
    d = [r for r in d if (r[0] + r[2] / 2) * 2 >= MIN_X]
    if not d: return None
    r = max(d, key=lambda q: q[2] * q[3])
    return (float(r[0] + r[2] / 2) * 2, float((r[11] + r[13]) / 2) * 2, float((r[5] + r[7]) / 2) * 2, float(r[1] + r[3]) * 2)
if __name__ == "__main__":
    import sys
    for t in sys.argv[2:]: print(t, mouth_at(sys.argv[1], float(t)))
