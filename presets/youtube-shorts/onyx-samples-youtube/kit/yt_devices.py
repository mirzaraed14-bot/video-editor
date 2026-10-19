"""yt_devices.py: the batch-3 picture devices of the YouTube look, drawn INTO the picture by yt_picture.py (so they travel with
the whip), from `projects/_onyx-batch3-2026-10/STYLE-RESEARCH.md` § D1, D2, D4, D6 (Shawn Ryan's evidence Shorts, 2026-10-14).

  Doc          the DOC shot: a still "receipt" (an article / post screenshot, a chart image, a thumbnail) as a card over a blurred,
               darkened plate of itself, tilted, pushed in on its key line, with a highlighter that sweeps the line on the spoken phrase;
               a `stack` of 2-3 cards fans 40 px / 3 deg per layer and a later layer can slap in on its own word.
  draw_marks   hand-drawn annotations (red circle, box, underline, arrow) that draw on around a box and stay to the cut.
  draw_chart   a line or bar chart with dated labels that draws on, its value counting up to the spoken number.
  apply_fx     one story effect (flicker, shake, freeze).
The spec keys and their numbers are documented in yt_picture.py's docstring and the preset README § 13. All output numbers are px on
the 1080x1920 frame; all times are seconds on the cut's timeline (the clock of audio.sfx and the transcript).
"""
import math, os
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

KIT = os.path.dirname(os.path.abspath(__file__))
W, H = 1080, 1920
NAMED = {"red": "#E70A24", "blue": "#3FA9F5", "yellow": "#F5DC0B", "gold": "#F6B412", "white": "#FFFFFF", "black": "#0E0E0E"}
SS = 3                                                    # stroke supersampling


def rgb(c):
    if isinstance(c, (list, tuple)):
        return tuple(int(v) for v in c[:3])
    c = NAMED.get(c, c).lstrip("#")
    return tuple(int(c[i:i + 2], 16) for i in (0, 2, 4))


def clamp01(x):
    return min(max(float(x), 0.0), 1.0)


def inout2(p):                                            # GSAP power2.inOut
    p = clamp01(p)
    return 2 * p * p if p < 0.5 else 1 - (-2 * p + 2) ** 2 / 2


def out3(p):                                              # power3.out
    p = clamp01(p)
    return 1 - (1 - p) ** 3


def a3(a):
    """A 2-D float alpha as 3 channels (numpy's (h, w, 1) broadcasting is ~5x slower than same-shape arrays)."""
    a = np.ascontiguousarray(a, np.float32)
    return cv2.merge([a, a, a])


def smooth(e0, e1, x):
    u = np.clip((np.asarray(x, np.float32) - e0) / (e1 - e0), 0, 1)
    return u * u * (3 - 2 * u)


# ---------------------------------------------------------------- strokes (marks, chart lines)

def stroke_alpha(strokes, x0, y0, w, h):
    """Union of variable-width round-capped strokes as a float alpha (h, w), supersampled x3 (no seams between segments)."""
    mask = np.zeros((h * SS, w * SS), np.uint8)
    for p, wd in strokes:
        if not len(p):
            continue
        q = np.round((np.asarray(p, np.float64) - (x0, y0)) * SS).astype(np.int64)
        if len(q) == 1:
            cv2.circle(mask, (int(q[0, 0]), int(q[0, 1])), max(1, int(round(wd[0] * SS / 2))), 255, -1)
            continue
        for i in range(len(q) - 1):
            cv2.line(mask, (int(q[i, 0]), int(q[i, 1])), (int(q[i + 1, 0]), int(q[i + 1, 1])), 255, max(1, int(round(wd[i] * SS))), cv2.LINE_8)
    return cv2.resize(mask, (w, h), interpolation=cv2.INTER_AREA).astype(np.float32) / 255


def draw_strokes(img, strokes, color, shadow=0.42, glow=0.0, glow_sigma=6.0, op=1.0):
    """Paint strokes [(pts (N,2) px, widths (N,))] onto img (uint8, in place) over a soft dark shadow (and an optional glow)."""
    strokes = [(np.asarray(p, np.float64), np.asarray(wd, np.float64)) for p, wd in strokes if len(p)]
    if not strokes:
        return
    allp = np.concatenate([p for p, _ in strokes])
    m = max(float(wd.max()) for _, wd in strokes) + 3 * max(glow_sigma if glow else 0, 3) + 4
    x0, y0 = int(max(0, math.floor(allp[:, 0].min() - m))), int(max(0, math.floor(allp[:, 1].min() - m)))
    x1, y1 = int(min(img.shape[1], math.ceil(allp[:, 0].max() + m))), int(min(img.shape[0], math.ceil(allp[:, 1].max() + m)))
    if x1 <= x0 or y1 <= y0:
        return
    a = stroke_alpha(strokes, x0, y0, x1 - x0, y1 - y0) * op
    reg = img[y0:y1, x0:x1].astype(np.float32)
    col = np.full(reg.shape, color, np.float32)
    if shadow:
        sh = cv2.GaussianBlur(a, (0, 0), 3.0)
        sh = np.roll(sh, 2, axis=0); sh[:2] = 0
        reg *= a3(1 - shadow * sh)
    if glow:
        g = a3(np.clip(cv2.GaussianBlur(a, (0, 0), glow_sigma) * glow, 0, 1))
        reg = reg * (1 - g) + col * g
    A = a3(a)
    reg = reg * (1 - A) + col * A
    img[y0:y1, x0:x1] = cv2.convertScaleAbs(reg)


