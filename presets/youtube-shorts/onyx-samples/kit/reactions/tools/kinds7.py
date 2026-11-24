"""kinds7.py: the batch-7 reaction kinds + entrance signatures = mgx6 (-> mgx -> overlays) + everything below, patched in at IMPORT.

  import kinds7            # after mgx6 (mgx7.py does exactly that and keeps mgx6's CLI)
  PYTHONUTF8=1 python mgx7.py <job>/plan.json [--captions] [--mg] [--only id,id] [--check] [--still t ...]

Nothing on disk changes for anyone else (the shared overlays.py / mgx.py / mgx6.py are never edited). Spec: reactions/NEW-KINDS.md.
Keys, defaults and one example per kind: KINDS7.md (next to this file).

KINDS      play_card  portal  scorecard  hl_sweep  inset_cam        (registered in X.NEW / O.SEEKABLE / O.build_mg)
ENTRANCES  tilt  slab  foldx  swing  shutter   plan["entrance"] / g["entrance"], on ANY sprite kind (O.pop_frame) and on the
           curated mgx kinds in WRAP (teaser, teaser2, still_card, era, source_tag, low_title) through a wrapper that transforms the
           kind's HOLD frame as a layer. Exits are the entrance played backwards, 30 % faster. Every transition frame is the average of
           5 premultiplied sub-frames (motion blur). Screen-locked marks (ring, select, spotlight, cursor, loupe, timecode, scrub,
           hl_sweep) are NOT wrapped: a tilt would move them off their target (they keep their own fade).
"""
import io, json, math, os, shutil, subprocess, sys, tempfile, time

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", "..", "..", "..", ".."))
T6 = os.path.dirname(os.path.abspath(__file__))
if T6 not in sys.path: sys.path.insert(0, T6)
import mgx6 as M6                                   # noqa: E402  (imports + patches mgx -> overlays)
X, O = M6.X, M6.O
G = O.G
import numpy as np                                  # noqa: E402
from PIL import Image, ImageChops, ImageDraw, ImageFilter  # noqa: E402

W, H, FPS, GOLD = O.W, O.H, O.FPS_MG, O.GOLD
PANEL = (0, 227, 1080, 1038)                        # the top panel of the SPLIT layout (frame px); every kind takes g["panel"] to override
BEBAS, INTER_B, INTER_R = O.BEBAS, O.INTER_B, O.INTER_R
INTER_SB = next((p for p in (os.path.expanduser("~/AppData/Local/Microsoft/Windows/Fonts/Inter-SemiBold.ttf"), "C:/Windows/Fonts/Inter-SemiBold.ttf",
                             os.path.join(REPO, "assets", "fonts", "Inter-SemiBold.otf")) if os.path.exists(p)), INTER_B)
F, blank, shadowed, rich_line, pill = X.F, X.blank, X.shadowed, X.rich_line, X.pill
WHITE = (255, 255, 255, 255)
MARKER = (242, 193, 78)                             # #F2C14E

# ---------------------------------------------------------------- easing
cl = lambda x, a=0.0, b=1.0: max(a, min(b, x))
e_q5 = lambda u: 1 - (1 - cl(u)) ** 5               # easeOutQuint
e_q4 = lambda u: 1 - (1 - cl(u)) ** 4               # easeOutQuart
e_c3 = lambda u: 1 - (1 - cl(u)) ** 3               # easeOutCubic
e_ex = lambda u: 1.0 if u >= 1 else 1 - 2 ** (-10 * cl(u))     # easeOutExpo
e_io3 = lambda u: (lambda x: 4 * x ** 3 if x < 0.5 else 1 - (-2 * x + 2) ** 3 / 2)(cl(u))
e_io_sine = lambda u: -(math.cos(math.pi * cl(u)) - 1) / 2


# ---------------------------------------------------------------- RGBA helpers
def paste_rgba(fr, im, x, y):
    """alpha_composite im at (x, y) into fr, cropping whatever falls outside fr"""
    x, y = int(round(x)), int(round(y))
    sx0, sy0 = max(0, -x), max(0, -y); sx1, sy1 = min(im.width, fr.width - x), min(im.height, fr.height - y)
    if sx1 <= sx0 or sy1 <= sy0: return
    part = im if (sx0, sy0, sx1, sy1) == (0, 0, im.width, im.height) else im.crop((sx0, sy0, sx1, sy1))
    fr.alpha_composite(part, (x + sx0, y + sy0))


def _pm(im):
    a = np.asarray(im.convert("RGBA"), dtype=np.float32)
    return np.concatenate([a[..., :3] * (a[..., 3:4] / 255.0), a[..., 3:4]], axis=2)


def _unpm(pm):
    al = pm[..., 3:4]
    rgb = np.where(al > 0.5, pm[..., :3] * 255.0 / np.maximum(al, 1e-6), 0)
    return Image.fromarray(np.clip(np.concatenate([rgb, al], axis=2) + 0.5, 0, 255).astype(np.uint8), "RGBA")


def average_renders(rs):
    """[(img, x, y), ...] -> (img, x, y): the mean of the images in PREMULTIPLIED alpha on their union bbox (motion blur)"""
    x0 = min(r[1] for r in rs); y0 = min(r[2] for r in rs)
    x1 = max(r[1] + r[0].width for r in rs); y1 = max(r[2] + r[0].height for r in rs)
    acc = np.zeros((y1 - y0, x1 - x0, 4), np.float32)
    for im, x, y in rs:
        acc[y - y0:y - y0 + im.height, x - x0:x - x0 + im.width] += _pm(im)
    return _unpm(acc / len(rs)), x0, y0


def bbox_alpha(im, thr=12):
    return im.split()[3].point(lambda v: 255 if v >= thr else 0).getbbox()


