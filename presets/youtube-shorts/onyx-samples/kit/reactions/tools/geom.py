"""geom.py: the reaction-video geometry (Affan's layout, 1080x1920) and the source-frame / preview helpers.

Layers (his values, read from the timeline 2026-10-07):
  screen  2560x1440 OBS capture, Scale 71 at (0.42963, 0.28906)  -> panel box x 0..1080, y 44..1038 (the face layer covers y >= 1038)
  face    1920x1080 camera, Scale 65 at (0.5, 0.72344) in the split; Scale 132 at (0.5, 0.48958) face-only (his own framing)
A VIEW is what the screen panel shows: a source-pixel centre (cx, cy) and a zoom z relative to his default (z = 1 is Scale 71).
view_motion() turns it into Premiere Motion values (Scale %, Position as a fraction of the frame, Crop % per edge, in layer
space) so the zoomed layer is cropped to exactly the panel box and never leaks into the bars.

A plan's views[] entry {t0, t1, view, [anim: [t, dur], from, anim_out: [t, dur]], [ease], [drift]} (2026-10-13 additions):
  ease   the curve of anim / anim_out: "outCubic" (default, the original push-in) | "inOutCubic" | "inOutSine" | "linear"
  drift  a z multiplier reached at the view's t1 (e.g. 1.06), eased inOutSine from 1.0 at t0, applied ON TOP of the view (and of
         any anim): the slow push on a long hold (research 2026-10-13 #5). apply.py bakes such a view as keys every 0.5 s.
"""
import io, json, math, subprocess
from PIL import Image

W, H = 1080, 1920
SW, SH = 2560, 1440
BASE = 0.71
BOX = (0, 44, 1080, 1038)                    # panel box in the sequence frame
DEFAULT_POS = (0.42962962388992, 0.2890625)
FACE_SPLIT = dict(scale=65, pos=(0.5, 0.72343748807907))
FACE_ONLY = dict(scale=132, pos=(0.5, 0.48958334326744))


def configure(plan):
    """Per-plan layout overrides (2026-10-08, Seq 37/38): "box" = the visible screen panel (the screen sits ABOVE the face
    there, so it runs to y 1066), "face_split" = his split framing. Defaults stay the Seq 33-35 values."""
    global BOX, FACE_SPLIT
    if plan.get("box"): BOX = tuple(plan["box"])
    if plan.get("face_split"): FACE_SPLIT = dict(scale=plan["face_split"]["scale"], pos=tuple(plan["face_split"]["pos"]))


def default_view():
    """His default framing expressed as a view: the source point under the panel-box centre."""
    s = BASE
    lx, ly = DEFAULT_POS[0] * W, DEFAULT_POS[1] * H          # layer centre in the frame
    bx, by = (BOX[0] + BOX[2]) / 2, (BOX[1] + BOX[3]) / 2
    return dict(cx=SW / 2 + (bx - lx) / s, cy=SH / 2 + (by - ly) / s, z=1.0)


def view_motion(v):
    s = BASE * v["z"]
    bw, bh = BOX[2] - BOX[0], BOX[3] - BOX[1]
    bx, by = (BOX[0] + BOX[2]) / 2, (BOX[1] + BOX[3]) / 2
    cx, cy = v["cx"], v["cy"]
    pos = ((bx + (SW / 2 - cx) * s) / W, (by + (SH / 2 - cy) * s) / H)
    x0, x1 = cx - bw / 2 / s, cx + bw / 2 / s
    y0, y1 = cy - bh / 2 / s, cy + bh / 2 / s
    crop = dict(L=max(0, x0 / SW * 100), R=max(0, (SW - x1) / SW * 100), T=max(0, y0 / SH * 100), B=max(0, (SH - y1) / SH * 100))
    return dict(scale=round(s * 100, 3), pos=(round(pos[0], 6), round(pos[1], 6)), crop={k: round(c, 3) for k, c in crop.items()})


def frame(path, t, scale=None):
    vf = [] if not scale else ["-vf", f"scale={scale}"]
    r = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{max(t, 0):.3f}", "-i", path, "-frames:v", "1", *vf, "-f", "image2pipe", "-vcodec", "png", "-"], capture_output=True)
    return Image.open(io.BytesIO(r.stdout)).convert("RGB")


