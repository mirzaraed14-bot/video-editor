"""overlays.py: render a reaction job's overlay layers from its plan.json (Affan's Tella brief, 2026-10-07).

  PYTHONUTF8=1 python overlays.py <job>/plan.json [--captions] [--mg] [--only <id>] [--still <t>] [--check]

  --captions  hf-free caption layer: one PNG per chunk (Bebas Neue, white, thin black stroke, no animation, centred on the
              split seam y 1038, ONE constant position) -> <job>/overlays/captions.mov (ProRes 4444 alpha, 30 fps, full length)
  --mg        every plan graphic -> <job>/overlays/mg/<id>.mov (ProRes 4444 alpha, 60 fps, exactly t1 - t0 long)
  --still t   write <job>/work/overlay-<t>.png (all layers at sequence time t) for review
  --check     the plan checker (after --captions): ERRORS (exit 1) and WARNINGS, see check() below; also planlib.check(plan_path)

Captions follow his reference reel (instagram.com/p/DbY2vIKtwvV): 1-3 words, uppercase, no animation; while the reviewed
video plays the caption reads *VIDEO* (his reference does exactly that). Punctuation: ! ? and quotes only (captext.clean).

Graphic kinds (plan["graphics"][], every one {id, kind, t0, t1, [sfx]}; "box" = a plan["boxes"] name, source px of the OBS
screen recording, or a literal [x0, y0, x1, y1]):
  label, title_card, channel_card, lower_third, stat, checklist, compare, steps, mock_title, arrow, underline, move,
  distance, group                     the batch-1/2 kinds (keys: see each sprite / frame function)
2026-10-13 additions (research-2026-10-13.md; no new key = today's output, byte for byte):
  placement   align "left" (the card's LEFT edge at x, default 56) | "right" (its right edge at x, default 1024), cy = y, on
              label / title_card / channel_card / lower_third / stat / checklist / compare / steps / chip; w = the card
              width on title_card / checklist / compare / steps (verdict cards: 760; long rows shrink to fit)
  rich text   "*word*" in a label / title / steps + checklist title / compare line / stat label / lower_third title /
              hook_title line: that word in plan["accent_font"] (default Playfair Display Italic), gold, cap height matched
              to the base face, on its baseline (a gold title turns white so its accent word carries the gold);
              plan["accent_weight"] / ["accent_opsz"] set a variable accent font's axes
  card_style  plan["card_style"] = "glass": every card a #1C1C1C -> #0C0C0C gradient @ 235 + a 1 px inner top highlight
  entrance    g["entrance"] overrides plan["entrance"]: "pop" | "rise" | "wipe" (a left->right mask reveal 0.36 s
              easeInOutCubic + a 12 px slide, fade out 0.24 s) | "lift" (scale 0.35 -> 1 from g["from_xy"] frame px in
              0.4 s easeOutBack 1.2, fading in over 0.15 s)
  showcase    the frame around our sample while it plays (FRAME track, see apply.py): box (our sample's video area), tag,
              tag2, blur (36), dim (0.35): the screen's own picture of that box, blurred + darkened, fills the
              panel outside the card (and its r 28 corner wedges), a hairline + shadow on the card edge; the view must be
              static across [t0, t1]
  ba_wipe     before / after = {"src": "obs", "t": <OBS s at t0>, "box": name} | {"file": <path>, "t": <s at t0>}; 520x924
              card in the panel, blurred `after` backdrop (opaque over the panel); wipe_at (s after t0, default 1.0),
              wipe_dur (0.7), park (s, optional: the line rests at x 540), dir "ltr" (default: the 4 px line travels left ->
              right, OURS opens behind it on the left) | "rtl" (ORIGINAL left / OURS right at the park); tags [before, after]
              (default ["ORIGINAL", "OURS"]) ride their own side's outer top corner
  ba_pair     before / after as ba_wipe, two 470x836 cards (x 65..535 / 545..1015), the right one rises 0.3 s after the
              left; labels (default ["ORIGINAL", "OURS"]), labels_at "above" (default) | "top" | "bottom" (inside the card)
  spotlight   box, pad (16), tag (optional Bebas tag docked outside the hole with a 2 px leader): the panel dims to 45 %
              black except a rounded hole (r 18, 10 px feather); follows the view per frame
  select      box, pad (8), chip (optional IBM Plex Mono 22 chip above the top-left corner), draw_at (s after t0, 0):
              a 2 px white outline drawn round the box in 0.3 s + four 12 px handles; follows the view per frame
  cursor      box, at "br" (default) | "tl" | "center", click_at (s after t0, 0.55), glide (0.55): a macOS arrow gliding in
              from target + (220, 260), a click squash + ripple ring; follows the view per frame
  loupe       box, mag (2.2 x the panel's display scale), r (150), rest ([x, y] frame px; default 60 px clear of the target
              on the roomier side), live (false: one still of the screen at t0 + 0.3; true: the playing screen)
  timecode    box, steps [[t_abs, "0:03 / 0:41"], ...], dock "tl" (default) | "tr" | "bl" | "br" (above_scrub: true lifts a
              bottom dock clear of a scrub bar): a mono chip 16 px inside the box's corner, 0.12 s cross-fades
  scrub       box, p0 / p1 (fractions across the graphic) or keys [[t_abs, frac], ...], ticks [[t_abs, frac(, sfx)], ...]:
              a 6 px bar along the box's bottom edge, gold fill, a playhead dot, gold ticks that pop and stay
  (the screen marks spotlight / select / cursor / loupe / timecode / scrub are clipped to the panel box; in a group the
  cursor goes LAST so it sits on top of the select it clicks)
  hook_title  line1 (Bebas 60, white 80 %), line2 (the accent font 84, gold; "*word*" spans make it rich Bebas), y (1450)
  chip        avatar ({"src": "file", "path"}, optional), name, sub (optional), verified (optional), x, y, align
  channel_card  + flip_at (abs s) + flip_to (box): from flip_at the card flies into the box (mapped through the view at
              flip_at + 0.05) in 0.45 s easeInOutCubic, scaling to its height, fading out over the last 0.15 s
plan["seam_line"]["draw"] = 0.22: at each face-only beat's end the seam line grows from the centre outward (outCubic, 60 fps).
DEFAULT_SFX / default_sfx(g): the tiered SFX palette per kind (research #12) for build_plan scripts; apply.py reads g["sfx"].
"""
import json, math, os, subprocess, sys, tempfile, shutil
from PIL import Image, ImageChops, ImageDraw, ImageEnhance, ImageFilter, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", "..", "..", "..", ".."))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(REPO, "presets", "youtube-shorts", "onyx-samples", "kit"))
import geom as G                 # noqa: E402
from captext import clean        # noqa: E402

W, H = G.W, G.H
SEAM = 1038
FPS_MG, FPS_CAP = 60, 30
GOLD = (232, 196, 104)
BEBAS = next(p for p in ("C:/Windows/Fonts/BebasNeue-Regular.ttf", os.path.expanduser("~/AppData/Local/Microsoft/Windows/Fonts/BebasNeue-Regular.ttf"))
             if os.path.exists(p))
INTER_B = os.path.join(REPO, "assets", "fonts", "Inter-Bold.otf")
INTER_R = os.path.join(REPO, "assets", "fonts", "Inter-Regular.otf")
INTER_K = os.path.join(REPO, "assets", "fonts", "Inter-Black.otf")
PLAYFAIR_I = os.path.join(REPO, "assets", "fonts", "PlayfairDisplay-Italic-VF.ttf")
PLEX_MONO = next((p for p in ("C:/Windows/Fonts/IBMPlexMono-Medium.ttf", os.path.expanduser("~/AppData/Local/Microsoft/Windows/Fonts/IBMPlexMono-Medium.ttf"),
                              "C:/Windows/Fonts/IBMPlexMono-Regular.ttf") if os.path.exists(p)), INTER_B)
FILLERS = {"uh", "um", "uhm", "erm"}
CARD_STYLE = None                # plan["card_style"]: None = the flat batch-2 card, "glass" = the gradient card (research #9)
ACCENT_FONT, ACCENT_AXES = PLAYFAIR_I, {}


# ---------- plan helpers ----------
def load(plan_path):
    plan = json.load(open(plan_path, encoding="utf-8"))
    plan["_dir"] = os.path.dirname(os.path.abspath(plan_path))
    global SEAM, ENTRANCE, CARD_STYLE, ACCENT_FONT, ACCENT_AXES
    SEAM = plan.get("seam", SEAM); G.configure(plan); ENTRANCE = plan.get("entrance", "pop")       # Seq 37/38: the screen sits above the face, the seam is y 1066
    CARD_STYLE = plan.get("card_style")
    ACCENT_FONT = plan.get("accent_font") or PLAYFAIR_I
    if not os.path.isabs(ACCENT_FONT) and not os.path.exists(ACCENT_FONT): ACCENT_FONT = os.path.join(REPO, ACCENT_FONT)
    ACCENT_AXES = {k: plan[p] for k, p in (("Weight", "accent_weight"), ("Optical size", "accent_opsz")) if plan.get(p) is not None}
    seq = next(s for s in json.load(open(os.path.join(plan["_dir"], plan["dump"]))) if s["name"] == plan["sequence"])
    return plan, seq


def ease(x):                     # easeOutCubic
    x = min(max(x, 0.0), 1.0); return 1 - (1 - x) ** 3


def ease_back(x, k=1.6):        # easeOutBack, a small overshoot
    x = min(max(x, 0.0), 1.0); return 1 + (k + 1) * (x - 1) ** 3 + k * (x - 1) ** 2


named, view_at = G.named, G.view_at


def src_to_frame(view, x, y):
    s = G.BASE * view["z"]
    bx, by = (G.BOX[0] + G.BOX[2]) / 2, (G.BOX[1] + G.BOX[3]) / 2
    return bx + (x - view["cx"]) * s, by + (y - view["cy"]) * s


ease_io3 = G.EASES["inOutCubic"]
clamp01 = lambda x: min(max(x, 0.0), 1.0)


def box_src(plan, box):
    return list(plan["boxes"][box]) if isinstance(box, str) else list(box)


def box_at(plan, name, t_abs, pad=0.0):
    """plan.boxes[name] (source px; or a literal [x0, y0, x1, y1]) mapped through the view at sequence time t_abs, in frame px,
    grown by pad; None while a face-only beat is up. The 2026-10-13 marks call it on EVERY frame, so they stay locked on their
    target through an eased zoom or a drift."""
    v = view_at(plan, t_abs)
    if v is None: return None
    b = box_src(plan, name)
    a = src_to_frame(v, b[0], b[1]); c = src_to_frame(v, b[2], b[3])
    return (a[0] - pad, a[1] - pad, c[0] + pad, c[1] + pad)


def fade_al(t, dur, t_in, t_out, ez=None):
    ez = ez or ease
    if t_in > 0 and t < t_in: return ez(t / t_in)
    if t_out > 0 and t > dur - t_out: return 1 - ez((t - (dur - t_out)) / t_out)
    return 1.0


def with_alpha(im, al):
    if al >= 1: return im
    im = im.copy(); im.putalpha(im.split()[3].point(lambda v: int(v * al))); return im


# ---------- rich text: "*word*" in the accent face (research #9 / #13) ----------
_FONTS = {}


def font_at(path, size, axes=None):
    key = (path, int(size), tuple(sorted((axes or {}).items())))
    if key not in _FONTS:
        f = ImageFont.truetype(path, int(size))
        if axes:
            try:
                ax = f.get_variation_axes()
                vals = []
                for a in ax:
                    n = a.get("name"); n = n.decode() if isinstance(n, bytes) else n
                    vals.append(axes.get(n, a["default"]))
                f.set_variation_by_axes(vals)
            except OSError:
                pass
        _FONTS[key] = f
    return _FONTS[key]


def cap_h(f):
    return -f.getbbox("H", anchor="ls")[1]


def accent_axes(path):
    """a variable accent face's axes: the plan's accent_weight / accent_opsz, else Medium for a Light-default face (Cormorant)
    and a display optical size (Bodoni Moda) so the hairlines survive a phone's compression"""
    ax = dict(ACCENT_AXES)
    try:
        for a in ImageFont.truetype(path, 40).get_variation_axes():
            n = a.get("name"); n = n.decode() if isinstance(n, bytes) else n
            if n == "Weight" and "Weight" not in ax and a["default"] < 400: ax["Weight"] = 500
            if n == "Optical size" and "Optical size" not in ax: ax["Optical size"] = min(a["maximum"], max(a["minimum"], 28))
    except OSError:
        pass
    return ax


def accent_for(fb):
    """the accent face size-matched to a base font: its cap height equals the base face's"""
    ax = accent_axes(ACCENT_FONT)
    probe = font_at(ACCENT_FONT, fb.size, ax)
    return font_at(ACCENT_FONT, max(1, round(fb.size * cap_h(fb) / max(1, cap_h(probe)))), ax)


def is_rich(text):
    return isinstance(text, str) and text.count("*") >= 2 and text.count("*") % 2 == 0


def rich_runs(text):
    return [(p, i % 2 == 1) for i, p in enumerate(text.split("*")) if p]


def rich_len(text, fb):
    if not is_rich(text): return ImageDraw.Draw(Image.new("RGBA", (1, 1))).textlength(text, font=fb)
    fa = accent_for(fb); d = ImageDraw.Draw(Image.new("RGBA", (1, 1)))
    return sum(d.textlength(s, font=fa) + 0.04 * fa.size if a else d.textlength(s, font=fb) for s, a in rich_runs(text))


def draw_rich(d, xy, text, fb, fill, anchor="la", accent=None):
    """d.text(xy, text, font=fb, fill=fill, anchor=anchor), except that "*word*" spans take the accent face (gold), on the
    base face's baseline. Plain text goes through d.text untouched (byte-identical to the batch-2 call)."""
    if not is_rich(text):
        d.text(xy, text, font=fb, fill=fill, anchor=anchor); return
    fa = accent_for(fb); acc = accent or GOLD + (255,)
    fill = tuple(fill)
    if fill[:3] == GOLD: fill = (255, 255, 255) + fill[3:]          # a gold title turns white: the accent word carries the gold
    runs = rich_runs(text); total = rich_len(text, fb)
    x, y = xy
    if anchor[0] == "m": x -= total / 2
    elif anchor[0] == "r": x -= total
    va = anchor[1] if len(anchor) > 1 else "a"
    base = y + d.textbbox((0, 0), "H", font=fb, anchor="l" + va)[3] - d.textbbox((0, 0), "H", font=fb, anchor="ls")[3]
    for s, a in runs:
        f = fa if a else fb
        d.text((x, base), s, font=f, fill=acc if a else fill, anchor="ls")
        x += d.textlength(s, font=f) + (0.04 * fa.size if a else 0)


def wrap_rich(text, fb, maxw):
    """word-wrap rich text: each line keeps its own *...* spans"""
    toks = []
    for s, a in rich_runs(text):
        for wd in s.split():
            toks.append((wd, a))
    lines, cur = [], []
    enc = lambda ts: " ".join(f"*{w}*" if a else w for w, a in ts)
    for tk in toks:
        if cur and rich_len(enc(cur + [tk]), fb) > maxw: lines.append(enc(cur)); cur = [tk]
        else: cur.append(tk)
    lines.append(enc(cur))
    return lines


# ---------- card styles ----------
def glass_rect(size, radius, outline=None, width=0, ss=2, alpha=235):
    """research #9: a vertical gradient #1C1C1C -> #0C0C0C @ 235, a 1 px inner top highlight (white @ 10 %), the same
    radius and hairline as the flat card"""
    w, h = size; W2, H2 = w * ss, h * ss
    col = Image.linear_gradient("L").resize((W2, H2)).point(lambda v: int(round(28 + (12 - 28) * v / 255)))
    im = Image.merge("RGB", (col, col, col)).convert("RGBA")
    m = Image.new("L", (W2, H2), 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, W2 - 1, H2 - 1), radius * ss, fill=alpha); im.putalpha(m)
    hl = Image.new("L", (W2, H2), 0); iw = max(1, width) * ss
    ImageDraw.Draw(hl).rounded_rectangle((iw, iw, W2 - 1 - iw, H2 - 1 - iw), max(1, radius - max(1, width)) * ss, outline=26, width=ss)
    ramp = Image.linear_gradient("L").resize((1, max(2, radius * ss))).point(lambda v: 255 - v).resize((W2, max(2, radius * ss)))
    fade = Image.new("L", (W2, H2), 0); fade.paste(ramp, (0, 0))
    lay = Image.new("RGBA", (W2, H2), (255, 255, 255, 0)); lay.putalpha(ImageChops.multiply(hl, fade)); im.alpha_composite(lay)
    if outline and width:
        ol = Image.new("RGBA", (W2, H2), (0, 0, 0, 0)); ImageDraw.Draw(ol).rounded_rectangle((0, 0, W2 - 1, H2 - 1), radius * ss, outline=outline, width=width * ss)
        im.alpha_composite(ol)
    return im.resize((w, h), Image.LANCZOS)


def card_body(size, radius, fill, outline=None, width=0, ss=2):
    """every card body: the flat batch-2 rrect, or the glass card when plan["card_style"] == "glass\""""
    if CARD_STYLE == "glass": return glass_rect(size, radius, outline=outline, width=width, ss=ss)
    return rrect(size, radius, fill, outline=outline, width=width, ss=ss)


def card_cx(g, sp, default=None):
    """the card's centre x: align "left" puts its left edge at x (default 56), "right" its right edge at x (default 1024);
    no align = today's centring (W / 2, or g["x"] for the kinds that already read it)"""
    al = g.get("align")
    if al == "left": return g.get("x", 56) + sp.width / 2
    if al == "right": return g.get("x", W - 56) - sp.width / 2
    return W / 2 if default is None else default


