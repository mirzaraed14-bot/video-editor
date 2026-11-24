"""mgxo.py: mgx7.py + the kit MENU kinds (kindsmenu.py). Same CLI."""

import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import viewpatch  # noqa: E402,F401  (per-view box + crop_left_src, fix shift)
import kindsmenu  # noqa: E402  (kinds7 -> mgx6 + the menu kinds)
K = kindsmenu.K
M6, X, O = K.M6, K.X, K.O
G = O.G
_cc = O.caption_chunks


def caption_chunks_0(plan):
    """R7 (fix shift): the first caption chunk starts on frame 0 (0.000), with the first word"""
    ch = _cc(plan)
    if ch and ch[0]["t0"] < 0.2: ch[0]["t0"] = 0.0
    return ch


O.caption_chunks = caption_chunks_0


def _sig_foldx8(c, tau):
    """V3 motion: the 'foldx' card entrance with NO big scale change (<= 8 %: the card opens from 0.92 to 1.00 of its width), no overshoot (outQuint), the 14 px rise and the fade kept"""
    u = K.cl(tau / 0.40); p = K.e_q5(u); sx = 0.92 + 0.08 * p
    S = c.S(shift=(0, 14 * (1 - K.e_q5((tau - 0.08) / 0.40))), mix=p)
    w2 = max(2, int(round(S.width * sx)))
    im = S.resize((w2, S.height), K.Image.LANCZOS) if w2 != S.width else S; al = min(1.0, u / 0.30)
    return (O.with_alpha(im, al) if al < 1 else im), -w2 / 2, -S.height / 2


# slab signature: the kinds7 default (no overshoot, no scale change)


def _cap_shift(orig):
    def f(text, size=96):
        im = orig(text, size); dy = int(round(float(CAP_Y[0]) - O.SEAM)) if CAP_Y[0] else 0
        if not dy: return im
        out = Image.new("RGBA", im.size, (0, 0, 0, 0)); out.paste(im, (0, dy)); return out
    return f


CAP_Y = [None]
O.caption_png = _cap_shift(O.caption_png)
from PIL import Image, ImageDraw, ImageFont         # noqa: E402

if __name__ == "__main__":
    a = sys.argv[1:]
    plan, seq = O.load(a[0])
    if plan.get("mouth_y"): M6.MOUTH_Y = float(plan["mouth_y"])
    CAP_Y[0] = plan.get("cap_y")          # V3: ONE constant caption base just below the measured lips (the seam line stays where it is)
    if "--captions" in a: O.build_captions(plan)
    if "--mg" in a: O.build_mg(plan, seq, a[a.index("--only") + 1] if "--only" in a else None)
    if "--check" in a:
        e_, _ = O.check(plan, seq); e2 = X.stage_check(plan, seq)
        if e_ or e2: sys.exit(1)
    if "--still" in a:
        ts = [float(x) for x in a[a.index("--still") + 1:] if not x.startswith("--")]
        import preview

        def fast_still(t):
            base = preview.render(plan, seq, t).convert("RGBA")
            for g in sorted(plan["graphics"], key=lambda g: 0 if g["kind"] == "showcase" else 1):
                if not (g["t0"] <= t < g["t1"]): continue
                for it in (g["items"] if g["kind"] == "group" else [g]):
                    if it["t0"] <= t < it["t1"]:
                        if it["kind"] in O.SEEKABLE:
                            fr = next(O.SEEKABLE[it["kind"]](plan, seq, it, int((t - it["t0"]) * K.FPS), 1), None)
                            if fr: base.alpha_composite(fr)
                            continue
                        fn, _ = O._frame_fn(plan, seq, it); base.alpha_composite(fn(int((t - it["t0"]) * K.FPS)))
            if plan.get("seam_line") and not G.face_at(plan, t):
                qq = O.seam_frac(plan, t); base.alpha_composite(O.seam_line_png(4) if qq >= 1 else O.seam_line_png(4, qq))
            cj = os.path.join(plan["_dir"], "overlays", "captions.json")
            if os.path.exists(cj):
                for c in json.load(open(cj, encoding="utf-8")):
                    if c["t0"] <= t < c["t1"]: base.alpha_composite(O.caption_png(c["text"]))
            return base.convert("RGB")
        ims = [fast_still(t) for t in ts]
        os.makedirs(os.path.join(plan["_dir"], "work"), exist_ok=True)
        fnt = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 54)
        for t, im in zip(ts, ims):
            ImageDraw.Draw(im).text((24, 1850), f"{t:.2f}", font=fnt, fill=(255, 220, 0))
            im.save(os.path.join(plan["_dir"], "work", f"still-{t:.2f}.png"))
        w, h = 432, 768
        sheet = Image.new("RGB", (w * min(5, len(ims)), h * ((len(ims) + 4) // 5)))
        for i, im in enumerate(ims): sheet.paste(im.resize((w, h), Image.LANCZOS), ((i % 5) * w, (i // 5) * h))
        p = os.path.join(plan["_dir"], "work", "stills.jpg"); sheet.save(p, quality=88); print(p)
