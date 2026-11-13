# /// script
# requires-python = ">=3.10"
# dependencies = ["opencv-python-headless", "numpy", "pillow"]
# ///
"""void-drop.py: VOID DROP, a reusable kit effect (2026-11-14, pbd-urine-prank; UPGRADES.md).  FX-33 "Dust Void Drop", learned from Patrick Cc: ("50 Cent Was Right About Floyd Mayweather").

ONE artifact on an empty near-black field with sparse film-dust specks.  No blur, no rotation (the reference's rule): it DROPS in from the top (an ease-in fall that lands with a short settle),
sits on the void with a slow push-in, then keeps falling out the bottom when the next picture is about to take the frame.  The artifact is a rounded-corner card (a photo, a headline block, a drawn
memo): the card's own pixels are never altered, so type stays crisp.

As a library:
    vd = VoidDrop(dict(dur=2.2, items=[dict(sprite=<RGBA ndarray | callable t->RGBA | image path>, w=420, cy=640, t_land=0.40, fall=0.42, t_out=1.8, radius=30, shadow=0.6)], dust=True, push=0.04))
    frame_rgb_uint8 = vd.frame(t)            # 1080 x 1920
An item's sprite is scaled to w px wide (a callable returns the RGBA at its final size).  `t_land` = the time the card first touches (the fall starts t_land - fall);
`t_out` = the time it starts falling out (None = it stays); `settle` px of bounce.  Several items may overlap in time (the next item falls in while the previous falls out: a chain).
CLI test clip:  uv run workflows/void-drop.py test PHOTO.jpg OUT.mp4 [--dur 2.4] [--fps 30]
"""
import math, os, subprocess, sys
import cv2, numpy as np
from PIL import Image, ImageDraw

W, H = 1080, 1920


def ease_in(p):
    p = min(1.0, max(0.0, p)); return p * p * p


def ease_out(p):
    p = min(1.0, max(0.0, p)); return 1 - (1 - p) ** 3


def rounded_alpha(w, h, r, ss=3):
    im = Image.new("L", (w * ss, h * ss), 0)
    ImageDraw.Draw(im).rounded_rectangle([0, 0, w * ss - 1, h * ss - 1], radius=r * ss, fill=255)
    return np.asarray(im.resize((w, h), Image.LANCZOS), np.float32) / 255.0