def fit_font(path, size, texts, maxw, minsize):
    """the largest size <= size at which every text (rich-aware) fits maxw"""
    for sz in range(size, minsize - 1, -1):
        f = ImageFont.truetype(path, sz)
        if all(rich_len(x, f) <= maxw for x in texts): return f
    return ImageFont.truetype(path, minsize)


# ---------- captions ----------
def caption_chunks(plan):
    words = json.load(open(os.path.join(plan["_dir"], "transcript", "seqwords.json"), encoding="utf-8"))
    vids = plan.get("video", [])
    invid = lambda t: any(a - 0.05 <= t <= b + 0.05 for a, b in vids)
    mine = [w for w in words if not invid((w["start"] + w["end"]) / 2) and clean(w["w"]).lower().strip("!?\"'") not in FILLERS and clean(w["w"])]
    for fx in plan.get("caption_fixes", []):                 # {"at": t, "w": "TEXT"} replaces the word starting at t ("" drops it)
        for w in mine:
            if abs(w["start"] - fx["at"]) < 0.03: w["w"] = fx["w"]
    mine = [w for w in mine if w["w"]]
    # glue: a word listed in plan.glue rides with the next one ("Mr." + "Chris")
    glue, out_ = {g.lower() for g in plan.get("glue", [])}, []
    for w in mine:
        if out_ and out_[-1]["w"].lower() in glue and w["start"] - out_[-1]["end"] < 0.6:
            out_[-1] = dict(out_[-1], w=clean(out_[-1]["w"]) + " " + w["w"], end=w["end"])
        else:
            out_.append(dict(w))
    mine = out_
    # drop stutters (a word repeated back to back: "the the", "this this")
    ded = []
    for w in mine:
        if ded and clean(w["w"]).lower() == clean(ded[-1]["w"]).lower() and w["start"] - ded[-1]["end"] < 0.7                 and ded[-1]["w"].rstrip()[-1:] not in ".?!,":
            continue
        ded.append(w)
    # phrases: split at sentence punctuation, pauses > 0.35 s and cuts with a pause; then balanced chunks of <= 3 words / 16 chars
    phrases, cur = [], []
    for w in ded:
        if cur and (w["start"] - cur[-1]["end"] > 0.35 or w["clip"] != cur[-1]["clip"]):
            phrases.append(cur); cur = []
        cur.append(w)
        if w["w"].rstrip()[-1:] in ".?!,":
            phrases.append(cur); cur = []
    if cur: phrases.append(cur)
    chunks = []
    txt = lambda ws: " ".join(clean(x["w"]).upper() for x in ws).replace(" ", " ")
    for ph in phrases:                      # greedy <= 3 words / 16 chars, then no one-word orphan at the end of a phrase
        parts, cur = [], []
        for w in ph:
            if cur and (len(cur) == 3 or len(txt(cur + [w])) > 16):
                parts.append(cur); cur = []
            cur.append(w)
        if cur: parts.append(cur)
        if len(parts) >= 2 and len(parts[-1]) == 1 and len(parts[-2]) >= 2 and len(txt(parts[-2][-1:] + parts[-1])) <= 16:
            parts[-1] = parts[-2][-1:] + parts[-1]; parts[-2] = parts[-2][:-1]
        i = 0
        while i < len(parts):
            if len(parts) > 1 and len(parts[i]) == 1 and len(txt(parts[i])) <= 4:
                if i + 1 < len(parts) and len(txt(parts[i] + parts[i + 1])) <= 18 and len(parts[i + 1]) <= 3:
                    parts[i:i + 2] = [parts[i] + parts[i + 1]]; continue
                if i > 0 and len(txt(parts[i - 1] + parts[i])) <= 18 and len(parts[i - 1]) <= 3:
                    parts[i - 1:i + 1] = [parts[i - 1] + parts[i]]; i -= 1; continue
            i += 1
        for pp in parts:
            chunks.append(dict(t0=pp[0]["start"], t1=pp[-1]["end"], text=txt(pp)))
    for a, b in vids:
        chunks.append(dict(t0=a, t1=b, text="*VIDEO*"))
    chunks.sort(key=lambda c: c["t0"])
    # hold each chunk until the next one (gaps under 0.6 s), never past the next start; drop overlaps
    out = []
    for i, c in enumerate(chunks):
        nxt = chunks[i + 1]["t0"] if i + 1 < len(chunks) else plan["end"]
        end = nxt if nxt - c["t1"] < 0.6 else c["t1"] + 0.25
        c["t1"] = round(min(end, nxt), 3)
        if c["t1"] - c["t0"] > 0.05:
            out.append(c)
    return out


def caption_png(text, size=96):
    f = ImageFont.truetype(BEBAS, size)
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    l, t, r, b = d.textbbox((0, 0), text, font=f, stroke_width=5)
    x, y = (W - (r - l)) / 2 - l, SEAM - (b - t) / 2 - t
    sh = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(sh).text((x, y + 4), text, font=f, fill=(0, 0, 0, 150), stroke_width=7, stroke_fill=(0, 0, 0, 150))
    im = Image.alpha_composite(im, sh.filter(ImageFilter.GaussianBlur(6)))
    ImageDraw.Draw(im).text((x, y), text, font=f, fill=(255, 255, 255, 255), stroke_width=5, stroke_fill=(0, 0, 0, 255))
    return im


