# /// script
# requires-python = ">=3.10"
# dependencies = ["opencv-python-headless", "numpy", "pillow"]
# ///
"""exhibit-grid.py: the EXHIBIT GRID scene (kit effect, FX-25 of research/effects-catalog; first used on Scott D. Clary x Eric Cole "Never Eat Steak With McAfee", 2026-11-11).

Evidence as OBJECTS.  Each noun the story needs is a real cut-out photo that LANDS on an endless near-black perspective grid floor, on its spoken word:
  1. a pinhole camera looks down at a floor of thin grey grid lines (a few % brightness, fading into black with distance, a soft pool of light under the stage),
  2. an object falls from above (motion-blurred), lands lying flat in the floor's own perspective with a tiny bounce, a contact shadow that tightens as it lands,
     and a ring of light that runs through the grid lines from the point of impact,
  3. its label is printed ON the floor in the same perspective (wide-tracked caps, "EXHIBIT A: SUSHI") and wipes in left to right,
  4. the camera never stops: a slow dolly and crane over the whole scene, so the pieces already on the floor keep drifting while the next one lands.
Learned from LEMMiNO ("The Search For D. B. Cooper", FX-25: each physical piece of evidence is a cut-out object lying on an infinite dark perspective grid floor, thin grey
lines fading to black at the edges, a label in the floor's perspective).  Everything but the object photos is drawn in code.  No sound (the build cues its usual whip swish).

  uv run workflows/exhibit-grid.py render OUT.mp4 --scene scene.json [--fps 30]
  uv run workflows/exhibit-grid.py still OUT.png T --scene scene.json            one frame at clip time T (look at it before a render)
  from importlib.machinery import SourceFileLoader; eg = SourceFileLoader("exhibit_grid", "workflows/exhibit-grid.py").load_module(); eg.render(out, scene, fps=30)

scene.json (SECONDS from the clip start; the build computes the times from the transcript):
  {"dur": 5.4,
   "camera": {"p0": 56, "p1": 52, "h0": 3.4, "h1": 2.9, "z0": -1.0, "z1": 0.3, "x0": 0.0, "x1": 0.0, "f": 1450, "cy": 560},      # pitch (deg, down), height, z, x of the camera at t=0 and t=dur; f px; cy = the horizon's pixel row offset (principal point y)
   "items": [{"id": "a", "sprite": "ref/cut/sushi_oval.png", "t": 0.9, "X": 0.0, "Z": 3.2, "w": 1.7, "rot": 8,                              # t = the moment it TOUCHES the floor
              "fall": 0.26, "y0": 2.6, "label": "EXHIBIT A: SUSHI", "label_dt": 0.12, "label_w": 2.8, "label_dz": -1.15}, ...],
   "dust": true, "grade": {"vignette": 0.45}}
Sprites are RGBA, tight-cropped; `w` is the world width of the sprite's long side lying along the floor's X axis (rotated by `rot` degrees about the vertical).
"""
import argparse, json, math, os, subprocess, sys
import cv2, numpy as np
from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1920
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, ".."))
FONT_DIR = os.path.join(REPO, "presets", "youtube-shorts", "onyx-samples-youtube", "kit", "fonts")
LABEL_FONT = os.path.join(FONT_DIR, "IBMPlexMono-SemiBold.ttf")
DEF_CAM = dict(p0=56.0, p1=52.0, h0=3.4, h1=2.9, z0=-1.0, z1=0.3, x0=0.0, x1=0.0, f=1450.0, cy=560.0)


def ease(p):
    p = min(1.0, max(0.0, p)); return p * p * (3 - 2 * p)


def inout(p):
    p = min(1.0, max(0.0, p)); return 0.5 * (1 - math.cos(math.pi * p))


