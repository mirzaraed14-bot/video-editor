# /// script
# requires-python = ">=3.10"
# dependencies = ["opencv-python-headless", "numpy", "pillow"]
# ///
"""ghost-dissolve.py: the GHOST DISSOLVE (kit effect, FX-37 of research/effects-catalog; first used on Scott D. Clary x Eric Cole "Never Eat Steak With McAfee", 2026-11-11).

A QUOTED FACE appears over the person who is quoting it.  While the guest speaks someone else's line ("and he goes, you're right because I might do that"), the real face of that
someone fades up over the live shot as a slow double exposure, matched on the EYES, so the viewer sees WHOSE words these are without a caption, a card or a second copy of the words:
  1. the live shot plays on (the guest's own crop, head track and push-in: the build hands this effect the frames of the SAME shot it replaces),
  2. a cut-out photo of the quoted person (RGBA, background removed) is warped (scale + roll + shift) so ITS eyes sit exactly on the guest's eyes, measured by YuNet in the photo and
     in every live frame (smoothed over ~0.15 s so the ghost glides with the head instead of jittering),
  3. it fades up over `t_full - t_in` s to `alpha` (a long cross-dissolve that STAYS on the double exposure: it never completes), the live frame under it dims a little and the ghost
     is cooled and lifted so it reads as a memory, with a slow breathing push-in; `t_out` fades it away (omit for a hard cut at the end of the clip).
Learned from Patrick Cc: ("50 Cent Was Right About Floyd Mayweather", FX-37 Ghost Dissolve: long dissolves that sit on a visible double exposure, a face ghosted over another picture).
The eye machinery (YuNet, NowFrames, the POP look) is workflows/tape-morph.py's, reused as it is.  No sound.

  uv run workflows/ghost-dissolve.py render OUT.mp4 --ghost GHOST.png --now NOW.mp4 [--now-ss S] [--dur 3.0] [--fps 30] [--t-in 0.0] [--t-full 0.7] [--alpha 0.55] [--t-out T]
        [--bake-look A] [--eyes-ghost x1,y1,x2,y2] [--scale 1.0] [--dx 0 --dy 0]
  uv run workflows/ghost-dissolve.py still OUT.png T [same options]        one frame at clip time T
  from importlib.machinery import SourceFileLoader; gd = SourceFileLoader("ghost_dissolve", "workflows/ghost-dissolve.py").load_module(); gd.render(...)

--now is a video (or an image).  A 9:16 clip (1080x1920) is used as it is; a 16:9 clip is cropped 9:16 around the detected eyes (a quick TEST only).
--ghost is an RGBA PNG (the person cut out, e.g. `npx hyperframes remove-background photo.jpg -o ghost.png`).  Clip time 0 = NOW frame 0.
"""
import argparse, math, os, subprocess
from importlib.machinery import SourceFileLoader
import cv2, numpy as np

W, H = 1080, 1920
HERE = os.path.dirname(os.path.abspath(__file__))
tm = SourceFileLoader("tape_morph", os.path.join(HERE, "tape-morph.py")).load_module()


def smooth(x):
    x = min(1.0, max(0.0, x)); return x * x * (3 - 2 * x)


def eyes_on_rgba(rgba):
    """eyes of the person in an RGBA cut-out (composited over mid-grey for the detector)."""
    a = rgba[..., 3:4].astype(np.float32) / 255.0
    bgr = (rgba[..., :3].astype(np.float32) * a + 128.0 * (1 - a)).astype(np.uint8)
    return tm.eyes_of(bgr, 0.4)


