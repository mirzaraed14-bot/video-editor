"""Abundance Wisdom subscribe CTA (Affan 2026-11-03: "a subtle CTA that plays along the video here and there, like if it's
a 40 second video two times is fine ... and the subscribe call to action at the end ... a blank screen ... this cool
animation of telling people to subscribe if they want more ... in our own aesthetic so it doesn't stand out like a sore
thumb"). The channel was at 540K, going for the 1M play button.

Both graphics are in HIS look: Gretaros caps, his caption glow stack (Deep Glow fitted on AE renders,
projects/aw-code-trial-parents/fit/glow.json + Bevel Alpha + the two hard drop shadows), his Red Shade (#DB4649) and the
caption gold (finish.py GOLD), motion from the label card (rise in, eased cubic, rise out).

  mid  2.8 s, transparent. A small red SUBSCRIBE pill (bell + word) with a soft red glow rises in at the low band (centre
       y 1392: under the caption line, where the labels live, above the bottom 300 px), a cursor glides in and taps it, the
       pill FLARES red (his review v1: "glow when the button clicks ... glows in red and it has this hue"), turns to a grey
       SUBSCRIBED while the bell rings and the hue dies, the cursor leaves, the pill rises out.
  end  4.0 s, opaque black: "Road to 1M" (his review v1 rejected the text-and-button card: research first, then a concept).
       See end_frame().

CLI (uv run -q --with numpy --with pillow --with opencv-python-headless python cta.py ...):
  render [--fps 60] [--subs 540000] [--only mid|end] [--out DIR, default E:/Shorts/Abudance Wisdom Shorts Exports/CTA]
         -> aw-cta-mid-<fps>.mov (ProRes 4444, straight alpha), aw-cta-end-<fps>.mov (ProRes 422 HQ),
            aw-cta-mid-sfx.wav, aw-cta-end-sfx.wav (48 kHz, cue crest on the motion's fastest frame)
  sheet  [--out DIR]  -> aw-cta-sheet-mid.png / -end.png (frames of both, the mid over a dark grey so the alpha reads)
In a code build:  sys.path.insert(0, <this folder>); import cta; cta.SUBS = <his count>; cta.FPS = <fps>
                  rgb, a = cta.frame('mid', u, cy=1392)   # numpy float32, rgb PREMULTIPLIED, u = seconds into the graphic
                  out = rgb + img * (1 - a[..., None])
"""
import math, os, subprocess, sys
import numpy as np
import cv2
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
W, H = 1080, 1920
FONT = r'C:/Users/affan/AppData/Local/Microsoft/Windows/Fonts/Gretaros-Regular.otf'   # his caption face
CAP_RATIO = 0.735                                   # Gretaros cap height / em (measured: 'H' 147 px at size 200)
GOLD = ((255, 107, 0), (250, 197, 4))               # his caption yellow (finish.py), top -> bottom
RED = ((236, 92, 96), (196, 50, 56))                # Red Shade Greators (#DB4649 mid), top -> bottom
GREY = (40, 40, 40)                                 # the SUBSCRIBED state
# his Deep Glow (fit/glow.json): glow = sum w_i blur(src, r_i * scale / 2), out = premult + EXP * glow, alpha = max channel
GLOW_W = [0.1067, 0.8237, 0.5537, 0.1757, 0.2262, 0.0, 0.0]
GLOW_R = [250 * 2 ** -i for i in range(7)]
GLOW_EXP, GLOW_THR, BEVEL = 0.976, 0.578, 0.333
DUR = {'mid': 2.8, 'end': 4.0}
SUBS = 540000                                       # his count on 2026-11-03 (render --subs N to update)
FPS = 60                                            # set by render(); the counter's motion blur samples inside one frame
SFX_DIR = os.path.join(HERE, 'sfx')                # two slices of his approved Patron swish set (patron-20000-cases/yt/sfx)
SS = 2                                              # supersample for every drawn sprite
OUT_DIR = r'E:/Shorts/Abudance Wisdom Shorts Exports/CTA'   # renders live here (beside Final Renders), never in git


# ------------------------------------------------------------------------------------------------------------- easing
def clamp01(u):
    return min(max(u, 0.0), 1.0)


def ease_out(u):
    u = clamp01(u)
    return 1 - (1 - u) ** 3


def ease_in(u):
    u = clamp01(u)
    return u ** 3


def ease_io(u):
    u = clamp01(u)
    return 4 * u ** 3 if u < 0.5 else 1 - (-2 * u + 2) ** 3 / 2


def back_out(u, c1=1.4):
    u = clamp01(u)
    c3 = c1 + 1
    return 1 + c3 * (u - 1) ** 3 + c1 * (u - 1) ** 2


