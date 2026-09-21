#!/usr/bin/env python
"""Abundance Wisdom caption layer builder.

Renders the caption layer the way the creator's Premiere export looks (see README.md §8):
Gretaros ALL CAPS, cap height ~39 px, line 1 centred at y1149, per-word vertical gradients,
"Revised Light pop" growth, wall-to-wall captions, BLACK background (the AE side drops the
black with Deep Glow → Unmult, after the creator's CapCut motion-blur pass).

usage:
  python build.py calibrate                      # font size + tracking check against the reference
  python build.py render <plan.json> <out.mov>   # render the caption layer
"""
import json, os, subprocess, sys
from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1920
FPS = 60
FONT = r'C:/Users/affan/AppData/Local/Microsoft/Windows/Fonts/Gretaros-Regular.otf'

# measured off the creator's own caption export (Caption Exports/wacko.mov):
# cap height 39 px, and two known strings ("YOU SHOULD NOT SAY" = 634 px,
# "REALLY DON'T KNOW" = 603 px) solve to size 52 / tracking -0.5.
FONT_SIZE = 52             # pt, gives a 39 px cap height
CAP_HEIGHT = 39.0
LINE1_TOP = 1129           # top of line 1 glyphs
LINE_PITCH = 59            # second line sits this far below the first
TRACKING = -0.5            # extra px between characters
ITALIC_SHEAR = 0.20        # faux italic: Gretaros ships Regular only

# vertical gradients, top colour -> bottom colour (README §8)
STYLES = {
    'white':   ((255, 255, 255), (255, 255, 255)),
    'red':     ((0xCC, 0x1B, 0x1E), (0xF4, 0x71, 0x72)),
    'magenta': ((0xCC, 0x14, 0xD9), (0xF1, 0x4D, 0xF7)),
    'yellow':  ((0xDD, 0x89, 0x00), (0xF7, 0xE2, 0x00)),
    'cyan':    ((0x00, 0x78, 0x8E), (0x44, 0xD1, 0xE3)),
}
# the creator's own style names
STYLES['pink'] = STYLES['magenta']      # "Pink Shade"
STYLES['blue'] = STYLES['cyan']         # "Light Blue Shade"
STYLES['red'] = STYLES['red']           # "Red Shade Greators"

# "Revised Light pop", MEASURED off the creator's caption export frame by frame (2026-09-21):
# the type grows steadily toward the preset's 112 %, most of it inside the first half second.
# (The nominal preset is Scale 100 -> 105 @0.05 s -> 112 @0.367 s; on screen it arrives slower,
# so these are the observed values, linearly interpolated.)
POP = [(0.000, 1.000), (0.050, 1.016), (0.100, 1.027), (0.150, 1.042), (0.200, 1.053),
       (0.250, 1.056), (0.300, 1.061), (0.350, 1.065), (0.400, 1.070), (0.500, 1.080),
       (0.600, 1.090), (0.800, 1.103), (1.000, 1.112), (1.400, 1.120)]


def pop_scale(t):
    if t <= POP[0][0]:
        return POP[0][1]
    for (t0, s0), (t1, s1) in zip(POP, POP[1:]):
        if t <= t1:
            return s0 + (s1 - s0) * (t - t0) / (t1 - t0)
    return POP[-1][1]


def font_at(scale=1.0):
    """The caption font at `scale` (the pop animation scales the type itself)."""
    return ImageFont.truetype(FONT, max(1, int(round(FONT_SIZE * scale))))


def word_width(font, text, tracking):
    w = font.getlength(text)
    return w + tracking * max(0, len(text) - 1)