class Ghost:
    def __init__(self, ghost_path, now, fps=30.0, dur=3.0, t_in=0.0, t_full=0.7, alpha=0.55, t_out=None, bake_look=None, eyes_ghost=None, scale=1.0, dx=0.0, dy=0.0, smooth_s=0.15, fade0=2.6, fade1=4.0, static=True):
        self.fps, self.dur, self.t_in, self.t_full, self.alpha, self.t_out, self.bake = fps, dur, t_in, t_full, alpha, t_out, bake_look
        self.scale, self.dx, self.dy = scale, dx, dy
        self.g = cv2.imread(ghost_path, cv2.IMREAD_UNCHANGED); assert self.g is not None and self.g.shape[2] == 4, "ghost must be an RGBA PNG: " + ghost_path
        rgba = cv2.cvtColor(self.g, cv2.COLOR_BGRA2RGBA)
        self.eg = eyes_ghost or eyes_on_rgba(rgba)
        assert self.eg, "no face found in the ghost cut-out: pass --eyes-ghost x1,y1,x2,y2"
        self.now = now
        n = int(round(dur * fps)); self.n = n
        raw = [tm.eyes_of(now[k]) for k in range(n)]
        good = [e for e in raw if e]
        assert good, "no face found in the live frames"
        med = np.median(np.array(good, np.float64), axis=0); dmed = math.hypot(med[2] - med[0], med[3] - med[1])
        # a frame where YuNet finds no face (a head turned away) or a wild one (> 0.7 of the eye distance off the median) takes the median eyes: with the kit's head track the eyes sit on a fixed spot
        fill = []
        for e in raw:
            ok = e is not None and math.hypot((e[0] + e[2]) / 2 - (med[0] + med[2]) / 2, (e[1] + e[3]) / 2 - (med[1] + med[3]) / 2) < 0.7 * dmed * 2.2 and 0.6 < math.hypot(e[2] - e[0], e[3] - e[1]) / dmed < 1.6
            fill.append(e if ok else tuple(med))
        self.detected = sum(1 for e, f in zip(raw, fill) if e is not None and f == e)
        E = np.array(fill, np.float64)                                      # (n, 4)
        self.static = static
        if static: E[:] = med                                                # the kit's head track keeps the eyes on a fixed spot: a STILL anchor never jitters and never fails on a turned head
        r = max(1, int(round(smooth_s * fps)))
        k = np.ones(2 * r + 1) / (2 * r + 1)
        Ep = np.pad(E, ((r, r), (0, 0)), mode="edge")
        self.E = np.stack([np.convolve(Ep[:, j], k, mode="valid") for j in range(4)], axis=1)
        # the ghost, premultiplied float, once
        gf = self.g.astype(np.float32) / 255.0
        ey = (self.eg[1] + self.eg[3]) / 2; dg = math.hypot(self.eg[2] - self.eg[0], self.eg[3] - self.eg[1])
        yy = np.arange(gf.shape[0], dtype=np.float32)[:, None]
        ramp = 1.0 - np.clip((yy - (ey + fade0 * dg)) / max((fade1 - fade0) * dg, 1.0), 0.0, 1.0)          # the body fades out below the chest (no podium edge)
        ramp = ramp * ramp * (3 - 2 * ramp)
        gf[..., 3] = gf[..., 3] * ramp
        self.gpm = np.concatenate([gf[..., :3] * gf[..., 3:4], gf[..., 3:4]], axis=-1)           # BGR premult + alpha

    def a_of(self, t):
        a = self.alpha * smooth((t - self.t_in) / max(self.t_full - self.t_in, 1e-3))
        if self.t_out is not None: a *= 1.0 - smooth((t - self.t_out) / 0.25)
        return a

    def frame(self, k):
        t = k / self.fps
        now = self.now[k]
        if self.bake: now = tm.bake(now, self.bake)
        a = self.a_of(t)
        if a <= 0.002: return now
        e = self.E[min(k, self.n - 1)]
        ex1, ey1, ex2, ey2 = self.eg
        dn = math.hypot(e[2] - e[0], e[3] - e[1]); dg = math.hypot(ex2 - ex1, ey2 - ey1)
        s = dn / dg * self.scale * (1.0 + 0.025 * max(0.0, t - self.t_in))                  # the slow breathing push-in
        rot = math.atan2(e[3] - e[1], e[2] - e[0]) - math.atan2(ey2 - ey1, ex2 - ex1)
        c, sn = math.cos(rot) * s, math.sin(rot) * s
        gm = ((ex1 + ex2) / 2, (ey1 + ey2) / 2); nm = ((e[0] + e[2]) / 2 + self.dx, (e[1] + e[3]) / 2 + self.dy)
        M = np.float32([[c, -sn, nm[0] - (c * gm[0] - sn * gm[1])], [sn, c, nm[1] - (sn * gm[0] + c * gm[1])]])
        wg = cv2.warpAffine(self.gpm, M, (W, H), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_CONSTANT, borderValue=(0, 0, 0, 0))
        al = np.clip(wg[..., 3:4], 0, 1)
        al = cv2.GaussianBlur(al, (0, 0), 3.0)[..., None] if al.ndim == 2 else cv2.GaussianBlur(al[..., 0], (0, 0), 3.0)[..., None]       # a soft edge
        col = wg[..., :3] / np.maximum(wg[..., 3:4], 1e-3)                                    # straight colour
        lum = (col[..., 0:1] * 0.114 + col[..., 1:2] * 0.587 + col[..., 2:3] * 0.299)
        col = col * 0.45 + lum * 0.55                                                       # mostly desaturated
        col = np.clip(col * np.array([1.08, 1.00, 0.90], np.float32) * 1.10 + 0.02, 0, 1)    # cooled (BGR: more blue, less red) and lifted: a memory, not a mask
        nowf = now.astype(np.float32) / 255.0
        dim = 1.0 - 0.16 * (a / max(self.alpha, 1e-3))
        out = nowf * dim * (1 - al * a) + col * al * a
        return np.clip(out * 255.0 + 0.5, 0, 255).astype(np.uint8)


