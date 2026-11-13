# /// script
# requires-python = ">=3.10"
# dependencies = ["opencv-python-headless", "numpy", "pillow"]
# ///
"""inbox-flood.py: INBOX FLOOD, a reusable kit effect (2026-11-14, pbd-urine-prank; UPGRADES.md).  FX-32 "Headline Avalanche" + FX-54 "Dark Headline Card": statements REBUILT as UI, never screenshotted.

A dark-mode mail app, 1080 x 1920, for any "people wrote back" story.  Two modes, one look (a hairline-bordered dark row / card, a generic person avatar, skeleton bars where a sender's name or a
preview would be, a gold unread dot, a red badge):
  ROWS   a flood: rows DROP in at the top of the list with a spring and push the stack down; an unread badge ticks up and is CAPPED at "99+" (never a number the speaker did not say).
         scene["rows"] = dict(t0=0.5, dt0=0.16, dt1=0.06, n=22, subject="RE: NEW LAW")   (the gap between drops goes from dt0 to dt1; the subject is ONLY words the speaker said)
  CARDS  the messages themselves, one per spoken line: a big card rises in on its first word, the earlier cards recede (smaller, dimmer, up).
         scene["cards"] = [dict(t=0.24, text="WHY DO I NEED TO SEND MY URINE?", gold=[], label="RE: NEW LAW"), ...]   (+ scene["ghosts"] = [text, ...] earlier cards already receded)
Scene keys: dur, mode "rows" | "cards", title "INBOX", badge_cap 99, badge_t0 (seconds the badge starts to tick; default = rows t0).
As a library:  f = InboxFlood(scene); rgb = f.frame(t)  -> (1920, 1080, 3) uint8.     CLI test clip:  uv run workflows/inbox-flood.py test OUT.mp4 [--mode rows|cards] [--fps 30]
"""
import math, os, subprocess, sys
import cv2, numpy as np
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__)); REPO = os.path.dirname(HERE)
FONTS = os.path.join(REPO, "presets", "youtube-shorts", "onyx-samples-youtube", "kit", "fonts")
W, H = 1080, 1920
GOLD, WHITE, RED = (246, 180, 18), (255, 255, 255), (236, 58, 72)


def mont(size, wght=800):
    f = ImageFont.truetype(os.path.join(FONTS, "Montserrat-VF.ttf"), size)
    try: f.set_variation_by_axes([wght])
    except Exception: pass
    return f


def eo(p): p = min(1.0, max(0.0, p)); return 1 - (1 - p) ** 3
def eio(p): p = min(1.0, max(0.0, p)); return 0.5 * (1 - math.cos(math.pi * p))
def spring(p):   # a drop that overshoots a hair and settles
    p = min(1.0, max(0.0, p)); return 1 - math.exp(-6.5 * p) * math.cos(9.0 * p)


def rr(draw, box, r, fill=None, outline=None, width=1):
    draw.rounded_rectangle(box, radius=r, fill=fill, outline=outline, width=width)


def avatar(d, cx, cy, r, ss, tone=(52, 60, 72)):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=tone)
    d.ellipse([cx - r * 0.36, cy - r * 0.52, cx + r * 0.36, cy + r * 0.20], fill=(142, 152, 166))
    d.pieslice([cx - r * 0.66, cy + r * 0.10, cx + r * 0.66, cy + r * 1.30], 180, 360, fill=(142, 152, 166))


