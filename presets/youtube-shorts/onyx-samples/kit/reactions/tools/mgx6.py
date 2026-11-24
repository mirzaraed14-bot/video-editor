"""mgx6.py: the R3 batch-6 v2 reactions (Drinkin' Bros, Still Here) = overlays.py + the reel's mgx.py kinds + the kinds below, JOB-LOCAL.

  PYTHONUTF8=1 python mgx6.py <job>/plan.json [--captions] [--mg] [--only id,id] [--check] [--still t t ...]

Why job-local: the shared toolkit (overlays.py) is in use by the R1/R2 builders at the same time;
everything here is patched in at import (the reel's mgx.py pattern), nothing on disk changes for anyone else.

v2 additions (REACTIONS-V2.md: denser, more refined overlays; captions below the lips):
  face framing   plan face[]["face_x"] may be [x, mouth_y] (camera px): face-only beats are framed so his MOUTH sits at plan["mouth_y"]
                 (frame px, default 915), i.e. above the one constant caption line (the seam, y 1038), the window y 227..1653 always
                 covered (the scale grows when the mouth sits low in the camera). geom.face_motion is patched (apply.py --layout and
                 the stills use the same numbers).
  entrances      "glide": in from 120 px right (easeOutQuint) with a horizontal motion blur of half the per-frame travel, fading over
                 the first 35 %; out 50 px left, blurred. "unfold": the card opens from its horizontal centre line (scaleY 0.08 -> 1,
                 easeOutQuint) while it fades; out = folds back to 0.6 + fade.
  teaser         a phone-shaped card holding a still of OUR sample (file, t) with a label pill; tilts in (-6 deg -> 0) and glides.
  comments       YouTube-style comment bubbles stacking up in the low band: items [[t_abs, "@user", "text"], ...].
  wave_cut       FX-60: a waveform strip of a raw range of the OBS audio (src_t0, src_t1, seconds) on the stage; its pauses (quiet
                 runs >= min_gap) shade red at mark_at; at cut_at the gaps close (segments slide together, eased) and a
                 chip shows the seconds saved; optional down chip (down_at, down_text).
  episode_bar    FX-68/70: a long episode bar (label), a playhead scanning it, markers [[t_abs, frac, "LABEL"], ...] dropping in gold,
                 a final line (final_at, final).
  source_tag     FX-39: the red YouTube glyph + "@handle" in white, small, bottom-left of the panel (x, y).
"""
import json, math, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
REEL = HERE
sys.path.insert(0, REEL)
import mgx as X                           # noqa: E402  (imports + patches overlays.py as X.O)
O = X.O
G = O.G
from PIL import Image, ImageDraw, ImageFilter  # noqa: E402
import numpy as np                         # noqa: E402

W, H, GOLD, FPS = O.W, O.H, O.GOLD, O.FPS_MG
WHITE = (255, 255, 255, 255)
RED = (226, 64, 58)
blank, ease, clamp, place, focus, shadowed, rich_line, pill, F, AF = X.blank, X.ease, X.clamp, X.place, X.focus, X.shadowed, X.rich_line, X.pill, X.F, X.AF
BEBAS, INTER_B, INTER_R = O.BEBAS, O.INTER_B, O.INTER_R
_C = {}

# ---------- face framing: the mouth above the caption line ----------
MOUTH_Y = 915.0
WIN = (227.0, 1653.0)
_orig_face_motion = G.face_motion


def face_motion(scale, face_x=None):
    if not isinstance(face_x, (list, tuple)): return _orig_face_motion(scale, face_x)
    fx, my = float(face_x[0]), float(face_x[1])
    s = scale / 100.0
    s = max(s, (WIN[1] - MOUTH_Y) / max(1.0, 1080 - my) + 1e-3, (MOUTH_Y - WIN[0]) / max(1.0, my) + 1e-3)     # keep the window covered
    cy = MOUTH_Y - (my - 540) * s
    cy = min(max(cy, WIN[1] - 540 * s), WIN[0] + 540 * s)
    half = 1920 * s / 2
    cx = min(max(W / 2 - (fx - 960) * s, W - half), half)
    top, bot = cy - 540 * s, cy + 540 * s
    cT = max(0.0, (WIN[0] - top) / s / 1080 * 100); cB = max(0.0, (bot - WIN[1]) / s / 1080 * 100)
    return dict(scale=round(s * 100, 3), pos=(round(cx / W, 6), round(cy / H, 6)), crop=dict(L=0, R=0, T=round(cT, 3), B=round(cB, 3)))


G.face_motion = face_motion


def mouth_frame_y(face_x, scale):
    m = face_motion(scale, face_x); s = m["scale"] / 100; cy = m["pos"][1] * H
    return cy + (face_x[1] - 540) * s


# ---------- entrances ----------
_orig_pop = O.pop_frame