def bez(p0, p1, p2, n):
    t = np.linspace(0, 1, max(2, int(n)))[:, None]
    return (1 - t) ** 2 * np.asarray(p0, float) + 2 * (1 - t) * t * np.asarray(p1, float) + t ** 2 * np.asarray(p2, float)


def taper(n, w):
    """Marker pressure: lands at 62 % width, full by 10 % of the stroke, lifts to 70 % over the last 14 %."""
    s = np.linspace(0, 1, n)
    return w * (0.62 + 0.38 * smooth(0, 0.10, s)) * (1 - 0.30 * smooth(0.86, 1.0, s))


def partial(path, wd, p):
    """The first fraction p (by arc length) of a stroke."""
    if p >= 1:
        return path, wd
    if p <= 0 or len(path) < 2:
        return path[:0], wd[:0]
    seg = np.hypot(*np.diff(path, axis=0).T)
    cum = np.concatenate([[0.0], np.cumsum(seg)])
    L = cum[-1] * p
    k = int(np.searchsorted(cum, L))
    k = max(1, min(k, len(path) - 1))
    f = (L - cum[k - 1]) / max(seg[k - 1], 1e-9)
    tip = path[k - 1] + (path[k] - path[k - 1]) * f
    return np.vstack([path[:k], tip]), np.concatenate([wd[:k], [wd[k - 1]]])


ARROW_FROM = {"left": (-1, 0), "right": (1, 0), "top": (0, -1), "bottom": (0, 1), "top-left": (-1, -1), "top-right": (1, -1),
              "bottom-left": (-1, 1), "bottom-right": (1, 1)}


def mark_geometry(m, hw, hh, seed):
    """Stroke paths (px, around a box of half-size hw x hh centred on 0, unrotated) for one mark: [(path, is_head)]."""
    rng = np.random.default_rng(seed)
    kind = m.get("type", "circle")
    if kind == "circle":
        pad = m.get("pad", 14)
        rx, ry = hw * 1.30 + pad, hh * 1.42 + pad
        th0 = -2.25 + rng.uniform(-0.25, 0.25)
        th = np.linspace(th0, th0 + 2 * np.pi * 1.10, 260)         # 1.1 turns: the pen closes past its start
        q = (th - th0) / (2 * np.pi)
        wob = 1 + 0.035 * np.sin(2 * th + rng.uniform(0, 2 * np.pi)) + 0.02 * np.sin(3 * th + rng.uniform(0, 2 * np.pi))
        grow = 1 + 0.07 * q                                          # and spirals out, so the overlap passes outside the start
        x, y = rx * wob * grow * np.cos(th), ry * wob * grow * np.sin(th)
        r = rng.uniform(-0.07, 0.07)
        return [(np.stack([x * np.cos(r) - y * np.sin(r), x * np.sin(r) + y * np.cos(r)], 1), False)]
    if kind == "box":
        p = m.get("pad", 12)
        X0, Y0, X1, Y1 = -hw - p, -hh - p, hw + p, hh + p
        c = [(X0, Y0), (X1, Y0), (X1, Y1), (X0, Y1)]
        c = [(x + rng.normal(0, 2.0), y + rng.normal(0, 2.0)) for x, y in c]
        c += [(c[0][0] + rng.normal(0, 1.5), c[0][1] + rng.normal(0, 1.5)), (c[0][0] + 0.10 * (X1 - X0), c[0][1] + rng.normal(0, 1.5) - 2)]
        segs = []
        for a, b in zip(c, c[1:]):
            L = math.hypot(b[0] - a[0], b[1] - a[1]) or 1.0
            nx, ny = -(b[1] - a[1]) / L, (b[0] - a[0]) / L
            bow = rng.uniform(-1, 1) * min(6.0, 0.02 * L)
            segs.append(bez(a, ((a[0] + b[0]) / 2 + nx * bow, (a[1] + b[1]) / 2 + ny * bow), b, max(8, L / 6))[:-1])
        return [(np.vstack(segs + [np.array([c[-1]])]), False)]
    if kind == "underline":
        y = hh + m.get("gap", 12)
        path = bez((-hw - 6, y + 3), (rng.uniform(-0.15, 0.15) * hw, y + 9), (hw + 10, y - 5), 90)
        path[:, 1] += 1.2 * np.sin(np.linspace(0, 3 * np.pi, len(path)) + rng.uniform(0, 6))
        return [(path, False)]
    if kind == "arrow":
        d = np.array(ARROW_FROM[m.get("from", "bottom-left")], float); d /= np.linalg.norm(d)
        te = min(hw / abs(d[0]) if d[0] else 1e9, hh / abs(d[1]) if d[1] else 1e9)
        end = d * (te + m.get("gap", 18))
        L = m.get("len", float(np.clip(max(hw, hh) + 140, 170, 380)))
        start = end + d * L
        ctrl = (start + end) / 2 + np.array([-d[1], d[0]]) * 0.20 * L * m.get("bend", 1)
        path = bez(start, ctrl, end, 90)
        tan = (end - ctrl) / np.linalg.norm(end - ctrl)                # the head follows the path's END TANGENT (CLAUDE.md craft rule)
        hl, ang = m.get("head", 38), math.radians(27)
        rot = lambda v, a: np.array([v[0] * math.cos(a) - v[1] * math.sin(a), v[0] * math.sin(a) + v[1] * math.cos(a)])
        h1, h2 = end - rot(tan, ang) * hl, end - rot(tan, -ang) * hl
        return [(path, False), (np.linspace(end, h1, 14), True), (np.linspace(end, h2, 14), True)]
    raise SystemExit(f"yt_devices: unknown mark type {kind!r} (circle | box | underline | arrow)")


