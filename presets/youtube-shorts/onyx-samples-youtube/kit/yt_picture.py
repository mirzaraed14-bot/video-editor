# /// script
# requires-python = ">=3.10"
# dependencies = ["opencv-python-headless", "numpy", "pillow"]
# ///
"""yt_picture.py: PASS 1 of a YouTube-look sample, driven by the job's spec (README § 3, § 4, § 6, § 7; PLAYBOOK § 5).

  uv run presets/youtube-shorts/onyx-samples-youtube/kit/yt_picture.py projects/<job> [--stills] [--base-1080] [--dir ig]

Reads `<job>/yt/spec.json` and writes the PICTURE track only (no captions, title, watermark or audio), 1080x1920 at the
spec's fps, to `<job>/yt/work/picture.mp4`, plus `<job>/yt/work/shots.json` (frame ranges + the whip cut list for
workflows/whip-slide.py). Shot kinds:
  A      the speaker: full-height 9:16 crop of the base (Topaz 4K base when present), face-tracked, linear push-in
  B      B-roll: a source clip retimed to the fps (speed > 1 for a time-lapse), centred on (cx, cy) or panned
  SPLIT  speaker on top (y 0 -> seam), B-roll below on a floating panel
  FIT    a source (or a `crop` box of it) fitted to the width over a blurred, darkened copy of itself; `fg_y` centres it
Spec keys: fps, frames, base, base_hq (optional, e.g. the Topaz 4K base), faces (json from yt_faces.py), broll_dir,
split {seam, bob_amp, bob_period}, shots [ {id, kind, f0, f1, ...} ], whip_dirs {shot id: "left"|"right"},
sticker (optional) {shot, matte, matte_first_base_frame, rise_start, settle, final_xy_out, height_out, angle},
grade (optional) {"A": {...}, "B": {...}}: a look per shot family (A = the speaker, also the SPLIT top; B = B-roll, FIT and the
SPLIT bottom), overridable per shot with "grade": {...}. Keys: "bw" (true: Rec.709 luma), "sat" (saturation x), "warm"
(+R / −B, e.g. 0.04), "contrast" (around mid-grey, e.g. 1.12), "black" (lift, e.g. 0.02). Built for the Instagram look
(a host whose own reels are black-and-white, with colour B-roll).
Frame ranges are [f0, f1) on the base cut's timeline; the shots must tile every frame. A B-roll `src` that is a bare
file name lives in broll_dir; one with a "/" is relative to the job folder.
"""
import json, math, os, subprocess, sys
import cv2, numpy as np
from PIL import Image, ImageDraw, ImageFont

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8")
    except Exception:
        pass

KIT = os.path.dirname(os.path.abspath(__file__))
W, H = 1080, 1920


def probe(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height",
                          "-of", "csv=p=0", path], capture_output=True, text=True).stdout.strip().split(",")
    return int(out[0]), int(out[1])


def src_fps(path):
    r = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=r_frame_rate", "-of", "csv=p=0", path],
                       capture_output=True, text=True).stdout.strip()
    n, _, d = r.partition("/")
    return float(n) / float(d or 1) if n else 0.0