def glide_frame(sprite, cx, cy, t, dur, t_in=0.36, t_out=0.26, dist=120):
    if t < t_in:
        u = t / t_in; dx = dist * (1 - u) ** 5; al = min(1.0, u / 0.35); v = dist * 5 * (1 - u) ** 4 / t_in / FPS
    elif t > dur - t_out:
        u = (t - (dur - t_out)) / t_out; dx = -50 * u ** 3; al = 1 - ease(u); v = 50 * 3 * u ** 2 / t_out / FPS
    else:
        dx, al, v = 0.0, 1.0, 0.0
    fr = blank()
    if al <= 0.01: return fr
    sh, pad = O.soft_shadow(sprite, blur=22, alpha=120, dy=10)
    sh, sx = O._hblur(sh, 0.5 * v)
    if al < 1: sh = O.with_alpha(sh, al)
    fr.alpha_composite(sh, (int(cx - sh.width / 2 + dx), int(cy - sh.height / 2)))
    return fr


def unfold_frame(sprite, cx, cy, t, dur, t_in=0.40, t_out=0.24):
    if t < t_in:
        u = t / t_in; sy = 0.08 + 0.92 * (1 - (1 - u) ** 5); al = min(1.0, u / 0.4)
    elif t > dur - t_out:
        u = (t - (dur - t_out)) / t_out; sy = 1 - 0.4 * ease(u); al = 1 - ease(u)
    else:
        sy, al = 1.0, 1.0
    fr = blank()
    if al <= 0.01: return fr
    sh, pad = O.soft_shadow(sprite, blur=22, alpha=120, dy=10)
    if sy < 0.999: sh = sh.resize((sh.width, max(1, int(sh.height * sy))), Image.LANCZOS)
    if al < 1: sh = O.with_alpha(sh, al)
    fr.alpha_composite(sh, (int(cx - sh.width / 2), int(cy - sh.height / 2)))
    return fr


def none_frame(sprite, cx, cy, t, dur, t_out=0.26):
    """frame 0 = the finished card (the hook: 'frame 0 carries ONE text layer plus the captions'); leaves with glide's exit"""
    if t > dur - t_out: return glide_frame(sprite, cx, cy, t, dur)
    fr = blank(); sh, pad = O.soft_shadow(sprite, blur=22, alpha=120, dy=10)
    fr.alpha_composite(sh, (int(cx - sh.width / 2), int(cy - sh.height / 2))); return fr


def pop_frame(sprite, cx, cy, t, dur, t_in=0.42, t_out=0.24, ent=None, from_xy=None):
    e = ent or O.ENTRANCE
    if e == "none": return none_frame(sprite, cx, cy, t, dur)
    if e == "glide": return glide_frame(sprite, cx, cy, t, dur)
    if e == "unfold": return unfold_frame(sprite, cx, cy, t, dur)
    return _orig_pop(sprite, cx, cy, t, dur, t_in, t_out, ent, from_xy)


O.pop_frame = pop_frame


def enter(g, sprite, cx, cy, t, dur):
    return pop_frame(sprite, cx, cy, t, dur, ent=g.get("entrance"))


# ---------- helpers ----------
def card(w, h, r=26, fill=(14, 14, 16, 236)):
    im = O.card_body((int(w), int(h)), r, fill, outline=(255, 255, 255, 40), width=2)
    return im


def frame_of(path, t, size=None):
    key = ("f", path, round(t, 3), size)
    if key not in _C:
        import subprocess, io
        r = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{t:.3f}", "-i", path, "-frames:v", "1", "-f", "image2pipe", "-vcodec", "png", "-"], capture_output=True)
        im = Image.open(io.BytesIO(r.stdout)).convert("RGBA")
        if size: im = im.resize(size, Image.LANCZOS)
        _C[key] = im
    return _C[key]