def mark_place(m, xf):
    """Box centre (output px), half-sizes and rotation of a mark: "space": "frame" = box in output px, else source-file fractions
    mapped through the shot's transform xf = (A 2x2, b 2, (source w, source h))."""
    bx, by, bw, bh = m["box"]
    if m.get("space", "src" if xf is not None else "frame") == "frame":
        return np.array([bx + bw / 2, by + bh / 2]), bw / 2, bh / 2, 0.0
    if xf is None:
        raise SystemExit(f"yt_devices: a source-space mark needs a B, FIT or DOC shot (use \"space\": \"frame\" with an output-px box)")
    if max(abs(v) for v in m["box"]) > 1.5:
        raise SystemExit(f"yt_devices: mark box {m['box']} looks like px: source-space boxes are fractions of the source file (or set \"space\": \"frame\")")
    A, b, (sw, sh) = xf
    c = A @ np.array([(bx + bw / 2) * sw, (by + bh / 2) * sh]) + b
    s = math.sqrt(abs(np.linalg.det(A)))
    return c, s * bw * sw / 2, s * bh * sh / 2, math.atan2(A[1, 0], A[0, 0])


def draw_marks(img, marks, t, xf, sid):
    """Every mark of a shot at time t: it draws on over `dur` (power2.inOut) from `t` and holds to the cut (or `until`)."""
    for i, m in enumerate(marks):
        if t < m["t"] or (m.get("until") is not None and t >= m["until"]):
            continue
        p = inout2((t - m["t"]) / m.get("dur", 0.35))
        c, hw, hh, phi = mark_place(m, xf)
        w = m.get("width", 8)
        seed = (int.from_bytes(f"{sid}:{i}".encode(), "little") % (2 ** 32)) if m.get("seed") is None else m["seed"]   # stable across runs
        R = np.array([[math.cos(phi), -math.sin(phi)], [math.sin(phi), math.cos(phi)]])
        geo = mark_geometry(m, hw, hh, seed)
        has_head = any(hd for _, hd in geo)
        strokes = []
        for path, is_head in geo:
            pts = path @ R.T + c
            wd = np.full(len(pts), w * 0.9) * (0.75 + 0.25 * smooth(0, 0.3, np.linspace(0, 1, len(pts)))) if is_head else taper(len(pts), w)
            pp = clamp01((p - 0.80) / 0.20) if is_head else (clamp01(p / 0.80) if has_head else p)
            strokes.append(partial(pts, wd, pp))
        draw_strokes(img, strokes, rgb(m.get("color", "red")), shadow=m.get("shadow", 0.42))


# ---------------------------------------------------------------- text (chart labels and chips)

_FONTS, _TXT = {}, {}
FONT = {"mono": "IBMPlexMono-SemiBold.ttf", "mono-med": "IBMPlexMono-Medium.ttf"}


def font(name, size):
    k = (name, size)
    if k not in _FONTS:
        _FONTS[k] = ImageFont.truetype(os.path.join(KIT, "fonts", FONT[name]), size)
    return _FONTS[k]


def label(text, name, size, color=(255, 255, 255), bg=None, bg_a=0.9, pad=(16, 9), radius=8, track=0.04):
    """Text (optionally on a rounded chip) as a straight-alpha float RGBA image; cached."""
    k = (text, name, size, tuple(color), bg and tuple(bg), bg_a, pad, radius, track)
    if k in _TXT:
        return _TXT[k]
    f = font(name, size)
    asc, desc = f.getmetrics()
    adv = [f.getlength(ch) for ch in text]
    tw = sum(adv) + track * size * max(0, len(text) - 1)
    px, py = pad if bg else (2, 2)
    w, h = int(math.ceil(tw)) + 2 * px, asc + desc + 2 * py
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    if bg:
        d.rounded_rectangle([0, 0, w - 1, h - 1], radius=radius, fill=tuple(bg) + (int(255 * bg_a),))
    x = px
    for ch, a in zip(text, adv):
        d.text((x, py), ch, font=f, fill=tuple(color) + (255,))
        x += a + track * size
    out = np.array(im, np.float32) / 255
    _TXT[k] = out
    return out


def blit(img, rgba, x, y, op=1.0):
    """Straight-alpha float RGBA onto uint8 img at (x, y) top-left (rounded), in place."""
    x, y = int(round(x)), int(round(y))
    h, w = rgba.shape[:2]
    X0, Y0, X1, Y1 = max(0, x), max(0, y), min(img.shape[1], x + w), min(img.shape[0], y + h)
    if X1 <= X0 or Y1 <= Y0 or op <= 0:
        return
    s = rgba[Y0 - y:Y1 - y, X0 - x:X1 - x]
    a = a3(s[..., 3] * op)
    reg = img[Y0:Y1, X0:X1].astype(np.float32)
    img[Y0:Y1, X0:X1] = cv2.convertScaleAbs(reg * (1 - a) + np.ascontiguousarray(s[..., :3]) * 255 * a)


def rounded_mask(h, w, r, ss=3):
    """Anti-aliased rounded-rectangle alpha (float 0-1)."""
    h, w = max(1, int(h)), max(1, int(w))
    R = int(round(max(0.0, min(r, h / 2, w / 2)) * ss))
    m = np.zeros((h * ss, w * ss), np.uint8)
    if R <= 0:
        m[:] = 255
    else:
        m[R:h * ss - R, :] = 255; m[:, R:w * ss - R] = 255
        for cx, cy in ((R, R), (w * ss - R - 1, R), (R, h * ss - R - 1), (w * ss - R - 1, h * ss - R - 1)):
            cv2.circle(m, (cx, cy), R, 255, -1)
    return cv2.resize(m, (w, h), interpolation=cv2.INTER_AREA).astype(np.float32) / 255


