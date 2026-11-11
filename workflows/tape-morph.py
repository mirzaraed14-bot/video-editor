# /// script
# requires-python = ">=3.10"
# dependencies = ["opencv-python-headless", "numpy", "pillow"]
# ///
"""tape-morph.py: the TAPE MORPH transition (kit effect, FX-43 of research/effects-catalog; first used on Scott D. Clary x Gary Vaynerchuk "Gary Vee Blamed Ricky", 2026-11-11).

A then -> now line about ONE person: a still of them years ago is matched to them today ON THE EYES and dissolved through a VHS tear:
  1. the THEN still holds with a quiet tape skin (fine scanlines, a 2 px RGB fringe, a head-switching band along the bottom, grain) and a steady push-in,
  2. the TEAR: horizontal bands of the picture slide sideways and switch from then to now at different moments (so the faces overlap band by band), the
     red / blue channels split apart, a bright tracking line rolls down, both faces get a DOUBLED OUTLINE (cyan for then, red for now) while they overlap,
  3. the NOW picture settles: the glitch AND the always-on tape skin decay to nothing over ~0.45 s (the frame is returned untouched after that) and the live frames play on, clean.
The eye match is measured, not guessed: YuNet (assets/models/face_detection_yunet_2023mar.onnx) finds both eyes in the still and in every NOW frame, and the
still is warped (scale + rotation + shift, the picture's own blurred edge fills the rest of the 9:16 frame) so its eyes sit exactly on today's eyes through the
whole tear.  Learned from Dodford ("Jack Black Doesn't Fit In": two stills of the same person at different ages matched on the eyes and dissolved through VHS glitch).
Everything is drawn in code from your two pictures; no sound (the build cues its usual whip swish into the shot).

  uv run workflows/tape-morph.py render OUT.mp4 --then THEN.jpg --now NOW.mp4 [--now-ss S] [--dur 3.2] [--fps 30] [--t-hold 1.1] [--t-tear 0.6]
        [--bake-look A] [--eyes-then x1,y1,x2,y2]
  uv run workflows/tape-morph.py still OUT.png T [same options]        one frame at clip time T
  from importlib.machinery import SourceFileLoader; tm = SourceFileLoader("tape_morph", "workflows/tape-morph.py").load_module(); tm.render(...)

--now is a video (or an image).  A 9:16 clip (1080x1920) is used as it is: the build hands it the frames of the SAME shot it replaces (rendered by the kit, the same
crop / head track / push-in), so the live frames stay in sync with the voice.  A 16:9 clip is cropped 9:16 around the detected eyes (a quick TEST only).
--bake-look A grades + sharpens the NOW frames with the job's POP look (grade-picture.py LOOK A, then the 0.55 / 0.40 unsharp pair) because a card (an mg-*.mp4
B shot) is excluded from both passes: the face inside the morph then matches the graded face shots on either side.
Clip time 0 = NOW frame 0.  Timings are seconds from the clip start.
"""
import argparse, math, os, subprocess, sys
import cv2, numpy as np

W, H = 1080, 1920
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, ".."))
MODEL = os.path.join(REPO, "assets", "models", "face_detection_yunet_2023mar.onnx")
CYAN, RED = np.array([255, 235, 60], np.float32), np.array([60, 60, 255], np.float32)      # BGR: cyan-white (then) / red (now) outline tints


def smooth(x):
    x = np.clip(x, 0.0, 1.0)
    return x * x * (3 - 2 * x)


_DET = {}
_GP = None


def eyes_of(img_bgr, thr=0.5):
    """(x1, y1, x2, y2): the two eyes of the largest face, image-left eye first; None when no face."""
    h, w = img_bgr.shape[:2]
    s = min(1.0, 1280 / max(h, w))
    im = cv2.resize(img_bgr, (int(round(w * s)), int(round(h * s)))) if s < 1 else img_bgr
    key = (im.shape[1], im.shape[0], thr)
    if key not in _DET:
        _DET[key] = cv2.FaceDetectorYN.create(MODEL, "", (im.shape[1], im.shape[0]), thr, 0.3, 5000)
    _, f = _DET[key].detect(im)
    if f is None or not len(f):
        return None
    r = max(f, key=lambda v: v[2] * v[3])
    a, b = (float(r[4]) / s, float(r[5]) / s), (float(r[6]) / s, float(r[7]) / s)
    if a[0] > b[0]:
        a, b = b, a
    return a[0], a[1], b[0], b[1]


