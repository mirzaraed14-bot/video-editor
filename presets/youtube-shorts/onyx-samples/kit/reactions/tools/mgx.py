"""mgx.py: the M look (the @affancuts reel "Shorts cooked") = overlays.py + the new kinds below, JOB-LOCAL.

  PYTHONUTF8=1 python mgx.py plan.json [--captions] [--mg] [--only id,id] [--check] [--still t t ...]     (overlays.py's CLI)

Why job-local: the shared toolkit (`_onyx-batch-2026-10/reactions/tools/overlays.py`) is being run by the J-L builder at the same
time; these kinds are patched into it at import (O._frame_fn, O.caption_chunks, O.caption_png), so its renderer, its checker and its
stills see them, and nothing on disk changes for anyone else.

Kinds (every one {id, kind, t0, t1}; times are sequence seconds; *word* = the accent face, gold):
  stage        any graphic with "stage": {"in": s, "out": s} first paints the PANEL backdrop (x 0-1080, y 44-1038: a dark graphite
               gradient + vignette) at full opacity, fading it in / out over "in" / "out" seconds at its own edges (0 = a hard
               join with the next stage scene, so a run of stage scenes reads as one stage)
  hook_big     frame 0 visible (no entrance): ghost {"text", "y", "alpha", "w"} (FX-41: a 75 %-wide ghost word, slow drift) + a
               two-line block at y: phases [[t_abs, line1, line2], ...] (line1 Bebas 84 white, line2 the accent face 150 gold);
               phase swaps focus-cross in 0.30 s; leaves with a 0.25 s focus-out
  era          FX-04: a persistent pill (gold dot + Bebas 44, rich text) at x, y (left edge), wiped in left->right 0.36 s
  ring         a gold rounded outline drawn round plan.boxes[box] (followed through the view every frame), pad, draw_at (s after
               t0), chip (Bebas 40 on a dark pill, "above" | "below"), count [value, suffix, dur] = the chip counts up to it
  sweep        gold underlines drawn under several boxes in turn (boxes [...], every 0.08 s) + an optional chip at chip_xy
  still_card   a crop of the SCREEN recording at obs_t (box = source px), as a card at cx, cy, width w; ring (source px) drawn at
               ring_at (abs) with a badge; tag = a pill above the card
  bars         FX-69 honest-scale bar chart on the stage: data [{v, style other|white|gold, label, sub, at}], vmax, title, group
               [i0, i1, text] (a bracket under the slivers), pin {at, text, sub} on the last gold bar, stamp {at, text}, push
               (FX-73: a slow z push of the whole chart, e.g. 1.05)
  grid         FX-66 the episode grid on the stage: 20 tiles (5 x 4) appearing from tiles_at, gold [indices] turning gold at gold_at
               (the rest dim), extract_at (every tile lights white), ask_at ("?" on each), waste_at (the non-gold tiles drop and
               fade), stamp (copies, e.g. mass production: tiles stamp in at "stamp_every"), titles [[t_abs, rich text], ...]
  stage_title  big centred type on the stage: label, lines [rich, ...], y; phases [[t_abs, label, [lines]]] optional
  low_title    a face-only beat's title in the low band: lines at y (Bebas 92 + accent), a dark pill behind
Entrances: "focus" (the M lead: 14 px blur -> 0, scale 1.05 -> 1, fade, 0.38 s easeOutCubic; out 0.24 s).
Captions: plan["caption_emph"] = [[t, "WORD"], ...]: that word of the chunk on screen at t is drawn gold (white base + one
coloured emphasis word; Affan's caption rule), everything else exactly overlays.py's captions.
"""
import json, math, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "_onyx-batch-2026-10", "reactions", "tools"))
import overlays as O                      # noqa: E402
from PIL import Image, ImageDraw, ImageFilter  # noqa: E402

W, H, GOLD, FPS = O.W, O.H, O.GOLD, O.FPS_MG
PANEL = (0, 44, 1080, 1038)
INTER_B, INTER_K, BEBAS = O.INTER_B, O.INTER_K, O.BEBAS
ease, eio = O.ease, O.ease_io3
WHITE = (255, 255, 255, 255)
_C = {}


def F(path, size, axes=None): return O.font_at(path, size, axes)
def AF(size): return O.font_at(O.ACCENT_FONT, size, O.accent_axes(O.ACCENT_FONT))
def clamp(x, a=0.0, b=1.0): return max(a, min(b, x))
def blank(): return Image.new("RGBA", (W, H), (0, 0, 0, 0))


def text_w(d, s, f): return d.textlength(s, font=f)


def rich_line(text, fb, fa=None, fill=WHITE, acc=None, track=0):
    """a sprite of one rich line: plain runs in fb, *runs* in fa (default: the accent face at the base's cap height)"""
    fa = fa or O.accent_for(fb); acc = acc or GOLD + (255,)
    runs = O.rich_runs(text) if O.is_rich(text) else [(text, False)]
    d = ImageDraw.Draw(Image.new("RGBA", (1, 1)))
    asc = max(-(fa.getbbox("Hg", anchor="ls")[1]), -(fb.getbbox("Hg", anchor="ls")[1])) + 6
    desc = max(fa.getbbox("Hgy", anchor="ls")[3], fb.getbbox("Hgy", anchor="ls")[3]) + 6
    widths = [text_w(d, s, fa if a else fb) + (0.04 * fa.size if a else 0) for s, a in runs]
    im = Image.new("RGBA", (int(sum(widths)) + 16, asc + desc), (0, 0, 0, 0)); dd = ImageDraw.Draw(im)
    x = 8
    for (s, a), w in zip(runs, widths):
        dd.text((x, asc), s, font=fa if a else fb, fill=acc if a else fill, anchor="ls"); x += w
    return im