# ---------------------------------------------------------------- chart (D4)

def human(v, f):
    """A value as the chart prints it: prefix + 2.4K / 313M / 1.2B (f["human"], default on) or with f["decimals"] + suffix."""
    pre, suf, dec = f.get("prefix", ""), f.get("suffix", ""), f.get("decimals")
    if f.get("human", True) and abs(v) >= 1000:
        for div, u in ((1e12, "T"), (1e9, "B"), (1e6, "M"), (1e3, "K")):
            if abs(v) >= div:
                x = v / div
                d = dec if dec is not None else (1 if abs(x) < 10 and abs(x - round(x)) >= 0.05 else 0)
                return f"{pre}{x:.{d}f}{u}{suf}"
    d = dec if dec is not None else (1 if abs(v) < 100 and abs(v - round(v)) >= 0.05 else 0)
    return f"{pre}{v:,.{d}f}{suf}"


_PLATES = {}


def draw_chart(img, c, t, shot_t0, kind_chart=False):
    """A line or bar chart that draws on (D4). See yt_picture.py's docstring for the keys."""
    x, y, w, h = c.get("box", [100, 360, 880, 560])
    t1 = c.get("t", shot_t0 + 0.2)
    dr = c.get("draw", 0.8)
    fade = clamp01((t - (t1 - 0.30)) / 0.30)
    if fade <= 0:
        return
    acc = rgb(c.get("color", "gold"))
    data = c["data"]
    labs, vals = [str(d[0]) for d in data], [float(d[1]) for d in data]
    n = len(vals)
    fmt = c.get("fmt", {})
    plate = c.get("plate", 0.0 if kind_chart else 0.6)
    if plate > 0:                                             # a frosted dark panel (blur 22 + darken) so it reads over moving B-roll
        px0, py0, pw, ph = x - 60, y - 130, w + 120, h + 240
        k = (px0, py0, pw, ph)
        if k not in _PLATES:
            _PLATES[k] = rounded_mask(ph, pw, 30)
        m = _PLATES[k]
        X0, Y0, X1, Y1 = max(0, px0), max(0, py0), min(img.shape[1], px0 + pw), min(img.shape[0], py0 + ph)
        reg = img[Y0:Y1, X0:X1].astype(np.float32)
        fr_ = cv2.GaussianBlur(reg, (0, 0), 22) * (1 - plate)
        mm = a3(m[Y0 - py0:Y1 - py0, X0 - px0:X1 - px0] * fade)
        img[Y0:Y1, X0:X1] = cv2.convertScaleAbs(reg * (1 - mm) + fr_ * mm)
        edge = np.clip(m - cv2.erode(m, np.ones((3, 3), np.uint8)), 0, 1)[Y0 - py0:Y1 - py0, X0 - px0:X1 - px0]
        _paint(img, edge * 0.16 * fade, X0, Y0, (255, 255, 255))      # a hairline rim
    elif kind_chart and c.get("glow_bg", 0.08):              # a faint accent lift behind the chart on the dark plate
        k = ("lift", x, y, w, h)
        if k not in _PLATES:                                  # full frame, so the falloff never meets a patch edge
            yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
            _PLATES[k] = np.exp(-(((xx - (x + w / 2)) / (0.5 * w)) ** 2 + ((yy - (y + h / 2)) / (0.6 * h)) ** 2))
        _paint(img, _PLATES[k] * c.get("glow_bg", 0.08) * fade, 0, 0, acc)
    white = (255, 255, 255)
    if c.get("title"):
        blit(img, label(c["title"].upper(), "mono", 34, white, track=0.10), x - 2, y - 92, 0.86 * fade)
    if c.get("source"):
        s_ = label(("SOURCE: " + c["source"]).upper(), "mono-med", 20, white, track=0.08)
        blit(img, s_, x + w - s_.shape[1] + 2, y + h + 70, 0.45 * fade)
    gp = inout2((t - (t1 - 0.30)) / 0.30)                    # the grid sweeps in left -> right with the fade
    xe = int(round(x + w * gp))
    for i in range(4):
        yy = int(round(y + h * i / 4))
        img[yy:yy + 1, x:xe] = (img[yy:yy + 1, x:xe].astype(np.float32) * 0.85 + 255 * 0.15).astype(np.uint8)
    img[y + h - 1:y + h + 1, x:xe] = (img[y + h - 1:y + h + 1, x:xe].astype(np.float32) * 0.7 + 255 * 0.3).astype(np.uint8)
    p = inout2((t - t1) / dr)
    lo, hi = min(vals), max(vals)
    if c.get("type", "line") == "bar":
        lo = c.get("y0", 0.0)
        hi = hi + 0.14 * (hi - lo or 1)
        slot = w / n; bw = slot * 0.58
        hi_i = c.get("hi", n - 1)
        for i, (lb, v) in enumerate(zip(labs, vals)):
            s0 = t1 + i * dr * 0.55 / max(1, n - 1)
            ph_ = out3((t - s0) / (dr * 0.45))
            bx = x + slot * (i + 0.5) - bw / 2
            l_ = label(lb.upper(), "mono-med", 26, white, track=0.06)
            blit(img, l_, bx + bw / 2 - l_.shape[1] / 2, y + h + 14, 0.7 * fade)
            if ph_ <= 0:
                continue
            bh_ = max(10.0, h * (v - lo) / (hi - lo)) * ph_
            m = rounded_mask(int(round(bh_)) + 8, int(round(bw)), 7)[:-8] if bh_ > 2 else np.ones((max(1, int(round(bh_))), int(round(bw))), np.float32)
            Y0 = int(round(y + h - bh_))
            if i == hi_i:
                g = np.zeros((m.shape[0] + 60, m.shape[1] + 60), np.float32); g[30:-30, 30:-30] = m
                g = cv2.GaussianBlur(g, (0, 0), 10)
                X0 = int(round(bx)) - 30; Y_ = Y0 - 30
                _paint(img, g * 0.55, X0, Y_, acc)
                _paint(img, m, int(round(bx)), Y0, acc)
                vt = human(v * ph_, fmt) if ph_ < 1 else c.get("value_label", human(v, fmt))
                lv = label(vt, "mono", 54, acc, track=0.0)
            else:
                _paint(img, m * 0.30, int(round(bx)), Y0, white)
                lv = label(human(v, fmt), "mono", 30, white, track=0.02)
            blit(img, lv, bx + bw / 2 - lv.shape[1] / 2, Y0 - lv.shape[0] - 8, (0.9 if i == hi_i else 0.72) * clamp01(ph_ * 2 - 0.6))
        return
    span = hi - lo or 1.0
    lo = c.get("y0", lo - 0.10 * span); hi = hi + 0.12 * span
    xs = np.array([x + w * i / max(1, n - 1) for i in range(n)])
    ys = np.array([y + h * (1 - (v - lo) / (hi - lo)) for v in vals])
    l0 = label(labs[0].upper(), "mono-med", 26, white, track=0.06)
    blit(img, l0, x, y + h + 16, 0.7 * fade)
    if p <= 0:
        return
    hx = x + w * p
    k = int(np.searchsorted(xs, hx, side="right"))
    k = max(1, min(k, n - 1)) if n > 1 else 0
    f = (hx - xs[k - 1]) / max(xs[k] - xs[k - 1], 1e-9) if n > 1 else 0
    hy = ys[k - 1] + (ys[k] - ys[k - 1]) * f if n > 1 else ys[0]
    hv = vals[k - 1] + (vals[k] - vals[k - 1]) * f if n > 1 else vals[0]
    pts = np.vstack([np.stack([xs[:k], ys[:k]], 1), [[hx, hy]]])
    if c.get("area", True):                                  # the fill under the line: accent, 22 % at the top fading to 0 at the base
        top = int(math.floor(min(pts[:, 1].min(), hy)))
        poly = np.vstack([pts, [[hx, y + h], [x, y + h]]])
        mh, mw = y + h - top + 2, int(math.ceil(hx - x)) + 2
        if mh > 2 and mw > 2:
            m = np.zeros((mh * SS, mw * SS), np.uint8)
            cv2.fillPoly(m, [np.round((poly - (x, top)) * SS).astype(np.int32)], 255)
            m = cv2.resize(m, (mw, mh), interpolation=cv2.INTER_AREA).astype(np.float32) / 255
            m *= np.linspace(0.22, 0.0, mh, dtype=np.float32)[:, None]
            _paint(img, m, x, top, acc)
    draw_strokes(img, [(pts, np.full(len(pts), c.get("width", 6.0)))], acc, shadow=0.0, glow=0.6, glow_sigma=6.0)
    land = clamp01((t - (t1 + dr)) / 0.35)
    r = 9 + 3 * (1 - out3(clamp01((t - (t1 + dr)) / 0.25))) * (land > 0)
    draw_strokes(img, [(np.array([[hx, hy]]), np.array([2 * r]))], acc, shadow=0.0, glow=0.7, glow_sigma=8.0)
    draw_strokes(img, [(np.array([[hx, hy]]), np.array([8.0]))], white, shadow=0.0)
    if 0 < land < 1:                                          # the landing: a ring expands from the head and fades
        rr = 12 + 26 * out3(land)
        th = np.linspace(0, 2 * np.pi, 64)
        ring = np.stack([hx + rr * np.cos(th), hy + rr * np.sin(th)], 1)
        draw_strokes(img, [(ring, np.full(64, 3.0))], acc, shadow=0.0, op=1 - land)
    vt = human(hv, fmt) if p < 1 else c.get("value_label", human(vals[-1], fmt))
    chip = label(vt, "mono", c.get("chip_px", 40), white, bg=rgb("black"), bg_a=0.9, pad=(18, 10))
    cx_ = min(max(hx - chip.shape[1] / 2, x - 30), x + w + 30 - chip.shape[1])
    cy_ = hy - chip.shape[0] - 26 if hy - chip.shape[0] - 26 > y - 60 else hy + 26
    blit(img, chip, cx_, cy_)
    if p >= 1:                                                # the date chip at the end point
        dc = label(labs[-1].upper(), "mono-med", 28, white, bg=rgb("black"), bg_a=0.9, pad=(14, 8))
        op = out3(clamp01((t - (t1 + dr)) / 0.18))
        blit(img, dc, min(xs[-1] - dc.shape[1] / 2, x + w + 30 - dc.shape[1]), y + h + 12, op)
        tick = int(round(xs[-1]))
        img[int(hy) + 14:y + h, tick:tick + 1] = (img[int(hy) + 14:y + h, tick:tick + 1].astype(np.float32) * (1 - 0.35 * op) + 255 * 0.35 * op).astype(np.uint8)


