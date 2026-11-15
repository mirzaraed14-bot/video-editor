# Gate-E checks for a finalist's downloaded sources (ig-icons, 14 Nov 2026). Silent: ffmpeg decodes to pipes / -f null only.
# Usage (python -I):
#   e_checks.py probe <file>
#   e_checks.py sheet <file> <out.jpg> <every_s> [start_s] [end_s] [cols=8] [tile_w=320]
#   e_checks.py audio <file> <words.json|-> <span_start> <span_end> [label]   -> LUFS, noise floor, gap flatness (music test)
#   e_checks.py anchor <out.jpg> <file>@<t>@<label>@<scale> ...               -> 1:1 face crops at delivery scale, 540 px tiles
#       scale = how much the source is enlarged on delivery (a 1920x1080 frame cropped to 9:16 full screen = 1.778; an already
#       delivered 1080x1920 Short = 1.0). The face is found with OpenCV's Haar cascade; the 540 px tile is centred on it.
import sys, json, subprocess, math, pathlib
import numpy as np

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8")
    except Exception:
        pass


def run(args, **kw):
    return subprocess.run(args, capture_output=True, **kw)


def probe(f):
    r = run(["ffprobe", "-v", "error", "-show_entries",
             "format=duration,bit_rate:stream=index,codec_type,codec_name,width,height,r_frame_rate,bit_rate,sample_rate,channels",
             "-of", "json", f], text=True)
    d = json.loads(r.stdout)
    fmt = d.get("format", {})
    print("file:", f)
    print("  duration %.2f s, total bitrate %.0f kb/s" % (float(fmt.get("duration", 0)), float(fmt.get("bit_rate", 0)) / 1000))
    for s in d.get("streams", []):
        if s["codec_type"] == "video":
            print("  video #%d %s %sx%s @ %s fps, %s kb/s" % (s["index"], s["codec_name"], s.get("width"), s.get("height"),
                                                             s.get("r_frame_rate"), int(s.get("bit_rate", 0) or 0) // 1000))
        elif s["codec_type"] == "audio":
            print("  audio #%d %s %s Hz %sch, %s kb/s" % (s["index"], s["codec_name"], s.get("sample_rate"), s.get("channels"),
                                                         int(s.get("bit_rate", 0) or 0) // 1000))


def grab(f, t, w=None):
    vf = ["-vf", "scale=%d:-2" % w] if w else []
    r = run(["ffmpeg", "-nostdin", "-v", "error", "-ss", "%.3f" % t, "-i", f, "-frames:v", "1"] + vf +
            ["-f", "image2pipe", "-vcodec", "png", "-"])
    import cv2
    if not r.stdout:
        return None
    return cv2.imdecode(np.frombuffer(r.stdout, np.uint8), cv2.IMREAD_COLOR)


def sheet(f, out, every, start=0.0, end=None, cols=8, tw=320):
    from PIL import Image, ImageDraw
    import cv2
    dur = float(json.loads(run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "json", f],
                               text=True).stdout)["format"]["duration"])
    end = min(end or dur, dur - 0.05)
    ts = list(np.arange(start, end, every))
    tiles = []
    for t in ts:
        img = grab(f, t, tw)
        if img is None:
            continue
        im = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        d = ImageDraw.Draw(im)
        m, s = divmod(int(t), 60)
        d.rectangle((0, 0, 62, 16), fill="black")
        d.text((3, 2), "%d:%02d" % (m, s), fill="yellow")
        tiles.append(im)
    th = tiles[0].height
    rows = math.ceil(len(tiles) / cols)
    sh = Image.new("RGB", (cols * tw, rows * th))
    for k, im in enumerate(tiles):
        sh.paste(im, ((k % cols) * tw, (k // cols) * th))
    sh.save(out, quality=85)
    print("sheet", out, len(tiles), "tiles", sh.size)


def pcm(f, ss, to, sr=16000):
    r = run(["ffmpeg", "-nostdin", "-v", "error", "-ss", "%.3f" % ss, "-to", "%.3f" % to, "-i", f, "-vn", "-ac", "1", "-ar",
             str(sr), "-f", "s16le", "-"])
    return np.frombuffer(r.stdout, np.int16).astype(np.float32) / 32768.0


def lufs(f, ss, to):
    r = run(["ffmpeg", "-nostdin", "-v", "info", "-ss", "%.3f" % ss, "-to", "%.3f" % to, "-i", f, "-vn", "-af",
             "ebur128=framelog=quiet", "-f", "null", "-"], text=True, errors="replace")
    i = lra = None
    for line in r.stderr.splitlines()[::-1]:
        line = line.strip()
        if i is None and line.startswith("I:"):
            i = float(line.split()[1])
        if lra is None and line.startswith("LRA:"):
            lra = float(line.split()[1])
    return i, lra


def flatness(x, sr=16000):
    if len(x) < 2048:
        return None
    hop, n = 512, 2048
    win = np.hanning(n)
    vals = []
    for k in range(0, len(x) - n, hop):
        p = np.abs(np.fft.rfft(x[k:k + n] * win)) ** 2 + 1e-12
        p = p[(np.fft.rfftfreq(n, 1 / sr) > 100) & (np.fft.rfftfreq(n, 1 / sr) < 6000)]
        vals.append(np.exp(np.mean(np.log(p))) / np.mean(p))
    return float(np.median(vals)) if vals else None


def audio(f, words, a, b, label=""):
    i, lra = lufs(f, a, b)
    x = pcm(f, a, b)
    w = int(0.05 * 16000)
    rms = np.sqrt(np.convolve(x ** 2, np.ones(w) / w, mode="valid")[::w] + 1e-12)
    db = 20 * np.log10(rms)
    print("%s span %.2f-%.2f: integrated %.1f LUFS, LRA %.1f LU; 50 ms RMS p10 %.1f dBFS (floor), p95 %.1f dBFS (speech peaks)"
          % (label, a, b, i if i is not None else float("nan"), lra if lra is not None else float("nan"),
             np.percentile(db, 10), np.percentile(db, 95)))
    if words and words != "-":
        ws = json.load(open(words, encoding="utf-8"))
        if isinstance(ws, dict) and "clips" in ws:      # transcribe.sh format: {"clips": [{"words": [{"w","start","end"}]}]}
            ws = [q for c in ws["clips"] for q in c.get("words", [])]
        elif isinstance(ws, dict):
            ws = ws.get("words", [])
        ws = [q for q in ws if "start" in q and "end" in q and a <= q["start"] <= b]
        gaps = [(p["end"], q["start"]) for p, q in zip(ws, ws[1:]) if q["start"] - p["end"] >= 0.30]
        fl = []
        for g0, g1 in gaps:
            v = flatness(x[int((g0 - a) * 16000):int((g1 - a) * 16000)])
            if v is not None:
                fl.append(v)
        if fl:
            print("  %d gaps >= 0.30 s between words: spectral flatness median %.2f (min %.2f, max %.2f); <0.15 = tonal (music)"
                  % (len(fl), np.median(fl), min(fl), max(fl)))
        else:
            print("  no word gaps >= 0.30 s in span")


def anchor(out, specs):
    import cv2
    from PIL import Image, ImageDraw
    # OpenCV 5 dropped the Haar cascades from the main build: use the repo's YuNet model (as workflows/face-frame.py does).
    yunet = str(pathlib.Path(__file__).resolve().parents[4] / "assets" / "models" / "face_detection_yunet_2023mar.onnx")

    class _Casc:
        def detectMultiScale(self, g, *_a, minSize=(40, 40)):
            img3 = cv2.cvtColor(g, cv2.COLOR_GRAY2BGR)
            det = cv2.FaceDetectorYN_create(yunet, "", (img3.shape[1], img3.shape[0]), score_threshold=0.6)
            _, faces = det.detect(img3)
            if faces is None:
                return []
            return [tuple(int(v) for v in f[:4]) for f in faces if f[2] >= minSize[0]]

    casc = _Casc()
    tiles = []
    for sp in specs:
        parts = sp.split("@")
        f, t, lab, sc = parts[:4]
        pick = parts[4] if len(parts) > 4 else "largest"   # largest | left | right | mid: which detected face to centre on
        img = grab(f, float(t))
        sc = float(sc)
        g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        mn = max(40, img.shape[0] // 25)
        fs = casc.detectMultiScale(g, 1.1, 5, minSize=(mn, mn))
        half = int(round(270 / sc))
        if len(fs):
            fs = sorted(fs, key=lambda r: r[0])
            if pick == "left":
                x, y, w, h = fs[0]
            elif pick == "right":
                x, y, w, h = fs[-1]
            elif pick == "mid":
                x, y, w, h = fs[len(fs) // 2]
            else:
                x, y, w, h = max(fs, key=lambda r: r[2] * r[3])
            cx, cy = x + w // 2, y + h // 2
            note = "face %dpx src, %dpx delivered" % (w, int(w * sc))
        else:
            cx, cy = img.shape[1] // 2, img.shape[0] // 2
            note = "no face found: centre crop"
        x0 = min(max(cx - half, 0), img.shape[1] - 2 * half)
        y0 = min(max(cy - half, 0), img.shape[0] - 2 * half)
        c = img[y0:y0 + 2 * half, x0:x0 + 2 * half]
        c = cv2.resize(c, (540, 540), interpolation=cv2.INTER_LANCZOS4)
        im = Image.fromarray(cv2.cvtColor(c, cv2.COLOR_BGR2RGB))
        d = ImageDraw.Draw(im)
        d.rectangle((0, 0, 540, 30), fill="black")
        d.text((6, 3), lab, fill="yellow")
        d.text((6, 16), "%s  x%.2f  t=%s" % (note, sc, t), fill="white")
        tiles.append(im)
    cols = 3
    rows = math.ceil(len(tiles) / cols)
    sh = Image.new("RGB", (cols * 540, rows * 540))
    for k, im in enumerate(tiles):
        sh.paste(im, ((k % cols) * 540, (k // cols) * 540))
    sh.save(out, quality=92)
    print("anchor sheet", out, len(tiles), "tiles")


if __name__ == "__main__":
    m = sys.argv[1]
    if m == "probe":
        for f in sys.argv[2:]:
            probe(f)
    elif m == "sheet":
        a = sys.argv[2:]
        sheet(a[0], a[1], float(a[2]), float(a[3]) if len(a) > 3 else 0.0, float(a[4]) if len(a) > 4 and a[4] != "-" else None,
              int(a[5]) if len(a) > 5 else 8, int(a[6]) if len(a) > 6 else 320)
    elif m == "audio":
        a = sys.argv[2:]
        audio(a[0], a[1], float(a[2]), float(a[3]), a[4] if len(a) > 4 else "")
    elif m == "anchor":
        anchor(sys.argv[2], sys.argv[3:])
