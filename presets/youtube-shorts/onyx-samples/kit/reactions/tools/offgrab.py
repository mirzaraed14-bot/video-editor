#!/usr/bin/env python3
"""offgrab.py: OFFLINE frame grabs of a placed Premiere sequence, rebuilt from a by-name DOM readback (dump.py writes it
without touching the active sequence), so QC never moves Affan's playhead or switches his timeline (2026-11-14: he edits
his AW Shorts in the same Premiere project while the reaction batch runs).

  python offgrab.py <job dir> [--dump work/dump-layout.json] [--grid 1.0] [--times 1.5,2,7.25] [--times-file f.txt]
                    [--edges] [--from T] [--to T] [--out work/offgrab] [--workers 8] [--sheet] [--compare <dir>]

  --grid S      one frame every S seconds over [from, to)          --edges  -2/0/+2 frames at every clip start and end
  --compare D   for every D/grab-TTTT.TT.png (a real Premiere grab) render the same time and report the difference
                (proof that this compositor matches Premiere for that job's layout); writes side-by-side pairs
  --sheet       contact sheets (32 per sheet) into <out>/sheets/

Model (Premiere's, for these timelines): tracks V1..Vn bottom to top; a muted track or a disabled clip is skipped; source
time = in + (t - start) * speed (speed from the readback's in/out vs start/end); Motion crop (percent of the source edges,
applied before scaling) -> scale about the anchor (Scale %, or Scale Width x Scale when not uniform) -> anchor placed at
Position (fractions of the frame); straight alpha-over (ProRes 4444 alpha kept). Keyframed Motion/Opacity, rotation and any
effect besides Opacity|Motion are NOT modelled: such clips are listed in <out>/REPORT.txt so nobody trusts those frames.
Frame index: sequence frame f = floor(t * fps) (the frame containing t, as Premiere shows it); source frame n = floor(src_t * src_fps + 1e-3), decoded exactly (seek a
third of a frame before its pts)."""
import argparse, concurrent.futures as cf, glob, json, math, os, re, subprocess, sys
from PIL import Image, ImageDraw, ImageFont

_probe = {}


def probe(path):
    if path not in _probe:
        r = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
                            "stream=width,height,r_frame_rate,start_time", "-of", "json", path],
                           capture_output=True, text=True)
        s = json.loads(r.stdout)["streams"][0]
        num, den = s["r_frame_rate"].split("/")
        _probe[path] = dict(w=int(s["width"]), h=int(s["height"]), fps=float(num) / float(den),
                            st=float(s.get("start_time") or 0.0))
    return _probe[path]


def decode(path, src_t):
    p = probe(path)
    n = max(0, math.floor(src_t * p["fps"] + 1e-3) + int(os.environ.get("OG_SRC_OFFSET", "0")))
    ss = p["st"] + n / p["fps"] - 0.33 / p["fps"]
    r = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{max(ss, 0):.6f}", "-i", path, "-frames:v", "1",
                        "-f", "rawvideo", "-pix_fmt", "rgba", "-"], capture_output=True)
    need = p["w"] * p["h"] * 4
    if len(r.stdout) < need:
        return None
    return Image.frombuffer("RGBA", (p["w"], p["h"]), r.stdout[:need], "raw", "RGBA", 0, 1)


def clip_at(track, t, eps):
    for c in track["clips"]:
        if c["s"] - eps <= t < c["e"] - eps:
            return c
    return None


UNMODELLED = ("Position", "Scale", "Scale Width", "Rotation", "Anchor Point", "Crop Left", "Crop Top",
              "Crop Right", "Crop Bottom", "Opacity")


def warnings_for(c):
    m, w = c.get("m") or {}, []
    for k in UNMODELLED:
        if m.get(k + "_kf"):
            w.append(f"{k} keyframed")
    if abs(float(m.get("Rotation", 0) or 0)) > 1e-6:
        w.append("rotation")
    if m.get("Blend Mode") not in (None, 0):
        w.append(f"blend mode {m.get('Blend Mode')}")
    fx = [f for f in str(m.get("fx", "Opacity|Motion")).split("|") if f]
    extra = [f for f in fx if f not in ("Opacity", "Motion")]
    if extra:
        w.append("effects " + "+".join(extra))
    return w


FIT = {}          # name substring -> "fit" (Scale to Frame Size: min(W/w, H/h)) or a number; from --fit / OG_FIT


def fit_factor(c, w, h, W, H):
    if c.get("fit") is not None:                      # a readback that knows the clip's Scale to Frame Size state
        return min(W / w, H / h) if c["fit"] else 1.0
    for key, v in FIT.items():
        if key in c.get("n", "") or key in c.get("p", ""):
            return min(W / w, H / h) if v == "fit" else float(v)
    return 1.0