def _paint(img, alpha, x0, y0, color):
    h, w = alpha.shape
    X0, Y0, X1, Y1 = max(0, x0), max(0, y0), min(img.shape[1], x0 + w), min(img.shape[0], y0 + h)
    if X1 <= X0 or Y1 <= Y0:
        return
    a = a3(alpha[Y0 - y0:Y1 - y0, X0 - x0:X1 - x0])
    reg = img[Y0:Y1, X0:X1].astype(np.float32)
    img[Y0:Y1, X0:X1] = cv2.convertScaleAbs(reg * (1 - a) + np.full(reg.shape, color, np.float32) * a)


# ---------------------------------------------------------------- story effects (D6)

def apply_fx(img, fxs, n, s, fps, state):
    """Per-shot "fx" [{kind: flicker | shake | freeze, f0, f1, ...}] on the graded picture (before charts and marks)."""
    for j, z in enumerate([fxs] if isinstance(fxs, dict) else fxs):
        f0, f1 = z.get("f0", s["f0"]), z.get("f1", s["f1"])
        if not f0 <= n < f1:
            continue
        k = z["kind"]
        if k == "freeze":                                     # the picture holds frame f0 (the readers keep running underneath)
            key = (s["id"], j, "freeze")
            if key not in state:
                state[key] = img.copy()
            img = state[key].copy()
        elif k == "flicker":                                  # brightness toggles `depth` (0.15) in seeded 1-4 frame runs (the farm ref)
            key = (s["id"], j, "runs")
            if key not in state:
                rng, runs, dim = np.random.default_rng(z.get("seed", f0)), [], False
                while len(runs) < f1 - f0:
                    runs += [dim] * int(rng.integers(1, 5)); dim = not dim
                state[key] = runs
            if state[key][n - f0]:
                img = (img.astype(np.float32) * (1 - z.get("depth", 0.15)) + 0.5).astype(np.uint8)
        elif k == "shake":                                    # <= 12 px, two incommensurate sines per axis, eases out over the last 45 %
            amp, hz = min(z.get("amp", 10), 12), z.get("hz", 7.0)
            u, T = (n - f0) / fps, max((f1 - f0) / fps, 1e-6)
            ph = np.random.default_rng(z.get("seed", f0)).uniform(0, 2 * np.pi, 4)
            env = 1 - float(smooth(0.55, 1.0, u / T))
            dx = amp * env * (0.65 * math.sin(2 * math.pi * hz * u + ph[0]) + 0.35 * math.sin(2 * math.pi * 1.73 * hz * u + ph[1]))
            dy = amp * env * (0.65 * math.sin(2 * math.pi * 0.91 * hz * u + ph[2]) + 0.35 * math.sin(2 * math.pi * 1.37 * hz * u + ph[3]))
            sc = 1 + 2.2 * amp / W
            M = np.float32([[sc, 0, (1 - sc) * W / 2 + dx], [0, sc, (1 - sc) * H / 2 + dy]])
            img = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)
        else:
            raise SystemExit(f"yt_devices: unknown fx kind {k!r} (flicker | shake | freeze)")
    return img


