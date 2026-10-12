"""ig_v2.py: the v2 look's OVERLAY ("look": "v2", batch 2, 2026-10-12): animated captions + the refined graphic vocabulary, as a
transparent HyperFrames composition -> <job>/ig/hf-overlay/index.html, <job>/ig/work/sfx-cues.json, <job>/ig/work/v2-events.json.
Called by ig_overlay.py when the spec says "look": "v2" (ig_build runs it; nothing here touches a v1 job).

Affan, 2026-10-12: "minimalistic… a LOT of motion graphics: minimalist, high quality, premium, refined… clean crisp sound effects; it
should look like an expensive video." Every number below is the research's (references/batch2-style-research.md § b), measured on
the reference reels' frames; the motion language is ONE family: type and cards rise / blur in with power3.out (0.12-0.45 s), objects
settle from 1.06-1.18 to 1.00 with NO overshoot (type never pops), lines draw on with power2.inOut, exits are 0.14-0.25 s fades with
a small rise, slides carry a directional motion blur. Glow lives on accent type and lines only; no paper, no drop shadows on type.

Coordinates: canvas px (1080 x 1920). A card's "y" is its top in canvas px; "wy" is its top INSIDE the window (frame.y + wy); "x" its
left (default: the window's left + 60). The window is ig_type.frame(spec) (1044 x 900 at x 18, y 510, radius 64).

CAPTIONS ("captions.mode", ONE per video; words land on their spoken word, the block anchor never moves: ig_capy places it)
  stack  word-by-word typographic stack (DOAC, Stealth Motion, Mark Brazil): lead words 54 px Inter Bold, ONE hero word per block on
         its own line, 124 px Cormorant Italic in the accent with a glow ("hero": "black" = 96 px Inter Black caps). Per word:
         opacity 0 -> 1, x +24 -> 0, blur 6 -> 0, scale 1.04 -> 1, 0.12 s power3.out (hero 0.18 s); the block leaves together
         (opacity -> 0, y -> -16, 0.14 s power2.in, done before the next block's first word). "align": "center" (default) | "left".
  word   one word at a time (YC, Valueclippss): "variant": "mono" (44 px IBM Plex Mono caps on a translucent box; hl = accent box) |
         "wide" (62 px Unbounded caps, a white -> cream gradient; hl = accent fill). In over 2 frames, scale 1.06 -> 1 in 0.10 s.
  line   2-4 word chunks rise 40 px out of a mask (0.32 s power3.out); each hl word's accent colour SWEEPS in left -> right on its own
         word (clip-path, 0.22 s power2.inOut); out in a 0.14 s fade.
  "cx": the x the block centres on (the mouth, when the speaker sits on a third). "case": "lower" | "upper" (default as spoken).
  All: captext.clean (only ! ? and quotes, Affan's rule), white base + coloured emphasis, "colors": {"word": "#hex"} for meaning
  (research: green #3DDC84 gain, red #FF4D4D loss), "accent" = the show's colour.
TOP / BOTTOM BAR
  "hook": {"t0", "t1" (<= 3 s), "lines": [...], "hl": [words], "kicker": "SHOW NAME", "y": centre px}   the hook title in the top
         bar (centred ~ y 365, inside the safe band): kicker blurs in, lines rise out of a mask, the hl word in the serif accent.
  "credit": "Rich Roll Podcast · Bryan Johnson", "credit_t0": s, "credit_y": px (default window bottom + 90 = 1500)   28 px mono,
         55 % white, a short accent dash; blurs in and holds (replaces the v1 grey pill: research § c 6).
CARDS ("cards": [{"kind", "t0", "t1", ...}]; each gets its SFX automatically, "sfx": false mutes it, "rel_db" shifts it)
  neon      {"lead", "value", "value2", "t2", "tail", "tv", "size": 150, "w", "align"}  a giant serif-italic number / phrase in the accent
            with a bloom between a small lead and tail line (Mark Brazil "$7 million" -> "$95 million"); its characters rise in at tv
            (default t0 + 0.25 + the lead's stagger), and RE-ROLL to value2 at t2 (0.45 s power2.inOut, character stagger);
            "lead2" / "tail2" swap the small lines with the re-roll ("bedtime 10 pm" -> "last food 6 pm").
  lower3    {"name", "role", "bar_h": 120}   the mono lower-third: a 6 px accent bar with a glow draws down (0.25 s power2.out), the
            name wipes in left -> right (0.35 s), the role 0.1 s later; exit 0.2 s (Mark Brazil, YC).
  reticle   {"box": [x, y, w, h] canvas px, "label", "label_pos": "top", "cross": true}   HUD: four corner brackets settle 1.18 ->
            1.00 (0.20 s power3.out), thin crosshair lines run from the box to the window edges, a mono label types in under (or
            over) it (YC). Measure the box on a frame of ig/work/picture.mp4.
  route     {"nodes": [[t, "LABEL", "sub"], ...], "title", "orient": "h" | "v", "step": 84, "pulses": [t], "src" (optional map
            still), "w", "h", "panel": true}   "v" = a compact timeline beside the head whose panel GROWS node by node; a /
            route: a thin line draws from node to node as each is SAID (0.55 s power2.inOut, landing on the node's time), each node
            settles with one pulse ring ("pulses" re-ring the newest node: a beat while the speaker elaborates); with "src" the panel
            is a darkened map drifting 4 % with grid lines (YC's map).
  widget    {"layout": "todo" | "list" | "progress" | "notify", "title", "meta", "items": [[t, "text", "sub"], ...], "values":
            [[t, pct], ...], "label", "sub", "app", "body", "cursor": true, "strike": true, "stamp": [t, "TEXT"], "w": 820}   an
            iOS-widget card in dark glass with an
            accent glow (vitalyframes): todo items tick at t (a cursor glides there and taps, the box fills, a hand-drawn strike
            draws through the text); list rows build one per beat and the card GROWS with them (never an empty box); progress fills a
            ring and counts; notify slides down with a vertical motion blur. "strike": false keeps the tick without the strike (a
            tick that means "logged", not "done"); "stamp" closes a todo / list with a mono accent line and a thud.
  wordscene {"words": [[t, "word"], ...], "hero": index, "bleed": false, "wy": px}   a full-window black scene, one lowercase word per beat
            (rise 24 px in 0.12 s), the hero word 1.6x in the serif accent (yp.motionstudio). "bleed": true opens the black to the
            full frame first (0.55 s power3.inOut) and closes it again.
  titlecard {"name", "role", "kicker", "pos": "top" | "bottom"}   a cinematic guest card over the RACKED picture (ig_window blurs + dims the window under
            it): the NAME in wide caps with an RGB split that settles to 0 (0.30 s), a slow push 1.00 -> 1.04 (DOAC).
  compare   {"left": {"label", "value", "sub"}, "right": {...}, "t_right", "win": "left" | "right", "t_win", "orient": "v"}   two glass columns
            ("v": stacked, for the space beside the head), a
            divider that draws, the right column at t_right, the winner lights in the accent at t_win and the loser dims with a strike.
  leak      {"t", "side": "right" | "left" | "top"}   a warm light leak on a SCENE change, drawn by ig_window (screen blend); here only
            its sound (whoosh + a soft flash).
  any card: "rack": true asks ig_window to blur + dim the picture under it ("rack_blur", "rack_dim").
SPLIT shots get a glowing seam over the picture's white line (Affan: every split has a white line) and a soft whoosh.
DENSITY: v2-events.json lists every designed event; the report prints events per 10 s (target 3-4, research move 16), the
full-window share (<= 25 %), the face between full-window scenes (>= 1.5 s), cards held > 6 s with no new beat, and full-window edges
within 3 frames of a cut that do not land ON it (Affan 2026-10-09: no stray frames).
"""
import json, math, os, shutil, sys

KIT = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(KIT, "..", "..", "..", ".."))
sys.path.insert(0, KIT)
import ig_type                           # noqa: E402
from captext import clean                # noqa: E402  (Affan, 2026-10-07: only ! ? and quotation marks)

W, H = 1080, 1920
FULL = {"wordscene", "titlecard"}        # cards that cover the whole window (they count against the 25 % budget)


def esc(t):
    return str(t).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def hexa(col, a):
    """#RRGGBB + alpha (0..1) -> #RRGGBBAA."""
    return f"{col}{int(round(a * 255)):02X}"


def cap_word(w):
    return clean(w).replace("'", "’")