def shadow_only(sprite, blur, alpha, dy, pad):
    """a black soft shadow of the sprite's alpha on a canvas sprite + 2 pad (the sprite is NOT drawn)"""
    sh = Image.new("RGBA", (sprite.width + 2 * pad, sprite.height + 2 * pad), (0, 0, 0, 0))
    a = sprite.split()[3].point(lambda v: v * alpha // 255)
    blk = Image.new("RGBA", sprite.size, (0, 0, 0, 255)); blk.putalpha(a)
    sh.paste(blk, (pad, pad + dy), blk)
    return sh.filter(ImageFilter.GaussianBlur(blur))


def shift_content(sprite, dx, dy):
    """the sprite's RGB moved by (dx, dy) px (edge-replicated, sub-pixel), its ALPHA kept: the card stays, what is printed on it slides
    inside its own silhouette (the 'content behind a mask' of slab / foldx)"""
    if abs(dx) < 0.05 and abs(dy) < 0.05: return sprite
    a = np.asarray(sprite, dtype=np.float32)
    al = a[..., 3:4]; pm = a[..., :3] * (al / 255.0)
    ex = int(math.ceil(max(abs(dx), abs(dy)))) + 2
    pp = np.pad(pm, ((ex, ex), (ex, ex), (0, 0)), mode="edge"); ap = np.pad(al[..., 0], ((ex, ex), (ex, ex)), mode="edge")
    co = (1, 0, -dx, 0, 1, -dy); sz = (pp.shape[1], pp.shape[0])
    rgb = np.asarray(Image.fromarray(np.clip(pp, 0, 255).astype(np.uint8), "RGB").transform(sz, Image.AFFINE, co, Image.BILINEAR)
                     .crop((ex, ex, ex + sprite.width, ex + sprite.height)), dtype=np.float32)
    sa = np.asarray(Image.fromarray(np.clip(ap, 0, 255).astype(np.uint8), "L").transform(sz, Image.AFFINE, co, Image.BILINEAR)
                    .crop((ex, ex, ex + sprite.width, ex + sprite.height)), dtype=np.float32)[..., None]
    straight = np.where(sa > 0.5, rgb * 255.0 / np.maximum(sa, 1e-6), 0)
    return Image.fromarray(np.clip(np.concatenate([straight, al], axis=2), 0, 255).astype(np.uint8), "RGBA")


def homography(dst, src):
    """PIL PERSPECTIVE coefficients mapping output (dst) px to source px, from 4 corner pairs"""
    A, b = [], []
    for (x, y), (u, v) in zip(dst, src):
        A.append([x, y, 1, 0, 0, 0, -u * x, -u * y]); b.append(u)
        A.append([0, 0, 0, x, y, 1, -v * x, -v * y]); b.append(v)
    return np.linalg.solve(np.array(A, float), np.array(b, float)).tolist()


def warp_quad(im, quad):
    """im drawn onto the quad [(x, y) x4: tl tr br bl] (any origin): (image, x, y) with the image on the quad's bbox"""
    xs = [p[0] for p in quad]; ys = [p[1] for p in quad]
    ox, oy = int(math.floor(min(xs))) - 1, int(math.floor(min(ys))) - 1
    bw, bh = int(math.ceil(max(xs))) - ox + 2, int(math.ceil(max(ys))) - oy + 2
    dst = [(p[0] - ox, p[1] - oy) for p in quad]
    src = [(0, 0), (im.width, 0), (im.width, im.height), (0, im.height)]
    return im.transform((bw, bh), Image.PERSPECTIVE, homography(dst, src), Image.BICUBIC), ox, oy


def rot_about(im, pivot, ang_deg, margin=None):
    """im rotated by ang_deg (counter-clockwise positive) about pivot (px in im): (image, dx, dy), (dx, dy) = the image's top-left
    relative to where the pivot lands"""
    m = margin if margin is not None else int(max(im.width, im.height) * 0.2) + 4
    canvas = Image.new("RGBA", (im.width + 2 * m, im.height + 2 * m), (0, 0, 0, 0)); canvas.paste(im, (m, m))
    out = canvas.rotate(ang_deg, resample=Image.BICUBIC, expand=False, center=(pivot[0] + m, pivot[1] + m))
    return out, -(pivot[0] + m), -(pivot[1] + m)


# ---------------------------------------------------------------- entrance signatures
SIGS = {"tilt": 0.42, "slab": 0.46, "foldx": 0.48, "swing": 0.46, "shutter": 0.40, "riseup": 0.42}      # entrance durations (s); riseup = the play_card default
OUT_K = 0.70                                         # exits: the entrance backwards, 30 % faster
SH_STD = (22, 120, 10)                               # the batch-6 card shadow (blur, alpha, dy)
SHUTTER_ANGLE = 0.5                                  # motion blur: the shutter is open half a frame, 5 sub-frames


def _lerp_alpha(a, b, k):
    aa = np.asarray(a.split()[3], np.float32); ba = np.asarray(b.split()[3], np.float32)
    out = Image.new("RGBA", a.size, (0, 0, 0, 0)); out.putalpha(Image.fromarray((aa * (1 - k) + ba * k).astype(np.uint8), "L"))
    return out


class Card:
    """a card to animate: `sprite` (RGBA, no shadow) or, for a layer cut out of a finished frame, a sprite that already carries its
    shadow (baked=True). rect = the card body inside S (pivots, strips, the slab line)"""

    def __init__(self, sprite, shadow=SH_STD, baked=False):
        self.sprite, self.baked, self.shadow = sprite, baked, shadow
        self.pad = 0 if baked else max(1, int(shadow[0]) * 3)
        self.w, self.h = sprite.size

    @property
    def rect(self):
        return (self.pad, self.pad, self.pad + self.w, self.pad + self.h)

    def S(self, shift=(0, 0), mix=1.0):
        """sprite + its shadow on the padded canvas. shift = (dx, dy): the content slides inside the silhouette;
        mix < 1 blends a tight 6 px shadow (mix 0) into the card's own (mix 1) (foldx)"""
        sp = shift_content(self.sprite, *shift) if (shift[0] or shift[1]) else self.sprite
        if self.baked: return sp
        bl, al, dy = self.shadow
        sh = shadow_only(self.sprite, bl, al, dy, self.pad)
        if mix < 0.999: sh = _lerp_alpha(shadow_only(self.sprite, 6, 150, 3, self.pad), sh, cl(mix))
        sh.alpha_composite(sp, (self.pad, self.pad))
        return sh


def _sig_tilt(c, tau):
    S = c.S(); w, h = S.size
    u = cl(tau / SIGS["tilt"]); p = e_q5(u)
    th = math.radians(16 * (1 - p)); dx = 60 * (1 - p); al = min(1.0, u / 0.35); f = 1400.0
    quad = []
    for x, y in ((-w / 2, -h / 2), (w / 2, -h / 2), (w / 2, h / 2), (-w / 2, h / 2)):
        z = x * math.sin(th); k = f / (f + z); quad.append((x * math.cos(th) * k, y * k))
    im, ox, oy = warp_quad(S, quad)
    return (O.with_alpha(im, al) if al < 1 else im), ox + dx, oy


def _sig_slab(c, tau):
    t_line, t_open = 0.10, SIGS["slab"] - 0.10
    lt = cl(tau / t_line); m = e_ex((tau - t_line) / t_open)
    S = c.S(shift=(-18 * (1 - m), 0)); w, h = S.size
    arr = np.asarray(S, np.float32).copy()
    xs = np.abs(np.arange(w, dtype=np.float32) + 0.5 - w / 2.0)
    arr[..., 3] *= np.clip(m * (w / 2.0) - xs + 0.5, 0, 1)[None, :]
    im = Image.fromarray(arr.astype(np.uint8), "RGBA")
    la = lt * (1 - cl(m / 0.35))                                       # the line fades as the mask passes
    if la > 0.01:
        x0, y0, x1, y1 = c.rect; ch = (y1 - y0) * e_q5(lt)
        ln = Image.new("RGBA", (w, h), (0, 0, 0, 0))
        ImageDraw.Draw(ln).rectangle((w / 2 - 2, (y0 + y1) / 2 - ch / 2, w / 2 + 1, (y0 + y1) / 2 + ch / 2), fill=GOLD + (255,))
        ln = Image.alpha_composite(O.with_alpha(ln.filter(ImageFilter.GaussianBlur(6)), 0.6), ln)
        im.alpha_composite(O.with_alpha(ln, la))
    return im, -w / 2, -h / 2


def _sig_foldx(c, tau):
    u = cl(tau / 0.40); p = e_q5(u); sx = 0.04 + 0.96 * p
    S = c.S(shift=(0, 14 * (1 - e_q5((tau - 0.08) / 0.40))), mix=p)
    w2 = max(2, int(round(S.width * sx)))
    im = S.resize((w2, S.height), Image.LANCZOS); al = min(1.0, u / 0.25)
    return (O.with_alpha(im, al) if al < 1 else im), -w2 / 2, -S.height / 2


def _sig_swing(c, tau):
    S = c.S(); p = e_c3(tau / SIGS["swing"]); al = min(1.0, tau / 0.2)
    px, py = S.width / 2, c.rect[1]
    im, dx, dy = rot_about(S, (px, py), -11.0 * (1 - p))
    return (O.with_alpha(im, al) if al < 1 else im), dx + (px - S.width / 2), dy + (py - S.height / 2)


def _sig_shutter(c, tau):
    S = c.S(); w, h = S.size; x0, y0, x1, y1 = c.rect; n = 5; sh_ = (y1 - y0) / n
    rs = [e_q4((tau - 0.04 * k) / 0.24) for k in range(n)]
    rows = np.arange(h, dtype=np.float32)
    alpha_row = np.full(h, float(np.mean(rs)), np.float32)              # the shadow follows the overall progress
    for k in range(n):
        a, b = y0 + k * sh_, y0 + (k + 1) * sh_
        inside = (rows >= np.floor(a)) & (rows < np.ceil(b))
        alpha_row = np.where(inside, np.clip(a + rs[k] * sh_ - rows, 0, 1), alpha_row)
    arr = np.asarray(S, np.float32).copy(); arr[..., 3] *= alpha_row[:, None]
    im = Image.fromarray(arr.astype(np.uint8), "RGBA")
    r4 = rs[-1]
    if 0.02 < r4 < 0.98:                                               # the 1 px hairline riding the edge of the last strip
        yy = int(round(y0 + (n - 1) * sh_ + r4 * sh_)) - 1
        ln = Image.new("RGBA", (w, h), (0, 0, 0, 0))
        ImageDraw.Draw(ln).rectangle((x0, yy, x1 - 1, yy), fill=(255, 255, 255, int(255 * min(1.0, (1 - r4) * 2.0))))
        im.alpha_composite(ln)
    return im, -w / 2, -h / 2


def _sig_riseup(c, tau):
    S = c.S(); u = cl(tau / SIGS["riseup"]); al = min(1.0, u / 0.35)
    return (O.with_alpha(S, al) if al < 1 else S), -S.width / 2, -S.height / 2


_SIG_FN = {"riseup": _sig_riseup, "tilt": _sig_tilt, "slab": _sig_slab, "foldx": _sig_foldx, "swing": _sig_swing, "shutter": _sig_shutter}


def sig_mode(name, t, dur):
    """'in' | 'out' | 'hold' at time t of a dur-long graphic"""
    t_in = SIGS[name]
    if t < t_in: return "in"
    if t > dur - t_in * OUT_K: return "out"
    return "hold"


def sig_card_frame(name, card, cx, cy, t, dur, rise=0.0):
    """one full-frame RGBA frame of `card` (centre cx, cy) under the entrance signature `name` at time t. rise = extra px the card
    climbs through the entrance (play_card: 60)"""
    mode = sig_mode(name, t, dur); t_in = SIGS[name]
    fr = blank()
    if mode == "hold":
        S = card.S(); paste_rgba(fr, S, cx - S.width / 2, cy - S.height / 2); return fr
    renders = []
    for k in range(5):
        tt = t + ((k + 0.5) / 5 - 0.5) * SHUTTER_ANGLE / FPS
        tau = cl(tt, 0, t_in) if mode == "in" else cl((dur - tt) / (t_in * OUT_K), 0, 1) * t_in      # entrance clock (out = backwards)
        if tau >= t_in - 1e-6:
            S = card.S(); renders.append((S, int(round(cx - S.width / 2)), int(round(cy - S.height / 2)))); continue
        im, ox, oy = _SIG_FN[name](card, tau)
        renders.append((im, int(round(cx + ox)), int(round(cy + oy + rise * (1 - e_q5(tau / t_in))))))
    img, x, y = average_renders(renders)
    paste_rgba(fr, img, x, y)
    return fr


def sig_frame(name, sprite, cx, cy, t, dur, shadow=SH_STD, rise=0.0):
    return sig_card_frame(name, Card(sprite, shadow), cx, cy, t, dur, rise)


# ---- chain into the sprite-kind entrance dispatcher (O.pop_frame / M6.pop_frame / M6.enter all resolve it at call time)
_prev_pop = O.pop_frame


def pop7(sprite, cx, cy, t, dur, t_in=0.42, t_out=0.24, ent=None, from_xy=None):
    e = ent or O.ENTRANCE
    if e in SIGS: return sig_frame(e, sprite, cx, cy, t, dur, rise=40.0 if e == "riseup" else 0.0)
    return _prev_pop(sprite, cx, cy, t, dur, t_in, t_out, ent, from_xy)


O.pop_frame = pop7
M6.pop_frame = pop7

# ---- the curated X.NEW kinds: transform the kind's HOLD frame as one layer (their own entrance never shows)
WRAP = ("teaser", "teaser2", "still_card", "era", "source_tag", "low_title")


def wrap_sig(builder):
    def b(plan, seq, g):
        fn, n = builder(plan, seq, g)
        ent = g.get("entrance") or O.ENTRANCE
        if ent not in SIGS: return fn, n
        dur = g["t1"] - g["t0"]
        hold_in = min(n - 1, int(math.ceil(max(0.5, SIGS[ent] + 0.1) * FPS)))
        hold_out = max(0, min(n - 1, int(math.floor((dur - 0.30) * FPS))))

        def fn2(i):
            t = i / FPS; mode = sig_mode(ent, t, dur)
            if mode == "hold": return fn(i)
            src = fn(hold_in if mode == "in" else hold_out)
            bb = bbox_alpha(src)
            if not bb: return src
            return sig_card_frame(ent, Card(src.crop(bb), baked=True), (bb[0] + bb[2]) / 2, (bb[1] + bb[3]) / 2, t, dur)
        return fn2, n
    return b


for _k in WRAP:
    if _k in X.NEW: X.NEW[_k] = wrap_sig(X.NEW[_k])


# ================================================================ video kinds: ffmpeg graphs straight to ProRes
PRORES = ["-c:v", "prores_ks", "-profile:v", "4444", "-pix_fmt", "yuva444p10le", "-vendor", "apl0"]


def _abs(plan, p):
    return p if os.path.isabs(p) else os.path.join(plan["_dir"], p)


def _out_args(cnt, out):
    a = ["-map", "[out]", "-frames:v", str(cnt), "-r", str(FPS)]
    return a + (["-f", "rawvideo", "-pix_fmt", "rgba", "-"] if out == "-" else PRORES + [out])


def read_raw(cmd, w, h, cnt, pix=4):
    """frames (PIL RGBA/RGB) from an ffmpeg command writing rawvideo to stdout; exactly cnt of them or SystemExit"""
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE); sz, k = w * h * pix, 0
    try:
        while k < cnt:
            b = p.stdout.read(sz)
            if len(b) < sz: break
            k += 1; yield Image.frombytes("RGBA" if pix == 4 else "RGB", (w, h), b)
    finally:
        if p.poll() is None: p.kill()
        p.stdout.close(); p.wait()
    if k < cnt: raise SystemExit(f"ffmpeg gave {k} of {cnt} frames: {' '.join(cmd[:12])} ...")


