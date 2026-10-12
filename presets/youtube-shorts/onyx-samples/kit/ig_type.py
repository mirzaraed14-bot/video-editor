"""ig_type.py: the v2 look's TYPE metrics, shared by ig_v2.py (lays the captions out) and ig_capy.py (needs each block's height).

Why in Python and not in the browser: the v2 caption block is anchored at ONE constant top for the whole video (Affan, 2026-10-07)
and must stay inside the letterbox window, so its height has to be known before the composition is written. Measuring in the page
is unreliable (the Rich Roll `rules` card: a font that is not loaded yet measures with the fallback face), so every line is broken
here with the real font files (PIL) and written into the HTML with an explicit line height. A block's height is then exact.

  layout_stack(words, cap)   -> {"lines": [{"role", "words": [i, ...], "size", "lh", "w"}], "h": px}
  cap_height(chunk, cap)     -> the px height of one caption chunk in its mode (stack / word / line)
"""
import os
from PIL import ImageFont

KIT = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(KIT, "..", "..", "..", ".."))
A, K = os.path.join(REPO, "assets", "fonts"), os.path.join(KIT, "fonts")
# key -> (file, variable-font weight or None, CSS family, CSS weight, CSS style). The CSS side lives in ig_v2.FONT_CSS.
FACES = {
    "inter-400": (os.path.join(A, "Inter-Regular.otf"), None),
    "inter-700": (os.path.join(A, "Inter-Bold.otf"), None),
    "inter-900": (os.path.join(A, "Inter-Black.otf"), None),
    "serif-it": (os.path.join(K, "Cormorant-Italic-VariableFont_wght.ttf"), 600),    # the DOAC / Stealth Motion hero word
    "play-it": (os.path.join(A, "PlayfairDisplay-Italic-VF.ttf"), 800),             # the Mark Brazil neon number
    "mono-400": (os.path.join(K, "IBMPlexMono-Regular.ttf"), None),
    "mono-500": (os.path.join(K, "IBMPlexMono-Medium.ttf"), None),
    "mono-600": (os.path.join(K, "IBMPlexMono-SemiBold.ttf"), None),
    "wide-700": (os.path.join(K, "Unbounded-VariableFont_wght.ttf"), 700),          # the Valueclippss wide caps, title-card names
}
_cache = {}

# The v2 letterbox window (research § d): measured on Stealth Motion's 512K reel (picture 1044 x 899 at x 22, bars 507 / 514, corner
# radius 64-80), rounded to an even 900 and centred: bars 510 / 510, which keeps the whole window inside the repo's 200 -> 1620 band.
FRAME = dict(x=18, y=510, w=1044, h=900, radius=64)


def frame(spec):
    """The window of a v2 spec (spec.frame overrides any key; e.g. the 4:3 square-cornered variant {"x": 0, "y": 555, "w": 1080,
    "h": 810, "radius": 0}, Valueclippss)."""
    return {**FRAME, **{k: v for k, v in spec.get("frame", {}).items() if k in FRAME}}


def font(key, size):
    k = (key, int(round(size)))
    if k not in _cache:
        path, wght = FACES[key]
        f = ImageFont.truetype(path, k[1])
        if wght is not None:
            f.set_variation_by_axes([wght])
        _cache[k] = f
    return _cache[k]


def width(text, key, size, track=0.0):
    """Advance width in px (track = letter-spacing in em, as the CSS sets it)."""
    return font(key, size).getlength(text) + track * size * len(text)


# The stack mode's defaults (research move 4, sizes estimated from DOAC crops 02-04 and Stealth Motion 13-14).
STACK = dict(lead_size=54, lead_face="inter-700", hero_size=124, hero_face="serif-it", max_w=860, lead_lh=1.14, hero_lh=1.0, gap=4)


def stack_cfg(cap):
    c = dict(STACK)
    if cap.get("hero") == "black":                 # DOAC's heavy caps hero instead of the serif-italic word
        c.update(hero_size=96, hero_face="inter-900")
    for k in ("lead_size", "hero_size", "max_w"):
        if k in cap:
            c[k] = cap[k]
    return c


def show_word(w, cap, role):
    """The text a word shows: the hero in caps when the hero face is the black one, otherwise as spoken."""
    return w.upper() if (role == "hero" and cap.get("hero") == "black") or cap.get("case") == "upper" else (w.lower() if cap.get("case") == "lower" else w)


def layout_stack(words, cap):
    """words: [[t0, t1, text, role], ...] (role lead | hero). The hero word gets a line of its own (the typographic stack: small lead-in,
    big hero, small tail, as DOAC's "I AM ONE OF / THE MOST" and Mark Brazil's "where my business went from / $7 million / in revenue");
    the other words wrap greedily at the lead size inside max_w. A hero wider than max_w shrinks to fit."""
    c = stack_cfg(cap)
    lines, cur, cur_w = [], [], 0.0
    sp = width(" ", c["lead_face"], c["lead_size"])

    def flush():
        nonlocal cur, cur_w
        if cur:
            lines.append(dict(role="lead", words=cur, size=c["lead_size"], lh=int(round(c["lead_size"] * c["lead_lh"])), w=round(cur_w, 1)))
        cur, cur_w = [], 0.0

    for i, (_, _, text, role) in enumerate(words):
        t = show_word(text, cap, role)
        if role == "hero":
            flush()
            size = c["hero_size"]
            hw = width(t, c["hero_face"], size)
            if hw > c["max_w"]:
                size = int(size * c["max_w"] / hw); hw = width(t, c["hero_face"], size)
            lines.append(dict(role="hero", words=[i], size=size, lh=int(round(size * c["hero_lh"])), w=round(hw, 1)))
            continue
        ww = width(t, c["lead_face"], c["lead_size"])
        if cur and cur_w + sp + ww > c["max_w"] * 0.97:       # 3 % margin: PIL and Chrome kern a hair differently
            flush()
        cur_w = cur_w + (sp if cur else 0) + ww
        cur.append(i)
    flush()
    return dict(lines=lines, h=sum(l["lh"] for l in lines) + c["gap"] * max(0, len(lines) - 1))


WORD = {"mono": dict(face="mono-600", size=44, track=0.04, pad=(8, 16), lh=1.15),       # YC: mono caps on a translucent box
        "wide": dict(face="wide-700", size=62, track=0.05, pad=(0, 0), lh=1.15)}        # Valueclippss: wide geometric caps
LINE = dict(face="inter-700", size=58, lh=1.2, mask_pad=10)


def cap_height(chunk, cap):
    mode = cap.get("mode")
    if mode == "stack":
        return layout_stack(chunk["words"], cap)["h"]
    if mode == "word":
        w = WORD[cap.get("variant", "mono")]
        return int(round(cap.get("size", w["size"]) * w["lh"])) + 2 * w["pad"][0]
    return int(round(cap.get("size", LINE["size"]) * LINE["lh"])) + 2 * LINE["mask_pad"]
