"""preview.py <plan.json> [t1 t2 ...] -> work/preview-<t>.png and a sheet: simulate the planned frame at sequence time t
(screen view + face layout + nothing else) from the sources, so framings are checked before the timeline is touched."""
import json, os, sys
from PIL import Image, ImageDraw, ImageFont
sys.path.insert(0, os.path.dirname(__file__))
import geom as G


def render(plan, seq, t):
    G.configure(plan)
    vs, vf = seq["v"][plan["screen_track"]], seq["v"][plan["face_track"]]
    c = Image.new("RGB", (G.W, G.H))
    face = G.face_at(plan, t)
    sc = G.clip_at(vs, t)
    def screen():
        if sc and not face:
            im = G.frame(sc["p"], G.src_time(sc, t))
            m = G.view_motion(G.view_at(plan, t))
            G.place(c, im, m["scale"], m["pos"], m["crop"])
    if not plan.get("screen_on_top"): screen()
    fc = G.clip_at(vf, t)
    if fc:
        im = G.frame(fc["p"], G.src_time(fc, t))
        if face:
            f = G.face_motion(face.get("scale", 132), face.get("face_x"))
        elif sc:
            f = dict(G.FACE_SPLIT, crop=None)
        else:
            f = dict(G.FACE_ONLY, crop=None)
        G.place(c, im, f["scale"], f["pos"], f.get("crop"))
    if plan.get("screen_on_top"): screen()
    return c

if __name__ == "__main__":
    plan = json.load(open(sys.argv[1]))
    seq = next(s for s in json.load(open(plan["dump"])) if s["name"] == plan["sequence"])
    ts = [float(x) for x in sys.argv[2:]]
    ims = [render(plan, seq, t) for t in ts]
    f = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 60)
    for t, im in zip(ts, ims):
        ImageDraw.Draw(im).text((20, 1830), f"{t:.2f}", font=f, fill="yellow")
    w = 360; h = 640
    sheet = Image.new("RGB", (w * min(6, len(ims)), h * ((len(ims) + 5) // 6)))
    for i, im in enumerate(ims):
        sheet.paste(im.resize((w, h)), ((i % 6) * w, (i // 6) * h))
    out = os.path.join(os.path.dirname(sys.argv[1]), "preview-sheet.jpg")
    sheet.save(out, quality=85); print(out)
