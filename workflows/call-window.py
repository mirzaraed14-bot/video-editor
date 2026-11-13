# /// script
# requires-python = ">=3.10"
# dependencies = ["opencv-python-headless", "numpy", "pillow"]
# ///
"""call-window.py: CALL WINDOW, a reusable kit effect (2026-11-14, pbd-urine-prank; UPGRADES.md).

A remote guest's feed is shown AS a call: a rounded 4:5 window (default 896 x 1120) with a hairline rim and a soft shadow over a blurred, darkened copy of itself, and an
optional call-chrome name pill (a live dot + NAME · DATE) that rises under it. Principle: Coffeezilla's FX-57 / FX-53 ("a recorded video call is never shown full-screen", the
evidence fills the frame and the host is a framed live inset). It is the answer to a SOFT remote picture (a 2020 phone / webcam): the window is a frame the viewer reads as "a call",
the picture is never magnified past ~1.05-1.2x, and the same window can show the host's half of the call for a reaction cutaway.

As a library (the job's picture engine calls it for every shot of a window):
    cw = CallWindow(spec["win"], fps)                       # spec["win"] = {"w", "h", "x", "y", "radius", "rim", "shadow", "plate_dim", "look": {...grade keys...}, "mask", "sharp"}
    frame = cw.compose(window_rgb_uint8, t_seconds, tag)    # window_rgb: (h, w, 3) RGB; tag = {"name", "date", "t0"} or None  ->  (1920, 1080, 3) RGB uint8
The window content is graded (workflows/grade-picture.py's grade(), with spec["win"]["look"] over its A look, relight off) and sharpened (two luma unsharp passes, ffmpeg's
unsharp 7x7 / 3x3 emulated) INSIDE the window only: the plate, the rim and the pill are never graded or sharpened.

As a test clip:  uv run workflows/call-window.py test BASE.mp4 OUT.mp4 [--side L|R] [--t0 1.0] [--dur 2.0] [--fps 30] [--tag "NAME|DATE"] [--grade-test]
(a fixed crop of the base's half, k = 1.04: a quick look at the framing, the plate, the pill and the grade; the job's engine adds the face tracking.)
"""
import math, os, subprocess, sys
from importlib.machinery import SourceFileLoader
import cv2, numpy as np
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__)); REPO = os.path.dirname(HERE)
FONTS = os.path.join(REPO, "presets", "youtube-shorts", "onyx-samples-youtube", "kit", "fonts")
W, H = 1080, 1920
_gp = SourceFileLoader("grade_picture", os.path.join(HERE, "grade-picture.py")).load_module()

DEFAULT = dict(w=896, h=1120, x=92, y=200, radius=34, rim=0.30, shadow=0.60, plate_dim=0.34, plate_blur=26.0, mask=0.55, sharp=0.40,
               look=dict(relight=0.0))


def ease_out(p):
    p = min(1.0, max(0.0, p)); return 1 - (1 - p) ** 3


def _mont(size, wght=700):
    f = ImageFont.truetype(os.path.join(FONTS, "Montserrat-VF.ttf"), size)
    try:
        f.set_variation_by_axes([wght])
    except Exception:
        pass
    return f


def _rounded_mask(w, h, r, ss=4):
    """an antialiased rounded-rectangle alpha (float32 0..1), supersampled."""
    im = Image.new("L", (w * ss, h * ss), 0)
    ImageDraw.Draw(im).rounded_rectangle([0, 0, w * ss - 1, h * ss - 1], radius=r * ss, fill=255)
    return np.asarray(im.resize((w, h), Image.LANCZOS), np.float32) / 255.0