def gradient_text(draw_img, words, font, tracking, cx, top, italic):
    """Draw one line of (text, style) words centred on cx, glyph tops at `top`."""
    space = font.getlength(' ') + tracking
    widths = [word_width(font, w.upper(), tracking) for w, _ in words]
    total = sum(widths) + space * (len(words) - 1)
    x = cx - total / 2
    box = font.getbbox('H')
    cap_h = box[3] - box[1]
    for (text, style), wdt in zip(words, widths):
        text = text.upper()
        layer = Image.new('RGBA', (int(wdt) + 80, int(cap_h * 2.4) + 80), (0, 0, 0, 0))
        d = ImageDraw.Draw(layer)
        cx0, cy0 = 40, 40
        base_y = cy0 + cap_h          # every character sits on ONE baseline, so commas
        if tracking:                  # and full stops stay down where they belong
            cur = cx0
            for ch in text:
                d.text((cur, base_y), ch, font=font, fill=(255, 255, 255, 255), anchor='ls')
                cur += font.getlength(ch) + tracking
        else:
            d.text((cx0, base_y), text, font=font, fill=(255, 255, 255, 255), anchor='ls')

        # paint the vertical gradient through the glyph alpha
        c_top, c_bot = STYLES[style]
        bbox = layer.getbbox()
        glyph_top = bbox[1] if bbox else 40
        if bbox:
            g_top, g_bot = bbox[1], bbox[3]
            grad = Image.new('RGBA', layer.size, (0, 0, 0, 0))
            gd = ImageDraw.Draw(grad)
            span = max(1, g_bot - g_top)
            for yy in range(g_top, g_bot):
                u = (yy - g_top) / span
                col = tuple(int(c_top[i] + (c_bot[i] - c_top[i]) * u) for i in range(3))
                gd.line([(0, yy), (layer.size[0], yy)], fill=col + (255,))
            grad.putalpha(layer.getchannel('A'))
            layer = grad

        if italic:
            wpx, hpx = layer.size
            layer = layer.transform((wpx + int(hpx * ITALIC_SHEAR), hpx), Image.AFFINE,
                                    (1, ITALIC_SHEAR, -ITALIC_SHEAR * hpx, 0, 1, 0),
                                    resample=Image.BICUBIC)
        # align the real glyph top (not the font's nominal box) to `top`
        draw_img.alpha_composite(layer, (int(round(x)) - 40, int(round(top)) - glyph_top))
        x += wdt + space


def render(plan_path, out_path, animate=True):
    """animate=False renders the captions static (no pop), for applying a preset by hand."""
    plan = json.load(open(plan_path, encoding='utf-8'))
    caps = plan['captions']
    duration = plan['duration']
    tracking = plan.get('tracking', TRACKING)
    frames = int(round(duration * FPS))

    tmp = os.path.join(os.path.dirname(os.path.abspath(out_path)), '_capframes')
    os.makedirs(tmp, exist_ok=True)
    for f in os.listdir(tmp):
        os.remove(os.path.join(tmp, f))

    for i in range(frames):
        t = i / FPS
        img = Image.new('RGBA', (W, H), (0, 0, 0, 255))
        cur = next((c for c in caps if c['start'] <= t < c['end']), None)
        if cur:
            s = pop_scale(t - cur['start']) if animate else 1.0
            font = font_at(s)
            lines = cur['lines']
            block_h = LINE_PITCH * (len(lines) - 1)
            top0 = LINE1_TOP - block_h / 2 if len(lines) > 1 else LINE1_TOP
            for li, line in enumerate(lines):
                words = [(w['t'], w.get('c', 'white')) for w in line]
                gradient_text(img, words, font, tracking * s,
                              W / 2, top0 + li * LINE_PITCH, cur.get('italic', False))
        img.convert('RGB').save(os.path.join(tmp, 'f%05d.png' % i))

    subprocess.run(['ffmpeg', '-hide_banner', '-loglevel', 'error', '-y', '-framerate', str(FPS),
                    '-i', os.path.join(tmp, 'f%05d.png'), '-c:v', 'libx264', '-preset', 'slow',
                    '-crf', '14', '-pix_fmt', 'yuv420p', '-r', str(FPS), out_path], check=True)
    print('rendered', out_path, frames, 'frames')


def calibrate():
    """Check size/tracking against strings measured in the creator's own export."""
    font = font_at(1.0)
    box = font.getbbox('H')
    print('font size %d -> cap height %d px (creator: %d)' % (FONT_SIZE, box[3] - box[1], CAP_HEIGHT))
    for text, target in (('YOU SHOULD NOT SAY', 634), ("REALLY DON'T KNOW", 603)):
        w = word_width(font, text, TRACKING)
        print('  %-20s %6.1f px  (creator %d, off by %+.1f)' % (text, w, target, w - target))


def still(text_json, out_png, scale=1.0):
    """Render one caption as a still, for comparing against a reference frame."""
    spec = json.loads(text_json)
    img = Image.new('RGBA', (W, H), (0, 0, 0, 255))
    font = font_at(scale)
    lines = spec['lines']
    block_h = LINE_PITCH * (len(lines) - 1)
    top0 = LINE1_TOP - block_h / 2 if len(lines) > 1 else LINE1_TOP
    for li, line in enumerate(lines):
        words = [(w['t'], w.get('c', 'white')) for w in line]
        gradient_text(img, words, font, TRACKING * scale, W / 2, top0 + li * LINE_PITCH,
                      spec.get('italic', False))
    img.convert('RGB').save(out_png)
    print('wrote', out_png)


if __name__ == '__main__':
    if sys.argv[1] == 'calibrate':
        calibrate()
    elif sys.argv[1] == 'still':
        still(sys.argv[2], sys.argv[3], float(sys.argv[4]) if len(sys.argv) > 4 else 1.0)
    else:
        render(sys.argv[2], sys.argv[3], animate='static' not in sys.argv[4:])