def shadowed(sp, blur=10, alpha=140, dy=4):
    sh, pad = O.soft_shadow(sp, blur=blur, alpha=alpha, dy=dy); return sh


def place(fr, sp, cx, cy, al=1.0, blur=0.0, scale=1.0, dy=0.0):
    if al <= 0.01: return
    if abs(scale - 1) > 1e-3: sp = sp.resize((max(1, int(sp.width * scale)), max(1, int(sp.height * scale))), Image.LANCZOS)
    if blur > 0.4: sp = sp.filter(ImageFilter.GaussianBlur(blur))
    if al < 0.999: sp = O.with_alpha(sp, al)
    fr.alpha_composite(sp, (int(round(cx - sp.width / 2)), int(round(cy - sp.height / 2 + dy))))


def focus(t, dur, t_in=0.38, t_out=0.24):
    """(alpha, blur, scale) of the focus entrance at t (s from t0) of a dur-long graphic"""
    if t_in > 0 and t < t_in:
        p = ease(t / t_in); return clamp(t / (t_in * 0.7)), 14 * (1 - p), 1.05 - 0.05 * p
    if t_out > 0 and t > dur - t_out:
        p = ease((t - (dur - t_out)) / t_out); return 1 - p, 6 * p, 1 - 0.02 * p
    return 1.0, 0.0, 1.0