def build(job, spec):
    fps, dur = spec["fps"], spec["frames"] / spec["fps"]
    q = lambda t: round(max(0.0, round(t * fps) - 0.25) / fps, 5)          # a quarter frame before the frame boundary (as v1)
    FR = ig_type.frame(spec)
    cap = spec.get("captions", {})
    ACC = cap.get("accent", spec.get("accent", "#F5C451"))
    colors = {k.lower(): v for k, v in cap.get("colors", {}).items()}
    out = os.path.join(job, "ig", "hf-overlay")
    for d in ("fonts", "vendor", "assets"):
        os.makedirs(os.path.join(out, d), exist_ok=True)
    for fn in ("Inter-Regular.otf", "Inter-Bold.otf", "Inter-Black.otf", "PlayfairDisplay-Italic-VF.ttf"):
        shutil.copy(os.path.join(REPO, "assets", "fonts", fn), os.path.join(out, "fonts", fn))
    for fn in os.listdir(os.path.join(KIT, "fonts")):
        shutil.copy(os.path.join(KIT, "fonts", fn), os.path.join(out, "fonts", fn))
    shutil.copy(os.path.join(REPO, "presets", "youtube-shorts", "onyx-samples-youtube", "kit", "vendor", "gsap.min.js"), os.path.join(out, "vendor", "gsap.min.js"))

    html, caph, js, sfx, ev = [], [], [], [], []  # caph: the captions (drawn last, over the cards); ev: (t, label, card index) designed events

    def cue(t, kind, k=None, rel=0.0):
        if k is not None and k.get("sfx") is False:
            return
        c = dict(t=round(max(0.0, t), 3), kind=kind)
        r = rel + (k.get("rel_db", 0.0) if k else 0.0)
        if r:
            c["rel_db"] = r
        sfx.append(c)

    def rise_in(sel, t, d=0.35, y=24, blur=8, stagger=0.0, ease="power3.out"):
        st = f", stagger: {stagger}" if stagger else ""
        return (f'tl.fromTo("{sel}", {{opacity: 0, y: {y}, filter: "blur({blur}px)"}}, {{opacity: 1, y: 0, filter: "blur(0px)", duration: {d}, '
                f'ease: "{ease}"{st}}}, {q(t)});')

    def out_fade(sel, t1, d=0.2, y=-14):
        return f'tl.to("{sel}", {{opacity: 0, y: {y}, filter: "blur(6px)", duration: {d}, ease: "power2.in"}}, {q(t1 - d - 0.02)});'

    def show(cid, t0, t1):
        return f'tl.set("#{cid}", {{autoAlpha: 1}}, {q(t0)}); tl.set("#{cid}", {{autoAlpha: 0}}, {q(t1)});'

    def mblur(fid, dx, dy, t, d, ease="power3.out"):
        """A directional motion blur that eases out with the slide (an SVG blur on the element, tweened through a proxy)."""
        return (f'(function () {{ const g = document.getElementById("{fid}g"), o = {{v: 1}}; tl.fromTo(o, {{v: 1}}, {{v: 0, duration: {d}, ease: "{ease}", '
                f'onUpdate: () => g.setAttribute("stdDeviation", (o.v * {dx}).toFixed(2) + " " + (o.v * {dy}).toFixed(2))}}, {q(t)}); '
                f'tl.set("[data-mb={fid}]", {{filter: "none"}}, {q(t + d + 0.02)}); }})();')

    def pulse(sel, origin, t, scale):
        """One expanding ring: in from invisible (so a seek back before t shows nothing), then out as it grows."""
        return (f'tl.fromTo("{sel}", {{opacity: 0, scale: 1, svgOrigin: "{origin}"}}, {{opacity: 0.75, scale: 1.08, svgOrigin: "{origin}", duration: 0.06, ease: "none"}}, {q(t)}); '
                f'tl.fromTo("{sel}", {{opacity: 0.75, scale: 1.08, svgOrigin: "{origin}"}}, {{opacity: 0, scale: {scale}, svgOrigin: "{origin}", duration: 0.95, ease: "power1.out", '
                f'immediateRender: false}}, {q(t + 0.06)}); ')

    def mbdef(fid):
        return (f'<svg width="0" height="0" style="position:absolute"><filter id="{fid}" x="-30%" y="-30%" width="160%" height="160%">'
                f'<feGaussianBlur id="{fid}g" stdDeviation="0 0"/></filter></svg>')

    def xy(k, w_default):
        x = k.get("x", FR["x"] + 60)
        y = k["y"] if "y" in k else FR["y"] + k.get("wy", 60)
        return x, y, k.get("w", w_default)

    # ------------------------------------------------------------------ captions
    mode = cap.get("mode", "stack")
    chunks = cap.get("chunks", [])
    for i, c in enumerate(chunks):
        cid, y = f"c{i}", int(c.get("y", FR["y"] + FR["h"] * 0.55))
        words = [[w[0], w[1], cap_word(w[2]), w[3]] for w in c.get("words", [])]
        words = [w for w in words if w[2]]
        if not words:
            continue
        col = lambda w: colors.get(w.strip("!?\"“”‘’").lower())
        if mode == "stack":
            lay = ig_type.layout_stack(words, cap)
            cfg = ig_type.stack_cfg(cap)
            # every line is placed in px (its width is measured): centred on captions.cx (default the window's centre; set it to the
            # mouth's x when the framing puts the speaker on a third), never closer than 40 px to the window's side edges
            cxl = cap.get("cx", FR["x"] + FR["w"] / 2)
            left, inner = FR["x"] + 40, FR["w"] - 80
            lines = []
            for li, L in enumerate(lay["lines"]):
                xl = FR["x"] + 72 if cap.get("align") == "left" else min(max(cxl - L["w"] / 2, left), left + inner - L["w"])
                spans = []
                for j in L["words"]:
                    t = ig_type.show_word(words[j][2], cap, words[j][3])
                    cw = col(words[j][2])
                    st = (f' style="color:{cw};text-shadow:0 0 18px {hexa(cw, 0.6)}, 0 0 4px {cw}"' if words[j][3] == "hero" else f' style="color:{cw}"') if cw else ""
                    spans.append(f'<span class="w" id="{cid}w{j}"{st}>{esc(t)}</span>')
                mt = (f"margin-top:{cfg['gap']}px;" if li else "") + f"padding-left:{max(0, xl - left):.0f}px;"
                lines.append(f'<div class="sl {L["role"]}{" black" if cap.get("hero") == "black" and L["role"] == "hero" else ""}" '
                             f'style="{mt}height:{L["lh"]}px;line-height:{L["lh"]}px;font-size:{L["size"]}px">{" ".join(spans)}</div>')
            caph.append(f'<div id="{cid}" class="cap2 stack" style="top:{y}px;left:{left:.0f}px;width:{inner}px;text-align:left">{"".join(lines)}</div>')
            js.append(f'tl.set("#{cid}", {{autoAlpha: 1}}, {q(c["start"])});')
            for j, w in enumerate(words):
                hero = w[3] == "hero"
                js.append(f'tl.fromTo("#{cid}w{j}", {{opacity: 0, x: {0 if hero else 24}, y: {14 if hero else 0}, filter: "blur(6px)", scale: 1.04}}, '
                          f'{{opacity: 1, x: 0, y: 0, filter: "blur(0px)", scale: 1, duration: {0.18 if hero else 0.12}, ease: "power3.out"}}, {q(max(c["start"], w[0] - 0.03))});')
            js.append(f'tl.to("#{cid}", {{opacity: 0, y: -16, duration: 0.14, ease: "power2.in"}}, {q(max(c["start"] + 0.2, c["end"] - 0.15))}); '
                      f'tl.set("#{cid}", {{autoAlpha: 0}}, {q(c["end"])});')
        elif mode == "word":
            var = cap.get("variant", "mono")
            spans = []
            for w in words:
                st = f' style="--hc:{col(w[2])}"' if col(w[2]) else ""
                spans.append(f'<span class="wd{" hl" if w[3] == "hero" or col(w[2]) else ""}"{st}>{esc(w[2].upper())}</span>')
            caph.append(f'<div id="{cid}" class="cap2 word {var}" style="top:{y}px;left:{cap.get("cx", FR["x"] + FR["w"] / 2) - FR["w"] / 2:.0f}px;width:{FR["w"]}px">'
                        f'<span class="wdw">{" ".join(spans)}</span></div>')
            js.append(f'tl.set("#{cid}", {{autoAlpha: 1}}, {q(c["start"])}); '
                      f'tl.fromTo("#{cid}", {{opacity: 0}}, {{opacity: 1, duration: {2 / 60:.4f}, ease: "none"}}, {q(c["start"])}); '
                      f'tl.fromTo("#{cid} .wdw", {{scale: 1.06}}, {{scale: 1, duration: 0.10, ease: "power2.out"}}, {q(c["start"])}); '
                      f'tl.set("#{cid}", {{autoAlpha: 0}}, {q(c["end"])});')
        else:                                                  # line
            spans = []
            for j, w in enumerate(words):
                if w[3] == "hero" or col(w[2]):
                    hc = col(w[2]) or ACC
                    spans.append(f'<span class="w sweep"><span class="base">{esc(w[2])}</span><span class="sw" id="{cid}s{j}" style="color:{hc};'
                                 f'text-shadow:0 0 16px {hexa(hc, 0.55)}">{esc(w[2])}</span></span>')
                    js.append(f'tl.fromTo("#{cid}s{j}", {{clipPath: "inset(0% 100% 0% 0%)"}}, {{clipPath: "inset(0% 0% 0% 0%)", duration: 0.22, '
                              f'ease: "power2.inOut"}}, {q(max(c["start"], w[0] - 0.02))});')
                else:
                    spans.append(f'<span class="w">{esc(w[2])}</span>')
            caph.append(f'<div id="{cid}" class="cap2 line" style="top:{y}px;left:{cap.get("cx", FR["x"] + FR["w"] / 2) - FR["w"] / 2:.0f}px;width:{FR["w"]}px"><div class="lmask"><div class="lin">'
                        f'{" ".join(spans)}</div></div></div>')
            js.append(f'tl.set("#{cid}", {{autoAlpha: 1}}, {q(c["start"])}); '
                      f'tl.fromTo("#{cid} .lin", {{y: 40}}, {{y: 0, duration: 0.32, ease: "power3.out"}}, {q(c["start"])}); '
                      f'tl.to("#{cid}", {{opacity: 0, duration: 0.14, ease: "power1.in"}}, {q(max(c["start"] + 0.2, c["end"] - 0.14))}); '
                      f'tl.set("#{cid}", {{autoAlpha: 0}}, {q(c["end"])});')

    # ------------------------------------------------------------------ the top bar (hook) and the bottom bar (credit)
    hk = spec.get("hook")
    if hk:
        hl = {h.lower() for h in hk.get("hl", [])}
        n_l = len(hk["lines"]); hgt = (44 if hk.get("kicker") else 0) + n_l * 80
        top = int(hk.get("y", (200 + FR["y"]) / 2 + 10) - hgt / 2)
        lines = []
        for li, line in enumerate(hk["lines"]):
            ws = [f'<span class="hhl">{esc(w)}</span>' if w.strip("!?\"").lower() in hl else esc(w) for w in line.split(" ")]
            lines.append(f'<div class="hmask"><div class="hline">{" ".join(ws)}</div></div>')
        kick = f'<div class="hkick">{esc(hk["kicker"])}</div>' if hk.get("kicker") else ""
        html.append(f'<div id="hook" class="v2c hook" style="top:{top}px">{kick}{"".join(lines)}</div>')
        t0, t1 = hk.get("t0", 0.1), hk.get("t1", 2.9)
        js.append(show("hook", t0, t1))
        if kick:
            js.append(rise_in("#hook .hkick", t0, d=0.45, y=10, blur=6))
        js.append(f'tl.fromTo("#hook .hline", {{yPercent: 105, filter: "blur(8px)"}}, {{yPercent: 0, filter: "blur(0px)", duration: 0.5, ease: "power3.out", stagger: 0.08}}, {q(t0 + 0.06)});')
        js.append(out_fade("#hook", t1, d=0.28, y=-18))
        cue(t0 + 0.06, "whoosh-soft"); cue(t0 + 0.3, "thud")
        ev.append((t0, "hook", None))
    credit = spec.get("credit")
    if credit:
        cy = spec.get("credit_y", FR["y"] + FR["h"] + 90)
        html.append(f'<div id="credit2" class="v2c credit2" style="top:{cy}px"><span class="cdash"></span>{esc(credit)}</div>')
        ct0 = spec.get("credit_t0", 0.0)
        js.append(f'tl.set("#credit2", {{autoAlpha: 1}}, {q(ct0)});' + rise_in("#credit2", ct0, d=0.5, y=8, blur=6))

    # ------------------------------------------------------------------ the split seams (Affan: every split has a white line)
    for s in spec.get("shots", []):
        if s["kind"] == "SPLIT" and spec.get("split", {}).get("line", True) is not None:
            seam = spec.get("split", {}).get("seam", FR["h"] // 2)
            cid = f"seam{s['id']}"
            html.append(f'<div id="{cid}" class="v2c seam" style="left:{FR["x"]}px;top:{FR["y"] + seam - 2}px;width:{FR["w"]}px"></div>')
            t0, t1 = s["f0"] / fps, s["f1"] / fps
            js.append(show(cid, t0, t1) + f'tl.fromTo("#{cid}", {{opacity: 0}}, {{opacity: 1, duration: 0.2, ease: "power1.out"}}, {q(t0)});')
            cue(t0 - 0.02, "whoosh-soft"); ev.append((t0, "split", None))

    # ------------------------------------------------------------------ cards
    for i, k in enumerate(spec.get("cards", [])):
        kind, cid = k["kind"], f"k{i}"
        t0, t1 = k.get("t0", k.get("t", 0)), k.get("t1", k.get("t", 0))
        if kind == "leak":
            cue(k["t"], "flash", k); cue(k["t"], "rise-air", k)
            ev.append((k["t"], "leak", i))
            continue
        if kind == "neon":
            x, y, w = xy(k, FR["w"] - 120)
            al = k.get("align", "left")
            size = k.get("size", 150)
            vals = [k["value"]] + ([k["value2"]] if k.get("value2") else [])
            wmax = max(ig_type.width(v, "play-it", size) for v in vals)
            if wmax > w * 0.98:
                size = int(size * w * 0.98 / wmax)
            chars = lambda v, cls: f'<span class="nv {cls}">' + "".join(f'<span class="ch">{"&nbsp;" if ch == " " else esc(ch)}</span>' for ch in v) + "</span>"
            ws_ = lambda key, cls: (f'<span class="{cls}">' + " ".join(f'<span class="nw">{esc(t)}</span>' for t in k[key].split()) + "</span>") if k.get(key) else ""
            # "lead2" / "tail2": the small lines change WITH the re-roll ("bedtime 10 pm" -> "last food 6 pm"), in the same grid cell
            lead, tail = ws_("lead", "n1") + ws_("lead2", "n2"), ws_("tail", "n1") + ws_("tail2", "n2")
            jst = "center" if al == "center" else "start"
            html.append(f'<div id="{cid}" class="v2c neon" style="left:{x}px;top:{y}px;width:{w}px;text-align:{al}">'
                        + (f'<div class="nlead" style="justify-items:{jst}">{lead}</div>' if lead else "")
                        + f'<div class="nval" style="justify-items:{"center" if al == "center" else "start"};font-size:{size}px">{chars(vals[0], "a")}'
                        + (chars(vals[1], "b") if len(vals) > 1 else "") + "</div>"
                        + (f'<div class="ntail" style="justify-items:{jst}">{tail}</div>' if tail else "") + "</div>")
            nlead = len(k.get("lead", "").split())
            tv = k.get("tv", t0 + 0.12 + 0.07 * nlead)
            js.append(show(cid, t0, t1))
            if lead:
                js.append(rise_in(f"#{cid} .nlead .n1 .nw", t0, d=0.3, y=16, blur=6, stagger=0.07))
            js.append(f'tl.fromTo("#{cid} .nv.a .ch", {{opacity: 0, yPercent: 40, filter: "blur(10px)"}}, {{opacity: 1, yPercent: 0, filter: "blur(0px)", '
                      f'duration: 0.45, ease: "power3.out", stagger: 0.03}}, {q(tv)});')
            if tail:
                js.append(rise_in(f"#{cid} .ntail .n1 .nw", tv + 0.3, d=0.3, y=16, blur=6, stagger=0.06))
            cue(tv + 0.12, "impact", k); ev.append((tv + 0.12, "neon", i))   # the event is the value landing
            if len(vals) > 1:
                t2 = k["t2"]
                js.append(f'tl.to("#{cid} .nv.a .ch", {{opacity: 0, yPercent: -55, filter: "blur(8px)", duration: 0.45, ease: "power2.inOut", stagger: 0.025}}, {q(t2 - 0.08)}); '
                          f'tl.fromTo("#{cid} .nv.b .ch", {{opacity: 0, yPercent: 55, filter: "blur(8px)"}}, {{opacity: 1, yPercent: 0, filter: "blur(0px)", '
                          f'duration: 0.45, ease: "power2.inOut", stagger: 0.025}}, {q(t2)});')
                for part in ("nlead", "ntail"):
                    if k.get(part.replace("n", "", 1) + "2"):
                        js.append(f'tl.to("#{cid} .{part} .n1 .nw", {{opacity: 0, y: -12, filter: "blur(6px)", duration: 0.25, ease: "power2.in", stagger: 0.03}}, {q(t2 - 0.12)}); '
                                  + rise_in(f"#{cid} .{part} .n2 .nw", t2 + 0.1, d=0.3, y=16, blur=6, stagger=0.06))
                cue(t2, "rise-air", k); cue(t2 + 0.32, "thud", k); ev.append((t2, "neon re-roll", i))
            js.append(out_fade(f"#{cid}", t1, d=0.22))
        elif kind == "lower3":
            x, y, _ = xy(k, 0)
            bh = k.get("bar_h", 120)
            html.append(f'<div id="{cid}" class="v2c l3" style="left:{x}px;top:{y}px"><div class="l3s"></div><div class="l3bar" style="height:{bh}px"></div>'
                        f'<div class="l3t"><div class="l3n">{esc(k["name"])}</div><div class="l3r">{esc(k.get("role", ""))}</div></div></div>')
            js.append(show(cid, t0, t1)
                      + f'tl.fromTo("#{cid} .l3bar", {{scaleY: 0, transformOrigin: "50% 0%"}}, {{scaleY: 1, duration: 0.25, ease: "power2.out"}}, {q(t0)}); '
                      f'tl.fromTo("#{cid} .l3n", {{clipPath: "inset(-20% 100% -20% 0%)"}}, {{clipPath: "inset(-20% 0% -20% 0%)", duration: 0.35, ease: "none"}}, {q(t0 + 0.2)}); '
                      f'tl.fromTo("#{cid} .l3r", {{clipPath: "inset(-20% 100% -20% 0%)"}}, {{clipPath: "inset(-20% 0% -20% 0%)", duration: 0.3, ease: "none"}}, {q(t0 + 0.3)}); '
                      + f'tl.fromTo("#{cid} .l3s", {{opacity: 0}}, {{opacity: 1, duration: 0.3, ease: "power1.out"}}, {q(t0)}); '
                      + out_fade(f"#{cid} .l3t, #{cid} .l3s", t1, d=0.2, y=0)
                      + f'tl.to("#{cid} .l3bar", {{scaleY: 0, transformOrigin: "50% 100%", duration: 0.2, ease: "power2.in"}}, {q(t1 - 0.22)});')
            cue(t0, "glass", k); cue(t0 + 0.2, "whoosh-soft", k); ev.append((t0, "lower3", i))
        elif kind == "reticle":
            bx, by, bw, bhh = k["box"]
            arm, pad = k.get("arm", 28), 6
            col = k.get("color", "#FFFFFF")
            p = lambda x0, y0, dx, dy: f'<path d="M{x0 + dx * arm} {y0} L{x0} {y0} L{x0} {y0 + dy * arm}" />'
            sw = bw + 2 * pad; shh = bhh + 2 * pad
            br = (p(1.5, 1.5, 1, 1) + p(sw - 1.5, 1.5, -1, 1) + p(1.5, shh - 1.5, 1, -1) + p(sw - 1.5, shh - 1.5, -1, -1))
            lab = (f'<div class="retlab{" top" if k.get("label_pos") == "top" else ""}" id="{cid}l" data-text="{esc(k["label"])}"></div>') if k.get("label") else ""
            html.append(f'<div id="{cid}" class="v2c ret" style="left:{bx - pad}px;top:{by - pad}px;width:{sw}px;height:{shh}px">'
                        f'<svg class="retb" width="{sw}" height="{shh}" viewBox="0 0 {sw} {shh}" fill="none" stroke="{col}" stroke-width="3" '
                        f'stroke-linecap="square">{br}</svg>{lab}</div>')
            js.append(show(cid, t0, t1)
                      + f'tl.fromTo("#{cid} .retb", {{scale: 1.18, opacity: 0, transformOrigin: "50% 50%"}}, {{scale: 1, opacity: 1, duration: 0.2, ease: "power3.out"}}, {q(t0)});')
            if k.get("cross", True):
                cx, cyy = bx + bw / 2 - FR["x"], by + bhh / 2 - FR["y"]
                l, r, tp, bt = bx - pad - FR["x"], bx + bw + pad - FR["x"], by - pad - FR["y"], by + bhh + pad - FR["y"]
                segs = [(0, cyy, l, 1, "h", "100% 50%"), (r, cyy, FR["w"] - r, 1, "h", "0% 50%"), (cx, 0, 1, tp, "v", "50% 100%"), (cx, bt, 1, FR["h"] - bt, "v", "50% 0%")]
                lines = "".join(f'<div class="rx" style="left:{a:.0f}px;top:{b:.0f}px;width:{c_:.0f}px;height:{d_:.0f}px;transform-origin:{o}"></div>' for a, b, c_, d_, _, o in segs if c_ > 2 or d_ > 2)
                html.append(f'<div id="{cid}x" class="v2c retx" style="left:{FR["x"]}px;top:{FR["y"]}px;width:{FR["w"]}px;height:{FR["h"]}px;border-radius:{FR["radius"]}px">{lines}</div>')
                js.append(show(f"{cid}x", t0, t1)
                          + f'tl.fromTo("#{cid}x .rx", {{scale: 0}}, {{scale: 1, duration: 0.45, ease: "power2.inOut"}}, {q(t0 + 0.04)}); '
                          + out_fade(f"#{cid}x", t1, d=0.18, y=0))
            if k.get("label"):
                n = len(k["label"])
                js.append(f'(function () {{ const el = document.getElementById("{cid}l"), s = el.dataset.text, o = {{v: 0}}; '
                          f'tl.fromTo(o, {{v: 0}}, {{v: s.length, duration: {max(0.12, n * 0.022):.3f}, ease: "none", onUpdate: () => {{ el.textContent = s.slice(0, Math.round(o.v)); }}}}, {q(t0 + 0.18)}); }})();')
                cue(t0 + 0.2, "blip", k)
            js.append(f'tl.to("#{cid}", {{opacity: 0, scale: 0.96, duration: 0.18, ease: "power2.in"}}, {q(t1 - 0.2)});')
            cue(t0, "focus", k); cue(t0 + 0.14, "shutter-film", k); ev.append((t0, "reticle", i))
        elif kind == "route":
            vert = k.get("orient") == "v"
            nodes = k["nodes"]; nn = len(nodes)
            x, y, w = xy(k, 440 if vert else FR["w"] - 120)
            if vert:        # nodes down a line at x 46; label and sub to the right of each node
                top0 = 92 if k.get("title") else 44
                step = k.get("step", 84)
                h = k.get("h", top0 + step * (nn - 1) + 56)
                xs, ys = [46.0] * nn, [top0 + step * j for j in range(nn)]
                lab_at = lambda j: (f'left:84px;top:{ys[j] - 30:.0f}px;width:{w - 100}px;text-align:left', f'left:84px;top:{ys[j] + 8:.0f}px;width:{w - 100}px;text-align:left')
            else:
                h = k.get("h", 230)
                padx = 70; ly = h * 0.56
                xs = [padx + (w - 2 * padx) * (j / max(1, nn - 1)) for j in range(nn)] if nn > 1 else [w / 2]
                ys = [ly] * nn
                lab_at = lambda j: (f'left:{xs[j] - 130:.0f}px;top:{ly - 66:.0f}px', f'left:{xs[j] - 130:.0f}px;top:{ly + 26:.0f}px')
            ln = lambda j: math.hypot(xs[j + 1] - xs[j], ys[j + 1] - ys[j])
            segs = "".join(f'<line id="{cid}s{j}" x1="{xs[j]:.1f}" y1="{ys[j]:.1f}" x2="{xs[j + 1]:.1f}" y2="{ys[j + 1]:.1f}" stroke="rgba(255,255,255,0.55)" stroke-width="2" '
                           f'stroke-dasharray="{ln(j):.1f}" stroke-dashoffset="{ln(j):.1f}"/>' for j in range(nn - 1))
            dots = "".join(f'<circle id="{cid}r{j}" cx="{xs[j]:.1f}" cy="{ys[j]:.1f}" r="14" fill="none" stroke="{ACC}" stroke-width="2" opacity="0"/>'
                           f'<circle id="{cid}d{j}" cx="{xs[j]:.1f}" cy="{ys[j]:.1f}" r="8" fill="{ACC}" opacity="0" style="filter:drop-shadow(0 0 6px {ACC})"/>' for j in range(nn))
            labs = "".join(f'<div class="rnl{" v" if vert else ""}" id="{cid}l{j}" style="{lab_at(j)[0]}">{esc(nd[1])}</div>'
                           + (f'<div class="rns{" v" if vert else ""}" id="{cid}u{j}" style="{lab_at(j)[1]}">{esc(nd[2])}</div>' if len(nd) > 2 and nd[2] else "")
                           for j, nd in enumerate(nodes))
            bg = ""
            if k.get("src"):
                fn = os.path.basename(k["src"]); shutil.copy(os.path.join(job, k["src"]), os.path.join(out, "assets", fn))
                bg = f'<div class="rmap"><img src="assets/{fn}" alt=""></div><div class="rgrid"></div>'
            ttl = f'<div class="rtitle">{esc(k["title"])}</div>' if k.get("title") else ""
            html.append(f'<div id="{cid}" class="v2c route{" glass" if k.get("panel", True) else ""}" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px">'
                        f'{bg}{ttl}<svg class="rsvg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">{segs}{dots}</svg>{labs}</div>')
            js.append(show(cid, t0, t1) + rise_in(f"#{cid}", t0, d=0.4, y=30, blur=10))
            if vert and k.get("grow", True):     # the vertical panel GROWS one node at a time (never an empty box waiting for its rows)
                js.append(f'tl.set("#{cid}", {{height: {top0 + 24}}}, 0);')
                for j, nd in enumerate(nodes):
                    js.append(f'tl.to("#{cid}", {{height: {min(h, ys[j] + 56):.0f}, duration: 0.32, ease: "power3.out"}}, {q(max(nd[0], t0 + 0.15) - 0.04)});')
            if k.get("src"):
                js.append(f'tl.fromTo("#{cid} .rmap img", {{scale: 1.0, xPercent: 0}}, {{scale: 1.04, xPercent: -1.5, duration: {max(0.5, t1 - t0):.2f}, ease: "none"}}, {q(t0)});')
            if ttl:
                js.append(rise_in(f"#{cid} .rtitle", t0 + 0.1, d=0.35, y=10, blur=6))
            for j, nd in enumerate(nodes):
                tj = max(nd[0], t0 + 0.15)
                if j:
                    js.append(f'tl.to("#{cid}s{j - 1}", {{attr: {{"stroke-dashoffset": 0}}, duration: 0.55, ease: "power2.inOut"}}, {q(tj - 0.55)});')
                o_ = f"{xs[j]:.1f} {ys[j]:.1f}"
                js.append(f'tl.fromTo("#{cid}d{j}", {{opacity: 0, scale: 1.6, svgOrigin: "{o_}"}}, {{opacity: 1, scale: 1, svgOrigin: "{o_}", duration: 0.25, ease: "power3.out"}}, {q(tj)}); '
                          + pulse(f"#{cid}r{j}", o_, tj, 2.4)
                          + rise_in(f"#{cid}l{j}", tj + 0.02, d=0.3, y=12, blur=6)
                          + (rise_in(f"#{cid}u{j}", tj + 0.1, d=0.3, y=-8, blur=6) if len(nd) > 2 and nd[2] else ""))
                if j or tj - t0 > 0.3:
                    cue(tj, "glass", k); ev.append((tj, "route node", i))
            for tp in k.get("pulses", []):      # a new beat on the newest node while the speaker elaborates (no card holds > 6 s silent)
                jn = max([j for j, nd in enumerate(nodes) if nd[0] <= tp] or [0])
                o_ = f"{xs[jn]:.1f} {ys[jn]:.1f}"
                js.append(pulse(f"#{cid}r{jn}", o_, tp, 2.6)
                          + f'tl.fromTo("#{cid}l{jn}", {{color: "#FFFFFF"}}, {{color: "{ACC}", duration: 0.12, ease: "none"}}, {q(tp)}); '
                          f'tl.fromTo("#{cid}l{jn}", {{color: "{ACC}"}}, {{color: "#FFFFFF", duration: 0.9, ease: "power1.out", immediateRender: false}}, {q(tp + 0.12)});')
                cue(tp, "glass", k, rel=-2); ev.append((tp, "route pulse", i))
            js.append(out_fade(f"#{cid}", t1, d=0.22))
            cue(t0, "whoosh-soft", k); ev.append((t0, "route", i))
        elif kind == "widget":
            lay = k.get("layout", "todo")
            x, y, w = xy(k, 820)
            if "x" not in k:
                x = int(FR["x"] + (FR["w"] - w) / 2)
            meta = f'<div class="wmeta"><span>{esc(k.get("meta", ""))}</span><span class="wdots">•••</span></div>' if k.get("meta") else ""
            title = f'<div class="wtitle">{esc(k["title"])}</div>' if k.get("title") else ""
            head_h = 28 + (42 if meta else 0) + (74 if title else 0)        # padding + the meta row + the title (62) and its 12 px margin
            inner, rows_js, grow = "", [], []
            cur = ""
            if lay in ("todo", "list"):
                rows, ry = [], head_h
                for j, it in enumerate(k["items"]):
                    tj, text = it[0], it[1]
                    sub = it[2] if len(it) > 2 else ""
                    rh = (66 if lay == "todo" else 76) + (36 if sub else 0)
                    if lay == "todo":
                        tw = min(ig_type.width(text, "inter-700", 38), w - 150)
                        m = 24
                        strike = (f'<svg class="wstrike" width="{tw + 16:.0f}" height="48" viewBox="0 0 {tw + 16:.0f} 48"><path id="{cid}k{j}" '
                                  f'd="M2 {m + 2} C {tw * 0.3:.0f} {m - 5}, {tw * 0.62:.0f} {m + 7}, {tw + 12:.0f} {m - 1}" fill="none" stroke="{ACC}" '
                                  f'stroke-width="4" stroke-linecap="round" stroke-dasharray="{tw * 1.1 + 20:.0f}" stroke-dashoffset="{tw * 1.1 + 20:.0f}"/></svg>')
                        strike = strike if k.get("strike", True) else ""
                        rows.append(f'<div class="wrow" id="{cid}r{j}" style="height:{rh}px"><div class="wbox" id="{cid}b{j}"><svg width="36" height="36" viewBox="0 0 36 36">'
                                    f'<path id="{cid}t{j}" d="M10 18.5 L15.5 24 L26 12.5" fill="none" stroke="#0B0B0B" stroke-width="3.4" stroke-linecap="round" '
                                    f'stroke-linejoin="round" stroke-dasharray="26" stroke-dashoffset="26"/></svg></div>'
                                    f'<div class="wtxt"><span class="wtx" id="{cid}x{j}">{esc(text)}</span>{strike}</div></div>')
                        cxr, cyr = 34 + 18, ry + rh / 2
                        if k.get("cursor", True):
                            cur_t = tj - 0.06
                            rows_js.append(f'tl.to("#{cid}cur", {{x: {cxr - 6:.0f}, y: {cyr - 4:.0f}, duration: 0.4, ease: "power2.inOut"}}, {q(cur_t - 0.4)}); '
                                           f'tl.fromTo("#{cid}cur svg", {{scale: 1}}, {{scale: 0.86, duration: 0.06, ease: "power2.out", yoyo: true, repeat: 1, transformOrigin: "10% 5%"}}, {q(cur_t)});')
                        rows_js.append(f'tl.to("#{cid}b{j}", {{backgroundColor: "{ACC}", borderColor: "{ACC}", boxShadow: "0 0 18px {hexa(ACC, 0.6)}", duration: 0.15, ease: "power1.out"}}, {q(tj)}); '
                                       f'tl.to("#{cid}t{j}", {{attr: {{"stroke-dashoffset": 0}}, duration: 0.18, ease: "power2.out"}}, {q(tj + 0.03)}); '
                                       + (f'tl.to("#{cid}k{j}", {{attr: {{"stroke-dashoffset": 0}}, duration: 0.26, ease: "power2.out"}}, {q(tj + 0.06)}); '
                                          f'tl.to("#{cid}x{j}", {{opacity: 0.5, duration: 0.25, ease: "power1.out"}}, {q(tj + 0.1)});' if k.get("strike", True) else ""))
                        last = j == len(k["items"]) - 1
                        cue(tj, "confirm" if last else "glass", k); ev.append((tj, "widget tick", i))
                    else:
                        num = f"{j + 1:02d}"
                        rows.append(f'<div class="wrow list" id="{cid}r{j}" style="height:{rh}px"><div class="wnum">{num}</div><div class="wtxt2"><div class="wmain">{esc(text)}</div>'
                                    + (f'<div class="wsub">{esc(sub)}</div>' if sub else "") + "</div></div>")
                        grow.append((tj, ry + rh))
                        rows_js.append(rise_in(f"#{cid}r{j}", tj, d=0.32, y=18, blur=8))
                        cue(tj, "glass", k); ev.append((tj, "widget row", i))
                    ry += rh
                if k.get("stamp"):          # [t, "YOU CAN'T CHEAT IT"]: the card's closing line, its own beat
                    ts_, txt = k["stamp"]
                    rows.append(f'<div class="wstamp" id="{cid}st"><div class="wsline"></div><span>{esc(txt)}</span></div>')
                    grow.append((ts_, ry + 66)) if lay == "list" else None
                    rows_js.append(f'tl.fromTo("#{cid}st .wsline", {{scaleX: 0}}, {{scaleX: 1, duration: 0.3, ease: "power2.inOut"}}, {q(ts_ - 0.1)}); '
                                   + rise_in(f"#{cid}st span", ts_, d=0.32, y=14, blur=8))
                    cue(ts_ + 0.05, "thud", k); ev.append((ts_, "widget stamp", i))
                    if lay == "todo":       # the todo card grows by the stamp's row when it lands (no blank strip before it)
                        rows_js.append(f'tl.set("#{cid}card", {{height: {ry + 22}}}, 0); tl.to("#{cid}card", {{height: {ry + 88}, duration: 0.32, ease: "power3.out"}}, {q(ts_ - 0.12)});')
                    ry += 66
                total_h = ry + 22
                inner = "".join(rows)
            elif lay == "progress":
                C = 2 * math.pi * 80
                inner = (f'<div class="wprog"><svg width="200" height="200" viewBox="0 0 200 200"><circle cx="100" cy="100" r="80" fill="none" stroke="rgba(255,255,255,0.12)" stroke-width="14"/>'
                         f'<circle id="{cid}arc" cx="100" cy="100" r="80" fill="none" stroke="{ACC}" stroke-width="14" stroke-linecap="round" stroke-dasharray="{C:.1f}" '
                         f'stroke-dashoffset="{C:.1f}" transform="rotate(-90 100 100)" style="filter:drop-shadow(0 0 8px {hexa(ACC, 0.7)})"/></svg>'
                         f'<div class="wpct"><span id="{cid}p">0</span><small>%</small></div><div class="wplab"><div class="wmain">{esc(k.get("label", ""))}</div>'
                         f'<div class="wsub">{esc(k.get("sub", ""))}</div></div></div>')
                total_h = head_h + 230
                prev = 0
                for tj, pct in k.get("values", []):
                    # the number is READ OFF the arc on every render, so it can never disagree with the ring (two counters writing one
                    # element showed the second value before the first fill, on a seek back: the mini test, 2026-10-12)
                    rows_js.append(f'tl.to("#{cid}arc", {{attr: {{"stroke-dashoffset": {C * (1 - pct / 100):.1f}}}, duration: 0.6, ease: "power2.inOut", onUpdate: () => {{ '
                                   f'const a = document.getElementById("{cid}arc"); document.getElementById("{cid}p").textContent = '
                                   f'Math.round((1 - parseFloat(a.getAttribute("stroke-dashoffset")) / {C:.1f}) * 100); }}}}, {q(tj)});')
                    prev = pct
                    cue(tj + 0.55, "glass", k); ev.append((tj + 0.55, "widget value", i))
            elif lay == "notify":
                ini = esc(k.get("initial", (k.get("app") or "A")[:1]))
                inner = (f'<div class="wnoti"><div class="wico">{ini}</div><div class="wntx"><div class="wnhead"><span>{esc(k.get("app", ""))}</span><span>{esc(k.get("time", "now"))}</span></div>'
                         f'<div class="wmain">{esc(k.get("title", ""))}</div><div class="wsub">{esc(k.get("body", ""))}</div></div></div>')
                total_h = None                 # content-sized: the title / body may wrap in a narrow card
                title, meta, head_h = "", "", 0
            if k.get("cursor", True) and lay == "todo":
                cur = (f'<div class="wcur" id="{cid}cur" style="transform:translate({w + 60}px,{(total_h or 200) + 80}px)"><svg width="44" height="56" viewBox="0 0 44 56">'
                       f'<path d="M4 3 L4 44 L14.5 34.5 L21.5 51 L28.5 48 L21.5 32 L35.5 32 Z" fill="#FFFFFF" stroke="#111111" stroke-width="2.4" stroke-linejoin="round"/></svg></div>')
            fid = f"mb{cid}"
            html.append(f'{mbdef(fid)}<div id="{cid}" class="v2c wwrap" style="left:{x}px;top:{y}px;width:{w}px">'
                        f'<div class="widget glass" id="{cid}card" data-mb="{fid}" style="{f"height:{total_h}px;" if total_h else ""}filter:url(#{fid})">{meta}{title}<div class="wbody">{inner}</div></div>{cur}</div>')
            js.append(show(cid, t0, t1))
            if lay == "notify":
                js.append(f'tl.fromTo("#{cid}card", {{opacity: 0, y: -70}}, {{opacity: 1, y: 0, duration: 0.45, ease: "power3.out"}}, {q(t0)});' + mblur(fid, 0, 16, t0, 0.45))
            else:
                js.append(f'tl.fromTo("#{cid}card", {{opacity: 0, x: 60}}, {{opacity: 1, x: 0, duration: 0.42, ease: "power3.out"}}, {q(t0)});' + mblur(fid, 18, 0, t0, 0.42))
            if grow:     # the list card GROWS with its rows (never an empty box; Rich Roll v2). Its height, not a clip: a clip would cut the glow
                js.append(f'tl.set("#{cid}card", {{height: {head_h + 8}}}, 0);')
                for tj, bottom in grow:
                    js.append(f'tl.to("#{cid}card", {{height: {bottom + 22}, duration: 0.32, ease: "power3.out"}}, {q(tj - 0.04)});')
            if cur:
                js.append(f'tl.fromTo("#{cid}cur", {{opacity: 0}}, {{opacity: 1, duration: 0.25}}, {q(t0 + 0.3)});')
            js += rows_js
            js.append(out_fade(f"#{cid}", t1, d=0.22))
            cue(t0, k.get("sfx_kind", "whoosh-soft"), k); ev.append((t0, f"widget {lay}", i))
        elif kind == "wordscene":
            bleed = k.get("bleed", False)
            hero = k.get("hero")
            ws = []
            for j, (tj, word) in enumerate(k["words"]):
                cls = "wsw hero" if j == hero else "wsw"
                ws.append(f'<div class="{cls}" id="{cid}w{j}">{esc(cap_word(word).lower() if j != hero else cap_word(word))}</div>')
            wy_ = k.get("wy", int(FR["h"] * 0.36))
            # the black ground and the words are two layers: the ground may "bleed" to the full frame while the words stay put in the window
            box = f'left:{FR["x"]}px;top:{FR["y"]}px;width:{FR["w"]}px;height:{FR["h"]}px;border-radius:{FR["radius"]}px'
            html.append(f'<div id="{cid}" class="v2c ws" style="{box}"><div class="wsglow" style="--wy:{wy_}px"></div></div>'
                        f'<div id="{cid}t" class="v2c wst" style="{box};--wy:{wy_}px">{"".join(ws)}</div>')
            js.append(show(cid, t0, t1) + show(f"{cid}t", t0, t1))
            if bleed:
                js.append(f'tl.fromTo("#{cid}", {{left: {FR["x"]}, top: {FR["y"]}, width: {FR["w"]}, height: {FR["h"]}, borderRadius: {FR["radius"]}, opacity: 0}}, '
                          f'{{left: 0, top: 0, width: {W}, height: {H}, borderRadius: 0, opacity: 1, duration: 0.55, ease: "power3.inOut"}}, {q(t0)}); '
                          f'tl.to("#{cid}", {{left: {FR["x"]}, top: {FR["y"]}, width: {FR["w"]}, height: {FR["h"]}, borderRadius: {FR["radius"]}, opacity: 0, duration: 0.55, ease: "power3.inOut"}}, {q(t1 - 0.57)});')
            else:
                js.append(f'tl.fromTo("#{cid}", {{opacity: 0}}, {{opacity: 1, duration: 0.18, ease: "power1.out"}}, {q(t0)}); '
                          f'tl.to("#{cid}", {{opacity: 0, duration: 0.2, ease: "power1.in"}}, {q(t1 - 0.22)});')
            for j, (tj, word) in enumerate(k["words"]):
                te = k["words"][j + 1][0] if j + 1 < len(k["words"]) else t1 - 0.22
                js.append(f'tl.fromTo("#{cid}w{j}", {{opacity: 0, y: 24, filter: "blur(8px)"}}, {{opacity: 1, y: 0, filter: "blur(0px)", duration: 0.12, ease: "power3.out"}}, {q(tj)}); '
                          f'tl.to("#{cid}w{j}", {{opacity: 0, y: -20, filter: "blur(8px)", duration: 0.12, ease: "power2.in"}}, {q(max(tj + 0.15, te - 0.12))});')
                if j:
                    cue(tj, "thud" if j == hero else "glass", k, rel=0 if j == hero else -3); ev.append((tj, "word", i))
            cue(t0, "whoosh-med", k); ev.append((t0, "wordscene", i))
        elif kind == "titlecard":
            name = k["name"].upper()
            nsize = k.get("size", 84)
            maxw = FR["w"] - 144
            lines_n = [name]
            if ig_type.width(name, "wide-700", nsize, 0.01) > maxw and " " in name:      # two lines, split nearest the middle
                sp = [j for j, ch in enumerate(name) if ch == " "]
                cut = min(sp, key=lambda j: abs(j - len(name) / 2))
                lines_n = [name[:cut], name[cut + 1:]]
            widest = max(ig_type.width(l, "wide-700", nsize, 0.01) for l in lines_n)
            if widest > maxw:
                nsize = int(nsize * maxw / widest)
            nm = "<br>".join(esc(l) for l in lines_n)
            kick = f'<div class="tck">{esc(k["kicker"])}</div>' if k.get("kicker") else ""
            html.append(f'<div id="{cid}" class="v2c tc" style="left:{FR["x"]}px;top:{FR["y"]}px;width:{FR["w"]}px;height:{FR["h"]}px;border-radius:{FR["radius"]}px">'
                        f'<div class="tcscrim{" top" if k.get("pos", "top") == "top" else ""}"></div><div class="tcin{" top" if k.get("pos", "top") == "top" else ""}">{kick}<div class="tcline"></div>'
                        f'<div class="tcn" style="font-size:{nsize}px"><span class="r">{nm}</span><span class="g">{nm}</span><span class="b">{nm}</span></div>'
                        f'<div class="tcr">{esc(k.get("role", ""))}</div></div></div>')
            js.append(show(cid, t0, t1)
                      + f'tl.fromTo("#{cid} .tcscrim", {{opacity: 0}}, {{opacity: 1, duration: 0.3, ease: "power1.out"}}, {q(t0)}); '
                      f'tl.fromTo("#{cid} .tcin", {{scale: 1.0, transformOrigin: "0% 100%"}}, {{scale: 1.04, duration: {max(0.5, t1 - t0):.2f}, ease: "none"}}, {q(t0)}); '
                      + (rise_in(f"#{cid} .tck", t0 + 0.05, d=0.35, y=10, blur=6) if kick else "")
                      + f'tl.fromTo("#{cid} .tcline", {{scaleX: 0, transformOrigin: "0% 50%"}}, {{scaleX: 1, duration: 0.3, ease: "power2.inOut"}}, {q(t0 + 0.08)}); '
                      f'tl.fromTo("#{cid} .tcn", {{opacity: 0}}, {{opacity: 1, duration: 0.12, ease: "none"}}, {q(t0 + 0.12)}); '
                      f'tl.fromTo("#{cid} .tcn .r", {{x: -7, filter: "blur(2px)"}}, {{x: 0, filter: "blur(0px)", duration: 0.3, ease: "power2.out"}}, {q(t0 + 0.2)}); '
                      f'tl.fromTo("#{cid} .tcn .b", {{x: 7, filter: "blur(2px)"}}, {{x: 0, filter: "blur(0px)", duration: 0.3, ease: "power2.out"}}, {q(t0 + 0.2)}); '
                      + rise_in(f"#{cid} .tcr", t0 + 0.38, d=0.35, y=12, blur=6)
                      + out_fade(f"#{cid}", t1, d=0.25, y=0))
            cue(t0, "whoosh-med", k); cue(t0 + 0.24, "thud-low", k); ev.append((t0, "titlecard", i))
        elif kind == "compare":
            x, y, w = xy(k, FR["w"] - 120)
            if "x" not in k:
                x = int(FR["x"] + (FR["w"] - w) / 2)
            vert = k.get("orient") == "v"
            cw = w if vert else (w - 70) / 2
            col_ = lambda side, d: (f'{mbdef(f"mb{cid}{side}")}<div class="cmpcol glass" id="{cid}{side}" data-mb="mb{cid}{side}" style="width:{cw:.0f}px;filter:url(#mb{cid}{side})">'
                                    f'<div class="cml">{esc(d.get("label", ""))}</div><div class="cmv"><span class="cmvv" id="{cid}{side}v">{esc(d.get("value", ""))}</span>'
                                    f'<span class="cmstrike" id="{cid}{side}s"></span></div><div class="cms">{esc(d.get("sub", ""))}</div></div>')
            html.append(f'<div id="{cid}" class="v2c cmp{" v" if vert else ""}" style="left:{x}px;top:{y}px;width:{w}px">{col_("L", k["left"])}'
                        f'<div class="cmmid"><div class="cmdiv" id="{cid}d"></div><div class="cmvs">VS</div></div>{col_("R", k["right"])}</div>')
            tr = k.get("t_right", t0 + 0.6)
            js.append(show(cid, t0, t1)
                      + f'tl.fromTo("#{cid}d", {{{"scaleX" if vert else "scaleY"}: 0}}, {{{"scaleX" if vert else "scaleY"}: 1, duration: 0.4, ease: "power2.inOut"}}, {q(t0)}); '
                      + rise_in(f"#{cid} .cmvs", t0 + 0.2, d=0.3, y=6, blur=4)
                      + f'tl.fromTo("#{cid}L", {{opacity: 0, x: -56}}, {{opacity: 1, x: 0, duration: 0.42, ease: "power3.out"}}, {q(t0)});' + mblur(f"mb{cid}L", 16, 0, t0, 0.42)
                      + f'tl.fromTo("#{cid}R", {{opacity: 0, x: {-56 if vert else 56}}}, {{opacity: 1, x: 0, duration: 0.42, ease: "power3.out"}}, {q(tr)});' + mblur(f"mb{cid}R", 16, 0, tr, 0.42))
            cue(t0, "whoosh-soft", k); cue(tr, "whoosh-soft", k); ev += [(t0, "compare", i), (tr, "compare right", i)]
            if k.get("win"):
                tw_ = k.get("t_win", tr + 0.7)
                wn, ls = ("R", "L") if k["win"] == "right" else ("L", "R")
                js.append(f'tl.to("#{cid}{wn}v", {{color: "{ACC}", textShadow: "0 0 22px {hexa(ACC, 0.7)}, 0 0 5px {ACC}", scale: 1.05, duration: 0.3, ease: "power2.out"}}, {q(tw_)}); '
                          f'tl.to("#{cid}{ls}", {{opacity: 0.45, duration: 0.3, ease: "power1.out"}}, {q(tw_)}); '
                          f'tl.fromTo("#{cid}{ls}s", {{scaleX: 0}}, {{scaleX: 1, duration: 0.3, ease: "power2.out"}}, {q(tw_ + 0.05)});')
                cue(tw_, "thud", k); ev.append((tw_, "compare win", i))
            js.append(out_fade(f"#{cid}", t1, d=0.22))
        else:
            sys.exit(f"ig_v2: card kind '{kind}' is not part of the v2 vocabulary (neon lower3 reticle route widget wordscene titlecard compare "
                     f"leak). The v1 paper cards stay on v1; their v2 equivalents: rules/receipt/check -> widget list/todo, notify/call -> widget notify, "
                     f"number -> neon, title/label -> hook or neon.")

    scenes = [(k["t0"], k["t1"]) for k in spec.get("cards", []) if k["kind"] in FULL or k.get("rack")]
    for i, k in enumerate(spec.get("cards", [])):
        if k["kind"] in FULL or k.get("rack") or k["kind"] == "leak":
            continue
        for a, b in scenes:
            if a < k["t1"] - 0.3 and b > k["t0"] + 0.3:
                js.append(f'tl.to("#k{i}", {{opacity: 0, duration: 0.18, ease: "power1.in"}}, {q(max(k["t0"], a))}); '
                          + (f'tl.to("#k{i}", {{opacity: 1, duration: 0.25, ease: "power1.out"}}, {q(b)});' if b < k["t1"] - 0.3 else ""))
    css = CSS.replace("ACC66", hexa(ACC, 0.4)).replace("ACC33", hexa(ACC, 0.2)).replace("ACC99", hexa(ACC, 0.6)).replace("ACCB3", hexa(ACC, 0.7)).replace("ACC", ACC)
    doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width={W}, height={H}" />
<style>
{css}
</style>
</head>
<body>
<div id="root" data-composition-id="onyx-ig-overlay" data-start="0" data-width="{W}" data-height="{H}" data-duration="{dur:.4f}" data-fps="{fps}">
  {chr(10).join(html + caph)}
</div>
<script src="vendor/gsap.min.js"></script>
<script>
(function () {{
  window.__timelines = window.__timelines || {{}};
  const COMP = "onyx-ig-overlay";
  const tl = gsap.timeline({{ paused: true }});
  {chr(10).join(js)}
  tl.set({{}}, {{}}, {dur:.4f});
  window.__timelines[COMP] = tl;
}})();
</script>
</body>
</html>
"""
    open(os.path.join(out, "index.html"), "w", encoding="utf-8").write(doc)
    os.makedirs(os.path.join(job, "ig", "work"), exist_ok=True)
    json.dump(sorted(sfx, key=lambda s: s["t"]), open(os.path.join(job, "ig", "work", "sfx-cues.json"), "w", encoding="utf-8"), indent=1)
    report = density(spec, ev, fps, dur, FR)
    json.dump(dict(events=sorted(ev), **report), open(os.path.join(job, "ig", "work", "v2-events.json"), "w", encoding="utf-8"), indent=1)
    print(f"ig_v2: {len(chunks)} caption chunks ({mode}), {len(spec.get('cards', []))} cards, {len(sfx)} sfx cues, {len(ev)} designed events -> {out}")
    for line in report["lines"]:
        print("  " + line)


def density(spec, ev, fps, dur, FR):
    """The research's pacing targets (move 16), measured on this spec: events per 10 s, the full-window budget, face between scenes,
    long holds, and full-window edges that miss a cut by 1-3 frames (a one-frame face flash, Affan 2026-10-09)."""
    ts = sorted(t for t, _, _ in ev)
    bins = [sum(1 for t in ts if b <= t < b + 10) for b in range(0, int(math.ceil(dur)), 10)]
    low = [f"{10 * j}-{10 * j + 10} s" for j, n in enumerate(bins) if n < 3 and 10 * j + 10 <= dur + 0.5]
    lines = [f"events per 10 s: {bins} (target >= 3-4; {len(ts) / dur * 10:.1f} overall)" + (f"  ** thin: {low}" if low else "")]
    cards = spec.get("cards", [])
    full = sorted((k["t0"], k["t1"], k["kind"]) for k in cards if k["kind"] in FULL or k.get("rack"))
    share = sum(b - a for a, b, _ in full) / dur
    lines.append(f"full-window scenes: {len(full)}, {share * 100:.0f} % of runtime (<= 25 %)" + ("  ** OVER **" if share > 0.25 else ""))
    for (a0, a1, ka), (b0, b1, kb) in zip(full, full[1:]):
        if b0 - a1 < 1.5:
            lines.append(f"  ** only {b0 - a1:.2f} s of face between {ka}@{a0} and {kb}@{b0} (>= 1.5 s)")
    for i, k in enumerate(cards):
        if k["kind"] in ("leak",):
            continue
        beats = sorted([k["t0"]] + [t for t, _, idx in ev if idx == i and k["t0"] < t < k["t1"]] + [k["t1"]])
        gap = max(b - a for a, b in zip(beats, beats[1:]))
        if gap > 6.0:
            lines.append(f"  ** {k['kind']}@{k['t0']} holds {gap:.1f} s with no new beat (<= 6 s)")
    cuts = [s["f0"] for s in spec.get("shots", []) if s["f0"] > 0]
    for a, b, kd in full:
        for edge in (a, b):
            f = round(edge * fps)
            near = [c for c in cuts if 0 < abs(c - f) <= 3]
            if near:
                lines.append(f"  ** {kd} edge {edge:.3f} s is {f - near[0]:+d} frames off the cut at frame {near[0]}: land it ON the cut")
    return dict(per10=bins, full_share=round(share, 3), lines=lines)


CSS = """
@font-face { font-family: "Inter"; src: url("fonts/Inter-Regular.otf"); font-weight: 400; }
@font-face { font-family: "Inter"; src: url("fonts/Inter-Bold.otf"); font-weight: 700; }
@font-face { font-family: "Inter"; src: url("fonts/Inter-Black.otf"); font-weight: 900; }
/* unique family names: one called "Serif" rendered as Inter italic in the final (the demo's first render, 2026-10-12) */
@font-face { font-family: "OnyxSerif"; src: url("fonts/Cormorant-Italic-VariableFont_wght.ttf"); font-weight: 300 700; font-style: italic; }
@font-face { font-family: "OnyxPlay"; src: url("fonts/PlayfairDisplay-Italic-VF.ttf"); font-weight: 400 900; font-style: italic; }
@font-face { font-family: "OnyxMono"; src: url("fonts/IBMPlexMono-Regular.ttf"); font-weight: 400; }
@font-face { font-family: "OnyxMono"; src: url("fonts/IBMPlexMono-Medium.ttf"); font-weight: 500; }
@font-face { font-family: "OnyxMono"; src: url("fonts/IBMPlexMono-SemiBold.ttf"); font-weight: 600; }
@font-face { font-family: "OnyxWide"; src: url("fonts/Unbounded-VariableFont_wght.ttf"); font-weight: 200 900; }
html, body { margin: 0; background: transparent; }
#root { position: relative; width: 1080px; height: 1920px; overflow: hidden; background: transparent; font-family: "Inter", sans-serif; color: #FFFFFF; }
.v2c { position: absolute; visibility: hidden; }
.glass { background: linear-gradient(180deg, rgba(36,36,40,0.84), rgba(14,14,16,0.88)); border: 1.5px solid rgba(255,255,255,0.10);
  border-radius: 40px; box-shadow: inset 0 1px 0 rgba(255,255,255,0.10), 0 0 46px ACC33, 0 26px 64px rgba(0,0,0,0.45); box-sizing: border-box; }

/* ---- captions */
.cap2 { position: absolute; visibility: hidden; }
.cap2.stack .sl { white-space: nowrap; }
.cap2.stack .w { display: inline-block; }
.cap2.stack .sl.lead { font-weight: 700; letter-spacing: -0.012em; text-shadow: 0 0 18px rgba(0,0,0,0.5), 0 0 3px rgba(0,0,0,0.35); }
.cap2.stack .sl.hero { font-family: "OnyxSerif"; font-style: italic; font-weight: 600; letter-spacing: -0.005em; color: ACC;
  text-shadow: 0 0 18px ACC99, 0 0 4px ACC; }
.cap2.stack .sl.hero.black { font-family: "Inter"; font-style: normal; font-weight: 900; letter-spacing: -0.02em; }
.cap2.word { text-align: center; }
.cap2.word .wdw { display: inline-block; }
.cap2.word.mono .wd { display: inline-block; font-family: "OnyxMono"; font-weight: 600; font-size: 44px; line-height: 1.15; letter-spacing: 0.04em;
  background: rgba(40,40,40,0.55); padding: 8px 16px; border-radius: 4px; }
.cap2.word.mono .wd.hl { background: var(--hc, ACC); color: #0B0B0B; }
.cap2.word.wide .wd { display: inline-block; font-family: "OnyxWide"; font-weight: 700; font-size: 62px; line-height: 1.15; letter-spacing: 0.05em;
  background: linear-gradient(180deg, #FFFFFF 20%, #E9E1D2 100%); -webkit-background-clip: text; background-clip: text; color: transparent;
  filter: drop-shadow(0 0 14px rgba(0,0,0,0.4)); }
.cap2.word.wide .wd.hl { background: none; color: var(--hc, ACC); -webkit-text-fill-color: var(--hc, ACC); }
.cap2.word.wide .wd + .wd { margin-left: 0.3em; }
.cap2.line { text-align: center; }
.cap2.line .lmask { overflow: hidden; padding: 10px 0; }
.cap2.line .lin { font-weight: 700; font-size: 58px; line-height: 1.2; letter-spacing: -0.012em; white-space: nowrap;
  text-shadow: 0 0 18px rgba(0,0,0,0.5), 0 0 3px rgba(0,0,0,0.35); }
.cap2.line .w { display: inline-block; }
.cap2.line .sweep { position: relative; }
.cap2.line .sweep .sw { position: absolute; left: 0; top: 0; clip-path: inset(0% 100% 0% 0%); }

/* ---- top bar hook, bottom bar credit, split seam */
.hook { left: 60px; width: 960px; text-align: center; }
.hook .hkick { font-family: "OnyxMono"; font-weight: 500; font-size: 24px; letter-spacing: 0.22em; text-transform: uppercase;
  color: rgba(255,255,255,0.6); height: 44px; line-height: 30px; }
.hook .hmask { overflow: hidden; height: 80px; padding: 16px 0 12px; margin: -16px 0 -12px; }
.hook .hline { display: inline-block; font-weight: 700; font-size: 62px; line-height: 80px; letter-spacing: -0.018em; white-space: nowrap; }
.hook .hhl { font-family: "OnyxSerif"; font-style: italic; font-weight: 600; font-size: 1.34em; line-height: 0.5; color: ACC; letter-spacing: 0;
  text-shadow: 0 0 18px ACC99, 0 0 4px ACC; }
.credit2 { left: 0; width: 1080px; text-align: center; font-family: "OnyxMono"; font-weight: 500; font-size: 26px; letter-spacing: 0.14em;
  text-transform: uppercase; color: rgba(255,255,255,0.55); }
.credit2 .cdash { display: inline-block; width: 28px; height: 2px; background: ACC; box-shadow: 0 0 8px ACC; vertical-align: 8px; margin-right: 16px; }
.seam { height: 4px; background: #FFFFFF; box-shadow: 0 0 10px rgba(255,255,255,0.8), 0 0 26px ACC66; }

/* ---- neon number / hero phrase */
.neon .nlead, .neon .ntail { font-weight: 700; font-size: 44px; line-height: 1.18; letter-spacing: -0.01em; text-shadow: 0 0 14px rgba(255,255,255,0.32), 0 0 2px rgba(0,0,0,0.4); }
.neon .nw { display: inline-block; }
.neon .nlead, .neon .ntail { display: grid; }
.neon .n1, .neon .n2 { grid-area: 1 / 1; }
.neon .n2 .nw { opacity: 0; }
.neon .nval { display: grid; margin: 4px 0 8px; }
.neon .nv { grid-area: 1 / 1; font-family: "OnyxPlay"; font-style: italic; font-weight: 800; line-height: 1.02; letter-spacing: -0.01em; white-space: nowrap;
  color: ACC; text-shadow: 0 0 26px ACCB3, 0 0 7px ACC; }
.neon .nv .ch { display: inline-block; }
.neon .nv.b .ch { opacity: 0; }

/* ---- mono lower third */
.l3 { display: flex; gap: 22px; align-items: flex-start; z-index: 0; }
.l3 .l3s { position: absolute; left: -70px; top: -50px; right: -90px; bottom: -50px; z-index: -1;
  background: radial-gradient(closest-side, rgba(0,0,0,0.34), rgba(0,0,0,0)); }
.l3bar { width: 6px; border-radius: 3px; background: ACC; box-shadow: 0 0 18px ACC, 0 0 4px ACC; flex: none; }
.l3n { font-family: "OnyxMono"; font-weight: 500; font-size: 44px; line-height: 1.15; letter-spacing: 0.04em; text-transform: uppercase; white-space: nowrap;
  text-shadow: 0 0 12px rgba(255,255,255,0.28); }
.l3r { font-family: "OnyxMono"; font-weight: 400; font-size: 30px; line-height: 1.2; color: rgba(255,255,255,0.82); margin-top: 10px; white-space: nowrap; }

/* ---- HUD reticle */
.ret .retb { position: absolute; left: 0; top: 0; overflow: visible; filter: drop-shadow(0 0 5px rgba(255,255,255,0.55)); }
.ret .retlab { position: absolute; left: -200px; right: -200px; top: calc(100% + 14px); text-align: center; font-family: "OnyxMono"; font-weight: 600;
  font-size: 28px; letter-spacing: 0.1em; text-transform: uppercase; white-space: nowrap; text-shadow: 0 0 10px rgba(0,0,0,0.7); }
.ret .retlab.top { top: auto; bottom: calc(100% + 14px); }
.retx { overflow: hidden; }
.retx .rx { position: absolute; background: rgba(255,255,255,0.28); }

/* ---- route / timeline */
.route { overflow: hidden; border-radius: 36px; }
.route .rsvg { position: absolute; left: 0; top: 0; overflow: visible; }
.route .rtitle { position: absolute; left: 34px; right: 20px; top: 26px; font-family: "OnyxMono"; font-weight: 500; font-size: 24px; letter-spacing: 0.16em;
  text-transform: uppercase; color: ACC; white-space: nowrap; overflow: hidden; }
.route .rnl { position: absolute; width: 260px; text-align: center; font-family: "OnyxMono"; font-weight: 600; font-size: 30px; letter-spacing: 0.06em;
  text-transform: uppercase; line-height: 40px; white-space: nowrap; }
.route .rns { position: absolute; width: 260px; text-align: center; font-size: 26px; line-height: 34px; color: rgba(255,255,255,0.66); white-space: nowrap; }
.route .rnl.v { font-size: 30px; line-height: 36px; letter-spacing: 0.04em; }
.route .rns.v { font-size: 26px; line-height: 32px; }
.route .rmap { position: absolute; inset: 0; overflow: hidden; }
.route .rmap img { width: 100%; height: 100%; object-fit: cover; filter: brightness(0.5) saturate(0.7); }
.route .rgrid { position: absolute; inset: 0; background: repeating-linear-gradient(90deg, rgba(255,255,255,0.22) 0 1px, rgba(0,0,0,0) 1px 25%); }

/* ---- widget */
.wwrap .widget { position: relative; overflow: hidden; padding: 28px 34px 0; }
.widget .wmeta { display: flex; justify-content: space-between; height: 42px; font-family: "OnyxMono"; font-weight: 500; font-size: 25px; line-height: 30px;
  letter-spacing: 0.08em; color: ACC; text-transform: uppercase; }
.widget .wdots { color: rgba(255,255,255,0.45); letter-spacing: 0.1em; flex: none; margin-left: 12px; }
.widget .wmeta span:first-child { white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.widget .wtitle { height: 62px; font-weight: 700; font-size: 40px; line-height: 50px; letter-spacing: -0.01em; border-bottom: 1px solid rgba(255,255,255,0.12); margin-bottom: 12px; }
.widget .wrow { display: flex; align-items: center; gap: 22px; box-sizing: border-box; }
.widget .wbox { width: 36px; height: 36px; border-radius: 18px; border: 2.5px solid rgba(255,255,255,0.5); box-sizing: border-box; flex: none;
  display: flex; align-items: center; justify-content: center; }
.widget .wbox svg { margin: -2.5px; }
.widget .wtxt { position: relative; font-weight: 700; font-size: 38px; line-height: 46px; white-space: nowrap; overflow: visible; }
.widget .wstrike { position: absolute; left: -6px; top: 0; overflow: visible; filter: drop-shadow(0 0 6px ACC66); }
.widget .wstamp { height: 66px; position: relative; font-family: "OnyxMono"; font-weight: 600; font-size: 26px; letter-spacing: 0.14em;
  text-transform: uppercase; color: ACC; text-shadow: 0 0 12px ACC99; line-height: 66px; white-space: nowrap; }
.widget .wstamp span { display: inline-block; }
.widget .wsline { position: absolute; left: 0; right: 0; top: 8px; height: 1px; background: rgba(255,255,255,0.18); transform-origin: 0% 50%; }
.widget .wrow.list { align-items: flex-start; padding-top: 14px; border-top: 1px solid rgba(255,255,255,0.07); }
.widget .wnum { font-family: "OnyxMono"; font-weight: 600; font-size: 30px; line-height: 46px; color: ACC; width: 52px; flex: none; text-shadow: 0 0 10px ACC66; }
.widget .wmain { font-weight: 700; font-size: 38px; line-height: 46px; letter-spacing: -0.01em; }
.widget .wsub { font-size: 28px; line-height: 36px; color: rgba(255,255,255,0.62); }
.widget .wprog { display: flex; align-items: center; gap: 30px; height: 230px; position: relative; }
.widget .wpct { position: absolute; left: 0; width: 200px; top: 0; height: 200px; display: flex; align-items: center; justify-content: center;
  font-family: "OnyxMono"; font-weight: 600; font-size: 54px; }
.widget .wpct small { font-size: 28px; margin-left: 2px; color: rgba(255,255,255,0.7); }
.widget .wnoti { display: flex; gap: 22px; align-items: flex-start; padding: 2px 0 28px; }
.widget .wnoti .wmain { font-size: 34px; line-height: 40px; margin-top: 4px; }
.widget .wnoti .wsub { font-size: 27px; line-height: 34px; }
.widget .wico { width: 66px; height: 66px; margin-top: 4px; border-radius: 18px; flex: none; background: linear-gradient(180deg, ACC, ACC99); color: #0B0B0B;
  font-weight: 900; font-size: 40px; display: flex; align-items: center; justify-content: center; }
.widget .wntx { flex: 1; min-width: 0; }
.widget .wnhead { display: flex; justify-content: space-between; font-family: "OnyxMono"; font-weight: 500; font-size: 24px; letter-spacing: 0.08em;
  text-transform: uppercase; color: rgba(255,255,255,0.6); }
.wcur { position: absolute; left: 0; top: 0; filter: drop-shadow(0 6px 10px rgba(0,0,0,0.45)); }

/* ---- word scene */
.ws { background: #000000; overflow: hidden; }
.ws .wsglow { position: absolute; inset: 0; background: radial-gradient(closest-side, ACC33, rgba(0,0,0,0) 70%); opacity: 0.55; }
.ws .wsglow { top: calc(var(--wy) - 450px); bottom: auto; height: 900px; }
.wst .wsw { position: absolute; left: 0; right: 0; top: var(--wy); margin-top: -70px; height: 140px; line-height: 140px; text-align: center; font-weight: 700;
  font-size: 104px; letter-spacing: -0.03em; opacity: 0; }
.wst .wsw.hero { font-family: "OnyxSerif"; font-style: italic; font-weight: 600; font-size: 166px; letter-spacing: -0.01em; color: ACC;
  text-shadow: 0 0 26px ACC99, 0 0 6px ACC; }

/* ---- title card */
.tc { overflow: hidden; }
.tc .tcscrim { position: absolute; inset: 0; background: linear-gradient(180deg, rgba(0,0,0,0.05) 20%, rgba(0,0,0,0.62) 100%); }
.tc .tcin { position: absolute; left: 72px; right: 72px; bottom: 120px; }
.tc .tcin.top { top: 92px; bottom: auto; }
.tc .tcscrim.top { background: linear-gradient(0deg, rgba(0,0,0,0.05) 25%, rgba(0,0,0,0.6) 100%); }
.tc .tck { font-family: "OnyxMono"; font-weight: 500; font-size: 24px; letter-spacing: 0.24em; text-transform: uppercase; color: ACC; margin-bottom: 18px; }
.tc .tcline { width: 72px; height: 3px; background: ACC; box-shadow: 0 0 10px ACC; margin-bottom: 22px; }
.tc .tcn { display: grid; isolation: isolate; font-family: "OnyxWide"; font-weight: 700; line-height: 1.04; letter-spacing: 0.01em; }
.tc .tcn span { grid-area: 1 / 1; mix-blend-mode: screen; }
.tc .tcn .r { color: #FF3B30; } .tc .tcn .g { color: #2BFF88; } .tc .tcn .b { color: #3B82FF; }
.tc .tcr { font-family: "OnyxMono"; font-weight: 400; font-size: 30px; letter-spacing: 0.06em; color: rgba(255,255,255,0.84); margin-top: 18px; }

/* ---- compare */
.cmp { display: flex; align-items: stretch; }
.cmp .cmpcol { padding: 26px 28px 28px; border-radius: 34px; }
.cmp .cml { font-family: "OnyxMono"; font-weight: 500; font-size: 24px; letter-spacing: 0.16em; text-transform: uppercase; color: rgba(255,255,255,0.62); }
.cmp .cmv { position: relative; display: inline-block; margin: 6px 0 2px; }
.cmp .cmvv { display: inline-block; font-family: "OnyxPlay"; font-style: italic; font-weight: 800; font-size: 84px; line-height: 1.05; transform-origin: 0% 60%; }
.cmp .cmstrike { position: absolute; left: -6px; right: -6px; top: 54%; height: 4px; background: rgba(255,255,255,0.85); transform: scaleX(0); transform-origin: 0% 50%; }
.cmp .cms { font-size: 28px; line-height: 36px; color: rgba(255,255,255,0.7); }
.cmp .cmmid { width: 70px; position: relative; flex: none; }
.cmp .cmdiv { position: absolute; left: 34px; top: 8px; bottom: 8px; width: 2px; background: rgba(255,255,255,0.3); transform-origin: 50% 50%; }
.cmp.v { flex-direction: column; }
.cmp.v .cmmid { width: auto; height: 34px; }
.cmp.v .cmdiv { left: 8px; right: 8px; top: 16px; bottom: auto; width: auto; height: 2px; }
.cmp.v .cmvs { display: none; }
.cmp.v .cmvv { font-size: 70px; }
.cmp .cmvs { position: absolute; left: 0; right: 0; top: 50%; margin-top: -18px; text-align: center; font-family: "OnyxMono"; font-weight: 600; font-size: 22px;
  letter-spacing: 0.1em; color: rgba(255,255,255,0.75); background: #111; line-height: 36px; }
"""
