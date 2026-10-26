"""mg-cards.py: small motion-graphic B-roll clips drawn frame by frame (PIL -> ffmpeg), so the kit places them like any B shot.

  python workflows/mg-cards.py dots     OUT.mp4 --n 3000 --label "1 OF 3,000 AGENTS" [--dur 3.0] [--w 1080 --h 1920]
  python workflows/mg-cards.py counter  OUT.mp4 --to 50 --label "SHOWS PITCHED" [--dur 3.0] [--money: $ and commas]
  python workflows/mg-cards.py inspection OUT.mp4 --mode open|passed [--dur 4]   (a U.S. Army facility-inspection clipboard)
  python workflows/mg-cards.py inspectors OUT.mp4 --label "4 INSPECTORS" [--dur 3]   (four figures pop in)
  python workflows/mg-cards.py craigslist OUT.mp4 --label "RECEPTIONIST NEEDED - MIAMI BEACH OFFICE" [--dur 3.5]
  python workflows/mg-cards.py calendar OUT.mp4 --label "A BANK CEO'S WEEK" [--dur 3.4]
  python workflows/mg-cards.py tvoff    OUT.mp4 --src STILL.jpg [--cx 0.5] [--dur 3.3]
  python workflows/mg-cards.py collateral OUT.mp4 --dur 9.4 --t1 3.0 --t2 6.3 [--r0 0 --r1 1.6]   (the $525M loan and the ten characters that secured it)
  python workflows/mg-cards.py sneaker  OUT.mp4 --src CUTOUT.png --mode real|fake|rule|button [--steps 600@0.9,700@1.3,800@1.7] [--t1 --t2]
  python workflows/mg-cards.py replies  OUT.mp4 --t1 2.2 [--dur 3]     (rates out, Yes / Yes / No. back; "No." lands at --t1)
  python workflows/mg-cards.py dayrate  OUT.mp4 --steps 250@0,300@2.6,400@3.0,600@3.4,800@3.8 [--label "HIS DAY RATE"]

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
    w, h = a.w, a.h; out = writer(a.out, w, h); N = round(a.dur * FPS)
    fmt = (lambda v: f"${v:,}") if a.money else str
    size = 360
    while ImageFont.truetype(ANTON, size).getlength(fmt(a.to)) > w - 120:
        size -= 10
    f = ImageFont.truetype(ANTON, size)
    val = lambda t: 1 + round((a.to - 1) * ease(t / 0.72))
    for i in range(N):
        t = i / (N - 1); v = val(t); speed = abs(v - val(max(t - 1 / (N - 1), 0)))   # numbers per frame
        im = Image.new("RGB", (w, h), NAVY)
        num = Image.new("RGB", (w, 520), NAVY); nd = ImageDraw.Draw(num); txt = fmt(v); tw = nd.textlength(txt, font=f)
        pop = 1 + 0.08 * (1 - eout((t - 0.72) / 0.12)) if v == a.to else 1.0           # the last number lands with a small settle
        nd.text((w / 2 - tw / 2, 40 + (360 - size) * 0.6), txt, font=f, fill=TEAL if v == a.to else WHITE)
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


def craigslist(a):
    """A Craigslist-style listing on a white page (the classic look: purple serif links, grey rules), the title types out word by
    word, then a cursor clicks "reply". For "hired a few girls off Craigslist to act as a receptionist" (War Dogs, 2026-10-23)."""
    w, h = a.w, a.h; out = writer(a.out, w, h); N = round(a.dur * FPS)
    serif = "C:/Windows/Fonts/times.ttf"; serif_b = "C:/Windows/Fonts/timesbd.ttf"
    fl, ft, fb, fs = ImageFont.truetype(serif_b, 120), ImageFont.truetype(serif_b, 86), ImageFont.truetype(serif, 62), ImageFont.truetype(serif, 40)
    PURPLE, GREY, INK = (128, 0, 128), (150, 150, 150), (30, 30, 30)
    title = a.label or "RECEPTIONIST NEEDED - MIAMI BEACH OFFICE"
    body = ["employment type: temporary", "start: this week"]          # only what he said: a receptionist, within a week
    words = title.split()
    for i in range(N):
        s_ = i / FPS; t = i / (N - 1)
        im = Image.new("RGB", (w, h), (255, 255, 255)); d = ImageDraw.Draw(im)
        d.text((80, 230), "craigslist", font=fl, fill=PURPLE)
        d.text((80 + d.textlength("craigslist ", font=fl), 278), "> miami > jobs", font=fs, fill=GREY)
        d.line((80, 390, w - 80, 390), fill=(220, 220, 220), width=3)
        nw = min(len(words), int(max(s_ - 0.25, 0) / 0.12) + (1 if s_ > 0.25 else 0))     # the title types word by word
        y = 430; line = ""
        for wd in words[:nw]:
            if d.textlength(line + wd + " ", font=ft) > w - 160:
                d.text((80, y), line, font=ft, fill=PURPLE); y += 104; line = ""
            line += wd + " "
        if line:
            d.text((80, y), line, font=ft, fill=PURPLE)
        if nw < len(words) and int(s_ * 4) % 2 == 0:
            d.rectangle((80 + d.textlength(line, font=ft), y + 8, 86 + d.textlength(line, font=ft), y + 76), fill=PURPLE)
        by = y + 150; bp = eout((s_ - 0.25 - 0.12 * len(words)) / 0.35)
        if bp > 0:
            for k, b in enumerate(body):
                c = tuple(int(255 + (v - 255) * bp) for v in INK); d.text((80, by + 80 * k), b, font=fb, fill=c)
            rb = (80, by + 80 * len(body) + 40, 330, by + 80 * len(body) + 124)
            d.rounded_rectangle(rb, radius=12, fill=tuple(int(255 + (v - 255) * bp) for v in (90, 90, 90)))
            d.text((rb[0] + 62, rb[1] + 14), "reply", font=fb, fill=(255, 255, 255))
            cp = eout((s_ - (0.6 + 0.12 * len(words))) / 0.4)                        # the cursor glides to "reply" and clicks
            if cp > 0:
                cx, cy = w - 120 + (rb[0] + 170 - (w - 120)) * cp, h - 300 + (rb[1] + 50 - (h - 300)) * cp
                d.polygon([(cx, cy), (cx, cy + 60), (cx + 16, cy + 46), (cx + 28, cy + 72), (cx + 38, cy + 67), (cx + 26, cy + 42), (cx + 46, cy + 42)], fill=INK, outline=(255, 255, 255))
        out.stdin.write(push(im, t, 0.05).tobytes())
    out.stdin.close(); out.wait()


def inspection(a):
    """A U.S. Army facility-inspection checklist on a clipboard (War Dogs, 2026-10-23). --mode open: the clipboard slides up, the rows
    appear one by one with empty boxes ("they wanted to send contracting officers... to do a facility inspection"). --mode passed: the
    same sheet, every box gets a teal tick in turn, then a red PASSED stamp slams ("they gave him glowing reviews")."""
    w, h = a.w, a.h; out = writer(a.out, w, h); N = round(a.dur * FPS)
    rows = ["OFFICE", "STAFF", "SIGNAGE", "RECEPTION"]
    fh_, fr_, fs_ = ImageFont.truetype(ANTON, 58), ImageFont.truetype(ANTON, 76), ImageFont.truetype(ANTON, 150)
    RED = (229, 56, 59); PAPER = (246, 244, 238); INK = (28, 32, 44)
    for i in range(N):
        s_ = i / FPS; t = i / (N - 1)
        im = Image.new("RGB", (w, h), NAVY); d = ImageDraw.Draw(im)
        up = eout(s_ / 0.45) if a.mode == "open" else 1.0
        x0, y0, x1, y1 = 130, 250 + round(500 * (1 - up)), w - 130, 1000 + round(500 * (1 - up))
        d.rounded_rectangle((x0 + 14, y0 + 18, x1 + 14, y1 + 18), radius=28, fill=(8, 12, 22))                 # shadow
        d.rounded_rectangle((x0, y0, x1, y1), radius=28, fill=PAPER)
        d.rounded_rectangle(((x0 + x1) / 2 - 120, y0 - 34, (x0 + x1) / 2 + 120, y0 + 30), radius=14, fill=(150, 156, 170))   # the clip
        d.text((x0 + 60, y0 + 70), "U.S. ARMY", font=fh_, fill=(120, 128, 145))
        d.text((x0 + 60, y0 + 130), "FACILITY INSPECTION", font=fr_, fill=INK)
        d.line((x0 + 60, y0 + 240, x1 - 60, y0 + 240), fill=(200, 200, 205), width=4)
        for k, r in enumerate(rows):
            p = eout((s_ - 0.45 - 0.22 * k) / 0.25) if a.mode == "open" else 1.0
            if p <= 0:
                continue
            ry = y0 + 290 + 105 * k + round(20 * (1 - p)); c = tuple(int(PAPER[j] + (INK[j] - PAPER[j]) * p) for j in range(3))
            d.rounded_rectangle((x0 + 60, ry, x0 + 128, ry + 68), radius=10, outline=c, width=6)
            d.text((x0 + 160, ry - 8), r, font=fr_, fill=c)
            if a.mode == "passed":                                                           # the ticks, one by one
                q = eout((s_ - 0.25 - 0.28 * k) / 0.2)
                if q > 0:
                    pts = [(x0 + 70, ry + 34), (x0 + 92, ry + 58), (x0 + 140, ry - 6)]
                    seg = q * 2
                    d.line([pts[0], (pts[0][0] + (pts[1][0] - pts[0][0]) * min(seg, 1), pts[0][1] + (pts[1][1] - pts[0][1]) * min(seg, 1))], fill=TEAL, width=14)
                    if seg > 1:
                        f_ = seg - 1
                        d.line([pts[1], (pts[1][0] + (pts[2][0] - pts[1][0]) * f_, pts[1][1] + (pts[2][1] - pts[1][1]) * f_)], fill=TEAL, width=14)
        if a.mode == "passed":
            sp = (s_ - (0.25 + 0.28 * len(rows) + 0.15)) / 0.16
            if sp > 0:
                k = 1 + 1.4 * (1 - eout(min(sp, 1)))
                st = Image.new("RGBA", (620, 230), (0, 0, 0, 0)); sd = ImageDraw.Draw(st)
                sd.rounded_rectangle((8, 8, 612, 222), radius=18, outline=RED + (255,), width=14)
                tw = sd.textlength("PASSED", font=fs_); sd.text((310 - tw / 2, 20), "PASSED", font=fs_, fill=RED + (255,))
                st = st.rotate(-9, Image.BICUBIC, expand=True); st = st.resize((round(st.width * k), round(st.height * k)), Image.LANCZOS)
                im.paste(st, (round(w / 2 - st.width / 2), round(y0 + 620 - st.height / 2)), st)
        out.stdin.write(push(im, t, 0.05).tobytes())
    out.stdin.close(); out.wait()


def inspectors(a):
    """Four simple figures pop in one by one on navy, the last one in teal, with a label ("a group of like four middle-aged older
    ladies", War Dogs 2026-10-23). Abstract icons: no real person is drawn."""
    w, h = a.w, a.h; out = writer(a.out, w, h); N = round(a.dur * FPS)
    n = 4; gap = 220; xs = [w / 2 + (k - (n - 1) / 2) * gap for k in range(n)]; cy = 640
    for i in range(N):
        s_ = i / FPS; t = i / (N - 1)
        im = Image.new("RGB", (w, h), NAVY); d = ImageDraw.Draw(im)
        for k, x in enumerate(xs):
            p = eout((s_ - 0.1 - 0.18 * k) / 0.25)
            if p <= 0:
                continue
            sc = 0.6 + 0.4 * p + 0.1 * math.sin(math.pi * min(p, 1)); col = TEAL if k == n - 1 else (236, 240, 247)
            c = tuple(int(NAVY[j] + (col[j] - NAVY[j]) * min(1, p * 1.4)) for j in range(3))
            hair = tuple(int(NAVY[j] + (c[j] - NAVY[j]) * 0.55) for j in range(3))
            d.rounded_rectangle((x - 92 * sc, cy - 80 * sc, x + 92 * sc, cy + 150 * sc), radius=int(70 * sc), fill=c)   # shoulders
            hy = cy - 150 * sc
            d.rounded_rectangle((x - 72 * sc, hy - 66 * sc, x + 72 * sc, hy + 78 * sc), radius=int(64 * sc), fill=hair)  # a bob of hair
            r = 50 * sc; d.ellipse((x - r, hy - r + 8 * sc, x + r, hy + r + 8 * sc), fill=c)                          # the face
        la = eout((s_ - 0.1 - 0.18 * n) / 0.35)
        if la > 0:
            label(d, a.label or "THE INSPECTORS", w / 2, 860, 96, tuple(int(NAVY[j] + (255 - NAVY[j]) * la) for j in range(3)), 1.0, la)
        out.stdin.write(push(im, t, 0.05).tobytes())
    out.stdin.close(); out.wait()


COLLATERAL = ["CAPTAIN AMERICA", "THE AVENGERS", "BLACK PANTHER", "DOCTOR STRANGE", "ANT-MAN", "HAWKEYE", "NICK FURY", "SHANG-CHI",
              "CLOAK & DAGGER", "POWER PACK"]     # the 2005 Merrill Lynch facility's collateral: theatrical film rights to these ten (SEC 8-K)


def collateral(a):
    """$525,000,000 rolls up ("IN DEBT"), then shrinks to the top while the ten characters whose movie rights secured the loan pop in
    (--t1 s), then a teal plate rises at the bottom: IF THE MOVIES FLOPPED / THE BANK GOT THEM (--t2 s). The caption band (y 1000-1200)
    and the safe bands stay clear. Marvel Studios' 2005 financing; Cuneo, Scott Clary 2026-10-21."""
    w, h = a.w, a.h; out = writer(a.out, w, h); N = round(a.dur * FPS); D = a.dur
    fbig, fn = ImageFont.truetype(ANTON, 172), ImageFont.truetype(ANTON, 64)
    mix = lambda col, q: tuple(int(NAVY[c] + (col[c] - NAVY[c]) * q) for c in range(3))     # fades go to the navy, never to black
    total = 525_000_000
    for i in range(N):
        s = i / FPS; t = i / (N - 1)
        im = Image.new("RGB", (w, h), NAVY); d = ImageDraw.Draw(im)
        rl = lambda x: ease(min(max(x - a.r0, 0) / (a.r1 - a.r0), 1))                   # the roll lands on the spoken number (--r0/--r1 s)
        v = round(total * rl(s)); prev = round(total * rl(s - 1 / FPS))
        g = eout((s - a.t1) / 0.45)                                                   # 0 -> 1: the number moves up and shrinks
        k = 1 - 0.42 * g; y = 330 - 130 * g
        num = Image.new("RGB", (w, 260), NAVY); nd = ImageDraw.Draw(num); txt = f"${v:,}"; tw = nd.textlength(txt, font=fbig)
        nd.text((w / 2 - tw / 2, 10), txt, font=fbig, fill=TEAL if v == total else WHITE)
        if v != prev:
            num = num.filter(ImageFilter.GaussianBlur(min(1.5 + abs(v - prev) / total * 60, 7)))
        if k != 1:
            nw, nh = round(w * k), round(260 * k); num = num.resize((nw, nh), Image.LANCZOS); im.paste(num, ((w - nw) // 2, round(y)))
        else:
            im.paste(num, (0, round(y)))
        la = eout((s - a.r0) / 0.4) * (1 - g)                                                    # "IN DEBT" under the rolling number, gone in phase 2
        if la > 0.01:
            label(d, "IN DEBT", w / 2, 600, 84, mix(WHITE, la), 1.0, eout((s - a.r0) / 0.4))
        if g > 0.01:
            label(d, "SECURED BY THE MOVIE RIGHTS TO", w / 2, 360, 52, mix((150, 165, 190), g), 1.0, g)
            for j, nm in enumerate(COLLATERAL):
                p = eout((s - a.t1 - 0.25 - 0.11 * j) / 0.22)
                if p <= 0:
                    continue
                col, row = j % 2, j // 2; cx = w * (0.28 if col == 0 else 0.72); cy = 470 + row * 98
                dim = 1 - 0.35 * eout((s - a.t2) / 0.4)
                ni = Image.new("RGBA", (520, 90), (0, 0, 0, 0)); ndd = ImageDraw.Draw(ni); tw = ndd.textlength(nm, font=fn)
                ndd.text((260 - tw / 2, 6), nm, font=fn, fill=mix(WHITE, dim) + (255,))
                sc = 0.6 + 0.4 * p + 0.08 * math.sin(math.pi * min(p, 1))                    # pops in with a small overshoot
                ni = ni.resize((round(520 * sc), round(90 * sc)), Image.LANCZOS); ni.putalpha(ni.getchannel("A").point(lambda q: int(q * p)))
                im.paste(ni, (round(cx - ni.width / 2), round(cy - ni.height / 2 + 20 * (1 - p))), ni)
        sp = eout((s - a.t2) / 0.35)
        if sp > 0:
            py = 1290 + 60 * (1 - sp); d.rounded_rectangle((90, py, w - 90, py + 230), radius=26, fill=tuple(int(NAVY[c] + (TEAL[c] - NAVY[c]) * sp) for c in range(3)))
            label(d, "IF THE MOVIES FLOPPED", w / 2, py + 22 - 30, 80, NAVY, sp, 1.0)
            label(d, "THE BANK GOT THEM", w / 2, py + 118 - 30, 80, NAVY, sp, 1.0)
        out.stdin.write(push(im, t, 0.05).tobytes())
    out.stdin.close(); out.wait()


SEGOE, SEGOE_SB, SEGOE_B, INK_FREE = (f"C:/Windows/Fonts/{f}" for f in ("segoeui.ttf", "seguisb.ttf", "segoeuib.ttf", "Inkfree.ttf"))
RED = (229, 56, 59)


def _steps(s):
    """'600@0.9,700@1.3,800@1.7' -> [(600, 0.9), ...]: a number and the second it lands (on the spoken word)."""
    return [(int(v), float(t)) for v, t in (p.split("@") for p in s.split(","))]


def _shoe(src, width, grey=0.0):
    im = Image.open(src).convert("RGBA"); im = im.crop(im.getbbox())
    im = im.resize((width, round(im.height * width / im.width)), Image.LANCZOS)
    if grey:
        g = im.convert("LA").convert("RGBA"); g.putalpha(im.getchannel("A")); im = Image.blend(im, g, grey)
    return im


def _paste_shoe(im, shoe, cx, cy, a=1.0, sc=1.0, glow=0.0):
    """The cutout centred on (cx, cy) with a soft floor shadow; glow > 0 adds a teal halo behind it."""
    s = shoe if sc == 1 else shoe.resize((round(shoe.width * sc), round(shoe.height * sc)), Image.LANCZOS)
    lay = Image.new("RGBA", im.size, (0, 0, 0, 0)); ld = ImageDraw.Draw(lay)
    ld.ellipse((cx - s.width * 0.42, cy + s.height * 0.40, cx + s.width * 0.42, cy + s.height * 0.56), fill=(0, 0, 0, int(150 * a)))
    if glow > 0:
        ld.ellipse((cx - s.width * 0.55, cy - s.height * 0.75, cx + s.width * 0.55, cy + s.height * 0.75), fill=TEAL + (int(120 * glow),))
    lay = lay.filter(ImageFilter.GaussianBlur(40 if glow > 0 else 18))
    sh = s.copy(); sh.putalpha(s.getchannel("A").point(lambda q: int(q * a)))
    lay.alpha_composite(sh, (round(cx - s.width / 2), round(cy - s.height / 2)))
    im.alpha_composite(lay)


def _marker_word(im, text, x, y, size, p, col=RED):
    """A word written on in marker (Ink Free), revealed left to right by p (0 -> 1): written, never stamped."""
    f = ImageFont.truetype(INK_FREE, size); lay = Image.new("RGBA", im.size, (0, 0, 0, 0)); ld = ImageDraw.Draw(lay)
    ld.text((x, y), text, font=f, fill=col + (255,), stroke_width=max(2, size // 40), stroke_fill=col + (255,))
    tw = ld.textlength(text, font=f) + size * 0.2
    m = Image.new("L", im.size, 0); ImageDraw.Draw(m).rectangle((x - 10, y - size * 0.3, x + tw * p, y + size * 1.5), fill=255)
    lay.putalpha(Image.composite(lay.getchannel("A"), Image.new("L", im.size, 0), m)); im.alpha_composite(lay)


def _marker_ring(d, box, p, col=RED, width=12):
    """A hand-drawn ring around box, drawn clockwise by p (0 -> 1), slightly overshooting where it closes."""
    if p > 0:
        d.arc(box, start=-200, end=-200 + 380 * p, fill=col, width=width)


def sneaker(a):
    """The sneaker beats of the Chris Do pricing Short (Scott Clary, 2026-10-24); --src is an RGBA product cutout.
    --mode real:   navy; LIMITED DROP, the shoe rises in, its resale price steps through --steps (600@t,700@t,800@t) on the spoken
                   numbers, the last in teal; an AUTHENTIC tick pops at --t1 ("that's the real one").
    --mode fake:   a sponsored Instagram-style ad on white (same shoe, LIMITED EDITION, Shop now); the price $150 pops at --t1
                   ("Ours is $150"); a red marker ring and FAKE are written on at --t2 ("that's a fake").
    --mode rule:   the two side by side, top = the real one $800, bottom = the fake $150 (FAKE in marker): "pricing is positioning".
    --mode button: the same layout already in; at --t1 the real one lights up teal and the fake dims ("a different kind of buyer").
    The caption band (y 1000-1200) and the safe bands (top 200, bottom 300) stay clear of key visuals."""
    w, h = a.w, a.h; out = writer(a.out, w, h); N = round(a.dur * FPS)
    big, mid, small = ImageFont.truetype(ANTON, 250), ImageFont.truetype(ANTON, 120), ImageFont.truetype(ANTON, 64)
    if a.mode == "real":
        shoe = _shoe(a.src, 900); steps = _steps(a.steps)
        for i in range(N):
            s = i / FPS; t = i / (N - 1)
            im = Image.new("RGBA", (w, h), NAVY + (255,)); d = ImageDraw.Draw(im)
            la = eout((s - 0.1) / 0.35); label(d, "LIMITED DROP", w / 2, 290, 72, (150, 165, 190), la, la)
            up = eout(s / 0.5); _paste_shoe(im, shoe, w / 2, 660 + 90 * (1 - up), a=up)
            cur = [k for k, (v, tt) in enumerate(steps) if s >= tt]
            if cur:
                k = cur[-1]; v, tt = steps[k]; q = eout((s - tt) / 0.18); txt = f"${v:,}"
                num = Image.new("RGBA", (w, 330), (0, 0, 0, 0)); nd = ImageDraw.Draw(num); tw = nd.textlength(txt, font=big)
                nd.text((w / 2 - tw / 2, 20), txt, font=big, fill=(TEAL if k == len(steps) - 1 else WHITE) + (255,))
                if q < 1:
                    num = num.filter(ImageFilter.GaussianBlur(4 * (1 - q)))
                im.alpha_composite(num, (0, round(1230 + 40 * (1 - q))))
                label(d, "RESALE PRICE", w / 2, 1262, 56, (150, 165, 190), eout((s - steps[0][1]) / 0.3), 1.0)   # between the watermark (~1185) and the number's glyph top (~1344)
            tp = (s - a.t1) / 0.25
            if tp > 0:                                                                  # AUTHENTIC: a teal pill with a drawn tick
                k_ = 0.7 + 0.3 * eout(tp) + 0.08 * math.sin(math.pi * min(tp, 1)); pw, ph = 420 * k_, 96 * k_; px, py = w / 2, 920
                d.rounded_rectangle((px - pw / 2, py - ph / 2, px + pw / 2, py + ph / 2), radius=int(ph / 2), fill=TEAL)
                d.line([(px - pw / 2 + 40 * k_, py), (px - pw / 2 + 62 * k_, py + 22 * k_), (px - pw / 2 + 100 * k_, py - 24 * k_)], fill=NAVY, width=int(12 * k_))
                f_ = ImageFont.truetype(ANTON, int(60 * k_)); d.text((px - pw / 2 + 118 * k_, py - 42 * k_), "AUTHENTIC", font=f_, fill=NAVY)
            out.stdin.write(push(im.convert("RGB"), t, 0.04).tobytes())
    elif a.mode == "fake":
        shoe = _shoe(a.src, 760); fh, fs, fsb, fb = (ImageFont.truetype(SEGOE_SB, 46), ImageFont.truetype(SEGOE, 38),
                                                    ImageFont.truetype(SEGOE_B, 52), ImageFont.truetype(SEGOE_SB, 50))
        for i in range(N):
            s = i / FPS; t = i / (N - 1)
            im = Image.new("RGBA", (w, h), NAVY + (255,)); d = ImageDraw.Draw(im)
            up = eout(s / 0.4); oy = round(120 * (1 - up)); x0, x1, y0, y1 = 70, w - 70, 210 + oy, 1600 + oy
            d.rounded_rectangle((x0, y0, x1, y1), radius=34, fill=(255, 255, 255))
            d.ellipse((x0 + 34, y0 + 30, x0 + 124, y0 + 120), fill=(40, 40, 40))         # the shop's avatar
            d.text((x0 + 150, y0 + 32), "kicks.deals.outlet", font=fh, fill=(20, 20, 20))
            d.text((x0 + 150, y0 + 84), "Sponsored", font=fs, fill=(120, 120, 120))
            d.rectangle((x0, y0 + 150, x1, y0 + 760), fill=(242, 242, 242))
            _paste_shoe(im, shoe, w / 2, y0 + 455)
            bw_ = d.textlength("LIMITED EDITION", font=fsb) + 48                         # a badge on the photo (the caption band runs under the image)
            d.rounded_rectangle((x0 + 30, y0 + 175, x0 + 30 + bw_, y0 + 255), radius=40, fill=(20, 20, 20))
            d.text((x0 + 54, y0 + 182), "LIMITED EDITION", font=fsb, fill=(255, 255, 255))
            pp = (s - a.t1) / 0.22                                                      # $150 pops in on "Ours is 150"
            if pp > 0:
                k_ = 0.6 + 0.4 * eout(pp) + 0.1 * math.sin(math.pi * min(pp, 1)); f_ = ImageFont.truetype(ANTON, int(190 * k_))
                d.text((x0 + 40, y0 + 1010 + 40 * (1 - k_)), "$150", font=f_, fill=RED)
            d.rounded_rectangle((x0 + 40, y1 - 150, x1 - 40, y1 - 50), radius=18, fill=(0, 149, 246))
            tw = d.textlength("Shop now", font=fb); d.text((w / 2 - tw / 2, y1 - 136), "Shop now", font=fb, fill=(255, 255, 255))
            rp = eout((s - a.t2) / 0.35)                                                # the ring, then FAKE written on
            _marker_ring(d, (x0 + 10, y0 + 990, x0 + 470, y0 + 1250), rp)
            if s > a.t2 + 0.3:
                _marker_word(im, "FAKE", x0 + 500, y0 + 1000, 170, eout((s - a.t2 - 0.3) / 0.3))
            out.stdin.write(push(im.convert("RGB"), t, 0.04).tobytes())
    else:                                                                               # rule / button: real on top, fake below
        real, fake = _shoe(a.src, 720), _shoe(a.src, 560, grey=0.35)
        for i in range(N):
            s = i / FPS; t = i / (N - 1)
            im = Image.new("RGBA", (w, h), NAVY + (255,)); d = ImageDraw.Draw(im)
            ina = 1.0 if a.mode == "button" else eout(s / 0.3)
            g = eout((s - a.t1) / 0.4) if a.mode == "button" else 0.0                  # the real one lights up, the fake dims
            _paste_shoe(im, real, w / 2, 560, a=ina, sc=1 + 0.06 * g, glow=g)
            tw = d.textlength("$800", font=mid); d.text((w / 2 - tw / 2, 770), "$800", font=mid, fill=tuple(int(c * ina) for c in TEAL))
            fa = ina * (1 - 0.65 * g); fy = 1340 + round(60 * (1 - ina))
            _paste_shoe(im, fake, w / 2 - 150, fy, a=fa)
            fc = tuple(int(NAVY[j] + (RED[j] - NAVY[j]) * fa) for j in range(3))
            d.text((w / 2 + 170, fy - 150), "$150", font=mid, fill=fc)
            if fa > 0.3:
                _marker_word(im, "FAKE", w / 2 + 160, fy + 30, 100, min(1.0, ina), fc)
            out.stdin.write(push(im.convert("RGB"), t, 0.03).tobytes())
    out.stdin.close(); out.wait()


def replies(a):
    """A client thread on navy: his raised rates go out ($$, $$$, $$$$, teal bubbles, right), the client answers Yes, Yes ... and
    a red "No." lands at --t1 ("until they start to say no", Chris Do, 2026-10-24). No invented numbers: the $ signs carry it."""
    w, h = a.w, a.h; out = writer(a.out, w, h); N = round(a.dur * FPS); f = ImageFont.truetype(SEGOE_SB, 72)
    msgs = [("out", "$$"), ("in", "Yes"), ("out", "$$$"), ("in", "Yes"), ("out", "$$$$"), ("in", "No.")]
    gap = max(min((a.t1 - 0.3) / 4, 0.35), 0.12); times = [0.05 + gap * k for k in range(5)] + [a.t1]   # the five land before "No."
    for i in range(N):
        s = i / FPS; t = i / (N - 1)
        im = Image.new("RGB", (w, h), NAVY); d = ImageDraw.Draw(im)
        for k, ((side, txt), tt) in enumerate(zip(msgs, times)):
            p = eout((s - tt) / 0.22)
            if p <= 0:
                continue
            tw = d.textlength(txt, font=f); bw, bh = tw + 100, 124; y = 240 + 124 * k + round(30 * (1 - p))
            last = k == len(msgs) - 1; col = TEAL if side == "out" else (RED if last else (226, 232, 240))
            x = w - 90 - bw if side == "out" else 90
            sc = 0.85 + 0.15 * p + (0.12 * math.sin(math.pi * min(p, 1)) if last else 0)
            bx0, by0 = x + bw * (1 - sc) / 2, y + bh * (1 - sc) / 2
            c = tuple(int(NAVY[j] + (col[j] - NAVY[j]) * p) for j in range(3))
            d.rounded_rectangle((bx0, by0, bx0 + bw * sc, by0 + bh * sc), radius=int(48 * sc), fill=c)
            tc = NAVY if side == "out" else ((255, 255, 255) if last else NAVY)
            d.text((bx0 + 50 * sc, by0 + 12 * sc), txt, font=ImageFont.truetype(SEGOE_SB, int(72 * sc)), fill=tuple(int(NAVY[j] + (tc[j] - NAVY[j]) * p) for j in range(3)))
        out.stdin.write(push(im, t, 0.04).tobytes())
    out.stdin.close(); out.wait()


def dayrate(a):
    """HIS DAY RATE: the number steps through --steps (250@t,300@t,...) on the spoken numbers, each change sliding up with motion
    blur, the last one teal, "/ DAY" under it; under the caption band a bar for each rate rises as it lands (Chris Do, 2026-10-24)."""
    w, h = a.w, a.h; out = writer(a.out, w, h); N = round(a.dur * FPS); steps = _steps(a.steps)
    big = ImageFont.truetype(ANTON, 300); top = max(v for v, _ in steps)
    for i in range(N):
        s = i / FPS; t = i / (N - 1)
        im = Image.new("RGB", (w, h), NAVY); d = ImageDraw.Draw(im)
        label(d, a.label or "HIS DAY RATE", w / 2, 270, 72, (150, 165, 190), eout(s / 0.3), eout(s / 0.3))
        cur = [k for k, (v, tt) in enumerate(steps) if s >= tt]
        if cur:
            k = cur[-1]; v, tt = steps[k]; q = eout((s - tt) / 0.16); txt = f"${v:,}"
            num = Image.new("RGB", (w, 380), NAVY); nd = ImageDraw.Draw(num); tw = nd.textlength(txt, font=big)
            nd.text((w / 2 - tw / 2, 10), txt, font=big, fill=TEAL if k == len(steps) - 1 else WHITE)
            if q < 1:
                num = num.filter(ImageFilter.GaussianBlur(5 * (1 - q)))
            im.paste(num, (0, round(400 + 50 * (1 - q))))
            label(d, "/ DAY", w / 2, 800, 96, WHITE, 1.0, 1.0)
        n = len(steps); bw = 120; gap = 46; x0 = w / 2 - (n * bw + (n - 1) * gap) / 2; base = 1600
        for k, (v, tt) in enumerate(steps):                                            # the bars under the caption band
            p = eout((s - tt) / 0.3)
            if p <= 0:
                continue
            bh = 340 * v / top * p; x = x0 + k * (bw + gap)
            d.rounded_rectangle((x, base - bh, x + bw, base), radius=14, fill=TEAL if k == n - 1 else (90, 108, 140))
        out.stdin.write(push(im, t, 0.04).tobytes())
    out.stdin.close(); out.wait()


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("kind", choices=["dots", "counter", "calendar", "tvoff", "collateral", "craigslist", "inspection", "inspectors",
                                     "sneaker", "replies", "dayrate"]); ap.add_argument("out")
    ap.add_argument("--steps", default="")
    ap.add_argument("--t1", type=float, default=3.0); ap.add_argument("--t2", type=float, default=6.3)
    ap.add_argument("--money", action="store_true"); ap.add_argument("--mode", default="open")
    ap.add_argument("--r0", type=float, default=0.0); ap.add_argument("--r1", type=float, default=1.6)
    ap.add_argument("--n", type=int, default=3000); ap.add_argument("--to", type=int, default=50); ap.add_argument("--label", default="")
    ap.add_argument("--src"); ap.add_argument("--cx", type=float, default=0.5); ap.add_argument("--dur", type=float, default=3.0); ap.add_argument("--w", type=int, default=1080); ap.add_argument("--h", type=int, default=1920)
    a = ap.parse_args()
    {"dots": dots, "counter": counter, "calendar": calendar, "tvoff": tvoff, "collateral": collateral, "craigslist": craigslist, "inspection": inspection, "inspectors": inspectors,
     "sneaker": sneaker, "replies": replies, "dayrate": dayrate}[a.kind](a)
    print("done", a.out)
