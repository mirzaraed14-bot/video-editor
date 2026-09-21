# /// script
# requires-python = ">=3.9"
# dependencies = ["opencv-python-headless", "numpy"]
# ///
"""
eye-line.py — split a talking-head video into EYE-CONTACT and READING segments.

WHY: on a shoot where the script sits on a monitor off to one side, the creator
looks into the lens for the lines that matter and turns their head to read. That
turn is a natural marker for the graphics pass: overlays and cutaways belong in
the READING segments, never over an eye-contact line. This measures the marker so
the graphics plan can honour it instead of guessing.

HOW: sample frames, detect the face (OpenCV YuNet, the model already vendored in
assets/models/ for face-frame.py and chin-line.py), and per frame compute a YAW
PROXY from the five landmarks:

    roll-corrected  (nose.x - midpoint(eyes).x) / interocular_distance

That ratio is ~0 facing the lens and grows with the head turn, in the direction of
the turn. It is scale-free, so it does not care how far you sit from the camera.

The threshold is NOT a hardcoded angle. Two modes:
  * calibrated  (--calib-camera / --calib-read, from a labelled clip): the
    threshold is the midpoint between the two measured means. Most reliable.
  * automatic   (default): 1-D Otsu over the sample histogram, which finds the
    split between the two clusters the take actually contains.

Either way the run reports SEPARATION (the gap between cluster means in pooled
standard deviations). Below ~2.0 the two states overlap and the split must not
drive anything untouched — use --contact-sheet and look at the frames.

USAGE
  uv run workflows/eye-line.py <video> --out projects/<job>/transcript/eye-line.json
  uv run workflows/eye-line.py <video> --calib-camera 0:00-0:03 --calib-read 0:04-0:07
  uv run workflows/eye-line.py <video> --contact-sheet projects/<job>/transcript/eye-line.png

Run it on the BASE CUT, so the timestamps line up with the graphics plan. Running
it on the raw is fine for a pre-shoot check; those times are raw times.

OUTPUT: JSON with `segments` [{state, t0, t1, dur}], the per-sample `samples`,
and a `calibration` block (threshold, cluster means, separation, miss rate).
"""
import argparse, json, os, subprocess, sys, tempfile

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL = os.path.join(REPO, "assets", "models", "face_detection_yunet_2023mar.onnx")
WIDTH = 960          # analysis width; landmarks are scale-free so this is plenty
MIN_SEG = 0.6        # seconds: shorter than this is a glance, not a state change


def parse_t(s):
    """'12.5' or '1:02.5' -> seconds."""
    s = str(s).strip()
    if ":" not in s:
        return float(s)
    mm, ss = s.rsplit(":", 1)
    return float(mm) * 60 + float(ss)


def parse_range(s):
    a, b = s.split("-", 1)
    return parse_t(a), parse_t(b)


def probe(path):
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
         "stream=width,height:format=duration", "-of", "json", path],
        capture_output=True, text=True, check=True).stdout
    d = json.loads(out)
    st = d["streams"][0]
    return int(st["width"]), int(st["height"]), float(d["format"]["duration"])


def extract(path, step, tmp):
    """One ffmpeg pass for every sample frame — a seek per frame is far too slow
    over a full talking-head take."""
    subprocess.run(
        ["ffmpeg", "-v", "error", "-i", path,
         "-vf", f"fps=1/{step},scale={WIDTH}:-2", "-q:v", "3",
         os.path.join(tmp, "f_%06d.png")], check=True)
    return sorted(f for f in os.listdir(tmp) if f.startswith("f_"))


def yaw_proxy(face):
    """YuNet row: [x, y, w, h, reye(2), leye(2), nose(2), rmouth(2), lmouth(2), score].
    'right eye' is the subject's right, i.e. the LEFT side of the image."""
    import numpy as np
    re = np.array(face[4:6], dtype=float)
    le = np.array(face[6:8], dtype=float)
    nose = np.array(face[8:10], dtype=float)
    eye_vec = le - re
    d = float(np.hypot(*eye_vec))
    if d < 1e-6:
        return None
    # roll correction: express nose relative to the eye midpoint in the eye-line
    # frame, so a tilted head does not read as a turn
    ux = eye_vec / d                      # unit vector along the eye line
    mid = (re + le) / 2.0
    return float(np.dot(nose - mid, ux) / d)


