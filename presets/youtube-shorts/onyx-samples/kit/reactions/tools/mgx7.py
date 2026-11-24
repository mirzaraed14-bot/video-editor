"""mgx7.py: the batch-7 reactions = mgx6 (-> mgx -> overlays) + kinds7 (play_card, portal, scorecard, hl_sweep, inset_cam + the entrances
tilt / slab / foldx / swing / shutter). Same CLI as mgx6:

  PYTHONUTF8=1 python mgx7.py <job>/plan.json [--captions] [--mg] [--only id,id] [--check] [--still t t ...]

Nothing is patched on disk: everything is applied at import. See KINDS7.md.
"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import kinds7 as K                                  # noqa: E402  (imports mgx6 first, then patches on top of it)
M6, X, O = K.M6, K.X, K.O
G = O.G
from PIL import Image, ImageDraw, ImageFont         # noqa: E402

if __name__ == "__main__":
    a = sys.argv[1:]
    plan, seq = O.load(a[0])
    if plan.get("mouth_y"): M6.MOUTH_Y = float(plan["mouth_y"])
    if "--captions" in a: O.build_captions(plan)
    if "--mg" in a: O.build_mg(plan, seq, a[a.index("--only") + 1] if "--only" in a else None)
    if "--check" in a:
        e_, _ = O.check(plan, seq); e2 = X.stage_check(plan, seq)
        if e_ or e2: sys.exit(1)
    if "--still" in a:
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