def yt_glyph(h=34):
    w = int(h * 1.42); im = Image.new("RGBA", (w * 3, h * 3), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle((0, 0, w * 3 - 1, h * 3 - 1), radius=int(h * 0.75), fill=(255, 0, 0, 255))
    d.polygon([(w * 1.18, h * 0.78), (w * 1.18, h * 2.22), (w * 2.05, h * 1.5)], fill=WHITE)
    return im.resize((w, h), Image.LANCZOS)


# ---------- kinds ----------
def k_teaser(plan, seq, g):
    dur = g["t1"] - g["t0"]; n = int(round(dur * FPS))
    pw, ph = g.get("w", 300), int(g.get("w", 300) * 16 / 9)
    st = frame_of(g["file"], g.get("t", 1.0), (pw, ph))
    m = O.rounded_mask((pw, ph), (0, 0, pw, ph), 30); st = st.copy(); st.putalpha(m)
    bz = 14; body = O.rrect((pw + 2 * bz, ph + 2 * bz), 44, (8, 8, 9, 255), outline=(255, 255, 255, 70), width=3)
    body.alpha_composite(st, (bz, bz))
    lab = pill(g["label"], 40) if g.get("label") else None
    side = g.get("side", "right")
    cx = g.get("cx", 820 if side == "right" else 260); cy = g.get("cy", 1400)

    def fn(i):
        t = i / FPS; fr = blank()
        tilt = -6 * (1 - ease(clamp(t / 0.5))) if t < 0.5 else 0.0
        sp = body.rotate(tilt, resample=Image.BICUBIC, expand=True) if abs(tilt) > 0.05 else body
        fr.alpha_composite(glide_frame(sp, cx, cy, t, dur))
        if lab and t > 0.25:
            u = t - 0.25; al, bl, sc = focus(u, dur - 0.25, 0.30, 0.24)
            lx = cx - body.width / 2 - lab.width / 2 - 24 if side == "right" else cx + body.width / 2 + lab.width / 2 + 24
            place(fr, shadowed(lab, 10, 130, 4), lx, cy + g.get("label_dy", 0), al=al, blur=bl, scale=sc)
        return fr
    return fn, n


def k_comments(plan, seq, g):
    dur = g["t1"] - g["t0"]; n = int(round(dur * FPS))
    fu, ft = F(INTER_B, 30), F(INTER_B, 40)
    bw = g.get("w", 760); cards = []
    for k, (ta, user, text) in enumerate(g["items"]):
        d = ImageDraw.Draw(Image.new("RGBA", (1, 1)))
        tw = min(bw - 150, d.textlength(text, font=ft)); h = 128
        c = card(bw, h, 24)
        cd = ImageDraw.Draw(c)
        av = Image.new("RGBA", (64, 64), (0, 0, 0, 0)); ImageDraw.Draw(av).ellipse((0, 0, 63, 63), fill=(70 + 40 * k, 90, 120 - 20 * k, 255))
        ImageDraw.Draw(av).text((32, 33), user[1:2].upper(), font=F(INTER_B, 30), fill=WHITE, anchor="mm")
        c.alpha_composite(av, (28, 32))
        cd.text((112, 30), user, font=fu, fill=(255, 255, 255, 150))
        cd.text((112, 66), text, font=ft, fill=WHITE)
        cards.append((ta - g["t0"], c))
    y0 = g.get("y", 1330); gap = g.get("gap", 18)

    def fn(i):
        t = i / FPS; fr = blank(); out_a = 1.0 if t < dur - 0.24 else 1 - ease((t - (dur - 0.24)) / 0.24)
        shown = [(tt, c) for tt, c in cards if t >= tt]
        for k, (tt, c) in enumerate(shown):
            u = t - tt; p = 1 - (1 - clamp(u / 0.36)) ** 4
            y = y0 + k * (128 + gap)
            sh = shadowed(c, 16, 130, 6)
            place(fr, sh, W / 2 + 60 * (1 - p), y, al=min(1.0, u / 0.15) * out_a, scale=0.94 + 0.06 * p)
        return fr
    return fn, n


def _audio(path, a, b, sr=8000):
    import subprocess
    x = np.frombuffer(subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{a}", "-t", f"{b - a}", "-i", path, "-vn", "-ac", "1", "-ar", str(sr), "-f", "f32le", "-"],
                                     capture_output=True).stdout, np.float32).astype(float)
    return x


def k_wave_cut(plan, seq, g):
    dur = g["t1"] - g["t0"]; n = int(round(dur * FPS))
    x = _audio(plan["obs_file"], g["src_t0"], g["src_t1"]); sr = 8000; hop = sr // 50          # 20 ms columns
    m = len(x) // hop; env = np.sqrt((x[:m * hop].reshape(m, hop) ** 2).mean(1)); db = 20 * np.log10(env + 1e-9)
    q = db < g.get("quiet_db", -45)
    gaps, k = [], 0
    while k < m:
        if q[k]:
            j = k
            while j < m and q[j]: j += 1
            if (j - k) * 0.02 >= g.get("min_gap", 0.30) and k > 0 and j < m: gaps.append((k, j))
            k = j
        else: k += 1
    amp = np.clip((db + 60) / 50, 0, 1)
    X0, X1, YC, HA = g.get("x0", 70), g.get("x1", 1010), g.get("yc", 600), g.get("h", 250)
    saved = sum(b - a for a, b in gaps) * 0.02
    cols = m; colw = (X1 - X0) / cols
    title = shadowed(rich_line(g.get("title", "THEIR *pauses*"), F(BEBAS, 64)), 10, 140, 4)
    chip = shadowed(pill(g.get("chip", "-{s} S OF DEAD AIR").replace("{s}", f"{saved:.1f}"), 46), 12, 130, 5)
    down = shadowed(pill(g["down_text"], 44, fill=(12, 12, 12, 232)), 12, 130, 5) if g.get("down_text") else None
    ingap = np.zeros(cols, bool)
    for a, b in gaps: ingap[a:b] = True
    t_mark, t_cut = g["mark_at"] - g["t0"], g["cut_at"] - g["t0"]

    def fn(i):
        t = i / FPS; fr = blank(); d = ImageDraw.Draw(fr)
        out_a = 1.0 if t < dur - 0.24 else 1 - ease((t - (dur - 0.24)) / 0.24)
        al, bl, sc = focus(t, 99, 0.36, 0)
        place(fr, title, W / 2, g.get("title_y", 262), al=al * out_a, blur=bl, scale=sc)
        draw = ease(clamp(t / 0.9))                                  # the strip draws on left -> right
        pc = clamp((t - t_cut) / 0.55); pc = 1 - (1 - pc) ** 4          # the collapse
        # the x of every column: gap columns shrink to 0 as pc -> 1, the rest re-centre
        wcol = np.where(ingap, colw * (1 - pc), colw); total = wcol.sum(); xs = X0 + (X1 - X0 - total) / 2 + np.concatenate([[0], np.cumsum(wcol)[:-1]])
        lay = blank(); ld = ImageDraw.Draw(lay)
        mark = clamp((t - t_mark) / 0.3)
        for c in range(int(cols * draw)):
            if wcol[c] < 0.3: continue
            hh = max(2.0, amp[c] * HA)
            col = (RED + (int(255 * (0.35 + 0.65 * mark)),)) if ingap[c] and mark > 0 else (235, 235, 238, 255)
            ld.rounded_rectangle((xs[c], YC - hh / 2, xs[c] + max(1.0, wcol[c] - 1.5), YC + hh / 2), 1, fill=col)
        if mark > 0 and pc < 1:
            for a, b in gaps:
                xa, xb = xs[a], xs[b - 1] + wcol[b - 1]
                if xb - xa > 4:
                    ld.rounded_rectangle((xa - 3, YC - HA / 2 - 18, xb + 3, YC + HA / 2 + 18), 10, outline=RED + (int(220 * mark * (1 - pc)),), width=3)
        fr.alpha_composite(lay)
        if t >= t_cut + 0.35:
            u = t - t_cut - 0.35; a2, b2, s2 = focus(u, 99, 0.30, 0)
            place(fr, chip, W / 2, YC + HA / 2 + 90, al=a2 * out_a, blur=b2, scale=s2)
        if down and g.get("down_at") and t >= g["down_at"] - g["t0"]:
            u = t - (g["down_at"] - g["t0"]); a3, b3, s3 = focus(u, 99, 0.30, 0)
            place(fr, down, W / 2, YC + HA / 2 + 170, al=a3 * out_a, blur=b3, scale=s3)
        return O.with_alpha(fr, out_a) if out_a < 1 else fr
    return fn, n