class NowFrames:
    """The NOW picture as 1080x1920 BGR frames: an image (held) or a video (read at its own fps)."""
    def __init__(self, path, ss=0.0, n=None, fps=30.0, crop_eyes=None):
        self.frames = []
        ext = os.path.splitext(path)[1].lower()
        if ext in (".png", ".jpg", ".jpeg", ".webp"):
            im = cv2.imread(path)
            self.frames = [self._fit(im)] * (n or 1)
            return
        cap = cv2.VideoCapture(path)
        cap.set(cv2.CAP_PROP_POS_MSEC, ss * 1000.0)
        ok, f = cap.read()
        sh, sw = f.shape[:2]
        crop_x = None
        if (sw, sh) != (W, H) and sw / sh > 0.7:                       # a 16:9 test clip: crop 9:16 around the eyes of its first frame
            e = eyes_of(f)
            cx = (e[0] + e[2]) / 2 if e else sw / 2
            cw = int(round(sh * 9 / 16)); crop_x = int(min(max(cx - cw / 2, 0), sw - cw))
        k = 0
        while ok and (n is None or k < n):
            if crop_x is not None:
                f = f[:, crop_x:crop_x + int(round(sh * 9 / 16))]
            self.frames.append(cv2.resize(f, (W, H), interpolation=cv2.INTER_CUBIC) if f.shape[:2] != (H, W) else f)
            ok, f = cap.read(); k += 1
        cap.release()

    @staticmethod
    def _fit(im):
        h, w = im.shape[:2]
        s = max(W / w, H / h)
        r = cv2.resize(im, (int(math.ceil(w * s)), int(math.ceil(h * s))), interpolation=cv2.INTER_CUBIC)
        y0, x0 = (r.shape[0] - H) // 2, (r.shape[1] - W) // 2
        return r[y0:y0 + H, x0:x0 + W]

    def __len__(self):
        return len(self.frames)

    def __getitem__(self, k):
        return self.frames[min(max(k, 0), len(self.frames) - 1)]


def bake(frame_bgr, look="A"):
    """The POP grade (grade-picture.py LOOK[look]) and the 0.55 / 0.40 luma unsharp pair, so the face matches the graded face shots around the card."""
    global _GP
    if _GP is None:
        from importlib.machinery import SourceFileLoader
        _GP = SourceFileLoader("grade_picture", os.path.join(HERE, "grade-picture.py")).load_module()
    gp = _GP
    a = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2RGB).astype(np.float32) / 255
    g = gp.grade(a, gp.LOOK[look])
    y = cv2.cvtColor((g * 255 + 0.5).astype(np.uint8), cv2.COLOR_RGB2YCrCb)
    l = y[..., 0].astype(np.float32)
    l = l + 0.55 * (l - cv2.GaussianBlur(l, (7, 7), 1.6))
    l = l + 0.40 * (l - cv2.GaussianBlur(l, (3, 3), 0.8))
    y[..., 0] = np.clip(l, 0, 255).astype(np.uint8)
    return cv2.cvtColor(cv2.cvtColor(y, cv2.COLOR_YCrCb2RGB), cv2.COLOR_RGB2BGR)


