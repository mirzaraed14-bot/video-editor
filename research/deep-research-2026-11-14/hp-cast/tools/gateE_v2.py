"""Gate E v2 (after the cold read): one labelled anchor sheet (8 tiles, delivery scale, Lanczos only), the music check
(spectral flatness of the quiet frames between words), and every measured number saved to proof/measures.txt.
run from the repo root:  uv run --with opencv-python-headless --with pillow python -I <this file>"""
import pathlib, subprocess
import cv2, numpy as np
from PIL import Image, ImageDraw

R = pathlib.Path(r"X:\Claude Projects\video-editor-client\video-editor")
H = R / "research/deep-research-2026-11-14/hp-cast"; S = H / "src"; P = H / "proof"
HSC1 = S / "yt_felton_hsc/pSWIM3Tc9y0_0-780.mp4"; HSC2 = S / "yt_felton_hsc/pSWIM3Tc9y0_1530-1980.mp4"
DEB = S / "yt_felton_debut/Ug1vk4ve2h8.mp4"; OLD = S / "yt_oldman_rickman/tVm7ajSlOIU.mp4"
SON = R / "projects/mj-son-step-outside/outputs/Why Michael Jackson's Son Had To Step Outside.mov"
COS = R / "projects/harry-potter-prank/src/snape/Wizard Duel_ Severus Snape vs Gilderoy Lockhart _ Harry Potter and the Chamber of Secrets.mp4"
M = str(R / "assets/models/face_detection_yunet_2023mar.onnx"); TMP = P / "_v2.png"; K = 1920 / 1080
log = []


def grab(f, t):
    subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-ss", str(t), "-i", str(f), "-frames:v", "1", str(TMP)], check=True)
    return cv2.imread(str(TMP))


def faces(img, thr=0.6):
    h, w = img.shape[:2]
    _, f = cv2.FaceDetectorYN_create(M, "", (w, h), score_threshold=thr).detect(img)
    return [] if f is None else [tuple(int(v) for v in r[:4]) for r in f]


def tile(img, cx, cy, text):
    x0 = int(min(max(cx - 270, 0), img.shape[1] - 540)); y0 = int(min(max(cy - 270, 0), img.shape[0] - 540))
    im = Image.fromarray(cv2.cvtColor(img[y0:y0 + 540, x0:x0 + 540], cv2.COLOR_BGR2RGB)).resize((400, 400), Image.LANCZOS)
    d = ImageDraw.Draw(im); d.rectangle((0, 0, 400, 30), fill="black"); d.text((4, 3), text[:62], fill="yellow"); d.text((4, 16), text[62:124], fill="yellow")
    return im


