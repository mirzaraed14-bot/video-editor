# /// script
# requires-python = ">=3.10"
# dependencies = ["opencv-python-headless", "numpy"]
# ///
"""yt_faces.py: face boxes on the base cut for every speaker shot of a spec -> <job>/<dir>/work/faces.json (the "faces" input
of yt_picture.py).

  uv run presets/youtube-shorts/onyx-samples-youtube/kit/yt_faces.py projects/<job> [--dir ig] [--step 2]

Reads `<job>/<dir>/spec.json`: "base" (the approved cut), "fps", "shots". Every A shot's "face" key and every SPLIT shot's
"top"."face" key is scanned over that shot's frames [f0, f1), every `--step` frames, with YuNet
(assets/models/face_detection_yunet_2023mar.onnx); the largest face wins. Boxes are stored in the BASE's pixels, also when
detection runs on a downscaled copy (bases wider than 1920 px). Several shots may share one key (one speaker): yt_picture
fits each shot only to the detections inside its own frame range.
"""
import json, os, subprocess, sys
import cv2, numpy as np

KIT = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(KIT, "..", "..", "..", ".."))
MODEL = os.path.join(REPO, "assets", "models", "face_detection_yunet_2023mar.onnx")


def probe(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height", "-of", "csv=p=0", path],
                         capture_output=True, text=True).stdout.strip().split(",")
    return int(out[0]), int(out[1])


def main():
    job = os.path.abspath(sys.argv[1])
    sub = sys.argv[sys.argv.index("--dir") + 1] if "--dir" in sys.argv else "yt"
    step = int(sys.argv[sys.argv.index("--step") + 1]) if "--step" in sys.argv else 2
    spec = json.load(open(os.path.join(job, sub, "spec.json"), encoding="utf-8"))
    base = spec["base"] if os.path.isabs(spec["base"]) else os.path.join(job, spec["base"])
    BW, BH = probe(base)
    s = min(1.0, 1920 / BW)
    W, H = int(round(BW * s)), int(round(BH * s))
    want = {}
    for sh in spec["shots"]:
        key = sh.get("face") if sh["kind"] == "A" else (sh.get("top", {}).get("face") if sh["kind"] == "SPLIT" else None)
        if key:
            for n in range(sh["f0"], sh["f1"], step):
                want[n] = key
            want[sh["f1"] - 1] = key
    det = cv2.FaceDetectorYN.create(MODEL, "", (W, H), 0.6, 0.3, 5000)
    proc = subprocess.Popen(["ffmpeg", "-v", "error", "-i", base, "-vf", f"scale={W}:{H}", "-f", "rawvideo", "-pix_fmt", "bgr24", "-"],
                            stdout=subprocess.PIPE)
    found = {}
    n = 0
    last = max(want) if want else -1
    while n <= last:
        buf = proc.stdout.read(W * H * 3)
        if len(buf) < W * H * 3:
            break
        if n in want:
            _, faces = det.detect(np.frombuffer(buf, np.uint8).reshape(H, W, 3))
            if faces is not None and len(faces):
                f = max(faces, key=lambda r: r[2] * r[3])
                found.setdefault(want[n], {})[n] = [round(float(v) / s, 1) for v in f[:4]]
        n += 1
    proc.stdout.close(); proc.kill()
    out = {}
    for key in sorted(set(want.values())):
        pf = found.get(key, {})
        if not pf:
            out[key] = {"frames": 0}
            print(f"{key:16s} NO FACE")
            continue
        b = np.array(list(pf.values()))
        cx, cy = b[:, 0] + b[:, 2] / 2, b[:, 1] + b[:, 3] / 2
        out[key] = {"frames": len(pf), "cx_med": round(float(np.median(cx)), 1), "cx_min": round(float(cx.min()), 1),
                    "cx_max": round(float(cx.max()), 1), "cy_med": round(float(np.median(cy)), 1), "h_med": round(float(np.median(b[:, 3])), 1),
                    "per_frame": {str(k): v for k, v in sorted(pf.items())}}
        o = out[key]
        print(f"{key:16s} n={o['frames']:4d}  cx {o['cx_med']:.0f} [{o['cx_min']:.0f}-{o['cx_max']:.0f}]  cy {o['cy_med']:.0f}  face h {o['h_med']:.0f}  (base {BW}x{BH})")
    os.makedirs(os.path.join(job, sub, "work"), exist_ok=True)
    json.dump(out, open(os.path.join(job, sub, "work", "faces.json"), "w", encoding="utf-8"), indent=1)


if __name__ == "__main__":
    main()
