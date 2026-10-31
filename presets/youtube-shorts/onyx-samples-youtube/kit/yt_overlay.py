"""yt_overlay.py: PASS 2 of a YouTube-look sample: the OVERLAY layer (captions, hook title, watermark) as a HyperFrames
composition with a transparent background (README § 5, § 6) -> <job>/yt/hf-overlay/index.html (+ fonts/, vendor/).

  python presets/youtube-shorts/onyx-samples-youtube/kit/yt_overlay.py projects/<job>
  cd projects/<job>/yt/hf-overlay && npx --yes hyperframes@0.8.16 render . --format mov --fps <fps> -o ../work/overlay.mov

Reads `<job>/yt/spec.json` → "hook": {"lines": ["SMALL WHITE LINE", "BIG GRADIENT LINE"], "caps": [49, 75], "y": [1357, 1442],
"max_w": 840, "t0": 0.0 (s: the card lands later, e.g. a guest credit on the line that names him)} and "watermark": "SHOW NAME" (+ optional "watermark_y", centre px, default 1160: lower it when the captions sit low, ig_capy.py), plus `<job>/yt/captions.json` (yt_captions.py). The hook slides in from the left
over ~0.46 s, holds, slides out over ~0.88 s and is gone by ~3.2 s, with per-frame horizontal motion blur; every timeline
step sits a quarter frame before its frame boundary (exact boundaries round a third of them a frame late).
"""
import json, math, os, shutil, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "onyx-samples", "kit"))
from captext import clean          # the caption punctuation rule (Affan, 2026-10-07: only ! ? and quotation marks)
from PIL import ImageFont

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8")
    except Exception:
        pass

KIT = os.path.dirname(os.path.abspath(__file__))
W, H = 1080, 1920
IN_24, HOLD_END_24, OUT_24 = 11, 56, 21          # frames at 24 fps (the reference); main() scales them to the job fps
BLURS = [2, 6, 12, 24, 40]


def mont(size):
    f = ImageFont.truetype(os.path.join(KIT, "fonts", "Montserrat-VF.ttf"), size)
    try:
        f.set_variation_by_axes([900])
    except Exception:
        pass
    return f


