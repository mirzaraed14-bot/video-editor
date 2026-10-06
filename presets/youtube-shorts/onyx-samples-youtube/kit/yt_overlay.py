"""yt_overlay.py: PASS 2 of a YouTube-look sample: the OVERLAY layer (captions, hook title, watermark) as a HyperFrames
composition with a transparent background (README § 5, § 6) -> <job>/yt/hf-overlay/index.html (+ fonts/, vendor/).

  python presets/youtube-shorts/onyx-samples-youtube/kit/yt_overlay.py projects/<job>
  cd projects/<job>/yt/hf-overlay && npx --yes hyperframes@0.8.16 render . --format mov --fps <fps> -o ../work/overlay.mov

Reads `<job>/yt/spec.json` → "hook": {"lines": ["SMALL WHITE LINE", "BIG GRADIENT LINE"], "caps": [49, 75], "y": [1357, 1442],
"max_w": 840} and "watermark": "SHOW NAME" (+ optional "watermark_y", centre px, default 1160: lower it when the captions sit low, ig_capy.py), plus `<job>/yt/captions.json` (yt_captions.py). The hook slides in from the left
over ~0.46 s, holds, slides out over ~0.88 s and is gone by ~3.2 s, with per-frame horizontal motion blur; every timeline
step sits a quarter frame before its frame boundary (exact boundaries round a third of them a frame late).
"""
import json, os, shutil, sys
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
    lines = hook.get("lines", [])
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

    out = os.path.join(job, "yt", "hf-overlay")
    os.makedirs(os.path.join(out, "fonts"), exist_ok=True)
    os.makedirs(os.path.join(out, "vendor"), exist_ok=True)
    for fn in ("Anton-Regular.ttf", "Montserrat-VF.ttf"):
        shutil.copy(os.path.join(KIT, "fonts", fn), os.path.join(out, "fonts", fn))
    shutil.copy(os.path.join(KIT, "vendor", "gsap.min.js"), os.path.join(out, "vendor", "gsap.min.js"))
    kit_css = open(os.path.join(KIT, "yt-captions.css"), encoding="utf-8").read()
    kit_js = open(os.path.join(KIT, "yt-captions.js"), encoding="utf-8").read()
    chunks = [dict(text=c["text"], start=c["start"], end=c["end"], voice=c["voice"], wipe=c["wipe"], **({"y": c["y"]} if "y" in c else {}),
                   **({"moves": c["moves"]} if c.get("moves") else {}))     # ig_capy.py: [frame, y] on a cut inside the chunk
              for c in cap["chunks"]]
    hb = "\n".join(f'<filter id="hook-hb{i + 1}" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="{bv} 0"/></filter>'
                   for i, bv in enumerate(BLURS))
    hook_divs = "".join(
        f'<div id="hl{i + 1}" class="hl" style="top:{ys[i] - sizes[i] * 0.62:.0f}px;font-size:{sizes[i]}px;height:{sizes[i] * 1.3:.0f}px" '
        f'data-layout-allow-overflow><span class="stroke">{txt}</span><span class="fill">{txt}</span></div>' for i, txt in enumerate(lines))
    wm = spec.get("watermark", "")
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
#hl1 .fill {{ color: #FFFFFF; }}
#hl2 .fill {{ background: linear-gradient(180deg, #F39A10 0%, #F6B412 45%, #F7D428 100%); -webkit-background-clip: text; background-clip: text;
  color: transparent; }}
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
  ytCaptions(tl, "#caps", {json.dumps(chunks, ensure_ascii=False)}, {{ fps: {fps} }});
  {json.dumps(steps)}.forEach(([t, x, b]) => {{
    tl.set("#hook", {{ x: x, filter: b ? "url(#hook-hb" + b + ")" : "none" }}, t);
  }});
  tl.set("#hook", {{ autoAlpha: 0 }}, {hide_t});
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