def k_episode_bar(plan, seq, g):
    dur = g["t1"] - g["t0"]; n = int(round(dur * FPS))
    X0, X1, Y = g.get("x0", 90), g.get("x1", 990), g.get("y", 640)
    title = shadowed(rich_line(g.get("title", "ONE *full* EPISODE"), F(BEBAS, 64)), 10, 140, 4)
    lab = rich_line(g.get("label", "1:30:00"), F(BEBAS, 40), fill=(255, 255, 255, 190))
    marks = [(ta - g["t0"], fr_, shadowed(pill(txt, 36, dot=False, fill=GOLD + (255,), hair=(255, 255, 255, 0), color=(12, 12, 12, 255)), 10, 120, 4)) for ta, fr_, txt in g["markers"]]
    final = shadowed(rich_line(g["final"], F(BEBAS, 70)), 12, 140, 5) if g.get("final") else None

    def fn(i):
        t = i / FPS; fr = blank(); lay = blank(); d = ImageDraw.Draw(lay)
        out_a = 1.0 if t < dur - 0.24 else 1 - ease((t - (dur - 0.24)) / 0.24)
        al, bl, sc = focus(t, 99, 0.36, 0); place(fr, title, W / 2, g.get("title_y", 262), al=al, blur=bl, scale=sc)
        p = ease(clamp((t - 0.1) / 0.7))
        d.rounded_rectangle((X0, Y - 9, X0 + (X1 - X0) * p, Y + 9), 9, fill=(70, 70, 76, 255))
        if p > 0.6: place(lay, lab, X0 + lab.width / 2 - 8, Y + 52, al=clamp((p - 0.6) / 0.4))
        scan = clamp((t - 0.4) / max(0.5, (marks[-1][0] if marks else dur) - 0.2))
        if p >= 1 and scan < 1:
            px = X0 + (X1 - X0) * scan; d.rounded_rectangle((X0, Y - 9, px, Y + 9), 9, fill=(150, 150, 156, 255))
            d.ellipse((px - 13, Y - 13, px + 13, Y + 13), fill=WHITE)
        for tt, f_, sp in marks:
            if t < tt: continue
            u = t - tt; q = 1 - (1 - clamp(u / 0.32)) ** 4; x = X0 + (X1 - X0) * f_
            glow = blank(); ImageDraw.Draw(glow).rounded_rectangle((x - 9, Y - 70 * q, x + 9, Y + 9), 6, fill=GOLD + (255,))
            lay.alpha_composite(O.with_alpha(glow.filter(ImageFilter.GaussianBlur(12)), 0.7)); lay.alpha_composite(glow)
            place(lay, sp, x, Y - 70 * q - 40, al=clamp(u / 0.15), scale=0.8 + 0.2 * q)
        fr.alpha_composite(lay)
        if final and t >= g["final_at"] - g["t0"]:
            u = t - (g["final_at"] - g["t0"]); a2, b2, s2 = focus(u, 99, 0.34, 0)
            place(fr, final, W / 2, Y + 170, al=a2, blur=b2, scale=s2)
        return O.with_alpha(fr, out_a) if out_a < 1 else fr
    return fn, n