def main():
    job = os.path.abspath(sys.argv[1])
    spec = json.load(open(os.path.join(job, "yt", "spec.json"), encoding="utf-8"))
    cap = json.load(open(os.path.join(job, "yt", "captions.json"), encoding="utf-8"))
    fps = spec["fps"]
    dur = cap["frames"] / fps
    hook = spec.get("hook") or {}
    lines = [clean(l) for l in hook.get("lines", [])]
    caps, ys, max_w = hook.get("caps", [49, 75]), hook.get("y", [1357, 1442]), min(hook.get("max_w", 840), 840)   # x 120-960: clear of YouTube's right-hand buttons
    l, t, r, b = mont(1000).getbbox("H")
    cr = (b - t) / 1000
    sizes = []
    for text, c in zip(lines, caps):
        size = c / cr
        width = mont(round(size)).getlength(text)
        sizes.append(round(size * min(1.0, max_w / width), 1))
    if len(sizes) == 2 and caps[1] and sizes[1] * caps[0] / caps[1] < sizes[0]:
        sizes[0] = round(sizes[1] * caps[0] / caps[1], 1)   # a width-capped big line shrinks the small line too: the 0.65 ratio stays (QA r2)
    # the hook's timing was measured at 24 fps (0.46 s in, out from 2.33 s, 0.88 s out, gone by 3.2 s): scale to this job's rate
    # (QA 2026-10-06: at 30 fps the raw frame counts ran 2.47 s)
    IN_FRAMES, HOLD_END, OUT_FRAMES = (int(round(n * fps / 24)) for n in (IN_24, HOLD_END_24, OUT_24))
    ease_in = lambda p: 1 if p >= 1 else 1 - 2 ** (-10 * p)
    hook_x = {}
    for f in range(IN_FRAMES):
        hook_x[f] = -1150 * (1 - ease_in((f + 1) / IN_FRAMES))
    for f in range(IN_FRAMES, HOLD_END):
        hook_x[f] = 0.0
    for i in range(OUT_FRAMES):
        hook_x[HOLD_END + i] = -1250 * ((i + 1) / OUT_FRAMES) ** 2

    def lvl(dx):
        s = min(abs(dx) * 0.25, 40)
        return 0 if s < 1 else 1 + min(range(len(BLURS)), key=lambda i: abs(BLURS[i] - s))

    steps, prev = [], hook_x[0] + 1150 * 0.6
    for f in range(HOLD_END + OUT_FRAMES):
        x = hook_x[f]
        steps.append((round(max(0.0, (f - 0.25) / fps), 5), round(x, 1), lvl(x - prev)))
        prev = x
    hide_t = round((HOLD_END + OUT_FRAMES - 0.25) / fps, 5)
    t0 = float(hook.get("t0", 0.0))             # hook.t0 (s): the card lands later, e.g. a guest credit on the line that names him (Scott 2026-10-21)
    if t0:
        steps = [(0.0, -1300.0, 0)] + [(round(t + t0, 5), x, bl) for t, x, bl in steps]; hide_t = round(hide_t + t0, 5)

    out = os.path.join(job, "yt", "hf-overlay")
    os.makedirs(os.path.join(out, "fonts"), exist_ok=True)
    os.makedirs(os.path.join(out, "vendor"), exist_ok=True)
    for fn in ("Anton-Regular.ttf", "Montserrat-VF.ttf"):
        shutil.copy(os.path.join(KIT, "fonts", fn), os.path.join(out, "fonts", fn))
    shutil.copy(os.path.join(KIT, "vendor", "gsap.min.js"), os.path.join(out, "vendor", "gsap.min.js"))
    kit_css = open(os.path.join(KIT, "yt-captions.css"), encoding="utf-8").read()
    kit_js = open(os.path.join(KIT, "yt-captions.js"), encoding="utf-8").read()
    chunks = [dict(text=clean(c["text"]), start=c["start"], end=c["end"], voice=c["voice"], wipe=c["wipe"], **({"y": c["y"]} if "y" in c else {}),
                   **({"moves": c["moves"]} if c.get("moves") else {}))     # ig_capy.py: [frame, y] on a cut inside the chunk
              for c in cap["chunks"]]
    hb = "\n".join(f'<filter id="hook-hb{i + 1}" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="{bv} 0"/></filter>'
                   for i, bv in enumerate(BLURS))
    hook_divs = "".join(
        f'<div id="hl{i + 1}" class="hl" style="top:{ys[i] - sizes[i] * 0.62:.0f}px;font-size:{sizes[i]}px;height:{sizes[i] * 1.3:.0f}px" '
        f'data-layout-allow-overflow><span class="stroke">{txt}</span><span class="fill">{txt}</span></div>' for i, txt in enumerate(lines))
    wm = spec.get("watermark", "")
    # captions.on_seam (Affan 2026-10-12): ONE constant caption line for the whole video, ON the split seam's white line, so a split
    # that arrives later finds the captions already there; captions.y pins any other constant glyph centre
    cs = spec.get("captions", {})
    cy_ = (spec.get("split", {}).get("seam", 1092) + cs.get("seam_dy", 0)) if cs.get("on_seam") else cs.get("y")
    cap_y = f", y: {float(cy_):.1f}" if cy_ is not None else ""
    # TAGS (Affan 2026-10-23, War Dogs): a name tag beside the guest's head ("THE REAL / DAVID PACKOUZ"). Spec "tags": [{"t0", "t1",
    # "x", "y" (the dot, output px, beside the head), "dx" (+ = the label opens to the right), "dy" (elbow rise, px), "small", "big" ("|" breaks a line),
    # "plate" (optional: a dark rounded backing under the label)}]
    tags = spec.get("tags", [])
    tag_divs, tag_js = [], []
    for i, g in enumerate(tags):
        sgn = 1 if g.get("dx", 220) >= 0 else -1; L = abs(g.get("dx", 220)); rise = g.get("dy", -90)
        ex, ey = g["x"] + sgn * L, g["y"] + rise                              # the elbow end, where the label hangs
        tag_divs.append(
            f'<div id="tg{i}" class="tag">'
            f'<div class="tdot" style="left:{g["x"] - 9}px;top:{g["y"] - 9}px"></div>'
            f'<div class="tdiag" style="left:{g["x"]}px;top:{g["y"]}px;width:{math.hypot(L * 0.35, rise):.0f}px;'
            f'transform:rotate({math.degrees(math.atan2(rise, sgn * L * 0.35)):.2f}deg)"></div>'
            f'<div class="thor" style="left:{min(g["x"] + sgn * L * 0.35, ex)}px;top:{ey - 2}px;width:{L * 0.65:.0f}px;'
            f'transform-origin:{"left" if sgn > 0 else "right"} center"></div>'
            f'<div class="tlab" style="{"left" if sgn > 0 else "right"}:{ex + 14 if sgn > 0 else W - ex + 14}px;top:{ey - 40}px;'
            f'text-align:{"left" if sgn > 0 else "right"};'
            f'{"background:rgba(8,12,22,0.66);padding:8px 16px 6px;border-radius:12px;" if g.get("plate") else ""}">'   # plate: a dark backing over a busy background (Chris Do's bookshelf, 2026-10-24)
            f'<div class="tsm">{clean(g.get("small", ""))}</div>'
            f'<div class="tbig">{"<br>".join(clean(x) for x in g.get("big", "").split("|"))}</div></div></div>')   # "|" = a line break
        t0, t1 = g["t0"], g["t1"]
        tag_js.append(
            f'tl.set("#tg{i}", {{autoAlpha: 1}}, {t0});'
            f'tl.fromTo("#tg{i} .tdot", {{scale: 0}}, {{scale: 1, duration: 0.22, ease: "back.out(3)"}}, {t0});'
            f'tl.fromTo("#tg{i} .tdiag", {{scaleX: 0}}, {{scaleX: 1, duration: 0.16, ease: "power2.out"}}, {t0 + 0.12});'
            f'tl.fromTo("#tg{i} .thor", {{scaleX: 0}}, {{scaleX: 1, duration: 0.22, ease: "power2.out"}}, {t0 + 0.26});'
            f'tl.fromTo("#tg{i} .tlab", {{clipPath: "inset(0 {"100%" if sgn > 0 else "0"} 0 {"0" if sgn > 0 else "100%"})", y: 6}}, '
            f'{{clipPath: "inset(0 0% 0 0%)", y: 0, duration: 0.34, ease: "power3.out"}}, {t0 + 0.42});'
            f'tl.to("#tg{i}", {{autoAlpha: 0, y: -10, duration: 0.25, ease: "power2.in"}}, {t1 - 0.25});')
    # STAMPS + GLINTS (War Dogs, 2026-10-23): "stamps": [{"t", "text", "x", "y" (centre px), "angle", "color"}] slam in and hold;
    # "glints": [{"t", "x", "y", "size"}] = a four-point star that flashes on a word ("diamonds")
    for i, g in enumerate(spec.get("stamps", [])):
        col = g.get("color", "#E5383B")
        tag_divs.append(f'<div id="st{i}" class="stamp" style="left:{g["x"]}px;top:{g["y"]}px;color:{col};border-color:{col};'
                        f'">{clean(g["text"])}</div>')
        tag_js.append(f'tl.set("#st{i}", {{xPercent: -50, yPercent: -50, rotation: {g.get("angle", -8)}}}, 0);'
                      f'tl.fromTo("#st{i}", {{autoAlpha: 0, scale: 2.4}}, {{autoAlpha: 1, scale: 1, duration: 0.16, ease: "power4.in"}}, {g["t"]});'
                      f'tl.to("#st{i}", {{keyframes: [{{x: -9, duration: 0.04}}, {{x: 7, duration: 0.04}}, {{x: -4, duration: 0.04}}, {{x: 0, duration: 0.05}}]}}, {g["t"] + 0.16});')
    for i, g in enumerate(spec.get("glints", [])):
        z = g.get("size", 90)
        tag_divs.append(f'<div id="gl{i}" class="glint" style="left:{g["x"] - z / 2}px;top:{g["y"] - z / 2}px;width:{z}px;height:{z}px"></div>')
        tag_js.append(f'tl.fromTo("#gl{i}", {{autoAlpha: 0, scale: 0.2, rotation: -30}}, {{autoAlpha: 1, scale: 1, rotation: 0, duration: 0.18, ease: "power2.out"}}, {g["t"]});'
                      f'tl.to("#gl{i}", {{autoAlpha: 0, scale: 0.4, rotation: 25, duration: 0.3, ease: "power2.in"}}, {g["t"] + 0.32});')
    # a hook of N lines (Pincus 2026-10-31, a 4-line credit): every line white but the LAST, which takes the gold gradient (2 lines: as before)
    hl_white = ", ".join(f"#hl{i + 1} .fill" for i in range(max(1, len(lines) - 1)))
    hl_gold = f"#hl{max(2, len(lines))} .fill"
    comp_id = "onyx-yt-overlay"
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width={W}, height={H}" />
<style>
{kit_css}