class VoidDrop:
    def __init__(self, scene, seed=7):
        self.s = scene; self.dur = scene["dur"]
        yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
        r = np.sqrt(((xx - W / 2) / (W * 0.62)) ** 2 + ((yy - H * 0.40) / (H * 0.42)) ** 2)
        self.bg = (np.array([6, 7, 9], np.float32) + np.array([13, 15, 19], np.float32) * np.clip(1.1 - r, 0, 1)[..., None])
        rng = np.random.default_rng(seed)
        n = 90 if scene.get("dust", True) else 0
        self.dust = [(rng.uniform(0, W), rng.uniform(0, H), rng.uniform(0.8, 2.0), rng.uniform(0.10, 0.34), rng.uniform(-6, 6), rng.uniform(4, 16), rng.uniform(0, 6.28)) for _ in range(n)]
        self.items = []
        for it in scene["items"]:
            sp = it["sprite"]
            if isinstance(sp, str):
                im = Image.open(sp).convert("RGBA"); k = it["w"] / im.width
                sp = np.asarray(im.resize((int(it["w"]), int(round(im.height * k))), Image.LANCZOS))
            self.items.append(dict(it, sprite=sp, _a=None))

    def _sprite(self, it, t):
        sp = it["sprite"](t) if callable(it["sprite"]) else it["sprite"]
        if sp.dtype != np.uint8: sp = np.clip(sp, 0, 255).astype(np.uint8)
        return sp

    def frame(self, t):
        out = self.bg.copy()
        dl = np.zeros((H, W), np.float32)
        for x, y, sz, a, vx, vy, ph in self.dust:                       # film dust: a few specks drifting slowly, twinkling
            px, py = (x + vx * t) % W, (y + vy * t) % H
            al = a * (0.65 + 0.35 * math.sin(ph + t * 2.1))
            cv2.circle(dl, (int(px), int(py)), max(1, int(round(sz / 1.2))), float(al), -1, cv2.LINE_AA)
        out = out * (1 - dl[..., None]) + 255.0 * dl[..., None]
        push = 1.0 + float(self.s.get("push", 0.04)) * (t / max(self.dur, 1e-6))
        for it in self.items:
            sp = self._sprite(it, t); h, w = sp.shape[:2]
            tl, fall = it["t_land"], it.get("fall", 0.42)
            cy_f = it["cy"]; top_f = cy_f - h / 2
            if t < tl - fall:
                continue
            if t < tl:                                                    # the fall: ease-in from above the frame to the resting top
                p = ease_in((t - (tl - fall)) / fall); y0 = -h - 40
                top = y0 + (top_f - y0) * p
            else:
                s_ = it.get("settle", 7)                                  # a short settle after the touch, then the slow push
                tt = t - tl
                top = top_f - s_ * math.exp(-tt * 9) * abs(math.sin(tt * 16)) * 1.0
            if it.get("t_out") is not None and t >= it["t_out"]:           # falls out the bottom (ease-in)
                p = ease_in((t - it["t_out"]) / it.get("out", 0.40)); top = top + (H + 40 - top) * p
            if top > H: continue
            sc = push if (t >= tl and (it.get("t_out") is None or t < it["t_out"])) else 1.0
            # the push-in scales the resting card about the frame centre: apply it to the position only for the resting card
            ww, hh = int(round(w * sc)), int(round(h * sc))
            spr = sp if sc == 1.0 else cv2.resize(sp, (ww, hh), interpolation=cv2.INTER_CUBIC if sc > 1 else cv2.INTER_AREA)
            x0 = int(round(W / 2 - ww / 2)); y0_ = int(round(top - (hh - h) / 2))
            al_r = rounded_alpha(ww, hh, int(it.get("radius", 28) * sc)) if it.get("radius", 28) else np.ones((hh, ww), np.float32)
            a = spr[..., 3:4].astype(np.float32) / 255.0 * al_r[..., None]
            # a soft contact pool of light under the card (not a blur of the card): a dark shadow behind it
            sh = float(it.get("shadow", 0.55))
            if sh > 0:
                m = np.zeros((H, W), np.float32); ya, yb = max(0, y0_ + 26), min(H, y0_ + hh + 26)
                if yb > ya:
                    m[ya:yb, max(0, x0):min(W, x0 + ww)] = 1.0; m = cv2.GaussianBlur(m, (0, 0), 30) * sh; out *= (1 - m[..., None])
            ya, yb, xa, xb = max(0, y0_), min(H, y0_ + hh), max(0, x0), min(W, x0 + ww)
            if yb <= ya or xb <= xa: continue
            sa = a[ya - y0_:yb - y0_, xa - x0:xb - x0]; sr = spr[ya - y0_:yb - y0_, xa - x0:xb - x0, :3].astype(np.float32)
            reg = out[ya:yb, xa:xb]; reg[:] = reg * (1 - sa) + sr * sa
        return np.clip(out, 0, 255).astype(np.uint8)

    def render(self, path, fps=30.0):
        n = int(round(self.dur * fps))
        enc = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(fps), "-i", "-", "-c:v", "libx264", "-crf", "14", "-pix_fmt", "yuv420p", path], stdin=subprocess.PIPE)
        for i in range(n):
            enc.stdin.write(self.frame(i / fps).tobytes())
        enc.stdin.close(); enc.wait(); return n


if __name__ == "__main__":
    if len(sys.argv) < 4 or sys.argv[1] != "test":
        sys.exit(__doc__)
    photo, outp = sys.argv[2], sys.argv[3]
    arg = lambda n, d: sys.argv[sys.argv.index(n) + 1] if n in sys.argv else d
    dur, fps = float(arg("--dur", "2.4")), float(arg("--fps", "30"))
    vd = VoidDrop(dict(dur=dur, items=[dict(sprite=photo, w=420, cy=640, t_land=0.45, fall=0.42, t_out=dur - 0.5, radius=30)], dust=True, push=0.04))
    print("wrote", outp, vd.render(outp, fps), "frames")