class Morph:
    def __init__(self, then_path, now, fps=30.0, t_hold=1.1, t_tear=0.6, t_settle=0.45, eyes_then=None, bake_look=None, seed=7):
        self.fps, self.t_hold, self.t_tear, self.t_settle, self.seed = fps, t_hold, t_tear, t_settle, seed
        self.then = cv2.imread(then_path)
        assert self.then is not None, then_path
        et = eyes_then or eyes_of(self.then)
        assert et, "no face found in the THEN still: pass --eyes-then x1,y1,x2,y2"
        self.et = et
        self.now = now
        self.bake = bake_look
        self.bg = self._plate()
        # NOW eye targets for every frame (detected on a half-size copy), then smoothed: the THEN still follows today's eyes through the tear
        n = len(now)
        raw = []
        for k in range(n):
            e = eyes_of(now[k], 0.4)
            raw.append(e)
        last = next((e for e in raw if e), None)
        assert last, "no face found in the NOW frames"
        fill = []
        for e in raw:
            last = e or last
            fill.append(last)
        arr = np.array(fill, np.float32)
        k = max(1, int(round(0.12 * fps)))
        ker = np.exp(-0.5 * (np.arange(-3 * k, 3 * k + 1) / k) ** 2); ker /= ker.sum()
        pad = np.pad(arr, ((3 * k, 3 * k), (0, 0)), mode="edge")
        self.E = np.stack([np.convolve(pad[:, c], ker, mode="valid") for c in range(4)], 1)
        self.t_a = max(0.0, t_hold - 0.15)

    def _plate(self):
        """What the still is feathered into: the still's own border colour (a portrait's dark ground continues), with a soft vertical falloff.  Never a blurred copy of the face."""
        h, w = self.then.shape[:2]
        m = max(4, int(0.04 * min(h, w)))
        edge = np.concatenate([self.then[:m].reshape(-1, 3), self.then[-m:].reshape(-1, 3), self.then[:, :m].reshape(-1, 3), self.then[:, -m:].reshape(-1, 3)])
        c = np.median(edge, axis=0).astype(np.float32) * 0.85
        g = (0.78 + 0.22 * np.linspace(1, 0, H, dtype=np.float32))[:, None, None]
        return np.clip(np.ones((H, W, 3), np.float32) * c * g, 0, 255).astype(np.uint8)

    def _target(self, k):
        e = self.E[min(k, len(self.E) - 1)]
        ka = int(round(self.t_a * self.fps))
        if k >= ka:
            return e
        e0 = self.E[min(ka, len(self.E) - 1)]                           # before the tear the still holds still on today's eyes at t_a, with a steady push-in about the eye centre
        s = 1.0 + 0.025 * (k - ka) / self.fps
        cx, cy = (e0[0] + e0[2]) / 2, (e0[1] + e0[3]) / 2
        return np.array([cx + (e0[0] - cx) * s, cy + (e0[1] - cy) * s, cx + (e0[2] - cx) * s, cy + (e0[3] - cy) * s], np.float32)

    def then_frame(self, k):
        t = self._target(k)
        p1, p2 = np.array(self.et[:2], np.float32), np.array(self.et[2:], np.float32)
        q1, q2 = t[:2], t[2:]
        d_p, d_q = p2 - p1, q2 - q1
        s = float(np.hypot(*d_q) / np.hypot(*d_p))
        th = math.atan2(d_q[1], d_q[0]) - math.atan2(d_p[1], d_p[0])
        c, sn = s * math.cos(th), s * math.sin(th)
        pm, qm = (p1 + p2) / 2, (q1 + q2) / 2
        M = np.array([[c, -sn, qm[0] - (c * pm[0] - sn * pm[1])], [sn, c, qm[1] - (sn * pm[0] + c * pm[1])]], np.float32)
        warped = cv2.warpAffine(self.then, M, (W, H), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_CONSTANT)
        m = cv2.warpAffine(np.ones(self.then.shape[:2], np.float32), M, (W, H), flags=cv2.INTER_LINEAR)
        m = cv2.GaussianBlur(cv2.erode(m, np.ones((41, 41), np.uint8)), (0, 0), 26)[..., None]      # a wide soft edge: the rotated still's rectangle never shows
        return (warped.astype(np.float32) * m + self.bg.astype(np.float32) * (1 - m))

    # ---- the VHS skin ---------------------------------------------------------------------------------------------
    @staticmethod
    def skin(img, I, k, rng, amt=1.0):
        """img float32 BGR 0..255; I = glitch intensity 0..1; amt = how much of the always-on tape look (scanlines, fringe, head-switching band, grain) is left: 1 on the
        still and in the tear, falling to 0 as the glitch settles, so the NOW picture ends CLEAN (the quote freezes its last frame)."""
        h, w = img.shape[:2]
        out = img
        rows = np.arange(h)
        # row jitter: a vertically-smooth noise, a little always, a lot in the tear
        n = rng.normal(0, 1, h // 6 + 2)
        jit = np.interp(rows / 6.0, np.arange(len(n)), n) * (0.8 * amt + 7.0 * I)
        # head-switching band along the bottom 46 px: strong sideways wobble, always
        jit[-46:] += (rng.normal(0, 9 + 18 * I, 46) + 14) * max(amt, I)
        # tear bands
        nb = int(round(2 * amt)) + int(10 * I)
        for _ in range(nb):
            y0 = int(rng.integers(0, h - 12)); bh = int(rng.integers(6, 70)); dx = float(rng.choice([-1, 1]) * rng.uniform(18, 120) * (0.25 * amt + I))
            jit[y0:y0 + bh] += dx * (rng.random() < 0.9)
        out = _shift_rows(out, jit)
        # RGB fringe: B left, R right
        f = int(round(2 * amt + 12 * I))
        out = out.copy()
        out[..., 2] = np.roll(out[..., 2], f, axis=1)
        out[..., 0] = np.roll(out[..., 0], -f, axis=1)
        # scanlines (every other row dimmer), grain, a touch of contrast
        sl = 1.0 - (0.10 * amt + 0.16 * I) * (rows % 2)[:, None, None]
        out = out * sl
        out = out + rng.normal(0, 3.5 * amt + 12 * I, (h, w, 1)).astype(np.float32)
        out = (out - 128) * (1.0 + 0.04 * amt + 0.1 * I) + 128
        return out

    def frame(self, k):
        t = k / self.fps
        t0, t1 = self.t_hold, self.t_hold + self.t_tear
        tm = (t0 + t1) / 2
        I0 = 0.20
        if t < self.t_a:
            I = I0
        elif t < tm:
            I = I0 + (1 - I0) * smooth((t - self.t_a) / (tm - self.t_a))
        else:
            I = max(0.0, math.exp(-(t - tm) / (self.t_settle * 0.7)) * 1.0)
            I = I if t < t1 + self.t_settle * 0.85 else 0.0
        p = (t - t0) / self.t_tear
        rng = np.random.default_rng(self.seed * 1000 + int(k * 15 / self.fps + 1e-6))
        A = self.then_frame(k)
        B = self.now[k].astype(np.float32)
        if self.bake:
            B = bake(self.now[k], self.bake).astype(np.float32)
        h = H
        if p <= 0:
            mix = A
            outl = 0.0
        elif p >= 1:
            mix = B
            outl = 0.0
        else:
            # bands switch from then to now at different moments
            brng = np.random.default_rng(self.seed)
            thr = np.zeros(h, np.float32); y = 0
            while y < h:
                bh = int(brng.integers(10, 110)); thr[y:y + bh] = brng.uniform(0.0, 0.7); y += bh
            wrow = smooth((p * 1.45 - thr) / 0.30)[:, None, None]
            wrow = np.clip(wrow, 0, 1)
            mix = A * (1 - wrow) + B * wrow
            outl = math.sin(math.pi * p) ** 0.8
        amt = 1.0 if t < t1 else float(max(0.0, 1.0 - smooth((t - t1) / max(self.t_settle, 1e-3))))
        if amt <= 0.0 and I <= 0.0:
            return np.clip(mix, 0, 255).astype(np.uint8)                   # settled: the NOW frame untouched
        out = self.skin(mix, I, k, rng, amt)
        if outl > 0.02:                                                # the DOUBLED OUTLINE while both faces overlap: then = cyan, now = red, 6 px apart
            ga = cv2.Canny(cv2.cvtColor(np.clip(A, 0, 255).astype(np.uint8), cv2.COLOR_BGR2GRAY), 70, 160)
            gb = cv2.Canny(cv2.cvtColor(np.clip(B, 0, 255).astype(np.uint8), cv2.COLOR_BGR2GRAY), 70, 160)
            ga = cv2.GaussianBlur(cv2.dilate(ga, np.ones((2, 2), np.uint8)).astype(np.float32) / 255, (0, 0), 1.0)
            gb = cv2.GaussianBlur(cv2.dilate(gb, np.ones((2, 2), np.uint8)).astype(np.float32) / 255, (0, 0), 1.0)
            ga = np.roll(ga, -7, axis=1); gb = np.roll(gb, 7, axis=1)
            out = out + outl * 0.8 * (ga[..., None] * CYAN + gb[..., None] * RED) * 0.9
        if 0 < p < 1.05 or (t0 - 0.2) < t < (t1 + 0.25):               # the tracking line: a bright noisy band rolling down through the tear
            q = (t - (t0 - 0.15)) / (self.t_tear + 0.35)
            if 0 <= q <= 1:
                cy = int(q * (h + 200) - 100)
                y0, y1 = max(cy - 9, 0), min(cy + 9, h)
                if y1 > y0:
                    band = rng.normal(210, 40, (y1 - y0, out.shape[1], 1)).astype(np.float32)
                    out[y0:y1] = out[y0:y1] * 0.35 + band * 0.65
        return np.clip(out, 0, 255).astype(np.uint8)


def _shift_rows(img, dx):
    """Shift each row of img sideways by dx[row] px (edge-clamped), vectorised through remap."""
    h, w = img.shape[:2]
    xs = (np.arange(w, dtype=np.float32)[None, :] - dx[:, None].astype(np.float32))
    xs = np.clip(xs, 0, w - 1).astype(np.float32)
    ys = np.repeat(np.arange(h, dtype=np.float32)[:, None], w, axis=1)
    return cv2.remap(img, xs, ys, cv2.INTER_LINEAR)


def render(out, then, now, fps=30.0, dur=3.2, t_hold=1.1, t_tear=0.6, bake_look=None, now_ss=0.0, eyes_then=None, crf=14):
    n = int(round(dur * fps))
    nf = now if isinstance(now, NowFrames) else NowFrames(now, now_ss, n, fps)
    m = Morph(then, nf, fps, t_hold, t_tear, eyes_then=eyes_then, bake_look=bake_look)
    enc = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "bgr24", "-s", f"{W}x{H}", "-r", str(fps), "-i", "-",
                            "-c:v", "libx264", "-crf", str(crf), "-pix_fmt", "yuv420p", "-preset", "medium", out], stdin=subprocess.PIPE)
    for k in range(n):
        enc.stdin.write(m.frame(k).tobytes())
    enc.stdin.close(); enc.wait()
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=["render", "still"])
    ap.add_argument("out"); ap.add_argument("t", nargs="?", type=float)
    ap.add_argument("--then", required=True); ap.add_argument("--now", required=True)
    ap.add_argument("--now-ss", type=float, default=0.0); ap.add_argument("--fps", type=float, default=30.0)
    ap.add_argument("--dur", type=float, default=3.2); ap.add_argument("--t-hold", type=float, default=1.1); ap.add_argument("--t-tear", type=float, default=0.6)
    ap.add_argument("--bake-look", default=None); ap.add_argument("--eyes-then", default=None)
    a = ap.parse_args()
    et = tuple(float(v) for v in a.eyes_then.split(",")) if a.eyes_then else None
    if a.mode == "render":
        render(a.out, a.then, a.now, a.fps, a.dur, a.t_hold, a.t_tear, a.bake_look, a.now_ss, et)
        print("wrote", a.out)
    else:
        n = int(round(a.dur * a.fps))
        nf = NowFrames(a.now, a.now_ss, n, a.fps)
        m = Morph(a.then, nf, a.fps, a.t_hold, a.t_tear, eyes_then=et, bake_look=a.bake_look)
        cv2.imwrite(a.out, m.frame(int(round(a.t * a.fps))))


if __name__ == "__main__":
    main()