def otsu(values, bins=64):
    import numpy as np
    v = np.asarray(values, dtype=float)
    lo, hi = float(v.min()), float(v.max())
    if hi - lo < 1e-9:
        return lo
    hist, edges = np.histogram(v, bins=bins, range=(lo, hi))
    centers = (edges[:-1] + edges[1:]) / 2.0
    total = hist.sum()
    w0 = np.cumsum(hist) / total
    m0 = np.cumsum(hist * centers) / total
    mT = m0[-1]
    denom = w0 * (1 - w0)
    with np.errstate(divide="ignore", invalid="ignore"):
        between = (mT * w0 - m0) ** 2 / denom
    between[~np.isfinite(between)] = -1
    return float(centers[int(between.argmax())])


def smooth(states, times, min_seg):
    """Collapse runs shorter than min_seg into their neighbours."""
    if not states:
        return []
    runs = []
    for s, t in zip(states, times):
        if runs and runs[-1][0] == s:
            runs[-1][2] = t
        else:
            runs.append([s, t, t])
    changed = True
    while changed and len(runs) > 1:
        changed = False
        for i, r in enumerate(runs):
            if r[2] - r[1] < min_seg:
                # absorb into the longer neighbour
                prev = runs[i - 1] if i > 0 else None
                nxt = runs[i + 1] if i + 1 < len(runs) else None
                target = prev if (nxt is None or (prev is not None and
                                  (prev[2] - prev[1]) >= (nxt[2] - nxt[1]))) else nxt
                target[1] = min(target[1], r[1]); target[2] = max(target[2], r[2])
                runs.pop(i)
                # merge any now-adjacent same-state runs
                j = 0
                while j + 1 < len(runs):
                    if runs[j][0] == runs[j + 1][0]:
                        runs[j][2] = max(runs[j][2], runs[j + 1][2]); runs.pop(j + 1)
                    else:
                        j += 1
                changed = True
                break
    return runs


