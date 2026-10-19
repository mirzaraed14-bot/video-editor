"""mg-cards.py: small motion-graphic B-roll clips drawn frame by frame (PIL -> ffmpeg), so the kit places them like any B shot.

  python workflows/mg-cards.py dots     OUT.mp4 --n 3000 --label "1 OF 3,000 AGENTS" [--dur 3.0] [--w 1080 --h 1920]
  python workflows/mg-cards.py counter  OUT.mp4 --to 50 --label "SHOWS PITCHED" [--dur 3.0]
  python workflows/mg-cards.py calendar OUT.mp4 --label "A BANK CEO'S WEEK" [--dur 3.4]
  python workflows/mg-cards.py tvoff    OUT.mp4 --src STILL.jpg [--cx 0.5] [--dur 3.3]

dots      a field of N white dots on navy; one dot turns teal and the camera eases in on it; the label rises in under it.
counter   a number rolls up from 1 to --to (ease-in-out), each change sliding up with a fading ghost; the final number turns teal.
calendar  a packed work week (Mon-Fri, 8am-8pm) whose meetings pop away one by one until three remain: the "white space".
Style (Scott Clary, 2026-10-19): Anton caps, white + one teal accent #19D3C5, navy #0E1726 or calendar white; everything eased, nothing
linear; a slow push on the whole card so it is never static. 30 fps (the kit's base rate), yuv420p H.264 CRF 14.
"""
import argparse, math, os, random, subprocess
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
ANTON = os.path.join(HERE, "..", "presets", "youtube-shorts", "onyx-samples-youtube", "kit", "fonts", "Anton-Regular.ttf")
TEAL, NAVY, WHITE = (25, 211, 197), (14, 23, 38), (255, 255, 255)
FPS = 30
ease = lambda t: 0.5 - 0.5 * math.cos(math.pi * min(max(t, 0), 1))
eout = lambda t: 1 - (1 - min(max(t, 0), 1)) ** 3


def writer(path, w, h):
    return subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{w}x{h}", "-r", str(FPS), "-i", "-",
                             "-c:v", "libx264", "-crf", "14", "-preset", "medium", "-pix_fmt", "yuv420p", path], stdin=subprocess.PIPE)


def push(img, t, amt=0.05):
    """A slow eased push on the whole card (nothing is ever static)."""
    w, h = img.size; k = 1 + amt * ease(t); cw, ch = w / k, h / k
    return img.crop((round((w - cw) / 2), round((h - ch) / 2), round((w + cw) / 2), round((h + ch) / 2))).resize((w, h), Image.LANCZOS)


def label(d, text, cx, y, size, col=WHITE, a=1.0, rise=0.0):
    f = ImageFont.truetype(ANTON, size); tw = d.textlength(text, font=f)
    c = tuple(int(v * a) for v in col)
    d.text((cx - tw / 2, y + 30 * (1 - rise)), text, font=f, fill=c)