@font-face {{ font-family: "YT Montserrat"; src: url("fonts/Montserrat-VF.ttf") format("truetype"); font-weight: 100 900; font-display: block; }}
html, body {{ margin: 0; background: transparent; }}
#root {{ position: relative; width: {W}px; height: {H}px; overflow: hidden; background: transparent; }}
.layer {{ position: absolute; inset: 0; pointer-events: none; }}
#hook {{ position: absolute; left: 0; top: 0; width: {W}px; height: {H}px; }}
.hl {{ position: absolute; left: 0; width: {W}px; text-align: center; font-family: "YT Montserrat", sans-serif; font-weight: 900;
  line-height: 1; white-space: nowrap; }}
.hl span {{ position: absolute; left: 0; width: {W}px; text-align: center; }}
.hl .stroke {{ color: #000; -webkit-text-stroke: 13px #000; text-shadow: 5px 7px 0 rgba(0,0,0,0.85); }}
{hl_white} {{ color: #FFFFFF; }}
{hl_gold} {{ background: linear-gradient(180deg, #F39A10 0%, #F6B412 45%, #F7D428 100%); -webkit-background-clip: text; background-clip: text;
  color: transparent; }}
.tag {{ position: absolute; inset: 0; visibility: hidden; }}
.tdot {{ position: absolute; width: 18px; height: 18px; border-radius: 50%; background: #19D3C5; box-shadow: 0 0 14px rgba(25,211,197,0.9); }}
.tdiag, .thor {{ position: absolute; height: 4px; background: #FFFFFF; transform-origin: left center; box-shadow: 0 2px 6px rgba(0,0,0,0.45); }}
.tlab {{ position: absolute; white-space: nowrap; filter: drop-shadow(0 4px 10px rgba(0,0,0,0.6)); }}
.tsm {{ font-family: "YT Montserrat", sans-serif; font-weight: 800; font-size: 26px; letter-spacing: 0.18em; color: #19D3C5; }}
.tbig {{ font-family: "YTC Anton", sans-serif; font-size: 58px; line-height: 1.02; color: #FFFFFF; letter-spacing: 0.01em; }}
.stamp {{ position: absolute; visibility: hidden; font-family: "YTC Anton", sans-serif; font-size: 112px; letter-spacing: 0.06em; padding: 4px 26px;
  border: 10px solid; border-radius: 14px; background: rgba(255,255,255,0.08); text-shadow: 0 0 2px rgba(0,0,0,0.3); mix-blend-mode: normal; }}
.glint {{ position: absolute; visibility: hidden; background: #FFFFFF; filter: drop-shadow(0 0 12px #CFF7FF) drop-shadow(0 0 26px #9EE7FF);
  clip-path: polygon(50% 0%, 58% 42%, 100% 50%, 58% 58%, 50% 100%, 42% 58%, 0% 50%, 42% 42%); }}
#wm {{ position: absolute; left: 0; width: {W}px; text-align: center; font-family: "YTC Anton", sans-serif; font-size: 47px;
  letter-spacing: 0.01em; color: rgba(255,255,255,0.38); transform: skewX(-12deg); text-shadow: 0 2px 4px rgba(0,0,0,0.18); line-height: 1; }}
</style>
</head>
<body>
<svg width="0" height="0" style="position:absolute"><defs>
{hb}
</defs></svg>
<div id="root" data-composition-id="{comp_id}" data-start="0" data-width="{W}" data-height="{H}" data-duration="{dur:.4f}" data-fps="{fps}">
  <div id="wm-layer" class="layer"><div id="wm" style="top:{spec.get("watermark_y", 1160) - 24}px">{wm}</div></div>
  <div id="tags" class="layer">{"".join(tag_divs)}</div>
  <div id="caps" class="layer"></div>
  <div id="hook" data-layout-allow-overflow>{hook_divs}</div>
</div>
<script src="vendor/gsap.min.js"></script>
<script>
{kit_js}
</script>
<script>
(function () {{
  window.__timelines = window.__timelines || {{}};
  const COMP = "{comp_id}";
  const tl = gsap.timeline({{ paused: true }});
  ytCaptions(tl, "#caps", {json.dumps(chunks, ensure_ascii=False)}, {{ fps: {fps}, palette: {json.dumps(spec.get("captions", {}).get("palette"))}{cap_y} }});
  {json.dumps(steps)}.forEach(([t, x, b]) => {{
    tl.set("#hook", {{ x: x, filter: b ? "url(#hook-hb" + b + ")" : "none" }}, t);
  }});
  tl.set("#hook", {{ autoAlpha: 0 }}, {hide_t});
  {"".join(tag_js)}
  tl.set({{}}, {{}}, {dur:.4f});
  window.__timelines[COMP] = tl;
}})();
</script>
</body>
</html>
"""
    open(os.path.join(out, "index.html"), "w", encoding="utf-8").write(html)
    print(f"yt_overlay: {len(chunks)} chunks, hook {lines} at {sizes} px, watermark '{wm}' -> {out}")


if __name__ == "__main__":
    main()
