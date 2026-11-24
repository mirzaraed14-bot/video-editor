"""kindsmenu.py: the FIXED MENU kinds of the Onyx reaction kit (from batch 7/9 kindsotn), patched in over kinds7 (-> mgx6 -> mgx -> overlays) at import.
  Menu items -> kinds: channel card=otn_hook, credential cards=cred_chips, play card=play_card (kinds7), theirs-vs-ours=twin_cards, number cards=pair_count/scorecard(big), pointer marks=pointer_tag/page_marks, title_strip.

  otn_hook       beat 1: the channel tag (avatar, name, @handle . subs, Subscribe pill), frame 0 = the finished card; a gold underline sweeps under "On That Note"
  cred_chips     beat 3: chips [[t_abs, text], ...] in the low band, a gold rule under them at rule_at + a rising label
  title_strip    beat 5: the FULL title of their Short on a dark card at the panel top, the part the player cuts off in grey behind a dashed boundary
  pointer_tag    beat 5: a tag + leader docked to a SCREEN point (source px)
  pair_count     beat 7: "1:27 THEIR SHORT" counts up, "0:43 OUR EDIT" rises, chips under them
  bar_to_short   beat 8: THE FULL EPISODE bar -> three gold segments lift out -> a 9:16 outline THE SHORT
  anatomy        beat 9 (hero): a 9:16 outline in three bands HOOK / MIDDLE / PAYOFF, thread, arc, tangents snipped
  twin_cards     beats 12 + 16: two 9:16 stills side by side, labels, a gold "=" or a lift
  badge_card     beat 17: a low card with an avatar badge, two lines in turn
  letter_card    envelope card, flap folds, gold seal (not on the MENU)
Times: *_at keys are seconds after t0 (kinds7 convention); lists marked t_abs are sequence seconds.
"""
import io, math, os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import kinds7 as K                                   # noqa: E402
M6, X, O = K.M6, K.X, K.O
G = O.G
from PIL import Image, ImageDraw, ImageFilter       # noqa: E402

W, H, FPS, GOLD = O.W, O.H, O.FPS_MG, O.GOLD
WHITE = (255, 255, 255, 255); GREY = (154, 154, 154, 255); MARK = (242, 193, 78, 255)
BEBAS, INTER_B, INTER_R = O.BEBAS, O.INTER_B, O.INTER_R
F, blank, shadowed, rich_line, pill, place, focus = X.F, X.blank, X.shadowed, X.rich_line, X.pill, X.place, X.focus
e_q5 = K.e_q5; e_c3 = K.e_c3; e_io3 = K.e_io3
INTER_SB = K.INTER_SB
_C = {}


def c01(x): return max(0.0, min(1.0, x))


def out_alpha(t, dur, d=0.24): return 1.0 if t < dur - d else 1 - e_io3((t - (dur - d)) / d)


def enter(g, sprite, cx, cy, t, dur):
    """the sprite on frame t under the reaction's entrance signature (foldx), shadow included"""
    return O.pop_frame(sprite, cx, cy, t, dur, ent=g.get("entrance") or O.ENTRANCE)


def src2frame(plan, view, sx, sy):
    """a point of the OBS screen (source px) -> frame px under a named static view"""
    v = plan["views_named"][view]; B = v.get("box") or plan.get("box") or list(G.BOX)
    s = G.BASE * v["z"]; return (B[0] + B[2]) / 2 + (sx - v["cx"]) * s, (B[1] + B[3]) / 2 + (sy - v["cy"]) * s


def still(path, t, size=None):
    k = ("s", path, round(t, 3), size)
    if k not in _C:
        r = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{t:.3f}", "-i", path, "-frames:v", "1", "-f", "image2pipe", "-vcodec", "png", "-"], capture_output=True)
        im = Image.open(io.BytesIO(r.stdout)).convert("RGBA")
        if size: im = im.resize(size, Image.LANCZOS)
        _C[k] = im
    return _C[k]


def rounded(im, r):
    m = O.rounded_mask(im.size, (0, 0, im.width, im.height), r); im = im.copy(); im.putalpha(m); return im