def encode_frames(gen, out):
    p = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgba", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-"] + PRORES + [out],
                         stdin=subprocess.PIPE)
    for fr in gen: p.stdin.write(fr.tobytes())
    p.stdin.close(); p.wait()


class Seg:
    """a stretch [f0, f0 + n) of a graphic's frames made either by an ffmpeg graph (cmd(lf0, cnt, out) -> argv; out '-' = rawvideo
    RGBA 1080x1920 on stdout, else a ProRes file) or by Python (gen(lf0, cnt) -> RGBA frames); lf0 = frame offset inside the Seg"""

    def __init__(self, f0, n, cmd=None, gen=None): self.f0, self.n, self.cmd, self.gen = f0, n, cmd, gen


def segs_frames(segs, f0, n):
    for s in segs:
        lo, hi = max(f0, s.f0), min(f0 + n, s.f0 + s.n)
        if hi <= lo: continue
        if s.gen: yield from s.gen(lo - s.f0, hi - lo)
        else: yield from read_raw(s.cmd(lo - s.f0, hi - lo, "-"), W, H, hi - lo)


def segs_build(segs, out, tmp):
    files = []
    for k, s in enumerate(segs):
        fp = os.path.join(tmp, f"seg{k}.mov")
        if s.cmd: subprocess.run(s.cmd(0, s.n, fp), check=True)
        else: encode_frames(s.gen(0, s.n), fp)
        files.append(fp)
    if len(files) == 1:
        shutil.move(files[0], out); return
    lst = os.path.join(tmp, "list.txt")
    open(lst, "w").write("".join("file '" + f.replace("\\", "/") + "'\n" for f in files))
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", out], check=True)


