"""headlock-check.py: does the head stay put across the jump cuts? Measures the eyes (YuNet), median of 6 frames before and 6 frames after
every joint that falls inside a speaker shot, on a rendered Short, and prints the jump in face-centre height and face size.

  python workflows/headlock-check.py RENDER.mp4 projects/<job> [--fps-mult 1]

Reads <job>/yt/spec.json (shots, head_lock joints) to pick the joints inside A shots. A clean lock: |dy| <= ~12 px and |dh| <= ~5 % (eye line, inter-eye distance)
at every joint (Affan 2026-10-19: "his face shouldn't be moving up and down with the cuts").
"""
import json, os, subprocess, sys
import cv2, numpy as np

REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
MODEL = os.path.join(REPO, "assets", "models", "face_detection_yunet_2023mar.onnx")


def frame(path, n, fps):
    out = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{n / fps:.4f}", "-i", path, "-frames:v", "1", "-f", "rawvideo", "-pix_fmt", "bgr24", "-"],
                         capture_output=True).stdout
    return np.frombuffer(out, np.uint8).reshape(1920, 1080, 3) if len(out) == 1920 * 1080 * 3 else None


def face(img, det):
    det.setInputSize((img.shape[1], img.shape[0])); _, f = det.detect(img)
    if f is None or not len(f):
        return None
    f = [r for r in f if r[3] >= 0.12 * img.shape[0] and r[1] + r[3] / 2 < 0.62 * img.shape[0]]   # a face, not a hand or the mic
    if not f:
        return None
    r = max(f, key=lambda r: r[14])                               # the most confident one; measured on the EYES (the box slides on a
    return (r[4] + r[6]) / 2, (r[5] + r[7]) / 2, float(np.hypot(r[6] - r[4], r[7] - r[5]))   # face looking down)


def main():
    src, job = sys.argv[1], sys.argv[2]
    mult = int(sys.argv[sys.argv.index("--fps-mult") + 1]) if "--fps-mult" in sys.argv else 1
    spec = json.load(open(os.path.join(job, "yt", "spec.json"), encoding="utf-8"))
    fps = spec["fps"] * mult
    det = cv2.FaceDetectorYN.create(MODEL, "", (1080, 1920), 0.6)
    js = [j for j in spec.get("head_lock", []) if any(s["kind"] == "A" and s["f0"] < j < s["f1"] for s in spec["shots"])]
    worst_y, worst_h, rows = 0.0, 0.0, []
    for j in js:
        def med(ns):                              # the median over 6 frames: one frame's detection is too noisy to judge a lock
            got = [face(im, det) for im in (frame(src, n * mult, fps) for n in ns) if im is not None]
            got = [g for g in got if g]
            return tuple(float(np.median([g[i] for g in got])) for i in range(3)) if len(got) >= 3 else None
        fa, fb = med(range(j - 7, j - 1)), med(range(j + 1, j + 7))
        if not fa or not fb:
            rows.append(f"  joint {j:5d}: face not found"); continue
        dy, dh = fb[1] - fa[1], 100 * (fb[2] - fa[2]) / fa[2]
        worst_y, worst_h = max(worst_y, abs(dy)), max(worst_h, abs(dh))
        rows.append(f"  joint {j:5d}: eyes y {fa[1]:6.0f} -> {fb[1]:6.0f} (dy {dy:+5.0f} px)   eye gap {fa[2]:4.0f} -> {fb[2]:4.0f} ({dh:+5.1f} %)")
    print(f"{os.path.basename(src)}: {len(js)} joints inside speaker shots")
    print("\n".join(rows))
    print(f"worst: |dy| {worst_y:.0f} px, |dh| {worst_h:.1f} %  ->  " + ("LOCKED" if worst_y <= 12 and worst_h <= 5 else "MOVES"))


if __name__ == "__main__":
    main()
