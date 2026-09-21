# /// script
# requires-python = ">=3.10"
# dependencies = ["opencv-python-headless"]
# ///
"""
chin-line.py — measure the chin line of a talking-head cut. Measured, not guessed.

Every overlay that shares the frame with the face lives BELOW the chin, and the
only honest way to know where the chin is is to look. This sweeps the video,
detects the face on each sample (OpenCV YuNet, model vendored in assets/models/)
and reports the LOWEST jaw line it finds — the worst case a fixed layout band has
to clear. The YuNet box bottom sits on the jaw, so it is the chin proxy.

Feeds the youtube/default text-animation band (presets/youtube/default/text-animation/build.py
TOP_MIN) and any hand-authored overlay that has to sit under the face. Re-derive
per shoot: a tighter or wider frame moves the chin by 100px+.

It also reports the HEAD'S HORIZONTAL EXTENT (the face box widened by an ear allowance,
worst case over the window) and the side-callout zones that leave it alone (the user,
2026-09-10: a side card never covers the ear; margin to the subject SUBJECT px, to the
frame edge EDGE px; the card goes on the side with more room and takes the room's width).
Usage:
  uv run workflows/chin-line.py projects/<job>/outputs/<job>.mp4
  uv run workflows/chin-line.py <video> --from 43.3 --to 47.0   # one graphic's window
  uv run workflows/chin-line.py <raw> --edl projects/<job>/transcript/cuts.json --from 46.6 --to 52.7 --step 0.1
        # app-finish job (no flat cut): --from/--to are TIMELINE seconds, mapped onto the raw through the EDL
  uv run workflows/chin-line.py <video> --json                  # machine-readable
  uv run workflows/chin-line.py <video> --out chin.json         # durable: a truncated pipe loses it
  uv run workflows/chin-line.py <video> --annotate out.png      # eyeball the worst frame
"""
import argparse, json, os, statistics, subprocess, sys, tempfile

# Windows consoles/pipes default to cp1252 and cannot encode the status glyphs below.
for _s in (sys.stdout, sys.stderr):
    try:
        if (getattr(_s, "encoding", "") or "").lower().replace("-", "") != "utf8":
            _s.reconfigure(encoding="utf-8")
    except AttributeError:
        pass

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL = os.path.join(REPO, "assets", "models", "face_detection_yunet_2023mar.onnx")
GAP = 70          # the breathing room a layout band leaves under the worst chin
STEP = 0.5        # sweep interval, seconds
EAR = 0.20        # ear allowance each side, as a fraction of the YuNet face-box width (the box stops at the cheek)
SUBJECT = 60      # px between a side callout and the head, ears included (default-overlay-style.md § Placement)
EDGE = 80         # px between a side callout and the frame edge (same home)


def edl_map(path):
    """timeline seconds -> source seconds through a cuts.json (segments' start/end are source times)."""
    c = json.load(open(path, encoding="utf-8"))
    segs = c.get("segments") if isinstance(c, dict) else c
    spans, t = [], 0.0
    for sg in segs:
        d = float(sg["end"]) - float(sg["start"])
        spans.append((t, t + d, float(sg["start"])))
        t += d
    def f(tl):
        for a, b, s0 in spans:
            if a <= tl < b:
                return s0 + (tl - a)
        return None
    return f