# ---------------------------------------------------------------- the DOC shot (D1)

def load_rgb(path):
    return np.array(Image.open(path).convert("RGB"))


def plate_dark(seed=7):
    """The neutral plate of a CHART / DOC with "bg": "dark": near-black vertical gradient, a soft lift behind the centre, fine grain."""
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
    g = 16 - 8 * yy / H
    lift = 10 * np.exp(-(((xx - W / 2) / 520) ** 2 + ((yy - 700) / 640) ** 2))
    noise = np.random.default_rng(seed).normal(0, 1.6, (H, W)).astype(np.float32)
    v = g + lift + noise
    return np.clip(np.stack([v, v * 1.02 + 0.5, v * 1.08 + 1], 2), 0, 255).astype(np.uint8)


def plate_self(img, dim, blur=28, vignette=0.35):
    """A still's own blurred, darkened, cover-fitted copy (like FIT), with a vignette for depth."""
    ih, iw = img.shape[:2]
    k = max(W / iw, H / ih)
    r = cv2.resize(img, (max(W, int(math.ceil(iw * k))), max(H, int(math.ceil(ih * k)))), interpolation=cv2.INTER_AREA if k < 1 else cv2.INTER_CUBIC)
    y0, x0 = (r.shape[0] - H) // 2, (r.shape[1] - W) // 2
    bg = cv2.GaussianBlur(r[y0:y0 + H, x0:x0 + W], (0, 0), blur).astype(np.float32) * dim
    if vignette:
        yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
        d = np.sqrt(((xx - W / 2) / (W / 2)) ** 2 + ((yy - H / 2) / (H / 2)) ** 2)
        bg *= (1 - vignette * smooth(0.45, 1.25, d))[..., None]
    return np.clip(bg + 0.5, 0, 255).astype(np.uint8)


