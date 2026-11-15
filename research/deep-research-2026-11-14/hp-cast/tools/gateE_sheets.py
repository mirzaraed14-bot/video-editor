"""Gate E for the hp-cast finalists: contact sheets, the anchor test (face crops at delivery scale against the approved
Prince ABC panels, Lanczos only, no Topaz), and the audio of every beat window (integrated LUFS, LRA, noise floor).
run from the repo root:  uv run --with opencv-python-headless --with pillow python -I <this file>
Outputs in hp-cast/proof/: sheet_hsc.jpg, sheet_debut.jpg, sheet_oldman.jpg, anchor_compare.jpg, audio.txt"""
import pathlib, re, subprocess
import cv2, numpy as np
from PIL import Image, ImageDraw

R = pathlib.Path(r"X:\Claude Projects\video-editor-client\video-editor")
H = R / "research/deep-research-2026-11-14/hp-cast"; S = H / "src"; P = H / "proof"; P.mkdir(exist_ok=True)
HSC1 = S / "yt_felton_hsc/pSWIM3Tc9y0_0-780.mp4"        # file time = RSS time (xcorr 0.00 s)
HSC2 = S / "yt_felton_hsc/pSWIM3Tc9y0_1530-1980.mp4"     # file time = RSS time - 1429.92 s
DEB = S / "yt_felton_debut/Ug1vk4ve2h8.mp4"
OLD = S / "yt_oldman_rickman/tVm7ajSlOIU.mp4"
SON = R / "projects/mj-son-step-outside/outputs/Why Michael Jackson's Son Had To Step Outside.mov"
TMP = P / "_f.png"
MODEL = str(R / "assets/models/face_detection_yunet_2023mar.onnx")  # the YuNet model workflows/face-frame.py uses (OpenCV 5 has no Haar)


def faces(img):
    h, w = img.shape[:2]
    _, f = cv2.FaceDetectorYN_create(MODEL, "", (w, h), score_threshold=0.6).detect(img)
    return [] if f is None else [tuple(int(v) for v in r[:4]) for r in f]


def grab(f, t):
    subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-ss", str(t), "-i", str(f), "-frames:v", "1", str(TMP)], check=True)
    return cv2.imread(str(TMP))


def label(im, text):
    d = ImageDraw.Draw(im); d.rectangle((0, 0, im.width, 20), fill="black"); d.text((5, 4), text, fill="yellow"); return im


def sheet(name, f, times, cols=4, w=400):
    tiles = []
    for t in times:
        img = cv2.cvtColor(grab(f, t), cv2.COLOR_BGR2RGB); h = int(w * img.shape[0] / img.shape[1])
        tiles.append(label(Image.fromarray(cv2.resize(img, (w, h), interpolation=cv2.INTER_AREA)), "%s %.0f s" % (name, t)))
    rows = (len(tiles) + cols - 1) // cols; th = tiles[0].height
    out = Image.new("RGB", (cols * w, rows * th))
    for k, im in enumerate(tiles):
        out.paste(im, ((k % cols) * w, (k // cols) * th))
    out.save(P / ("sheet_%s.jpg" % name), quality=85)


def face_tile(lab, f, times, scale):
    """Largest frontal face over the candidate times, shown 540x540 at DELIVERY scale (Lanczos), as the Short would show it."""
    best = None
    for t in times:
        img = grab(f, t)
        if scale != 1:
            img = cv2.resize(img, None, fx=scale, fy=scale, interpolation=cv2.INTER_LANCZOS4)
        fs = faces(img)
        if len(fs):
            x, y, w, h = max(fs, key=lambda r: r[2] * r[3])
            if best is None or w > best[0]:
                best = (w, t, img, x + w // 2, y + h // 2)
    if best is None:
        img = grab(f, times[0]); return label(Image.fromarray(cv2.cvtColor(cv2.resize(img, (540, 540)), cv2.COLOR_BGR2RGB)), lab + " (no face)")
    w, t, img, cx, cy = best
    x0 = min(max(cx - 270, 0), img.shape[1] - 540); y0 = min(max(cy - 270, 0), img.shape[0] - 540)
    crop = cv2.cvtColor(img[y0:y0 + 540, x0:x0 + 540], cv2.COLOR_BGR2RGB)
    return label(Image.fromarray(crop), "%s @%.1fs face %dpx" % (lab, t, w))


def audio(lab, f, ss, to):
    r = subprocess.run(["ffmpeg", "-nostdin", "-v", "info", "-ss", str(ss), "-to", str(to), "-i", str(f), "-vn", "-af", "ebur128", "-f", "null", "-"],
                       capture_output=True, text=True, encoding="utf-8", errors="replace").stderr
    i = re.findall(r"I:\s+(-?[\d.]+) LUFS", r); lra = re.findall(r"LRA:\s+([\d.]+) LU", r)
    x = np.frombuffer(subprocess.run(["ffmpeg", "-v", "error", "-ss", str(ss), "-to", str(to), "-i", str(f), "-vn", "-ac", "1", "-ar", "16000",
                                      "-f", "s16le", "-"], capture_output=True).stdout, np.int16).astype(np.float32) / 32768
    fr = x[: len(x) // 800 * 800].reshape(-1, 800); rms = 20 * np.log10(np.sqrt((fr ** 2).mean(1)) + 1e-9)
    return "%-34s %7.1f-%7.1f s  I %6s LUFS  LRA %5s LU  floor(p5) %6.1f dBFS  peak %6.1f dBFS" % (
        lab, ss, to, i[-1] if i else "?", lra[-1] if lra else "?", np.percentile(rms, 5), 20 * np.log10(np.abs(x).max() + 1e-9))


sheet("hsc", HSC1, [28, 349, 360, 370, 380, 395, 440, 470])
sheet("hsc2", HSC2, [156, 175, 190, 201, 212, 222, 235, 250])
sheet("debut", DEB, [2, 7, 12, 17, 22, 27, 32, 38])
sheet("oldman", OLD, [3, 13, 23, 33, 43, 53, 63, 75])
k = 1920 / 1080  # a 16:9 1080p source shown full-height in a 1080x1920 Short
tiles = [face_tile("APPROVED Prince ABC P7", SON, [25.0], 1), face_tile("APPROVED Prince ABC P8", SON, [32.5], 1),
         face_tile("Felton HSC (confession)", HSC1, [356, 362, 368, 374, 386], k),
         face_tile("Felton HSC (Potter)", HSC2, [176, 184, 192, 204, 216], k),
         face_tile("Felton debut clip", DEB, [8, 12, 16, 20, 24, 28, 32, 36], k),
         face_tile("Oldman TIFF clip", OLD, [5, 15, 25, 35, 45, 55, 65, 75], k)]
out = Image.new("RGB", (1620, 1080))
for n, im in enumerate(tiles):
    out.paste(im.resize((540, 540)), ((n % 3) * 540, (n // 3) * 540))
out.save(P / "anchor_compare.jpg", quality=90)
lines = [audio("Felton HSC cold open", HSC1, 0, 45), audio("Felton HSC confession+roar talk", HSC1, 345, 490),
         audio("Felton HSC Potter passage", HSC2, 150, 260), audio("Felton debut clip (whole)", DEB, 0, 41.7),
         audio("Oldman Rickman clip (whole)", OLD, 0, 82.9)]
(P / "audio.txt").write_text("\n".join(lines) + "\n", encoding="utf-8"); print("\n".join(lines))
TMP.unlink(missing_ok=True)