def place(canvas, im, c, W, H):
    m = c.get("m") or {}
    w, h = im.size
    L = float(m.get("Crop Left", 0) or 0) / 100 * w
    T = float(m.get("Crop Top", 0) or 0) / 100 * h
    R = w - float(m.get("Crop Right", 0) or 0) / 100 * w
    B = h - float(m.get("Crop Bottom", 0) or 0) / 100 * h
    if R - L < 1 or B - T < 1:
        return
    sy = float(m.get("Scale", 100) or 100) / 100
    sx = sy if m.get("Uniform Scale", True) else float(m.get("Scale Width", 100) or 100) / 100
    k = fit_factor(c, w, h, W, H)
    sx, sy = sx * k, sy * k
    ax, ay = (m.get("Anchor Point") or [0.5, 0.5])
    px, py = (m.get("Position") or [0.5, 0.5])
    x0 = px * W + (L - ax * w) * sx
    y0 = py * H + (T - ay * h) * sy
    sub = im.crop((round(L), round(T), round(R), round(B)))
    tw, th = max(1, round(sub.width * sx)), max(1, round(sub.height * sy))
    if (tw, th) != sub.size:
        sub = sub.resize((tw, th), Image.BILINEAR)
    op = float(m.get("Opacity", 100) or 100) / 100
    if op < 0.999:
        sub.putalpha(sub.getchannel("A").point(lambda v: round(v * op)))
    X, Y = round(x0), round(y0)
    cx0, cy0 = max(0, -X), max(0, -Y)
    cx1, cy1 = min(sub.width, W - X), min(sub.height, H - Y)
    if cx1 <= cx0 or cy1 <= cy0:
        return
    canvas.alpha_composite(sub.crop((cx0, cy0, cx1, cy1)), dest=(X + cx0, Y + cy0))


def render(seq, t):
    W, H, fps = seq["w"], seq["h"], float(seq["fps"])
    f = math.floor(t * fps + 1e-4)       # Premiere shows the frame whose span CONTAINS t (floor), proven 2026-11-14 at cuts
    tq = f / fps
    eps = 0.25 / fps
    canvas = Image.new("RGBA", (W, H), (0, 0, 0, 255))
    used, warn = [], []
    for k, tr in enumerate(seq["v"]):
        if tr.get("muted"):
            continue
        c = clip_at(tr, tq, eps)
        if not c or c.get("d"):
            continue
        dur = c["e"] - c["s"]
        src = c.get("o", c["i"] + dur) - c["i"]
        speed = src / dur if dur > 0 else 1.0
        if abs(speed - 1) < 0.002:
            speed = 1.0
        im = decode(c["p"], c["i"] + (tq - c["s"]) * speed)
        if im is None:
            warn.append(f"V{k + 1} {c['n']}: no frame decoded")
            continue
        place(canvas, im, c, W, H)
        used.append(f"V{k + 1}:{c['n']}")
        warn += [f"V{k + 1} {c['n']}: {x}" for x in warnings_for(c)]
    return canvas.convert("RGB"), tq, used, warn


def edge_times(seq):
    fps, out = float(seq["fps"]), set()
    last = round(seq["end"] * fps)
    for tr in seq["v"]:
        for c in tr["clips"]:
            for edge in (c["s"], c["e"]):
                f = round(edge * fps)
                for d in (-2, 0, 2):
                    if 0 <= f + d < last:
                        out.add((f + d) / fps)
    return sorted(out)