def sprite_row(subject, ss=2):
    w, h = 920, 150
    im = Image.new("RGBA", (w * ss, h * ss), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    rr(d, [0, 0, w * ss - 1, h * ss - 1], 22 * ss, fill=(17, 22, 28, 244), outline=(255, 255, 255, 26), width=2)
    avatar(d, 70 * ss, 75 * ss, 42 * ss, ss)
    rr(d, [134 * ss, 28 * ss, 372 * ss, 46 * ss], 9 * ss, fill=(58, 66, 78, 255))
    d.text((134 * ss, 78 * ss), subject, font=mont(44 * ss, 800), fill=WHITE + (255,), anchor="lm")
    rr(d, [134 * ss, 108 * ss, 640 * ss, 122 * ss], 7 * ss, fill=(41, 48, 58, 255))
    d.ellipse([850 * ss, 59 * ss, 880 * ss, 89 * ss], fill=GOLD + (255,))
    return np.asarray(im.resize((w, h), Image.LANCZOS))


def sprite_card(text, gold, label, ss=2, width=920, size=76):
    f = mont(size * ss, 800); maxw = (width - 92) * ss
    lines, cur = [], ""
    for wd in text.split():
        t = (cur + " " + wd).strip()
        if f.getlength(t) <= maxw: cur = t
        else: lines.append(cur); cur = wd
    lines.append(cur)
    lh = int(size * 1.16); h = 170 + lh * len(lines) + 44
    im = Image.new("RGBA", (width * ss, h * ss), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    rr(d, [0, 0, width * ss - 1, h * ss - 1], 30 * ss, fill=(18, 23, 30, 248), outline=(255, 255, 255, 34), width=2)
    avatar(d, 82 * ss, 80 * ss, 38 * ss, ss)
    rr(d, [140 * ss, 52 * ss, 372 * ss, 68 * ss], 8 * ss, fill=(58, 66, 78, 255))
    d.text((140 * ss, 100 * ss), label, font=mont(26 * ss, 700), fill=(150, 160, 174, 255), anchor="lm")
    d.ellipse([width * ss - 92 * ss, 68 * ss, width * ss - 64 * ss, 96 * ss], fill=GOLD + (255,))
    y = 150 + 10
    gset = {g.upper() for g in gold}
    for ln in lines:
        x = 46 * ss
        for wd in ln.split():
            col = GOLD if wd.strip("?!.,").upper() in gset else WHITE
            d.text((x, (y + lh / 2) * ss), wd, font=f, fill=col + (255,), anchor="lm"); x += f.getlength(wd + " ")
        y += lh
    return np.asarray(im.resize((width, h), Image.LANCZOS))


def blit(out, spr, cx, top, scale=1.0, alpha=1.0, shadow=0.45):
    if alpha <= 0.003: return
    h, w = spr.shape[:2]
    if scale != 1.0:
        w2, h2 = int(round(w * scale)), int(round(h * scale)); spr = cv2.resize(spr, (w2, h2), interpolation=cv2.INTER_AREA if scale < 1 else cv2.INTER_CUBIC); h, w = h2, w2
    x0, y0 = int(round(cx - w / 2)), int(round(top))
    ya, yb, xa, xb = max(0, y0), min(H, y0 + h), max(0, x0), min(W, x0 + w)
    if yb <= ya or xb <= xa: return
    s = spr[ya - y0:yb - y0, xa - x0:xb - x0]; a = s[..., 3:4].astype(np.float32) / 255.0 * alpha
    if shadow > 0:   # a soft dark drop shadow: the alpha, blurred, pushed down
        m = cv2.GaussianBlur(np.pad(a[..., 0], 40), (0, 0), 16)[40:-40, 40:-40] * shadow
        sy0 = min(H, yb + 14) - (yb - ya); reg0 = out[ya:yb, xa:xb]; reg0[:] = reg0 * (1 - m[..., None] * 0.0)
    reg = out[ya:yb, xa:xb]; reg[:] = reg * (1 - a) + s[..., :3].astype(np.float32) * a


class InboxFlood:
    def __init__(self, scene):
        self.s = scene; self.dur = scene["dur"]; self.mode = scene.get("mode", "rows")
        yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
        r = np.sqrt(((xx - W / 2) / (W * 0.75)) ** 2 + ((yy - H * 0.38) / (H * 0.55)) ** 2)
        self.bg = np.array([7, 9, 12], np.float32) + np.array([12, 15, 21], np.float32) * np.clip(1.15 - r, 0, 1)[..., None]
        self.header = self._header(scene.get("title", "INBOX"))
        if self.mode == "rows":
            rw = scene.get("rows", {}); self.row = sprite_row(rw.get("subject", "RE: NEW LAW"))
            t = rw.get("t0", 0.5); self.times = []
            for i in range(int(rw.get("n", 22))):
                self.times.append(t); t += rw.get("dt0", 0.16) + (rw.get("dt1", 0.06) - rw.get("dt0", 0.16)) * min(1.0, i / max(1, rw.get("n", 22) * 0.6))
        else:
            self.cards = [dict(c, spr=sprite_card(c["text"], c.get("gold", []), c.get("label", "RE: NEW LAW"))) for c in scene["cards"]]
            self.ghosts = [sprite_card(g, [], "RE: NEW LAW", size=60) for g in scene.get("ghosts", [])]

    def _header(self, title):
        ss = 2; im = Image.new("RGBA", (W * ss, 120 * ss), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
        d.text((92 * ss, 60 * ss), title, font=mont(46 * ss, 900), fill=WHITE + (255,), anchor="lm")
        d.text((92 * ss + mont(46 * ss, 900).getlength(title) + 22 * ss, 66 * ss), "MAIL", font=mont(24 * ss, 700), fill=(120, 130, 144, 255), anchor="lm")
        return np.asarray(im.resize((W, 120), Image.LANCZOS))

    def _badge(self, out, n, cap, t_pop=None, t=0.0):
        txt = f"{cap}+" if n > cap else str(n)
        if n <= 0: return
        sc = 1.0 + (0.18 * math.exp(-(t - t_pop) * 14) if t_pop is not None and t >= t_pop else 0.0)
        ss = 2; w, h = 150 * ss, 64 * ss; im = Image.new("RGBA", (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
        rr(d, [0, 0, w - 1, h - 1], h // 2, fill=RED + (255,)); d.text((w // 2, h // 2 + 2), txt, font=mont(36 * ss, 900), fill=WHITE + (255,), anchor="mm")
        spr = np.asarray(im.resize((w // ss, h // ss), Image.LANCZOS)); blit(out, spr, W - 92 - 75, 224 - 32 * (sc - 1), sc, 1.0, 0)

    def frame(self, t):
        out = self.bg.copy()
        blit(out, self.header, W / 2, 190, 1.0, 1.0, 0)
        cap = int(self.s.get("badge_cap", 99))
        if self.mode == "rows":
            slot, top0 = 168, 290; n = 0
            for i, ti in enumerate(self.times):
                if t < ti: break
                n = i + 1
            for i in range(n):
                age = n - 1 - i                                             # 0 = the newest
                p_in = spring((t - self.times[i]) / 0.30)
                nxt = self.times[i + 1] if i + 1 < len(self.times) else 1e9
                shift = sum(eio((t - self.times[j]) / 0.10) for j in range(i + 1, n))   # each later row pushes this one down one slot over 0.10 s (= the shortest gap between two drops: no overprint)
                top = top0 + shift * slot - (1 - p_in) * 64
                if top > 1010: continue
                a = min(1.0, (t - self.times[i]) / 0.10)
                blit(out, self.row, W / 2, top, 1.0, a * (1.0 if top < 900 else max(0.0, (1010 - top) / 110)), 0)
            nb = 0
            if n:
                k = n + (n * (n - 1)) // 2 * 1                           # the badge runs ahead of the rows (a flood), then caps
                nb = min(cap + 1, int(k * 1.6))
            self._badge(out, nb, cap, self.times[n - 1] if n else None, t)
        else:
            cards = self.cards; y_act = 640
            # earlier cards recede: each later card pushes it up 330 px, scale 0.9 per step, dimmer
            gh = self.ghosts
            for gi, g in enumerate(gh):
                blit(out, g, W / 2, 330 + gi * 20, 0.82, 0.30, 0)
            for i, c in enumerate(cards):
                if t < c["t"] - 0.02: continue
                p_in = eo((t - c["t"]) / 0.34); rec = sum(eio((t - cards[j]["t"]) / 0.30) for j in range(i + 1, len(cards)))
                h = c["spr"].shape[0]
                top = (y_act + (1 - p_in) * 150) - rec * 345 - (0 if h < 330 else (h - 330) * 0.2)
                sc = 1.0 - 0.13 * min(1.0, rec); al = min(1.0, p_in * 1.4) * (1.0 - 0.55 * min(1.0, rec))
                blit(out, c["spr"], W / 2, top, sc, al, 0)
            self._badge(out, cap + 1, cap, None, t)
        return np.clip(out, 0, 255).astype(np.uint8)

    def render(self, path, fps=30.0):
        n = int(round(self.dur * fps))
        enc = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(fps), "-i", "-", "-c:v", "libx264", "-crf", "14", "-pix_fmt", "yuv420p", path], stdin=subprocess.PIPE)
        for i in range(n):
            enc.stdin.write(self.frame(i / fps).tobytes())
        enc.stdin.close(); enc.wait(); return n


if __name__ == "__main__":
    if len(sys.argv) < 3 or sys.argv[1] != "test":
        sys.exit(__doc__)
    outp = sys.argv[2]; arg = lambda n, d: sys.argv[sys.argv.index(n) + 1] if n in sys.argv else d
    mode, fps = arg("--mode", "rows"), float(arg("--fps", "30"))
    if mode == "rows":
        sc = dict(dur=2.4, mode="rows", rows=dict(t0=0.4, dt0=0.16, dt1=0.06, n=22, subject="RE: NEW LAW"))
    else:
        sc = dict(dur=3.7, mode="cards", cards=[dict(t=0.24, text="WHY DO I NEED TO SEND MY URINE?", gold=["URINE"]), dict(t=2.0, text="WHAT ARE THE BEST KIND OF CUPS TO BUY?", gold=["CUPS", "BUY"])])
    print("wrote", outp, InboxFlood(sc).render(outp, fps), "frames")