def contact_sheet(frames_dir, names, picks, out_path, cols=6):
    import cv2
    tiles = []
    for idx, label in picks:
        img = cv2.imread(os.path.join(frames_dir, names[idx]))
        if img is None:
            continue
        img = cv2.resize(img, (320, int(320 * img.shape[0] / img.shape[1])))
        cv2.rectangle(img, (0, 0), (img.shape[1], 22), (0, 0, 0), -1)
        cv2.putText(img, label, (4, 16), cv2.FONT_HERSHEY_SIMPLEX, 0.45,
                    (255, 255, 255), 1, cv2.LINE_AA)
        tiles.append(img)
    if not tiles:
        return False
    h = min(t.shape[0] for t in tiles)
    tiles = [t[:h] for t in tiles]
    rows = [cv2.hconcat(tiles[i:i + cols]) for i in range(0, len(tiles), cols)]
    w = max(r.shape[1] for r in rows)
    import numpy as np
    rows = [np.pad(r, ((0, 0), (0, w - r.shape[1]), (0, 0))) for r in rows]
    cv2.imwrite(out_path, cv2.vconcat(rows))
    return True


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("video")
    ap.add_argument("--step", type=float, default=0.25, help="sample interval, seconds (default 0.25)")
    ap.add_argument("--min-seg", type=float, default=MIN_SEG,
                    help=f"shortest state run to keep, seconds (default {MIN_SEG})")
    ap.add_argument("--calib-camera", metavar="T0-T1", help="a range where you are ON the lens")
    ap.add_argument("--calib-read", metavar="T0-T1", help="a range where you are READING the monitor")
    ap.add_argument("--out", metavar="FILE", help="write the JSON here")
    ap.add_argument("--contact-sheet", metavar="OUT.PNG",
                    help="write a grid of frames at every state switch, for eyeballing")
    a = ap.parse_args()

    if not os.path.exists(MODEL):
        sys.exit(f"missing face model: {MODEL}")
    import cv2, numpy as np

    w, h, dur = probe(a.video)
    tmp = tempfile.mkdtemp(prefix="eyeline_")
    names = extract(a.video, a.step, tmp)
    if not names:
        sys.exit("ffmpeg produced no frames")

    first = cv2.imread(os.path.join(tmp, names[0]))
    fh, fw = first.shape[:2]
    det = cv2.FaceDetectorYN.create(MODEL, "", (fw, fh), 0.6, 0.3, 5000)
    det.setInputSize((fw, fh))

    samples, misses = [], 0
    for i, n in enumerate(names):
        img = cv2.imread(os.path.join(tmp, n))
        if img is None:
            misses += 1; continue
        _, faces = det.detect(img)
        if faces is None or len(faces) == 0:
            misses += 1; continue
        face = max(faces, key=lambda f: f[2] * f[3])   # the biggest face is the creator
        y = yaw_proxy(face)
        if y is None:
            misses += 1; continue
        samples.append({"i": i, "t": round(i * a.step, 3), "yaw": round(y, 4)})

    if len(samples) < 8:
        sys.exit(f"only {len(samples)} usable samples of {len(names)} frames — "
                 "no face found often enough to measure; check lighting and framing")

    vals = [s["yaw"] for s in samples]

    # --- threshold -----------------------------------------------------------
    mode, thr = "otsu", None
    if a.calib_camera and a.calib_read:
        c0, c1 = parse_range(a.calib_camera); r0, r1 = parse_range(a.calib_read)
        cam = [s["yaw"] for s in samples if c0 <= s["t"] <= c1]
        red = [s["yaw"] for s in samples if r0 <= s["t"] <= r1]
        if len(cam) < 2 or len(red) < 2:
            sys.exit("calibration ranges did not contain enough detected frames")
        thr = (float(np.mean(cam)) + float(np.mean(red))) / 2.0
        mode = "calibrated"
        cam_mean, read_mean = float(np.mean(cam)), float(np.mean(red))
        read_is_high = read_mean > cam_mean
    else:
        thr = otsu(vals)
        lo = [v for v in vals if v <= thr]; hi = [v for v in vals if v > thr]
        if not lo or not hi:
            sys.exit("could not split the samples into two clusters")
        # the camera cluster is the one whose mean sits nearer a centred nose
        lo_m, hi_m = float(np.mean(lo)), float(np.mean(hi))
        read_is_high = abs(hi_m) > abs(lo_m)
        cam_mean, read_mean = (lo_m, hi_m) if read_is_high else (hi_m, lo_m)

    cam_v = [v for v in vals if (v <= thr) == (read_is_high)]
    read_v = [v for v in vals if (v > thr) == (read_is_high)]
    pooled = float(np.sqrt((np.var(cam_v) + np.var(read_v)) / 2.0)) if cam_v and read_v else 0.0
    separation = abs(read_mean - cam_mean) / pooled if pooled > 1e-9 else float("inf")

    # --- states --------------------------------------------------------------
    states, times = [], []
    for s in samples:
        is_read = (s["yaw"] > thr) if read_is_high else (s["yaw"] < thr)
        s["state"] = "reading" if is_read else "camera"
        states.append(s["state"]); times.append(s["t"])
    runs = smooth(states, times, a.min_seg)
    segments = [{"state": st, "t0": round(t0, 2),
                 "t1": round(min(t1 + a.step, dur), 2),
                 "dur": round(min(t1 + a.step, dur) - t0, 2)} for st, t0, t1 in runs]

    cam_time = sum(s["dur"] for s in segments if s["state"] == "camera")
    read_time = sum(s["dur"] for s in segments if s["state"] == "reading")
    result = {
        "video": os.path.abspath(a.video), "duration": round(dur, 2),
        "step": a.step, "min_seg": a.min_seg,
        "calibration": {
            "mode": mode, "threshold": round(thr, 4),
            "camera_mean": round(cam_mean, 4), "reading_mean": round(read_mean, 4),
            "reading_side": "higher" if read_is_high else "lower",
            "separation_sd": round(separation, 2) if separation != float("inf") else None,
            "samples": len(samples), "frames": len(names),
            "miss_rate": round(misses / max(len(names), 1), 3),
        },
        "totals": {"camera_s": round(cam_time, 2), "reading_s": round(read_time, 2),
                   "camera_share": round(cam_time / max(cam_time + read_time, 1e-9), 3)},
        "segments": segments, "samples": samples,
    }

    if a.out:
        os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
        with open(a.out, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=1)

    if a.contact_sheet:
        picks = []
        for seg in segments:
            near = min(samples, key=lambda s: abs(s["t"] - seg["t0"]))
            picks.append((near["i"], f'{seg["state"][:4].upper()} {seg["t0"]}s'))
        ok = contact_sheet(tmp, names, picks[:36], a.contact_sheet)
        if not ok:
            print("! contact sheet could not be written", file=sys.stderr)

    verdict = ("RELIABLE" if separation >= 2.0 else
               "WEAK — do not let this drive placement untouched; check the frames")
    print(f"samples {len(samples)}/{len(names)}  misses {misses} "
          f"({result['calibration']['miss_rate']*100:.0f}%)")
    print(f"mode {mode}  threshold {thr:+.3f}  camera {cam_mean:+.3f}  reading {read_mean:+.3f}")
    print(f"separation {separation:.2f} SD  -> {verdict}")
    print(f"segments {len(segments)}  camera {cam_time:.1f}s  reading {read_time:.1f}s "
          f"({result['totals']['camera_share']*100:.0f}% on the lens)")
    if a.out:
        print(f"wrote {a.out}")
    if a.contact_sheet:
        print(f"wrote {a.contact_sheet}")


if __name__ == "__main__":
    main()