class Camera:
    """Pinhole camera: position (x, h, z), pitch p degrees looking DOWN the +z axis; pixel (px, py) <-> floor (X, Z)."""

    def __init__(self, c, t, dur):
        k = inout(t / max(dur, 1e-6)) if dur > 0 else 0.0
        mix = lambda a, b: a + (b - a) * k
        self.p = math.radians(mix(c["p0"], c["p1"])); self.h = mix(c["h0"], c["h1"]); self.z = mix(c["z0"], c["z1"]); self.x = mix(c["x0"], c["x1"])
        self.f = float(c["f"]); self.cx0 = W / 2.0; self.cy0 = float(c["cy"])
        self.sp, self.cp = math.sin(self.p), math.cos(self.p)

    def project(self, X, y, Z):
        """world (X, y, Z) -> pixel; arrays or scalars."""
        vx, vy, vz = X - self.x, y - self.h, Z - self.z
        zc = vy * (-self.sp) + vz * self.cp                    # along the view direction d = (0, -sp, cp)
        yc = vy * self.cp + vz * self.sp                       # along the up vector u = (0, cp, sp)
        zc = np.maximum(zc, 1e-3)
        return self.cx0 + self.f * vx / zc, self.cy0 - self.f * yc / zc

    def floor(self, px, py):
        """pixel arrays -> (X, Z, depth, ok) on y = 0."""
        dx = (px - self.cx0)
        du = (self.cy0 - py)
        dir_y = -self.sp * self.f + self.cp * du
        ok = dir_y < -1e-3
        t = np.where(ok, self.h / np.where(ok, -dir_y, 1.0), 0.0)
        X = self.x + t * dx
        Z = self.z + t * (self.cp * self.f + self.sp * du)
        return X, Z, t * self.f, ok


def label_tex(text, tracking=0.26, px=64):
    """RGBA texture of a wide-tracked caps label (white, soft glow), the text running left -> right."""
    f = ImageFont.truetype(LABEL_FONT, px)
    ws = [f.getlength(ch) for ch in text]; gap = px * tracking
    w = int(sum(ws) + gap * (len(text) - 1) + 40); h = int(px * 1.5)
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(im); x = 20
    for ch, cw in zip(text, ws):
        d.text((x, h * 0.18), ch, font=f, fill=(238, 240, 245, 255)); x += cw + gap
    a = np.array(im)
    return a, (w, h)


class Item:
    def __init__(self, it, base):
        self.id = it.get("id", "?"); self.t = float(it["t"]); self.X = float(it["X"]); self.Z = float(it["Z"]); self.w = float(it["w"]); self.rot = math.radians(it.get("rot", 0.0))
        self.fall = float(it.get("fall", 0.26)); self.y0 = float(it.get("y0", 2.6)); self.tilt0 = math.radians(it.get("spin0", 14.0))
        self.glow = float(it.get("ripple", 1.0)); self.scale_pop = float(it.get("pop", 0.035))
        sp = it["sprite"]; sp = sp if os.path.isabs(sp) else os.path.join(base, sp)
        im = Image.open(sp).convert("RGBA"); self.spr = np.array(im); self.ar = im.height / im.width      # RGBA uint8
        self.h = self.w * self.ar
        self.label = it.get("label"); self.label_t = self.t + float(it.get("label_dt", 0.12)); self.label_w = float(it.get("label_w", 2.8)); self.label_dz = float(it.get("label_dz", -(self.h / 2 + 0.55)))
        self.label_dx = float(it.get("label_dx", 0.0)); self.label_wipe = float(it.get("label_wipe", 0.38))
        if self.label:
            self.ltex, (lw, lh) = label_tex(self.label); self.label_h = self.label_w * lh / lw
        self._cache = {}

    def height(self, t):
        """height above the floor (world units): a fall (ease-in), a small bounce, then rest. None before the fall starts."""
        ts = self.t - self.fall
        if t < ts: return None
        if t < self.t:
            p = (t - ts) / self.fall; return self.y0 * (1 - p * p)
        q = t - self.t
        return 0.12 * max(0.0, math.sin(min(q / 0.17, 1.0) * math.pi)) * (1 - min(q / 0.17, 1.0) * 0.5) if q < 0.17 else 0.0

    def corners(self, y, scale=1.0, spin=0.0):
        hw, hh = self.w / 2 * scale, self.h / 2 * scale
        c, s = math.cos(self.rot + spin), math.sin(self.rot + spin)
        pts = [(-hw, hh), (hw, hh), (hw, -hh), (-hw, -hh)]        # sprite TL, TR, BR, BL: the sprite's TOP edge is the far edge (larger Z)
        return [(self.X + x * c - z * s, y, self.Z + x * s + z * c) for x, z in pts]


