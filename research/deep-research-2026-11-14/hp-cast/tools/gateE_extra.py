"""Oldman face at delivery scale (raw-frame detection, leftmost large face) + the debut clip as a 9:16 full-height crop."""
import pathlib, subprocess, cv2
from PIL import Image
R = pathlib.Path(r"X:\Claude Projects\video-editor-client\video-editor"); H = R / "research/deep-research-2026-11-14/hp-cast"; P = H / "proof"
M = str(R / "assets/models/face_detection_yunet_2023mar.onnx"); T = P / "_g.png"
def grab(f, t):
    subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-ss", str(t), "-i", str(f), "-frames:v", "1", str(T)], check=True); return cv2.imread(str(T))
best = None
for t in (8, 13, 23, 33, 53, 75):
    img = grab(H / "src/yt_oldman_rickman/tVm7ajSlOIU.mp4", t); h, w = img.shape[:2]
    _, fs = cv2.FaceDetectorYN_create(M, "", (w, h), score_threshold=0.5).detect(img)
    for r in ([] if fs is None else fs):
        x, y, bw, bh = (int(v) for v in r[:4]); print("oldman t=%d face x=%d y=%d w=%d score=%.2f" % (t, x, y, bw, r[-1]))
        if x < w * 0.6 and (best is None or bw > best[0]): best = (bw, t, img, x + bw // 2, y + bh // 2)
k = 1920 / 1080; bw, t, img, cx, cy = best
big = cv2.resize(img, None, fx=k, fy=k, interpolation=cv2.INTER_LANCZOS4); cx, cy = int(cx * k), int(cy * k)
x0 = min(max(cx - 270, 0), big.shape[1] - 540); y0 = min(max(cy - 270, 0), big.shape[0] - 540)
a = Image.fromarray(cv2.cvtColor(big[y0:y0 + 540, x0:x0 + 540], cv2.COLOR_BGR2RGB))
d = grab(H / "src/yt_felton_debut/Ug1vk4ve2h8.mp4", 27); cxd = int(d.shape[1] * 0.72)   # Felton stands right of centre
x1 = min(max(cxd - 304, 0), d.shape[1] - 608); b = Image.fromarray(cv2.cvtColor(d[:, x1:x1 + 608], cv2.COLOR_BGR2RGB)).resize((304, 540), Image.LANCZOS)
out = Image.new("RGB", (844, 540)); out.paste(a, (0, 0)); out.paste(b, (540, 0)); out.save(P / "anchor_extra.jpg", quality=90)
print("oldman best t=%d face %dpx raw -> %dpx at delivery" % (t, bw, int(bw * k))); T.unlink(missing_ok=True)
