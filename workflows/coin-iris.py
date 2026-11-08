# /// script
# requires-python = ">=3.10"
# dependencies = ["opencv-python-headless", "numpy", "pillow"]
# ///
"""coin-iris.py: the COIN IRIS transition (kit effect, first used on Scott D. Clary x Moshe Haimoff / David Dobrik, 2026-11-09).

A hero OBJECT carries the cut, and its round rim becomes the lens that opens onto the next real picture:
  1. a gold coin is tossed up from below the frame, spinning on its horizontal axis (motion-blurred), flying toward the lens,
  2. it lands face-up in the centre (a small squash, a ring flash),
  3. its rim OPENS like an iris (a gold ring on the expanding edge, the footage inside the circle pushing out from x1.18 to x1.0), and the coin is the first thing the footage pushes aside.
Learned from: Cleo Abram's round LENS MASKS as the scene container and transition (Shorts, "You're Dead. What Next?", 1.1M) + MrBeast's hero object that carries every cut
(briefcase, "What's Inside My Briefcase?", 127M), and FX-16 Portal Zoom of research/effects-catalog.  Everything is drawn in code: no logo, no photo of a coin, no sound
(the transition's only sound is the whip swish the build already cues into the clip).

  uv run workflows/coin-iris.py render OUT.mp4 [--footage F.mp4 --ss S] [--fps 30] [--dur 2.03] [--mode iris|toss]
        [--t-up 0.0 --t-land 1.2 --t-open 1.5 --open-dur 0.5 --cx 540 --cy 900 --r-land 300 --flips 4 --front "$" --back "*"]   (flips = half turns: an EVEN number lands the front, "$", face up)
  uv run workflows/coin-iris.py still OUT.png T [same options]        one frame at clip time T (look at it before a render)
  from importlib.machinery import SourceFileLoader; ci = SourceFileLoader("coin_iris", "workflows/coin-iris.py").load_module(); ci.render(...)

Modes: iris = toss -> land -> iris opens on --footage (the transition); toss = the coin is tossed up and leaves the top of the frame, still spinning (the plant:
the flip is announced, the landing comes later).  Clip time 0 = the first frame.  Timings are SECONDS from the clip start: the build computes them from the transcript.
"""
import argparse, math, os, subprocess, sys
import cv2, numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

W, H = 1080, 1920
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, ".."))
FONT = os.path.join(REPO, "presets", "youtube-shorts", "onyx-samples-youtube", "kit", "fonts", "Anton-Regular.ttf")
GOLD_HI, GOLD_MID, GOLD_LO, GOLD_DK = (255, 226, 120), (246, 180, 18), (178, 118, 8), (104, 66, 4)


def ease(p):
    p = min(1.0, max(0.0, p)); return p * p * (3 - 2 * p)


def inout(p):
    p = min(1.0, max(0.0, p)); return 0.5 * (1 - math.cos(math.pi * p))


def out3(p):
    p = min(1.0, max(0.0, p)); return 1 - (1 - p) ** 3


def plate():
    y, x = np.mgrid[0:H, 0:W].astype(np.float32)
    r = np.sqrt(((x - W / 2) / (W * 0.72)) ** 2 + ((y - 900) / (H * 0.6)) ** 2)
    base = np.array([30, 36, 52], np.float32)[None, None, :] * np.clip(1.12 - r, 0.0, 1.0)[..., None] + np.array([6, 8, 13], np.float32)[None, None, :]
    rng = np.random.default_rng(11); base += rng.normal(0, 1.1, (H, W, 1)).astype(np.float32)
    return np.clip(base, 0, 255).astype(np.uint8)