# ------------------------------------------------------------------------------------------------------------- filters
def blur(x, sigma):
    if sigma < 0.6:
        return x
    h, w = x.shape[:2]
    f = int(min(8, max(1, sigma // 4)))
    if f > 1 and h // f > 4 and w // f > 4:         # big radii on a downsampled copy (his Deep Glow downsamples too)
        s = cv2.resize(x, (w // f, h // f), interpolation=cv2.INTER_AREA)
        s = cv2.GaussianBlur(s, (0, 0), sigma / f)
        return cv2.resize(s, (w, h), interpolation=cv2.INTER_LINEAR)
    return cv2.GaussianBlur(x, (0, 0), sigma)


def shift(a, dx, dy):
    M = np.float32([[1, 0, dx], [0, 1, dy]])
    return cv2.warpAffine(a, M, (a.shape[1], a.shape[0]), flags=cv2.INTER_LINEAR, borderValue=0)


def glow(P, A, scale, gain=1.0):
    """his Deep Glow on a premultiplied sprite: the bright part (max channel over the threshold) blurred at seven radii."""
    lum = P.max(-1)
    k = np.clip((lum - (GLOW_THR - 0.03)) / 0.06, 0, 1)
    k = k * k * (3 - 2 * k)
    src = P * k[..., None]
    g = sum(w * blur(src, r * scale / 2.0) for w, r in zip(GLOW_W, GLOW_R) if w > 0)
    out = np.clip(P + GLOW_EXP * gain * g, 0, 1)
    return out, np.maximum(A, out.max(-1))


def bevel(P, A, edge):
    th = math.radians(-60.0)
    lx, ly = math.sin(th), -math.cos(th)
    b = blur(A, max(edge / 2, 0.5))
    gx = np.zeros_like(b); gy = np.zeros_like(b)
    gx[:, 1:-1] = (b[:, 2:] - b[:, :-2]) / 2
    gy[1:-1] = (b[2:] - b[:-2]) / 2
    shade = -(gx * lx + gy * ly) * edge * BEVEL * 2
    return np.clip(P + shade[..., None] * A[..., None], 0, 1), A


def hard_shadow(P, A, dist):
    d = dist * math.sin(math.radians(135.0))        # direction 135: down-right, softness 0 (his two stacked Drop Shadows)
    s = shift(A, d, d)
    return P, A + s * (1 - A)


def soft_shadow(P, A, sigma, op, dx, dy):
    s = shift(blur(A, sigma), dx, dy) * op
    return P, A + s * (1 - A)


def caption_stack(P, A, scale=0.5, dist=12.0, gain=1.0):
    """the stack his captions carry (README § 8: Deep Glow, Bevel Alpha 2.4, 2 x Drop Shadow at distance 12 in 4K = 6 px)."""
    P, A = glow(P, A, scale, gain)
    P, A = bevel(P, A, 2.4 * scale)
    P, A = hard_shadow(P, A, dist * scale)
    return hard_shadow(P, A, dist * scale)


# ------------------------------------------------------------------------------------------------------------- sprites
class Sprite:
    """premultiplied rgb (h, w, 3) + alpha (h, w); (ax, ay) = the sprite pixel that sits on the placement point."""
    def __init__(self, P, A, ax, ay):
        self.P, self.A, self.ax, self.ay = P.astype(np.float32), A.astype(np.float32), ax, ay


def down(arr):
    """SS-times supersampled array -> 1x."""
    h, w = arr.shape[:2]
    return cv2.resize(arr, (w // SS, h // SS), interpolation=cv2.INTER_AREA)


def vgrad(c0, c1, h, y0, y1):
    """(h, 1, 3) vertical gradient c0 -> c1 between rows y0 and y1 (0-1 floats)."""
    t = np.clip((np.arange(h, dtype=np.float32) - y0) / max(y1 - y0, 1), 0, 1)[:, None]
    return (np.array(c0, np.float32)[None] + (np.array(c1, np.float32) - np.array(c0, np.float32))[None] * t)[:, None, :] / 255


_FONTS = {}


def font(cap):
    key = round(cap * SS)
    if key not in _FONTS:
        _FONTS[key] = ImageFont.truetype(FONT, int(round(cap * SS / CAP_RATIO)))
    return _FONTS[key]


def text_width(text, cap, track):
    f = font(cap)
    return (sum(f.getlength(ch) for ch in text) + track * SS * (len(text) - 1)) / SS


def text_sprite(segments, cap, track, pad=12, stack=None):
    """segments = [(text, 'white' | 'gold')]; anchor = left end of the cap line, cap-centre height."""
    f = font(cap)
    full = ''.join(s for s, _ in segments)
    tw = text_width(full, cap, track)
    w, h = int(math.ceil(tw + 2 * pad)), int(math.ceil(cap * 1.6 + 2 * pad))
    base = pad + cap * 1.3                          # baseline row (1x)
    m = {c: Image.new('L', (w * SS, h * SS), 0) for c in ('white', 'gold')}
    x = pad * SS
    for s, c in segments:
        d = ImageDraw.Draw(m[c])
        for ch in s:
            d.text((x, base * SS), ch, font=f, fill=255, anchor='ls')
            x += f.getlength(ch) + track * SS
    mw = down(np.asarray(m['white'], np.float32) / 255)
    mg = down(np.asarray(m['gold'], np.float32) / 255)
    gold = vgrad(GOLD[0], GOLD[1], h, base - cap, base)
    P = mw[..., None] * 1.0 + mg[..., None] * gold
    A = np.maximum(mw, mg)
    ay = base - cap / 2
    if stack:
        P, A, ax, ay = padded(P, A, pad, ay, stack['pad'])
        P, A = stack['fn'](P, A)
    else:
        ax = pad
    return Sprite(P, A, ax, ay), tw


def padded(P, A, ax, ay, p):
    P2 = np.zeros((P.shape[0] + 2 * p, P.shape[1] + 2 * p, 3), np.float32); P2[p:-p, p:-p] = P
    A2 = np.zeros((A.shape[0] + 2 * p, A.shape[1] + 2 * p), np.float32); A2[p:-p, p:-p] = A
    return P2, A2, ax + p, ay + p


def rrect_mask(w, h, r, inset=0.0):
    im = Image.new('L', (int(math.ceil(w * SS)), int(math.ceil(h * SS))), 0)
    i = inset * SS
    ImageDraw.Draw(im).rounded_rectangle([i, i, w * SS - 1 - i, h * SS - 1 - i], radius=max(r * SS - i, 1), fill=255)
    return down(np.asarray(im, np.float32) / 255)


def pill_sprite(w, h, mix, pad=24):
    """the button: Red Shade gradient (mix 0) -> grey SUBSCRIBED with a faint white rim (mix 1), soft shadow under it."""
    m = rrect_mask(w, h, h / 2)
    rim = np.clip(m - rrect_mask(w, h, h / 2, inset=1.6), 0, 1)
    red = vgrad(RED[0], RED[1], m.shape[0], 0, m.shape[0]) * np.ones((1, m.shape[1], 1), np.float32)
    grey = np.array(GREY, np.float32)[None, None] / 255 * np.ones_like(red)
    a_fill = m * (1 - mix) + m * 0.86 * mix
    col = red * (1 - mix) + grey * mix
    P = col * a_fill[..., None]
    A = a_fill.copy()
    ra = rim * 0.30 * mix                           # the rim only on the grey state
    P = P * (1 - ra[..., None]) + ra[..., None]
    A = A + ra * (1 - A)
    P, A, ax, ay = padded(P, A, 0, 0, pad)
    P, A = soft_shadow(P, A, 8.0, 0.55, 0, 5)
    return Sprite(P, A, ax, ay)                     # anchor = the pill's top-left corner


def bell_sprite(s, pad=10):
    """a plain white bell, s px tall; anchor = the pivot at its top knob (it rings about that point)."""
    S = s * SS
    w, h = int(S * 1.1) + 2 * pad * SS, int(S * 1.35) + 2 * pad * SS
    im = Image.new('L', (w, h), 0); d = ImageDraw.Draw(im)
    cx, top = w / 2, pad * SS + S * 0.10
    pts_l, pts_r = [], []
    for i in range(41):
        t = i / 40
        if t < 0.32:
            hw = 0.31 * math.sqrt(max(0.0, 1 - ((0.32 - t) / 0.32) ** 2))
        elif t < 0.84:
            hw = 0.31 + 0.06 * ((t - 0.32) / 0.52) ** 2
        else:
            hw = 0.37 + 0.11 * ((t - 0.84) / 0.16)
        y = top + t * S * 0.86
        pts_l.append((cx - hw * S, y)); pts_r.append((cx + hw * S, y))
    d.polygon(pts_l + pts_r[::-1], fill=255)
    yb = top + S * 0.86
    d.rounded_rectangle([cx - 0.50 * S, yb - 0.02 * S, cx + 0.50 * S, yb + 0.07 * S], radius=0.035 * S, fill=255)
    d.ellipse([cx - 0.07 * S, top - 0.10 * S, cx + 0.07 * S, top + 0.04 * S], fill=255)
    d.ellipse([cx - 0.11 * S, yb + 0.09 * S, cx + 0.11 * S, yb + 0.27 * S], fill=255)
    A = down(np.asarray(im, np.float32) / 255)
    P = np.repeat(A[..., None], 3, -1)
    return Sprite(P, A, w / 2 / SS, (top - 0.03 * S) / SS)


def cursor_sprite(s, pad=20):
    """the arrow pointer, s px tall: white with a thin dark edge and a soft shadow; anchor = the tip."""
    k = s / 19.2 * SS
    pts = [(0, 0), (0, 16.6), (4.2, 12.7), (7.0, 19.2), (9.7, 18.1), (6.9, 11.7), (12.6, 11.7)]
    o = pad * SS
    w, h = int(13 * k + 2 * o), int(19.5 * k + 2 * o)
    fill = Image.new('L', (w, h), 0); edge = Image.new('L', (w, h), 0)
    xy = [(o + x * k, o + y * k) for x, y in pts]
    ImageDraw.Draw(edge).polygon(xy, fill=255, outline=255, width=int(2.2 * SS))
    ImageDraw.Draw(fill).polygon(xy, fill=255)
    fe = ImageDraw.Draw(fill)
    fe.line(xy + [xy[0]], fill=0, width=int(2.2 * SS))   # carve the edge out of the fill: white body, dark rim
    Af, Ae = down(np.asarray(fill, np.float32) / 255), down(np.asarray(edge, np.float32) / 255)
    P = np.repeat(Af[..., None], 3, -1) * 0.97 + np.repeat((Ae - Af).clip(0, 1)[..., None], 3, -1) * 0.08
    A = np.maximum(Ae, Af)
    P, A = soft_shadow(P, A, 5.0, 0.5, 3, 5)
    return Sprite(P, A, o / SS, o / SS)


def ring_sprite(r, width, op, col=GOLD[1]):
    p = int(r + 60)
    im = Image.new('L', (2 * p * SS, 2 * p * SS), 0)
    c = p * SS
    ImageDraw.Draw(im).ellipse([c - r * SS, c - r * SS, c + r * SS, c + r * SS], outline=255, width=max(1, int(width * SS)))
    A = down(np.asarray(im, np.float32) / 255) * op
    P = A[..., None] * (np.array(col, np.float32) / 255)[None, None]
    P, A = glow(P, A, 0.30, 0.55)
    return Sprite(P, A, p, p)


# ------------------------------------------------------------------------------------------------------------- compositing
def blit(P, A, s, x, y, op=1.0, scale=1.0, rot=0.0):
    """composite sprite s with its anchor on (x, y), scaled and rotated (degrees, clockwise) about the anchor."""
    if op <= 0.002:
        return
    c, si = math.cos(math.radians(rot)) * scale, math.sin(math.radians(rot)) * scale
    h, w = s.A.shape
    corners = np.array([[0, 0], [w, 0], [0, h], [w, h]], np.float32) - [s.ax, s.ay]
    pts = np.stack([corners[:, 0] * c - corners[:, 1] * si, corners[:, 0] * si + corners[:, 1] * c], 1) + [x, y]
    x0, y0 = int(max(0, math.floor(pts[:, 0].min()) - 1)), int(max(0, math.floor(pts[:, 1].min()) - 1))
    x1, y1 = int(min(W, math.ceil(pts[:, 0].max()) + 1)), int(min(H, math.ceil(pts[:, 1].max()) + 1))
    if x1 <= x0 or y1 <= y0:
        return
    M = np.float32([[c, -si, x - x0 - (c * s.ax - si * s.ay)], [si, c, y - y0 - (si * s.ax + c * s.ay)]])
    sz = (x1 - x0, y1 - y0)
    p = cv2.warpAffine(s.P, M, sz, flags=cv2.INTER_LINEAR, borderValue=0) * op
    a = cv2.warpAffine(s.A, M, sz, flags=cv2.INTER_LINEAR, borderValue=0) * op
    P[y0:y1, x0:x1] = p + P[y0:y1, x0:x1] * (1 - a[..., None])
    A[y0:y1, x0:x1] = a + A[y0:y1, x0:x1] * (1 - a)


# ------------------------------------------------------------------------------------------------------------- the button
class Button:
    """the SUBSCRIBE -> SUBSCRIBED pill, sized by its cap height. It carries his Deep Glow in Red Shade (Affan 2026-11-03:
    "more glowy ... when the button clicks ... the button glows in red and it has this hue to it"): a soft red hue while it
    says SUBSCRIBE, a flare on the click, the hue dying into the grey SUBSCRIBED."""
    def __init__(self, cap, gscale):
        self.cap, self.h, self.gscale = cap, round(cap * 2.7), gscale
        self.pad_l, self.pad_r, self.gap, self.bell_s = cap * 0.95, cap * 1.05, cap * 0.50, cap * 1.12
        self.track = cap * 0.10
        tglow = {'pad': 40, 'fn': lambda P, A: glow(P, A, 0.25, 0.6)}
        self.t1, self.w1 = text_sprite([('SUBSCRIBE', 'white')], cap, self.track, stack=tglow)
        self.t2, self.w2 = text_sprite([('SUBSCRIBED', 'white')], cap, self.track, stack=tglow)
        self.bell = bell_sprite(self.bell_s)
        self.halo_soft = self._halo(gscale, 1.0)
        self.halo_flare = self._halo(gscale * 1.9, 1.5)
        self.cache = {}

    def _halo(self, scale, gain):
        w, h = self.width(0), self.h
        m = rrect_mask(w, h, h / 2)
        red = vgrad(RED[0], RED[1], m.shape[0], 0, m.shape[0]) * np.ones((1, m.shape[1], 1), np.float32)
        P, A, ax, ay = padded(red * m[..., None], m, 0, 0, int(scale * 260) + 30)
        P, A = glow(P, A, scale, gain)
        return Sprite(P, A, ax, ay)

    def width(self, mix):
        tw = self.w1 + (self.w2 - self.w1) * mix
        return self.pad_l + self.bell_s + self.gap + tw + self.pad_r

    def pill(self, mix):
        key = round(mix, 2)
        if key not in self.cache:
            self.cache[key] = pill_sprite(self.width(key), self.h, key)
        return self.cache[key]

    def draw(self, P, A, cx, cy, op=1.0, scale=1.0, mix=0.0, ring_deg=0.0, hue=0.0, flare=0.0):
        """the pill centred on (cx, cy); everything scales about that centre."""
        w = self.width(mix)
        w0 = self.width(0)
        for halo, k in ((self.halo_soft, hue), (self.halo_flare, flare)):
            if k > 0.01:
                blit(P, A, halo, cx - w0 / 2 * scale, cy - self.h / 2 * scale, op * min(k, 1.0), scale)
        pl = self.pill(mix)
        blit(P, A, pl, cx - w / 2 * scale, cy - self.h / 2 * scale, op, scale)
        bx = cx + (-w / 2 + self.pad_l + self.bell_s / 2) * scale
        by = cy + (-self.bell_s * 0.52) * scale
        blit(P, A, self.bell, bx, by, op, scale, ring_deg)
        tx = cx + (-w / 2 + self.pad_l + self.bell_s + self.gap) * scale
        blit(P, A, self.t1, tx, cy, op * (1 - mix), scale)
        blit(P, A, self.t2, tx, cy, op * mix, scale)
        return w

    def tap_point(self, cx, cy):
        return cx + self.width(0) * 0.20, cy + self.h * 0.18


def ring_angle(u):
    """the bell rings: a damped swing, 3 swings over 0.7 s."""
    if u <= 0 or u > 0.8:
        return 0.0
    return 16.0 * math.sin(2 * math.pi * 3.6 * u) * math.exp(-4.0 * u)


def red_glow(u, t_on, t_tap):
    """(hue, flare): the soft red hue comes up with the pill, flares on the click, then dies into the grey state."""
    hue = 0.9 * ease_out((u - t_on) / 0.45)
    v = u - t_tap
    if v <= 0:
        return hue, 0.0
    flare = clamp01(v / 0.06) * math.exp(-max(v - 0.06, 0.0) / 0.24)
    return hue * (1 - ease_out((v - 0.08) / 0.6)), flare


def tap_sequence(P, A, btn, cx, cy, u, t_in, t_tap, t_out, cur, ring_r):
    """cursor glides in (t_in -> t_tap - 0.05), taps (t_tap), the pill flips + the bell rings + a red ring, cursor leaves."""
    tx, ty = btn.tap_point(cx, cy)
    mix = ease_out((u - t_tap - 0.10) / 0.22)       # the red holds through the flare, then turns grey
    v = (u - t_tap)
    if v > 0:
        rr = ring_r * ease_out(v / 0.5)
        rop = 0.9 * (1 - clamp01(v / 0.5))
        if rop > 0.01 and rr > 2:
            blit(P, A, ring_sprite(rr, 3.0, rop, RED[0]), tx, ty)
    # the cursor: in along a soft curve, a press (scale 0.86) on the tap, out down-right
    if t_in <= u < t_out + 0.35:
        if u < t_tap - 0.05:
            e = ease_io((u - t_in) / (t_tap - 0.05 - t_in))
            x = tx + (1 - e) * 250 + math.sin(e * math.pi) * 20
            y = ty + (1 - e) * 210
            op = clamp01((u - t_in) / 0.15)
        elif u < t_out:
            x, y, op = tx, ty, 1.0
        else:
            e = ease_in((u - t_out) / 0.35)
            x, y, op = tx + e * 200, ty + e * 170, 1 - e
        press = 1.0
        if t_tap - 0.05 <= u < t_tap + 0.15:
            k = (u - (t_tap - 0.05)) / 0.20
            press = 1 - 0.14 * math.sin(math.pi * k)
        return mix, ring_angle(u - t_tap - 0.04), (cur, x, y, op, press)
    return mix, ring_angle(u - t_tap - 0.04), None


# ------------------------------------------------------------------------------------------------------------- the plaque
FW, FH = 400, 300                                   # the gold play button plaque, face size at rest (px)
PLQ = (540.0, 770.0)                                # its centre on the end screen


def ramp(t, stops):
    t = np.clip(t, 0, 1)
    xs = np.array([s for s, _ in stops], np.float32)
    out = np.stack([np.interp(t, xs, np.array([c[k] for _, c in stops], np.float32)) for k in range(3)], -1)
    return out / 255


METAL = [(0.0, (112, 70, 14)), (0.20, (204, 150, 48)), (0.40, (255, 228, 146)), (0.52, (214, 160, 58)),
         (0.76, (126, 80, 16)), (1.0, (192, 140, 46))]


def plaque_face():
    """the face texture (premultiplied, alpha): brushed gold, a recessed panel, the raised play emblem with its triangle cut
    in, ABUNDANCE WISDOM engraved under it. His 1M plaque, before he has it."""
    rng = np.random.default_rng(3)
    Y, X = np.mgrid[0:FH, 0:FW].astype(np.float32)
    brush = cv2.blur(rng.standard_normal((FH, FW)).astype(np.float32), (71, 1)) * 0.10
    m = rrect_mask(FW, FH, 26)
    col = ramp((X * 0.45 + Y) / (FH + FW * 0.45) + brush, METAL)
    # recessed panel 16 px in: a touch darker, lit from the top-left (a groove, not a bevel)
    panel = np.zeros_like(m)
    pm = rrect_mask(FW - 32, FH - 32, 16); panel[16:16 + pm.shape[0], 16:16 + pm.shape[1]] = pm
    col = col * (1 - 0.12 * panel[..., None])
    b = blur(panel, 2.0)
    gx = np.zeros_like(b); gy = np.zeros_like(b)
    gx[:, 1:-1] = (b[:, 2:] - b[:, :-2]) / 2; gy[1:-1] = (b[2:] - b[:-2]) / 2
    col = np.clip(col + (gx + gy)[..., None] * 1.6, 0, 1)                    # dark top-left lip, light bottom-right
    # the emblem: a raised, polished rounded rectangle with the play triangle cut in
    ew, eh = 156, 110
    ex, ey = (FW - ew) // 2, int(FH * 0.40 - eh / 2)
    em = np.zeros_like(m); e1 = rrect_mask(ew, eh, 32); em[ey:ey + e1.shape[0], ex:ex + e1.shape[1]] = e1
    tri = Image.new('L', (FW * SS, FH * SS), 0)
    cx, cy = FW / 2 + 4, ey + eh / 2
    ImageDraw.Draw(tri).polygon([((cx - 20) * SS, (cy - 27) * SS), ((cx - 20) * SS, (cy + 27) * SS), ((cx + 28) * SS, cy * SS)], fill=255)
    tm = down(np.asarray(tri, np.float32) / 255)
    shine = ramp((X * 0.45 + Y - ey) / (eh + FW * 0.2) * 0.8 + 0.25 + brush * 0.5, METAL)
    col = col * (1 - em[..., None]) + shine * em[..., None]
    for mask, k in ((em, 2.2), (tm, -1.8)):                                     # emblem raised, triangle sunk
        b = blur(mask, 1.6)
        gx = np.zeros_like(b); gy = np.zeros_like(b)
        gx[:, 1:-1] = (b[:, 2:] - b[:, :-2]) / 2; gy[1:-1] = (b[2:] - b[:-2]) / 2
        col = np.clip(col - (gx + gy)[..., None] * k, 0, 1)
    col = col * (1 - tm[..., None] * 0.45)
    # engraving
    f = font(15)
    txt = 'ABUNDANCE WISDOM'
    tw = text_width(txt, 15, 5)
    eng = Image.new('L', (FW * SS, FH * SS), 0); d = ImageDraw.Draw(eng)
    x = (FW - tw) / 2 * SS
    for ch in txt:
        d.text((x, (FH * 0.79 + 7) * SS), ch, font=f, fill=255, anchor='ls'); x += f.getlength(ch) + 5 * SS
    en = down(np.asarray(eng, np.float32) / 255)
    lit = shift(en, 0, 1.0)
    col = np.clip(col * (1 - en[..., None] * 0.55) + (lit - en).clip(0, 1)[..., None] * 0.35, 0, 1)
    return col * m[..., None], m


def plaque_layer(P, A, t_rot, shine, glow_gain, cx, cy):
    """the plaque turned t_rot degrees about its vertical axis, in perspective, with its gold edge showing; a shine band
    (shine = band centre along the face diagonal, None = none) and his Deep Glow on the bright gold."""
    S = sprites()
    face, fa = S['face']
    tex = face.copy()
    if shine is not None:
        Y, X = np.mgrid[0:FH, 0:FW].astype(np.float32)
        d = X * math.cos(math.radians(25)) + Y * math.sin(math.radians(25)) - shine
        band = np.exp(-(d / 34.0) ** 2) * 0.55 + np.exp(-(d / 9.0) ** 2) * 0.35
        tex = np.clip(tex + band[..., None] * fa[..., None] * np.array([1.0, 0.94, 0.78], np.float32), 0, 1)
    th = math.radians(t_rot)
    f, dep = 1500.0, 22.0

    def proj(x, y, z):
        xr, zr = x * math.cos(th) + z * math.sin(th), -x * math.sin(th) + z * math.cos(th)
        k = f / (f + zr)
        return cx + xr * k, cy + y * k

    hw, hh = FW / 2, FH / 2
    front = [proj(-hw, -hh, 0), proj(hw, -hh, 0), proj(hw, hh, 0), proj(-hw, hh, 0)]
    ex = hw if t_rot > 0 else -hw                   # the edge that turns toward camera shows its gold side
    side = [proj(ex, -hh + 10, 0), proj(ex, -hh + 10, dep), proj(ex, hh - 10, dep), proj(ex, hh - 10, 0)]
    pts = np.array(front + side, np.float32)
    x0, y0 = int(max(0, pts[:, 0].min() - 160)), int(max(0, pts[:, 1].min() - 160))
    x1, y1 = int(min(W, pts[:, 0].max() + 160)), int(min(H, pts[:, 1].max() + 160))
    lw, lh = x1 - x0, y1 - y0
    LP = np.zeros((lh, lw, 3), np.float32); LA = np.zeros((lh, lw), np.float32)
    if abs(t_rot) > 0.5:
        im = Image.new('L', (lw * SS, lh * SS), 0)
        ImageDraw.Draw(im).polygon([((x - x0) * SS, (y - y0) * SS) for x, y in side], fill=255)
        sm = down(np.asarray(im, np.float32) / 255)
        sh = 0.55 + 0.35 * abs(math.sin(th))
        LP = sm[..., None] * np.array([150, 102, 24], np.float32) / 255 * sh; LA = sm
    src = np.float32([[0, 0], [FW, 0], [FW, FH], [0, FH]])
    dst = np.float32([[x - x0, y - y0] for x, y in front])
    M = cv2.getPerspectiveTransform(src, dst)
    fp = cv2.warpPerspective(tex, M, (lw, lh), flags=cv2.INTER_LINEAR, borderValue=0)
    fa2 = cv2.warpPerspective(fa, M, (lw, lh), flags=cv2.INTER_LINEAR, borderValue=0)
    LP = fp + LP * (1 - fa2[..., None]); LA = fa2 + LA * (1 - fa2)
    LP, LA = glow(LP, LA, 0.35, glow_gain)
    P[y0:y1, x0:x1] = LP + P[y0:y1, x0:x1] * (1 - LA[..., None])
    A[y0:y1, x0:x1] = LA + A[y0:y1, x0:x1] * (1 - LA)


# ------------------------------------------------------------------------------------------------------------- the counter
CNT = (540.0, 1042.0)                               # the subscriber counter's centre
CNT_CAP = 84


def counter_value(u):
    """0 -> SUBS (fast, easing out: the funnel count, catalog FX-71), then +1 when the button is tapped."""
    n = SUBS * (1 - (1 - clamp01((u - 0.85) / 0.95)) ** 4)
    if u > END_TAP + 0.08:
        n = SUBS + ease_io((u - END_TAP - 0.08) / 0.30)
    return n


def counter_layer(P, A, u, op):
    """the odometer: each column rolls only while the column under it passes 9 -> 0; fast columns get real motion blur
    (5 sub-frame samples over half the frame time); leading zeros stay dim until the count reaches them; his caption stack."""
    S = sprites()
    digs, adv, cw, pitch = S['digits']
    ndig = len(str(SUBS + 1))
    cols = []                                        # (x offset of the column centre, place k) right to left
    x = 0.0
    for i in range(ndig):
        k = i
        if i and i % 3 == 0:
            x -= cw
            cols.append(('comma', x + cw / 2, k))
        x -= adv
        cols.append(('d', x + adv / 2, k))
    total = -x
    pad = 120
    lw, lh = int(total + 2 * pad), int(pitch + 2 * pad)
    acc = np.zeros((lh, lw), np.float32)
    ns = [counter_value(u + (s / 4 - 0.5) * 0.5 / FPS) for s in range(5)]
    for n in ns:
        L = np.zeros((lh, lw), np.float32)
        for kind, xc, k in cols:
            on = 0.28 + 0.72 * clamp01((n - 10 ** k * 0.95) / (10 ** k * 0.05)) if k else 1.0
            if kind == 'comma':
                g = digs[',']
                place(L, g, xc + total + pad, pad + pitch / 2, on)
                continue
            p = n / 10 ** k
            d = int(math.floor(p)) % 10
            if k == 0:
                fr = n - math.floor(n)
            else:
                rem = n - math.floor(n / 10 ** k) * 10 ** k
                fr = clamp01(rem - (10 ** k - 1))
            for dd, off in ((d, -fr), ((d + 1) % 10, 1 - fr)):
                if abs(off) < 1:
                    place(L, digs[str(dd)], xc + total + pad, pad + pitch / 2 + off * pitch, on)
        acc += L / len(ns)
    # a soft window: digits fade as they roll out above or below the line
    yy = np.arange(lh, dtype=np.float32)[:, None]
    acc *= np.clip((yy - (pad - 6)) / 22, 0, 1) * np.clip(((pad + pitch + 6) - yy) / 22, 0, 1)
    Pc = np.repeat(acc[..., None], 3, -1)
    Pc, Ac = caption_stack(Pc, acc, 0.5, 12.0, 0.9)
    spr = Sprite(Pc, Ac, pad + total / 2, pad + pitch / 2)
    blit(P, A, spr, CNT[0], CNT[1], op)


def place(L, g, xc, yc, op):
    """add glyph mask g (centred) into L at (xc, yc), subpixel, clipped."""
    if op <= 0:
        return
    h, w = g.shape
    M = np.float32([[1, 0, xc - w / 2], [0, 1, yc - h / 2]])
    L += cv2.warpAffine(g, M, (L.shape[1], L.shape[0]), flags=cv2.INTER_LINEAR, borderValue=0) * op


def digit_sprites(cap):
    f = font(cap)
    out = {}
    for ch in '0123456789,':
        w = int(f.getlength(ch) / SS) + 12
        h = int(cap * 1.6)
        im = Image.new('L', (w * SS, h * SS), 0)
        ImageDraw.Draw(im).text((w * SS / 2, (h / 2 + cap / 2) * SS), ch, font=f, fill=255, anchor='ms')
        out[ch] = down(np.asarray(im, np.float32) / 255)
    adv = max(font(cap).getlength(c) for c in '0123456789') / SS + cap * 0.06
    cw = font(cap).getlength(',') / SS + cap * 0.05
    return out, adv, cw, cap * 1.25


# ------------------------------------------------------------------------------------------------------------- particles
def dot_sprite(r, col, soft):
    p = int(r * 3 + 4)
    Y, X = np.mgrid[-p:p + 1, -p:p + 1].astype(np.float32)
    d = np.sqrt(X * X + Y * Y)
    a = np.clip(r + 0.5 - d, 0, 1) if not soft else np.exp(-(d / max(r * 0.75, 0.5)) ** 2)
    a = np.maximum(a, np.exp(-(d / (r * 2.2 + 1)) ** 2) * 0.35)               # its own small glow
    c = np.array(col, np.float32) / 255
    return Sprite(a[..., None] * c, a, p, p)


def dust_field(seed, n, rmin, rmax, opmin, opmax, soft):
    rng = np.random.default_rng(seed)
    return [dict(x=rng.uniform(80, 1000), y=rng.uniform(320, 1500), r=rng.uniform(rmin, rmax), v=rng.uniform(8, 34),
                 sw=rng.uniform(4, 16), ph=rng.uniform(0, 6.28), fl=rng.uniform(0.6, 2.2), op=rng.uniform(opmin, opmax),
                 soft=soft) for _ in range(n)]


def draw_dust(P, A, field, u, k_op):
    for d in field:
        key = ('dot', round(d['r'] * 2) / 2, d['soft'])
        S = sprites()
        if key not in S:
            S[key] = dot_sprite(key[1], (255, 222, 150), d['soft'])
        x = d['x'] + d['sw'] * math.sin(u * 0.9 + d['ph'])
        y = d['y'] - d['v'] * u
        op = d['op'] * (0.65 + 0.35 * math.sin(u * d['fl'] * 6.28 + d['ph'])) * k_op
        blit(P, A, S[key], x, y, op)


def sparks(P, A, u, src, dst):
    """the subscribe feeds the plaque: gold sparks leave the button on the tap and stream up into the plaque, each with a
    short motion trail (5 samples back along its own path)."""
    S = sprites()
    rng = np.random.default_rng(11)
    for i in range(40):
        t0 = END_TAP + 0.06 + i * 0.009
        dur = rng.uniform(0.55, 0.78)
        jx, jy = rng.uniform(-14, 14), rng.uniform(-8, 8)
        tx, ty = dst[0] + rng.uniform(-140, 140), dst[1] + rng.uniform(-90, 90)
        mx = (src[0] + tx) / 2 + rng.uniform(-300, 300)
        my = (src[1] + ty) / 2 + rng.uniform(-60, 120)
        r = rng.uniform(2.2, 4.0)
        key = ('spark', round(r * 2) / 2)
        if key not in S:
            S[key] = dot_sprite(key[1], (255, 236, 180), False)
        for j in range(7):
            e = (u - j * 0.010 - t0) / dur
            if not 0 < e < 1:
                continue
            e = ease_io(e)
            x = (1 - e) ** 2 * (src[0] + jx) + 2 * e * (1 - e) * mx + e * e * tx
            y = (1 - e) ** 2 * (src[1] + jy) + 2 * e * (1 - e) * my + e * e * ty
            op = (1 - j / 7) * min(1.0, (1 - e) * 4)
            blit(P, A, S[key], x, y, op, 1 - j * 0.09)


def streak_sprite():
    """an anamorphic light streak: a hot thin core with a wide warm halo."""
    w, h = 1800, 220
    Y, X = np.mgrid[0:h, 0:w].astype(np.float32)
    X -= w / 2; Y -= h / 2
    core = np.exp(-(Y / 1.6) ** 2) * np.exp(-(X / 560) ** 2)
    halo = np.exp(-(Y / 26) ** 2) * np.exp(-(X / 320) ** 2) * 0.30
    hot = np.exp(-(X * X + Y * Y) / (2 * 22.0 ** 2)) * 0.9
    a = np.clip(core + halo + hot, 0, 1)
    c = np.array([1.0, 0.90, 0.70], np.float32)
    return Sprite(a[..., None] * c, a, w / 2, h / 2)


def radial_sprite(r, col, peak):
    p = int(r * 1.2)
    Y, X = np.mgrid[-p:p + 1, -p:p + 1].astype(np.float32)
    a = np.exp(-(X * X + Y * Y) / (2 * (r / 2.2) ** 2)) * peak
    return Sprite(a[..., None] * (np.array(col, np.float32) / 255), a, p, p)


# ------------------------------------------------------------------------------------------------------------- the graphics
_S = {}
END_TAP = 2.30                                      # the end screen's click


def sprites():
    if not _S:
        _S['btn_mid'] = Button(26, 0.35)
        _S['btn_end'] = Button(30, 0.45)
        _S['cur_mid'] = cursor_sprite(54)
        _S['cur_end'] = cursor_sprite(62)
        cap = lambda P, A: caption_stack(P, A)
        _S['l1'] = text_sprite([('WANT ', 'white'), ('MORE', 'gold'), (' STORIES', 'white')], 44, 4, stack={'pad': 120, 'fn': cap})
        _S['l2'] = text_sprite([('LIKE THIS?', 'white')], 32, 4, stack={'pad': 120, 'fn': cap})
        _S['road'] = text_sprite([('ROAD TO 1,000,000', 'gold')], 20, 7, stack={'pad': 40, 'fn': lambda P, A: glow(P, A, 0.15, 0.5)})
        _S['plus'] = text_sprite([('+1', 'gold')], 40, 3, stack={'pad': 120, 'fn': cap})
        _S['face'] = plaque_face()
        _S['digits'] = digit_sprites(CNT_CAP)
        _S['streak'] = streak_sprite()
        _S['amb'] = radial_sprite(420, (255, 180, 70), 0.16)
        _S['far'] = dust_field(7, 70, 0.9, 2.4, 0.30, 0.80, False)
        _S['near'] = dust_field(19, 9, 9.0, 20.0, 0.05, 0.12, True)
    return _S


def bar_layer(P, A, frac, head_pulse, op):
    """the road to 1M: a faint track and a gold fill with his glow, a bright head where it stops."""
    x0, x1, y = 540 - 280, 540 + 280, 1168
    lw, lh = 820, 260
    ox, oy = 540 - lw // 2, y - lh // 2
    L = np.zeros((lh, lw, 3), np.float32); LA = np.zeros((lh, lw), np.float32)
    trk = rrect_mask(x1 - x0, 5, 2.5)
    tx, ty = x0 - ox, y - 2 - oy
    L[ty:ty + trk.shape[0], tx:tx + trk.shape[1]] += trk[..., None] * 0.20; LA[ty:ty + trk.shape[0], tx:tx + trk.shape[1]] += trk * 0.20
    fw = (x1 - x0) * frac
    if fw > 2:
        fm = rrect_mask(fw, 5, 2.5)
        g = ramp(np.linspace(0, 1, fm.shape[1])[None, :] * np.ones((fm.shape[0], 1)), [(0, GOLD[0]), (1, GOLD[1])])
        sl = (slice(ty, ty + fm.shape[0]), slice(tx, tx + fm.shape[1]))
        L[sl] = g * fm[..., None] + L[sl] * (1 - fm[..., None]); LA[sl] = fm + LA[sl] * (1 - fm)
        hx, hy = tx + fw, ty + 2.5
        Yh, Xh = np.mgrid[0:lh, 0:lw].astype(np.float32)
        hd = np.exp(-((Xh - hx) ** 2 + (Yh - hy) ** 2) / (2 * (4.0 + 3 * head_pulse) ** 2))
        L = np.clip(L + hd[..., None] * np.array([1.0, 0.95, 0.8], np.float32), 0, 1); LA = np.maximum(LA, hd)
    L, LA = glow(L, LA, 0.4, 0.8 + 0.8 * head_pulse)
    blit(P, A, Sprite(L, LA, 0, 0), ox, oy, op)


def frame(kind, u, cy=None):
    """one frame of a graphic at u seconds: (premultiplied rgb (H, W, 3), alpha (H, W)), float32 0-1."""
    S = sprites()
    P = np.zeros((H, W, 3), np.float32); A = np.zeros((H, W), np.float32)
    if kind == 'mid':
        cy = 1392 if cy is None else cy
        cx = 540.0
        btn = S['btn_mid']
        e_in = ease_out((u - 0.12) / 0.36)
        e_out = ease_in((u - 2.40) / 0.36)
        op = e_in * (1 - e_out)
        y = cy + (1 - e_in) * 24 - e_out * 18
        sc = 0.94 + 0.06 * e_in
        mix, deg, cur = tap_sequence(P, A, btn, cx, y, u, 0.62, 1.22, 1.62, S['cur_mid'], 70)
        hue, flare = red_glow(u, 0.12, 1.22)
        btn.draw(P, A, cx, y, op, sc, mix, deg, hue, flare)
        if v_ok(cur):
            c, x, yy, cop, press = cur
            blit(P, A, c, x, yy, cop * (1 - e_out), press)
        return P, A
    if kind == 'end':
        return end_frame(u)
    raise ValueError(kind)


def end_frame(u):
    """Road to 1M (Affan 2026-11-03: the first end screen was "just a motion graphic and a text"): out of a black beat a
    light streak crosses the frame and turns HIS gold play button plaque into view (perspective flip, gold edge, his glow),
    gold dust drifts at two depths, WANT MORE STORIES / LIKE THIS? rise in, the subscriber count rolls 0 -> 540,000 on the
    road to 1,000,000, the red SUBSCRIBE pill pops and is tapped: it flares, the count ticks +1, and the sparks of that
    subscribe stream up into the plaque, which shines. A slow camera push the whole time; fades to black for the loop."""
    S = sprites()
    P = np.zeros((H, W, 3), np.float32); A = np.zeros((H, W), np.float32)
    fade = 1 - ease_in((u - 3.62) / 0.38)
    # far dust behind everything
    draw_dust(P, A, S['far'], u, clamp01((u - 0.15) / 0.8))
    # ambient warmth behind the plaque, then the plaque
    e_p = clamp01((u - 0.32) / 0.14)
    blit(P, A, S['amb'], PLQ[0], PLQ[1], 0.9 * ease_out((u - 0.35) / 0.8))
    if e_p > 0:
        rot = 84.0 * (1 - back_out((u - 0.32) / 0.80, 1.1))
        rot += 4.0 * math.sin(2 * math.pi * (u - 1.1) / 2.9) * ease_io((u - 1.1) / 0.8)
        bob = 5.0 * math.sin(2 * math.pi * (u - 1.1) / 3.4) * ease_io((u - 1.1) / 0.8)
        shine = None
        diag = FW * math.cos(math.radians(25)) + FH * math.sin(math.radians(25))
        for t0, dur in ((1.20, 0.75), (END_TAP + 0.72, 0.65)):
            if t0 <= u < t0 + dur:
                shine = -80 + (diag + 160) * ease_io((u - t0) / dur)
        arrive = clamp01((u - END_TAP - 0.62) / 0.06) * math.exp(-max(0.0, u - END_TAP - 0.68) / 0.35)
        plaque_layer(P, A, rot, shine, 0.16 + 0.6 * arrive, PLQ[0], PLQ[1] + bob)
    # the light streak that brings it in
    if 0.08 <= u < 0.85:
        e = ease_io((u - 0.08) / 0.72)
        blit(P, A, S['streak'], -500 + 2080 * e, PLQ[1], math.sin(math.pi * clamp01((u - 0.08) / 0.72)))
    # headline
    for key, t0, yc, rise in (('l1', 0.62, 470, 28), ('l2', 0.74, 528, 20)):
        spr, tw = S[key]
        e = ease_out((u - t0) / 0.45)
        blit(P, A, spr, 540 - tw / 2, yc + (1 - e) * rise, e)
    # the count, the road, the bar
    e_c = ease_out((u - 0.80) / 0.30)
    if e_c > 0:
        counter_layer(P, A, u, e_c)
    spr, tw = S['road']
    e = ease_out((u - 1.05) / 0.45)
    blit(P, A, spr, 540 - tw / 2, 1122 + (1 - e) * 12, e)
    pulse = math.exp(-max(0.0, u - END_TAP - 0.1) / 0.3) if u > END_TAP + 0.1 else 0.0
    if u > 0.85:
        bar_layer(P, A, SUBS / 1e6 * (1 - (1 - clamp01((u - 0.85) / 0.95)) ** 4), pulse, ease_out((u - 0.85) / 0.3))
    # +1
    v = u - END_TAP - 0.12
    if 0 < v < 0.9:
        spr, tw = S['plus']
        blit(P, A, spr, CNT[0] + 236, CNT[1] - 34 - 46 * ease_out(v / 0.7), clamp01(v / 0.1) * (1 - ease_in((v - 0.45) / 0.45)))
    # the button
    btn = S['btn_end']
    bx, by = 540.0, 1312.0
    e = back_out((u - 1.40) / 0.45)
    bop = clamp01((u - 1.40) / 0.10)
    mix, deg, cur = tap_sequence(P, A, btn, bx, by, u, 1.80, END_TAP, 2.62, S['cur_end'], 92)
    hue, flare = red_glow(u, 1.40, END_TAP)
    btn.draw(P, A, bx, by, bop, 0.6 + 0.4 * e if u >= 1.40 else 0.6, mix, deg, hue, flare)
    if u > END_TAP:
        sparks(P, A, u, btn.tap_point(bx, by), PLQ)
    if v_ok(cur):
        c, x, yy, cop, press = cur
        blit(P, A, c, x, yy, cop, press)
    # camera: a slow push into the plaque; the near bokeh pushes faster (depth)
    s = 1 + 0.06 * ease_io(u / 4.0)
    M = np.float32([[s, 0, (1 - s) * 540], [0, s, (1 - s) * 880]])
    P = cv2.warpAffine(P, M, (W, H), flags=cv2.INTER_LINEAR, borderValue=0)
    A = cv2.warpAffine(A, M, (W, H), flags=cv2.INTER_LINEAR, borderValue=0)
    draw_dust(P, A, S['near'], u * 1.6, clamp01((u - 0.3) / 0.8))
    return P * fade, np.ones((H, W), np.float32)    # opaque: the black end screen


def v_ok(cur):
    return cur is not None and cur[3] > 0.002


# ------------------------------------------------------------------------------------------------------------- outputs
def sfx(kind, out):
    """the cue track: his approved soft swishes (the Patron set), crest on each entrance's fastest frame; the tap, the count
    and the sparks are silent (a click is foley, sparkle sounds are 'magic': both banned in a premium Short). Levels as
    sliced: mix the cue's peak ~15-19 dB under the local voice peak."""
    def load(name):
        raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', os.path.join(SFX_DIR, name + '.wav'), '-f', 'f32le', '-ac', '2',
                              '-ar', '48000', '-'], capture_output=True, check=True).stdout
        return np.frombuffer(raw, np.float32).reshape(-1, 2)
    crest = {'s5-classic': 0.17, 's3-wide': 0.31}
    cues = {'mid': [('s5-classic', 0.15)], 'end': [('s3-wide', 0.44), ('s5-classic', 1.45)]}[kind]
    buf = np.zeros((int(48000 * DUR[kind]) + 1, 2), np.float32)
    for name, at in cues:
        x = load(name)
        start = int(round((at - crest[name]) * 48000))
        if start < 0:
            x, start = x[-start:], 0
        n = min(len(x), len(buf) - start)
        buf[start:start + n] += x[:n]
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'f32le', '-ar', '48000', '-ac', '2', '-i', '-', '-c:a', 'pcm_s24le', out],
                   input=buf.tobytes(), check=True)


def render(kind, fps, out):
    global FPS
    FPS = fps
    n = int(round(DUR[kind] * fps))
    if kind == 'mid':
        enc = ['-c:v', 'prores_ks', '-profile:v', '4', '-pix_fmt', 'yuva444p10le', '-alpha_bits', '16', '-vendor', 'apl0']
        pix = 'rgba'
    else:
        enc = ['-c:v', 'prores_ks', '-profile:v', '3', '-pix_fmt', 'yuv422p10le', '-vendor', 'apl0']
        pix = 'rgb24'
    p = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', pix, '-s', f'{W}x{H}', '-r', str(fps),
                          '-i', '-'] + enc + ['-color_primaries', 'bt709', '-color_trc', 'bt709', '-colorspace', 'bt709', out],
                         stdin=subprocess.PIPE)
    for i in range(n):
        P, A = frame(kind, i / fps)
        if kind == 'mid':
            rgb = P / np.maximum(A[..., None], 1e-6)          # ProRes 4444 alpha is straight
            img = np.dstack([rgb, A])
        else:
            img = P
        p.stdin.write((np.clip(img, 0, 1) * 255 + 0.5).astype(np.uint8).tobytes())
    p.stdin.close(); p.wait()


def sheet(out):
    rows = []
    for kind, ts in (('mid', [0.3, 0.9, 1.20, 1.27, 1.36, 1.6, 2.2]), ('end', [0.35, 0.6, 1.0, 1.5, 2.33, 2.6, 3.2])):
        tiles = []
        for t in ts:
            P, A = frame(kind, t)
            if kind == 'mid':
                img = P + np.full((H, W, 3), 0.30, np.float32) * (1 - A[..., None])
                crop = img[1150:1650]
            else:
                crop = P[300:1500]
            tiles.append(cv2.resize(crop, (crop.shape[1] // 2, crop.shape[0] // 2), interpolation=cv2.INTER_AREA))
        rows.append(np.concatenate(tiles, 1))
    for i, r in enumerate(rows):
        Image.fromarray((np.clip(r, 0, 1) * 255).astype(np.uint8)).save(out.replace('.png', f'-{["mid", "end"][i]}.png'))


if __name__ == '__main__':
    args = sys.argv[1:]
    cmd = args[0] if args else 'render'
    out = args[args.index('--out') + 1] if '--out' in args else OUT_DIR
    fps = int(args[args.index('--fps') + 1]) if '--fps' in args else 60
    if '--subs' in args:
        SUBS = int(args[args.index('--subs') + 1])
    only = args[args.index('--only') + 1] if '--only' in args else None
    os.makedirs(out, exist_ok=True)
    if cmd == 'sheet':
        sheet(os.path.join(out, 'aw-cta-sheet.png'))
    else:
        for kind in ('mid', 'end'):
            if only and kind != only:
                continue
            render(kind, fps, os.path.join(out, f'aw-cta-{kind}-{fps}.mov'))
            sfx(kind, os.path.join(out, f'aw-cta-{kind}-sfx.wav'))
    print('done', out)