def warp_quad(spr_rgba, quad_px, out_w, out_h, pad=0, box=None):
    """warp a premultiplied float RGBA sprite through the 4 pixel corners (TL, TR, BR, BL) into a crop of the frame: returns (crop, x0, y0) or None when it is off screen.
    `box` = (x0, y0, x1, y1) forces the crop (so several sub-frames share one canvas)."""
    sh, sw = spr_rgba.shape[:2]
    dst = np.array(quad_px, np.float32)
    if box is None:
        x0 = int(max(0, math.floor(dst[:, 0].min()) - pad)); y0 = int(max(0, math.floor(dst[:, 1].min()) - pad))
        x1 = int(min(out_w, math.ceil(dst[:, 0].max()) + pad)); y1 = int(min(out_h, math.ceil(dst[:, 1].max()) + pad))
    else:
        x0, y0, x1, y1 = box
    if x1 <= x0 or y1 <= y0: return None
    wpx = max(np.hypot(*(dst[1] - dst[0])), np.hypot(*(dst[2] - dst[3])), 8)
    k = min(1.0, (wpx * 1.6) / sw)
    spr = cv2.resize(spr_rgba, (max(8, int(sw * k)), max(8, int(sh * k))), interpolation=cv2.INTER_AREA) if k < 1.0 else spr_rgba
    h2, w2 = spr.shape[:2]
    src = np.array([[0, 0], [w2, 0], [w2, h2], [0, h2]], np.float32)
    M = cv2.getPerspectiveTransform(src, dst - np.array([x0, y0], np.float32))
    return cv2.warpPerspective(spr, M, (x1 - x0, y1 - y0), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT, borderValue=(0, 0, 0, 0)), x0, y0


def over_roi(img, crop, x0, y0, mult=1.0, colour_scale=255.0):
    """composite a premultiplied RGBA crop (0..1) onto the float RGB frame at (x0, y0)."""
    h, w = crop.shape[:2]
    reg = img[y0:y0 + h, x0:x0 + w]
    a = crop[..., 3:4] * mult
    reg[:] = reg * (1.0 - a) + crop[..., :3] * colour_scale * mult