def face_sprite(glyph, R=420):
    """One coin face at 2R x 2R (RGBA): gold radial lighting, a raised rim, an inner ring, the glyph embossed."""
    S = 2 * R; ss = 2
    y, x = np.mgrid[0:S * ss, 0:S * ss].astype(np.float32); c = S * ss / 2
    d = np.sqrt((x - c) ** 2 + (y - c) ** 2) / (R * ss)
    lx, ly = (x - c * 0.72) / (R * ss), (y - c * 0.62) / (R * ss)
    light = np.clip(1.0 - np.sqrt(lx ** 2 + ly ** 2) * 0.62, 0.0, 1.0)
    img = np.zeros((S * ss, S * ss, 3), np.float32)
    for i, (lo, hi) in enumerate(zip(GOLD_LO, GOLD_HI)):
        img[..., i] = lo + (hi - lo) * light
    rim = np.clip((d - 0.86) / 0.14, 0, 1)                         # raised rim: bright band then a dark lip
    img *= (1.0 + 0.22 * np.sin(np.clip((d - 0.80) / 0.06, 0, 1) * math.pi) * (d < 0.93))[..., None]
    img *= (1.0 - 0.42 * np.clip((d - 0.94) / 0.06, 0, 1))[..., None]
    ring = np.exp(-((d - 0.74) / 0.012) ** 2)                      # inner engraved ring
    img *= (1.0 - 0.28 * ring)[..., None]
    pil = Image.fromarray(np.clip(img, 0, 255).astype(np.uint8)).convert("RGBA")
    f = ImageFont.truetype(FONT, int(R * ss * 1.05))
    g = Image.new("L", pil.size, 0); gd = ImageDraw.Draw(g)
    if glyph == "*":                                                # the tails face: a five-point star (a '*' reads as a footnote mark)
        pts = []
        for k in range(10):
            ang = -math.pi / 2 + k * math.pi / 5; rr = R * ss * (0.50 if k % 2 == 0 else 0.215)
            pts.append((c + rr * math.cos(ang), c + rr * math.sin(ang) + R * ss * 0.03))
        gd.polygon(pts, fill=255)
    else:
        bb = gd.textbbox((0, 0), glyph, font=f)
        gd.text((c - (bb[0] + bb[2]) / 2, c - (bb[1] + bb[3]) / 2 - R * ss * 0.04), glyph, font=f, fill=255)
    ga = np.asarray(g, np.float32) / 255
    emb = np.asarray(pil, np.float32)[..., :3]
    sh = np.asarray(g.filter(ImageFilter.GaussianBlur(5 * ss)), np.float32) / 255
    dark = emb * (1.0 - 0.5 * sh[..., None])                        # soft recess round the glyph
    lit = np.clip(np.array(GOLD_DK, np.float32)[None, None, :] * 0.55 + emb * 0.28, 0, 255)
    out = dark * (1 - ga[..., None]) + lit * ga[..., None]
    mask = (d <= 1.0).astype(np.float32); mask = cv2.GaussianBlur(mask, (0, 0), 1.2 * ss)
    rgba = np.dstack([np.clip(out, 0, 255), mask * 255]).astype(np.uint8)
    return Image.fromarray(rgba, "RGBA").resize((S, S), Image.LANCZOS)