def dots(a):
    w, h, n = a.w, a.h, a.n; S = 2                                   # the field drawn at 2x, then the camera crops into it
    rng = random.Random(7); field = Image.new("RGB", (w * S, h * S), NAVY); d = ImageDraw.Draw(field)
    cols = int(math.sqrt(n * w / h)); rows = math.ceil(n / cols); gx, gy = w * S / (cols + 1), h * S / (rows + 1)
    pts = [((i % cols + 1) * gx + rng.uniform(-gx * .18, gx * .18), (i // cols + 1) * gy + rng.uniform(-gy * .18, gy * .18)) for i in range(n)]
    r = max(2, int(min(gx, gy) * 0.18))
    for x, y in pts:
        d.ellipse((x - r, y - r, x + r, y + r), fill=(205, 214, 228))
    tx, ty = min(pts, key=lambda p: abs(p[0] - w * S * .5) + abs(p[1] - h * S * .46))
    out = writer(a.out, w, h); N = round(a.dur * FPS)
    for i in range(N):
        t = i / (N - 1); z = 1 + 5.0 * ease((t - 0.25) / 0.6)                 # hold the whole field, then ease in on the one
        fr = field.copy(); fd = ImageDraw.Draw(fr); g = eout((t - 0.12) / 0.2)
        if g > 0:
            for k in range(6, 0, -1):                                         # the glow
                rr = r * (1 + k * 0.9 * g); fd.ellipse((tx - rr, ty - rr, tx + rr, ty + rr), fill=tuple(int(NAVY[j] + (TEAL[j] - NAVY[j]) * g / (k + 1)) for j in range(3)))
            fd.ellipse((tx - r * 1.3, ty - r * 1.3, tx + r * 1.3, ty + r * 1.3), fill=TEAL)
        cw, ch = w * S / z, h * S / z; cx = tx + (w * S / 2 - tx) / z; cy = ty + (h * S / 2 - ty) / z
        im = fr.crop((round(cx - cw / 2), round(cy - ch / 2), round(cx + cw / 2), round(cy + ch / 2))).resize((w, h), Image.LANCZOS)
        ld = ImageDraw.Draw(im); la = eout((t - 0.62) / 0.2)
        if la > 0:
            fw = ld.textlength(a.label, font=ImageFont.truetype(ANTON, 96))
            ld.rounded_rectangle((w / 2 - fw / 2 - 36, h * 0.30 - 6 + 30 * (1 - la), w / 2 + fw / 2 + 36, h * 0.30 + 136 + 30 * (1 - la)),
                                 radius=22, fill=tuple(int(c * la) for c in NAVY))          # a plate so the label never sits on the dots
            label(ld, a.label, w / 2, h * 0.30, 96, WHITE, la, la)
        out.stdin.write(im.tobytes())
    out.stdin.close(); out.wait()


def counter(a):
    w, h = a.w, a.h; out = writer(a.out, w, h); N = round(a.dur * FPS); f = ImageFont.truetype(ANTON, 360)
    val = lambda t: 1 + round((a.to - 1) * ease(t / 0.72))
    for i in range(N):
        t = i / (N - 1); v = val(t); speed = abs(v - val(max(t - 1 / (N - 1), 0)))   # numbers per frame
        im = Image.new("RGB", (w, h), NAVY)
        num = Image.new("RGB", (w, 520), NAVY); nd = ImageDraw.Draw(num); txt = str(v); tw = nd.textlength(txt, font=f)
        pop = 1 + 0.08 * (1 - eout((t - 0.72) / 0.12)) if v == a.to else 1.0           # the last number lands with a small settle
        nd.text((w / 2 - tw / 2, 40), txt, font=f, fill=TEAL if v == a.to else WHITE)
        if speed:
            num = num.filter(ImageFilter.GaussianBlur(min(1.5 + speed * 1.5, 7)))       # motion blur while it rolls
        if pop != 1.0:
            nw, nh = round(w * pop), round(520 * pop); num = num.resize((nw, nh), Image.LANCZOS).crop(((nw - w) // 2, (nh - 520) // 2, (nw - w) // 2 + w, (nh - 520) // 2 + 520))
        im.paste(num, (0, int(h * 0.30)))
        label(ImageDraw.Draw(im), a.label, w / 2, h * 0.62, 84, WHITE, eout(t / 0.25), eout(t / 0.25))
        out.stdin.write(push(im, t, 0.04).tobytes())
    out.stdin.close(); out.wait()


def calendar(a):
    w, h = a.w, a.h; out = writer(a.out, w, h); N = round(a.dur * FPS)
    x0, x1, y0, y1 = 110, w - 50, int(h * 0.30), int(h * 0.80); days = ["MON", "TUE", "WED", "THU", "FRI"]; dw = (x1 - x0) / 5; hh = (y1 - y0) / 12
    rng = random.Random(3); blocks = []
    for di in range(5):
        hr = 0.0
        while hr < 11.5:
            ln = rng.choice([0.5, 1.0, 1.0, 1.5]); blocks.append((di, hr, min(ln, 12 - hr))); hr += ln + rng.choice([0, 0, 0.5])
    keep = {3, len(blocks) // 2, len(blocks) - 6}
    order = [k for k in range(len(blocks)) if k not in keep]; rng.shuffle(order)
    palette = [(255, 196, 120), (140, 190, 255), (255, 150, 160), (170, 220, 170), (200, 170, 255)]
    fl = ImageFont.truetype(ANTON, 44); fh = ImageFont.truetype(ANTON, 30)
    for i in range(N):
        t = i / (N - 1); im = Image.new("RGB", (w, h), (248, 249, 251)); d = ImageDraw.Draw(im)
        label(d, a.label, w / 2, h * 0.17, 92, NAVY, 1.0, eout(t / 0.2))
        for di, nm in enumerate(days):
            tw = d.textlength(nm, font=fl); d.text((x0 + di * dw + dw / 2 - tw / 2, y0 - 70), nm, font=fl, fill=(90, 100, 120))
        for k in range(13):
            y = y0 + k * hh; d.line((x0, y, x1, y), fill=(225, 229, 236), width=2)
            if k % 2 == 0:
                d.text((20, y - 16), f"{(8 + k - 1) % 12 + 1}{'AM' if 8 + k < 12 else 'PM'}", font=fh, fill=(150, 158, 175))
        for k, (di, hr, ln) in enumerate(blocks):
            g = 1.0
            if k in order:
                j = order.index(k); start = 0.22 + 0.5 * j / len(order); g = 1 - eout((t - start) / 0.06)
            if g <= 0.01:
                continue
            col = TEAL if k in keep and t > 0.8 else palette[(di + k) % 5]
            bx0, by0, bx1, by1 = x0 + di * dw + 8, y0 + hr * hh + 4, x0 + (di + 1) * dw - 8, y0 + (hr + ln) * hh - 4
            cx, cy, sw, sh = (bx0 + bx1) / 2, (by0 + by1) / 2, (bx1 - bx0) * g, (by1 - by0) * g
            d.rounded_rectangle((cx - sw / 2, cy - sh / 2, cx + sw / 2, cy + sh / 2), radius=12, fill=col)
        out.stdin.write(push(im, t, 0.05).tobytes())
    out.stdin.close(); out.wait()


def tvoff(a):
    """An old TV switching off over a still (--src): scanlines and a faint flicker, then the picture collapses to a bright line, then
    to a dot that fades ("cable TV was slowly going down"). The collapse lands at 70 % of --dur."""
    w, h = a.w, a.h; out = writer(a.out, w, h); N = round(a.dur * FPS)
    src = Image.open(a.src).convert("RGB"); k = max(w / src.width, h / src.height)
    src = src.resize((round(src.width * k), round(src.height * k)), Image.LANCZOS)
    x0 = round(a.cx * src.width - w / 2); x0 = min(max(x0, 0), src.width - w); y0 = (src.height - h) // 2; src = src.crop((x0, y0, x0 + w, y0 + h))
    scan = np.ones((h, 1, 1), np.float32); scan[::4] = 0.82                                        # scanlines every 4 px
    rng = random.Random(5)
    for i in range(N):
        t = i / (N - 1); tc = (t - 0.62) / 0.12                                                    # collapse window
        frame = push(src, t, 0.05)
        arr = np.asarray(frame, np.float32) * scan * (1 + 0.04 * rng.uniform(-1, 1))
        im = Image.new("RGB", (w, h), (0, 0, 0))
        if tc < 1:
            sy = 1 - eout(max(tc, 0)) * 0.995; bright = 1 + 1.5 * eout(max(tc, 0))                  # squash vertically, flare up
            pic = Image.fromarray(np.clip(arr * bright, 0, 255).astype(np.uint8)).resize((w, max(2, round(h * sy))), Image.LANCZOS)
            im.paste(pic, (0, (h - pic.height) // 2))
        else:
            tl = (t - 0.74) / 0.18; lw = max(0.0, 1 - eout(tl)); d = ImageDraw.Draw(im)              # the line shrinks to a dot, then fades
            if lw > 0.02:
                L = w * lw; d.rounded_rectangle((w / 2 - L / 2, h / 2 - 3, w / 2 + L / 2, h / 2 + 3), radius=3, fill=(235, 245, 255))
            else:
                fa = max(0.0, 1 - eout((t - 0.92) / 0.08)); r = 7
                d.ellipse((w / 2 - r, h / 2 - r, w / 2 + r, h / 2 + r), fill=tuple(int(c * fa) for c in (235, 245, 255)))
        out.stdin.write(im.tobytes())
    out.stdin.close(); out.wait()


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("kind", choices=["dots", "counter", "calendar", "tvoff"]); ap.add_argument("out")
    ap.add_argument("--n", type=int, default=3000); ap.add_argument("--to", type=int, default=50); ap.add_argument("--label", default="")
    ap.add_argument("--src"); ap.add_argument("--cx", type=float, default=0.5); ap.add_argument("--dur", type=float, default=3.0); ap.add_argument("--w", type=int, default=1080); ap.add_argument("--h", type=int, default=1920)
    a = ap.parse_args()
    {"dots": dots, "counter": counter, "calendar": calendar, "tvoff": tvoff}[a.kind](a)
    print("done", a.out)