class Scene:
    def __init__(self, scene, base="."):
        self.s = scene; self.dur = float(scene["dur"]); self.cam = {**DEF_CAM, **scene.get("camera", {})}
        self.items = [Item(i, base) for i in scene["items"]]
        for it in self.items:                                      # premultiplied float sprites
            a = it.spr.astype(np.float32) / 255.0; a[..., :3] *= a[..., 3:4]; it.fspr = a
        rng = np.random.default_rng(5)
        self.dust = rng.random((70, 4)) if scene.get("dust", True) else None
        self.vig = float(scene.get("grade", {}).get("vignette", 0.5))
        self.gridmax = float(scene.get("grid_depth", 15.0))
        self.px, self.py = np.meshgrid(np.arange(W, dtype=np.float32) + 0.5, np.arange(H, dtype=np.float32) + 0.5)

    # ---- the floor ------------------------------------------------------------------------------------------------------------------
    def floor_img(self, cam, t):
        X, Z, depth, ok = cam.floor(self.px, self.py)
        gx = np.abs(np.gradient(X, axis=1)) + np.abs(np.gradient(X, axis=0)); gz = np.abs(np.gradient(Z, axis=1)) + np.abs(np.gradient(Z, axis=0))
        spacing = 0.5
        def lines(C, g):
            d = np.abs(((C / spacing) + 0.5) % 1.0 - 0.5) * spacing
            w = np.maximum(g * 0.9, 1e-4)
            return np.clip(1.0 - d / w, 0.0, 1.0) * np.clip(0.55 / (w / spacing * 14.0 + 0.55), 0.0, 1.0)     # thin, and fade out where the lines get denser than a pixel
        g = np.maximum(lines(X, gx), lines(Z, gz))
        major = np.maximum(np.clip(1.0 - np.abs(((X / 2.0) + 0.5) % 1.0 - 0.5) * 2.0 / np.maximum(gx * 0.9, 1e-4), 0, 1), np.clip(1.0 - np.abs(((Z / 2.0) + 0.5) % 1.0 - 0.5) * 2.0 / np.maximum(gz * 0.9, 1e-4), 0, 1))
        fade = np.clip(1.0 - depth / (self.gridmax * cam.f * 0.9 / 1.0), 0.0, 1.0) ** 1.6
        radial = np.exp(-(((X - 0.0) / 5.5) ** 2 + ((Z - 3.2) / 6.5) ** 2))          # the soft pool of light under the stage
        # ripples: a ring of light running through the grid from every impact
        rip = np.zeros_like(X)
        for it in self.items:
            q = t - it.t
            if 0 <= q < 0.9 and it.glow > 0:
                r = 7.0 * q ** 0.8 * 1.15; dist = np.sqrt((X - it.X) ** 2 + (Z - it.Z) ** 2)
                rip += np.exp(-((dist - r) / 0.28) ** 2) * (1 - q / 0.9) ** 1.5 * it.glow
        lum = (0.27 * g + 0.15 * major) * (0.30 + 0.85 * radial) * fade * (1.0 + 3.2 * rip)
        base = (0.020 + 0.055 * radial * fade)
        col = np.stack([base * 0.95 + lum * 0.88, base * 1.00 + lum * 0.93, base * 1.12 + lum * 1.00], axis=-1)
        col[~ok] = 0.012
        return np.clip(col * 255.0, 0, 255).astype(np.float32)

    # ---- one frame --------------------------------------------------------------------------------------------------------------------
    def draw_items(self, img, cam, t):
        for it in sorted(self.items, key=lambda i: -i.Z):               # far first
            y = it.height(t)
            if y is None: continue
            falling = (it.t - it.fall <= t < it.t)
            sub = 9 if falling else 1
            shutter = 0.017                                              # a 180-degree shutter at 30 fps: smooth blur, not ghost copies
            quads = []
            for k in range(sub):
                tt = t - shutter * (sub - 1 - k) / max(sub - 1, 1) if sub > 1 else t
                yy = it.height(tt)
                if yy is None: continue
                q = tt - it.t
                scale = 1.0 + (it.scale_pop * math.sin(min(max(q / 0.12, 0.0), 1.0) * math.pi) if q >= 0 else 0.0)
                spin = it.tilt0 * (1 - min(max((tt - (it.t - it.fall)) / it.fall, 0.0), 1.0)) if tt < it.t else 0.0
                quads.append((tt, [(float(a), float(b)) for a, b in (cam.project(*c) for c in it.corners(yy, scale, spin))]))
            if not quads: continue
            allx = [p[0] for _, qd in quads for p in qd]; ally = [p[1] for _, qd in quads for p in qd]
            bx0, by0 = int(max(0, math.floor(min(allx)) - 2)), int(max(0, math.floor(min(ally)) - 2)); bx1, by1 = int(min(W, math.ceil(max(allx)) + 2)), int(min(H, math.ceil(max(ally)) + 2))
            # contact shadow first (the footprint on the floor, blurred; light from the upper left: it falls right / toward the camera); none while the object is high in the air
            hh = y; near = max(0.0, 1.0 - hh / max(it.y0, 1e-3)) ** 1.6
            if near > 0.02:
                sc = 1.0 + 0.06 * hh
                sq = [tuple(map(float, cam.project(it.X + 0.05 + 0.10 * hh + (c[0] - it.X) * sc, 0.0, it.Z - 0.04 - 0.10 * hh + (c[2] - it.Z) * sc))) for c in it.corners(0.0)]
                blur = 9 + int(26 * min(hh, 2.0)); blur += 1 - blur % 2
                shadow_spr = np.concatenate([np.zeros_like(it.fspr[..., :3]), it.fspr[..., 3:4]], axis=-1)
                ws = warp_quad(shadow_spr, sq, W, H, pad=blur + 4)
                if ws is not None:
                    crop, x0, y0 = ws
                    al = cv2.GaussianBlur(crop[..., 3], (blur, blur), 0) * (0.72 - 0.35 * min(hh, 2.0) / 2.0) * near
                    reg = img[y0:y0 + al.shape[0], x0:x0 + al.shape[1]]; reg *= (1.0 - al[..., None])
            if bx1 <= bx0 or by1 <= by0: continue
            acc = np.zeros((by1 - by0, bx1 - bx0, 4), np.float32)
            for tt, qd in quads:
                w_ = warp_quad(it.fspr, qd, W, H, box=(bx0, by0, bx1, by1))
                if w_ is None: continue
                acc += w_[0] * min(1.0, max(0.0, (tt - (it.t - it.fall)) / 0.06))
            acc /= len(quads)
            over_roi(img, acc, bx0, by0)
        return img

    def draw_labels(self, img, cam, t):
        for it in self.items:
            if not it.label or t < it.label_t: continue
            p = min(1.0, (t - it.label_t) / max(it.label_wipe, 1e-3)); p = 1 - (1 - p) ** 2
            tex = it.ltex.astype(np.float32) / 255.0; th, tw = tex.shape[:2]
            tex[..., :3] *= tex[..., 3:4]
            cut = max(1, int(tw * p)); tex[:, cut:, :] = 0.0                                  # the left -> right wipe
            cx, cz = it.X + it.label_dx, it.Z + it.label_dz
            hw, hh = it.label_w / 2, it.label_h / 2
            quad = [cam.project(cx - hw, 0.0, cz + hh), cam.project(cx + hw, 0.0, cz + hh), cam.project(cx + hw, 0.0, cz - hh), cam.project(cx - hw, 0.0, cz - hh)]
            wq = warp_quad(tex, [(float(a), float(b)) for a, b in quad], W, H, pad=2)
            if wq is None: continue
            over_roi(img, wq[0], wq[1], wq[2], mult=min(1.0, (t - it.label_t) / 0.1) * 0.80)
        return img

    def frame(self, t):
        cam = Camera(self.cam, t, self.dur)
        img = self.floor_img(cam, t)
        img = self.draw_items(img, cam, t)
        img = self.draw_labels(img, cam, t)
        if self.dust is not None:                                          # sparse film-dust specks (FX-33 flavour), drifting up-left, each twinkling
            for k, (a, b, c, d) in enumerate(self.dust):
                x = (a * W - 14 * t * (0.4 + c)) % W; y = (b * H - 9 * t * (0.3 + d)) % H
                tw = 0.5 + 0.5 * math.sin(t * (1.5 + 2 * c) + 6.28 * d); r = 1 + int(d * 2)
                cv2.circle(img, (int(x), int(y)), r, (150 * tw, 155 * tw, 165 * tw), -1, cv2.LINE_AA)
        yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
        vg = 1.0 - self.vig * np.clip(((xx - W / 2) / (W * 0.78)) ** 2 + ((yy - H * 0.5) / (H * 0.74)) ** 2, 0, 1) ** 1.2
        img *= vg[..., None]
        rng = np.random.default_rng(int(t * 1000) % 977); img += rng.normal(0, 1.0, (H, W, 1)).astype(np.float32)
        return np.clip(img, 0, 255).astype(np.uint8)