class Coin:
    def __init__(self, front="$", back="*", R=420, thick=34):
        self.R, self.thick = R, thick
        self.front, self.back = face_sprite(front, R), face_sprite(back, R)
        self.side = Image.fromarray(np.dstack([np.full((2 * R, 2 * R, 3), GOLD_DK, np.uint8), np.asarray(self.front)[..., 3]]), "RGBA")

    def draw(self, canvas, cx, cy, radius, theta):
        """Paste the coin at (cx, cy), screen radius `radius` px, turned by theta about its horizontal axis (0 = front face-on)."""
        k = radius / self.R; c, s = math.cos(theta), math.sin(theta)
        h = max(2, int(round(2 * radius * abs(c))));  w = int(round(2 * radius))
        face = (self.front if c >= 0 else self.back).resize((w, h), Image.LANCZOS)
        edge = max(1.0, self.thick * k * abs(s))                      # the visible thickness grows as the coin turns edge-on
        side = self.side.resize((w, h), Image.LANCZOS)
        dy = int(round(edge / 2))
        n = max(2, int(edge // 3))
        for i in range(n, 0, -1):                                     # the extruded side, back to front
            canvas.alpha_composite(side, (int(cx - w / 2), int(cy - h / 2 + dy * (i / n) * (1 if s >= 0 else -1) + dy * (1 if s >= 0 else -1) * 0)))
        # a darker gold edge band must read when nearly edge-on: draw one more thin gold ellipse on top of the side stack
        canvas.alpha_composite(face, (int(cx - w / 2), int(cy - h / 2 - dy * (1 if s >= 0 else -1) * 0)))


def footage_frames(path, ss, n, fps):
    """n frames of the footage from `ss`, 1080x1920 cover, as uint8 RGB arrays (ffmpeg pipe, no blending)."""
    if not path:
        return None
    cmd = ["ffmpeg", "-v", "error", "-ss", f"{ss:.3f}", "-i", path, "-vf", f"fps={fps},scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H}", "-frames:v", str(n),
           "-f", "rawvideo", "-pix_fmt", "rgb24", "-"]
    raw = subprocess.run(cmd, capture_output=True).stdout
    arr = np.frombuffer(raw, np.uint8)
    m = arr.size // (W * H * 3)
    fr = arr[:m * W * H * 3].reshape(m, H, W, 3)
    return [fr[min(i, m - 1)] for i in range(n)]


class Scene:
    def __init__(self, a):
        self.a = a; self.coin = Coin(a.front, a.back); self.plate = plate()

    def path(self, t):
        """(cx, cy, radius, theta) of the coin at clip time t: tossed from below, peaks, lands face-up at (a.cx, a.cy)."""
        a = self.a
        if a.mode == "toss":                                          # up and OUT through the top, spinning
            p = (t - a.t_up) / max(a.t_land - a.t_up, 1e-3)
            cy = 2150 - 2700 * out3(p) if p >= 0 else 2150
            return W / 2 + 40 * math.sin(p * 2.0), cy, a.r_land * (0.62 + 0.14 * p), a.flips * math.pi * min(max(p, 0), 1) ** 0.8 + 0.4
        p = (t - a.t_up) / max(a.t_land - a.t_up, 1e-3)
        if p < 0:
            return W / 2, 2300, a.r_land * 0.5, 0.0
        peak = max(a.cy - 400, 230)
        if p < 0.5:                                                   # rising: decelerating
            q = p / 0.5; cy = 2150 + (peak - 2150) * out3(q)
        elif p < 1.0:                                                 # falling toward the lens: accelerating, growing
            q = (p - 0.5) / 0.5; cy = peak + (a.cy - peak) * (q * q)
        else:
            q = min((t - a.t_land) / 0.22, 1.0)
            cy = a.cy - 26 * math.sin(math.pi * q) * (1 - q)          # a tiny hop on the landing
        grow = 0.55 + 0.45 * ease(min(p, 1.0))
        theta = a.flips * math.pi * (1 - (1 - min(max(p, 0), 1)) ** 2.2)   # fast, then slowing
        end = round(a.flips) * math.pi                                 # land on a whole number of half turns -> front or back face-up
        if p >= 1.0:
            theta = end
        else:
            theta = theta * (end / (a.flips * math.pi))
        sq = 1.0 - 0.07 * math.sin(math.pi * min(max((t - a.t_land) / 0.18, 0.0), 1.0)) if t >= a.t_land else 1.0
        return W / 2 + 18 * math.sin(p * 3.0) * (1 - min(p, 1)), cy, a.r_land * grow * sq, theta

    def frame(self, t, foot=None):
        a = self.a
        sub = 5 if (a.t_up <= t < a.t_land) else 1                    # motion blur only while it spins
        acc = np.zeros((H, W, 3), np.float32)
        for k in range(sub):
            tt = t - (0.016 * (sub - 1 - k) / max(sub - 1, 1)) if sub > 1 else t
            cv = Image.fromarray(self.plate).convert("RGBA")
            cx, cy, r, th = self.path(tt)
            glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
            if r > 20 and -400 < cy < H + 500:
                gd = ImageDraw.Draw(glow); gd.ellipse((cx - r * 1.12, cy - r * 1.12 * max(abs(math.cos(th)), 0.18), cx + r * 1.12, cy + r * 1.12 * max(abs(math.cos(th)), 0.18)), fill=(246, 180, 18, 60))
                glow = glow.filter(ImageFilter.GaussianBlur(46)); cv.alpha_composite(glow)
                self.coin.draw(cv, cx, cy, r, th)
            acc += np.asarray(cv.convert("RGB"), np.float32)
        img = acc / sub
        if a.mode == "iris" and foot is not None and t >= a.t_open:
            p = inout((t - a.t_open) / a.open_dur)
            cx, cy = a.cx, a.cy
            rmax = math.hypot(max(cx, W - cx), max(cy, H - cy)) + 40
            rad = a.r_land * 0.86 + (rmax - a.r_land * 0.86) * p
            zoom = 1.18 - 0.18 * p
            M = np.float32([[zoom, 0, cx - cx * zoom], [0, zoom, cy - cy * zoom]])
            fz = cv2.warpAffine(foot, M, (W, H), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE).astype(np.float32)
            y, x = np.mgrid[0:H, 0:W].astype(np.float32)
            d = np.sqrt((x - cx) ** 2 + (y - cy) ** 2)
            inside = np.clip((rad - d) / 2.5 + 0.5, 0, 1)[..., None]        # a ~2.5 px soft edge
            ring_w = 15 * (1 - p) + 4
            ring = np.exp(-((d - rad) / ring_w) ** 2)[..., None]
            ringc = np.array(GOLD_MID, np.float32)[None, None, :] * 0.85 + np.array(GOLD_HI, np.float32)[None, None, :] * 0.15
            out = img * (1 - inside) + fz * inside
            out = out * (1 - 0.92 * ring * (1 - p * 0.6)) + ringc * (0.92 * ring * (1 - p * 0.6))
            img = out
        elif a.mode == "iris" and foot is not None and a.t_land <= t < a.t_open:
            q = (t - a.t_land) / max(a.t_open - a.t_land, 1e-3)           # a ring flash on the landing
            y, x = np.mgrid[0:H, 0:W].astype(np.float32); d = np.sqrt((x - a.cx) ** 2 + (y - a.cy) ** 2)
            rr = a.r_land * (1.0 + 0.5 * out3(min(q * 2.2, 1.0)))
            fl = np.exp(-((d - rr) / 7.0) ** 2)[..., None] * (1 - min(q * 2.2, 1.0)) * 0.7
            img = img * (1 - fl) + np.array(GOLD_HI, np.float32)[None, None, :] * fl
        return np.clip(img, 0, 255).astype(np.uint8)


def render(out, fps=30, dur=2.03, footage=None, ss=0.0, mode="iris", t_up=0.0, t_land=1.2, t_open=1.5, open_dur=0.5, cx=540, cy=900, r_land=300, flips=3.5,
           front="$", back="*"):
    a = argparse.Namespace(mode=mode, t_up=t_up, t_land=t_land, t_open=t_open, open_dur=open_dur, cx=cx, cy=cy, r_land=r_land, flips=flips, front=front, back=back)
    n = int(round(dur * fps)); sc = Scene(a); foot = footage_frames(footage, ss, n, fps)
    enc = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(fps), "-i", "-", "-c:v", "libx264", "-crf", "14",
                            "-pix_fmt", "yuv420p", out], stdin=subprocess.PIPE)
    for i in range(n):
        enc.stdin.write(sc.frame(i / fps, foot[i] if foot else None).tobytes())
    enc.stdin.close(); enc.wait()
    return n


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("cmd", choices=["render", "still"]); ap.add_argument("out"); ap.add_argument("t", nargs="?", type=float, default=0.0)
    ap.add_argument("--footage"); ap.add_argument("--ss", type=float, default=0.0); ap.add_argument("--fps", type=float, default=30); ap.add_argument("--dur", type=float, default=2.03)
    ap.add_argument("--mode", default="iris", choices=["iris", "toss"]); ap.add_argument("--t-up", type=float, default=0.0, dest="t_up"); ap.add_argument("--t-land", type=float, default=1.2, dest="t_land")
    ap.add_argument("--t-open", type=float, default=1.5, dest="t_open"); ap.add_argument("--open-dur", type=float, default=0.5, dest="open_dur")
    ap.add_argument("--cx", type=float, default=540); ap.add_argument("--cy", type=float, default=900); ap.add_argument("--r-land", type=float, default=300, dest="r_land")
    ap.add_argument("--flips", type=float, default=3.5); ap.add_argument("--front", default="$"); ap.add_argument("--back", default="*")
    a = ap.parse_args()
    if a.cmd == "render":
        n = render(a.out, a.fps, a.dur, a.footage, a.ss, a.mode, a.t_up, a.t_land, a.t_open, a.open_dur, a.cx, a.cy, a.r_land, a.flips, a.front, a.back); print(n, "frames ->", a.out)
    else:
        sc = Scene(a); foot = footage_frames(a.footage, a.ss + a.t, 1, a.fps)
        Image.fromarray(sc.frame(a.t, foot[0] if foot else None)).save(a.out); print("still ->", a.out)


if __name__ == "__main__":
    main()