def face_tile(lab, f, t, scale, pick=lambda fs: max(fs, key=lambda r: r[2])):
    img = grab(f, t)
    if scale != 1:
        img = cv2.resize(img, None, fx=scale, fy=scale, interpolation=cv2.INTER_LANCZOS4)
    fs = faces(img)
    if not fs:
        log.append("%s @%.1fs: no face detected" % (lab, t)); return tile(img, img.shape[1] // 2, img.shape[0] // 2, "%s @%.1fs: NO FACE FOUND" % (lab, t))
    x, y, w, h = pick(fs)
    log.append("%s @%.1fs: face %d px wide at delivery scale" % (lab, t, w))
    return tile(img, x + w // 2, y + h // 2, "%s @%.1fs face %dpx (delivery)" % (lab, t, w))


tiles = [face_tile("APPROVED Prince ABC P7", SON, 25.0, 1), face_tile("APPROVED Prince ABC P8", SON, 32.5, 1),
         face_tile("Felton HSC confession", HSC1, 362, K), face_tile("Felton HSC Potter (YT 28:34)", HSC2, 184, K),
         face_tile("Oldman TIFF (left face)", OLD, 53, K, pick=lambda fs: min(fs, key=lambda r: r[0])),
         face_tile("Film CoS: Draco 'Scared, Potter?'", COS, 119.3, K, pick=lambda fs: min(fs, key=lambda r: r[0]))]
# the debut clip: Felton stands near 49 % of the width at 27 s; show him at delivery scale and measure his face if it is found
d = cv2.resize(grab(DEB, 27), None, fx=K, fy=K, interpolation=cv2.INTER_LANCZOS4)
fs = [r for r in faces(d, 0.3) if abs((r[0] + r[2] / 2) / d.shape[1] - 0.49) < 0.12]
lab = ("debut 27s: Felton, face %d px at delivery (wide only)" % fs[0][2]) if fs else "debut 27s: Felton figure; face too small to detect (wide only)"
log.append(lab)
cx = int(d.shape[1] * 0.49); col = d[:, max(cx - 304 * 2, 0):cx + 304 * 2]
fy = fs[0][1] + fs[0][3] // 2 if fs else int(d.shape[0] * 0.40)
tiles.append(tile(d, cx, fy, lab))
# the audience shot (debut 7 s), for the minors check: the centre of the balcony at delivery scale
a = cv2.resize(grab(DEB, 7), None, fx=K, fy=K, interpolation=cv2.INTER_LANCZOS4)
tiles.append(tile(a, a.shape[1] // 2, int(a.shape[0] * 0.45), "debut 7s: audience (minors check), centre crop"))
sheet = Image.new("RGB", (1600, 800))
for n, im in enumerate(tiles):
    sheet.paste(im, ((n % 4) * 400, (n // 4) * 400))
sheet.save(P / "anchor_v2.jpg", quality=88)
Image.fromarray(cv2.cvtColor(cv2.resize(grab(DEB, 7), (1280, 720), interpolation=cv2.INTER_AREA), cv2.COLOR_BGR2RGB)).save(P / "debut_audience_7s.jpg", quality=85)


def flat(f, ss, to, lab):
    x = np.frombuffer(subprocess.run(["ffmpeg", "-v", "error", "-ss", str(ss), "-to", str(to), "-i", str(f), "-vn", "-ac", "1", "-ar", "16000",
                                      "-f", "s16le", "-"], capture_output=True).stdout, np.int16).astype(np.float32) / 32768
    fr = x[: len(x) // 800 * 800].reshape(-1, 800)
    rms = np.sqrt((fr ** 2).mean(1)); q = fr[rms <= np.percentile(rms, 15)]
    sp = np.abs(np.fft.rfft(q * np.hanning(800), axis=1)) ** 2 + 1e-12
    fl = np.exp(np.log(sp[:, 3:]).mean(1)) / sp[:, 3:].mean(1)
    log.append("%-32s %6.1f-%6.1f s: quiet-frame spectral flatness median %.2f (noise-like >= 0.3 = no music bed; tonal < 0.1 = music)" % (lab, ss, to, np.median(fl)))


def band(f, ss, to, lab):
    """The quietest 10 % of 100 ms frames: spectral flatness in 300-4000 Hz (speech band, above room hum), the strongest bins, the level."""
    x = np.frombuffer(subprocess.run(["ffmpeg", "-v", "error", "-ss", str(ss), "-to", str(to), "-i", str(f), "-vn", "-ac", "1", "-ar", "16000",
                                      "-f", "s16le", "-"], capture_output=True).stdout, np.int16).astype(np.float32) / 32768
    fr = x[: len(x) // 1600 * 1600].reshape(-1, 1600); rms = np.sqrt((fr ** 2).mean(1)); q = fr[rms <= np.percentile(rms, 10)]
    sp = (np.abs(np.fft.rfft(q * np.hanning(1600), axis=1)) ** 2).mean(0) + 1e-12; fq = np.fft.rfftfreq(1600, 1 / 16000)
    b = (fq >= 300) & (fq <= 4000); fl = np.exp(np.log(sp[b]).mean()) / sp[b].mean(); lo = fq >= 40
    top = sorted(int(v) for v in fq[lo][np.argsort(sp[lo])[::-1][:5]])
    log.append("%-34s %6.1f-%6.1f s: band flatness %.2f; strongest bins %s Hz; quiet level %.1f dBFS" % (
        lab, ss, to, fl, ",".join(map(str, top)), 20 * np.log10(np.sqrt((q ** 2).mean()) + 1e-9)))


log.append("MUSIC CHECK v1 (full band, 50 ms frames, quietest 15 %): dominated by 40-100 Hz room hum, so not usable:")
flat(HSC1, 345, 490, "HSC confession + roar answer"); flat(HSC2, 150, 260, "HSC Potter passage"); flat(OLD, 0, 82.9, "Oldman TIFF clip")
log.append("MUSIC CHECK v2 (300-4000 Hz, 100 ms frames, quietest 10 %; noise-like >= 0.4 = no bed, tonal < 0.2 = music):")
band(HSC1, 345, 490, "HSC confession + roar answer"); band(HSC2, 150, 260, "HSC Potter passage"); band(OLD, 0, 82.9, "Oldman TIFF clip")
band(HSC1, 41, 75, "POSITIVE CONTROL: HSC theme + intro"); band(DEB, 3, 40, "CONTROL: debut roar (crowd, no music)")
log += ["xcorr (hp-cast/tools/xcorr.py, 30 s RSS snippets vs the section audio):",
        "  section 1: rss 20.0 -> file 20.00 (z=298); rss 345.0 -> file 345.00 (z=316); rss 430.0 -> file 430.00 (z=321): file = RSS + 0.00 s",
        "  section 2: rss 1595.0 -> file 165.08 (z=308); rss 1630.0 -> file 200.08 (z=344): YouTube = file + 1530 = RSS + 100.08 s"]
(P / "measures.txt").write_text("\n".join(log) + "\n", encoding="utf-8"); print("\n".join(log)); TMP.unlink(missing_ok=True)