def load_scene(path_or_dict, base="."):
    s = path_or_dict if isinstance(path_or_dict, dict) else json.load(open(path_or_dict, encoding="utf-8"))
    return Scene(s, base)


_SC = None


def _init(scene, base):
    global _SC
    _SC = load_scene(scene, base)


def _frame_bytes(i_fps):
    i, fps = i_fps
    return _SC.frame(i / fps).tobytes()


def render(out, scene, fps=30, base=".", workers=4):
    """one frame per time step; frames render in parallel (a process pool: call this through the CLI or from a script's main guard)."""
    sc = load_scene(scene, base); n = int(round(sc.dur * fps))
    enc = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(fps), "-i", "-", "-c:v", "libx264", "-crf", "14", "-pix_fmt", "yuv420p", out], stdin=subprocess.PIPE)
    if workers > 1:
        from concurrent.futures import ProcessPoolExecutor
        with ProcessPoolExecutor(max_workers=workers, initializer=_init, initargs=(scene, base)) as ex:
            for fb in ex.map(_frame_bytes, [(i, fps) for i in range(n)], chunksize=2):
                enc.stdin.write(fb)
    else:
        for i in range(n):
            enc.stdin.write(sc.frame(i / fps).tobytes())
    enc.stdin.close(); enc.wait()
    return n


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("cmd", choices=["render", "still"]); ap.add_argument("out"); ap.add_argument("t", nargs="?", type=float, default=0.0)
    ap.add_argument("--scene", required=True); ap.add_argument("--fps", type=float, default=30); ap.add_argument("--base", default="."); ap.add_argument("--workers", type=int, default=4)
    a = ap.parse_args()
    if a.cmd == "render":
        n = render(a.out, a.scene, a.fps, a.base, a.workers); print(n, "frames ->", a.out)
    else:
        sc = load_scene(a.scene, a.base); Image.fromarray(sc.frame(a.t)).save(a.out); print("still ->", a.out)


if __name__ == "__main__":
    main()