# ---------- the stage ----------
def stage_bg():
    if "stage" not in _C:
        x0, y0, x1, y1 = PANEL; w, h = x1 - x0, y1 - y0
        im = Image.new("RGBA", (w, h), (0, 0, 0, 255)); px = im.load()
        g = Image.new("L", (w // 4, h // 4)); gp = g.load()
        for y in range(h // 4):
            for x in range(w // 4):
                dx, dy = (x * 4 - w / 2) / (w * 0.62), (y * 4 - h * 0.38) / (h * 0.75)
                gp[x, y] = int(clamp(1 - math.sqrt(dx * dx + dy * dy)) * 255)
        g = g.resize((w, h), Image.BICUBIC).filter(ImageFilter.GaussianBlur(6))
        lo, hi = (9, 9, 10), (27, 26, 28)
        base = Image.new("RGBA", (w, h), lo + (255,)); top = Image.new("RGBA", (w, h), hi + (255,))
        im = Image.composite(top, base, g)
        ImageDraw.Draw(im).line([(0, 0), (w, 0)], fill=(255, 255, 255, 18), width=1)
        fr = blank(); fr.paste(im, (x0, y0)); _C["stage"] = fr
    return _C["stage"]


def stage_alpha(g, t, dur):
    st = g.get("stage") or {}
    a = 1.0
    if st.get("in", 0) > 0 and t < st["in"]: a = eio(t / st["in"])
    if st.get("out", 0) > 0 and t > dur - st["out"]: a = min(a, 1 - eio((t - (dur - st["out"])) / st["out"]))
    return a


def with_stage(g, fn):
    dur = g["t1"] - g["t0"]
    if not g.get("stage"): return fn

    def f(i):
        t = i / FPS; fr = blank(); a = stage_alpha(g, t, dur)
        bg = stage_bg()
        fr.alpha_composite(bg if a >= 0.999 else O.with_alpha(bg, a))
        top = fn(i); fr.alpha_composite(top if a >= 0.999 else O.with_alpha(top, a)); return fr
    return f


# ---------- pills / chips ----------
def pill(text, size=44, dot=True, fill=(12, 12, 12, 232), hair=(255, 255, 255, 46), color=WHITE):
    f = F(BEBAS, size); sp = rich_line(text, f, fill=color)
    w, h = sp.width + (58 if dot else 36), int(size * 1.62)
    im = O.card_body((w, h), h // 2, fill, outline=hair, width=2) if fill[:3] == (12, 12, 12) else O.rrect((w, h), h // 2, fill, outline=hair, width=2)
    d = ImageDraw.Draw(im)
    if dot: d.ellipse((24, h / 2 - 7, 38, h / 2 + 7), fill=GOLD + (255,))
    im.alpha_composite(sp, ((46 if dot else 18) - 8, int(h / 2 - sp.height / 2 + 2)))
    return im


def fmt_count(v, suffix):
    return f"{int(round(v))}{suffix}"


# ---------- kinds ----------
def k_hook_big(plan, seq, g):
    dur = g["t1"] - g["t0"]; n = int(round(dur * FPS))
    gh = g.get("ghost")
    if gh:
        f = F(BEBAS, 400); d = ImageDraw.Draw(Image.new("RGBA", (1, 1)))
        tw = text_w(d, gh["text"], f); size = int(400 * gh.get("w", 0.75) * W / tw)
        gsp = rich_line(gh["text"], F(BEBAS, size), fill=(255, 255, 255, int(255 * gh.get("alpha", 0.16))))
    f1, f2 = F(BEBAS, g.get("size1", 84)), AF(g.get("size2", 150))
    sprites = []
    for ph in g["phases"]:
        a = rich_line(ph[1], f1, fill=(255, 255, 255, 235)); b = rich_line(ph[2], f2, fa=f2, fill=GOLD + (255,)) if ph[2] else None
        sprites.append((ph[0] - g["t0"], shadowed(a, 12, 150, 4), shadowed(b, 16, 150, 6) if b else None))
    y = g.get("y", 1430)

    def fn(i):
        t = i / FPS; fr = blank()
        out_a = 1.0 if t < dur - 0.25 else 1 - ease((t - (dur - 0.25)) / 0.25)
        if gh:
            p = t / max(dur, 1e-3)
            place(fr, gsp, W / 2, gh["y"] - 24 * p, al=out_a, scale=1.0 + 0.035 * p)
        k = max((j for j, s in enumerate(sprites) if s[0] <= t + 1e-6), default=-1)     # phases=[] -> the ghost alone (v3)
        for j in ((k - 1, k) if k >= 0 else ()):
            if j < 0: continue
            t0, a, b = sprites[j]
            if j == k:
                u = t - t0; al, bl, sc = (1.0, 0.0, 1.0) if (j == 0 or u >= 0.30) else (ease(u / 0.30), 10 * (1 - ease(u / 0.30)), 1.04 - 0.04 * ease(u / 0.30))
            else:
                u = t - sprites[k][0]
                if u >= 0.22: continue
                al, bl, sc = 1 - ease(u / 0.22), 6 * ease(u / 0.22), 1.0
            al *= out_a
            place(fr, a, W / 2, y - (a.height / 2 + 8 if b else 0), al=al, blur=bl, scale=sc)
            if b: place(fr, b, W / 2, y + b.height / 2 - 30, al=al, blur=bl, scale=sc)
        return fr
    return fn, n


def k_era(plan, seq, g):
    dur = g["t1"] - g["t0"]; n = int(round(dur * FPS)); sp = shadowed(pill(g["text"], g.get("size", 44)), 14, 130, 6)

    def fn(i):
        t = i / FPS; fr = blank(); x, y = g.get("x", 56), g.get("y", 250)
        if t < 0.36:
            p = eio(t / 0.36); m = Image.new("L", sp.size, 0); ImageDraw.Draw(m).rectangle((0, 0, int(sp.width * p), sp.height), fill=255)
            s = sp.copy(); s.putalpha(O.ImageChops.multiply(sp.split()[3], m))
            fr.alpha_composite(s, (int(x - 14 + 14 * p), int(y - sp.height / 2)))
        else:
            al = 1.0 if t < dur - 0.24 else 1 - ease((t - (dur - 0.24)) / 0.24)
            fr.alpha_composite(O.with_alpha(sp, al) if al < 1 else sp, (int(x), int(y - sp.height / 2)))
        return fr
    return fn, n


def _round_outline(size, rect, r, frac, width=4, color=GOLD, glow=True):
    """an antialiased rounded-rect outline drawn on to frac (clockwise from the top-left), with a soft glow"""
    ss = 3; w, h = size; lay = Image.new("RGBA", (w * ss, h * ss), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    x0, y0, x1, y1 = [v * ss for v in rect]; rr = r * ss
    pts = []
    def arc(cx, cy, a0, a1):
        for k in range(9): a = math.radians(a0 + (a1 - a0) * k / 8); pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
    arc(x0 + rr, y0 + rr, 180, 270); arc(x1 - rr, y0 + rr, 270, 360); arc(x1 - rr, y1 - rr, 0, 90); arc(x0 + rr, y1 - rr, 90, 180); pts.append(pts[0])
    L = [0.0]
    for a, b in zip(pts, pts[1:]): L.append(L[-1] + math.dist(a, b))
    stop = L[-1] * clamp(frac); seg = [pts[0]]
    for k in range(1, len(pts)):
        if L[k] <= stop: seg.append(pts[k])
        else:
            a, b = pts[k - 1], pts[k]; q = (stop - L[k - 1]) / max(1e-6, L[k] - L[k - 1]); seg.append((a[0] + (b[0] - a[0]) * q, a[1] + (b[1] - a[1]) * q)); break
    if len(seg) > 1: d.line(seg, fill=color + (255,), width=width * ss, joint="curve")
    lay = lay.resize((w, h), Image.LANCZOS)
    if glow:
        gl = lay.filter(ImageFilter.GaussianBlur(7)); out = Image.new("RGBA", (w, h), (0, 0, 0, 0)); out.alpha_composite(O.with_alpha(gl, 0.9)); out.alpha_composite(lay); return out
    return lay


def k_ring(plan, seq, g):
    dur = g["t1"] - g["t0"]; n = int(round(dur * FPS)); pad = g.get("pad", 10); da = g.get("draw_at", 0.0)
    cnt = g.get("count")

    def fn(i):
        t = i / FPS; fr = blank(); ta = g["t0"] + t
        b = O.box_at(plan, g["box"], ta, pad)
        if b is None: return fr
        out_a = 1.0 if t < dur - 0.24 else 1 - ease((t - (dur - 0.24)) / 0.24)
        frac = ease((t - da) / 0.42) if t >= da else 0.0
        if frac > 0:
            x0, y0, x1, y1 = b; m = 30
            ol = _round_outline((int(x1 - x0) + 2 * m, int(y1 - y0) + 2 * m), (m, m, m + x1 - x0, m + y1 - y0), g.get("r", 16), frac)
            if out_a < 1: ol = O.with_alpha(ol, out_a)
            fr.alpha_composite(ol, (int(x0 - m), int(y0 - m)))
            fr.paste(Image.new("RGBA", (W, PANEL[1]), (0, 0, 0, 0)), (0, 0))       # never above the panel
            fr.paste(Image.new("RGBA", (W, H - PANEL[3]), (0, 0, 0, 0)), (0, PANEL[3]))
        if g.get("chip") and t >= da + 0.25:
            u = t - da - 0.25; txt = g["chip"]
            if cnt:
                q = ease(clamp(u / cnt[2])); txt = txt.replace("{n}", fmt_count(cnt[0] * q, cnt[1]))
            sp = shadowed(pill(txt, g.get("chip_size", 42)), 12, 130, 5)
            al, bl, sc = focus(u, dur - da - 0.25, 0.30, 0.24)
            x0, y0, x1, y1 = b; cx = clamp((x0 + x1) / 2, sp.width / 2 + 30, W - sp.width / 2 - 30)
            cy = y0 - sp.height / 2 - 14 if g.get("chip_at", "above") == "above" else y1 + sp.height / 2 + 14
            cy = clamp(cy, 200 + sp.height / 2, 990 - sp.height / 2)
            place(fr, sp, cx, cy, al=al * out_a, blur=bl, scale=sc)
        return fr
    return fn, n


def k_sweep(plan, seq, g):
    dur = g["t1"] - g["t0"]; n = int(round(dur * FPS)); step = g.get("every", 0.08)

    def fn(i):
        t = i / FPS; fr = blank(); ta = g["t0"] + t; d = ImageDraw.Draw(fr)
        out_a = 1.0 if t < dur - 0.24 else 1 - ease((t - (dur - 0.24)) / 0.24)
        for k, bx in enumerate(g["boxes"]):
            b = O.box_at(plan, bx, ta, 0)
            if b is None: continue
            p = ease((t - k * step) / 0.30) if t >= k * step else 0
            if p <= 0: continue
            x0, y0, x1, y1 = b; y = y1 + 6
            lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ImageDraw.Draw(lay).rounded_rectangle((x0, y, x0 + (x1 - x0) * p, y + 5), 2, fill=GOLD + (int(255 * out_a),))
            fr.alpha_composite(lay.filter(ImageFilter.GaussianBlur(5))); fr.alpha_composite(lay)
        fr.paste(Image.new("RGBA", (W, PANEL[1]), (0, 0, 0, 0)), (0, 0)); fr.paste(Image.new("RGBA", (W, H - PANEL[3]), (0, 0, 0, 0)), (0, PANEL[3]))
        if g.get("chip"):
            u = t - g.get("chip_at", 0.6)
            if u >= 0:
                sp = shadowed(pill(g["chip"], 44), 12, 130, 5); al, bl, sc = focus(u, dur - g.get("chip_at", 0.6), 0.30, 0.24)
                place(fr, sp, g["chip_xy"][0], g["chip_xy"][1], al=al, blur=bl, scale=sc)
        return fr
    return fn, n


def _obs_frame(plan, seq, obs_t, box):
    key = ("obs", obs_t, tuple(box))
    if key not in _C:
        import subprocess
        raw =subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{obs_t:.3f}", "-i", plan["obs_file"], "-frames:v", "1", "-f", "rawvideo", "-pix_fmt", "rgb24", "-"],
                             capture_output=True).stdout
        im = Image.frombytes("RGB", (2560, 1440), raw).crop(tuple(box)).convert("RGBA"); _C[key] = im
    return _C[key]


def k_still_card(plan, seq, g):
    dur = g["t1"] - g["t0"]; n = int(round(dur * FPS))
    src = _obs_frame(plan, seq, g["obs_t"], g["box"]); s = g["w"] / src.width
    card = src.resize((int(src.width * s), int(src.height * s)), Image.LANCZOS)
    m = O.rounded_mask(card.size, (0, 0, card.width, card.height), 22); card.putalpha(m)
    pad = 40; full = Image.new("RGBA", (card.width + 2 * pad, card.height + 2 * pad), (0, 0, 0, 0)); full.alpha_composite(card, (pad, pad))
    full.alpha_composite(O.card_dressing(full.size, (pad, pad, pad + card.width, pad + card.height), 22))
    rx0, ry0, rx1, ry1 = g["ring"]; bx, by = g["box"][0], g["box"][1]
    rr = (pad + (rx0 - bx) * s, pad + (ry0 - by) * s, pad + (rx1 - bx) * s, pad + (ry1 - by) * s)
    tag = shadowed(pill(g["tag"], 42), 12, 130, 5) if g.get("tag") else None
    badge = shadowed(pill(g["badge"], 46, dot=False, fill=GOLD + (255,), hair=(255, 255, 255, 0), color=(12, 12, 12, 255)), 10, 120, 4) if g.get("badge") else None

    def fn(i):
        t = i / FPS; fr = blank(); al, bl, sc = focus(t, dur)
        im = full.copy()
        if t >= g["ring_at"] - g["t0"]:
            q = ease((t - (g["ring_at"] - g["t0"])) / 0.42)
            m2 = 30; ol = _round_outline((int(rr[2] - rr[0]) + 2 * m2, int(rr[3] - rr[1]) + 2 * m2), (m2, m2, m2 + rr[2] - rr[0], m2 + rr[3] - rr[1]), 14, q, width=5)
            im.alpha_composite(ol, (int(rr[0] - m2), int(rr[1] - m2)))
            if badge and q >= 0.6:
                u = (t - (g["ring_at"] - g["t0"]) - 0.25) / 0.25; bsp = badge.resize((max(1, int(badge.width * (0.6 + 0.4 * ease(clamp(u))))), max(1, int(badge.height * (0.6 + 0.4 * ease(clamp(u)))))), Image.LANCZOS)
                im.alpha_composite(O.with_alpha(bsp, clamp(u * 2)), (int(rr[0] + 18), int(rr[1] - bsp.height / 2)))
        place(fr, im, g["cx"], g["cy"], al=al, blur=bl, scale=sc, dy=26 * (1 - ease(clamp(t / 0.38))))
        if tag:
            a2, b2, s2 = focus(t - 0.15, dur - 0.15, 0.32, 0.24) if t >= 0.15 else (0, 0, 1)
            place(fr, tag, W / 2, g.get("tag_y", 236), al=a2, blur=b2, scale=s2)
        return fr
    return fn, n


def k_bars(plan, seq, g):
    dur = g["t1"] - g["t0"]; n = int(round(dur * FPS))
    X0, X1, BASE, HMAX = g.get("x0", 90), g.get("x1", 990), g.get("base", 880), g.get("hmax", 520)
    data = g["data"]; N = len(data); gap = g.get("gap", 12); bw = (X1 - X0 - gap * (N - 1)) / N
    vmax = g.get("vmax") or max(d["v"] for d in data)
    tl = g.get("titles") or [[g["t0"], g["title"]]]
    titles = [(tt - g["t0"], shadowed(rich_line(txt, F(BEBAS, g.get("title_size", 64))), 10, 140, 4)) for tt, txt in tl]
    fl, fs = F(BEBAS, g.get("label_size", 46)), F(BEBAS, g.get("sub_size", 30))
    col = {"other": (120, 120, 124), "white": (238, 238, 238), "gold": GOLD, "dim": (70, 70, 74)}

    def fn(i):
        t = i / FPS; ta = g["t0"] + t; lay = blank(); d = ImageDraw.Draw(lay)
        out_a = 1.0 if t < dur - 0.24 else 1 - ease((t - (dur - 0.24)) / 0.24)
        k = max([j for j, (tt, _) in enumerate(titles) if tt <= t + 1e-6] or [0])
        for j in (k - 1, k):
            if j < 0: continue
            tt, sp = titles[j]
            if j == k: a, bl, sc = focus(t - tt, 99, 0.38, 0)
            else:
                u = t - titles[k][0]
                if u >= 0.22: continue
                a, bl, sc = 1 - ease(u / 0.22), 6 * ease(u / 0.22), 1.0
            place(lay, sp, W / 2, g.get("title_y", 262), al=a, blur=bl, scale=sc)
        d.line([(X0 - 10, BASE + 2), (X1 + 10, BASE + 2)], fill=(255, 255, 255, 60), width=2)
        tops = []
        for k, b in enumerate(data):
            p = ease(clamp((ta - b["at"]) / b.get("rise", 0.55)))
            h = max(3.0, b["v"] / vmax * HMAX) * p if p > 0 else 0
            x = X0 + k * (bw + gap); c = col[b.get("style", "other")]
            if h > 0:
                bar = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ImageDraw.Draw(bar).rounded_rectangle((x, BASE - h, x + bw, BASE), min(6, bw / 2, max(1, h / 2)), fill=c + (255,))
                if b.get("style") == "gold":
                    lay.alpha_composite(O.with_alpha(bar.filter(ImageFilter.GaussianBlur(16)), 0.55))
                lay.alpha_composite(bar)
            tops.append((x + bw / 2, BASE - h, p))
            if b.get("label") and p > 0.15:
                txt = b["label"]
                if b.get("count"):
                    v, suf = b["count"]; txt = txt.replace("{n}", fmt_count(v * p, suf))
                sp = rich_line(txt, fl, fill=(c + (255,)) if b.get("style") != "other" else WHITE)
                place(lay, sp, clamp(x + bw / 2 + b.get("label_dx", 0), sp.width / 2 + 20, W - sp.width / 2 - 20), BASE - h - 34, al=clamp((p - 0.15) / 0.3))
            if b.get("sub") and p > 0.5:
                sp = rich_line(b["sub"], fs, fill=(255, 255, 255, 170)); place(lay, sp, clamp(x + bw / 2, sp.width / 2 + 20, W - sp.width / 2 - 20), BASE + 30, al=clamp((p - 0.5) / 0.3))
        if g.get("group"):
            i0, i1, txt = g["group"]; p = clamp((ta - data[i1]["at"] - 0.2) / 0.3)
            if p > 0:
                xa, xb = X0 + i0 * (bw + gap), X0 + i1 * (bw + gap) + bw; y = BASE + 22
                d.line([(xa, y), (xa, y + 12), (xb, y + 12), (xb, y)], fill=(255, 255, 255, int(150 * p)), width=2)
                sp = rich_line(txt, F(BEBAS, 34), fill=(255, 255, 255, 210)); place(lay, sp, clamp((xa + xb) / 2, sp.width / 2 + 24, W - sp.width / 2 - 24), y + 44, al=p)
        if g.get("pin"):
            pn = g["pin"]; u = ta - pn["at"]
            if u >= 0:
                gx, gy, _ = tops[max(k for k, b in enumerate(data) if b.get("style") == "gold")]
                al, bl2, sc2 = focus(u, 99, 0.32, 0)
                sp = shadowed(pill(pn["text"], 38), 10, 130, 4); px_ = clamp(gx - sp.width / 2 - 40, sp.width / 2 + 24, W - sp.width / 2 - 24)
                py = gy + pn.get("dy", 90)
                d2 = ImageDraw.Draw(lay); d2.line([(px_ + sp.width / 2 - 6, py), (gx - bw / 2 - 4, py)], fill=GOLD + (int(220 * al),), width=2)
                place(lay, sp, px_, py, al=al, blur=bl2, scale=sc2)
                if pn.get("sub") and u >= pn.get("sub_after", 0.6):
                    s2 = rich_line(pn["sub"], F(BEBAS, 32), fill=(255, 255, 255, 200)); place(lay, s2, px_, py + 46, al=clamp((u - pn.get("sub_after", 0.6)) / 0.3))
        if g.get("stamp"):
            stp = g["stamp"]; u = ta - stp["at"]
            if u >= 0:
                sp = shadowed(rich_line(stp["text"], AF(stp.get("size", 120)), fa=AF(stp.get("size", 120)), fill=GOLD + (255,)), 16, 150, 6)
                q = ease(clamp(u / 0.30)); place(lay, sp, stp.get("x", 380), stp.get("y", 560), al=q, blur=8 * (1 - q), scale=1.18 - 0.18 * q)
        if g.get("push"):
            z = 1 + (g["push"] - 1) * eio(t / dur)
            if z > 1.0005:
                big = lay.resize((int(W * z), int(H * z)), Image.LANCZOS); cx, cy = W / 2, (PANEL[1] + PANEL[3]) / 2
                lay = blank(); lay.alpha_composite(big.crop((int(cx * z - cx), int(cy * z - cy), int(cx * z - cx) + W, int(cy * z - cy) + H)))
                lay.paste(Image.new("RGBA", (W, PANEL[1]), (0, 0, 0, 0)), (0, 0)); lay.paste(Image.new("RGBA", (W, H - PANEL[3]), (0, 0, 0, 0)), (0, PANEL[3]))
        return O.with_alpha(lay, out_a) if out_a < 1 else lay
    return fn, n


def k_grid(plan, seq, g):
    dur = g["t1"] - g["t0"]; n = int(round(dur * FPS))
    cols, rows = 5, 4; tw = th = g.get("tile", 150); gx = gy = g.get("tgap", 26)
    X0 = (W - (cols * tw + (cols - 1) * gx)) / 2; Y0 = g.get("y0", 360)
    gold = set(g.get("gold", []))
    titles = [(tt - g["t0"], shadowed(rich_line(txt, F(BEBAS, 64)), 10, 140, 4)) for tt, txt in g["titles"]]
    q_mark = rich_line("?", F(BEBAS, 84), fill=(18, 18, 18, 255))      # on the lit (white) tiles
    play = Image.new("RGBA", (40, 40), (0, 0, 0, 0)); ImageDraw.Draw(play).polygon([(12, 8), (32, 20), (12, 32)], fill=(255, 255, 255, 120))

    def tile(style, a):
        key = ("tile", style)
        if key not in _C:
            if style == "gold": fill, hair = GOLD + (255,), (255, 240, 200, 140)
            elif style == "lit": fill, hair = (232, 232, 232, 255), (255, 255, 255, 90)
            elif style == "dim": fill, hair = (34, 34, 36, 255), (255, 255, 255, 26)
            else: fill, hair = (52, 52, 56, 255), (255, 255, 255, 50)
            im = O.rrect((tw, th), 18, fill, outline=hair, width=2)
            pc = play.copy()
            if style in ("gold", "lit"): pc = Image.new("RGBA", (40, 40), (0, 0, 0, 0)); ImageDraw.Draw(pc).polygon([(12, 8), (32, 20), (12, 32)], fill=(20, 20, 20, 160))
            if not (style == "lit" and g.get("ask_at")): im.alpha_composite(pc, (tw // 2 - 20, th // 2 - 20))
            _C[key] = im
        return O.with_alpha(_C[key], a) if a < 1 else _C[key]

    def fn(i):
        t = i / FPS; ta = g["t0"] + t; lay = blank()
        out_a = 1.0 if t < dur - 0.24 else 1 - ease((t - (dur - 0.24)) / 0.24)
        k = max([j for j, (tt, _) in enumerate(titles) if tt <= t + 1e-6] or [0])
        for j in (k - 1, k):
            if j < 0: continue
            tt, sp = titles[j]
            if j == k:
                u = t - tt; al, bl, sc = focus(u, 99, 0.32, 0) if (j > 0 or g.get("title_focus", True)) else (1, 0, 1)
            else:
                u = t - titles[k][0]
                if u >= 0.22: continue
                al, bl, sc = 1 - ease(u / 0.22), 6 * ease(u / 0.22), 1.0
            place(lay, sp, W / 2, g.get("title_y", 262), al=al, blur=bl, scale=sc)
        for idx in range(cols * rows):
            r_, c_ = divmod(idx, cols); x = X0 + c_ * (tw + gx); y = Y0 + r_ * (th + gy)
            if g.get("stamp_every"):
                at = g["tiles_at"] + idx * g["stamp_every"]
            else:
                at = g["tiles_at"] + (r_ + c_) * 0.035
            p = ease(clamp((ta - at) / 0.30))
            if p <= 0: continue
            style, a, dy = "base", p, 22 * (1 - p)
            if g.get("extract_at") and ta >= g["extract_at"]: style = "lit"
            if g.get("gold_at") and ta >= g["gold_at"] + (sorted(gold).index(idx) * 0.06 if idx in gold else 0):
                if idx in gold: style = "gold"
                else: style = "dim"
            if g.get("waste_at") and idx not in gold and ta >= g["waste_at"]:
                q = ease(clamp((ta - g["waste_at"] - (idx % 5) * 0.03) / 0.45)); style = "dim"; a *= 1 - 0.75 * q; dy += 30 * q
            sp = tile(style, a)
            if style == "gold":
                gl = O.with_alpha(sp.filter(ImageFilter.GaussianBlur(14)), 0.6); lay.alpha_composite(gl, (int(x), int(y + dy)))
            lay.alpha_composite(sp, (int(x), int(y + dy)))
            if g.get("ask_at") and ta >= g["ask_at"] and not (g.get("waste_at") and ta >= g["waste_at"]):
                q = ease(clamp((ta - g["ask_at"] - idx * 0.02) / 0.25))
                if q > 0: place(lay, q_mark, x + tw / 2, y + th / 2 + dy, al=q * a, scale=0.85 + 0.15 * q)
        if g.get("count_chip"):
            cc = g["count_chip"]; u = ta - cc[0]
            if u >= 0:
                sp = shadowed(pill(cc[1], 44), 12, 130, 5); al, bl, sc = focus(u, 99, 0.30, 0)
                place(lay, sp, W / 2, Y0 + rows * (th + gy) + 30, al=al, blur=bl, scale=sc)
        return O.with_alpha(lay, out_a) if out_a < 1 else lay
    return fn, n


def k_stage_title(plan, seq, g):
    dur = g["t1"] - g["t0"]; n = int(round(dur * FPS))
    phases = g.get("phases") or [[g["t0"], g.get("label"), g["lines"]]]
    built = []
    for tt, lab, lines in phases:
        fb = F(BEBAS, g.get("size", 132)); sps = [shadowed(rich_line(L, fb), 14, 150, 6) for L in lines]
        lsp = shadowed(rich_line(lab, F(BEBAS, 46), fill=(255, 255, 255, 190)), 8, 120, 3) if lab else None
        built.append((tt - g["t0"], lsp, sps))
    y = g.get("y", 560)

    def fn(i):
        t = i / FPS; fr = blank()
        out_a = 1.0 if t < dur - 0.24 else 1 - ease((t - (dur - 0.24)) / 0.24)
        k = max(j for j, b in enumerate(built) if b[0] <= t + 1e-6)
        for j in (k - 1, k):
            if j < 0: continue
            tt, lsp, sps = built[j]
            if j == k: al, bl, sc = focus(t - tt, 99, 0.38, 0)
            else:
                u = t - built[k][0]
                if u >= 0.22: continue
                al, bl, sc = 1 - ease(u / 0.22), 6 * ease(u / 0.22), 1.0
            al *= out_a
            hs = sum(s.height - 28 for s in sps); yy = y - hs / 2
            if lsp: place(fr, lsp, W / 2, yy - 40, al=al, blur=bl, scale=sc)
            for s in sps:
                place(fr, s, W / 2, yy + (s.height - 28) / 2, al=al, blur=bl, scale=sc); yy += s.height - 28
        return fr
    return fn, n


def k_low_title(plan, seq, g):
    dur = g["t1"] - g["t0"]; n = int(round(dur * FPS))
    fb = F(BEBAS, g.get("size", 92)); sps = [rich_line(L, fb) for L in g["lines"]]
    w = max(s.width for s in sps) + 80; h = sum(s.height - 16 for s in sps) + 50
    card = O.card_body((int(w), int(h)), 28, (10, 10, 10, 200), outline=(255, 255, 255, 34), width=2)
    yy = 25
    for s in sps: card.alpha_composite(s, (int(w / 2 - s.width / 2), int(yy - 8))); yy += s.height - 16
    card = shadowed(card, 18, 130, 8)

    def fn(i):
        t = i / FPS; fr = blank(); al, bl, sc = focus(t, dur)
        place(fr, card, W / 2, g.get("y", 1440), al=al, blur=bl, scale=sc); return fr
    return fn, n


NEW = {"hook_big": k_hook_big, "era": k_era, "ring": k_ring, "sweep": k_sweep, "still_card": k_still_card, "bars": k_bars,
       "grid": k_grid, "stage_title": k_stage_title, "low_title": k_low_title}
_orig_frame_fn = O._frame_fn


def _frame_fn(plan, seq, g):
    if g["kind"] in NEW:
        fn, n = NEW[g["kind"]](plan, seq, g)
        return with_stage(g, fn), n
    fn, n = _orig_frame_fn(plan, seq, g)
    return with_stage(g, fn), n


O._frame_fn = _frame_fn
O.PANEL_KINDS = set(O.PANEL_KINDS) | {"bars", "grid", "still_card", "stage_title"}


def stage_check(plan, seq, out=print):
    """the safe-zone rule for STAGED scenes (exempt above: their backdrop is the panel itself, background by design): every staged
    graphic is sampled WITHOUT its backdrop at 30 / 55 / 80 % and its content must sit inside y 200..1620 (alpha >= 25 %)."""
    errs = []
    for g in plan["graphics"]:
        if not g.get("stage"): continue
        h = {k: v for k, v in g.items() if k != "stage"}; fn, n = O._frame_fn(plan, seq, h)
        for f in (0.30, 0.55, 0.80):
            bb = O._alpha_bbox(fn(min(n - 1, int(n * f))))
            if bb and (bb[1] < 200 or bb[3] > 1620): errs.append(f"{g['id']} content y {bb[1]}..{bb[3]} at {f:.0%}"); break
    for e in errs: out(f"  ERROR    {e}")
    out(f"stage_check: {len(errs)} error(s) on {sum(1 for g in plan['graphics'] if g.get('stage'))} staged scenes")
    return errs


# ---------- captions: one gold emphasis word ----------
_orig_chunks = O.caption_chunks


def caption_chunks(plan):
    ch = _orig_chunks(plan)
    for t, word in plan.get("caption_emph", []):
        c = next((c for c in ch if c["t0"] - 0.08 <= t < c["t1"]), None)
        if c is None: print(f"  caption_emph {t} {word}: no chunk"); continue
        toks = c["text"].split(" ")
        hit = next((k for k, x in enumerate(toks) if x.strip("!?\"'") == word.upper()), None)
        if hit is None: print(f"  caption_emph {t} {word}: not in {c['text']!r}"); continue
        toks[hit] = "^" + toks[hit]; c["text"] = " ".join(toks)
    return ch


def caption_png(text, size=96):
    if "^" not in text: return _orig_png(text, size)
    f = O.ImageFont.truetype(BEBAS, size); im = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    plain = text.replace("^", "")
    l, t, r, b = d.textbbox((0, 0), plain, font=f, stroke_width=5)
    x, y = (W - (r - l)) / 2 - l, O.SEAM - (b - t) / 2 - t
    sh = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(sh).text((x, y + 4), plain, font=f, fill=(0, 0, 0, 150), stroke_width=7, stroke_fill=(0, 0, 0, 150))
    im = Image.alpha_composite(im, sh.filter(ImageFilter.GaussianBlur(6))); d = ImageDraw.Draw(im)
    cx = x
    for k, tok in enumerate(text.split(" ")):
        em = tok.startswith("^"); s = tok.lstrip("^") + (" " if k < len(text.split(" ")) - 1 else "")
        d.text((cx, y), s, font=f, fill=(GOLD + (255,)) if em else (255, 255, 255, 255), stroke_width=5, stroke_fill=(0, 0, 0, 255))
        cx += d.textlength(s, font=f)
    return im


_orig_png = O.caption_png
O.caption_chunks = caption_chunks
O.caption_png = caption_png
_orig_clean = O.clean
O.clean = lambda s: _orig_clean(s.replace("^", "")) if isinstance(s, str) else _orig_clean(s)


if __name__ == "__main__":
    a = sys.argv[1:]
    plan, seq = O.load(a[0])
    if "--captions" in a: O.build_captions(plan)
    if "--mg" in a: O.build_mg(plan, seq, a[a.index("--only") + 1] if "--only" in a else None)
    if "--check" in a:
        e_, _ = O.check(plan, seq); e2 = stage_check(plan, seq)
        if e_ or e2: sys.exit(1)
    if "--still" in a:
        ts = [float(x) for x in a[a.index("--still") + 1:] if not x.startswith("--")]
        import preview

        def fast_still(t):          # O.still with random-access frames (O.still runs every frame from t0 up to t)
            base = preview.render(plan, seq, t).convert("RGBA")
            for g in plan["graphics"]:
                if not (g["t0"] <= t < g["t1"]): continue
                items = g["items"] if g["kind"] == "group" else [g]
                for it in items:
                    if it["t0"] <= t < it["t1"]:
                        fn, _ = O._frame_fn(plan, seq, it); base.alpha_composite(fn(int((t - it["t0"]) * FPS)))
            if plan.get("seam_line") and not O.G.face_at(plan, t):
                q = O.seam_frac(plan, t); base.alpha_composite(O.seam_line_png(4) if q >= 1 else O.seam_line_png(4, q))
            cj = os.path.join(plan["_dir"], "overlays", "captions.json")
            if os.path.exists(cj):
                for c in json.load(open(cj, encoding="utf-8")):
                    if c["t0"] <= t < c["t1"]: base.alpha_composite(O.caption_png(c["text"]))
            return base.convert("RGB")
        ims = [fast_still(t) for t in ts]
        w, h = 432, 768
        sheet = Image.new("RGB", (w * min(5, len(ims)), h * ((len(ims) + 4) // 5)))
        for i, im in enumerate(ims): sheet.paste(im.resize((w, h), Image.LANCZOS), ((i % 5) * w, (i // 5) * h))
        p = os.path.join(plan["_dir"], "work", "stills.jpg"); sheet.save(p, quality=88); print(p)