def sheet(items, out_dir, per=32, cols=8):
    os.makedirs(out_dir, exist_ok=True)
    tw, th = 216, 384
    try:
        font = ImageFont.truetype("arial.ttf", 18)
    except Exception:
        font = ImageFont.load_default()
    names = []
    for k in range(0, len(items), per):
        chunk = items[k:k + per]
        rows = math.ceil(len(chunk) / cols)
        sh = Image.new("RGB", (cols * tw, rows * (th + 22)), (24, 24, 24))
        d = ImageDraw.Draw(sh)
        for j, (t, p) in enumerate(chunk):
            im = Image.open(p).convert("RGB").resize((tw, th))
            x, y = (j % cols) * tw, (j // cols) * (th + 22)
            sh.paste(im, (x, y + 22))
            d.text((x + 4, y + 2), f"{t:.2f}", fill=(255, 210, 0), font=font)
        n = os.path.join(out_dir, f"sheet-{k // per:02d}.jpg")
        sh.save(n, quality=85)
        names.append(n)
    return names


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("job")
    ap.add_argument("--dump", default="work/dump-layout.json")
    ap.add_argument("--grid", type=float)
    ap.add_argument("--times")
    ap.add_argument("--times-file")
    ap.add_argument("--edges", action="store_true")
    ap.add_argument("--from", dest="t0", type=float, default=0.0)
    ap.add_argument("--to", dest="t1", type=float)
    ap.add_argument("--out", default="work/offgrab")
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--sheet", action="store_true")
    ap.add_argument("--compare")
    ap.add_argument("--fit", default=os.environ.get("OG_FIT", ""),
                    help="name=fit|factor[,name=...]: scale-to-frame-size per source (until the readback carries it)")
    ap.add_argument("--monitor", default="1814,124,2454,1260",
                    help="program-monitor box inside a 2576x1408 window grab (apply.py grabs are window screenshots)")
    a = ap.parse_args()
    for kv in [x for x in a.fit.split(",") if "=" in x]:
        k_, v_ = kv.split("=", 1)
        FIT[k_.strip()] = v_.strip()
    dump = json.load(open(os.path.join(a.job, a.dump), encoding="utf-8"))
    seq = dump[0] if isinstance(dump, list) else dump
    out = os.path.join(a.job, a.out)
    os.makedirs(out, exist_ok=True)
    t1 = a.t1 if a.t1 is not None else seq["end"]
    ts = set()
    if a.grid:
        k = 0
        while a.t0 + k * a.grid < t1 - 1e-9:
            ts.add(round(a.t0 + k * a.grid, 4))
            k += 1
    if a.times:
        ts |= {float(x) for x in a.times.split(",") if x.strip()}
    if a.times_file:
        ts |= {float(x) for x in re.findall(r"[-+]?\d+(?:\.\d+)?", open(a.times_file).read())}
    if a.edges:
        ts |= {t for t in edge_times(seq) if a.t0 - 1e-9 <= t < t1}
    pairs = []
    if a.compare:
        for g in sorted(glob.glob(os.path.join(a.compare, "grab-*.png"))):
            mm = re.search(r"grab-(\d+(?:\.\d+)?)\.png$", g)
            if mm:
                pairs.append((float(mm.group(1)), g))
                ts.add(float(mm.group(1)))
    ts = sorted(ts)
    if not ts:
        sys.exit("no times: give --grid, --times, --times-file, --edges or --compare")
    report = {}

    def one(t):
        img, tq, used, warn = render(seq, t)
        p = os.path.join(out, f"og-{t:08.3f}.png")
        img.save(p)
        return t, p, used, warn

    with cf.ThreadPoolExecutor(a.workers) as ex:
        for t, p, used, warn in ex.map(one, ts):
            report[t] = (p, used, warn)
    warns = sorted({w for (_, _, ws) in report.values() for w in ws})
    with open(os.path.join(out, "REPORT.txt"), "w", encoding="utf-8") as fh:
        fh.write(f"{seq['name']}  {len(ts)} frames  dump {a.dump}\n")
        fh.write("UNMODELLED (do not trust these layers in the frames):\n")
        fh.write(("\n".join("  " + w for w in warns) or "  none") + "\n")
        for t in ts:
            fh.write(f"{t:9.3f}  " + "  ".join(report[t][1]) + "\n")
    print(f"{len(ts)} frames -> {out}  (unmodelled: {len(warns)})")
    for w in warns[:20]:
        print("  UNMODELLED", w)
    if a.sheet:
        for n in sheet([(t, report[t][0]) for t in ts], os.path.join(out, "sheets")):
            print("  sheet", n)
    if pairs:
        cmp_dir = os.path.join(out, "compare")
        os.makedirs(cmp_dir, exist_ok=True)
        rows = []
        for t, g in pairs:
            A = Image.open(report[t][0]).convert("RGB")
            Bm = Image.open(g).convert("RGB")
            if Bm.size == (2576, 1408):                       # a window screenshot: cut the program monitor out
                Bm = Bm.crop(tuple(int(v) for v in a.monitor.split(",")))
            if Bm.size != A.size:
                Bm = Bm.resize(A.size, Image.LANCZOS)
            al = A.convert("L").resize((270, 480)).load()
            bl = Bm.convert("L").resize((270, 480)).load()
            diffs = sorted(abs(al[x, y] - bl[x, y]) for y in range(480) for x in range(270))
            mad = sum(diffs) / len(diffs)
            rows.append((t, mad, diffs[int(0.99 * len(diffs))], sum(1 for d in diffs if d > 48) / len(diffs)))
            side = Image.new("RGB", (1080, 960))
            side.paste(A.resize((540, 960)), (0, 0))
            side.paste(Bm.resize((540, 960)), (540, 0))
            side.save(os.path.join(cmp_dir, f"pair-{t:08.3f}.jpg"), quality=80)
        rows.sort(key=lambda r: -r[1])
        with open(os.path.join(out, "COMPARE.txt"), "w") as fh:
            fh.write("t  MAD(0-255, 270x480 luma)  p99  share>48   (left = offline, right = Premiere)\n")
            for r in rows:
                fh.write(f"{r[0]:9.3f}  {r[1]:6.2f}  {r[2]:4d}  {r[3]:.4f}\n")
        mads = sorted(r[1] for r in rows)
        print(f"compare {len(rows)} grabs: MAD median {mads[len(mads) // 2]:.2f}, max {rows[0][1]:.2f} at "
              f"{rows[0][0]:.2f}; share>48 max {max(r[3] for r in rows):.4f}  (pairs in {cmp_dir})")


if __name__ == "__main__":
    main()