class Doc:
    """One DOC shot (see yt_picture.py's docstring for the keys)."""

    def __init__(self, s, SRC, fps):
        self.s, self.t0 = s, s["f0"] / fps
        dur = (s["f1"] - s["f0"]) / fps
        self.push = s.get("push", 0.07)
        entries = [e if isinstance(e, dict) else {"src": e} for e in (s.get("stack") or [s["src"]])]
        n = len(entries)
        look = s.get("look", "paper")
        w_out, max_h, cy = s.get("w", 900), s.get("max_h", 860), s.get("fg_y", 660)
        tilt = s.get("tilt", -3.0)
        sdx, sdy, sdeg = s.get("stack_step", [-40, -40, 3])
        grow = (1 + self.push * dur) * 1.07                       # the largest the card gets: the push plus a slap's overshoot
        self.layers = []
        for i, e in enumerate(entries):
            full = load_rgb(SRC(e["src"]))
            FH, FW = full.shape[:2]
            cr = e.get("crop") or (s.get("crop") if i == n - 1 else None) or [0, 0, 1, 1]
            X0, Y0 = int(round(cr[0] * FW)), int(round(cr[1] * FH))
            img = full[Y0:int(round(cr[3] * FH)), X0:int(round(cr[2] * FW))]
            ih, iw = img.shape[:2]
            k_rest = min(w_out / iw, max_h / ih)
            pre = min(1.0, k_rest * grow)                         # prescale once (never up): card px ~ output px at the largest size
            if pre < 1:
                img = cv2.resize(img, (max(1, round(iw * pre)), max(1, round(ih * pre))), interpolation=cv2.INTER_AREA)
            ps = img.shape[1] / iw                                # source px -> card px
            k = k_rest / ps                                       # card px -> output px at rest
            canvas, alpha, inner = self.card(img, k, look)
            sig = s.get("shadow_blur", 26) / k
            P = int(3 * sig) + 2
            shadow = cv2.GaussianBlur(np.pad(alpha, P), (0, 0), sig)
            d = n - 1 - i                                         # 0 = the front card
            sg = 1 if tilt >= 0 else -1
            self.layers.append(dict(
                canvas=canvas, alpha=alpha, pm=self.premult(canvas, alpha), shadow=shadow, P=P, k=k,
                ang=tilt + sdeg * d * sg, c=(W / 2 + sdx * d, cy + sdy * d),
                at=e.get("at") if e.get("at") is not None and e.get("at") > self.t0 + 1e-6 else None,
                src_map=(ps, inner[0] - X0 * ps, inner[1] - Y0 * ps), full=(FW, FH), crop=cr))
        self.front = self.layers[-1]
        self.hl = []
        for h in s.get("highlight", []):
            hd = h if isinstance(h, dict) else dict(t=h[0], box=h[1:5], **({"dur": h[5]} if len(h) > 5 else {}))
            self.hl.append(dict(t=hd["t"], box=hd["box"], dur=hd.get("dur", 0.35), rgb=np.array(rgb(hd.get("color", "yellow")), np.float32) / 255,
                                a=hd.get("a", s.get("hl_a", 0.45)), seed=len(self.hl) * 7 + 3))
        fo = s.get("focus")
        if fo is None:
            src_marks = [m for m in s.get("marks", []) if m.get("space", "src") == "src"]
            fo = ([self.hl[0]["box"][0] + self.hl[0]["box"][2] / 2, self.hl[0]["box"][1] + self.hl[0]["box"][3] / 2] if self.hl else
                  [src_marks[0]["box"][0] + src_marks[0]["box"][2] / 2, src_marks[0]["box"][1] + src_marks[0]["box"][3] / 2] if src_marks else
                  [(self.front["crop"][0] + self.front["crop"][2]) / 2, (self.front["crop"][1] + self.front["crop"][3]) / 2])
        L = self.front
        q = self.to_canvas(L, fo)
        self.F = (self.rest(L) @ np.array([q[0], q[1], 1.0]))[:2]
        self.dur, self.drift = dur, s.get("drift", 0.7)          # the push also glides the focus `drift` of the way to the frame's centre

        bg = s.get("bg", "self")
        if bg == "dark":
            self.bg = plate_dark()
        else:                                                     # the BACK-most source, uncropped (a cropped clipping blown up to
            self.bg = plate_self(load_rgb(SRC(bg if bg != "self" else entries[0]["src"])), s.get("bg_dim", 0.32))   # cover reads as giant letters)
        self.M_front = None

    def card(self, img, k, look):
        """The card's RGB, its alpha and the image's offset inside it. paper = rounded 10 px; screen = a 14 px near-black bezel,
        radius 30, a faint top-left glare and a 1.5 px light edge."""
        s = self.s
        ch, cw = img.shape[:2]
        if look == "screen":
            b = max(2, int(round(s.get("bezel", 14) / k)))
            R_out = s.get("radius", 30) / k
            Hc, Wc = ch + 2 * b, cw + 2 * b
            canvas = np.empty((Hc, Wc, 3), np.float32); canvas[:] = (12, 12, 14)
            ia = rounded_mask(ch, cw, max(1.0, R_out - b))[..., None]
            yy, xx = np.mgrid[0:ch, 0:cw].astype(np.float32)
            glare = np.clip(1 - (xx / cw + yy / ch) / 1.15, 0, 1) ** 2 * 0.07
            im = img.astype(np.float32); im = im + (255 - im) * glare[..., None]
            canvas[b:b + ch, b:b + cw] = canvas[b:b + ch, b:b + cw] * (1 - ia) + im * ia
            alpha = rounded_mask(Hc, Wc, R_out)
            e = max(2, int(round(1.5 / k)) * 2 + 1)
            ring = np.clip(alpha - cv2.erode(alpha, np.ones((e, e), np.uint8)), 0, 1)[..., None]
            canvas = canvas * (1 - ring * 0.6) + np.array([78, 78, 86], np.float32) * ring * 0.6
            return np.clip(canvas + 0.5, 0, 255).astype(np.uint8), alpha, (b, b)
        return img.copy(), rounded_mask(ch, cw, s.get("radius", 10) / k), (0, 0)

    @staticmethod
    def premult(canvas, alpha):
        return np.dstack([np.clip(canvas.astype(np.float32) * alpha[..., None] + 0.5, 0, 255), alpha * 255 + 0.5]).astype(np.uint8)

    @staticmethod
    def to_canvas(L, frac):
        ps, ox, oy = L["src_map"]
        return np.array([frac[0] * L["full"][0] * ps + ox, frac[1] * L["full"][1] * ps + oy])

    @staticmethod
    def rest(L, es=1.0, ea=0.0):
        Hc, Wc = L["canvas"].shape[:2]
        a = math.radians(L["ang"] + ea); k = L["k"] * es
        R = np.array([[k * math.cos(a), -k * math.sin(a)], [k * math.sin(a), k * math.cos(a)]])
        M = np.eye(3); M[:2, :2] = R; M[:2, 2] = np.array(L["c"]) - R @ np.array([Wc / 2, Hc / 2])
        return M

    def highlighted(self, t):
        """The front card's premultiplied RGBA with every started highlight swept in (multiply, D1)."""
        L = self.front
        live = [h for h in self.hl if t >= h["t"]]
        if not live:
            return L["pm"]
        cv = L["canvas"].astype(np.float32)
        fe = max(0.6, 1.0 / L["k"])                              # ~1 output px of soft edge
        for h in live:
            p = clamp01((t - h["t"]) / h["dur"])                 # linear, left -> right (D1: 0.35 s)
            if p <= 0:
                continue
            x0, y0 = self.to_canvas(L, h["box"][:2])
            x1, y1 = self.to_canvas(L, (h["box"][0] + h["box"][2], h["box"][1] + h["box"][3]))
            bh = y1 - y0
            pad, lead = 0.14 * bh, 0.22 * bh
            left = x0 - lead; right = left + (x1 - x0 + 2 * lead) * p
            amp = 0.05 * bh
            X0, X1 = int(max(0, math.floor(left - 3))), int(min(cv.shape[1], math.ceil(right + 3)))
            Y0, Y1 = int(max(0, math.floor(y0 - pad - amp - 3))), int(min(cv.shape[0], math.ceil(y1 + pad + amp + 3)))
            if X1 <= X0 or Y1 <= Y0:
                continue
            yy, xx = np.mgrid[Y0:Y1, X0:X1].astype(np.float32)
            ph = h["seed"]
            cyy = (y0 + y1) / 2 + amp * np.sin(2 * np.pi * xx / (3.3 * bh) + ph)
            hl_ = (right - left) / 2; hh_ = bh / 2 + pad
            r = min(0.30 * 2 * hh_, hl_)
            qx = np.abs(xx - (left + right) / 2) - (hl_ - r); qy = np.abs(yy - cyy) - (hh_ - r)
            dist = np.hypot(np.maximum(qx, 0), np.maximum(qy, 0)) + np.minimum(np.maximum(qx, qy), 0) - r
            al = np.clip(0.5 - dist / fe, 0, 1) * h["a"]
            cv[Y0:Y1, X0:X1] *= 1 - al[..., None] * (1 - h["rgb"])
        return self.premult(cv, L["alpha"])

    def frame(self, t):
        """The DOC picture at time t (uint8 HxWx3). Also sets self.M_front for the marks."""
        out = self.bg.copy()
        u = t - self.t0
        sc = 1 + self.push * u
        dx = (W / 2 - self.F[0]) * self.drift * float(smooth(0, 1, u / max(self.dur, 1e-6)))
        G = np.array([[sc, 0, self.F[0] * (1 - sc) + dx], [0, sc, self.F[1] * (1 - sc)], [0, 0, 1]])
        self.M_front = G @ self.rest(self.front)                 # marks follow the front card (set before it slaps in, too)
        for L in self.layers:
            if L["at"] is not None and t < L["at"] - 1e-6:
                continue
            pe = out3((t - L["at"]) / 0.24) if L["at"] is not None else 1.0       # a later layer slaps in: 7 % big, 1.4 deg off, settles
            M = G @ self.rest(L, 1 + 0.07 * (1 - pe), 1.4 * (1 - pe))
            if L is self.front:
                self.M_front = M
            self.composite(out, L["pm"] if L is not self.front else self.highlighted(t), M, L, min(1.0, pe * 4))
        return out

    def composite(self, out, pm, M, L, op):
        Hc, Wc = pm.shape[:2]
        sh_op, sh_off = self.s.get("shadow", 0.55), 20.0
        cor = M[:2] @ np.array([[0, Wc, 0, Wc], [0, 0, Hc, Hc], [1, 1, 1, 1]], float)
        mg = 3 * self.s.get("shadow_blur", 26) + sh_off + 4
        x0, y0 = int(max(0, math.floor(cor[0].min() - mg))), int(max(0, math.floor(cor[1].min() - mg)))
        x1, y1 = int(min(W, math.ceil(cor[0].max() + mg))), int(min(H, math.ceil(cor[1].max() + mg)))
        if x1 <= x0 or y1 <= y0:
            return
        Mr = M[:2].copy(); Mr[:, 2] -= (x0, y0)
        Ms = Mr.copy(); Ms[:, 2] = Mr[:, 2] - M[:2, :2] @ np.array([L["P"], L["P"]], float) + (0, sh_off)
        sh = cv2.warpAffine(L["shadow"], Ms, (x1 - x0, y1 - y0), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT, borderValue=0)
        c4 = cv2.warpAffine(pm, Mr, (x1 - x0, y1 - y0), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_CONSTANT, borderValue=0)
        al = c4[..., 3]
        rgb_ = cv2.min(np.ascontiguousarray(c4[..., :3]), cv2.merge([al, al, al]))     # premultiplied: cubic overshoot never exceeds alpha
        a = al.astype(np.float32) * (op / 255)
        keep = (1 - sh_op * op * sh) * (1 - a)                    # under the card: its shadow, then the card over it
        out[y0:y1, x0:x1] = cv2.convertScaleAbs(out[y0:y1, x0:x1].astype(np.float32) * a3(keep) + rgb_.astype(np.float32) * op)

    def mark_xf(self):
        """Source-file px -> output px through the front card (for "src"-space marks)."""
        L, M = self.front, self.M_front
        ps, ox, oy = L["src_map"]
        A = M[:2, :2] * ps
        return A, M[:2, :2] @ np.array([ox, oy]) + M[:2, 2], L["full"]