def seam_line_png(w=4, frac=1.0):
    """Affan 2026-10-12: "when I do split screens I always have a white line in the middle… it feels organized"; the captions
    sit ON it. A thin white line across the seam, drawn only while the screen is split (never over a face-only beat).
    frac < 1: the line part-drawn, frac x 1080 px wide, centred (the draw-on when the split returns, research #15)."""
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    if frac >= 1:
        ImageDraw.Draw(im).rectangle((0, SEAM - w // 2, W, SEAM - w // 2 + w - 1), fill=(255, 255, 255, 255))
        return im
    ss = 4; half = W * frac / 2
    if half <= 0: return im
    lay = Image.new("RGBA", (W * ss, (w + 4) * ss), (0, 0, 0, 0))
    ImageDraw.Draw(lay).rectangle((round((W / 2 - half) * ss), 2 * ss, round((W / 2 + half) * ss) - 1, (2 + w) * ss - 1), fill=(255, 255, 255, 255))
    im.alpha_composite(lay.resize((W, w + 4), Image.LANCZOS), (0, SEAM - w // 2 - 2))
    return im


def seam_frac(plan, t):
    """how much of the seam line shows at sequence time t: 1.0, or the draw-on (plan["seam_line"]["draw"] s, outCubic, per
    60 fps frame) right after a face-only beat ends"""
    d = (plan.get("seam_line") or {}).get("draw")
    if not d: return 1.0
    nf = max(1, int(round(d * 60)))
    for f in plan.get("face", []):
        if f["t1"] < plan["end"] - 1e-6 and f["t1"] - 1e-6 <= t < f["t1"] + nf / 60 - 1e-6:
            k = max(0, int((t - f["t1"]) * 60 + 1e-6)); return ease((k + 1) / nf)
    return 1.0


def build_captions(plan):
    out = os.path.join(plan["_dir"], "overlays"); cdir = os.path.join(out, "captions"); os.makedirs(cdir, exist_ok=True)
    chunks = caption_chunks(plan)
    json.dump(chunks, open(os.path.join(out, "captions.json"), "w", encoding="utf-8"), indent=0, ensure_ascii=False)
    sl = plan.get("seam_line")                      # {"w": 4}: the line UNDER the captions, on every split frame
    faces = [(f["t0"], f["t1"]) for f in plan.get("face", [])]
    split_at = lambda t: not any(a - 1e-4 <= t < b - 1e-4 for a, b in faces)
    draw = (sl or {}).get("draw")                  # research #15: the line grows back from the centre when the split returns
    anim = set()
    if draw:
        nf = max(1, int(round(draw * 60)))
        anim = {f["t1"] + k / 60 for f in plan.get("face", []) if f["t1"] < plan["end"] - 1e-6 for k in range(nf + 1)}
    cuts = sorted({0.0, plan["end"]} | {c[k] for c in chunks for k in ("t0", "t1")} | ({x for f in faces for x in f} if sl else set()) | anim)
    cuts = [x for x in cuts if 0 <= x <= plan["end"]]
    line_im = seam_line_png(sl.get("w", 4)) if sl else None
    cache, lines = {}, []
    for a, b in zip(cuts, cuts[1:]):
        if b - a < 1e-4: continue
        m = (a + b) / 2
        ci = next((i for i, c in enumerate(chunks) if c["t0"] - 1e-6 <= m < c["t1"]), None)
        ln = bool(sl) and split_at(m)
        q = seam_frac(plan, m) if (draw and ln) else 1.0
        key = (ci, ln) if q >= 1 else (ci, ln, round(q, 5))
        if key not in cache:
            im = (line_im.copy() if q >= 1 else seam_line_png(sl.get("w", 4), q)) if ln else Image.new("RGBA", (W, H), (0, 0, 0, 0))
            if ci is not None: im = Image.alpha_composite(im, caption_png(chunks[ci]["text"]))
            tag = "" if q >= 1 else f"_d{int(round(q * 10000)):05d}"
            path = os.path.join(cdir, f"c{ci if ci is not None else 'none'}{'_l' if ln else ''}{tag}.png"); im.save(path); cache[key] = path
        if draw:                                   # 1/60 s segments: the image demuxer's own 1/25 s clock would merge them
            lines += [f"file '{cache[key]}'", "option framerate 60", f"duration {b - a:.6f}"]
        else:
            lines += [f"file '{cache[key]}'", f"duration {b - a:.4f}"]
    lines += lines[-3:-1] if draw else [lines[-2]]
    lst = os.path.join(cdir, "list.txt"); open(lst, "w").write("\n".join(x.replace("\\", "/") for x in lines))
    mov = os.path.join(out, plan.get("captions_file", "captions.mov"))   # a new name when Premiere holds the old one (relink with changeMediaPath)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-vf", f"fps={plan.get('cap_fps', 60 if plan.get('seam_line') else FPS_CAP)}", "-t", f"{plan['end']:.3f}",
                    "-c:v", "prores_ks", "-profile:v", "4444", "-pix_fmt", "yuva444p10le", "-vendor", "apl0", mov], check=True)
    print(f"captions: {len(chunks)} chunks -> {mov}")
    return chunks


# ---------- motion graphics ----------
def rrect(size, radius, fill, outline=None, width=0, ss=2):
    w, h = size
    im = Image.new("RGBA", (w * ss, h * ss), (0, 0, 0, 0))
    ImageDraw.Draw(im).rounded_rectangle((0, 0, w * ss - 1, h * ss - 1), radius * ss, fill=fill, outline=outline, width=width * ss)
    return im.resize((w, h), Image.LANCZOS)


def soft_shadow(sprite, blur=18, alpha=140, dy=8):
    pad = blur * 3
    sh = Image.new("RGBA", (sprite.width + 2 * pad, sprite.height + 2 * pad), (0, 0, 0, 0))
    a = sprite.split()[3].point(lambda v: v * alpha // 255)
    blk = Image.new("RGBA", sprite.size, (0, 0, 0, 255)); blk.putalpha(a)
    sh.paste(blk, (pad, pad + dy), blk)
    sh = sh.filter(ImageFilter.GaussianBlur(blur))
    sh.alpha_composite(sprite, (pad, pad))
    return sh, pad


def avatar_img(plan, seq, g, d):
    a = g["avatar"]
    if a.get("src") == "file":          # the channel's REAL profile picture (Affan 2026-10-08: "his pfp youtube, not a freeze frame")
        im = Image.open(os.path.join(plan["_dir"], a["path"])).convert("RGB"); s = min(im.size)
        im = im.crop(((im.width - s) // 2, (im.height - s) // 2, (im.width + s) // 2, (im.height + s) // 2)).resize((d * 2, d * 2), Image.LANCZOS)
    else:
        tr = seq["v"][plan["screen_track"]]
        c = G.clip_at(tr, a["t"]); im = G.frame(c["p"], G.src_time(c, a["t"])).crop(tuple(a["box"])).resize((d * 2, d * 2), Image.LANCZOS)
    m = Image.new("L", (d * 2, d * 2), 0); ImageDraw.Draw(m).ellipse((0, 0, d * 2 - 1, d * 2 - 1), fill=255)
    out = Image.new("RGBA", (d * 2, d * 2), (0, 0, 0, 0)); out.paste(im, (0, 0), m)
    return out.resize((d, d), Image.LANCZOS)


def verified(d):
    im = Image.new("RGBA", (d * 4, d * 4), (0, 0, 0, 0)); dr = ImageDraw.Draw(im)
    dr.ellipse((0, 0, d * 4 - 1, d * 4 - 1), fill=(170, 170, 170, 255))
    dr.line([(d * 1.0, d * 2.1), (d * 1.75, d * 2.85), (d * 3.05, d * 1.35)], fill=(18, 18, 18, 255), width=int(d * 0.55), joint="curve")
    return im.resize((d, d), Image.LANCZOS)


def sprite_channel_card(plan, seq, g):
    w, h = 940, 184
    card = card_body((w, h), 40, (16, 16, 16, 238), outline=(255, 255, 255, 38), width=2)
    av = avatar_img(plan, seq, g, 128); card.alpha_composite(av, (28, (h - 128) // 2))
    d = ImageDraw.Draw(card)
    fn, fs = ImageFont.truetype(INTER_B, 44), ImageFont.truetype(INTER_R, 27)
    x = 28 + 128 + 28
    d.text((x, 44), g["name"], font=fn, fill=(255, 255, 255, 255))
    nw = d.textlength(g["name"], font=fn)
    if g.get("verified", True):      # 2026-10-19: "verified": false for a channel without YouTube's badge (TFTC); default = the old card
        card.alpha_composite(verified(30), (int(x + nw + 12), 56))
    d.text((x, 108), f"{g['handle']} \u00b7 {g['subs']}", font=fs, fill=(170, 170, 170, 255))
    pill = rrect((176, 64), 32, (255, 255, 255, 255))
    ImageDraw.Draw(pill).text((88, 32), "Subscribe", font=ImageFont.truetype(INTER_B, 26), fill=(15, 15, 15, 255), anchor="mm")
    # the subscribe pill only fits if the text block leaves room; otherwise it sits under the name row
    tw = max(nw + 54, d.textlength(f"{g['handle']} \u00b7 {g['subs']}", font=fs))
    if x + tw + 24 + 176 + 28 <= w:
        card.alpha_composite(pill, (w - 28 - 176, (h - 64) // 2))
    return card


def sprite_lower_third(g, phase2):
    ft, f2 = ImageFont.truetype(BEBAS, 92), ImageFont.truetype(INTER_B, 30)
    tmp = ImageDraw.Draw(Image.new("RGBA", (1, 1)))
    tw = rich_len(g["title"], ft) if is_rich(g["title"]) else tmp.textlength(g["title"], font=ft); w2 = tmp.textlength(g["line2"], font=f2)
    w = int(max(tw, w2) + 40 + 22 + 40); h = 176
    card = card_body((w, h), 34, (16, 16, 16, 238), outline=(255, 255, 255, 38), width=2)
    ImageDraw.Draw(card).rounded_rectangle((26, 30, 34, h - 30), 4, fill=GOLD + (255,))
    d = ImageDraw.Draw(card)
    draw_rich(d, (62, 18), g["title"], ft, (255, 255, 255, 255))
    if phase2 > 0:
        lay = Image.new("RGBA", card.size, (0, 0, 0, 0))
        ImageDraw.Draw(lay).text((64, 118), g["line2"], font=f2, fill=GOLD + (255,))
        cut = int(64 + (w2 + 4) * ease(phase2))                 # a left-to-right wipe
        m = Image.new("L", card.size, 0); ImageDraw.Draw(m).rectangle((0, 0, cut, h), fill=255)
        card.paste(lay, (0, 0), Image.composite(lay, Image.new("RGBA", card.size), m).split()[3])
    return card


def sprite_title_card(g):
    fl, ft = ImageFont.truetype(INTER_B, 24), ImageFont.truetype(INTER_B, 44)
    w = g.get("w", 900); tmp = ImageDraw.Draw(Image.new("RGBA", (1, 1)))
    if is_rich(g["text"]):
        lines = wrap_rich(g["text"], ft, w - 80)
    else:
        words, lines, cur = g["text"].split(), [], ""
        for x in words:
            if tmp.textlength((cur + " " + x).strip(), font=ft) > w - 80: lines.append(cur); cur = x
            else: cur = (cur + " " + x).strip()
        lines.append(cur)
    h = 40 + 30 + 18 + 58 * len(lines) + 30
    card = card_body((w, h), 34, (16, 16, 16, 238), outline=(255, 255, 255, 38), width=2)
    d = ImageDraw.Draw(card)
    d.ellipse((40, 49, 52, 61), fill=GOLD + (255,))
    d.text((64, 42), g["label"], font=fl, fill=(170, 170, 170, 255))
    for i, ln in enumerate(lines):
        draw_rich(d, (40, 40 + 30 + 18 + 58 * i), ln, ft, (255, 255, 255, 255))
    return card


def sprite_label(g):
    f = ImageFont.truetype(BEBAS, 64)
    tw = rich_len(g["text"], f) if is_rich(g["text"]) else ImageDraw.Draw(Image.new("RGBA", (1, 1))).textlength(g["text"], font=f)
    w, h = int(tw + 40 + 26 + 34), 92
    pill = card_body((w, h), 46, (10, 10, 10, 225), outline=(255, 255, 255, 40), width=2)
    d = ImageDraw.Draw(pill)
    d.ellipse((30, h / 2 - 8, 46, h / 2 + 8), fill=GOLD + (255,))
    draw_rich(d, (66, h / 2 + 3), g["text"], f, (255, 255, 255, 255), anchor="lm")
    return pill


ENTRANCE = "pop"                 # plan["entrance"]: "rise" = batch 2's refined entrance (Affan 2026-10-12: "more refined, more premium")


def rise_frame(sprite, cx, cy, t, dur, t_in=0.42, t_out=0.26):
    """The refined entrance: the card rises 38 px out of a 10 px blur while it fades in (easeOutCubic), holds still, and leaves
    with a short fade, a 10 px lift and a light blur. No overshoot, no scale: premium cards settle, they don't bounce."""
    if t < t_in:
        p = ease(t / t_in); dy, al, bl = 38 * (1 - p), min(1.0, ease(t / (t_in * 0.7))), 10 * (1 - p)
    elif t > dur - t_out:
        p = ease((t - (dur - t_out)) / t_out); dy, al, bl = -10 * p, 1 - p, 5 * p
    else:
        dy, al, bl = 0.0, 1.0, 0.0
    fr = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    if al <= 0.01: return fr
    sh, pad = soft_shadow(sprite, blur=22, alpha=120, dy=10)
    if bl > 0.4: sh = sh.filter(ImageFilter.GaussianBlur(bl))
    if al < 1: sh.putalpha(sh.split()[3].point(lambda v: int(v * al)))
    fr.alpha_composite(sh, (int(cx - sh.width / 2), int(cy - sh.height / 2 + dy)))
    return fr


def wipe_frame(sprite, cx, cy, t, dur, t_in=0.36, t_out=0.24, edge=40):
    """research #14 (verdict cards): a left -> right mask reveal (easeInOutCubic, a 40 px soft front) while the card slides
    the last 12 px into place; leaves with a plain 0.24 s fade."""
    import numpy as np
    fr = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    if t < t_in: p = ease_io3(t / t_in); dx, al = -12 * (1 - p), 1.0
    elif t > dur - t_out: p, dx, al = 1.0, 0.0, 1 - ease((t - (dur - t_out)) / t_out)
    else: p, dx, al = 1.0, 0.0, 1.0
    if al <= 0.01 or p <= 0: return fr
    sh, pad = soft_shadow(sprite, blur=22, alpha=120, dy=10)
    if p < 1:
        front = pad - edge + (sprite.width + 2 * edge) * p
        ramp = np.clip((front - np.arange(sh.width, dtype=np.float32)) / edge, 0, 1)
        m = Image.fromarray((np.tile(ramp, (sh.height, 1)) * 255).astype(np.uint8), "L")
        sh.putalpha(ImageChops.multiply(sh.split()[3], m))
    if al < 1: sh.putalpha(sh.split()[3].point(lambda v: int(v * al)))
    fr.alpha_composite(sh, (int(cx - sh.width / 2 + dx), int(cy - sh.height / 2)))
    return fr


def lift_frame(sprite, cx, cy, t, dur, from_xy=None, t_in=0.4, t_out=0.22):
    """research #14 (things that come FROM the screen): the card lifts out of from_xy (frame px), scale 0.35 -> 1 while it
    travels to its rest spot (easeOutBack k 1.2), fading in over the first 0.15 s; out: scale 1 -> 0.9 + fade."""
    fx, fy = from_xy if from_xy else (cx, cy)
    if t < t_in:
        p = ease_back(t / t_in, 1.2); sc, al = 0.35 + 0.65 * p, clamp01(t / 0.15); x, y = fx + (cx - fx) * p, fy + (cy - fy) * p
    elif t > dur - t_out:
        q = ease((t - (dur - t_out)) / t_out); sc, al, x, y = 1 - 0.1 * q, 1 - q, cx, cy
    else:
        sc, al, x, y = 1.0, 1.0, cx, cy
    fr = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    if al <= 0.01: return fr
    sh, pad = soft_shadow(sprite, blur=22, alpha=120, dy=10)
    s = sh.resize((max(1, int(sh.width * sc)), max(1, int(sh.height * sc))), Image.LANCZOS)
    if al < 1: s.putalpha(s.split()[3].point(lambda v: int(v * al)))
    fr.alpha_composite(s, (int(x - s.width / 2), int(y - s.height / 2)))
    return fr


def _hblur(im, n):
    """a horizontal box motion blur of n px (premultiplied, so the edges do not darken): (image, x shift to apply when placing)"""
    import numpy as np
    n = int(round(n))
    if n < 2: return im, 0
    a = np.asarray(im.convert("RGBA")).astype(np.float32); al = a[..., 3:4] / 255.0
    pm = np.concatenate([a[..., :3] * al, a[..., 3:4]], axis=2)
    pm = np.pad(pm, ((0, 0), (n, n), (0, 0)))
    c = np.cumsum(np.pad(pm, ((0, 0), (1, 0), (0, 0))), axis=1)
    o = (c[:, n:] - c[:, :-n]) / n
    A_ = o[..., 3:4]; rgb = np.where(A_ > 0.5, o[..., :3] / np.maximum(A_ / 255.0, 1e-6), 0)
    out = np.concatenate([np.clip(rgb, 0, 255), np.clip(A_, 0, 255)], axis=2).astype(np.uint8)
    return Image.fromarray(out, "RGBA"), -(n + 1) // 2 - n // 2 + n // 2


def push_frame(sprite, cx, cy, t, dur, t_in=0.34, t_out=0.26, dist=150):
    """2026-10-27 (Reaction J, FX-38's hard push as a card language): the card is pushed in from 150 px left (easeOutQuint) with a
    horizontal motion blur that is half its per-frame travel (the craft rule: a slide renders with motion blur), fading in over the
    first 35 %; it leaves pushed on 60 px to the right (easeInCubic, blurred) while it fades."""
    if t < t_in:
        u = t / t_in; dx = -dist * (1 - u) ** 5; al = min(1.0, u / 0.35); v = dist * 5 * (1 - u) ** 4 / t_in / FPS_MG
    elif t > dur - t_out:
        u = (t - (dur - t_out)) / t_out; dx = 60 * u ** 3; al = 1 - ease(u); v = 60 * 3 * u ** 2 / t_out / FPS_MG
    else:
        dx, al, v = 0.0, 1.0, 0.0
    fr = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    if al <= 0.01: return fr
    sh, pad = soft_shadow(sprite, blur=22, alpha=120, dy=10)
    sh, sx = _hblur(sh, 0.5 * v)
    if al < 1: sh.putalpha(sh.split()[3].point(lambda q: int(q * al)))
    fr.alpha_composite(sh, (int(cx - sh.width / 2 + dx), int(cy - sh.height / 2)))
    return fr


def focus_frame(sprite, cx, cy, t, dur, t_in=0.46, t_out=0.28):
    """2026-10-27 (Reaction K, a rack focus): the card resolves out of a 14 px defocus while it settles from 106 % to 100 % (easeOutCubic),
    fading in over the first half; it leaves by going soft (8 px) and 3 % larger while it fades. No travel."""
    if t < t_in:
        u = t / t_in; p = ease(u); bl, sc, al = 14 * (1 - p), 1.06 - 0.06 * p, min(1.0, u / 0.5)
    elif t > dur - t_out:
        u = (t - (dur - t_out)) / t_out; bl, sc, al = 8 * u, 1 + 0.03 * u, 1 - ease(u)
    else:
        bl, sc, al = 0.0, 1.0, 1.0
    fr = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    if al <= 0.01: return fr
    sh, pad = soft_shadow(sprite, blur=22, alpha=120, dy=10)
    if abs(sc - 1) > 1e-3: sh = sh.resize((max(1, int(sh.width * sc)), max(1, int(sh.height * sc))), Image.LANCZOS)
    if bl > 0.4: sh = sh.filter(ImageFilter.GaussianBlur(bl))
    if al < 1: sh.putalpha(sh.split()[3].point(lambda q: int(q * al)))
    fr.alpha_composite(sh, (int(cx - sh.width / 2), int(cy - sh.height / 2)))
    return fr


def drop_frame(sprite, cx, cy, t, dur, t_in=0.42, t_out=0.24):
    """2026-10-27 (Reaction L): the card drops 46 px from above and settles with a small overshoot (easeOutBack k 1.25), fading in
    over the first 30 %; it leaves falling a further 22 px while it fades. The opposite direction of `rise`, and no blur."""
    if t < t_in:
        u = t / t_in; dy, al = -46 * (1 - ease_back(u, 1.25)), min(1.0, u / 0.3)
    elif t > dur - t_out:
        u = (t - (dur - t_out)) / t_out; dy, al = 22 * ease(u) ** 2, 1 - ease(u)
    else:
        dy, al = 0.0, 1.0
    fr = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    if al <= 0.01: return fr
    sh, pad = soft_shadow(sprite, blur=22, alpha=120, dy=10)
    if al < 1: sh.putalpha(sh.split()[3].point(lambda q: int(q * al)))
    fr.alpha_composite(sh, (int(cx - sh.width / 2), int(cy - sh.height / 2 + dy)))
    return fr


def pop_frame(sprite, cx, cy, t, dur, t_in=0.42, t_out=0.24, ent=None, from_xy=None):
    """A sprite popping in (easeOutBack scale + fade), holding, and popping out (scale down + fade). ent (a graphic's own
    "entrance") overrides plan["entrance"]: "pop" | "rise" | "wipe" | "lift" (from from_xy)."""
    e = ent or ENTRANCE
    if e == "rise": return rise_frame(sprite, cx, cy, t, dur)
    if e == "wipe": return wipe_frame(sprite, cx, cy, t, dur)
    if e == "lift": return lift_frame(sprite, cx, cy, t, dur, from_xy)
    if e == "push": return push_frame(sprite, cx, cy, t, dur)
    if e == "focus": return focus_frame(sprite, cx, cy, t, dur)
    if e == "drop": return drop_frame(sprite, cx, cy, t, dur)
    if t < t_in:
        sc, al = 0.55 + 0.45 * ease_back(t / t_in), ease(t / (t_in * 0.6))
    elif t > dur - t_out:
        p = (t - (dur - t_out)) / t_out; sc, al = 1 - 0.1 * ease(p), 1 - ease(p)
    else:
        sc, al = 1.0, 1.0
    fr = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    if al <= 0.01: return fr
    sh, pad = soft_shadow(sprite)
    s = sh.resize((max(1, int(sh.width * sc)), max(1, int(sh.height * sc))), Image.LANCZOS)
    if al < 1: s.putalpha(s.split()[3].point(lambda v: int(v * al)))
    fr.alpha_composite(s, (int(cx - s.width / 2), int(cy - s.height / 2 + pad * sc * 0)))
    return fr


def bezier(p0, p1, p2, n=60):
    return [((1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u * u * p2[0], (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u * u * p2[1])
            for u in (i / (n - 1) for i in range(n))]


def arrow_frame(box, t, dur, ss=2):
    """Rounded highlight box drawing on around the target + a curved arrow drawing in toward it, a gentle bob, fade out."""
    x0, y0, x1, y1 = box; pad = 14
    rx0, ry0, rx1, ry1 = x0 - pad, y0 - pad, x1 + pad, y1 + pad
    mid = ((rx0 + rx1) / 2, (ry0 + ry1) / 2)
    room_above = ry0 - G.BOX[1]; room_below = G.BOX[3] - ry1
    side = -1 if room_above >= room_below else 1            # -1: arrow comes from above
    tip = (mid[0] + 40, (ry0 - 12) if side < 0 else (ry1 + 12))
    start = (tip[0] + 190, tip[1] + side * 210)
    ctrl = (tip[0] + 200, tip[1] + side * 40)
    bob = 6 * math.sin(2 * math.pi * max(t - 0.6, 0) / 1.2)
    al = 1.0 if t < dur - 0.25 else max(0.0, 1 - (t - (dur - 0.25)) / 0.25)
    im = Image.new("RGBA", (W * ss, H * ss), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    S = lambda p: (p[0] * ss, p[1] * ss)
    # highlight box: perimeter reveal 0 -> 0.32 s
    pb = ease(t / 0.32)
    if pb > 0:
        per = [(rx0, ry0), (rx1, ry0), (rx1, ry1), (rx0, ry1), (rx0, ry0)]
        L = 2 * ((rx1 - rx0) + (ry1 - ry0)); goal = L * pb; acc = 0; pts = [per[0]]
        for a, b in zip(per, per[1:]):
            seg = math.dist(a, b)
            if acc + seg >= goal:
                u = (goal - acc) / seg; pts.append((a[0] + (b[0] - a[0]) * u, a[1] + (b[1] - a[1]) * u)); break
            pts.append(b); acc += seg
        d.line([S(p) for p in pts], fill=(255, 255, 255, 255), width=6 * ss, joint="curve")
    # arrow: draws 0.12 -> 0.5 s, the head lands at the end
    pa = ease((t - 0.12) / 0.38)
    if pa > 0:
        path = [(x, y + side * -bob * 0) for x, y in bezier(start, ctrl, tip)]
        path = [(x - side * 0, y - side * bob) for x, y in path]
        n = max(2, int(len(path) * pa)); seg = path[:n]
        d.line([S(p) for p in seg], fill=(255, 255, 255, 255), width=9 * ss, joint="curve")
        e = seg[-1]; e2 = seg[-2]; ang = math.atan2(e[1] - e2[1], e[0] - e2[0]); L2 = 34
        if pa > 0.8:
            for da in (2.6, -2.6):
                d.line([S(e), S((e[0] + L2 * math.cos(ang + da), e[1] + L2 * math.sin(ang + da)))], fill=(255, 255, 255, 255), width=9 * ss)
    im = im.resize((W, H), Image.LANCZOS)
    sh = Image.new("RGBA", (W, H), (0, 0, 0, 0)); a = im.split()[3].point(lambda v: v * 150 // 255)
    blk = Image.new("RGBA", (W, H), (0, 0, 0, 255)); blk.putalpha(a); sh.paste(blk, (0, 4), blk)
    out = Image.alpha_composite(sh.filter(ImageFilter.GaussianBlur(5)), im)
    if al < 1: out.putalpha(out.split()[3].point(lambda v: int(v * al)))
    return out


def underline_frame(box, t, dur, ss=2):
    x0, y0, x1, y1 = box; y = y1 + 16
    p = ease(t / 0.5); al = 1.0 if t < dur - 0.25 else max(0.0, 1 - (t - (dur - 0.25)) / 0.25)
    im = Image.new("RGBA", (W * ss, H * ss), (0, 0, 0, 0))
    if p > 0:
        ImageDraw.Draw(im).line([(x0 * ss, y * ss), ((x0 + (x1 - x0) * p) * ss, y * ss)], fill=GOLD + (255,), width=9 * ss)
    im = im.resize((W, H), Image.LANCZOS)
    if al < 1: im.putalpha(im.split()[3].point(lambda v: int(v * al)))
    return im


def distance_frame(plan, g, t, dur, ss=2):
    """A measured gap: a vertical bracket from (x, y0) to (x, y1) in source pixels, growing out from its middle, with a label."""
    v = view_at(plan, g["t0"] + 0.3)
    x, ya = src_to_frame(v, g["x"], g["y0"]); _, yb = src_to_frame(v, g["x"], g["y1"])
    p = ease(t / 0.4); al = 1.0 if t < dur - 0.25 else max(0.0, 1 - (t - (dur - 0.25)) / 0.25)
    mid = (ya + yb) / 2; a, b = mid - (mid - ya) * p, mid + (yb - mid) * p
    im = Image.new("RGBA", (W * ss, H * ss), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    S = lambda q: (q[0] * ss, q[1] * ss); wd = 7 * ss
    d.line([S((x, a)), S((x, b))], fill=(255, 255, 255, 255), width=wd)
    for yy, sg in ((a, 1), (b, -1)):
        d.line([S((x - 22, yy)), S((x + 22, yy))], fill=(255, 255, 255, 255), width=wd)
        if p > 0.9:
            d.line([S((x, yy)), S((x - 16, yy + sg * 20))], fill=(255, 255, 255, 255), width=wd)
            d.line([S((x, yy)), S((x + 16, yy + sg * 20))], fill=(255, 255, 255, 255), width=wd)
    im = im.resize((W, H), Image.LANCZOS)
    sh = Image.new("RGBA", (W, H), (0, 0, 0, 0)); al_ = im.split()[3].point(lambda q: q * 150 // 255)
    blk = Image.new("RGBA", (W, H), (0, 0, 0, 255)); blk.putalpha(al_); sh.paste(blk, (0, 4), blk)
    out = Image.alpha_composite(sh.filter(ImageFilter.GaussianBlur(5)), im)
    if p > 0.6:
        lab = sprite_label({"text": g["label"]})
        lab = lab.resize((int(lab.width * 0.8), int(lab.height * 0.8)), Image.LANCZOS)
        out.alpha_composite(pop_frame(lab, x - 40 - lab.width / 2, mid, t - 0.25, dur - 0.25))
    if al < 1: out.putalpha(out.split()[3].point(lambda q: int(q * al)))
    return out


def sprite_steps(g, shown):
    """THE HOOK card: a title and numbered rows; rows appear as `shown` (0..1 per row) rises."""
    ft, fr, fn = ImageFont.truetype(BEBAS, 60), ImageFont.truetype(INTER_B, 31), ImageFont.truetype(INTER_K, 28)
    w = g.get("w", 940); rows = g["steps"]; h = 36 + 62 + 22 + 74 * len(rows) + 20
    if "w" in g:                                           # a narrower verdict card: long rows / titles shrink to fit
        ft = fit_font(BEBAS, 60, [g["title"]], w - 80, 40); fr = fit_font(INTER_B, 31, [x for _, x in rows], w - 112 - 36, 22)
    card = card_body((w, h), 34, (16, 16, 16, 252), outline=(255, 255, 255, 38), width=2)
    d = ImageDraw.Draw(card)
    draw_rich(d, (40, 30), g["title"], ft, GOLD + (255,))
    for i, (_, txt) in enumerate(rows):
        a = shown[i]
        if a <= 0: continue
        lay = Image.new("RGBA", card.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
        y = 36 + 62 + 22 + 74 * i + int((1 - ease(a)) * 18)
        dl.ellipse((40, y, 92, y + 52), fill=(255, 255, 255, 255))
        dl.text((66, y + 26), str(i + 1), font=fn, fill=(15, 15, 15, 255), anchor="mm")
        dl.text((112, y + 26), txt, font=fr, fill=(255, 255, 255, 255), anchor="lm")
        if a < 1: lay.putalpha(lay.split()[3].point(lambda q: int(q * ease(a))))
        card.alpha_composite(lay)
    return card


RED, GREEN = (235, 87, 87), (88, 196, 120)


def sprite_stat(g, p):
    """A big number counting up (p 0..1 of the count) over a quiet gold label: '60%' / 'OF VIEWS LOST WITHOUT CAPTIONS'."""
    fn, fl, fs = ImageFont.truetype(BEBAS, 178), ImageFont.truetype(INTER_B, 34), ImageFont.truetype(INTER_R, 26)
    v = g["value"]; cur = v * ease(p)
    num = f"{g.get('prefix', '')}{cur:,.{g.get('decimals', 0)}f}{g.get('suffix', '')}"      # thousands grouped: "$23,000", never "$23000"
    full = f"{g.get('prefix', '')}{v:,.{g.get('decimals', 0)}f}{g.get('suffix', '')}"
    tmp = ImageDraw.Draw(Image.new("RGBA", (1, 1)))
    w = int(max(tmp.textlength(full, font=fn), rich_len(g["label"], fl) if is_rich(g["label"]) else tmp.textlength(g["label"], font=fl),
                tmp.textlength(g.get("sub", ""), font=fs)) + 112)
    w = max(w, 560); h = 70 + 150 + 26 + 44 + (40 if g.get("sub") else 0) + 34
    card = card_body((w, h), 38, (14, 14, 14, 244), outline=(255, 255, 255, 34), width=2)
    d = ImageDraw.Draw(card)
    d.rounded_rectangle((56, 44, 56 + 64, 50), 3, fill=GOLD + (255,))                 # a short gold rule above the number
    d.text((52, 58), num, font=fn, fill=(255, 255, 255, 255))
    draw_rich(d, (56, 70 + 150 + 26), g["label"], fl, GOLD + (255,))
    if g.get("sub"): d.text((56, 70 + 150 + 26 + 50), g["sub"], font=fs, fill=(165, 165, 165, 255))
    return card


def _partial(pts, q):
    """the first q (0..1) of a polyline, by length"""
    L = [math.dist(a, b) for a, b in zip(pts, pts[1:])]; goal = sum(L) * q; out = [pts[0]]; acc = 0.0
    for (a, b), l in zip(zip(pts, pts[1:]), L):
        if acc + l >= goal:
            u = (goal - acc) / l if l else 1; out.append((a[0] + (b[0] - a[0]) * u, a[1] + (b[1] - a[1]) * u)); return out
        out.append(b); acc += l
    return out


def sprite_checklist(g, tt):
    """A title and rows that land one by one; each row's mark DRAWS (an X in red, a tick in green), and a missing item is
    struck through, quietly."""
    ft = ImageFont.truetype(BEBAS, 58)
    rows = g["rows"]; w = g.get("w", 900); h = 34 + 58 + 26 + 86 * len(rows) + 22; ss = 3
    rsz = 34
    if "w" in g:                                           # a narrower verdict card: long rows / titles shrink to fit
        ft = fit_font(BEBAS, 58, [g["title"]], w - 88, 40); rsz = fit_font(INTER_B, 34, [r_[1] for r_ in rows], w - 120 - 36, 22).size
    card = card_body((w, h), 36, (14, 14, 14, 244), outline=(255, 255, 255, 34), width=2)
    draw_rich(ImageDraw.Draw(card), (44, 30), g["title"], ft, GOLD + (255,))
    fr3 = ImageFont.truetype(INTER_B, rsz * ss)
    for i, (st, txt, mark) in enumerate(rows):
        a = min(1.0, max(0.0, (tt - st) / 0.32))
        if a <= 0: continue
        lay = Image.new("RGBA", (w * ss, h * ss), (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
        y = 34 + 58 + 26 + 86 * i + (1 - ease(a)) * 16; cy = y + 30
        S = lambda q_: (q_[0] * ss, q_[1] * ss)
        dl.text(S((120, cy)), txt, font=fr3, fill=(255, 255, 255, 255), anchor="lm")
        dl.rounded_rectangle((44 * ss, (cy - 26) * ss, 96 * ss, (cy + 26) * ss), 14 * ss, outline=(255, 255, 255, 70), width=2 * ss)
        m = min(1.0, max(0.0, (tt - st - 0.18) / 0.30))          # the mark draws after the row lands
        col = (RED if mark == "x" else GREEN) + (255,)
        if m > 0 and mark == "x":
            for (p0, p1), q in ((((57, cy - 13), (83, cy + 13)), min(1, m * 2)), (((83, cy - 13), (57, cy + 13)), max(0, m * 2 - 1))):
                if q > 0: dl.line([S(x) for x in _partial([p0, p1], q)], fill=col, width=6 * ss)
        elif m > 0:
            dl.line([S(x) for x in _partial([(56, cy + 1), (66, cy + 11), (85, cy - 12)], m)], fill=col, width=6 * ss, joint="curve")
        if mark == "x":
            q = min(1.0, max(0.0, (tt - st - 0.5) / 0.25))
            if q > 0:
                tw = dl.textlength(txt, font=fr3) / ss
                dl.line([S((118, cy + 2)), S((118 + (tw + 6) * ease(q), cy + 2))], fill=(255, 255, 255, 150), width=3 * ss)
        lay = lay.resize((w, h), Image.LANCZOS)
        if a < 1: lay.putalpha(lay.split()[3].point(lambda q_: int(q_ * ease(a))))
        card.alpha_composite(lay)
    return card


def sprite_compare(g, tt):
    """Two quiet panels side by side (left lands, then right): a small gold label over heavy white lines, a hairline between."""
    fl, fv = ImageFont.truetype(INTER_B, 24), ImageFont.truetype(BEBAS, 62)
    nl = max(len(sd[2].split("|")) for sd in g["sides"])
    w, h = g.get("w", 960), 110 + 62 * nl + 30
    if "w" in g:                                           # a narrower verdict card: long lines shrink to fit their half
        fv = fit_font(BEBAS, 62, [ln for sd in g["sides"] for ln in sd[2].split("|")], w // 2 - 44 - 20, 36)
    card = card_body((w, h), 36, (14, 14, 14, 244), outline=(255, 255, 255, 34), width=2)
    ImageDraw.Draw(card).line([(w // 2, 34), (w // 2, h - 34)], fill=(255, 255, 255, 46), width=2)
    for k, side in enumerate(g["sides"]):                       # [[t, "LABEL", "LINE|LINE"], [t, "LABEL", "LINE|LINE"]]
        a = min(1.0, max(0.0, (tt - side[0]) / 0.34))
        if a <= 0: continue
        lay = Image.new("RGBA", card.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
        x0 = 44 + k * (w // 2); dy = int((1 - ease(a)) * 14)
        dl.text((x0, 48 + dy), side[1], font=fl, fill=GOLD + (255,))
        for j, ln in enumerate(side[2].split("|")): draw_rich(dl, (x0, 88 + 62 * j + dy), ln, fv, (255, 255, 255, 255))
        if a < 1: lay.putalpha(lay.split()[3].point(lambda q_: int(q_ * ease(a))))
        card.alpha_composite(lay)
    return card


def mock_title_frame(plan, g, t, dur):
    """What the Short is missing, shown ON the Short: its title set as a hook over the top of the player (plan box), the way our
    samples carry one: a dark band, heavy white type rising in line by line, a small tag above."""
    x0, y0, x1, y1 = target_box(plan, g)
    al = 1.0 if t < dur - 0.26 else max(0.0, 1 - (t - (dur - 0.26)) / 0.26)
    fr = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    band = Image.new("RGBA", (int(x1 - x0), int(y1 - y0)), (0, 0, 0, 0))
    ImageDraw.Draw(band).rounded_rectangle((0, 0, band.width - 1, band.height - 1), 22, fill=(0, 0, 0, int(150 * ease(min(1, t / 0.3)))))
    fr.alpha_composite(band, (int(x0), int(y0)))
    fsz = g.get("size", 54); f = ImageFont.truetype(INTER_K, fsz)
    lines = g["text"].split("|"); lh = int(fsz * 1.12)
    for j, ln in enumerate(lines):
        a = min(1.0, max(0.0, (t - 0.12 - 0.1 * j) / 0.36))
        if a <= 0: continue
        lay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        cy = (y0 + y1) / 2 - (len(lines) - 1) * lh / 2 + j * lh + (1 - ease(a)) * 22
        ImageDraw.Draw(lay).text(((x0 + x1) / 2, cy), ln, font=f, fill=(255, 255, 255, 255), anchor="mm", stroke_width=3, stroke_fill=(0, 0, 0, 255))
        if a < 1: lay.putalpha(lay.split()[3].point(lambda q_: int(q_ * ease(a))))
        fr.alpha_composite(lay)
    if g.get("tag") and t > 0.3:
        tag = sprite_label({"text": g["tag"]}); tag = tag.resize((int(tag.width * 0.62), int(tag.height * 0.62)), Image.LANCZOS)
        fr.alpha_composite(rise_frame(tag, (x0 + x1) / 2, y0 - tag.height / 2 - 14, t - 0.3, dur - 0.3))
    if al < 1: fr.putalpha(fr.split()[3].point(lambda q_: int(q_ * al)))
    return fr


def move_frame(plan, g, t, dur, ss=2):
    """Where it should go: a dashed target box (plan box) + an arrow rising to it from the current spot (from_box) + a label."""
    v = view_at(plan, g["t0"] + 0.3)
    def fb(name):
        b = plan["boxes"][name]; a = src_to_frame(v, b[0], b[1]); c = src_to_frame(v, b[2], b[3]); return (a[0], a[1], c[0], c[1])
    tx0, ty0, tx1, ty1 = fb(g["box"]); fx0, fy0, fx1, fy1 = fb(g["from_box"])
    al = 1.0 if t < dur - 0.25 else max(0.0, 1 - (t - (dur - 0.25)) / 0.25)
    im = Image.new("RGBA", (W * ss, H * ss), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    S = lambda q: (q[0] * ss, q[1] * ss)
    pb = ease(t / 0.35)
    if pb > 0:                                       # dashed target, revealed around its perimeter
        per = [(tx0, ty0), (tx1, ty0), (tx1, ty1), (tx0, ty1), (tx0, ty0)]
        L = 2 * ((tx1 - tx0) + (ty1 - ty0)); goal = L * pb; acc = 0.0
        for a, b in zip(per, per[1:]):
            seg = math.dist(a, b); u = 0.0
            while u < seg and acc + u < goal:
                u2 = min(u + 20, seg, goal - acc)
                pa = (a[0] + (b[0] - a[0]) * u / seg, a[1] + (b[1] - a[1]) * u / seg)
                pz = (a[0] + (b[0] - a[0]) * u2 / seg, a[1] + (b[1] - a[1]) * u2 / seg)
                d.line([S(pa), S(pz)], fill=GOLD + (255,), width=6 * ss)
                u += 34
            acc += seg
    pa_ = ease((t - 0.25) / 0.45)
    if pa_ > 0:                                      # the arrow rises from the current captions to the target
        start = ((fx0 + fx1) / 2 + 60, fy0 - 10); tip = ((tx0 + tx1) / 2 + 60, ty1 + 16)
        ctrl = (start[0] + 120, (start[1] + tip[1]) / 2)
        path = bezier(start, ctrl, tip); n = max(2, int(len(path) * pa_)); seg = path[:n]
        d.line([S(q) for q in seg], fill=(255, 255, 255, 255), width=9 * ss, joint="curve")
        if pa_ > 0.8:
            e, e2 = seg[-1], seg[-2]; ang = math.atan2(e[1] - e2[1], e[0] - e2[0])
            for da in (2.6, -2.6):
                d.line([S(e), S((e[0] + 34 * math.cos(ang + da), e[1] + 34 * math.sin(ang + da)))], fill=(255, 255, 255, 255), width=9 * ss)
    im = im.resize((W, H), Image.LANCZOS)
    sh = Image.new("RGBA", (W, H), (0, 0, 0, 0)); a_ = im.split()[3].point(lambda q: q * 150 // 255)
    blk = Image.new("RGBA", (W, H), (0, 0, 0, 255)); blk.putalpha(a_); sh.paste(blk, (0, 4), blk)
    out = Image.alpha_composite(sh.filter(ImageFilter.GaussianBlur(5)), im)
    if t > 0.45:
        lab = sprite_label({"text": g["label"]}); lab = lab.resize((int(lab.width * 0.8), int(lab.height * 0.8)), Image.LANCZOS)
        out.alpha_composite(pop_frame(lab, (tx0 + tx1) / 2, ty0 - 20 - lab.height / 2, t - 0.45, dur - 0.45))
    if al < 1: out.putalpha(out.split()[3].point(lambda q: int(q * al)))
    return out


def target_box(plan, g):
    src = plan["boxes"][g["box"]]
    v = view_at(plan, g["t0"] + 0.6)
    a = src_to_frame(v, src[0], src[1]); b = src_to_frame(v, src[2], src[3])
    return (a[0], a[1], b[0], b[1])


# ---------- 2026-10-13: footage pipes (the OBS recording through the dump's cuts, or a file) ----------
def _rgb_pipe(path, t, n, vf, w, h):
    """n RGB frames (w x h) of `path` from t s, 60 fps, through the filter chain vf (ONE ffmpeg decode); past the source's end
    the last frame holds"""
    cmd = ["ffmpeg", "-v", "error", "-ss", f"{max(t, 0.0):.4f}", "-i", path, "-an", "-sn", "-vf", ",".join([f"fps={FPS_MG}"] + vf),
           "-frames:v", str(n), "-f", "rawvideo", "-pix_fmt", "rgb24", "-"]
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    sz, k, last = w * h * 3, 0, None
    try:
        while k < n:
            b = p.stdout.read(sz)
            if len(b) < sz: break
            last = Image.frombytes("RGB", (w, h), b); k += 1
            yield last
    finally:
        if p.poll() is None: p.kill()
        p.stdout.close(); p.wait()
    while k < n:
        k += 1; yield last if last is not None else Image.new("RGB", (w, h))


def seq_pieces(plan, seq, t0, f0, n):
    """[[clip, source_t, frames]] covering the graphic frames f0 .. f0 + n (graphic starting at sequence time t0) through the
    screen track: one piece per screen clip (a range across cuts maps to several source ranges)"""
    tr = seq["v"][plan["screen_track"]]; out = []
    for i in range(f0, f0 + n):
        T = t0 + i / FPS_MG; c = G.clip_at(tr, T)
        if out and out[-1][0] is c: out[-1][2] += 1
        else: out.append([c, G.src_time(c, T) if c else None, 1])
    return out


def seq_pipe(plan, seq, t0, f0, n, vf, w, h):
    for c, st, k in seq_pieces(plan, seq, t0, f0, n):
        if c is None:
            for _ in range(k): yield Image.new("RGB", (w, h))
        else:
            yield from _rgb_pipe(c["p"], st, k, vf, w, h)


def crop_vf(b):
    x0, y0 = max(0, int(round(b[0]))), max(0, int(round(b[1]))); x1, y1 = min(G.SW, int(round(b[2]))), min(G.SH, int(round(b[3])))
    return f"crop={x1 - x0}:{y1 - y0}:{x0}:{y0}"


def cover_vf(w, h):
    return [f"scale={w}:{h}:force_original_aspect_ratio=increase:flags=bicubic", f"crop={w}:{h}"]


def obs_path(plan, seq, t_src):
    cl = seq["v"][plan["screen_track"]]["clips"]
    return next((c for c in cl if c["i"] - 1e-6 <= t_src < c["o"]), cl[0])["p"]


def media_pipe(plan, seq, m, f0, n, w, h):
    """a before / after source, scaled to cover w x h: {"file": path, "t": s at the graphic's t0} or {"src": "obs", "t": OBS s
    at t0, "box": name} (a crop of the screen recording)"""
    if m.get("file"):
        p = m["file"] if os.path.isabs(m["file"]) else os.path.join(plan["_dir"], m["file"]); vf = cover_vf(w, h)
    else:
        p = m.get("path") or obs_path(plan, seq, m["t"]); vf = [crop_vf(box_src(plan, m["box"]))] + cover_vf(w, h)
    return _rgb_pipe(p, m.get("t", 0.0) + f0 / FPS_MG, n, vf, w, h)


# ---------- 2026-10-13: shared dressing ----------
def rounded_mask(size, rect, r, corners=(True, True, True, True), ss=4):
    """L mask: 255 inside rect (float px), r-rounded at the corners flagged (tl, tr, br, bl), antialiased"""
    w, h = size; m = Image.new("L", (w * ss, h * ss), 0)
    x0, y0, x1, y1 = rect
    ImageDraw.Draw(m).rounded_rectangle((x0 * ss, y0 * ss, x1 * ss - 1, y1 * ss - 1), r * ss, fill=255, corners=tuple(corners))
    return m.resize((w, h), Image.LANCZOS)


def card_dressing(size, rect, r, corners=(True, True, True, True), shadow=30, sh_alpha=150, dy=8, hair=(255, 255, 255, 64)):
    """RGBA: a card's 30 px soft shadow cast OUTSIDE rect + a 2 px hairline on its edge (white @ 25 %)"""
    w, h = size
    hole = rounded_mask(size, rect, r, corners)
    sh = Image.new("L", size, 0); sh.paste(hole, (0, dy))
    sh = sh.filter(ImageFilter.GaussianBlur(shadow / 3)).point(lambda v: v * sh_alpha // 255)
    lay = Image.new("RGBA", size, (0, 0, 0, 255)); lay.putalpha(ImageChops.multiply(sh, ImageChops.invert(hole)))
    ss = 3; hl = Image.new("RGBA", (w * ss, h * ss), (0, 0, 0, 0))
    x0, y0, x1, y1 = rect
    ImageDraw.Draw(hl).rounded_rectangle((x0 * ss, y0 * ss, x1 * ss - 1, y1 * ss - 1), r * ss, outline=hair, width=2 * ss, corners=tuple(corners))
    lay.alpha_composite(hl.resize(size, Image.LANCZOS))
    return lay


def text_sprite(text, f, fill, shadow=150, blur=4):
    """a text run with a soft shadow, cropped to its box (+ margin)"""
    d0 = ImageDraw.Draw(Image.new("RGBA", (1, 1)))
    l, t_, r, b = d0.textbbox((0, 0), text, font=f)
    m = blur * 3; w, h = int(r - l) + 2 * m, int(b - t_) + 2 * m
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    sh = Image.new("RGBA", (w, h), (0, 0, 0, 0)); ImageDraw.Draw(sh).text((m - l, m - t_ + 2), text, font=f, fill=(0, 0, 0, shadow))
    im.alpha_composite(sh.filter(ImageFilter.GaussianBlur(blur)))
    ImageDraw.Draw(im).text((m - l, m - t_), text, font=f, fill=fill)
    return im, m


def drop_shadow(im, blur=4, alpha=130, dy=2):
    a = im.split()[3].point(lambda v: v * alpha // 255)
    sh = Image.new("RGBA", im.size, (0, 0, 0, 255)); sh.putalpha(Image.new("L", im.size, 0)); sh.paste(Image.new("RGBA", im.size, (0, 0, 0, 255)), (0, dy), a)
    out = sh.filter(ImageFilter.GaussianBlur(blur)); out.alpha_composite(im)
    return out


class Local:
    """a supersampled drawing region of the frame: draw in FRAME px through S() / R(), then out() -> (image, (x, y))"""
    def __init__(self, x0, y0, x1, y1, ss=3):
        self.x0, self.y0 = int(math.floor(x0)), int(math.floor(y0))
        self.w, self.h = max(1, int(math.ceil(x1)) - self.x0), max(1, int(math.ceil(y1)) - self.y0); self.ss = ss
        self.im = Image.new("RGBA", (self.w * ss, self.h * ss), (0, 0, 0, 0)); self.d = ImageDraw.Draw(self.im)
    def S(self, p): return ((p[0] - self.x0) * self.ss, (p[1] - self.y0) * self.ss)
    def R(self, b): return (*self.S(b[:2]), *self.S(b[2:]))
    def out(self): return self.im.resize((self.w, self.h), Image.LANCZOS), (self.x0, self.y0)


def clip_panel(fr):
    """screen marks live ON the screen: nothing of them outside the panel box (a box can run past the panel's crop)"""
    B = G.BOX
    for r in ((0, 0, W, B[1]), (0, B[3], W, H), (0, 0, B[0], H), (B[2], 0, W, H)):
        if r[2] > r[0] and r[3] > r[1]: fr.paste((0, 0, 0, 0), r)
    return fr


def put(fr, im, xy):
    """alpha-composite im onto the frame at (possibly off-frame) xy"""
    x, y = int(round(xy[0])), int(round(xy[1]))
    l, t_ = max(0, -x), max(0, -y); r, b = min(im.width, W - x), min(im.height, H - y)
    if r > l and b > t_: fr.alpha_composite(im.crop((l, t_, r, b)) if (l, t_, r, b) != (0, 0, im.width, im.height) else im, (x + l, y + t_))


def sprite_tag(text, size=44, h=56):
    """the small docked tag (spotlight): Bebas 44 on a 56 px dark pill with the gold dot"""
    f = ImageFont.truetype(BEBAS, size); tw = rich_len(text, f)
    w = int(tw + 40 + 22); pill = card_body((w, h), h // 2, (10, 10, 10, 225), outline=(255, 255, 255, 40), width=2)
    d = ImageDraw.Draw(pill); d.ellipse((18, h / 2 - 6, 30, h / 2 + 6), fill=GOLD + (255,))
    draw_rich(d, (40, h / 2 + 2), text, f, (255, 255, 255, 255), anchor="lm")
    return pill


def sprite_mono(text, size=22, h=None, dot=False, r=8, fill=(14, 14, 14, 235)):
    """a mono chip: IBM Plex Mono on a dark pill (select's chip, the timecode)"""
    f = ImageFont.truetype(PLEX_MONO, size)
    tw = ImageDraw.Draw(Image.new("RGBA", (1, 1))).textlength(text, font=f)
    h = h or int(size * 1.45); px = int(size * 0.55); ds = round(size / 3); dx = (ds + int(size * 0.4)) if dot else 0
    w = int(tw + 2 * px + dx)
    pill = card_body((w, h), r, fill, outline=(255, 255, 255, 40), width=2)
    d = ImageDraw.Draw(pill)
    if dot:
        d.ellipse((px, h / 2 - ds / 2, px + ds, h / 2 + ds / 2), fill=GOLD + (255,))
    d.text((px + dx, h / 2 + 1), text, font=f, fill=(255, 255, 255, 255), anchor="lm")
    return pill


# ---------- showcase (research #1) ----------
def showcase_geom(plan, g):
    n = int(round((g["t1"] - g["t0"]) * FPS_MG))
    mid = view_at(plan, (g["t0"] + g["t1"]) / 2)
    if mid is None: raise SystemExit(f"showcase {g['id']}: a face-only beat at its mid-time")
    for k in range(n):
        v = view_at(plan, g["t0"] + k / FPS_MG)
        if v is None or any(abs(v[q] - mid[q]) > 1e-9 for q in ("cx", "cy", "z")):
            raise SystemExit(f"showcase {g['id']}: the screen view is not static across [{g['t0']}, {g['t1']}] "
                             f"(at {g['t0'] + k / FPS_MG:.3f}: {v} vs {mid})")
    b = box_src(plan, g["box"]); a = src_to_frame(mid, b[0], b[1]); c = src_to_frame(mid, b[2], b[3])
    return mid, (a[0], a[1], c[0], c[1])


def showcase_layers(plan, g):
    """(mask L, top RGBA), both panel-sized: 255 outside the card + its corner wedges; the shadow, hairline and gutter tag"""
    P = G.BOX; pw, ph = P[2] - P[0], P[3] - P[1]
    _, rect = showcase_geom(plan, g)
    lr = (rect[0] - P[0], rect[1] - P[1], rect[2] - P[0], rect[3] - P[1])
    ins = (lr[0] >= 6, lr[1] >= 6, lr[2] <= pw - 6, lr[3] <= ph - 6)                       # l t r b
    corners = (ins[0] and ins[1], ins[1] and ins[2], ins[2] and ins[3], ins[3] and ins[0])   # tl tr br bl
    hole = rounded_mask((pw, ph), lr, 28, corners)
    top = card_dressing((pw, ph), lr, 28, corners)
    if g.get("tag") and lr[0] >= 200:                # the tab in the left gutter (x 40, y 236), only where the gutter is wide
        x, y = 40 - P[0], 236 - P[1]
        t1, m1 = text_sprite(g["tag"], ImageFont.truetype(INTER_B, 24), (255, 255, 255, 255))
        dot = Image.new("RGBA", (30, 30), (0, 0, 0, 0)); ImageDraw.Draw(dot).ellipse((10, 10, 20, 20), fill=GOLD + (255,))
        top.alpha_composite(dot, (x + 5 - 15, y + 9 - 15))           # a 10 px gold dot on the tag's cap-height middle
        top.alpha_composite(t1, (x + 18 - m1, y - m1))
        if g.get("tag2"):
            t2, m2 = text_sprite(g["tag2"], ImageFont.truetype(INTER_R, 20), (175, 175, 175, 255))
            top.alpha_composite(t2, (x + 18 - m2, y + 36 - m2))
    return ImageChops.invert(hole), top


def showcase_cmd(plan, seq, g, f0, n, out, tmp):
    """ONE ffmpeg graph: each screen piece cropped to the box -> cover the panel -> gblur -> desaturate -> darken, the
    static mask as alpha, the dressing on top, padded into the 1080x1920 frame (transparent outside the panel)"""
    P = G.BOX; pw, ph = P[2] - P[0], P[3] - P[1]
    mask, top = showcase_layers(plan, g)
    mp, tp = os.path.join(tmp, "mask.png"), os.path.join(tmp, "top.png"); mask.save(mp); top.save(tp)
    pieces = seq_pieces(plan, seq, g["t0"], f0, n)
    b = box_src(plan, g["box"]); sigma = g.get("blur", 36); keep = 1 - g.get("dim", 0.35)
    args, fl = ["ffmpeg", "-v", "error", "-y"], []
    for k, (c, st, cnt) in enumerate(pieces):
        if c is None: raise SystemExit(f"showcase {g['id']}: no screen clip at frame {f0 + k}")
        args += ["-ss", f"{st:.4f}", "-t", f"{cnt / FPS_MG + 0.5:.4f}", "-i", c["p"]]
        fl.append(f"[{k}:v]fps={FPS_MG},{crop_vf(b)},scale={pw}:{ph}:force_original_aspect_ratio=increase,crop={pw}:{ph},"
                  f"trim=end_frame={cnt},setpts=PTS-STARTPTS[p{k}]")
    K = len(pieces)
    args += ["-i", mp, "-i", tp]
    src = "".join(f"[p{k}]" for k in range(K)) + (f"concat=n={K}:v=1:a=0," if K > 1 else "")
    fl.append(f"{src}gblur=sigma={sigma},eq=saturation=0.9,format=rgba,colorchannelmixer=rr={keep:.3f}:gg={keep:.3f}:bb={keep:.3f}[bg]")
    fl.append(f"[bg][{K}:v]alphamerge[am]")
    fl.append(f"[am][{K + 1}:v]overlay=0:0:format=auto,format=rgba,pad={W}:{H}:{P[0]}:{P[1]}:color=black@0,"
              f"tpad=stop_mode=clone:stop={n}[out]")
    args += ["-filter_complex", ";".join(fl), "-map", "[out]", "-frames:v", str(n), "-r", str(FPS_MG)]
    if out == "-": args += ["-f", "rawvideo", "-pix_fmt", "rgba", "-"]
    else: args += ["-c:v", "prores_ks", "-profile:v", "4444", "-pix_fmt", "yuva444p10le", "-vendor", "apl0", out]
    return args


def showcase_frames(plan, seq, g, f0, n):
    tmp = tempfile.mkdtemp(prefix="showcase-")
    try:
        p = subprocess.Popen(showcase_cmd(plan, seq, g, f0, n, "-", tmp), stdout=subprocess.PIPE)
        sz, k = W * H * 4, 0
        try:
            while k < n:
                b = p.stdout.read(sz)
                if len(b) < sz: break
                k += 1; yield Image.frombytes("RGBA", (W, H), b)
        finally:
            if p.poll() is None: p.kill()
            p.stdout.close(); p.wait()
        if k < n: raise SystemExit(f"showcase {g['id']}: ffmpeg gave {k} of {n} frames")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


# ---------- before / after: ba_wipe, ba_pair (research #2) ----------
def _backdrop(im, pw, ph, dim=0.35):
    """the blurred, darkened cover of a card frame over the whole panel (blurred at 1/4 size: the same look, 16x cheaper)"""
    q = 4; sw, sh = pw // q, ph // q
    sm = im.resize((max(1, im.width // q), max(1, im.height // q)), Image.BILINEAR)
    s = max(sw / sm.width, sh / sm.height); sm = sm.resize((int(math.ceil(sm.width * s)), int(math.ceil(sm.height * s))), Image.BILINEAR)
    l, t_ = (sm.width - sw) // 2, (sm.height - sh) // 2
    sm = sm.crop((l, t_, l + sw, t_ + sh)).filter(ImageFilter.GaussianBlur(9))
    sm = ImageEnhance.Color(sm).enhance(0.9); sm = ImageEnhance.Brightness(sm).enhance(1 - dim)
    return sm.resize((pw, ph), Image.BILINEAR)


def _wipe_frac(g, t):
    wa, wd, pk = g.get("wipe_at", 1.0), g.get("wipe_dur", 0.7), g.get("park", 0.0)
    u = t - wa
    if u <= 0: return 0.0
    if not pk: return ease_io3(u / wd)
    hf = wd / 2
    if u < hf: return 0.5 * ease_io3(u / hf)
    if u < hf + pk: return 0.5
    return 0.5 + 0.5 * ease_io3((u - hf - pk) / hf)


def ba_frames(plan, seq, g, f0, n):
    pair = g["kind"] == "ba_pair"; dur = g["t1"] - g["t0"]
    P = G.BOX; pw, ph = P[2] - P[0], P[3] - P[1]
    cw, ch = (470, 836) if pair else (520, 924)
    xs = [65, 545] if pair else [(W - cw) / 2 - P[0]]
    y0 = (ph - ch) / 2
    words = g.get("labels" if pair else "tags") or ["ORIGINAL", "OURS"]
    srcB = media_pipe(plan, seq, g["before"], f0, n, cw, ch); srcA = media_pipe(plan, seq, g["after"], f0, n, cw, ch)
    cmask = rounded_mask((cw, ch), (0, 0, cw, ch), 28)
    m = 60; dress = card_dressing((cw + 2 * m, ch + 2 * m), (m, m, m + cw, m + ch), 28)
    fb, fa_ = text_sprite(words[0], ImageFont.truetype(INTER_B, 26), (255, 255, 255, 178)), text_sprite(words[1], ImageFont.truetype(INTER_B, 26), GOLD + (255,))
    rtl = g.get("dir") == "rtl"
    line = Image.new("RGBA", (40, ch), (0, 0, 0, 0)); ImageDraw.Draw(line).rectangle((18, 0, 21, ch), fill=(255, 255, 255, 120))
    line = line.filter(ImageFilter.GaussianBlur(5)); ImageDraw.Draw(line).rectangle((18, 0, 21, ch), fill=(255, 255, 255, 255))
    for i in range(f0, f0 + n):
        t = i / FPS_MG
        bf, af = next(srcB), next(srcA)
        panel = _backdrop(af, pw, ph, g.get("dim", 0.35)).convert("RGBA")
        if not pair:
            fr_ = _wipe_frac(g, t); xl = int(round(cw * (1 - fr_ if rtl else fr_)))
            bp, ap = bf.convert("RGBA"), af.convert("RGBA")          # each side carries its own tag, so a tag shows only on its side
            (tb, mb), (ta, ma) = fb, fa_
            bpos = (14 - mb, 14 - mb) if rtl else (cw - 14 - (tb.width - 2 * mb) - mb, 14 - mb)
            apos = (cw - 14 - (ta.width - 2 * ma) - ma, 14 - ma) if rtl else (14 - ma, 14 - ma)
            bp.alpha_composite(tb, bpos); ap.alpha_composite(ta, apos)
            pic = bp
            if fr_ > 0:
                if rtl: pic.paste(ap.crop((xl, 0, cw, ch)), (xl, 0))
                else: pic.paste(ap.crop((0, 0, xl, ch)), (0, 0))
            if 0 < fr_ < 1: pic.alpha_composite(line, (xl - 20, 0))
            pic.putalpha(cmask)
            sp = dress.copy(); sp.alpha_composite(pic, (m, m))
            panel.alpha_composite(sp, (int(round(xs[0] - m)), int(round(y0 - m))))
        else:
            for k, (img, (ts, ms)) in enumerate(((bf, fb), (af, fa_))):
                tk = t - 0.3 * k
                if tk <= 0: continue
                p = ease(tk / 0.42); dy, al = 38 * (1 - p), min(1.0, ease(tk / (0.42 * 0.7)))
                pic = img.convert("RGBA"); pic.putalpha(cmask)
                sp = dress.copy(); sp.alpha_composite(pic, (m, m))
                at = g.get("labels_at", "above")
                lx = m + 4 - ms if at == "above" else m + 18 - ms
                ly = (m - 14 - (ts.height - 2 * ms) - ms) if at == "above" else (m + 16 - ms if at == "top" else m + ch - 16 - (ts.height - 2 * ms) - ms)
                sp.alpha_composite(ts, (lx, ly))
                panel.alpha_composite(with_alpha(sp, al), (int(round(xs[k] - m)), int(round(y0 - m + dy))))
        fr = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        fr.paste(with_alpha(panel, fade_al(t, dur, g.get("fade_in", 0.3), 0.24)), (P[0], P[1]))
        yield fr


# ---------- screen marks: spotlight, select, cursor (research #4) ----------
def spotlight_frame(plan, g, t, dur):
    fr = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    b = box_at(plan, g["box"], g["t0"] + t, g.get("pad", 16))
    if b is None: return fr
    al = fade_al(t, dur, 0.25, 0.2)
    P = G.BOX; pw, ph = P[2] - P[0], P[3] - P[1]
    hole = Image.new("L", (pw, ph), 0)
    ImageDraw.Draw(hole).rounded_rectangle((b[0] - P[0], b[1] - P[1], b[2] - P[0], b[3] - P[1]), 18, fill=255)
    hole = hole.filter(ImageFilter.GaussianBlur(5))                  # ~10 px feather
    dimL = ImageChops.invert(hole).point(lambda v: int(v * 0.45 * al))
    lay = Image.new("RGBA", (pw, ph), (0, 0, 0, 255)); lay.putalpha(dimL); fr.alpha_composite(lay, (P[0], P[1]))
    if g.get("tag") and t > 0.15:
        tag = sprite_tag(g["tag"]); gap = 26
        below = (b[3] + gap, b[3] + gap + tag.height); above = (b[1] - gap - tag.height, b[1] - gap)
        ok = lambda yy: yy[0] >= 200 and yy[1] <= min(1620, P[3] - 70)
        ty0, ty1 = below if ok(below) or not ok(above) else above
        tx0 = min(max(b[0], 40), W - 40 - tag.width)
        pl = clamp01((t - 0.15) / 0.2); pa = clamp01((t - 0.25) / 0.3)
        Lc = Local(tx0 + 20, min(ty0, b[3]) - 4, tx0 + 36, max(ty1, b[1]) + 4)
        lx = tx0 + 28
        ya, yb = (b[3], ty0) if ty0 >= b[3] else (b[1], ty1)
        Lc.d.line([Lc.S((lx, ya)), Lc.S((lx, ya + (yb - ya) * ease(pl)))], fill=(255, 255, 255, 230), width=2 * Lc.ss)
        im, xy = Lc.out(); put(fr, with_alpha(im, al), xy)
        if pa > 0:
            sh, pad = soft_shadow(tag, blur=14, alpha=110, dy=6)
            put(fr, with_alpha(sh, ease(pa) * al), (tx0 - pad, ty0 - pad + 10 * (1 - ease(pa))))
    return fr


def _perimeter(b):
    x0, y0, x1, y1 = b
    return [(x0, y0), (x1, y0), (x1, y1), (x0, y1), (x0, y0)]


def select_frame(plan, g, t, dur):
    fr = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    td = t - g.get("draw_at", 0.0)
    b = box_at(plan, g["box"], g["t0"] + t, g.get("pad", 8))
    if b is None or td < 0: return fr
    al = fade_al(t, dur, 0, 0.2)
    p = ease_io3(td / 0.3)
    x0, y0, x1, y1 = b; Lp = 2 * ((x1 - x0) + (y1 - y0))
    Lc = Local(x0 - 14, y0 - 14, x1 + 14, y1 + 14); S = Lc.S
    if p > 0: Lc.d.line([S(q) for q in _partial(_perimeter(b), p)], fill=(255, 255, 255, 255), width=2 * Lc.ss, joint="curve")
    reach = [0.0, (x1 - x0) / Lp, ((x1 - x0) + (y1 - y0)) / Lp, (2 * (x1 - x0) + (y1 - y0)) / Lp]
    for (cx, cy), fq in zip([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], reach):
        if p + 1e-9 < fq: continue
        tq = 0.0 if fq <= 0 else next((k / 600 for k in range(601) if ease_io3(k / 600) >= fq), 1.0) * 0.3
        s = 6 * ease_back(clamp01((td - tq) / 0.14), 2.0)
        if s <= 0.2: continue
        Lc.d.rectangle(Lc.R((cx - s - 1, cy - s - 1, cx + s + 1, cy + s + 1)), fill=(18, 18, 18, 255))
        Lc.d.rectangle(Lc.R((cx - s, cy - s, cx + s, cy + s)), fill=(255, 255, 255, 255))
    im, xy = Lc.out(); im = drop_shadow(im, blur=3, alpha=120, dy=1)
    put(fr, with_alpha(im, al), xy)
    if g.get("chip") and td > 0.22:
        pc = ease(clamp01((td - 0.22) / 0.28)); chip = sprite_mono(g["chip"], 22)
        sh, pad = soft_shadow(chip, blur=10, alpha=110, dy=4)
        put(fr, with_alpha(sh, pc * al), (x0 - pad, y0 - 34 - pad + 8 * (1 - pc)))
    return fr


_CURSOR = {}


def cursor_sprite(sc=1.0):
    """the macOS arrow: 46 px tall, white, a 2.5 px black outline, a 6 px shadow; returns (sprite, tip offset)"""
    key = round(sc, 3)
    if key in _CURSOR: return _CURSOR[key]
    pts = [(0, 0), (0, 28.5), (6.5, 22.4), (10.6, 31.6), (14.3, 30.0), (10.3, 21.0), (19.5, 21.0)]
    k = 41 / 31.6 * sc; ss = 4; m = 16
    w, h = int(19.5 * k + 2 * m), int(31.6 * k + 2 * m)
    im = Image.new("RGBA", (w * ss, h * ss), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    P_ = [((x * k + m) * ss, (y * k + m) * ss) for x, y in pts]
    d.polygon(P_, fill=(0, 0, 0, 255)); d.line(P_ + [P_[0], P_[1]], fill=(0, 0, 0, 255), width=int(5 * ss * sc), joint="curve")
    d.polygon(P_, fill=(255, 255, 255, 255))
    im = im.resize((w, h), Image.LANCZOS)
    a = im.split()[3].point(lambda v: v * 110 // 255); sh = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    sh.paste(Image.new("RGBA", (w, h), (0, 0, 0, 255)), (2, 3), a); sh = sh.filter(ImageFilter.GaussianBlur(3)); sh.alpha_composite(im)
    _CURSOR[key] = (sh, (m, m)); return _CURSOR[key]


def cursor_point(b, at):
    if at == "tl": return (b[0], b[1])
    if at == "center": return ((b[0] + b[2]) / 2, (b[1] + b[3]) / 2)
    return (b[2], b[3])


def cursor_frame(plan, g, t, dur):
    fr = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    b = box_at(plan, g["box"], g["t0"] + t)
    if b is None: return fr
    P0 = cursor_point(b, g.get("at", "br")); gl = g.get("glide", 0.55); ck = g.get("click_at", 0.55)
    st = (P0[0] + 220, P0[1] + 260); ctrl = (P0[0] + 190, P0[1] + 70)
    u = ease_io3(t / gl) if gl > 0 else 1.0
    pos = ((1 - u) ** 2 * st[0] + 2 * (1 - u) * u * ctrl[0] + u * u * P0[0], (1 - u) ** 2 * st[1] + 2 * (1 - u) * u * ctrl[1] + u * u * P0[1])
    al = min(clamp01(t / 0.1), fade_al(t, dur, 0, 0.2))
    tc = t - ck
    sc = 1.0
    if 0 <= tc < 0.12: sc = 1 - 0.12 * (1 - abs(tc - 0.06) / 0.06)
    if 0 <= tc < 0.35:                                      # the ripple ring: r 0 -> 48, 3 px, alpha 1 -> 0
        q = tc / 0.35; r = 48 * ease(q)
        Lc = Local(P0[0] - 56, P0[1] - 56, P0[0] + 56, P0[1] + 56)
        if r > 1.5: Lc.d.ellipse(Lc.R((P0[0] - r, P0[1] - r, P0[0] + r, P0[1] + r)), outline=(255, 255, 255, int(255 * (1 - q))), width=3 * Lc.ss)
        im, xy = Lc.out(); put(fr, with_alpha(im, al), xy)
    sp, (ox, oy) = cursor_sprite(sc)
    put(fr, with_alpha(sp, al), (pos[0] - ox, pos[1] - oy))
    return fr


# ---------- loupe (research #7) ----------
def loupe_geom(plan, g):
    r = g.get("r", 150)
    tb = box_at(plan, g["box"], g["t0"] + 0.05)
    if tb is None: raise SystemExit(f"loupe {g['id']}: a face-only beat at its start")
    if g.get("rest"): rx, ry = g["rest"]
    else:
        room = {"right": 1020 - tb[2], "left": tb[0] - 60, "below": 1000 - tb[3], "above": tb[1] - 236}
        side = max(room, key=room.get); mx, my = (tb[0] + tb[2]) / 2, (tb[1] + tb[3]) / 2
        rx, ry = {"right": (tb[2] + 60 + r, my), "left": (tb[0] - 60 - r, my), "below": (mx, tb[3] + 60 + r), "above": (mx, tb[1] - 60 - r)}[side]
    clampc = lambda v, lo, hi: (lo + hi) / 2 if lo > hi else min(max(v, lo), hi)
    return r, (clampc(rx, 60 + r, 1020 - r), clampc(ry, 236 + r, 1000 - r))


def loupe_src_rect(plan, g, r):
    """the source square the lens shows: mag x the panel's display scale, centred on the target, kept inside the recording"""
    v = view_at(plan, g["t0"] + 0.3) or view_at(plan, g["t0"] + 0.05)
    k = G.BASE * v["z"] * g.get("mag", 2.2); rs = r / k
    b = box_src(plan, g["box"]); cx, cy = (b[0] + b[2]) / 2, (b[1] + b[3]) / 2
    cx, cy = min(max(cx, rs), G.SW - rs), min(max(cy, rs), G.SH - rs)
    return (cx - rs, cy - rs, cx + rs, cy + rs)


def loupe_lens(content, r):
    """content (2r x 2r RGB) -> the lens sprite: a circle, a 4 px white ring + a 1 px dark outer ring, a 26 px shadow"""
    ss = 3; m = 40; D = 2 * r
    im = Image.new("RGBA", ((D + 2 * m) * ss, (D + 2 * m) * ss), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    big = content.resize((D * ss, D * ss), Image.BICUBIC).convert("RGBA")
    cm = Image.new("L", (D * ss, D * ss), 0); ImageDraw.Draw(cm).ellipse((0, 0, D * ss - 1, D * ss - 1), fill=255)
    im.paste(big, (m * ss, m * ss), cm)
    o = m * ss
    d.ellipse((o - 5 * ss, o - 5 * ss, o + D * ss + 5 * ss - 1, o + D * ss + 5 * ss - 1), outline=(20, 20, 20, 200), width=1 * ss)
    d.ellipse((o - 4 * ss, o - 4 * ss, o + D * ss + 4 * ss - 1, o + D * ss + 4 * ss - 1), outline=(255, 255, 255, 255), width=4 * ss)
    im = im.resize((D + 2 * m, D + 2 * m), Image.LANCZOS)
    a = im.split()[3].point(lambda v: v * 150 // 255); sh = Image.new("RGBA", im.size, (0, 0, 0, 0))
    sh.paste(Image.new("RGBA", im.size, (0, 0, 0, 255)), (0, 8), a); sh = sh.filter(ImageFilter.GaussianBlur(13)); sh.alpha_composite(im)
    return sh, m + r


def loupe_frames(plan, seq, g, f0, n):
    dur = g["t1"] - g["t0"]
    r, rest = loupe_geom(plan, g)
    sr = loupe_src_rect(plan, g, r)
    if g.get("live"):
        src = seq_pipe(plan, seq, g["t0"], f0, n, [crop_vf(sr), f"scale={2 * r}:{2 * r}:flags=bicubic"], 2 * r, 2 * r)
        lens = None
    else:
        tr = seq["v"][plan["screen_track"]]; ts = g["t0"] + 0.3; c = G.clip_at(tr, ts)
        still_ = G.frame(c["p"], G.src_time(c, ts)).crop(tuple(int(round(x)) for x in sr)).resize((2 * r, 2 * r), Image.BICUBIC)
        lens = loupe_lens(still_, r); src = None
    for i in range(f0, f0 + n):
        t = i / FPS_MG
        if src is not None: ls, off = loupe_lens(next(src), r)
        else: ls, off = lens
        fr = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        tb = box_at(plan, g["box"], g["t0"] + t)
        if tb is None: yield fr; continue
        start = ((tb[0] + tb[2]) / 2, (tb[1] + tb[3]) / 2)
        if t < 0.4:
            p = ease_back(t / 0.4, 1.2); sc, al = 0.35 + 0.65 * p, clamp01(t / 0.15); c_ = (start[0] + (rest[0] - start[0]) * p, start[1] + (rest[1] - start[1]) * p)
        elif t > dur - 0.22:
            q = ease((t - (dur - 0.22)) / 0.22); sc, al, c_ = 1 - 0.1 * q, 1 - q, rest
        else:
            sc, al, c_ = 1.0, 1.0, rest
        if al <= 0.01: yield fr; continue
        pl = ease(clamp01((t - 0.3) / 0.2))                 # the leader draws in 0.2 s once the lens has nearly landed
        if pl > 0:
            ang = math.atan2(c_[1] - start[1], c_[0] - start[0])
            # from the target box's edge (towards the lens) to the lens rim
            hx, hy = (tb[2] - tb[0]) / 2, (tb[3] - tb[1]) / 2
            kx = hx / abs(math.cos(ang)) if abs(math.cos(ang)) > 1e-6 else 1e9; ky = hy / abs(math.sin(ang)) if abs(math.sin(ang)) > 1e-6 else 1e9
            e0 = (start[0] + math.cos(ang) * (min(kx, ky) + 6), start[1] + math.sin(ang) * (min(kx, ky) + 6))
            e1 = (c_[0] - math.cos(ang) * (r * sc + 5), c_[1] - math.sin(ang) * (r * sc + 5))
            if math.dist(start, c_) > math.dist(start, e0) + r * sc:
                Lc = Local(min(e0[0], e1[0]) - 10, min(e0[1], e1[1]) - 10, max(e0[0], e1[0]) + 10, max(e0[1], e1[1]) + 10)
                e2 = (e0[0] + (e1[0] - e0[0]) * pl, e0[1] + (e1[1] - e0[1]) * pl)
                Lc.d.line([Lc.S(e0), Lc.S(e2)], fill=(255, 255, 255, 235), width=2 * Lc.ss)
                Lc.d.ellipse(Lc.R((e0[0] - 4, e0[1] - 4, e0[0] + 4, e0[1] + 4)), fill=(255, 255, 255, 235))
                im, xy = Lc.out(); put(fr, with_alpha(drop_shadow(im, 3, 110, 1), al), xy)
        s = ls if sc == 1 else ls.resize((max(1, int(ls.width * sc)), max(1, int(ls.height * sc))), Image.LANCZOS)
        put(fr, with_alpha(s, al), (c_[0] - s.width / 2, c_[1] - s.height / 2))
        yield clip_panel(fr)


# ---------- timecode + scrub (research #11) ----------
def timecode_frame(plan, g, t, dur, cache):
    fr = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ta = g["t0"] + t; b = box_at(plan, g["box"], ta)
    if b is None: return fr
    steps = sorted(g["steps"], key=lambda s_: s_[0])
    k = max([i for i, s_ in enumerate(steps) if s_[0] <= ta + 1e-9] or [0])
    al = fade_al(t, dur, 0.3, 0.24); dy = 10 * (1 - ease(clamp01(t / 0.3)))
    def pill(txt):
        if txt not in cache: cache[txt] = soft_shadow(sprite_mono(txt, 30, h=56, dot=True, r=16, fill=(14, 14, 14, 230)), blur=12, alpha=110, dy=5)
        return cache[txt]
    dock = g.get("dock", "tl"); sw = pill(steps[k][1])[0].width - 2 * pill(steps[k][1])[1]
    x = b[0] + 16 if dock in ("tl", "bl") else b[2] - 16 - sw
    y = (b[1] + 16 if dock in ("tl", "tr") else b[3] - 16 - 56 - (24 if g.get("above_scrub") else 0)) + dy
    xf = clamp01((ta - steps[k][0]) / 0.12) if k > 0 and steps[k][0] > g["t0"] else 1.0
    if xf < 1:
        sp, pad = pill(steps[k - 1][1]); put(fr, with_alpha(sp, al * (1 - xf)), (x - pad, y - pad))
    sp, pad = pill(steps[k][1]); put(fr, with_alpha(sp, al * xf), (x - pad, y - pad))
    return fr


def scrub_frac(g, ta):
    if g.get("keys"):
        ks = sorted(g["keys"])
        if ta <= ks[0][0]: return ks[0][1]
        for (a, fa), (b, fb_) in zip(ks, ks[1:]):
            if ta <= b: return fa + (fb_ - fa) * (ta - a) / max(b - a, 1e-6)
        return ks[-1][1]
    return g.get("p0", 0.0) + (g.get("p1", 1.0) - g.get("p0", 0.0)) * clamp01((ta - g["t0"]) / max(g["t1"] - g["t0"], 1e-6))


def scrub_frame(plan, g, t, dur):
    fr = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ta = g["t0"] + t; b = box_at(plan, g["box"], ta)
    if b is None: return fr
    al = fade_al(t, dur, 0.25, 0.24)
    x0, x1, yc = b[0], b[2], b[3] - 10
    Lc = Local(x0 - 16, yc - 20, x1 + 16, yc + 20); S = Lc.S; d = Lc.d; ss = Lc.ss
    d.rounded_rectangle(Lc.R((x0, yc - 3, x1, yc + 3)), 3 * ss, fill=(255, 255, 255, 64))
    fx = x0 + (x1 - x0) * clamp01(scrub_frac(g, ta))
    if fx > x0 + 1: d.rounded_rectangle(Lc.R((x0, yc - 3, fx, yc + 3)), 3 * ss, fill=GOLD + (255,))
    for tk in g.get("ticks", []):
        q = (ta - tk[0]) / 0.18
        if q <= 0: continue
        hgt = 9 * ease_back(clamp01(q), 2.0); tx = x0 + (x1 - x0) * tk[1]
        d.rounded_rectangle(Lc.R((tx - 2, yc - hgt, tx + 2, yc + hgt)), 2 * ss, fill=GOLD + (255,))
    d.ellipse(Lc.R((fx - 7, yc - 7, fx + 7, yc + 7)), fill=(255, 255, 255, 255))
    im, xy = Lc.out(); put(fr, with_alpha(drop_shadow(im, 3, 140, 1), al), xy)
    return fr


# ---------- hook_title (research #13), chip (research #10) ----------
def sprite_hook_title(g):
    f1 = ImageFont.truetype(BEBAS, 60)
    l2 = g["line2"]
    if is_rich(l2): f2, plain2 = ImageFont.truetype(BEBAS, 84), False
    else: f2, plain2 = font_at(ACCENT_FONT, 84, accent_axes(ACCENT_FONT)), True
    tmp = ImageDraw.Draw(Image.new("RGBA", (1, 1)))
    w1 = tmp.textlength(g.get("line1", ""), font=f1); w2 = rich_len(l2, f2) if not plain2 else tmp.textlength(l2, font=f2)
    w = int(max(w1, w2) + 60); c1 = cap_h(f1)
    gap = 26; h = int(30 + c1 + gap + cap_h(f2) + f2.getmetrics()[1] + 20)
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    b1 = 30 + c1
    if g.get("line1"): d.text((w / 2, b1), g["line1"], font=f1, fill=(255, 255, 255, 204), anchor="ms")
    b2 = b1 + gap + cap_h(f2)
    if plain2: d.text((w / 2, b2), l2, font=f2, fill=GOLD + (255,), anchor="ms")
    else: draw_rich(d, (w / 2, b2), l2, f2, (255, 255, 255, 255), anchor="ms")
    return im


def sprite_chip(plan, seq, g):
    fn, fs = ImageFont.truetype(INTER_B, 30), ImageFont.truetype(INTER_R, 22)
    tmp = ImageDraw.Draw(Image.new("RGBA", (1, 1)))
    nw = tmp.textlength(g["name"], font=fn); sw = tmp.textlength(g.get("sub", ""), font=fs) if g.get("sub") else 0
    h = 84; x = 10 + 64 + 16
    w = int(x + max(nw + (40 if g.get("verified") else 0), sw) + 30)
    pill = card_body((w, h), h // 2, (16, 16, 16, 238), outline=(255, 255, 255, 38), width=2)
    if g.get("avatar"):
        pill.alpha_composite(avatar_img(plan, seq, g, 64), (10, 10))
    else:
        av = Image.new("RGBA", (64 * 3, 64 * 3), (0, 0, 0, 0)); ImageDraw.Draw(av).ellipse((0, 0, 191, 191), fill=GOLD + (255,))
        ImageDraw.Draw(av).text((96, 98), g["name"][:1].upper(), font=ImageFont.truetype(INTER_B, 96), fill=(15, 15, 15, 255), anchor="mm")
        pill.alpha_composite(av.resize((64, 64), Image.LANCZOS), (10, 10))
    d = ImageDraw.Draw(pill)
    if g.get("sub"):
        d.text((x, 40), g["name"], font=fn, fill=(255, 255, 255, 255), anchor="ls"); d.text((x, 68), g["sub"], font=fs, fill=(165, 165, 165, 255), anchor="ls")
    else:
        d.text((x, h / 2), g["name"], font=fn, fill=(255, 255, 255, 255), anchor="lm")
    if g.get("verified"): pill.alpha_composite(verified(24), (int(x + nw + 10), 18 if g.get("sub") else 30))
    return pill


def flip_frame(sp, g, plan, t, cx, cy):
    """channel_card flip_at / flip_to (research #8): the card flies into the real page's box, scaling to its height, and
    cross-fades out over the last 0.15 s"""
    u = (g["t0"] + t - g["flip_at"]) / 0.45
    fr = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    if u >= 1: return fr
    tb = box_at(plan, g["flip_to"], g["flip_at"] + 0.05)
    if tb is None: raise SystemExit(f"channel_card {g['id']}: flip_to lands on a face-only beat")
    p = ease_io3(u); tx, ty = (tb[0] + tb[2]) / 2, (tb[1] + tb[3]) / 2
    sc = 1 + ((tb[3] - tb[1]) / sp.height - 1) * p
    x, y = cx + (tx - cx) * p, cy + (ty - cy) * p
    al = 1.0 if u < 1 - 0.15 / 0.45 else (1 - u) / (0.15 / 0.45)
    sh, pad = soft_shadow(sp, blur=22, alpha=120, dy=10)
    s = sh.resize((max(1, int(sh.width * sc)), max(1, int(sh.height * sc))), Image.LANCZOS)
    put(fr, with_alpha(s, al), (x - s.width / 2, y - s.height / 2))
    return fr


# ---------- 2026-10-27: batch-5 reaction heroes (J ink_reveal, K rows_blur, L quadrant) ----------
INK = (196, 18, 30)


def ink_frames(plan, seq, g, f0, n):
    """ink_reveal (Reaction J, FX-15 Red Ink Bleed): a red ink blot opens at g["origin_src"] (screen source px, mapped through the
    view at t0) and spreads over the whole panel with a wet, feathered, wobbling edge, revealing `card` inside: the FIRST frame of
    a ba_wipe master card ({"file": <master>, "t": s}), drawn exactly as ba_frames draws it, so the play card that starts at t1
    (its fade_in 0) continues it without a seam. The panel outside the ink darkens to 30 % while it spreads. grow (s, default
    the whole graphic) easeInOutCubic; the red rim is 34 px wide at the edge and fades as the blot covers the panel."""
    import numpy as np
    dur = g["t1"] - g["t0"]; P = G.BOX; pw, ph = P[2] - P[0], P[3] - P[1]
    card = dict(kind="ba_wipe", t0=g["t0"], t1=g["t0"] + 1.0, before=g["card"], after=g["card"], wipe_at=999, wipe_dur=0.7,
                tags=g.get("tags", ["", ""]), dim=g.get("dim", 0.35), fade_in=0)
    full = next(ba_frames(plan, seq, card, 0, 1)).crop((P[0], P[1], P[2], P[3]))
    v = view_at(plan, g["t0"] + 0.01); ox, oy = src_to_frame(v, *g["origin_src"]); ox, oy = ox - P[0], oy - P[1]
    q = 2; gw, gh = pw // q, ph // q
    yy, xx = np.mgrid[0:gh, 0:gw].astype(np.float32); xx = xx * q - ox; yy = yy * q - oy
    d = np.sqrt(xx * xx + yy * yy); th = np.arctan2(yy, xx)
    rmax = max(math.hypot(ox - x, oy - y) for x in (0, pw) for y in (0, ph)) * 1.5
    rng = np.random.default_rng(g.get("seed", 15))
    harm = [(k, 0.16 / (1 + 0.55 * (k - 3)), rng.uniform(0, 6.283), rng.uniform(-1.6, 1.6)) for k in range(3, 15)]
    fine = np.asarray(Image.fromarray((rng.random((gh // 6 + 2, gw // 6 + 2)) * 255).astype(np.uint8)).resize((gw, gh), Image.BICUBIC)).astype(np.float32) / 255 - 0.5
    grow = g.get("grow", dur); veil = g.get("veil", 0.3)
    full_np = np.asarray(full.convert("RGBA")).astype(np.float32)
    for i in range(f0, f0 + n):
        t = i / FPS_MG; p = ease_io3(min(1.0, t / grow)); R = 6 + (rmax - 6) * p
        wob = sum(a * np.sin(k * th + ph0 + w * t) for k, a, ph0, w in harm)
        r = R * (1 + 0.55 * wob * (1 - 0.5 * p)) + 18 * fine * (1 - 0.4 * p)
        feather = 10 + 14 * p
        m = np.clip((r - d) / feather + 0.5, 0, 1) if p < 0.999 else np.ones_like(d)      # 1 inside the blot (all of it at the end)
        rim = np.clip(1 - (r - d) / (34 + 20 * p), 0, 1) * m * (1 - 0.85 * p ** 3)   # red near the edge, gone as it covers
        M = np.asarray(Image.fromarray((m * 255).astype(np.uint8)).resize((pw, ph), Image.BILINEAR)).astype(np.float32)[..., None] / 255
        Rm = np.asarray(Image.fromarray((rim * 255).astype(np.uint8)).resize((pw, ph), Image.BILINEAR)).astype(np.float32)[..., None] / 255
        rgb = full_np[..., :3] * (1 - Rm * 0.92) + np.array(INK, np.float32) * (Rm * 0.92)
        a_in = M; a_out = (1 - M) * veil * min(1.0, t / 0.25)                 # the darkening veil outside the ink
        al = a_in + a_out
        col = (rgb * a_in + 0 * a_out) / np.maximum(al, 1e-6)
        out = np.concatenate([np.clip(col, 0, 255), np.clip(al * 255, 0, 255)], axis=2).astype(np.uint8)
        fr = Image.new("RGBA", (W, H), (0, 0, 0, 0)); fr.paste(Image.fromarray(out, "RGBA"), (P[0], P[1]))
        yield fr


def sprite_rows_blur(g, tt):
    """rows_blur (Reaction K, FX-35 Blur-Isolate Row, the casual viewer's experience): a title and rows of the terms their Short used,
    each landing SHARP as it is named (rows [[t, "TERM", "small grey gloss"]]); from blur_at every row defocuses (0 -> 7 px, staggered
    60 ms per row) and dims to 45 %, and the verdict line (verdict [t, "TOO *niche*"]) lands under them, sharp."""
    ft = fit_font(BEBAS, 54, [g["title"]], g.get("w", 760) - 88, 36)
    rows = g["rows"]; w = g.get("w", 760); rh = 74; h = 30 + 54 + 20 + rh * len(rows) + (96 if g.get("verdict") else 18)
    card = card_body((w, h), 34, (14, 14, 14, 244), outline=(255, 255, 255, 34), width=2)
    draw_rich(ImageDraw.Draw(card), (44, 28), g["title"], ft, GOLD + (255,))
    fr_ = fit_font(INTER_B, 34, [r_[1] for r_ in rows], w - 88 - 190, 22); fs = ImageFont.truetype(PLEX_MONO, 20)
    ba = g.get("blur_at", 1e9)
    for i, row in enumerate(rows):
        st, txt = row[0], row[1]; sub = row[2] if len(row) > 2 else ""
        a = min(1.0, max(0.0, (tt - st) / 0.3))
        if a <= 0: continue
        lay = Image.new("RGBA", (w, rh), (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
        dl.text((44, rh / 2), txt, font=fr_, fill=(255, 255, 255, 255), anchor="lm")
        if sub: dl.text((w - 44, rh / 2), sub, font=fs, fill=(150, 150, 150, 255), anchor="rm")
        dl.line([(44, rh - 2), (w - 44, rh - 2)], fill=(255, 255, 255, 22), width=1)
        b = min(1.0, max(0.0, (tt - ba - 0.06 * i) / 0.55))
        if b > 0:
            lay = lay.filter(ImageFilter.GaussianBlur(7 * ease(b))); lay.putalpha(lay.split()[3].point(lambda q_: int(q_ * (1 - 0.55 * ease(b)))))
        if a < 1: lay.putalpha(lay.split()[3].point(lambda q_: int(q_ * ease(a))))
        card.alpha_composite(lay, (0, int(30 + 54 + 20 + rh * i + (1 - ease(a)) * 12)))
    if g.get("verdict"):
        vt, vtxt = g["verdict"]; a = min(1.0, max(0.0, (tt - vt) / 0.32))
        if a > 0:
            fv = fit_font(BEBAS, 64, [vtxt.replace("*", "")], w - 88, 40)
            lay = Image.new("RGBA", (w, 90), (0, 0, 0, 0)); draw_rich(ImageDraw.Draw(lay), (44, 12), vtxt, fv, (255, 255, 255, 255))
            if a < 1: lay.putalpha(lay.split()[3].point(lambda q_: int(q_ * ease(a))))
            card.alpha_composite(lay, (0, h - 96 + int((1 - ease(a)) * 10)))
    return card


def sprite_quadrant(g, tt):
    """quadrant (Reaction L, FX-69/70 Lone Yellow Bar + Ring as a two-axis map of his words): x axis = g["x_label"], y axis =
    g["y_label"], each axis DRAWS from the origin at its time (axes [[t, "x"|"y"]]), corner tags fade in at theirs (tags [[t, "tl"|"bl"|"br",
    "TEXT"]]), dots pop at theirs (dots [[t, fx, fy, "LABEL", "grey"|"gold"]], fx / fy 0..1 of the plot) and a gold dot gets a ring
    that draws round it 0.25 s after it lands."""
    w = g.get("w", 760); h = g.get("h", 700); ss = 3
    card = card_body((w, h), 36, (14, 14, 14, 244), outline=(255, 255, 255, 34), width=2)
    dc = ImageDraw.Draw(card)
    ft = fit_font(BEBAS, 50, [g["title"].replace("*", "")], w - 88, 34); draw_rich(dc, (44, 26), g["title"], ft, GOLD + (255,))
    x0, y0, x1, y1 = 96, 120, w - 50, h - 92                                 # the plot box (origin bottom-left)
    lay = Image.new("RGBA", (w * ss, h * ss), (0, 0, 0, 0)); dl = ImageDraw.Draw(lay); S = lambda x, y: (x * ss, y * ss)
    fl = ImageFont.truetype(PLEX_MONO, 20 * ss); fg = ImageFont.truetype(INTER_B, 22 * ss); fd = ImageFont.truetype(INTER_B, 24 * ss)
    for at, ax in g.get("axes", []):
        a = ease(min(1.0, max(0.0, (tt - at) / 0.45)))
        if a <= 0: continue
        if ax == "x":
            dl.line([S(x0, y1), S(x0 + (x1 - x0) * a, y1)], fill=(255, 255, 255, 200), width=3 * ss)
            if a > 0.95: dl.polygon([S(x1, y1), S(x1 - 14, y1 - 8), S(x1 - 14, y1 + 8)], fill=(255, 255, 255, 200))
            dl.text(S(x1, y1 + 22), g["x_label"], font=fl, fill=(170, 170, 170, int(255 * a)), anchor="ra")
        else:
            dl.line([S(x0, y1), S(x0, y1 - (y1 - y0) * a)], fill=(255, 255, 255, 200), width=3 * ss)
            if a > 0.95: dl.polygon([S(x0, y0), S(x0 - 8, y0 + 14), S(x0 + 8, y0 + 14)], fill=(255, 255, 255, 200))
            tl = Image.new("RGBA", (int(dl.textlength(g["y_label"], font=fl)) + 8, 30 * ss), (0, 0, 0, 0))
            ImageDraw.Draw(tl).text((0, 0), g["y_label"], font=fl, fill=(170, 170, 170, int(255 * a)))
            tl = tl.rotate(90, expand=True); lay.alpha_composite(tl, (int((x0 - 52) * ss), int(y0 * ss)))
    pos = {"tl": (x0 + 24, y0 + 10, "la"), "bl": (x0 + 24, y1 - 40, "la"), "br": (x1 - 10, y1 - 40, "ra"), "tr": (x1 - 10, y0 + 10, "ra")}
    for at, c, txt in g.get("tags", []):
        a = ease(min(1.0, max(0.0, (tt - at) / 0.35)))
        if a > 0: x, y, an = pos[c]; dl.text(S(x, y), txt, font=fg, fill=(150, 150, 150, int(255 * a)), anchor=an)
    for at, fx, fy, txt, kind in g.get("dots", []):
        u = (tt - at) / 0.4
        if u <= 0: continue
        sc = ease_back(min(1.0, u), 1.7); x = x0 + (x1 - x0) * fx; y = y1 - (y1 - y0) * fy; rr = 13 * sc
        col = GOLD + (255,) if kind == "gold" else (190, 190, 190, 255)
        if kind == "gold":
            gl = Image.new("RGBA", lay.size, (0, 0, 0, 0)); ImageDraw.Draw(gl).ellipse([S(x - 34, y - 34), S(x + 34, y + 34)], fill=GOLD + (90,))
            lay.alpha_composite(gl.filter(ImageFilter.GaussianBlur(14 * ss)))
        dl.ellipse([S(x - rr, y - rr), S(x + rr, y + rr)], fill=col)
        if kind == "gold":
            rp = min(1.0, max(0.0, (tt - at - 0.25) / 0.45))
            if rp > 0: dl.arc([S(x - 30, y - 30), S(x + 30, y + 30)], -90, -90 + 360 * ease(rp), fill=GOLD + (255,), width=3 * ss)
        al = int(255 * min(1.0, u))
        left = fx > 0.6
        dl.text(S(x - 44 if left else x + 44, y), txt, font=fd, fill=(col[0], col[1], col[2], al), anchor="rm" if left else "lm")
    card.alpha_composite(lay.resize((w, h), Image.LANCZOS))
    return card


SEEKABLE = {"showcase": showcase_frames, "ba_wipe": ba_frames, "ba_pair": ba_frames, "loupe": loupe_frames, "ink_reveal": ink_frames}


def frames_from(plan, seq, g, f0, n):
    """frames f0 .. f0 + n of a graphic: a direct seek for the footage kinds, else the full generator (skipping)"""
    if g["kind"] in SEEKABLE: yield from SEEKABLE[g["kind"]](plan, seq, g, f0, n); return
    for i, f in enumerate(mg_frames(plan, seq, g)):
        if i >= f0 + n: return
        if i >= f0: yield f


# ---------- the tiered SFX palette (research #12): build_plan scripts import it; apply.py reads g["sfx"] / g["cues"] ----------
DEFAULT_SFX = {
    # native objects (cards / chips that ARE platform UI): a glassy tick / a soft pop
    "chip": "tick-glass", "channel_card": "pop-glass", "lower_third": "pop-soft", "label": "pop-soft", "timecode": "tick-glass",
    # screen marks: the click on the click, the lens focus on the loupe, a soft whoosh on the spotlight
    "cursor": None, "select": "tick-glass", "spotlight": "whoosh-soft", "loupe": "focus-pull", "scrub": None,
    "arrow": "whoosh-light", "underline": "whoosh-light", "move": "pop-soft", "distance": "pop-soft", "mock_title": "pop-glass",
    # verdict cards: pop-glass with a thin thud under it; count-ups: the data blip
    "title_card": "pop-glass", "checklist": "pop-glass", "compare": "pop-glass", "steps": "pop-glass", "stat": "blip-data",
    "hook_title": "whoosh-soft",
    # before / after: whoosh-soft at the sweep, shutter-film on the park, thud-thin on the reveal
    "ba_wipe": None, "ba_pair": "tick-glass", "showcase": None, "group": None,
}
UNDER_THUD = {"title_card", "checklist", "compare", "steps"}       # "thud-thin under pop-glass"


def default_sfx(g):
    """{"sfx": <sound at t0 or None>, "cues": [[t_abs, sound], ...]} for a graphic from the palette; a build_plan does
    `d = default_sfx(g); g.setdefault("sfx", d["sfx"]); g["cues"] = g.get("cues", []) + d["cues"]` (cues: abs times)"""
    k, t0 = g["kind"], g["t0"]; cues = []
    if k in UNDER_THUD: cues.append([round(t0, 3), "thud-thin"])
    if k == "cursor": cues.append([round(t0 + g.get("click_at", 0.55), 3), "click"])
    if k == "select" and g.get("draw_at"): return {"sfx": None, "cues": [[round(t0 + g["draw_at"], 3), "tick-glass"]]}
    if k == "scrub": cues += [[tk[0], "tick-glass"] for tk in g.get("ticks", [])]
    if k == "ba_pair": cues.append([round(t0 + 0.3, 3), "tick-glass"])
    if k == "ba_wipe":
        wa, wd, pk = g.get("wipe_at", 1.0), g.get("wipe_dur", 0.7), g.get("park", 0.0)
        cues.append([round(t0 + wa, 3), "whoosh-soft"])
        if pk: cues.append([round(t0 + wa + wd / 2, 3), "shutter-film"])
        cues.append([round(t0 + wa + wd + pk, 3), "thud-thin"])
    return {"sfx": DEFAULT_SFX.get(k), "cues": cues}


def graphic_cues(g):
    """every SFX cue of a graphic, (t_abs, sound), exactly as apply.py --overlays places them"""
    cues = []
    if g.get("sfx"): cues.append((g["t0"] + g.get("sfx_lead", 0.0), g["sfx"]))
    if g.get("sfx2"): cues.append((g.get("line2_at", g["t0"]), g["sfx2"]))
    if g.get("step_sfx"): cues += [(st, g["step_sfx"]) for st, _ in g["steps"][1:]]
    cues += [(c[0], c[1]) for c in g.get("cues", [])]          # 2026-10-27: a cue may carry its level as a 3rd item
    cues += [(tk[0], tk[2]) for tk in g.get("ticks", []) if len(tk) > 2 and tk[2]]
    return cues


def _frame_fn(plan, seq, g):
    """(fn, n): fn(i) renders frame i of a single (non-group, non-footage) graphic. Called in order by mg_frames, the caches
    behave exactly as the batch-2 generator's did (byte-identical output); check() calls it out of order."""
    dur = g["t1"] - g["t0"]; n = int(round(dur * FPS_MG))
    k = g["kind"]; E, F = g.get("entrance"), g.get("from_xy")
    if k == "channel_card":
        sp = sprite_channel_card(plan, seq, g); cx = card_cx(g, sp)
        if g.get("flip_at") is not None:
            tf = g["flip_at"] - g["t0"]
            return (lambda i: pop_frame(sp, cx, g["y"], i / FPS_MG, max(dur, tf) + 10, ent=E, from_xy=F) if i / FPS_MG < tf
                    else flip_frame(sp, g, plan, i / FPS_MG, cx, g["y"])), n
        return (lambda i: pop_frame(sp, cx, g["y"], i / FPS_MG, dur, ent=E, from_xy=F)), n
    if k in ("title_card", "label", "chip"):
        sp = sprite_chip(plan, seq, g) if k == "chip" else {"title_card": sprite_title_card, "label": sprite_label}[k](g)
        cx = card_cx(g, sp)
        return (lambda i: pop_frame(sp, cx, g["y"], i / FPS_MG, dur, ent=E, from_xy=F)), n
    if k == "hook_title":
        sp = sprite_hook_title(g)
        return (lambda i: pop_frame(sp, g.get("x", W / 2), g.get("y", 1450), i / FPS_MG, dur, ent=E or "rise", from_xy=F)), n
    if k == "lower_third":
        cache = {}
        def fn(i):
            nonlocal cache
            t = i / FPS_MG; ph2 = min(1.0, max(0.0, (g["t0"] + t - g["line2_at"]) / 0.45))
            key = round(ph2, 2)
            if key not in cache: cache = {key: sprite_lower_third(g, ph2)}
            return pop_frame(cache[key], card_cx(g, cache[key]), g["y"], t, dur, ent=E, from_xy=F)
        return fn, n
    if k == "move": return (lambda i: move_frame(plan, g, i / FPS_MG, dur)), n
    if k == "distance": return (lambda i: distance_frame(plan, g, i / FPS_MG, dur)), n
    if k == "steps":
        def fn(i):
            t = i / FPS_MG; tt = g["t0"] + t
            shown = [min(1.0, max(0.0, (tt - st) / 0.35)) for st, _ in g["steps"]]
            sp = sprite_steps(g, shown)
            return pop_frame(sp, card_cx(g, sp), g["y"], t, dur, ent=E, from_xy=F)
        return fn, n
    if k == "stat":
        cache = {}
        def fn(i):
            nonlocal cache
            t = i / FPS_MG; p = min(1.0, max(0.0, (t - 0.12) / g.get("count", 0.75))); key = round(p, 3)
            if key not in cache: cache = {key: sprite_stat(g, p)}
            return pop_frame(cache[key], card_cx(g, cache[key], g.get("x", W / 2)), g["y"], t, dur, ent=E, from_xy=F)
        return fn, n
    if k in ("checklist", "compare"):
        spf = sprite_checklist if k == "checklist" else sprite_compare
        def fn(i):
            t = i / FPS_MG; sp = spf(g, g["t0"] + t)
            return pop_frame(sp, card_cx(g, sp, g.get("x", W / 2)), g["y"], t, dur, ent=E, from_xy=F)
        return fn, n
    if k == "mock_title": return (lambda i: mock_title_frame(plan, g, i / FPS_MG, dur)), n
    if k == "arrow":
        box = target_box(plan, g); return (lambda i: arrow_frame(box, i / FPS_MG, dur)), n
    if k == "underline":
        box = target_box(plan, g); return (lambda i: underline_frame(box, i / FPS_MG, dur)), n
    if k == "spotlight": return (lambda i: clip_panel(spotlight_frame(plan, g, i / FPS_MG, dur))), n
    if k == "select": return (lambda i: clip_panel(select_frame(plan, g, i / FPS_MG, dur))), n
    if k == "cursor": return (lambda i: clip_panel(cursor_frame(plan, g, i / FPS_MG, dur))), n
    if k == "timecode":
        cache = {}; return (lambda i: clip_panel(timecode_frame(plan, g, i / FPS_MG, dur, cache))), n
    if k == "scrub": return (lambda i: clip_panel(scrub_frame(plan, g, i / FPS_MG, dur))), n
    if k in ("rows_blur", "quadrant"):                  # 2026-10-27: batch-5 heroes K / L (cards: placement + entrance as every card)
        spf = sprite_rows_blur if k == "rows_blur" else sprite_quadrant
        def fn(i):
            t = i / FPS_MG; sp = spf(g, g["t0"] + t)
            return pop_frame(sp, card_cx(g, sp, g.get("x", W / 2)), g["y"], t, dur, ent=E, from_xy=F)
        return fn, n
    raise SystemExit(f"unknown graphic kind {k}")


def mg_frames(plan, seq, g):
    dur = g["t1"] - g["t0"]; n = int(round(dur * FPS_MG))
    k = g["kind"]
    if k == "group":                                   # graphics that overlap in time share one layer (one MG track)
        gens = {}
        for i in range(n):
            ta = g["t0"] + i / FPS_MG; fr = Image.new("RGBA", (W, H), (0, 0, 0, 0))
            for j, it in enumerate(g["items"]):
                if it["t0"] - 1e-6 <= ta < it["t1"]:
                    if j not in gens: gens[j] = mg_frames(plan, seq, it)
                    f = next(gens[j], None)
                    if f is not None: fr.alpha_composite(f)
            yield fr
        return
    if k in SEEKABLE:                                  # footage kinds: decoded once, composited per frame
        yield from SEEKABLE[k](plan, seq, g, 0, n); return
    fn, n = _frame_fn(plan, seq, g)
    for i in range(n): yield fn(i)


NEW_KINDS = {"ink_reveal", "rows_blur", "quadrant", "showcase", "ba_wipe", "ba_pair", "spotlight", "select", "cursor", "loupe", "timecode", "scrub", "hook_title", "chip"}


def build_mg(plan, seq, only=None):
    import time
    out = os.path.join(plan["_dir"], "overlays", "mg"); os.makedirs(out, exist_ok=True)
    for g in plan["graphics"]:
        if only and g["id"] not in only.split(","): continue
        mov = os.path.join(out, f"{g['id']}.mov"); t0 = time.time()
        n = int(round((g["t1"] - g["t0"]) * FPS_MG))
        if g["kind"] == "showcase":                    # one ffmpeg graph straight to ProRes (no frames through Python)
            tmp = tempfile.mkdtemp(prefix="showcase-")
            try: subprocess.run(showcase_cmd(plan, seq, g, 0, n, mov, tmp), check=True)
            finally: shutil.rmtree(tmp, ignore_errors=True)
            print(f"mg {g['id']}: {n} frames -> {mov} ({time.time() - t0:.1f} s)")
            continue
        p = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgba", "-s", f"{W}x{H}", "-r", str(FPS_MG), "-i", "-",
                              "-c:v", "prores_ks", "-profile:v", "4444", "-pix_fmt", "yuva444p10le", "-vendor", "apl0", mov], stdin=subprocess.PIPE)
        k = 0
        for fr in mg_frames(plan, seq, g):
            p.stdin.write(fr.tobytes()); k += 1
        p.stdin.close(); p.wait()
        print(f"mg {g['id']}: {k} frames -> {mov}" + (f" ({time.time() - t0:.1f} s)" if g["kind"] in NEW_KINDS else ""))


def still(plan, seq, t):
    """All overlay layers at sequence time t, composited over the simulated base (preview.render)."""
    import preview
    base = preview.render(plan, seq, t).convert("RGBA")
    for g in sorted(plan["graphics"], key=lambda g: 0 if g["kind"] == "showcase" else 1):    # the frame track sits under the MG track
        if g["t0"] <= t < g["t1"]:
            fr = None
            if g["kind"] in SEEKABLE:
                fr = next(SEEKABLE[g["kind"]](plan, seq, g, int((t - g["t0"]) * FPS_MG), 1), None)
            else:
                for i, f in enumerate(mg_frames(plan, seq, g)):
                    if i == int((t - g["t0"]) * FPS_MG): fr = f; break
            if fr: base.alpha_composite(fr)
    if plan.get("seam_line") and not G.face_at(plan, t):                                   # under the captions
        q = seam_frac(plan, t)
        base.alpha_composite(seam_line_png(plan["seam_line"].get("w", 4)) if q >= 1 else seam_line_png(plan["seam_line"].get("w", 4), q))
    cj = os.path.join(plan["_dir"], "overlays", "captions.json")
    if os.path.exists(cj):
        for c in json.load(open(cj, encoding="utf-8")):
            if c["t0"] <= t < c["t1"]: base.alpha_composite(caption_png(c["text"]))
    return base.convert("RGB")


# ---------- the plan checker (research #3 / #5 / #9 / #12) ----------
CARD_KINDS = {"stat", "checklist", "compare", "steps", "title_card"}
PANEL_KINDS = {"showcase", "ba_wipe", "ba_pair", "spotlight", "ink_reveal"}           # panel-wide by design: exempt from the safe-zone bbox


def _alpha_bbox(fr, thr=64):
    """the bbox of the frame's real pixels: alpha >= 64 (25 %), so a card's soft drop shadow is not counted as a key visual"""
    return fr.split()[3].point(lambda v: 255 if v >= thr else 0).getbbox()


def _sample_frames(plan, seq, g, fracs=(0.30, 0.55, 0.80)):
    n = int(round((g["t1"] - g["t0"]) * FPS_MG)); idx = [min(n - 1, max(0, int(n * f))) for f in fracs]
    if g["kind"] in SEEKABLE: return [(i, next(SEEKABLE[g["kind"]](plan, seq, g, i, 1))) for i in idx]
    fn, _ = _frame_fn(plan, seq, g)
    return [(i, fn(i)) for i in idx]


def check(plan, seq, out=print):
    """ERRORS: a graphic's pixels (alpha >= 25 %, 3 frames at 30 / 55 / 80 %) outside y 200..1620 (kinds showcase / ba_wipe /
    ba_pair / spotlight and g["allow_unsafe"] exempt; group items are checked one by one); two MG-track graphics at once
    (showcase sits on the frame track and may overlap them; two showcases may not overlap); a graphic under 0.6 s.
    WARNINGS: more than 1 label per 15 s; a label whose words are > 50 % the captions on screen during it; a card (stat /
    checklist / compare / steps / title_card) over 6 s without g["allow_long"]; one SFX sound over 35 % of all cues; a static
    screen view (no anim, no drift) showing > 8 s with no graphic over it. Returns (errors, warnings)."""
    errs, warns = [], []
    gs = plan["graphics"]
    for g in gs:
        if g["t1"] - g["t0"] < 0.6: errs.append(f"{g['id']}: {g['t1'] - g['t0']:.2f} s long (min 0.6 s)")
    for track, sel in (("MG", lambda g: g["kind"] != "showcase"), ("frame", lambda g: g["kind"] == "showcase")):
        last = None
        for g in sorted([g for g in gs if sel(g)], key=lambda g: g["t0"]):
            if last and g["t0"] < last["t1"] - 1e-3:
                errs.append(f"{track} track overlap: {last['id']} {last['t0']:.3f}-{last['t1']:.3f} / {g['id']} {g['t0']:.3f}-{g['t1']:.3f}")
            if not last or g["t1"] > last["t1"]: last = g
    for g in gs:
        for it in (g["items"] if g["kind"] == "group" else [g]):
            if it["kind"] in PANEL_KINDS or it.get("allow_unsafe") or g.get("allow_unsafe"): continue
            for i, fr in _sample_frames(plan, seq, it):
                bb = _alpha_bbox(fr)
                if bb and (bb[1] < 200 or bb[3] > 1620):
                    errs.append(f"{it['id']} ({it['kind']}) at {it['t0'] + i / FPS_MG:.2f} s: pixels y {bb[1]}..{bb[3]} outside the safe zone 200..1620")
                    break
    labels = sorted([it for g in gs for it in (g["items"] if g["kind"] == "group" else [g]) if it["kind"] == "label"], key=lambda g: g["t0"])
    for a, b in zip(labels, labels[1:]):
        if b["t0"] - a["t0"] < 15:
            warns.append(f"labels {a['id']} ({a['t0']:.1f} s) and {b['id']} ({b['t0']:.1f} s): {b['t0'] - a['t0']:.1f} s apart (max 1 per 15 s)")
    cj = os.path.join(plan["_dir"], "overlays", "captions.json")
    if os.path.exists(cj):
        caps = json.load(open(cj, encoding="utf-8"))
        wd = lambda s_: {x for x in (clean(w).lower().strip("!?\"'()") for w in s_.replace("*", " ").split()) if x}
        for lb in labels:
            cw_ = set().union(*[wd(c["text"]) for c in caps if c["t0"] < lb["t1"] and c["t1"] > lb["t0"]] or [set()])
            lw = wd(lb["text"])
            if lw and len(lw & cw_) / len(lw) > 0.5:
                warns.append(f"label {lb['id']} \"{lb['text']}\" repeats the captions on screen ({len(lw & cw_)}/{len(lw)} words)")
    else:
        warns.append("no overlays/captions.json: the label / caption overlap is not checked (run --captions first)")
    for g in gs:
        if g["kind"] in CARD_KINDS and g["t1"] - g["t0"] > 6 and not g.get("allow_long"):
            warns.append(f"card {g['id']} ({g['kind']}) holds {g['t1'] - g['t0']:.1f} s (max 6 s without allow_long)")
    cues = [x for g in gs for _, x in graphic_cues(g)]
    if cues:
        from collections import Counter
        top, c = Counter(cues).most_common(1)[0]
        if c / len(cues) > 0.35: warns.append(f"SFX: {top} is {c} of {len(cues)} cues ({c / len(cues) * 100:.0f} %, max 35 %)")
    cover = sorted((g["t0"], g["t1"]) for g in gs)
    faces = [(f["t0"], f["t1"]) for f in plan["face"]]
    for v in plan["views"]:
        if "anim" in v or v.get("drift"): continue
        segs = [(v["t0"], v["t1"])]
        for a, b in faces + cover:                    # what is left of the hold: split screen, nothing over it
            nxt = []
            for x, y in segs:
                if b <= x or a >= y: nxt.append((x, y)); continue
                if a > x: nxt.append((x, a))
                if b < y: nxt.append((b, y))
            segs = nxt
        for x, y in segs:
            if y - x > 8: warns.append(f"static view '{v['view']}' {x:.1f}-{y:.1f} s ({y - x:.1f} s) with no move and no graphic")
    for e in errs: out(f"  ERROR    {e}")
    for w_ in warns: out(f"  WARNING  {w_}")
    out(f"check {plan.get('job', '')}: {len(errs)} error(s), {len(warns)} warning(s)")
    return errs, warns


if __name__ == "__main__":
    a = sys.argv[1:]
    plan, seq = load(a[0])
    if "--captions" in a: build_captions(plan)
    if "--mg" in a: build_mg(plan, seq, a[a.index("--only") + 1] if "--only" in a else None)
    if "--check" in a:
        e_, _ = check(plan, seq)
        if e_: sys.exit(1)
    if "--still" in a:
        ts = [float(x) for x in a[a.index("--still") + 1:] if not x.startswith("--")]
        ims = [still(plan, seq, t) for t in ts]
        w, h = 432, 768
        sheet = Image.new("RGB", (w * min(5, len(ims)), h * ((len(ims) + 4) // 5)))
        for i, im in enumerate(ims): sheet.paste(im.resize((w, h), Image.LANCZOS), ((i % 5) * w, (i // 5) * h))
        os.makedirs(os.path.join(plan["_dir"], "work"), exist_ok=True)
        p = os.path.join(plan["_dir"], "work", "stills.jpg"); sheet.save(p, quality=88); print(p)