def probe(video):
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-select_streams", "v:0",
         "-show_entries", "stream=width,height,duration", "-of", "csv=p=0", video],
        capture_output=True, text=True, check=True).stdout
    # iPhone side-data streams make the csv writer emit extra elements — keep the reals.
    out = [t for t in out.strip().splitlines()[0].split(",") if t.strip()]
    return int(out[0]), int(out[1]), float(out[2])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("video")
    ap.add_argument("--from", dest="t0", type=float, default=0.0)
    ap.add_argument("--to", dest="t1", type=float, default=None)
    ap.add_argument("--step", type=float, default=STEP)
    ap.add_argument("--gap", type=float, default=GAP)
    ap.add_argument("--edl", metavar="CUTS.JSON", help="--from/--to are timeline seconds; map them onto the video through this EDL")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--out", metavar="FILE", help="also write the JSON to FILE (stdout can be truncated)")
    ap.add_argument("--annotate", metavar="OUT.PNG")
    a = ap.parse_args()

    import cv2
    w, h, dur = probe(a.video)
    t1 = a.t1 if a.t1 is not None else dur
    det = cv2.FaceDetectorYN.create(MODEL, "", (w, h), 0.6, 0.3, 5000)
    det.setInputSize((w, h))

    td = tempfile.mkdtemp()
    frame = os.path.join(td, "f.png")
    to_src = edl_map(a.edl) if a.edl else (lambda x: x)
    hits, boxes, misses, t = [], [], 0, a.t0 + (0.05 if a.edl else 0.3)
    while t < t1:
        st = to_src(t)
        if st is None:
            t += a.step; continue
        subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{st}", "-i", a.video,
                        "-frames:v", "1", "-y", frame], check=True)
        img = cv2.imread(frame)
        _, faces = det.detect(img)
        if faces is None:
            misses += 1
        else:
            f = faces[0]
            hits.append((round(float(f[1] + f[3])), round(t, 2)))
            boxes.append((float(f[0]), float(f[0] + f[2]), float(f[1]), float(f[2]), round(t, 2)))
        t += a.step

    if not hits:
        sys.exit("no face detected anywhere in the window — measure by hand")

    hits.sort(reverse=True)
    lowest, at = hits[0]
    med = statistics.median([v for v, _ in hits])
    floor = round(lowest + a.gap)

    # the head, worst case over the window: leftmost box edge, rightmost box edge, each widened by the ear
    ear = round(EAR * statistics.median(b[3] for b in boxes))
    hl_box = min(boxes, key=lambda b: b[0]); hr_box = max(boxes, key=lambda b: b[1])
    head_left, head_right = round(hl_box[0] - ear), round(hr_box[1] + ear)
    head_top = round(min(b[2] for b in boxes))
    zone_l = [EDGE, head_left - SUBJECT]; zone_r = [head_right + SUBJECT, w - EDGE]
    room_l, room_r = zone_l[1] - zone_l[0], zone_r[1] - zone_r[0]
    side = "L" if room_l >= room_r else "R"
    head = {"left": head_left, "right": head_right, "top": head_top,
            "face_left": round(hl_box[0]), "face_right": round(hr_box[1]), "ear_px": ear,
            "left_at": hl_box[4], "right_at": hr_box[4]}
    callout = {"L": zone_l, "R": zone_r, "room_left": room_l, "room_right": room_r, "side": side,
               "subject_margin": SUBJECT, "edge_margin": EDGE}

    if a.annotate:
        subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{to_src(at)}", "-i", a.video,
                        "-frames:v", "1", "-y", frame], check=True)
        img = cv2.imread(frame)
        cv2.line(img, (0, lowest), (w, lowest), (0, 0, 255), 3)
        cv2.line(img, (0, floor), (w, floor), (0, 255, 0), 3)
        cv2.rectangle(img, (head_left, head_top), (head_right, lowest), (0, 200, 255), 3)
        for z in (zone_l, zone_r):
            cv2.rectangle(img, (z[0], 150), (z[1], 710), (255, 160, 0), 3)
        cv2.putText(img, f"chin {lowest}", (24, lowest - 14),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.1, (0, 0, 255), 3)
        cv2.putText(img, f"floor {floor}", (24, floor - 14),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.1, (0, 255, 0), 3)
        cv2.imwrite(a.annotate, img)

    payload = {"lowest_chin": lowest, "at": at, "median_chin": med,
               "floor": floor, "gap": a.gap, "samples": len(hits),
               "misses": misses, "frame": [w, h], "head": head, "callout": callout,
               "window": [a.t0, t1], "timeline": bool(a.edl)}
    if a.out:
        with open(a.out, "w", encoding="utf-8") as fh:
            json.dump(payload, fh, indent=2)
    if a.json:
        print(json.dumps(payload, indent=2))
        return
    print(f"samples {len(hits)} (+{misses} no-face)   frame {w}x{h}")
    print(f"median chin  y{med:.0f}")
    print(f"LOWEST chin  y{lowest}  at t={at}s   ← the worst case a band must clear")
    print(f"→ overlay floor  y{floor}  (chin + {a.gap:.0f}px)")
    print(f"HEAD incl. ears  x{head_left}–{head_right}  (face box {head['face_left']}–{head['face_right']}, ear +{ear}px; "
          f"leftmost at t={hl_box[4]}s, rightmost at t={hr_box[4]}s)")
    print(f"→ side callouts  L x{zone_l[0]}–{zone_l[1]} ({room_l}px wide) · R x{zone_r[0]}–{zone_r[1]} ({room_r}px wide)"
          f"  → more room on the {'LEFT' if side == 'L' else 'RIGHT'}   ({SUBJECT}px off the head, {EDGE}px off the edge)")
    if a.annotate:
        print(f"  annotated worst frame: {a.annotate}")
    if a.out:
        print(f"  json: {a.out}")


if __name__ == "__main__":
    main()