def place(canvas, im, scale_pct, pos, crop=None):
    s = scale_pct / 100
    if crop:
        L, T = crop["L"] / 100 * im.width, crop["T"] / 100 * im.height
        R, B = im.width - crop["R"] / 100 * im.width, im.height - crop["B"] / 100 * im.height
        sub = im.crop((round(L), round(T), round(R), round(B)))
        cxl, cyl = pos[0] * W, pos[1] * H
        x0 = cxl + (L - im.width / 2) * s; y0 = cyl + (T - im.height / 2) * s
        canvas.paste(sub.resize((max(1, round(sub.width * s)), max(1, round(sub.height * s)))), (round(x0), round(y0)))
    else:
        w, h = round(im.width * s), round(im.height * s)
        canvas.paste(im.resize((w, h)), (round(pos[0] * W - w / 2), round(pos[1] * H - h / 2)))


def clip_at(track, t):
    for c in track["clips"]:
        if c["s"] - 1e-6 <= t < c["e"]:
            return c
    return None


def src_time(c, t):
    return c["i"] + (t - c["s"])


def _ease(x):
    x = min(max(x, 0.0), 1.0); return 1 - (1 - x) ** 3


def _clamp01(f):
    return lambda x: f(min(max(x, 0.0), 1.0))


EASES = {"outCubic": _ease,
         "inOutCubic": _clamp01(lambda x: 4 * x ** 3 if x < 0.5 else 1 - (-2 * x + 2) ** 3 / 2),
         "inOutSine": _clamp01(lambda x: -(math.cos(math.pi * x) - 1) / 2),
         "linear": _clamp01(lambda x: x)}


def named(plan, v):
    return dict(default_view()) if v in (None, "default") else dict(plan["views_named"][v])


def view_at(plan, t):
    """The screen view at sequence time t (None while the face-only layout is up), with eased push-ins (v["ease"]) and the
    slow drift (v["drift"]) on top."""
    if any(f["t0"] <= t < f["t1"] for f in plan["face"]):
        return None
    for v in plan["views"]:
        if v["t0"] <= t < v["t1"]:
            to = named(plan, v["view"])
            if "anim" in v:
                ez = EASES[v.get("ease", "outCubic")]
                ta, d = v["anim"]; fr = named(plan, v.get("from", "default")); p = ez((t - ta) / d)
                if "anim_out" in v:                       # ...and back out to the from-view (a page about to scroll away)
                    tb, d2 = v["anim_out"]; p *= 1 - ez((t - tb) / d2)
                to = {k: fr[k] + (to[k] - fr[k]) * p for k in ("cx", "cy", "z")}
            if v.get("drift"):                           # the slow push across the hold, centred on the view
                q = EASES["inOutSine"]((t - v["t0"]) / max(v["t1"] - v["t0"], 1e-6))
                to = dict(to, z=to["z"] * (1 + (v["drift"] - 1) * q))
            return to
    return default_view()


def motion_rect(m):
    """The frame rect (x0, y0, x1, y1) a screen layer with Motion values m (view_motion's output) actually covers: the crop
    applied, then scaled about the layer centre. apply.py checks every baked key against BOX with it (no leak into the bars)."""
    s = m["scale"] / 100; cx, cy = m["pos"][0] * W, m["pos"][1] * H; c = m["crop"]
    return (cx + (c["L"] / 100 * SW - SW / 2) * s, cy + (c["T"] / 100 * SH - SH / 2) * s,
            cx + (SW / 2 - c["R"] / 100 * SW) * s, cy + (SH / 2 - c["B"] / 100 * SH) * s)


def face_at(plan, t):
    return next((f for f in plan["face"] if f["t0"] <= t < f["t1"]), None)


def face_motion(scale, face_x=None):
    """Face-only at his 132 framing; a punch-in (e.g. 150) keeps the SAME window (y 227..1653) by cropping top and bottom.
    face_x (camera source px, 1920 wide): put that x at the frame centre (his face moves between takes), clamped so the
    layer always covers the full width."""
    s = scale / 100
    top = FACE_ONLY["pos"][1] * H - 1080 * s / 2
    want = FACE_ONLY["pos"][1] * H - 1080 * 1.32 / 2
    c = max(0.0, (want - top) / s / 1080 * 100)
    px = FACE_ONLY["pos"][0]
    if face_x is not None:
        half = 1920 * s / 2
        cx = min(max(W / 2 - (face_x - 960) * s, W - half), half)
        px = round(cx / W, 6)
    return dict(scale=scale, pos=(px, FACE_ONLY["pos"][1]), crop=dict(L=0, R=0, T=round(c, 3), B=round(c, 3)))