def avatar(path, d):
    im = Image.open(path).convert("RGB"); s = min(im.size)
    im = im.crop(((im.width - s) // 2, (im.height - s) // 2, (im.width + s) // 2, (im.height + s) // 2)).resize((d * 2, d * 2), Image.LANCZOS)
    m = Image.new("L", (d * 2, d * 2), 0); ImageDraw.Draw(m).ellipse((0, 0, d * 2 - 1, d * 2 - 1), fill=255)
    o = Image.new("RGBA", (d * 2, d * 2), (0, 0, 0, 0)); o.paste(im, (0, 0), m); return o.resize((d, d), Image.LANCZOS)


def tw(text, font): return ImageDraw.Draw(Image.new("RGBA", (1, 1))).textlength(text, font=font)


def rise_in(fr, sp, cx, cy, u, d=0.34, dy=18, al=1.0):
    """type-safe entrance: rises dy px behind its own alpha (no pop)"""
    p = e_q5(u / d)
    if p <= 0: return
    place(fr, sp, cx, cy, al=min(1.0, u / (d * 0.6)) * al, dy=dy * (1 - p))


def card_dark(w, h, r=26, a=238): return O.card_body((int(w), int(h)), r, (14, 14, 16, a), outline=(255, 255, 255, 40), width=2)


# ------------------------------------------------------------------ otn_hook
def _frame0(sprite, cx, cy, t, dur):
    """frame 0 = the finished card (REACTIONS-V2 rule 8: the channel tag IS the hook); leaves with the foldx exit"""
    if t > dur - 0.3: return O.pop_frame(sprite, cx, cy, t, dur, ent="foldx")
    fr = blank(); sh, pad = O.soft_shadow(sprite, blur=22, alpha=120, dy=10)
    fr.alpha_composite(sh, (int(cx - sh.width / 2), int(cy - sh.height / 2))); return fr


def k_otn_hook(plan, seq, g):
    """fix shift R8 (2026-11-09): the @handle and the subscriber count are TWO sub-lines in Inter 42 (cap height 30.5 px on the 1080 frame), the name line unchanged"""
    dur = g["t1"] - g["t0"]; n = int(round(dur * FPS)); w, h = 1040, 214
    card = O.card_body((w, h), 42, (16, 16, 16, 238), outline=(255, 255, 255, 38), width=2)
    card.alpha_composite(avatar(os.path.join(plan["_dir"], g["avatar"]), 130), (28, (h - 130) // 2))
    d = ImageDraw.Draw(card); fn, fs = F(INTER_B, 48), F(INTER_R, 42); x = 28 + 130 + 26
    name = g["name"]; d.text((x, 20), name, font=fn, fill=WHITE)
    d.text((x, 80), g["handle"], font=fs, fill=(190, 190, 190, 255)); d.text((x, 130), g["subs"], font=fs, fill=(190, 190, 190, 255))
    pl = O.rrect((150, 56), 28, WHITE); ImageDraw.Draw(pl).text((75, 28), "Subscribe", font=F(INTER_B, 40), fill=(15, 15, 15, 255), anchor="mm")
    card.alpha_composite(pl, (w - 26 - 150, (h - 56) // 2))
    sw = g.get("sweep", g["name"]); i0 = name.index(sw); xa = x + tw(name[:i0], fn); xb = x + tw(name[:i0 + len(sw)], fn)
    cx, cy = W / 2, g.get("y", 1420)
    assert x + tw(g["handle"], fs) < w - 26 - 150 - 16, "handle runs into the Subscribe pill"

    def f(i):
        t = i / FPS; c = card
        if g.get("sweep_at") is not None and t >= g["sweep_at"]:
            q = e_c3((t - g["sweep_at"]) / g.get("sweep_dur", 0.8)); c = card.copy()
            ImageDraw.Draw(c).rounded_rectangle((xa, 64, xa + (xb - xa) * q, 69), 3, fill=MARK)
        return _frame0(c, cx, cy, t, dur)
    return f, n


# ------------------------------------------------------------------ cred_chips
def k_cred_chips(plan, seq, g):
    dur = g["t1"] - g["t0"]; n = int(round(dur * FPS)); gap = 20
    chips = [(ta - g["t0"], shadowed(pill(txt, 50), 12, 130, 5)) for ta, txt in g["chips"]]
    lab = shadowed(rich_line(g["label"], F(BEBAS, 84)), 12, 140, 5); y0 = g.get("y", 1370)

    def f(i):
        t = i / FPS; fr = blank(); oa = out_alpha(t, dur)
        shown = [(tt, c) for tt, c in chips if t >= tt]
        rows, cur, cw = [], [], 0
        for tt, c in shown:
            if cur and cw + c.width + gap > 980: rows.append(cur); cur, cw = [], 0
            cur.append((tt, c)); cw += c.width + gap
        if cur: rows.append(cur)
        ybot = y0
        for r_, row in enumerate(rows):
            wr = sum(c.width for _, c in row) + gap * (len(row) - 1); x = W / 2 - wr / 2; yy = y0 + r_ * 92
            for tt, c in row:
                u = t - tt; p = e_q5(u / 0.3)
                place(fr, c, x + c.width / 2, yy + 16 * (1 - p), al=min(1.0, u / 0.15) * oa); x += c.width + gap
            ybot = yy
        if g.get("rule_at") is not None and t >= g["rule_at"]:
            q = e_c3((t - g["rule_at"]) / 0.4); yr = ybot + 62; half = 330 * q
            ImageDraw.Draw(fr).rounded_rectangle((W / 2 - half, yr, W / 2 + half, yr + 5), 3, fill=MARK[:3] + (int(255 * oa),))
            if t >= g["rule_at"] + 0.12:
                u = t - g["rule_at"] - 0.12; a2, b2, s2 = focus(u, 99, 0.34, 0)
                place(fr, lab, W / 2, yr + 66, al=a2 * oa, blur=b2, scale=s2)
        return fr
    return f, n


# ------------------------------------------------------------------ title_strip
def k_title_strip(plan, seq, g):
    """fix shift R3: no 'WHAT THE VIEWER SEES' header (back to the PLAN's bare strip), Inter SemiBold 32, sits BELOW the (shorter) player panel and above the caption line"""
    dur = g["t1"] - g["t0"]; n = int(round(dur * FPS)); w = 980; fnt = F(INTER_SB, 40); LH = 54
    vis, hid = g["visible"], g["hidden"]; d0 = ImageDraw.Draw(Image.new("RGBA", (1, 1)))
    xb = 34 + d0.textlength(vis + " ", font=fnt); words = hid.split(" "); l1, l2, cur = "", "", ""
    for wd in words:
        t_ = (cur + " " + wd).strip()
        if not l2 and xb + d0.textlength(t_, font=fnt) > w - 34: l1, cur = cur, wd; l2 = "_"
        else: cur = t_
    if l2: l2 = cur
    else: l1 = cur
    y1, y2 = 22, 22 + LH; h = (y2 + LH + 10) if l2 else (y1 + LH + 10)
    base = card_dark(w, h)
    bd = ImageDraw.Draw(base); bd.text((34, y1), vis, font=fnt, fill=WHITE)
    hidl = Image.new("RGBA", (w, h), (0, 0, 0, 0)); hd = ImageDraw.Draw(hidl)
    hd.text((xb, y1), l1, font=fnt, fill=(255, 255, 255, 115))
    if l2: hd.text((34, y2), l2, font=fnt, fill=(255, 255, 255, 115))
    bx = int(xb - 10)
    for yy in range(y1 - 6, y1 + 38, 14): hd.line((bx, yy, bx, yy + 8), fill=MARK[:3] + (230,), width=3)
    cx, cy = W / 2, g.get("y", 880); t_rev = g.get("reveal_at", 0.45)

    def f(i):
        t = i / FPS; fr = blank(); a, b, s = focus(t, dur, 0.34, 0.24); c = base.copy()
        if t >= t_rev:
            u = e_c3((t - t_rev) / 0.45); u2 = e_c3((t - t_rev - 0.3) / 0.45); m = Image.new("L", (w, h), 0); md = ImageDraw.Draw(m)
            md.rectangle((bx - 6, 0, bx - 6 + int((w - bx + 6) * u), y2 - 2 if l2 else h), fill=255)
            if l2: md.rectangle((0, y2 - 2, int(w * u2), h), fill=255)
            part = Image.new("RGBA", (w, h), (0, 0, 0, 0)); part.paste(hidl, (0, 0), m); c.alpha_composite(part)
        place(fr, shadowed(c, 16, 130, 6), cx, cy, al=a, blur=b, scale=s)
        return fr
    return f, n


# ------------------------------------------------------------------ pointer_tag
def k_pointer_tag(plan, seq, g):
    dur = g["t1"] - g["t0"]; n = int(round(dur * FPS)); px, py = src2frame(plan, g["view"], *g["point"])
    rl = rich_line(g["text"], F(BEBAS, 54)); bw, bh = rl.width + 24, rl.height + 8
    box = O.card_body((bw, bh), bh // 2, (12, 12, 12, 238), outline=(255, 255, 255, 60), width=2); box.alpha_composite(rl, (8, 4))
    ty = py - g.get("lift", 110); tx = g.get("tag_x") or min(max(px, bw / 2 + 24), W - bw / 2 - 24)

    def f(i):
        t = i / FPS; fr = blank(); a, b, s = focus(t, dur, 0.32, 0.24); lq = e_c3(t / 0.3); d = ImageDraw.Draw(fr)
        d.line((px, ty + bh / 2, px, ty + bh / 2 + (py - 12 - ty - bh / 2) * lq), fill=MARK[:3] + (int(255 * a),), width=3)
        if lq > 0.95: d.ellipse((px - 7, py - 19, px + 7, py - 5), fill=MARK[:3] + (int(255 * a),))
        place(fr, shadowed(box, 10, 140, 4), tx, ty, al=a, blur=b, scale=s); return fr
    return f, n


# ------------------------------------------------------------------ pair_count
def k_pair_count(plan, seq, g):
    dur = g["t1"] - g["t0"]; n = int(round(dur * FPS)); big = F(BEBAS, 250); ta, tb = g["a_at"], g["b_at"]; cyn = g.get("y", 560)
    la = shadowed(rich_line(g["a_label"], F(BEBAS, 54), fill=GREY), 8, 120, 3); lb = shadowed(rich_line(g["b_label"], F(BEBAS, 54), fill=MARK), 8, 120, 3)
    chips = [(c[0], shadowed(pill(c[1], 46, dot=False) if len(c) < 3 else rich_line(c[1], F(BEBAS, 40), fill=GREY), 10, 130, 4)) for c in g["chips"]]
    xa, xb = 300, 780

    def s2(sec): return f"{int(sec // 60)}:{int(sec % 60):02d}"

    def numsprite(txt, col):
        im = Image.new("RGBA", (int(tw(txt, big)) + 40, 280), (0, 0, 0, 0)); ImageDraw.Draw(im).text((im.width / 2, 140), txt, font=big, fill=col, anchor="mm"); return shadowed(im, 14, 150, 6)

    def f(i):
        t = i / FPS; fr = blank(); oa = out_alpha(t, dur)
        if t >= ta:
            u = t - ta; v = g["a_sec"] * e_c3(u / 0.7); a_, b_, s_ = focus(u, 99, 0.3, 0)
            place(fr, numsprite(s2(v), (235, 235, 238, 255)), xa, cyn, al=a_ * oa, blur=b_, scale=s_)
            if u > 0.15: rise_in(fr, la, xa, cyn + 150, u - 0.15, al=oa)
        if t >= tb:
            u = t - tb; a_, b_, s_ = focus(u, 99, 0.34, 0)
            place(fr, numsprite(g["b_text"], MARK), xb, cyn, al=a_ * oa, blur=b_, scale=s_)
            if u > 0.18: rise_in(fr, lb, xb, cyn + 150, u - 0.18, al=oa)
        shown = [(tt, sp) for tt, sp in chips if t >= tt]
        if shown:
            tot = sum(sp.width for _, sp in shown) + 22 * (len(shown) - 1); x = W / 2 - tot / 2
            for tt, sp in shown:
                u = t - tt; p = e_q5(u / 0.3); place(fr, sp, x + sp.width / 2, cyn + 270 + 14 * (1 - p), al=min(1.0, u / 0.15) * oa); x += sp.width + 22
        return fr
    return f, n


# ------------------------------------------------------------------ bar_to_short
def k_bar_to_short(plan, seq, g):
    dur = g["t1"] - g["t0"]; n = int(round(dur * FPS)); X0, X1, Y = 90, 990, g.get("y", 470); BH = 78
    segs = g["segments"]; t_seg = g["seg_at"]; t_rest = g["rest_at"]; t_lift = g["lift_at"]
    lab_full = shadowed(rich_line(g.get("label", "THE FULL EPISODE"), F(BEBAS, 60), fill=GREY), 8, 120, 3)
    lab_rest = shadowed(rich_line(g["rest_label"], F(BEBAS, 62)), 10, 140, 4); lab_short = shadowed(rich_line("THE SHORT", F(BEBAS, 70), fill=MARK), 10, 140, 4)
    OW, OHt = 240, 427; ox, oy = W / 2 - 60, g.get("oy", 800)

    def f(i):
        t = i / FPS; fr = blank(); oa = out_alpha(t, dur); lay = blank(); d = ImageDraw.Draw(lay)
        p = e_io3((t - 0.05) / 0.7); xr = X0 + (X1 - X0) * p
        if p > 0: d.rounded_rectangle((X0, Y - BH / 2, xr, Y + BH / 2), 16, fill=(64, 64, 70, 255), outline=(255, 255, 255, 60), width=2)
        for k, (a, b) in enumerate(segs):
            ts = t_seg[k]; sx0, sx1 = X0 + (X1 - X0) * a, X0 + (X1 - X0) * b
            if t < ts: continue
            if t < t_lift[0]:
                u = e_c3((t - ts) / 0.3); d.rounded_rectangle((sx0, Y - BH / 2 + 6, sx0 + (sx1 - sx0) * u, Y + BH / 2 - 6), 10, fill=MARK)
            else:
                q = e_io3((t - t_lift[0]) / 0.7); cxs = (sx0 + sx1) / 2; tx, ty = ox, oy + OHt / 2 - 62 - k * 66
                cx_, cy_ = cxs + (tx - cxs) * q, Y + (ty - Y) * q; wd = (sx1 - sx0) + (190 - (sx1 - sx0)) * q
                d.rounded_rectangle((cx_ - wd / 2, cy_ - 26, cx_ + wd / 2, cy_ + 26), 10, fill=MARK)
        fr.alpha_composite(O.with_alpha(lay, oa) if oa < 1 else lay)
        if t >= 0.35: rise_in(fr, lab_full, W / 2, Y - 90, t - 0.35, al=oa)
        if t >= t_rest: rise_in(fr, lab_rest, (X0 + X1) / 2, Y + 90, t - t_rest, al=oa)
        if t >= t_lift[0]:
            u = e_c3((t - t_lift[0]) / 0.6); o = Image.new("RGBA", (OW + 8, OHt + 8), (0, 0, 0, 0))
            ImageDraw.Draw(o).rounded_rectangle((2, 2, OW + 2, OHt + 2), 28, outline=(255, 255, 255, int(178 * u)), width=3)
            place(fr, o, ox, oy, al=oa)
            if t >= t_lift[1]: rise_in(fr, lab_short, ox + OW / 2 + 40 + lab_short.width / 2, oy, t - t_lift[1], al=oa)
        return fr
    return f, n


# ------------------------------------------------------------------ anatomy (hero)
def k_anatomy(plan, seq, g):
    dur = g["t1"] - g["t0"]; n = int(round(dur * FPS)); OW, OHt = 360, 640; cx, cy = g.get("cx", 600), g.get("cy", 640)
    x0, y0 = cx - OW / 2, cy - OHt / 2; bands = [("HOOK", 0.0, 0.26), ("MIDDLE", 0.26, 0.74), ("PAYOFF", 0.74, 1.0)]
    T = {k: g[k] for k in ("hook_at", "thread_at", "payoff_at", "arc_at", "branch_at", "snip_at")}
    labs = {nm: rich_line(nm, F(BEBAS, 56), fill=WHITE) for nm, _, _ in bands}; labd = {nm: rich_line(nm, F(BEBAS, 56), fill=(14, 14, 16, 255)) for nm, _, _ in bands}
    tl = shadowed(rich_line("TANGENT", F(BEBAS, 44), fill=GREY), 8, 110, 3); te = shadowed(rich_line("EXTRA DETAILS", F(BEBAS, 38), fill=GREY), 8, 110, 3)

    def f(i):
        t = i / FPS; fr = blank(); oa = out_alpha(t, dur); lay = blank(); d = ImageDraw.Draw(lay)
        shrink = 0.12 * e_io3((t - T["snip_at"] - 0.55) / 0.5) if t >= T["snip_at"] + 0.55 else 0.0
        by = []
        for k, (nm, a, b) in enumerate(bands):
            if k == 1: a, b = a + (b - a) * shrink / 2, b - (b - a) * shrink / 2
            by.append((y0 + OHt * a, y0 + OHt * b))
        for k, (nm, a, b) in enumerate(bands):
            ya, yb = by[k]
            if k in (0, 2) and t >= (T["hook_at"] if k == 0 else T["payoff_at"]):
                q = e_c3((t - (T["hook_at"] if k == 0 else T["payoff_at"])) / 0.3)
                d.rectangle((x0 + 3, ya + (3 if k == 0 else 1), x0 + OW - 3, yb - (1 if k == 0 else 3)), fill=MARK[:3] + (int(235 * q),))
            if k: d.line((x0, ya, x0 + OW, ya), fill=(255, 255, 255, 90), width=2)
        d.rounded_rectangle((x0, y0, x0 + OW, y0 + OHt), 28, outline=(255, 255, 255, 178), width=3)
        for k, (nm, a, b) in enumerate(bands):
            on = (k == 0 and t >= T["hook_at"] + 0.1) or (k == 2 and t >= T["payoff_at"] + 0.1)
            rise_in(lay, (labd if on else labs)[nm], cx + (24 if k == 1 else 0), (by[k][0] + by[k][1]) / 2, t, al=oa)
        if t >= T["thread_at"]:
            q = e_c3((t - T["thread_at"]) / 0.6); ya, yb = by[0][1], by[1][1]
            d.line((x0 + 36, ya - 8, x0 + 36, ya - 8 + (yb - ya + 16) * q), fill=MARK, width=5)
        if t >= T["arc_at"]:
            q = e_io3((t - T["arc_at"]) / 0.8); ap = (by[2][0] + by[2][1]) / 2; ah = (by[0][0] + by[0][1]) / 2; pts = []
            for s_ in range(41):
                u = s_ / 40; pts.append((x0 + OW + 6 + 70 * math.sin(math.pi * u), ap + (ah - ap) * u))
            m = max(2, int(len(pts) * q)); d.line(pts[:m], fill=MARK, width=5, joint="curve")
            if q > 0.97:
                (xa, ya_), (xb, yb_) = pts[-3], pts[-1]; a_ = math.atan2(yb_ - ya_, xb - xa)
                for da in (2.55, -2.55): d.line((xb, yb_, xb + 26 * math.cos(a_ + da), yb_ + 26 * math.sin(a_ + da)), fill=MARK, width=5)
        mid = (by[1][0] + by[1][1]) / 2
        if t >= T["branch_at"]:
            q = e_c3((t - T["branch_at"]) / 0.55); fade = 1 - e_c3((t - T["snip_at"] - 0.1) / 0.4) if t >= T["snip_at"] else 1.0
            if fade > 0.02:
                for sgn, lab in ((-1, tl), (1, te)):
                    x1 = cx + sgn * (OW / 2); x2 = x1 + sgn * 100 * q; y2 = mid + (-100 if sgn < 0 else 100) * q
                    L = math.hypot(x2 - x1, y2 - mid); k_ = max(1, int(L // 14))
                    for s_ in range(0, k_, 2):
                        ua, ub = s_ / k_, min(1, (s_ + 1) / k_)
                        d.line((x1 + (x2 - x1) * ua, mid + (y2 - mid) * ua, x1 + (x2 - x1) * ub, mid + (y2 - mid) * ub), fill=(255, 255, 255, int(220 * fade)), width=4)
                    if q > 0.8: place(lay, lab, x2 + (lab.width / 2 - 10 if sgn < 0 else lab.width / 2 - 20), y2 + (-34 if sgn < 0 else 34), al=fade * c01((q - 0.8) / 0.2))
                    ts_ = T["snip_at"] + (0.0 if sgn < 0 else 0.25)
                    if t >= ts_:
                        u = c01((t - ts_) / 0.2); xm, ym = (x1 + x2) / 2, (mid + y2) / 2; col = (255, 255, 255, int(255 * u * fade))
                        d.line((xm - 16, ym - 16, xm + 16, ym + 16), fill=col, width=5); d.line((xm - 16, ym + 16, xm + 16, ym - 16), fill=col, width=5)
        fr.alpha_composite(O.with_alpha(lay, oa) if oa < 1 else lay)
        return fr
    return f, n


# ------------------------------------------------------------------ twin_cards
def k_twin_cards(plan, seq, g):
    dur = g["t1"] - g["t0"]; n = int(round(dur * FPS)); cw, ch = 300, 533; cy = g.get("cy", 650)
    xs = [W / 2 - 190, W / 2 + 190]; cards = []
    for k in (0, 1):
        s = g["cards"][k]; im = rounded(still(s["file"], s["t"], (cw, ch)), 22)
        body = Image.new("RGBA", (cw + 8, ch + 8), (0, 0, 0, 0)); body.alpha_composite(im, (4, 4))
        ImageDraw.Draw(body).rounded_rectangle((2, 2, cw + 5, ch + 5), 24, outline=(255, 255, 255, 178), width=3); cards.append(body)
    labs = [shadowed(rich_line(g["labels"][k], F(BEBAS, 46), fill=(GREY if k == 0 else MARK)), 8, 120, 3) for k in (0, 1)]
    ev = g.get("events", []); ent = g.get("entrance") or "foldx"

    def f(i):
        t = i / FPS; fr = blank(); oa = out_alpha(t, dur)
        for k in (0, 1):
            lift = 0.0
            for at, who, tx in ev:
                if who == k and t >= at: lift = 10 * e_c3((t - at) / 0.3)
            for at, who, tx in ev:
                if who == "settle" and t >= at: lift *= 1 - e_c3((t - at) / 0.4)
            u = t - k * 0.12
            if u < 0: continue
            fr.alpha_composite(O.pop_frame(shadowed(cards[k], 22, 120, 10), xs[k], cy - lift, u, dur - k * 0.12, ent=ent))
        for k in (0, 1):
            if t >= 0.35 + 0.1 * k: rise_in(fr, labs[k], xs[k], cy + ch / 2 + 44, t - 0.35 - 0.1 * k, al=oa)
        for at, who, tx in ev:
            if who == "eq" and t >= at:
                u = t - at; q = e_q5(u / 0.3); eq = rich_line("=", F(BEBAS, 150), fill=MARK)
                place(fr, shadowed(eq, 12, 150, 4), W / 2, cy, al=min(1, u / 0.15) * oa, scale=0.7 + 0.3 * q)
                if u > 0.25: rise_in(fr, shadowed(rich_line(tx, F(BEBAS, 72)), 10, 140, 4), W / 2, cy - ch / 2 - 56, u - 0.25, al=oa)
            if who in (0, 1) and t >= at:
                rise_in(fr, shadowed(rich_line(tx, F(BEBAS, 44)), 10, 140, 4), xs[who], cy - ch / 2 - 40, t - at, al=oa)
        return fr
    return f, n


# ------------------------------------------------------------------ badge_card
def k_badge_card(plan, seq, g):
    dur = g["t1"] - g["t0"]; n = int(round(dur * FPS)); av = avatar(os.path.join(plan["_dir"], g["avatar"]), 118)
    for fs_ in (92, 84, 76, 70, 64):
        lines = [(tt - g["t0"], rich_line(tx, F(BEBAS, fs_))) for tt, tx in g["lines"]]
        if max(l.width for _, l in lines) <= 800: break
    w, h = int(min(1020, max(760, max(l.width for _, l in lines) + 230))), 190
    card = O.card_body((w, h), 40, (16, 16, 16, 238), outline=(255, 255, 255, 38), width=2); card.alpha_composite(av, (30, (h - 118) // 2))
    cx, cy = W / 2, g.get("y", 1430)

    def f(i):
        t = i / FPS; fr = blank(); oa = out_alpha(t, dur)
        fr.alpha_composite(enter(g, card, cx, cy, t, dur))
        k = max([j for j, (tt, _) in enumerate(lines) if tt <= t + 1e-6] or [0])
        if t < lines[0][0]: return fr
        for j in (k - 1, k):
            if j < 0: continue
            tt, sp = lines[j]
            if j == k: u = t - tt; al = e_q5(u / 0.34); dy = 16 * (1 - e_q5(u / 0.34))
            else:
                u = t - lines[k][0]
                if u >= 0.22: continue
                al = 1 - u / 0.22; dy = -10 * u / 0.22
            place(fr, sp, cx + 70, cy + dy, al=al * (oa if t >= dur - 0.24 else 1.0))
        return fr
    return f, n


# ------------------------------------------------------------------ letter_card
def k_letter_card(plan, seq, g):
    dur = g["t1"] - g["t0"]; n = int(round(dur * FPS)); av = avatar(os.path.join(plan["_dir"], g["avatar"]), 116)
    w, h = 1000, 270; card = O.card_body((w, h), 30, (18, 18, 20, 244), outline=(255, 255, 255, 46), width=2); d = ImageDraw.Draw(card)
    d.text((176, 40), g.get("to", "TO:"), font=F(BEBAS, g.get("to_px", 48)), fill=GREY)
    card.alpha_composite(rich_line(g["name"], F(BEBAS, 54)), (168, 98))
    d.line((176, 190, w - 60, 190), fill=(255, 255, 255, 46), width=2); d.text((176, g.get("sub_y", 204)), g.get("sub", ""), font=F(INTER_R, g.get("sub_px", 40)), fill=(170, 170, 170, 255))
    card.alpha_composite(av, (34, 30))
    cx, cy = W / 2, g.get("y", 1400); t_fold = g["fold_at"]; t_seal = t_fold + 0.42; fh = int(h * 0.30); pad = int(fh * 1.6)
    _nm = rich_line(g["name"], F(BEBAS, 54)); nm_w, nm_h = _nm.width, _nm.height; SD = 80                                  # fix shift: the seal sits RIGHT of the name with >= 16 px air, never over the type
    seal_cx = min(168 + nm_w + 16 + SD / 2, w - 22 - SD / 2); assert seal_cx - SD / 2 >= 168 + nm_w + 16 - 0.5, f"seal would touch the name (name {nm_w} px, seal_cx {seal_cx})"
    seal = Image.new("RGBA", (SD, SD), (0, 0, 0, 0)); sd = ImageDraw.Draw(seal)
    sd.ellipse((3, 3, SD - 4, SD - 4), fill=MARK[:3] + (255,), outline=(255, 232, 160, 255), width=3); sd.text((SD / 2, SD / 2), (g.get("seal") or "")[:3], font=F(BEBAS, 40), fill=(40, 28, 6, 255), anchor="mm")

    def f(i):
        t = i / FPS; q = e_io3((t - t_fold) / 0.42)
        big = Image.new("RGBA", (w, h + pad), (0, 0, 0, 0)); big.alpha_composite(card, (0, pad)); bd = ImageDraw.Draw(big)
        tip_y = pad - fh * 1.3 * (1 - q) + fh * q
        bd.polygon([(0, pad), (w, pad), (w / 2, tip_y)], fill=(30, 30, 33, 255), outline=(255, 255, 255, 60))
        if t >= t_seal:
            u = e_q5((t - t_seal) / 0.25); k_ = 0.6 + 0.4 * u; s2 = seal.resize((int(SD * k_), int(SD * k_)), Image.LANCZOS)
            big.alpha_composite(s2, (int(seal_cx - s2.width / 2), int(pad + 98 + nm_h / 2 - s2.height / 2)))
        return enter(g, big, cx, cy - pad / 2, t, dur)
    return f, n


# ------------------------------------------------------------------ fan_cards (beat 17b, fix shift 2026-11-09)
def k_fan_cards(plan, seq, g):
    """FACE beat, low band: our two sample covers as small 9:16 cards fanned on the LEFT (YT -4 deg, IG +4 deg overlapping, 1 px keyline at 25 %, soft shadow); two lines of
    type on the RIGHT (Bebas white + the accent face): rows appear at g['rows'] = [[t_abs, row, text], ...]; a later entry for the same row swaps it (rise out / rise in, never a pop)"""
    dur = g["t1"] - g["t0"]; n = int(round(dur * FPS)); cw, ch = 230, 410; cy = g.get("y", 1375); ent = g.get("entrance") or "foldx"
    def cover(c, ang):
        im = rounded(still(c["file"], c["t"], (cw, ch)), 18)
        body = Image.new("RGBA", (cw + 6, ch + 6), (0, 0, 0, 0)); body.alpha_composite(im, (3, 3))
        ImageDraw.Draw(body).rounded_rectangle((1, 1, cw + 4, ch + 4), 20, outline=(255, 255, 255, 64), width=1)
        return shadowed(body.rotate(ang, resample=Image.BICUBIC, expand=True), 22, 130, 10)
    cards = [cover(g["cards"][0], 4), cover(g["cards"][1], -4)]              # PIL angle > 0 = counter-clockwise = CSS -4 deg (YT); IG clockwise (+4)
    xs = [g.get("x0", 215), g.get("x0", 215) + 110]; delay = [0.0, 0.1]
    rows = {}
    for t_abs, row, txt in g["rows"]:
        for fs_ in range(96, 56, -4):
            sp = rich_line(txt, F(BEBAS, fs_))
            if sp.width <= 470: break
        rows.setdefault(row, []).append((t_abs - g["t0"], shadowed(sp, 10, 140, 4)))
    ry = {0: cy - 52, 1: cy + 50}; rx = 810

    def f(i):
        t = i / FPS; fr = blank(); oa = out_alpha(t, dur)
        for k in (0, 1):
            u = t - delay[k]
            if u < 0: continue
            fr.alpha_composite(O.pop_frame(cards[k], xs[k], cy, u, dur - delay[k], ent=ent))
        for row, lst in rows.items():
            k = max([j for j, (tt, _) in enumerate(lst) if tt <= t + 1e-6] or [-1])
            if k < 0: continue
            for j in (k - 1, k):
                if j < 0: continue
                tt, sp = lst[j]
                if j == k: u = t - tt; al = e_q5(u / 0.34); dy = 16 * (1 - e_q5(u / 0.34))
                else:
                    u = t - lst[k][0]
                    if u >= 0.22: continue
                    al = 1 - u / 0.22; dy = -10 * u / 0.22
                place(fr, sp, rx, ry[row] + dy, al=al * oa)
        return fr
    return f, n


NEW = {"otn_hook": k_otn_hook, "cred_chips": k_cred_chips, "title_strip": k_title_strip, "pointer_tag": k_pointer_tag, "pair_count": k_pair_count,
       "bar_to_short": k_bar_to_short, "anatomy": k_anatomy, "twin_cards": k_twin_cards, "badge_card": k_badge_card, "letter_card": k_letter_card, "fan_cards": k_fan_cards}
X.NEW.update(NEW)
O.PANEL_KINDS = set(O.PANEL_KINDS) | {"pair_count", "bar_to_short", "anatomy", "twin_cards"}


# ------------------------------------------------------------------ page_marks (full-window page: a read-along sweep + a gold ring on source-px boxes)
WIN = (0, 227, 1080, 1653)


def src2win(plan, view, sx, sy):
    v = plan["views_named"][view]; s = G.BASE * v["z"]
    return (WIN[0] + WIN[2]) / 2 + (sx - v["cx"]) * s, (WIN[1] + WIN[3]) / 2 + (sy - v["cy"]) * s


def k_page_marks(plan, seq, g):
    dur = g["t1"] - g["t0"]; n = int(round(dur * FPS))
    x0, y0 = src2win(plan, g["view"], *g["sweep"][:2]); x1, y1 = src2win(plan, g["view"], *g["sweep"][2:])
    rx0, ry0 = src2win(plan, g["view"], *g["ring"][:2]); rx1, ry1 = src2win(plan, g["view"], *g["ring"][2:]); pad = g.get("ring_pad", 12)
    t_s, t_r = g["sweep_at"], g["ring_at"]

    def f(i):
        t = i / FPS; fr = blank(); oa = out_alpha(t, dur, 0.2); lay = blank(); d = ImageDraw.Draw(lay)
        if t >= t_s:
            p = e_c3((t - t_s) / 0.45); lh = y1 - y0
            d.rounded_rectangle((x0, (y0 + y1) / 2 - 0.48 * lh, x0 + (x1 - x0) * p, (y0 + y1) / 2 + 0.48 * lh), 4, fill=MARK[:3] + (107,))
        if t >= t_r:
            q = e_io3((t - t_r) / 0.45); ring = X._round_outline((int(rx1 - rx0) + 2 * pad + 40, int(ry1 - ry0) + 2 * pad + 40), (20, 20, 20 + rx1 - rx0 + 2 * pad, 20 + ry1 - ry0 + 2 * pad), 14, q, width=5)
            lay.alpha_composite(ring, (int(rx0 - pad - 20), int(ry0 - pad - 20)))
        fr.alpha_composite(O.with_alpha(lay, oa) if oa < 1 else lay); return fr
    return f, n


X.NEW["page_marks"] = k_page_marks
O.PANEL_KINDS = set(O.PANEL_KINDS) | {"page_marks"}


# ------------------------------------------------------------------ scorecard "big" (polish shift 2026-11-09): phone-size type, full panel width
import re as _re
_sc0 = X.NEW["scorecard"]


def k_scorecard_big(plan, seq, g):
    if not g.get("big"): return _sc0(plan, seq, g)
    dur = g["t1"] - g["t0"]; n = int(round(dur * FPS)); rows = g["rows"]; P = tuple(g.get("panel", K.PANEL))
    cw = int(g.get("w", 960)); hdr = 104; pad_b = 24; row_h = g.get("row_h", 158); ch = hdr + row_h * len(rows) + pad_b
    cx = g.get("x", W / 2); cy = g.get("y", (P[1] + P[3]) / 2)
    if cy - ch / 2 < 200 or cy + ch / 2 > 1620 or ch > P[3] - P[1]: raise SystemExit(f"scorecard {g['id']}: card {ch} px does not fit the panel")
    colw = int(cw * 0.46); xl, xm, xr = cw * 0.255, cw * 0.5, cw * 0.745
    LAB, COPY, NUM = g.get("lab_px", 48), g.get("copy_px", 64), g.get("num_px", 90)
    base = O.rrect((cw, ch), 26, (14, 14, 16, 240), outline=(255, 255, 255, 34), width=1)
    hl = Image.new("RGBA", (cw, ch), (0, 0, 0, 0)); ImageDraw.Draw(hl).line((26, 1, cw - 26, 1), fill=(255, 255, 255, 46), width=1); base.alpha_composite(hl)
    bd = ImageDraw.Draw(base)
    bd.text((xl, hdr * 0.55), "THEIRS", font=F(BEBAS, 46), fill=GREY, anchor="mm")
    bd.text((xr, hdr * 0.55), "OURS", font=F(BEBAS, 46), fill=GOLD + (255,), anchor="mm")
    bd.line((30, hdr, cw - 30, hdr), fill=(255, 255, 255, 30), width=1)
    for k in range(1, len(rows)): bd.line((46, hdr + k * row_h, cw - 46, hdr + k * row_h), fill=(255, 255, 255, 14), width=1)
    dm = ImageDraw.Draw(Image.new("RGBA", (1, 1)))

    def cell(text, fill):
        isnum = bool(_re.fullmatch(r"[\d:.,% ]+", text)); px = NUM if isnum else COPY; f = F(INTER_B, px); lines = K._wrap(text, f, colw)
        assert len(lines) <= 2 and all(dm.textlength(l, font=f) <= colw for l in lines), f"scorecard cell '{text}' does not fit {colw} px at {px} px"
        lh = int(px * 1.2); im = Image.new("RGBA", (colw + 8, lh * len(lines) + 6), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
        for k, l in enumerate(lines): d.text((im.width / 2, 3 + lh * k + lh / 2), l, font=f, fill=fill, anchor="mm")
        return im
    R = []
    for k, row in enumerate(rows):
        R.append(dict(t=row[0] - g["t0"], lab=row[1], th=cell(row[2], (225, 225, 228, 255)), ou=cell(row[3], GOLD + (255,)), y=hdr + k * row_h))

    def rise(layer, im, xc, yc, u):
        if u <= 0: return
        p = e_q5(u / 0.32); dy = 24 * (1 - p)
        layer.alpha_composite(O.with_alpha(im, min(1.0, u / 0.16)) if u < 0.16 else im, (int(xc - im.width / 2), int(yc - im.height / 2 + dy)))

    def fn(i):
        t = i / FPS; sp = base.copy()
        for r in R:
            if t < r["t"]: continue
            u = t - r["t"]; row = Image.new("RGBA", (cw, row_h), (0, 0, 0, 0)); rd = ImageDraw.Draw(row)
            if u > 0:
                a = int(204 * min(1.0, u / 0.16)); rd.text((xm, 30 + 24 * (1 - e_q5(u / 0.32))), r["lab"], font=F(INTER_SB, LAB), fill=(255, 255, 255, a), anchor="mm")
            yc = 30 + (row_h - 30) / 2 + 6
            rise(row, r["th"], xl, yc, u); uo = u - 0.18; rise(row, r["ou"], xr, yc, uo)
            if uo > 0:
                w_ = r["ou"].width * 0.0 + min(r["ou"].width, 300) * 0.62; q = e_c3(uo / 0.25); yy = row_h - 12
                rd.rounded_rectangle((xr - w_ / 2, yy, xr - w_ / 2 + w_ * q, yy + 3), 1, fill=GOLD + (255,))
            sp.alpha_composite(row, (0, r["y"]))
        return M6.enter(g, sp, cx, cy, t, dur)
    return fn, n


X.NEW["scorecard"] = k_scorecard_big