def render(out, ghost, now, fps=30.0, dur=3.0, t_in=0.0, t_full=0.7, alpha=0.55, t_out=None, bake_look=None, now_ss=0.0, eyes_ghost=None, scale=1.0, dx=0.0, dy=0.0, crf=14):
    n = int(round(dur * fps))
    nf = now if hasattr(now, "frames") else tm.NowFrames(now, now_ss, n, fps)
    gh = Ghost(ghost, nf, fps, dur, t_in, t_full, alpha, t_out, bake_look, eyes_ghost, scale, dx, dy)
    enc = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "bgr24", "-s", f"{W}x{H}", "-r", str(fps), "-i", "-", "-c:v", "libx264", "-crf", str(crf), "-pix_fmt", "yuv420p", out], stdin=subprocess.PIPE)
    for k in range(n):
        enc.stdin.write(gh.frame(k).tobytes())
    enc.stdin.close(); enc.wait()
    return n


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("cmd", choices=["render", "still"]); ap.add_argument("out"); ap.add_argument("t", nargs="?", type=float, default=0.0)
    ap.add_argument("--ghost", required=True); ap.add_argument("--now", required=True); ap.add_argument("--now-ss", type=float, default=0.0, dest="now_ss")
    ap.add_argument("--dur", type=float, default=3.0); ap.add_argument("--fps", type=float, default=30); ap.add_argument("--t-in", type=float, default=0.0, dest="t_in")
    ap.add_argument("--t-full", type=float, default=0.7, dest="t_full"); ap.add_argument("--alpha", type=float, default=0.55); ap.add_argument("--t-out", type=float, default=None, dest="t_out")
    ap.add_argument("--bake-look", default=None, dest="bake_look"); ap.add_argument("--eyes-ghost", default=None, dest="eyes_ghost")
    ap.add_argument("--scale", type=float, default=1.0); ap.add_argument("--dx", type=float, default=0.0); ap.add_argument("--dy", type=float, default=0.0)
    a = ap.parse_args()
    eg = tuple(float(v) for v in a.eyes_ghost.split(",")) if a.eyes_ghost else None
    if a.cmd == "render":
        n = render(a.out, a.ghost, a.now, a.fps, a.dur, a.t_in, a.t_full, a.alpha, a.t_out, a.bake_look, a.now_ss, eg, a.scale, a.dx, a.dy); print(n, "frames ->", a.out)
    else:
        n = int(round(a.dur * a.fps)); nf = tm.NowFrames(a.now, a.now_ss, n, a.fps)
        gh = Ghost(a.ghost, nf, a.fps, a.dur, a.t_in, a.t_full, a.alpha, a.t_out, a.bake_look, eg, a.scale, a.dx, a.dy)
        cv2.imwrite(a.out, gh.frame(min(int(round(a.t * a.fps)), n - 1))); print("still ->", a.out)


if __name__ == "__main__":
    main()