def zoom_expr(zexpr, cw, ch):
    """perspective= option text zooming the cw x ch canvas about its centre by the ffmpeg expression zexpr (sub-pixel, fixed size)"""
    K = f"(1-1/({zexpr}))"
    x0, x1, y0, y1 = f"{cw / 2}*{K}", f"{cw}-{cw / 2}*{K}", f"{ch / 2}*{K}", f"{ch}-{ch / 2}*{K}"
    return (f"perspective=x0='{x0}':y0='{y0}':x1='{x1}':y1='{y0}':x2='{x0}':y2='{y1}':x3='{x1}':y3='{y1}':eval=frame:interpolation=cubic")


def _tracked(text, font, track, fill):
    d = ImageDraw.Draw(Image.new("RGBA", (1, 1)))
    ws = [d.textlength(c, font=font) + track for c in text]
    asc = -font.getbbox("H", anchor="ls")[1]
    im = Image.new("RGBA", (int(sum(ws)) + 4, int(font.size * 1.3)), (0, 0, 0, 0)); dd = ImageDraw.Draw(im); x = 2
    for c, w in zip(text, ws): dd.text((x, asc + 2), c, font=font, fill=fill, anchor="ls"); x += w
    return im, asc


def ours_pill(text, tag2=None):
    f = F(BEBAS, 48); tx, asc = _tracked(text, f, 4, WHITE); h = 66;   # kit: type never < 40 (was 30 / 44)
    w = tx.width + 36
    im = O.rrect((w, h), h // 2, (17, 17, 17, 230), outline=GOLD + (255,), width=1)
    im.alpha_composite(tx, (16, int(h / 2 - asc / 2 - 2)))
    return im


class Play:
    """one clean file playing as a card in the top panel (play_card's picture). spec: file | still, src_t0, push, D (the push lasts D
    s), handle (their Short's source tag) | tag, tag2 (our sample's pill). Writes its PNG assets to tmp."""

    def __init__(self, plan, g, spec, tmp, name):
        self.plan, self.spec = plan, spec
        P = tuple(g.get("panel", PANEL)); self.P = P
        self.pw, self.ph = P[2] - P[0], P[3] - P[1]
        M = 36; self.ch = self.ph - 2 * M; self.cw = int(round(self.ch * 9 / 16)); self.R, self.pad = 22, 64
        self.x0, self.y0 = (self.pw - self.cw) // 2, M
        self.push = float(spec.get("push", 0.03)); self.D = float(spec["D"])
        cw, ch, pad = self.cw, self.ch, self.pad
        mask = O.rounded_mask((cw, ch), (0, 0, cw, ch), self.R)
        card = Image.new("RGBA", (cw, ch), (0, 0, 0, 255)); card.putalpha(mask)
        sh = shadow_only(card, 12, 150, 8, pad)                                     # the 36 px soft shadow
        ss = 4; ring = Image.new("RGBA", (cw * ss, ch * ss), (0, 0, 0, 0))
        ImageDraw.Draw(ring).rounded_rectangle((0, 0, cw * ss - 1, ch * ss - 1), self.R * ss, outline=(255, 255, 255, 178), width=2 * ss)
        self.ring = ring.resize((cw, ch), Image.LANCZOS)                            # 2 px white keyline at 70 %
        line = Image.new("RGBA", sh.size, (0, 0, 0, 0)); line.alpha_composite(self.ring, (pad, pad))
        self.paths = {}
        for k, im in (("mask", mask), ("shadow", sh), ("line", line)):
            self.paths[k] = os.path.join(tmp, f"{name}-{k}.png"); im.save(self.paths[k])
        self.tag, self.tag_xy = self._tag(spec)
        tg = Image.new("RGBA", (self.pw, self.ph), (0, 0, 0, 0))
        if self.tag is not None: paste_rgba(tg, self.tag, *self.tag_xy)
        self.paths["tag"] = os.path.join(tmp, f"{name}-tag.png"); tg.save(self.paths["tag"])
        if spec.get("still"):
            self.paths["still"] = os.path.join(tmp, f"{name}-still.png")
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{spec['still']:.4f}", "-i", spec["file"], "-frames:v", "1", self.paths["still"]], check=True)

    def _tag(self, spec):
        cw, ch, x0, y0 = self.cw, self.ch, self.x0, self.y0
        if spec.get("handle"):                                                      # THEIR Short: the FX-39 source tag
            for size in (26, 24, 22, 20, 18):
                gl = M6.yt_glyph(int(size * 1.1)); tx = rich_line(spec["handle"], F(INTER_SB, size))
                vis = Image.new("RGBA", (gl.width + 8 + tx.width, max(gl.height, tx.height) + 4), (0, 0, 0, 0))
                vis.alpha_composite(gl, (0, (vis.height - gl.height) // 2)); vis.alpha_composite(tx, (gl.width + 2, (vis.height - tx.height) // 2 + 1))
                if vis.width <= x0 - 14 - 12: break
            sp, pad = O.soft_shadow(vis, blur=8, alpha=170, dy=2)
            return sp, (x0 - 14 - vis.width - pad, y0 + ch - vis.height - pad)
        if spec.get("tag"):                                                         # OUR sample: the pill on the top-left corner
            pl = ours_pill(spec["tag"])
            sp, pad = O.soft_shadow(pl, blur=8, alpha=150, dy=3)
            if spec.get("tag2"):
                t2 = rich_line(spec["tag2"], F(INTER_SB, 40), fill=(255, 255, 255, 215)); sp2, p2 = O.soft_shadow(t2, blur=6, alpha=170, dy=2)
                full = Image.new("RGBA", (max(sp.width, sp2.width), sp.height + sp2.height - 2 * p2 + 6), (0, 0, 0, 0))
                full.alpha_composite(sp, (0, 0)); full.alpha_composite(sp2, (pad - p2 + 6, sp.height - pad - p2 + 6)); sp = full
            return sp, (x0 - 14 - pad, y0 - pl.height // 2 - pad)
        return None, (0, 0)

    # --- the picture as an ffmpeg graph fragment
    def _src(self, fg, start, nfr):
        s = self.spec
        if s.get("still"):
            return fg.inp("-loop", "1", "-framerate", str(FPS), "-t", f"{nfr / FPS + 0.5:.4f}", "-i", self.paths["still"])
        return fg.inp("-ss", f"{s['src_t0'] + start:.4f}", "-t", f"{nfr / FPS + 0.5:.4f}", "-i", s["file"])

    def composite(self, fg, lab, start, nfr):
        """append the inputs + filters that make [lab]: the opaque panel picture (pw x ph rgba), `start` s into the beat"""
        cw, ch, pad, pw, ph = self.cw, self.ch, self.pad, self.pw, self.ph
        i0 = self._src(fg, start, nfr)
        im, ish, iln, itg = [fg.inp("-loop", "1", "-framerate", str(FPS), "-t", f"{nfr / FPS + 0.5:.4f}", "-i", self.paths[k]) for k in ("mask", "shadow", "line", "tag")]
        z = f"1+{self.push}*(0.5-0.5*cos(PI*min(1,(in+{start * FPS})/{max(1.0, self.D * FPS)})))"
        fg.f(f"[{i0}:v]fps={FPS},tpad=stop_mode=clone:stop=60,setpts=PTS-STARTPTS,split=2[{lab}a][{lab}b]")
        fg.f(f"[{lab}a]scale={pw // 4}:{ph // 4}:force_original_aspect_ratio=increase:flags=bilinear,crop={pw // 4}:{ph // 4},gblur=sigma=10,"
             f"colorchannelmixer=rr=0.45:gg=0.45:bb=0.45,scale={pw}:{ph}:flags=bilinear,format=rgba[{lab}bd]")
        fg.f(f"[{lab}b]scale={cw}:{ch}:force_original_aspect_ratio=increase:flags=bicubic,crop={cw}:{ch},format=rgba[{lab}vid]")
        fg.f(f"[{im}:v]format=gray[{lab}mk]")
        fg.f(f"[{lab}vid][{lab}mk]alphamerge[{lab}card]")
        fg.f(f"[{ish}:v]format=rgba[{lab}shd]; [{lab}shd][{lab}card]overlay={pad}:{pad}:format=auto[{lab}c1]")
        fg.f(f"[{iln}:v]format=rgba[{lab}ln]; [{lab}c1][{lab}ln]overlay=0:0:format=auto[{lab}c2]")
        fg.f(f"[{lab}c2]{zoom_expr(z, cw + 2 * pad, ch + 2 * pad)}[{lab}c3]")
        fg.f(f"[{lab}bd][{lab}c3]overlay={self.x0 - pad}:{self.y0 - pad}:format=auto[{lab}o1]")
        fg.f(f"[{itg}:v]format=rgba[{lab}tg]; [{lab}o1][{lab}tg]overlay=0:0:format=auto[{lab}]")

    def layer_cmd(self, which, start, cnt):
        """rawvideo for the head: 'bd' = the blurred backdrop (pw x ph rgba), 'card' = the card + its keyline (cw x ch rgba)"""
        fg = FG(); cw, ch, pw, ph = self.cw, self.ch, self.pw, self.ph
        i0 = self._src(fg, start, cnt)
        if which == "bd":
            fg.f(f"[{i0}:v]fps={FPS},tpad=stop_mode=clone:stop=60,scale={pw // 4}:{ph // 4}:force_original_aspect_ratio=increase:flags=bilinear,crop={pw // 4}:{ph // 4},"
                 f"gblur=sigma=10,colorchannelmixer=rr=0.45:gg=0.45:bb=0.45,scale={pw}:{ph}:flags=bilinear,format=rgba[out]")
        else:
            im = fg.inp("-loop", "1", "-framerate", str(FPS), "-t", f"{cnt / FPS + 0.5:.4f}", "-i", self.paths["mask"])
            fg.f(f"[{i0}:v]fps={FPS},tpad=stop_mode=clone:stop=60,scale={cw}:{ch}:force_original_aspect_ratio=increase:flags=bicubic,crop={cw}:{ch},format=rgba[v]")
            fg.f(f"[{im}:v]format=gray[mk]; [v][mk]alphamerge[c]")
            ring = os.path.join(os.path.dirname(self.paths["line"]), os.path.basename(self.paths["line"]).replace("-line", "-ring"))
            if not os.path.exists(ring): self.ring.save(ring)
            ir = fg.inp("-loop", "1", "-framerate", str(FPS), "-t", f"{cnt / FPS + 0.5:.4f}", "-i", ring)
            fg.f(f"[{ir}:v]format=rgba[r]; [c][r]overlay=0:0:format=auto[out]")
        return fg.cmd(cnt, "-")


class FG:
    """a filter_complex under construction: inp() adds an input and returns its index, f() adds a filter line"""

    def __init__(self): self.args, self.fl, self.n = ["ffmpeg", "-v", "error", "-y"], [], 0

    def inp(self, *a):
        self.args += list(a); self.n += 1; return self.n - 1

    def f(self, txt): self.fl.append(txt)

    def cmd(self, cnt, out):
        return self.args + ["-filter_complex", ";".join(self.fl)] + _out_args(cnt, out)


def _pad_panel(fg, lab, P):
    fg.f(f"[{lab}]pad={W}:{H}:{P[0]}:{P[1]}:color=black@0,format=rgba[out]")


def play_head_gen(plan, g, play, dur, ent, n_in):
    """Python frames [lf0, lf0 + cnt) of the play_card's entrance: the backdrop crossfades in over 0.2 s, the card enters with the
    reaction's signature (+ a 60 px rise), the tag rises behind a mask 0.18 s after"""
    P = play.P

    def gen(lf0, cnt):
        bd = read_raw(play.layer_cmd("bd", lf0 / FPS, cnt), play.pw, play.ph, cnt)
        cd = read_raw(play.layer_cmd("card", lf0 / FPS, cnt), play.cw, play.ch, cnt)
        for j in range(cnt):
            t = (lf0 + j) / FPS; b, c = next(bd), next(cd)
            fr = blank(); a = e_c3(t / 0.2)
            panel = O.with_alpha(b, a) if a < 0.999 else b
            fr.alpha_composite(panel, (P[0], P[1]))
            cx, cy = P[0] + play.x0 + play.cw / 2, P[1] + play.y0 + play.ch / 2
            fr.alpha_composite(sig_card_frame(ent, Card(c, (12, 150, 8)), cx, cy, t, dur, rise=60.0))
            if play.tag is not None and t > 0.18:
                u = e_c3((t - 0.18) / 0.30); sp = play.tag
                shifted = Image.new("RGBA", sp.size, (0, 0, 0, 0)); shifted.alpha_composite(sp.crop((0, 0, sp.width, sp.height - int(12 * (1 - u)))), (0, int(12 * (1 - u))))
                paste_rgba(fr, O.with_alpha(shifted, u) if u < 1 else shifted, P[0] + play.tag_xy[0], P[1] + play.tag_xy[1])
            yield fr
    return gen


def _ent_of(g):
    e = g.get("entrance") or O.ENTRANCE
    return e if e in SIGS else "riseup"


def play_segments(plan, seq, g):
    dur = g["t1"] - g["t0"]; n = int(round(dur * FPS))
    f = _abs(plan, g["file"]); spec = dict(file=f, src_t0=g.get("src_t0", 0.0), push=g.get("push", 0.03), D=dur,
                                            handle=g.get("handle"), tag=g.get("tag"), tag2=g.get("tag2"))
    tmp = tempfile.mkdtemp(prefix="playcard-"); play = Play(plan, g, spec, tmp, "p")
    ent = _ent_of(g); n_in = min(n, int(round((SIGS[ent] + 0.06) * FPS)))
    segs = [Seg(0, n_in, gen=play_head_gen(plan, g, play, dur, ent, n_in))]

    def steady(lf0, cnt, out):
        fg = FG(); play.composite(fg, "pl", (n_in + lf0) / FPS, cnt); _pad_panel(fg, "pl", play.P)
        return fg.cmd(cnt, out)
    if n > n_in: segs.append(Seg(n_in, n - n_in, cmd=steady))
    return segs, tmp


# ---------------------------------------------------------------- portal
def _zoom_blur(arr, s, blur_px, pw, ph):
    """arr (ph, pw, 3|4 float32) scaled by s about its centre; blur_px = the radial smear at the panel's half width (average of
    7 scales spanning s * (1 +- blur_px / (pw / 2) / 2))"""
    K = 7 if blur_px > 0.8 else 1
    im = Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8), "RGBA" if arr.shape[2] == 4 else "RGB")
    acc = np.zeros(arr.shape, np.float32)
    for k in range(K):
        sc = s * (1 + ((k / (K - 1) - 0.5) * blur_px / (pw / 2)) if K > 1 else 1)
        sc = max(sc, 1.0)
        w2, h2 = int(math.ceil(pw * sc)), int(math.ceil(ph * sc))
        big = im.resize((w2, h2), Image.BILINEAR)
        l, t = (w2 - pw) // 2, (h2 - ph) // 2
        acc += np.asarray(big.crop((l, t, l + pw, t + ph)), np.float32)
    return acc / K


def portal_segments(plan, seq, g):
    dur = g["t1"] - g["t0"]; n = int(round(dur * FPS)); at = float(g["at"]); TT = float(g.get("tt", 0.5))     # V3: g["dissolve"] = a plain cross-dissolve of g["tt"] s (6 frames = 0.1), no zoom, no ring
    f_at = int(round(at * FPS)); n_tr = int(round(TT * FPS))
    tmp = tempfile.mkdtemp(prefix="portal-")
    a_file, b_file = _abs(plan, g["a_file"]), _abs(plan, g["b_file"])
    A = dict(file=a_file, push=g.get("push", 0.03), D=at + TT, handle=g.get("a_handle", g.get("handle")), tag=g.get("a_tag"), tag2=g.get("a_tag2"))
    if g.get("a_src_t0") is not None: A["src_t0"] = float(g["a_src_t0"])
    else: A["still"] = float(g["a_t"]); A["src_t0"] = float(g["a_t"])
    B = dict(file=b_file, src_t0=float(g["b_t"]), push=g.get("push", 0.03), D=max(1.0, dur - at), tag=g.get("b_tag"), tag2=g.get("b_tag2"), handle=g.get("b_handle"))
    pa, pb = Play(plan, g, A, tmp, "a"), Play(plan, g, B, tmp, "b")
    P = pa.P; pw, ph = pa.pw, pa.ph
    ent = _ent_of(g); n_in = min(f_at, int(round((SIGS[ent] + 0.06) * FPS))) if g.get("enter", True) else 0
    segs = []
    if n_in: segs.append(Seg(0, n_in, gen=play_head_gen(plan, g, pa, dur, ent, n_in)))

    def a_steady(lf0, cnt, out):
        fg = FG(); pa.composite(fg, "pl", (n_in + lf0) / FPS, cnt); _pad_panel(fg, "pl", P); return fg.cmd(cnt, out)

    def comp_cmd(pl, start, cnt):
        fg = FG(); pl.composite(fg, "pl", start, cnt); fg.f("[pl]format=rgba[out]"); return fg.cmd(cnt, "-")
    # the ring: 2 px gold, flashing outward from the card centre on the crossing
    cxp, cyp = pw / 2, ph / 2

    def transition(lf0, cnt):
        ga = read_raw(comp_cmd(pa, at + lf0 / FPS, cnt), pw, ph, cnt)
        gb = read_raw(comp_cmd(pb, lf0 / FPS, cnt), pw, ph, cnt)
        for j in range(cnt):
            t = (lf0 + j) / FPS; fa, fb = next(ga), next(gb); p = e_io3(t / TT)
            if g.get("dissolve"):
                k_ = min(1.0, (j + 0.5) / max(1, cnt)); pan = Image.new("RGBA", (pw, ph), (0, 0, 0, 255)); pan.alpha_composite(fa); pan.alpha_composite(O.with_alpha(fb, k_)); fr = blank(); fr.alpha_composite(pan, (P[0], P[1])); yield fr; continue
            ar = _zoom_blur(np.asarray(fa, np.float32), 1 + 0.9 * p, 24 * p, pw, ph)
            br = _zoom_blur(np.asarray(fb, np.float32), 1.35 - 0.35 * p, 24 * (1 - p), pw, ph)
            aA = 1.0 if t < TT - 0.22 else 1 - e_io3((t - (TT - 0.22)) / 0.22); aB = e_io3(t / 0.22) if t < 0.22 else 1.0
            ia = Image.fromarray(np.clip(ar, 0, 255).astype(np.uint8), "RGBA"); ib = Image.fromarray(np.clip(br, 0, 255).astype(np.uint8), "RGBA")
            ia = O.with_alpha(ia, aA) if aA < 1 else ia; ib = O.with_alpha(ib, aB) if aB < 1 else ib
            pan = Image.new("RGBA", (pw, ph), (0, 0, 0, 255)); pan.alpha_composite(ia); pan.alpha_composite(ib)
            u = (t - 0.20) / 0.25
            if 0 <= u < 1:                                                      # the gold ring, 0.6 -> 0 over 0.25 s
                ss = 2; rr = (28 + 540 * e_c3(u)) * ss
                ring = Image.new("RGBA", (pw * ss, ph * ss), (0, 0, 0, 0))
                ImageDraw.Draw(ring).ellipse((cxp * ss - rr, cyp * ss - rr, cxp * ss + rr, cyp * ss + rr), outline=GOLD + (int(255 * 0.6 * (1 - u)),), width=2 * ss)
                pan.alpha_composite(ring.resize((pw, ph), Image.LANCZOS))
            fr = blank(); fr.alpha_composite(pan, (P[0], P[1])); yield fr

    def b_steady(lf0, cnt, out):
        fg = FG(); pb.composite(fg, "pl", TT + lf0 / FPS + (0.0), cnt); _pad_panel(fg, "pl", P); return fg.cmd(cnt, out)

    def b_steady2(lf0, cnt, out):                       # B has been playing for (frames since the crossing) s
        fg = FG(); pb.composite(fg, "pl", (n_tr + lf0) / FPS, cnt); _pad_panel(fg, "pl", P); return fg.cmd(cnt, out)
    if f_at > n_in: segs.append(Seg(n_in, f_at - n_in, cmd=a_steady))
    segs.append(Seg(f_at, min(n_tr, n - f_at), gen=transition))
    if n > f_at + n_tr: segs.append(Seg(f_at + n_tr, n - f_at - n_tr, cmd=b_steady2))
    return segs, tmp


# ---------------------------------------------------------------- inset_cam
def inset_segments(plan, seq, g):
    dur = g["t1"] - g["t0"]; n = int(round(dur * FPS))
    IX, IY, IW, IH = g.get("rect", (744, 1190, 300, 400)); R, pad = 28, 36
    cam = _abs(plan, g["cam"]); off = float(g["cam_offset"]); fx, my = g["face_x"]
    crop_h = float(g.get("crop_h", 900)); crop_w = crop_h * IW / IH; camw, camh = g.get("cam_size", (1920, 1080))
    eye = my - float(g.get("eye_dy", 160)); cy0 = min(max(eye - 0.38 * crop_h, 0), camh - crop_h); cx0 = min(max(fx - crop_w / 2, 0), camw - crop_w)
    tmp = tempfile.mkdtemp(prefix="inset-")
    mask = O.rounded_mask((IW, IH), (0, 0, IW, IH), R)
    card = Image.new("RGBA", (IW, IH), (0, 0, 0, 255)); card.putalpha(mask)
    sh = shadow_only(card, 10, 150, 8, pad)                                          # 30 px shadow
    ss = 4; ring = Image.new("RGBA", (IW * ss, IH * ss), (0, 0, 0, 0))
    ImageDraw.Draw(ring).rounded_rectangle((0, 0, IW * ss - 1, IH * ss - 1), R * ss, outline=(255, 255, 255, 204), width=2 * ss)   # 2 px, 80 %
    line = Image.new("RGBA", sh.size, (0, 0, 0, 0)); line.alpha_composite(ring.resize((IW, IH), Image.LANCZOS), (pad, pad))
    pm, ps, pl = (os.path.join(tmp, k + ".png") for k in ("mask", "shadow", "line")); mask.save(pm); sh.save(ps); line.save(pl)

    def cmd(lf0, cnt, out):
        pieces = O.seq_pieces(plan, seq, g["t0"], lf0, cnt)
        fg = FG(); labs = []
        for k, (c, st, kk) in enumerate(pieces):
            if c is None: raise SystemExit(f"inset_cam {g['id']}: no screen clip at frame {lf0}")
            i = fg.inp("-ss", f"{st + off:.4f}", "-t", f"{kk / FPS + 0.5:.4f}", "-i", cam)
            fg.f(f"[{i}:v]fps={FPS},crop={int(round(crop_w))}:{int(round(crop_h))}:{int(round(cx0))}:{int(round(cy0))},scale={IW}:{IH}:flags=lanczos,"
                 f"tpad=stop_mode=clone:stop=30,trim=end_frame={kk},setpts=PTS-STARTPTS[p{k}]")
            labs.append(f"[p{k}]")
        fg.f("".join(labs) + (f"concat=n={len(labs)}:v=1:a=0," if len(labs) > 1 else "") + "format=rgba[cam]")
        im, ish, iln = (fg.inp("-loop", "1", "-framerate", str(FPS), "-t", f"{cnt / FPS + 0.5:.4f}", "-i", p) for p in (pm, ps, pl))
        fg.f(f"[{im}:v]format=gray[mk]; [cam][mk]alphamerge[card]")
        fg.f(f"[{ish}:v]format=rgba[shd]; [shd][card]overlay={pad}:{pad}:format=auto[c1]")
        fg.f(f"[{iln}:v]format=rgba[ln]; [c1][ln]overlay=0:0:format=auto[c2]")
        tt = f"((in+{lf0})/{FPS})"; u = f"clip(min({tt}/0.28,({dur}-{tt})/0.2),0,1)"
        z = f"0.92+0.08*(1-pow(1-{u},3))"
        fg.f(f"[c2]{zoom_expr(z, IW + 2 * pad, IH + 2 * pad)},setpts=PTS+{lf0 / FPS}/TB,fade=t=in:st=0:d=0.28:alpha=1,fade=t=out:st={dur - 0.2:.4f}:d=0.2:alpha=1,"
             f"setpts=PTS-STARTPTS,pad={W}:{H}:{IX - pad}:{IY - pad}:color=black@0,format=rgba[out]")
        return fg.cmd(cnt, out)
    return [Seg(0, n, cmd=cmd)], tmp


# ---------------------------------------------------------------- registration of the video kinds
VIDEO_SEGS = {"play_card": play_segments, "portal": portal_segments, "inset_cam": inset_segments}


def video_frames(plan, seq, g, f0, n):
    segs, tmp = VIDEO_SEGS[g["kind"]](plan, seq, g)
    try: yield from segs_frames(segs, f0, n)
    finally: shutil.rmtree(tmp, ignore_errors=True)


def build_video(plan, seq, g, mov):
    n = int(round((g["t1"] - g["t0"]) * FPS)); segs, tmp = VIDEO_SEGS[g["kind"]](plan, seq, g)
    try:
        if segs: assert sum(s.n for s in segs) == n, f"{g['id']}: segments cover {sum(s.n for s in segs)} of {n} frames"
        segs_build(segs, mov, tmp)
    finally: shutil.rmtree(tmp, ignore_errors=True)


for _k in VIDEO_SEGS: O.SEEKABLE[_k] = (lambda k: (lambda plan, seq, g, f0, n: video_frames(plan, seq, g, f0, n)))(_k)
O.NEW_KINDS = set(O.NEW_KINDS) | set(VIDEO_SEGS) | {"scorecard", "hl_sweep"}
O.PANEL_KINDS = set(O.PANEL_KINDS) | {"play_card", "portal", "hl_sweep", "scorecard"}
_orig_build_mg = O.build_mg


def build_mg7(plan, seq, only=None):
    out = os.path.join(plan["_dir"], "overlays", "mg"); os.makedirs(out, exist_ok=True)
    ids = set(only.split(",")) if only else None
    for g in plan["graphics"]:
        if ids and g["id"] not in ids: continue
        if g["kind"] in VIDEO_SEGS:
            t0 = time.time(); mov = os.path.join(out, f"{g['id']}.mov")
            build_video(plan, seq, g, mov)
            print(f"mg {g['id']}: {int(round((g['t1'] - g['t0']) * FPS))} frames -> {mov} ({time.time() - t0:.1f} s)")
        else:
            _orig_build_mg(plan, seq, g["id"])


O.build_mg = build_mg7


# ================================================================ scorecard: THEIRS vs OURS (FX-36 tale of the tape + FX-65 banner bars)
GREY = (154, 154, 154, 255)


def _wrap(text, font, maxw):
    d = ImageDraw.Draw(Image.new("RGBA", (1, 1))); words, lines, cur = str(text).split(" "), [], ""
    for w_ in words:
        t = (cur + " " + w_).strip()
        if cur and d.textlength(t, font=font) > maxw: lines.append(cur); cur = w_
        else: cur = t
    lines.append(cur); return lines


def _cell(cell, size, maxw, fill, bold_font):
    """(sprite, text width) of one THEIRS / OURS cell: wrapped Inter (<= 2 lines, shrinking) or the gold count; returns a builder for count-ups"""
    if isinstance(cell, dict):                                                  # {"count": 41, "suffix": " s"}
        return ("count", cell)
    f = F(bold_font, size)
    for s in range(size, 15, -2):
        f = F(bold_font, s); lines = _wrap(cell, f, maxw)
        if len(lines) <= 2 and all(ImageDraw.Draw(Image.new("RGBA", (1, 1))).textlength(l, font=f) <= maxw + 1 for l in lines): break
    else:
        raise SystemExit(f"scorecard: '{cell}' does not fit a {maxw} px cell in 2 lines even at 16 px")
    lh = int(f.size * 1.22); im = Image.new("RGBA", (int(maxw) + 8, lh * len(lines) + 6), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    for k, l in enumerate(lines): d.text((im.width / 2, 3 + lh * k + lh / 2), l, font=f, fill=fill, anchor="mm")
    return ("text", im)


def k_scorecard(plan, seq, g):
    dur = g["t1"] - g["t0"]; n = int(round(dur * FPS)); rows = g["rows"]
    if not 1 <= len(rows) <= 5: raise SystemExit(f"scorecard {g['id']}: 1-5 rows (got {len(rows)})")
    low = bool(g.get("low")); P = tuple(g.get("panel", PANEL))
    cw = int(g.get("w", 960 if low else 920)); hdr = 74 if low else 92; pad_b = 22
    avail = (1600 - 1150) if low else (P[3] - P[1] - 44)
    row_h = min(116 if not low else 92, (avail - hdr - pad_b) // len(rows))
    if row_h < 58: raise SystemExit(f"scorecard {g['id']}: {len(rows)} rows need {58 * len(rows) + hdr + pad_b} px, only {avail} px in the {'low band' if low else 'panel'}")
    ch = hdr + row_h * len(rows) + pad_b
    cx = g.get("x", W / 2); cy = g.get("y", (1150 + 1600) / 2 if low else (P[1] + P[3]) / 2)
    if low: cy = g.get("y", 1150 + ch / 2)
    if cy - ch / 2 < 200 or cy + ch / 2 > 1620: raise SystemExit(f"scorecard {g['id']}: the card (y {cy - ch / 2:.0f}..{cy + ch / 2:.0f}) leaves the safe band 200..1620")
    size = 26 if low else 30; colw = int(cw * 0.31); xl, xm, xr = cw * 0.215, cw * 0.5, cw * 0.785
    # base card: header + dividers (no rows)
    base = O.rrect((cw, ch), 26, (14, 14, 16, 240), outline=(255, 255, 255, 34), width=1)
    hl = Image.new("RGBA", (cw, ch), (0, 0, 0, 0)); ImageDraw.Draw(hl).line((26, 1, cw - 26, 1), fill=(255, 255, 255, 46), width=1); base.alpha_composite(hl)
    bd = ImageDraw.Draw(base)
    bd.text((xl, hdr * 0.55), "THEIRS", font=F(BEBAS, 40), fill=GREY, anchor="mm")
    bd.text((xr, hdr * 0.55), "OURS", font=F(BEBAS, 40), fill=GOLD + (255,), anchor="mm")
    bd.line((30, hdr, cw - 30, hdr), fill=(255, 255, 255, 30), width=1)
    for k in range(1, len(rows)): bd.line((46, hdr + k * row_h, cw - 46, hdr + k * row_h), fill=(255, 255, 255, 14), width=1)
    recap = g.get("recap"); t_rc = (recap - g["t0"]) if recap is not None else None
    R = []
    for k, row in enumerate(rows):
        ta, label, th, ou = row[0], row[1], row[2], row[3]
        ta = ta - g["t0"]
        batch = False
        if t_rc is not None and ta >= t_rc - 1e-6: ta, batch = max(t_rc, 0.1) if t_rc <= 0.05 else t_rc, True
        lab = _cell(label, 26 if not low else 22, int(cw * 0.17), (255, 255, 255, 204), INTER_SB)
        R.append(dict(t=ta, batch=batch, lab=lab[1], th=_cell(th, size, colw, (255, 255, 255, 235), INTER_B), ou=_cell(ou, size, colw, GOLD + (255,), INTER_B), y=hdr + k * row_h))

    def draw_cell(layer, kind_v, xc, yc, u, color, count_phase):
        """one cell on `layer`, `u` seconds after it began: rises 24 px behind the row's mask (the caller clips), 0.32 s easeOutQuint"""
        if u <= 0: return
        p = e_q5(u / 0.32); dy = 24 * (1 - p)
        k_, v_ = kind_v
        if k_ == "text":
            layer.alpha_composite(O.with_alpha(v_, min(1.0, u / 0.16)) if u < 0.16 else v_, (int(xc - v_.width / 2), int(yc - v_.height / 2 + dy)))
        else:
            q = e_c3(cl((u - 0.05) / 0.6)); val = v_["count"] * q
            txt = (f"{val:.{v_.get('dec', 0)}f}") + v_.get("suffix", "")
            fnt = F(BEBAS, 64 if not low else 52); d = ImageDraw.Draw(layer)
            d.text((xc, yc + dy + 2), txt, font=fnt, fill=color, anchor="mm")

    def fn(i):
        t = i / FPS; sp = base.copy()
        for r in R:
            if t < r["t"]: continue
            row = Image.new("RGBA", (cw, row_h), (0, 0, 0, 0)); yc = row_h / 2
            u = t - r["t"]
            draw_cell(row, ("text", r["lab"]) if not isinstance(r["lab"], tuple) else r["lab"], xm, yc, u, (255, 255, 255, 204), 0)
            draw_cell(row, r["th"], xl, yc, u, (225, 225, 228, 255), 0)
            uo = u - (0.0 if r["batch"] else 0.18)
            draw_cell(row, r["ou"], xr, yc, uo, GOLD + (255,), 0)
            if uo > 0 and r["ou"][0] == "text":                                  # the gold underline draws left -> right under OURS
                w_ = r["ou"][1].width * 0.62; q = e_c3(uo / 0.25); yy = yc + r["ou"][1].height / 2 + 4
                ImageDraw.Draw(row).rounded_rectangle((xr - w_ / 2, yy, xr - w_ / 2 + w_ * q, yy + 3), 1, fill=GOLD + (255,))
            sp.alpha_composite(row, (0, r["y"]))                                  # the row is its own mask: nothing leaves its band
        return M6.enter(g, sp, cx, cy, t, dur)
    return fn, n


# ================================================================ hl_sweep: the read-along highlighter on a real page (FX-34 / FX-45)
def k_hl_sweep(plan, seq, g):
    dur = g["t1"] - g["t0"]; n = int(round(dur * FPS)); P = tuple(g.get("panel", tuple(G.BOX))); pw, ph = P[2] - P[0], P[3] - P[1]
    lines = [dict(box=g["box"], at=float(g.get("at", 0.3)))]
    if g.get("box2") is not None: lines.append(dict(box=g["box2"], at=float(g.get("at2", g.get("at", 0.3) + g.get("dur", 0.45) + 0.12))))
    sw = float(g.get("dur", 0.45)); a_dim = float(g.get("dim", 0.40)); a_mk = float(g.get("strength", 0.42))

    def fn(i):
        t = i / FPS; ta = g["t0"] + t; fr = blank()
        out = 1.0 if t < dur - 0.2 else 1 - e_c3((t - (dur - 0.2)) / 0.2)
        ps = [e_c3((t - ln["at"]) / sw) for ln in lines]
        if max(ps) <= 0: return fr
        dimk = max(ps)                                                          # the page dims over the same time as the sweep
        hole = Image.new("L", (pw, ph), 0); hd = ImageDraw.Draw(hole)
        mk = Image.new("RGBA", (pw, ph), (0, 0, 0, 0)); md = ImageDraw.Draw(mk)
        for ln, p in zip(lines, ps):
            b = O.box_at(plan, ln["box"], ta)
            if b is None or p <= 0: continue
            x0, y0, x1, y1 = b[0] - P[0], b[1] - P[1], b[2] - P[0], b[3] - P[1]; lh = y1 - y0
            xs = x0 + (x1 - x0) * p
            hd.rounded_rectangle((x0 - 6, y0 - 3, xs + 6, y1 + 3), 6, fill=255)
            md.rounded_rectangle((x0, (y0 + y1) / 2 - 0.45 * lh, xs, (y0 + y1) / 2 + 0.45 * lh), 3, fill=MARKER + (int(255 * a_mk),))
        hole = hole.filter(ImageFilter.GaussianBlur(4))
        dim = Image.new("L", (pw, ph), int(255 * a_dim * dimk)); dim = ImageChops.multiply(dim, ImageChops.invert(hole))
        lay = Image.new("RGBA", (pw, ph), (0, 0, 0, 0)); lay.putalpha(dim)
        lay.alpha_composite(mk)
        fr.alpha_composite(O.with_alpha(lay, out) if out < 1 else lay, (P[0], P[1]))
        return fr
    return fn, n


X.NEW["scorecard"] = k_scorecard
X.NEW["hl_sweep"] = k_hl_sweep


# ================================================================ SFX hints (names are symbolic: the builder maps them to files)
def suggest_cues(g):
    """[(t_abs, sound)] the NEW-KINDS spec asks for: scorecard = a paper slide on the card's entrance + one wooden tap per row
    (alternating takes a / b); portal = an air pass at the crossing; hl_sweep = a felt-tip stroke per line"""
    k, t0 = g["kind"], g["t0"]
    if k == "scorecard":
        c = [(t0, "paper-slide")] + [(r[0] if g.get("recap") is None else min(r[0], g["recap"]), "wood-tap-" + "ab"[i % 2]) for i, r in enumerate(g["rows"])]
        return [(round(a, 3), b) for a, b in c]
    if k == "portal": return [(round(t0 + g["at"], 3), "air-pass")]
    if k == "hl_sweep":
        c = [(t0 + g.get("at", 0.3), "marker-stroke")]
        if g.get("box2") is not None: c.append((t0 + g.get("at2", g.get("at", 0.3) + g.get("dur", 0.45) + 0.12), "marker-stroke"))
        return [(round(a, 3), b) for a, b in c]
    return []


_orig_default_sfx = O.default_sfx


def default_sfx7(g):
    d = _orig_default_sfx(g)
    if g["kind"] in ("scorecard", "portal", "hl_sweep"):
        cs = suggest_cues(g); d = {"sfx": None, "cues": [[a, b] for a, b in cs]}
    return d


O.default_sfx = default_sfx7