class Reader:
    """Raw frames from ffmpeg: a section of a source at the comp fps. speed == 1 CONFORMS the source (every source frame
    becomes one output frame, a 25 or 30 fps clip plays at 0.96x or 0.8x: no dropped-frame judder, QA 2026-10-05);
    speed > 1 retimes (a time-lapse); a still image loops."""
    def __init__(self, path, src_in, n, fps, speed=1.0, alpha=False, skip=0):
        self.w, self.h = probe(path)
        self.c = 4 if alpha else 3
        if skip:                                  # frame-exact: decode from the start and drop `skip` frames
            src_in, n = 0.0, n + skip
        tail = ",scale=in_color_matrix=auto:in_range=auto:out_range=full"
        if path.lower().endswith((".png", ".jpg", ".jpeg")):
            inp, vf = ["-loop", "1", "-framerate", str(fps), "-i", path], "null" + tail
        else:
            sf = src_fps(path)
            if speed == 1 and 20 <= sf <= 32:
                vf = f"setpts=(PTS-STARTPTS)*{sf / fps:.6f}" + tail
                dur = n / sf + 0.5
            else:
                vf = f"setpts=(PTS-STARTPTS)/{speed},fps={fps}" + tail
                dur = n / fps * speed + 0.5
            inp = ["-ss", f"{src_in:.3f}", "-t", f"{dur:.3f}", "-i", path]
        cmd = ["ffmpeg", "-v", "error", *inp, "-vf", vf, "-fps_mode", "passthrough", "-frames:v", str(n),
               "-f", "rawvideo", "-pix_fmt", "rgba" if alpha else "rgb24", "-"]
        self.p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        self.last = None
        for _ in range(skip):
            self.p.stdout.read(self.w * self.h * self.c)

    def read(self):
        buf = self.p.stdout.read(self.w * self.h * self.c)
        if len(buf) == self.w * self.h * self.c:
            self.last = np.frombuffer(buf, np.uint8).reshape(self.h, self.w, self.c)
        return self.last

    def close(self):
        self.p.stdout.close(); self.p.wait()


def warp(img, k, x0, y0, out_w, out_h):
    M = np.float32([[k, 0, -x0 * k], [0, k, -y0 * k]])
    return cv2.warpAffine(img, M, (out_w, out_h), flags=cv2.INTER_CUBIC if k >= 1 else cv2.INTER_AREA, borderMode=cv2.BORDER_REFLECT)


def view(sw, sh, cx_px, cy_px, k, out_w, out_h, fx_out=0.5, fy_out=0.5):
    vw, vh = out_w / k, out_h / k
    return (min(max(cx_px - fx_out * vw, 0), max(sw - vw, 0)), min(max(cy_px - fy_out * vh, 0), max(sh - vh, 0)))


def ease_out(p):
    p = min(max(p, 0.0), 1.0)
    return 1 - (1 - p) ** 3


def make_sticker(height_px):
    """Anton's "!" glyph, flat red vertical gradient #C90506 -> #9A0204, no outline (README § 6)."""
    font = ImageFont.truetype(os.path.join(KIT, "fonts", "Anton-Regular.ttf"), 1000)
    l, t, r, b = font.getbbox("!")
    glyph = Image.new("L", (r - l + 20, b - t + 20), 0)
    ImageDraw.Draw(glyph).text((10 - l, 10 - t), "!", font=font, fill=255)
    gw, gh = glyph.size
    top, bot = np.array([0xC9, 0x05, 0x06]), np.array([0x9A, 0x02, 0x04])
    grad = np.stack([(top + (bot - top) * y / max(gh - 1, 1)) for y in range(gh)])[:, None, :].repeat(gw, 1).astype(np.uint8)
    im = Image.fromarray(np.dstack([grad, np.array(glyph)]), "RGBA")
    s = height_px / gh
    return im.resize((max(1, round(gw * s)), round(gh * s)), Image.LANCZOS)


def over(dst, src_rgba, x, y):
    h, w = dst.shape[:2]
    layer = cv2.warpAffine(src_rgba, np.float32([[1, 0, x], [0, 1, y]]), (w, h), flags=cv2.INTER_LINEAR,
                           borderMode=cv2.BORDER_CONSTANT, borderValue=(0, 0, 0, 0))
    a = layer[..., 3:4].astype(np.float32) / 255
    dst[:] = (dst.astype(np.float32) * (1 - a) + layer[..., :3].astype(np.float32) * a).astype(np.uint8)