def k_source_tag(plan, seq, g):
    dur = g["t1"] - g["t0"]; n = int(round(dur * FPS))
    gl = yt_glyph(30); tx = rich_line(g["handle"], F(INTER_B, 30))
    sp = Image.new("RGBA", (gl.width + tx.width + 20, max(gl.height, tx.height) + 8), (0, 0, 0, 0))
    sp.alpha_composite(gl, (0, (sp.height - gl.height) // 2)); sp.alpha_composite(tx, (gl.width + 6, (sp.height - tx.height) // 2 + 2))
    sp = shadowed(sp, 8, 170, 2); x, y = g.get("x", 40), g.get("y", 990)

    def fn(i):
        t = i / FPS; fr = blank(); al, bl, sc = focus(t, dur, 0.30, 0.24)
        place(fr, sp, x + sp.width / 2, y, al=al, blur=bl, scale=sc); return fr
    return fn, n


def k_teaser2(plan, seq, g):
    """two phones (our YouTube cut + our Instagram cut stills), tilting in one after the other, labels under each"""
    dur = g["t1"] - g["t0"]; n = int(round(dur * FPS)); pw = g.get("w", 230); ph = int(pw * 16 / 9); bz = 12
    phones = []
    for k, (f, tt, lab) in enumerate(g["phones"]):
        st = frame_of(f, tt, (pw, ph)).copy(); st.putalpha(O.rounded_mask((pw, ph), (0, 0, pw, ph), 26))
        body = O.rrect((pw + 2 * bz, ph + 2 * bz), 38, (8, 8, 9, 255), outline=(255, 255, 255, 70), width=3); body.alpha_composite(st, (bz, bz))
        phones.append((body, shadowed(pill(lab, 34, dot=False), 8, 120, 3)))
    xs = g.get("xs", [700, 930]); cy = g.get("cy", 1420)

    def fn(i):
        t = i / FPS; fr = blank()
        for k, (body, lab) in enumerate(phones):
            u = t - k * 0.22
            if u <= 0: continue
            tilt = (-7 if k == 0 else 7) * (1 - ease(clamp(u / 0.5)))
            sp = body.rotate(tilt, resample=Image.BICUBIC, expand=True) if abs(tilt) > 0.05 else body
            fr.alpha_composite(glide_frame(sp, xs[k], cy, u, dur - k * 0.22))
            if u > 0.3:
                a2, b2, s2 = focus(u - 0.3, dur - k * 0.22 - 0.3, 0.28, 0.24); place(fr, lab, xs[k], cy + body.height / 2 + 34, al=a2, blur=b2, scale=s2)
        if g.get("label") and t > 0.4:
            a3, b3, s3 = focus(t - 0.4, dur - 0.4, 0.3, 0.24)
            sp = shadowed(pill(g["label"], 40), 10, 130, 4); place(fr, sp, g.get("label_x", 300), cy, al=a3, blur=b3, scale=s3)
        return fr
    return fn, n


def k_audience(plan, seq, g):
    """two concentric audiences on the stage: a small circle (small_label) lit gold at small_at, the big one (big_label) dim; at big_at
    the big circle fills gold and grows 4 %. Titles [[t_abs, rich], ...] as the reel's bars."""
    dur = g["t1"] - g["t0"]; n = int(round(dur * FPS)); cx, cy, RB, RS = W / 2, g.get("cy", 640), g.get("rb", 300), g.get("rs", 92)
    titles = [(tt - g["t0"], shadowed(rich_line(txt, F(BEBAS, 64)), 10, 140, 4)) for tt, txt in g["titles"]]
    lb, ls = rich_line(g["big_label"], F(BEBAS, 46)), rich_line(g["small_label"], F(BEBAS, 40), fill=(12, 12, 12, 255))
    t_s, t_b = g["small_at"] - g["t0"], g["big_at"] - g["t0"]

    def disc(r, fill, outline, w=4):
        ss = 3; im = Image.new("RGBA", (int(2 * r * ss + 8 * ss), int(2 * r * ss + 8 * ss)), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
        d.ellipse((4 * ss, 4 * ss, 4 * ss + 2 * r * ss, 4 * ss + 2 * r * ss), fill=fill, outline=outline, width=w * ss)
        return im.resize((im.width // ss, im.height // ss), Image.LANCZOS)

    def fn(i):
        t = i / FPS; fr = blank(); out_a = 1.0 if t < dur - 0.24 else 1 - ease((t - (dur - 0.24)) / 0.24)
        k = max([j for j, (tt, _) in enumerate(titles) if tt <= t + 1e-6] or [0])
        for j in (k - 1, k):
            if j < 0: continue
            tt, sp = titles[j]
            if j == k: al, bl, sc = focus(t - tt, 99, 0.34, 0)
            else:
                u = t - titles[k][0]
                if u >= 0.22: continue
                al, bl, sc = 1 - ease(u / 0.22), 6 * ease(u / 0.22), 1.0
            place(fr, sp, W / 2, g.get("title_y", 262), al=al, blur=bl, scale=sc)
        pb = ease(clamp(t / 0.5)); qb = ease(clamp((t - t_b) / 0.45)) if t >= t_b else 0.0
        big = disc(RB * (0.9 + 0.1 * pb) * (1 + 0.04 * qb), (int(40 + 150 * qb), int(40 + 120 * qb), int(44 + 50 * qb), int(255 * (0.55 + 0.35 * qb))), (255, 255, 255, 60))
        if qb > 0: fr.alpha_composite(O.with_alpha(big.filter(ImageFilter.GaussianBlur(22)), 0.35 * qb), (int(cx - big.width / 2), int(cy - big.height / 2)))
        place(fr, big, cx, cy, al=pb)
        place(fr, lb, cx, cy - RB * 0.62, al=pb * (1 - 0.0 * qb))
        ps = ease(clamp((t - t_s) / 0.35)) if t >= t_s else 0.0
        if ps > 0:
            sm = disc(RS * (0.7 + 0.3 * ps), GOLD + (255,), (255, 255, 255, 120), 3)
            fr.alpha_composite(O.with_alpha(sm.filter(ImageFilter.GaussianBlur(14)), 0.5 * ps), (int(cx - sm.width / 2), int(cy + 70 - sm.height / 2)))
            place(fr, sm, cx, cy + 70, al=ps); place(fr, ls, cx, cy + 72, al=ps)
        return O.with_alpha(fr, out_a) if out_a < 1 else fr
    return fn, n


def k_filler_strip(plan, seq, g):
    """FX-18 + FX-55 on THEIR audio: their words land one by one as chips in a centred strip (y); a filler (fillers set) lands red and is
    struck through 0.25 s later, then shrinks out of the strip (the cut a clipper makes). words [[t_abs, "text"], ...]."""
    dur = g["t1"] - g["t0"]; n = int(round(dur * FPS)); fills = set(x.lower() for x in g.get("fillers", ["uh", "um", "well", "like", "you know"]))
    fb = F(INTER_B, g.get("size", 40)); y = g.get("y", 300); gap = 14
    chips = []
    for tt, txt in g["words"]:
        bad = txt.lower().strip(",.?") in fills
        d = ImageDraw.Draw(Image.new("RGBA", (1, 1))); w = int(d.textlength(txt, font=fb)) + 40; h = int(fb.size * 1.7)
        c = O.rrect((w, h), h // 2, (RED + (255,)) if bad else (16, 16, 18, 236), outline=(255, 255, 255, 60), width=2)
        ImageDraw.Draw(c).text((w / 2, h / 2 + 1), txt, font=fb, fill=WHITE, anchor="mm")
        chips.append((tt - g["t0"], bad, c))
    t_cut = g.get("cut_at", g["t1"]) - g["t0"]

    def fn(i):
        t = i / FPS; fr = blank(); out_a = 1.0 if t < dur - 0.24 else 1 - ease((t - (dur - 0.24)) / 0.24)
        shown = [(tt, bad, c) for tt, bad, c in chips if t >= tt]
        ws = []
        for tt, bad, c in shown:
            sc = 1.0
            if bad and t > t_cut: sc = 1 - ease(clamp((t - t_cut) / 0.4))
            ws.append(c.width * sc)
        rows, cur, cw = [], [], 0                                       # wrap into rows of <= 960 px
        for (tt, bad, c), w in zip(shown, ws):
            if cur and cw + w + gap > 960: rows.append(cur); cur, cw = [], 0
            cur.append((tt, bad, c, w)); cw += w + gap
        if cur: rows.append(cur)
        for r_, row in enumerate(rows):
            tot = sum(x[3] for x in row) + gap * (len(row) - 1); x = W / 2 - tot / 2; yy = y + r_ * 74
            for tt, bad, c, w in row:
                if w < 2: x += gap * 0; continue
                u = t - tt; p = 1 - (1 - clamp(u / 0.22)) ** 3
                sp = c if abs(w - c.width) < 0.5 else c.resize((max(1, int(w)), c.height), Image.LANCZOS)
                if bad and u > 0.25:
                    sp = sp.copy(); q = clamp((u - 0.25) / 0.2); ImageDraw.Draw(sp).line((10, sp.height / 2, 10 + (sp.width - 20) * q, sp.height / 2), fill=WHITE, width=4)
                place(fr, shadowed(sp, 8, 130, 3), x + w / 2, yy + 14 * (1 - p), al=p * out_a)
                x += w + gap
        return fr
    return fn, n


_orig_teaser = k_teaser
NEW6 = {"teaser": k_teaser, "teaser2": k_teaser2, "comments": k_comments, "wave_cut": k_wave_cut, "episode_bar": k_episode_bar, "source_tag": k_source_tag,
        "audience": k_audience, "filler_strip": k_filler_strip}
X.NEW.update(NEW6)
O.PANEL_KINDS = set(O.PANEL_KINDS) | {"wave_cut", "episode_bar", "audience", "filler_strip"}


# ---- 2026-11-02 reviewer fixes (Drinkin' Bros r1) ----
_k_ring = X.NEW["ring"] if "ring" in X.NEW else X.k_ring


def k_ring6(plan, seq, g):
    """ring + chip_dy: the chip moved down by chip_dy px (clear of the sample's own burnt caption under the box)"""
    fn0, n = _k_ring(plan, seq, g); dy = g.get("chip_dy", 0)
    if not dy: return fn0, n

    def fn(i):
        orig = X.place
        X.place = lambda fr, sp, cx, cy, **k: orig(fr, sp, cx, cy + dy, **k)
        try: return fn0(i)
        finally: X.place = orig
    return fn, n


X.NEW["ring"] = k_ring6


def ba_frames6(plan, seq, g, f0, n):
    """overlays.ba_frames + tag_pos "bottom" for ba_wipe: the tags ride the card's BOTTOM corners (the top ones sat at frame y ~93, inside
    the platform's top-200 band). Everything else is overlays.ba_frames, line for line."""
    if g["kind"] != "ba_wipe" or g.get("tag_pos", "top") == "top":
        yield from _ba_frames(plan, seq, g, f0, n); return
    P = G.BOX; pw, ph = P[2] - P[0], P[3] - P[1]; dur = g["t1"] - g["t0"]
    cw, ch = 520, 924; xs = [(O.W - cw) / 2 - P[0]]; y0 = (ph - ch) / 2
    words = g.get("tags") or ["ORIGINAL", "OURS"]
    srcB = O.media_pipe(plan, seq, g["before"], f0, n, cw, ch); srcA = O.media_pipe(plan, seq, g["after"], f0, n, cw, ch)
    cmask = O.rounded_mask((cw, ch), (0, 0, cw, ch), 28)
    m = 60; dress = O.card_dressing((cw + 2 * m, ch + 2 * m), (m, m, m + cw, m + ch), 28)
    from PIL import ImageFont
    fb = O.text_sprite(words[0] or " ", ImageFont.truetype(O.INTER_B, 26), (255, 255, 255, 230))
    fa_ = O.text_sprite(words[1] or " ", ImageFont.truetype(O.INTER_B, 26), O.GOLD + (255,))
    rtl = g.get("dir") == "rtl"
    line = Image.new("RGBA", (40, ch), (0, 0, 0, 0)); ImageDraw.Draw(line).rectangle((18, 0, 21, ch), fill=(255, 255, 255, 120))
    line = line.filter(ImageFilter.GaussianBlur(5)); ImageDraw.Draw(line).rectangle((18, 0, 21, ch), fill=(255, 255, 255, 255))
    # a soft dark foot under the tag so it reads on any picture
    foot = Image.new("RGBA", (cw, 90), (0, 0, 0, 0)); fd = ImageDraw.Draw(foot)
    for yy in range(90): fd.line((0, yy, cw, yy), fill=(0, 0, 0, int(150 * yy / 89)))
    for i in range(f0, f0 + n):
        t = i / O.FPS_MG
        bf, af = next(srcB), next(srcA)
        panel = O._backdrop(af, pw, ph, g.get("dim", 0.35)).convert("RGBA")
        fr_ = O._wipe_frac(g, t); xl = int(round(cw * (1 - fr_ if rtl else fr_)))
        bp, ap = bf.convert("RGBA"), af.convert("RGBA")
        (tb, mb), (ta, ma) = fb, fa_
        yb = ch - 18 - (tb.height - 2 * mb) - mb; ya = ch - 18 - (ta.height - 2 * ma) - ma
        bpos = (18 - mb, yb) if rtl else (cw - 18 - (tb.width - 2 * mb) - mb, yb)
        apos = (cw - 18 - (ta.width - 2 * ma) - ma, ya) if rtl else (18 - ma, ya)
        if words[0]: bp.alpha_composite(foot, (0, ch - 90))
        if words[1]: ap.alpha_composite(foot, (0, ch - 90))
        if words[0]: bp.alpha_composite(tb, bpos)
        if words[1]: ap.alpha_composite(ta, apos)
        pic = bp
        if fr_ > 0:
            if rtl: pic.paste(ap.crop((xl, 0, cw, ch)), (xl, 0))
            else: pic.paste(ap.crop((0, 0, xl, ch)), (0, 0))
        if 0 < fr_ < 1: pic.alpha_composite(line, (xl - 20, 0))
        pic.putalpha(cmask)
        sp = dress.copy(); sp.alpha_composite(pic, (m, m))
        panel.alpha_composite(sp, (int(round(xs[0] - m)), int(round(y0 - m))))
        fr = Image.new("RGBA", (O.W, O.H), (0, 0, 0, 0))
        fr.paste(O.with_alpha(panel, O.fade_al(t, dur, g.get("fade_in", 0.3), 0.24)), (P[0], P[1]))
        yield fr


def k_still_card6(plan, seq, g):
    """mgx.k_still_card + badge_at "below": the gold badge sits UNDER the card, centred below the ring (the default sits on the ring's
    top edge, i.e. on the line above it: on the Still Here header it covered the channel name). Otherwise mgx.k_still_card, line for line."""
    if g.get("badge_at", "top") == "top": return _k_still_card(plan, seq, g)
    E, C, FPS, W = X.ease, X.clamp, X.FPS, X.W
    dur = g["t1"] - g["t0"]; n = int(round(dur * FPS))
    src = X._obs_frame(plan, seq, g["obs_t"], g["box"]); s = g["w"] / src.width
    card = src.resize((int(src.width * s), int(src.height * s)), Image.LANCZOS)
    m = O.rounded_mask(card.size, (0, 0, card.width, card.height), 22); card.putalpha(m)
    pad = 40; full = Image.new("RGBA", (card.width + 2 * pad, card.height + 2 * pad), (0, 0, 0, 0)); full.alpha_composite(card, (pad, pad))
    full.alpha_composite(O.card_dressing(full.size, (pad, pad, pad + card.width, pad + card.height), 22))
    rx0, ry0, rx1, ry1 = g["ring"]; bx, by = g["box"][0], g["box"][1]
    rr = (pad + (rx0 - bx) * s, pad + (ry0 - by) * s, pad + (rx1 - bx) * s, pad + (ry1 - by) * s)
    tag = X.shadowed(X.pill(g["tag"], 42), 12, 130, 5) if g.get("tag") else None
    badge = X.shadowed(X.pill(g["badge"], 46, dot=False, fill=X.GOLD + (255,), hair=(255, 255, 255, 0), color=(12, 12, 12, 255)), 10, 120, 4)

    def fn(i):
        t = i / FPS; fr = X.blank(); al, bl, sc = X.focus(t, dur)
        im = full.copy()
        if t >= g["ring_at"] - g["t0"]:
            q = E((t - (g["ring_at"] - g["t0"])) / 0.42)
            m2 = 30; ol = X._round_outline((int(rr[2] - rr[0]) + 2 * m2, int(rr[3] - rr[1]) + 2 * m2), (m2, m2, m2 + rr[2] - rr[0], m2 + rr[3] - rr[1]), 14, q, width=5)
            im.alpha_composite(ol, (int(rr[0] - m2), int(rr[1] - m2)))
        X.place(fr, im, g["cx"], g["cy"], al=al, blur=bl, scale=sc, dy=26 * (1 - E(C(t / 0.38))))
        if t >= g["ring_at"] - g["t0"] and E((t - (g["ring_at"] - g["t0"])) / 0.42) >= 0.6:     # the badge UNDER the card, below the ring
            u = (t - (g["ring_at"] - g["t0"]) - 0.25) / 0.25; k = 0.6 + 0.4 * E(C(u))
            bsp = badge.resize((max(1, int(badge.width * k)), max(1, int(badge.height * k))), Image.LANCZOS)
            X.place(fr, bsp, g["cx"] - full.width / 2 + (rr[0] + rr[2]) / 2, g["cy"] + full.height / 2 + 16, al=al * C(u * 2))
        if tag:
            a2, b2, s2 = X.focus(t - 0.15, dur - 0.15, 0.32, 0.24) if t >= 0.15 else (0, 0, 1)
            X.place(fr, tag, W / 2, g.get("tag_y", 236), al=a2, blur=b2, scale=s2)
        return fr
    return fn, n


_k_still_card = X.NEW["still_card"]
X.NEW["still_card"] = k_still_card6

_ba_frames = O.SEEKABLE["ba_wipe"]
O.SEEKABLE["ba_wipe"] = ba_frames6
O.ba_frames = ba_frames6


if __name__ == "__main__":
    a = sys.argv[1:]
    plan, seq = O.load(a[0])
    if plan.get("mouth_y"): MOUTH_Y = float(plan["mouth_y"])
    if "--captions" in a: O.build_captions(plan)
    if "--mg" in a: O.build_mg(plan, seq, a[a.index("--only") + 1] if "--only" in a else None)
    if "--check" in a:
        e_, _ = O.check(plan, seq); e2 = X.stage_check(plan, seq)
        if e_ or e2: sys.exit(1)
    if "--still" in a:
        sys.argv = [sys.argv[0]] + a          # reuse the reel's fast still (preview.render sees the patched face_motion)
        import runpy
        ts = [float(x) for x in a[a.index("--still") + 1:] if not x.startswith("--")]
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        import preview

        def fast_still(t):
            base = preview.render(plan, seq, t).convert("RGBA")
            for g in sorted(plan["graphics"], key=lambda g: 0 if g["kind"] == "showcase" else 1):
                if not (g["t0"] <= t < g["t1"]): continue
                for it in (g["items"] if g["kind"] == "group" else [g]):
                    if it["t0"] <= t < it["t1"]:
                        if it["kind"] in O.SEEKABLE:
                            fr = next(O.SEEKABLE[it["kind"]](plan, seq, it, int((t - it["t0"]) * FPS), 1), None)
                            if fr: base.alpha_composite(fr)
                            continue
                        fn, _ = O._frame_fn(plan, seq, it); base.alpha_composite(fn(int((t - it["t0"]) * FPS)))
            if plan.get("seam_line") and not G.face_at(plan, t):
                qq = O.seam_frac(plan, t); base.alpha_composite(O.seam_line_png(4) if qq >= 1 else O.seam_line_png(4, qq))
            cj = os.path.join(plan["_dir"], "overlays", "captions.json")
            if os.path.exists(cj):
                for c in json.load(open(cj, encoding="utf-8")):
                    if c["t0"] <= t < c["t1"]: base.alpha_composite(O.caption_png(c["text"]))
            return base.convert("RGB")
        ims = [fast_still(t) for t in ts]
        from PIL import ImageFont
        fnt = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 54)
        for t, im in zip(ts, ims): ImageDraw.Draw(im).text((24, 1850), f"{t:.2f}", font=fnt, fill=(255, 220, 0))
        w, h = 432, 768
        sheet = Image.new("RGB", (w * min(5, len(ims)), h * ((len(ims) + 4) // 5)))
        for i, im in enumerate(ims): sheet.paste(im.resize((w, h), Image.LANCZOS), ((i % 5) * w, (i // 5) * h))
        p = os.path.join(plan["_dir"], "work", "stills.jpg"); sheet.save(p, quality=88); print(p)