class CallWindow:
    def __init__(self, spec=None, fps=30.0):
        s = {**DEFAULT, **(spec or {})}
        self.s = s; self.fps = fps
        self.w, self.h, self.x, self.y = int(s["w"]), int(s["h"]), int(s["x"]), int(s["y"])
        self.look = {**_gp.LOOK["A"], **s.get("look", {})}
        self.mask = _rounded_mask(self.w, self.h, int(s["radius"]))
        m3 = self.mask[..., None]
        # the hairline rim: the mask minus the mask eroded by 2 px (a 2 px inner ring), white at s["rim"]
        er = cv2.erode(self.mask, np.ones((5, 5), np.uint8))
        self.ring = np.clip(self.mask - er, 0, 1)[..., None] * float(s["rim"])
        # the soft drop shadow: the mask, blurred, pushed 22 px down, over the whole frame
        sh = np.zeros((H, W), np.float32); sh[self.y + 22:self.y + 22 + self.h, self.x:self.x + self.w] = self.mask
        sh = cv2.GaussianBlur(sh, (0, 0), 34); self.shadow = (sh * float(s["shadow"]))[..., None]
        yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
        self.vig = (1.0 - 0.45 * np.clip(((xx - W / 2) / (W * 0.8)) ** 2 + ((yy - H * 0.45) / (H * 0.75)) ** 2, 0, 1) ** 1.1)[..., None]
        self._pill = {}

    # ---- the window content: the guest's grade + the finishing sharpen, inside the window only ----
    def grade(self, img):
        a = img.astype(np.float32) / 255.0
        g = _gp.grade(a, self.look)
        out = (np.clip(g, 0, 1) * 255 + 0.5).astype(np.uint8)
        y = cv2.cvtColor(out, cv2.COLOR_RGB2YCrCb); L = y[..., 0].astype(np.float32)
        for ksz, sig, amt in ((7, 1.75, float(self.s["mask"])), (3, 0.75, float(self.s["sharp"]))):
            L = L + amt * (L - cv2.GaussianBlur(L, (ksz, ksz), sig))
        y[..., 0] = np.clip(L, 0, 255).astype(np.uint8)
        return cv2.cvtColor(y, cv2.COLOR_YCrCb2RGB)

    def plate(self, img):
        """a blurred, darkened, cover-fitted copy of the window picture, at 1/8 size then scaled up (cheap, smooth)."""
        k = max(W / self.w, H / self.h)
        sw, sh_ = int(round(self.w * k / 8)), int(round(self.h * k / 8))
        small = cv2.resize(img, (sw, sh_), interpolation=cv2.INTER_AREA)
        x0, y0 = max(0, (sw - W // 8) // 2), max(0, (sh_ - H // 8) // 2)
        small = small[y0:y0 + H // 8, x0:x0 + W // 8]
        small = cv2.GaussianBlur(small, (0, 0), float(self.s["plate_blur"]) / 8)
        big = cv2.resize(small, (W, H), interpolation=cv2.INTER_CUBIC).astype(np.float32)
        return big * float(self.s["plate_dim"]) * self.vig

    def pill(self, tag):
        key = (tag["name"], tag["date"])
        if key not in self._pill:
            ss = 2; text = f"{tag['name']}   ·   {tag['date']}"
            f = _mont(34 * ss, 700); tw = int(f.getlength(text)); ph = 78 * ss; pw = 78 * ss + tw + 40 * ss
            im = Image.new("RGBA", (pw, ph), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
            d.rounded_rectangle([0, 0, pw - 1, ph - 1], radius=ph // 2, fill=(10, 12, 16, 214), outline=(255, 255, 255, 46), width=2)
            d.text((78 * ss, ph // 2), text, font=f, fill=(255, 255, 255, 255), anchor="lm")
            base = np.asarray(im.resize((pw // ss, ph // ss), Image.LANCZOS), np.float32)
            self._pill[key] = (base, 30.0 * 1.0)         # (rgba, dot x), the dot is drawn per frame (it breathes)
        return self._pill[key][0]

    def compose(self, win_rgb, t=0.0, tag=None, graded=False):
        g = win_rgb if graded else self.grade(win_rgb)
        out = self.plate(g)
        out *= (1.0 - self.shadow)
        reg = out[self.y:self.y + self.h, self.x:self.x + self.w]
        m3 = self.mask[..., None]
        reg[:] = reg * (1 - m3) + g.astype(np.float32) * m3
        reg[:] = reg * (1 - self.ring) + 255.0 * self.ring
        if tag:
            t0 = float(tag.get("t0", 0.30)); p = ease_out((t - t0) / 0.30)
            if p > 0:
                pl = self.pill(tag); ph, pw = pl.shape[:2]
                px = (W - pw) // 2; py = int(round(self.y + self.h - ph / 2 + (1 - p) * 18))
                a = pl[..., 3:4] / 255.0 * p
                # the live dot breathes: a soft red disc with a glow
                dot = np.zeros((ph, pw, 1), np.float32); cv2.circle(dot, (int(46), ph // 2), 10, 1.0, -1, cv2.LINE_AA)
                glow = cv2.GaussianBlur(dot[..., 0], (0, 0), 9)[..., None] * (0.35 + 0.30 * math.sin(2 * math.pi * t / 1.4) ** 2)
                rgb = pl[..., :3] * (1 - dot) + np.array([236, 58, 72], np.float32) * dot
                rgb = rgb + np.array([236, 58, 72], np.float32) * glow * (1 - dot) * 0.8
                dst = out[py:py + ph, px:px + pw]
                dst[:] = dst * (1 - a) + np.clip(rgb, 0, 255) * a
        return np.clip(out, 0, 255).astype(np.uint8)


def main():
    if len(sys.argv) < 2 or sys.argv[1] != "test":
        sys.exit(__doc__)
    base, outp = sys.argv[2], sys.argv[3]
    arg = lambda n, d: sys.argv[sys.argv.index(n) + 1] if n in sys.argv else d
    side, t0, dur, fps = arg("--side", "L"), float(arg("--t0", "1.0")), float(arg("--dur", "2.0")), float(arg("--fps", "30"))
    tag = None
    if "--tag" in sys.argv:
        nm, dt = arg("--tag", "NAME|DATE").split("|"); tag = {"name": nm, "date": dt, "t0": 0.30}
    cw = CallWindow({}, fps); n = int(round(dur * fps))
    p = subprocess.Popen(["ffmpeg", "-v", "error", "-ss", f"{t0}", "-i", base, "-t", f"{dur}", "-vf", f"fps={fps}", "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], stdout=subprocess.PIPE)
    enc = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(fps), "-i", "-", "-c:v", "libx264", "-crf", "14", "-pix_fmt", "yuv420p", outp], stdin=subprocess.PIPE)
    bw, bh = 1920, 1080; half = bw // 2; hx = 0 if side == "L" else half
    k = max(cw.w / half, cw.h / bh) * 1.02; vw, vh = cw.w / k, cw.h / k
    x0 = hx + (half - vw) * (0.80 if side == "L" else 0.35); y0 = 0.0
    for i in range(n):
        b = p.stdout.read(bw * bh * 3)
        if len(b) < bw * bh * 3: break
        fr = np.frombuffer(b, np.uint8).reshape(bh, bw, 3)
        M = np.float32([[k, 0, -x0 * k], [0, k, -y0 * k]])
        win = cv2.warpAffine(fr, M, (cw.w, cw.h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REFLECT)
        enc.stdin.write(cw.compose(win, i / fps, tag).tobytes())
    enc.stdin.close(); enc.wait(); p.stdout.close(); print("wrote", outp, n, "frames")


if __name__ == "__main__":
    main()