def grade(img, g):
    """A simple per-frame look (see the docstring's "grade" keys). No-op when g is empty."""
    if not g:
        return img
    x = img.astype(np.float32) / 255
    y = x[..., 0] * 0.2126 + x[..., 1] * 0.7152 + x[..., 2] * 0.0722
    if g.get("bw"):
        x = np.repeat(y[..., None], 3, axis=2)
    elif "sat" in g:
        x = y[..., None] + (x - y[..., None]) * g["sat"]
    if g.get("warm"):
        x[..., 0] *= 1 + g["warm"]; x[..., 2] *= 1 - g["warm"]
    if g.get("contrast"):
        x = 0.5 + (x - 0.5) * g["contrast"]
    if g.get("black"):
        x = g["black"] + x * (1 - g["black"])
    return (np.clip(x, 0, 1) * 255 + 0.5).astype(np.uint8)


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    job = os.path.abspath(sys.argv[1])
    stills = "--stills" in sys.argv
    sub = sys.argv[sys.argv.index("--dir") + 1] if "--dir" in sys.argv else "yt"     # "ig" for an Instagram-look job (same picture engine)
    spec = json.load(open(os.path.join(job, sub, "spec.json"), encoding="utf-8"))
    P = lambda rel: rel if os.path.isabs(rel) else os.path.join(job, rel)
    fps, nframes = spec["fps"], spec["frames"]
    base = P(spec["base"])
    if spec.get("base_hq") and os.path.exists(P(spec["base_hq"])) and "--base-1080" not in sys.argv:
        base = P(spec["base_hq"])
    BW, BH = probe(base)
    S = BW / probe(P(spec["base"]))[0]           # faces were measured on the original base
    K0 = H / BH
    faces = json.load(open(P(spec["faces"]), encoding="utf-8")) if spec.get("faces") else {}
    split = {"seam": 1092, "bob_amp": 11, "bob_period": 1.25, **spec.get("split", {})}
    broll = P(spec.get("broll_dir", f"{sub}/assets/broll"))
    SRC = lambda src: P(src) if ("/" in src or "\\" in src) else os.path.join(broll, src)   # a bare name lives in broll_dir; a path is job-relative
    work = os.path.join(job, sub, "work")
    os.makedirs(os.path.join(work, "stills") if stills else work, exist_ok=True)

    fits = {}

    def face_track(key, n_abs, f0, f1):
        """The face centre (base px) at base frame n_abs: a straight-line fit of the detections INSIDE the shot [f0, f1)
        (a running median flipped between neighbours and shook the crop, QA 2026-10-05); the slope is capped at 2 px/frame."""
        if (key, f0, f1) not in fits:
            f = faces[key]; pf = f["per_frame"]
            ks = [int(k) for k in pf if f0 <= int(k) < f1] or [int(k) for k in pf]
            xs = np.array(ks, float); cx = np.array([pf[str(k)][0] + pf[str(k)][2] / 2 for k in ks])
            cy = np.median([pf[str(k)][1] + pf[str(k)][3] / 2 for k in ks])
            if len(ks) >= 3:
                b, a0 = np.polyfit(xs, cx, 1); b = float(np.clip(b, -2, 2)); a0 = float(np.mean(cx) - b * np.mean(xs))
            else:
                b, a0 = 0.0, float(np.mean(cx))
            fits[(key, f0, f1)] = (a0, b, float(cy))
        a0, b, cy = fits[(key, f0, f1)]
        return (a0 + b * n_abs) * S, cy * S

    def render_A(base_rgb, key, n_abs, fx_out, fy_out, z0, r, u, out_w, out_h, panel_h=None, rng=(0, 10 ** 9)):
        k = max(out_w / BW, (panel_h or out_h) / BH) * z0 * (1 + r * u)
        fx, fy = face_track(key, n_abs, *rng)
        x0, y0 = view(BW, BH, fx, fy, k, out_w, panel_h or out_h, fx_out, fy_out)
        return warp(base_rgb, k, x0, y0, out_w, out_h)

    def render_B(frame, d, u, out_w, out_h):
        sw, sh = frame.shape[1], frame.shape[0]
        k = max(out_w / sw, out_h / sh) * d.get("z0", 1.0) * (1 + d.get("r", 0.0) * u)
        if "pan" in d:
            p = u / d["_dur"] if d["_dur"] > 0 else 0
            p = p * p * (3 - 2 * p)
            cx = d["pan"][0] + (d["pan"][1] - d["pan"][0]) * p
        else:
            cx = d["cx"]
        cy = d.get("cy", 0.5)
        if "pan_y" in d:
            p = u / d["_dur"] if d["_dur"] > 0 else 0
            p = p * p * (3 - 2 * p)
            cy = d["pan_y"][0] + (d["pan_y"][1] - d["pan_y"][0]) * p
        x0, y0 = view(sw, sh, cx * sw, cy * sh, k, out_w, out_h)
        return warp(frame, k, x0, y0, out_w, out_h)

    shots = spec["shots"]
    plan = []
    for s in shots:
        s["_dur"] = (s["f1"] - s["f0"]) / fps
        if s.get("bottom"):
            s["bottom"]["_dur"] = s["_dur"]
        plan.append(dict(id=s["id"], kind=s["kind"], first=s["f0"], last=s["f1"] - 1, t0=round(s["f0"] / fps, 4), t1=round(s["f1"] / fps, 4),
                         whip_in=spec.get("whip_dirs", {}).get(s["id"])))
    assert plan[0]["first"] == 0 and plan[-1]["last"] == nframes - 1, "shots must cover every frame"
    for p, q in zip(plan, plan[1:]):
        assert p["last"] + 1 == q["first"], f"gap/overlap between {p['id']} and {q['id']}"
    json.dump(dict(fps=fps, frames=nframes, shots=plan, cuts=[dict(frame=p["first"], dir=p["whip_in"] or "left") for p in plan[1:]]),
              open(os.path.join(work, "shots.json"), "w", encoding="utf-8"), indent=1)

    st = spec.get("sticker")
    sticker_rot = np.array(make_sticker(st["height_out"]).rotate(st["angle"], resample=Image.BICUBIC, expand=True)) if st else None
    basep = subprocess.Popen(["ffmpeg", "-v", "error", "-i", base, "-vf", "scale=in_color_matrix=auto:out_range=full", "-f", "rawvideo",
                              "-pix_fmt", "rgb24", "-"], stdout=subprocess.PIPE)
    enc = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(fps), "-i", "-",
                            "-vf", "scale=out_color_matrix=bt709:out_range=tv,setparams=color_primaries=bt709:color_trc=bt709:colorspace=bt709",
                            "-c:v", "libx264", "-crf", "12", "-preset", "slow", "-pix_fmt", "yuv420p", os.path.join(work, "picture.mp4")],
                           stdin=subprocess.PIPE)
    for s in shots:
        a, b = s["f0"], s["f1"]
        rd = {}
        if s["kind"] in ("B", "FIT"):
            rd["main"] = Reader(SRC(s["src"]), s["src_in"], b - a, fps, s.get("speed", 1.0))
        if s["kind"] == "SPLIT":
            bt = s["bottom"]
            rd["bottom"] = Reader(SRC(bt["src"]), bt["src_in"], b - a, fps, bt.get("speed", 1.0))
        is_st = bool(st and st["shot"] == s["id"])
        if is_st:
            rd["matte"] = Reader(P(st["matte"]), 0, b - a, fps, alpha=True, skip=a - st["matte_first_base_frame"])
            k_start = K0 * s["z0"]
            x0s, y0s = view(BW, BH, *face_track(s["face"], a, a, b), k_start, W, H, s["fx_out"], s["fy_out"])
            sc = 1 / k_start
            stk = cv2.resize(sticker_rot, (max(1, round(sticker_rot.shape[1] * sc)), max(1, round(sticker_rot.shape[0] * sc))), interpolation=cv2.INTER_AREA)
        G = spec.get("grade", {})
        gA = {**G.get("A", {}), **(s.get("grade", {}) if s["kind"] == "A" else {})}
        gB = {**G.get("B", {}), **(s.get("grade", {}) if s["kind"] in ("B", "FIT") else {})}
        for n_abs in range(a, b):
            raw = basep.stdout.read(BW * BH * 3)
            base_rgb = np.frombuffer(raw, np.uint8).reshape(BH, BW, 3).copy()
            u = (n_abs - a) / fps
            if s["kind"] == "A":
                if is_st:
                    m = rd["matte"].read()
                    if n_abs >= st["rise_start"] and m is not None:
                        p = ease_out((n_abs - st["rise_start"] + 1) / (st["settle"] - st["rise_start"] + 1))
                        fxs = x0s + st["final_xy_out"][0] / k_start; fys = y0s + st["final_xy_out"][1] / k_start
                        ang = math.radians(st["angle"]); travel = 1.25 * st["height_out"] / k_start
                        cx = fxs + math.sin(ang) * travel * (1 - p); cy = fys + math.cos(ang) * travel * (1 - p)
                        comp = base_rgb.copy()
                        over(comp, stk, cx - stk.shape[1] / 2, cy - stk.shape[0] / 2)
                        ma = m[..., 3] if m.shape[1] == BW else cv2.resize(m[..., 3], (BW, BH), interpolation=cv2.INTER_CUBIC)
                        al = ma[..., None].astype(np.float32) / 255
                        base_rgb = (comp.astype(np.float32) * (1 - al) + base_rgb.astype(np.float32) * al).astype(np.uint8)
                out = grade(render_A(base_rgb, s["face"], n_abs, s["fx_out"], s["fy_out"], s["z0"], s["r"], u, W, H, rng=(a, b)), gA)
            elif s["kind"] == "B":
                out = grade(render_B(rd["main"].read(), s, u, W, H), gB)
            elif s["kind"] == "FIT":
                fr = rd["main"].read()
                bg = cv2.GaussianBlur(render_B(fr, dict(cx=0.5, cy=0.5, z0=1.0, r=0.0, _dur=1), 0, W, H), (0, 0), 28)
                out = (bg.astype(np.float32) * s.get("bg_dim", 0.5)).astype(np.uint8)
                if s.get("crop"):                  # fit only this box of the source (fractions x0, y0, x1, y1)
                    cx0, cy0, cx1, cy1 = s["crop"]
                    fr = fr[int(cy0 * fr.shape[0]):int(cy1 * fr.shape[0]), int(cx0 * fr.shape[1]):int(cx1 * fr.shape[1])]
                kf = W / fr.shape[1] * s["z0"] * (1 + s["r"] * u)
                fw, fh = int(round(fr.shape[1] * kf)), int(round(fr.shape[0] * kf))
                fg = cv2.resize(np.ascontiguousarray(fr), (fw, fh), interpolation=cv2.INTER_CUBIC if kf >= 1 else cv2.INTER_AREA)
                x, y = (W - fw) // 2, (int(s["fg_y"]) - fh // 2) if s.get("fg_y") else (H - fh) // 2
                dx0, dy0 = max(0, x), max(0, y); sx0, sy0 = dx0 - x, dy0 - y
                ww, hh = min(W - dx0, fw - sx0), min(H - dy0, fh - sy0)
                out[dy0:dy0 + hh, dx0:dx0 + ww] = fg[sy0:sy0 + hh, sx0:sx0 + ww]
                out = grade(out, gB)
            elif s["kind"] == "SPLIT":
                t = s["top"]
                out = grade(render_A(base_rgb, t["face"], n_abs, 0.5, t["fy_out"], t["z0"], t["r"], u, W, H, panel_h=split["seam"] + split["bob_amp"] + 4, rng=(a, b)),
                            {**G.get("A", {}), **t.get("grade", {})})
                seam = int(round(split["seam"] + split["bob_amp"] * math.sin(2 * math.pi * u / split["bob_period"])))
                panel = grade(render_B(rd["bottom"].read(), s["bottom"], u, W, H - (split["seam"] - split["bob_amp"])),
                              {**G.get("B", {}), **s["bottom"].get("grade", {})})
                out[seam:] = panel[:H - seam]
            enc.stdin.write(np.ascontiguousarray(out).tobytes())
            if stills and n_abs == (a + b) // 2:
                Image.fromarray(out).resize((360, 640)).save(os.path.join(work, "stills", f"{s['id']}.jpg"), quality=85)
        for r_ in rd.values():
            r_.close()
        print(f"  {s['id']} {s['kind']:5s} frames {a}-{b - 1} ({(b - a) / fps:.2f} s)")
    basep.stdout.close(); basep.wait()
    enc.stdin.close(); enc.wait()
    print(f"wrote {nframes} frames -> {os.path.join(work, 'picture.mp4')}  (base: {os.path.basename(base)}, {BW}x{BH})")


if __name__ == "__main__":
    main()
