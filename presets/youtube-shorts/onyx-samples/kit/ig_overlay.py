"""ig_overlay.py: the OVERLAY layer of an Instagram-look sample (README § 3-6 + LESSONS "Reference study 1") as a transparent
HyperFrames composition -> <job>/ig/hf-overlay/index.html, plus <job>/ig/work/sfx-cues.json (one sound per graphic entrance).

  python presets/youtube-shorts/onyx-samples/kit/ig_overlay.py projects/<job>
  cd projects/<job>/ig/hf-overlay && npx --yes hyperframes@0.8.16 render . --format mov --fps <fps> -o ../work/overlay.mov

Reads `<job>/ig/spec.json`:
  "fps", "frames",
  "captions": {"style": "box" | "pill" | "accent", "y": 1310 (fallback; each chunk's own "y" from ig_capy.py wins), "accent": "#CFAA5A",
               "chunks": [{"text": "Is it okay if I tell you", "start": s, "end": s, "hl": ["tell"]}]}   (from ig_captions.py)
      box    white rounded box, black sentence-case text
      darkbox white text on a near-black box with small corners (Chris Do's real house style, LESSONS reference study 3)
      pill   dark translucent pill, white text (Ali Abdaal's)
      accent white text with a soft shadow, the hl words in the accent colour (the pilot's)
      plain  text in "color" (e.g. a host's own caption colour, Rob Dial's yellow) with a dark glow and a soft radial scrim
             (legible over bright sky and white clothes, QA r1)
               optional for every style: "size" (px, default 52), "weight" (default 700), "color" (plain/accent text),
               "italic": true (Pomp's house style),
               "align": "left" + "x" (px) + "width" (px): a LEFT-aligned block that wraps into lines (Rich Roll's house
               style); "y" is then the block's top
  "cards": [{"t0": s, "t1": s, "kind": "title" | "chip" | "number" | "image" | "prompt", ...}]   graphics in the top band (y 260-760)
      title   {"text": "THE LOWBALL TEST", "sub": "optional small line"}                         rises in, fades out
              ("serif": true sets it in PT Serif Bold; "align": "left" + "x" (px) left-aligns it; "lines" [..] stacks lines)
      check   {"payee": "Zac Clark", "amount": "5,000.00", "words": "Five thousand and 00/100", "signature": "", "no": "1047"}
              a paper bank check (no bank's name or logo) that rises in, then the ink writes itself on (paper + pen sounds)
      chip    {"text": "Anchor first", "icon": "⚓"}                                              pops in
      number  {"from": 0, "to": 20000, "prefix": "$", "suffix": "", "label": "the final price", "box": true}  counts up
              ("box": a dark pill behind the digits, when they sit over busy picture)
      image   {"src": "ig/assets/x.png", "w": 760, "radius": 28, "label": "optional caption"}    pops in, soft shadow
      prompt  {"text": "What would you say?", "options": ["A  Take it", "B  Walk away"]}       participation card
      call    {"name": "Mom", "sub": "calling...", "initials": "M"}                                an incoming-call banner (vibrate sound)
      notify  {"app": "BANK", "title": "Wire transfer received", "body": "+$23,000.00", "time": "now"}   a phone notification (ding)
      label   {"lines": ["When A Nonprofit", "Lowballs You"]}   white boxes, black bold Title Case: the hook title held over the
              first seconds (Modern Wisdom, LESSONS reference study 3); rises in
      circles {"a": 1000, "b": 15000, "la": "$1,000", "lb": "$15,000", "sa": "their budget", "sb": "his fee", "text": "the gap"}
              a FULL-SCREEN near-black canvas (the voice keeps running): two thin white circles whose AREAS are in the ratio a:b,
              drawn on in turn ("tb": seconds after t0 for the second, default 0.9), small labels, one small line of type above,
              "cy" = the big circle's centre (default 880, keeps the labels above the captions), a dot orbiting it (Dan Koe-minimal, LESSONS reference study 3); a tick as each circle closes
      sheet   {"title": "one sheet, all the numbers", "rows": [["Field office", "212-555-0147"], ...], "hi": [[row, t, "#FFE45C"], ...]}
              a FULL-SCREEN dark canvas with a paper list (a phone sheet, a ledger); each "hi" lights a row at time t (a tick)
      chat    {"channel": "ftx-alameda", "note": "as described in court", "msgs": [[t, "Caroline", "C", "text"], ...]}
              a Slack-style message card; each message pops in at its t (a soft pop each). PARAPHRASE only, and say so in "note"
      tabs    {"file": "balance_sheet.xlsx", "tabs": ["Version 1", ...], "t_tabs": s, "step": 0.09, "pick": [i, t]}
              a spreadsheet window; the tabs pop in one by one from t_tabs; "pick" turns tab i red at t
      (label also takes "italic": true: Pomp's bold-italic title box)
      every card also takes "y" (top, px) to override its default slot
  "credit": "@thechrisdo"   small credit line above the captions (a prospect's condition: Rob Dial, Rollo); "credit_t0" (s) delays it
      (keep it out of the hook), "credit_y" (px) places it (default: 80 px above the captions),
      "credit_pill": true backs it with a soft dark pill (when it sits over busy picture, e.g. a mic logo)
Motion: type and cards rise 40 px under a mask (power3.out 0.45 s), objects pop 0.85 → 1, exits fade 0.25 s; every step on
the frame grid a quarter frame early.
"""
import json, math, os, shutil, sys

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8")
    except Exception:
        pass

KIT = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(KIT, "..", "..", "..", ".."))
W, H = 1080, 1920
SLOTS = {"chat": 300, "tabs": 300, "sheet": 0, "check": 300, "title": 300, "chip": 420, "number": 330, "image": 300, "prompt": 300, "call": 280, "notify": 280, "label": 300, "circles": 0}


def esc(t):
    return str(t).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def main():
    job = os.path.abspath(sys.argv[1])
    spec = json.load(open(os.path.join(job, "ig", "spec.json"), encoding="utf-8"))
    fps = spec["fps"]
    dur = spec["frames"] / fps
    q = lambda t: round(max(0.0, round(t * fps) - 0.25) / fps, 5)          # a quarter frame before the frame boundary
    cap = spec.get("captions", {})
    style, cy, accent = cap.get("style", "box"), cap.get("y", 1310), cap.get("accent", "#CFAA5A")
    csize, cweight, ccolor = cap.get("size", 52), cap.get("weight", 700), cap.get("color", "#FFFFFF")
    out = os.path.join(job, "ig", "hf-overlay")
    os.makedirs(os.path.join(out, "fonts"), exist_ok=True)
    os.makedirs(os.path.join(out, "vendor"), exist_ok=True)
    os.makedirs(os.path.join(out, "assets"), exist_ok=True)
    for fn in ("Inter-Regular.otf", "Inter-Bold.otf", "Inter-Black.otf", "PTSerif-Bold.ttf", "PlayfairDisplay-Italic-VF.ttf"):
        shutil.copy(os.path.join(REPO, "assets", "fonts", fn), os.path.join(out, "fonts", fn))
    shutil.copy(os.path.join(REPO, "presets", "youtube-shorts", "onyx-samples-youtube", "kit", "vendor", "gsap.min.js"), os.path.join(out, "vendor", "gsap.min.js"))

    # ---- captions
    cap_html, cap_js = [], []
    for i, c in enumerate(cap.get("chunks", [])):
        words = []
        for w in c["text"].replace("'", "’").split(" "):        # typographic apostrophes, matching the title
            P = ".,!?;:\"“”‘’'"                                      # punctuation never blocks a highlight ("AMERICAN." == "AMERICAN"; QA 2026-10-06)
            hl = any(w.strip(P).lower() == h.strip(P).lower() for h in c.get("hl", []))
            words.append(f'<span class="w{" hl" if hl else ""}">{esc(w)}</span>')
        ytop = f' style="top:{int(c["y"])}px"' if "y" in c else ""          # per-chunk y from ig_capy.py: just under the speaker's lips
        cap_html.append(f'<div id="c{i}" class="cap {style}"{ytop}><span class="inner">{" ".join(words)}</span></div>')
        t_in, t_out = c.get("show", c["start"]), c.get("hide", c["end"])          # ig_capy.py snaps a start onto a cut 1-2 frames later
        moves = "".join(f' tl.set("#c{i}", {{top: {int(y)}}}, {q(n / fps)});' for n, y in c.get("moves", []))   # new shot, new lip line, ON the cut
        cap_js.append(f'tl.set("#c{i}", {{autoAlpha: 1}}, {q(t_in)}); tl.fromTo("#c{i} .inner", {{y: 14}}, {{y: 0, duration: 0.16, ease: "power2.out"}}, {q(t_in)}); '
                      f'tl.set("#c{i}", {{autoAlpha: 0}}, {q(t_out)});{moves}')

    # ---- cards
    card_html, card_js, sfx = [], [], []
    for i, k in enumerate(spec.get("cards", [])):
        kind, y, cid = k["kind"], k.get("y", SLOTS.get(k["kind"], 320)), f"k{i}"
        if kind == "title":
            tcls = "title serif" if k.get("serif") else "title"
            inner = "".join(f'<div class="mask"><div class="rise {tcls}">{esc(l)}</div></div>' for l in k.get("lines", [k.get("text", "")])) + (f'<div class="mask"><div class="rise sub">{esc(k["sub"])}</div></div>' if k.get("sub") else "")
            card_js.append(f'tl.set("#{cid}", {{autoAlpha: 1}}, {q(k["t0"])}); tl.fromTo("#{cid} .rise", {{yPercent: 110}}, {{yPercent: 0, duration: 0.45, ease: "power3.out", stagger: 0.06}}, {q(k["t0"])});')
        elif kind == "chip":
            ico = f'<span class="ico">{esc(k["icon"])}</span>' if k.get("icon") else ""          # no empty icon slot (it pushed the text off-centre)
            inner = f'<div class="chip">{ico}{esc(k["text"])}</div>'
            card_js.append(f'tl.set("#{cid}", {{autoAlpha: 1}}, {q(k["t0"])}); tl.fromTo("#{cid} .chip", {{scale: 0.85, opacity: 0}}, {{scale: 1, opacity: 1, duration: 0.3, ease: "back.out(2)"}}, {q(k["t0"])});')
        elif kind == "number":
            inner = (f'<div class="{"numbox" if k.get("box") else ""}"><div class="num"><span class="pre">{esc(k.get("prefix", ""))}</span><span class="val" id="{cid}v">{k.get("from", 0):,}</span>'
                     f'<span class="suf">{esc(k.get("suffix", ""))}</span></div></div>' + (f'<div class="numlab">{esc(k["label"])}</div>' if k.get("label") else ""))
            d = min(0.9, max(0.4, (k["t1"] - k["t0"]) * 0.4))
            card_js.append(f'tl.set("#{cid}", {{autoAlpha: 1}}, {q(k["t0"])}); tl.fromTo("#{cid}", {{y: 40}}, {{y: 0, duration: 0.45, ease: "power3.out"}}, {q(k["t0"])}); '
                           f'(function(){{ const o = {{v: {k.get("from", 0)}}}; tl.to(o, {{v: {k["to"]}, duration: {d:.2f}, ease: "power2.out", onUpdate: () => {{ document.getElementById("{cid}v").textContent = Math.round(o.v).toLocaleString("en-US"); }}}}, {q(k["t0"] + 0.1)}); }})();')
            sfx.append(dict(t=round(k["t0"] + 0.1 + 0.63 * d, 3), kind="tick"))     # power2.out reaches the final value at ~63 % of d (QA 2026-10-06)
        elif kind == "image":
            src = k["src"]
            dst = os.path.join(out, "assets", os.path.basename(src))
            shutil.copy(os.path.join(job, src), dst)
            inner = (f'<div class="imgcard" style="width:{k.get("w", 760)}px;border-radius:{k.get("radius", 28)}px"><img src="assets/{os.path.basename(src)}" alt=""></div>'
                     + (f'<div class="imglab">{esc(k["label"])}</div>' if k.get("label") else ""))
            card_js.append(f'tl.set("#{cid}", {{autoAlpha: 1}}, {q(k["t0"])}); tl.fromTo("#{cid} .imgcard", {{scale: 0.88, y: 30, opacity: 0}}, {{scale: 1, y: 0, opacity: 1, duration: 0.4, ease: "back.out(1.6)"}}, {q(k["t0"])});')
        elif kind == "prompt":
            opts = "".join(f'<div class="opt">{esc(o)}</div>' for o in k.get("options", []))
            inner = f'<div class="prompt"><div class="pq">{esc(k["text"])}</div>{opts}</div>'
            card_js.append(f'tl.set("#{cid}", {{autoAlpha: 1}}, {q(k["t0"])}); tl.fromTo("#{cid} .prompt", {{y: 40, opacity: 0}}, {{y: 0, opacity: 1, duration: 0.45, ease: "power3.out"}}, {q(k["t0"])}); '
                           f'tl.fromTo("#{cid} .opt", {{x: -30, opacity: 0}}, {{x: 0, opacity: 1, duration: 0.3, ease: "power2.out", stagger: 0.12}}, {q(k["t0"] + 0.25)});')
        elif kind == "call":
            ini = esc(k.get("initials", k["name"][:1]))
            inner = (f'<div class="call"><div class="av">{ini}</div><div class="ctext"><div class="cname">{esc(k["name"])}</div>'
                     f'<div class="csub">{esc(k.get("sub", "calling..."))}</div></div>'
                     f'<div class="cbtn dec"><svg viewBox="0 0 24 24"><path d="M3 15c5-5 13-5 18 0l-2.4 2.4c-.5.5-1.3.5-1.8.1l-2-1.6c-.4-.3-.6-.8-.5-1.3l.3-1.6c-2-.8-4.2-.8-6.2 0l.3 1.6c.1.5-.1 1-.5 1.3l-2 1.6c-.5.4-1.3.4-1.8-.1z"/></svg></div>'
                     f'<div class="cbtn acc"><svg viewBox="0 0 24 24"><path d="M6.6 10.8c1.4 2.8 3.8 5.1 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1C10.6 21 3 13.4 3 4c0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.3.2 2.5.6 3.6.1.3 0 .7-.2 1z"/></svg></div></div>')
            reps = max(1, int((k["t1"] - k["t0"] - 0.5) / 0.35))
            card_js.append(f'tl.set("#{cid}", {{autoAlpha: 1}}, {q(k["t0"])}); tl.fromTo("#{cid} .call", {{y: -60, opacity: 0}}, {{y: 0, opacity: 1, duration: 0.45, ease: "power3.out"}}, {q(k["t0"])}); '
                           f'tl.fromTo("#{cid} .acc", {{scale: 1}}, {{scale: 1.12, duration: 0.35, ease: "sine.inOut", yoyo: true, repeat: {reps}}}, {q(k["t0"] + 0.45)});')
            sfx.append(dict(t=round(k["t0"] + 0.05, 3), kind="vibrate"))
        elif kind == "notify":
            inner = (f'<div class="noti"><div class="nhead"><div class="nico">$</div><div class="napp">{esc(k.get("app", "BANK"))}</div>'
                     f'<div class="ntime">{esc(k.get("time", "now"))}</div></div><div class="ntitle">{esc(k["title"])}</div>'
                     f'<div class="nbody">{esc(k.get("body", ""))}</div></div>')
            card_js.append(f'tl.set("#{cid}", {{autoAlpha: 1}}, {q(k["t0"])}); tl.fromTo("#{cid} .noti", {{y: -60, opacity: 0, scale: 0.96}}, {{y: 0, opacity: 1, scale: 1, duration: 0.45, ease: "back.out(1.4)"}}, {q(k["t0"])});')
            sfx.append(dict(t=round(k["t0"] + 0.05, 3), kind="notify"))
        elif kind == "label":
            inner = "".join(f'<div class="mask"><div class="rise lab{" it" if k.get("italic") else ""}">{esc(l)}</div></div>' for l in k["lines"])
            card_js.append(f'tl.set("#{cid}", {{autoAlpha: 1}}, {q(k["t0"])}); tl.fromTo("#{cid} .rise", {{yPercent: 110}}, {{yPercent: 0, duration: 0.45, ease: "power3.out", stagger: 0.07}}, {q(k["t0"])});')
        elif kind == "circles":
            rb = 300.0; ra = rb * math.sqrt(k["a"] / k["b"])
            cyb = k.get("cy", 880); cya = cyb + rb - ra                      # both circles stand on one baseline
            xa, xb = 250, 640
            tb = k.get("tb", 0.9)
            circ = lambda r: 2 * math.pi * r
            inner = (f'<div class="gfx"><div class="gtext" style="top:{cyb - rb - 150:.0f}px">{esc(k.get("text", ""))}</div>'
                     f'<svg class="gsvg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">'
                     f'<circle id="{cid}a" cx="{xa}" cy="{cya:.1f}" r="{ra:.1f}" fill="none" stroke="#FFFFFF" stroke-width="3" '
                     f'stroke-dasharray="{circ(ra):.1f}" stroke-dashoffset="{circ(ra):.1f}" transform="rotate(-90 {xa} {cya:.1f})"/>'
                     f'<circle id="{cid}b" cx="{xb}" cy="{cyb}" r="{rb:.1f}" fill="none" stroke="#FFFFFF" stroke-width="3" '
                     f'stroke-dasharray="{circ(rb):.1f}" stroke-dashoffset="{circ(rb):.1f}" transform="rotate(-90 {xb} {cyb})"/>'
                     f'<g id="{cid}o"><circle cx="{xb}" cy="{cyb - rb:.1f}" r="9" fill="#FFFFFF"/></g></svg>'
                     f'<div class="glab" id="{cid}la" style="left:{xa - 200}px;top:{cyb + rb + 40:.0f}px">{esc(k["la"])}<span>{esc(k.get("sa", ""))}</span></div>'
                     f'<div class="glab" id="{cid}lb" style="left:{xb - 200}px;top:{cyb + rb + 40:.0f}px">{esc(k["lb"])}<span>{esc(k.get("sb", ""))}</span></div></div>')
            orbit = max(0.5, k["t1"] - k["t0"] - tb - 0.6)
            card_js.append(f'tl.set("#{cid}", {{autoAlpha: 1}}, {q(k["t0"])}); tl.fromTo("#{cid} .gfx", {{opacity: 0}}, {{opacity: 1, duration: 0.25, ease: "power1.out"}}, {q(k["t0"])}); '
                           f'tl.fromTo("#{cid} .gtext", {{y: 30, opacity: 0}}, {{y: 0, opacity: 1, duration: 0.45, ease: "power3.out"}}, {q(k["t0"] + 0.1)}); '
                           f'tl.to("#{cid}a", {{attr: {{"stroke-dashoffset": 0}}, duration: 0.5, ease: "power2.inOut"}}, {q(k["t0"] + 0.2)}); '
                           f'tl.fromTo("#{cid}la", {{y: 20, opacity: 0}}, {{y: 0, opacity: 1, duration: 0.35, ease: "power3.out"}}, {q(k["t0"] + 0.5)}); '
                           f'tl.to("#{cid}b", {{attr: {{"stroke-dashoffset": 0}}, duration: 0.6, ease: "power2.inOut"}}, {q(k["t0"] + tb)}); '
                           f'tl.fromTo("#{cid}lb", {{y: 20, opacity: 0}}, {{y: 0, opacity: 1, duration: 0.35, ease: "power3.out"}}, {q(k["t0"] + tb + 0.35)}); '
                           f'tl.fromTo("#{cid}o", {{opacity: 0}}, {{opacity: 1, duration: 0.2}}, {q(k["t0"] + tb + 0.6)}); '
                           f'tl.fromTo("#{cid}o", {{rotation: 0}}, {{rotation: {360 * orbit / 4.0:.1f}, svgOrigin: "{xb} {cyb}", duration: {orbit:.2f}, ease: "none"}}, {q(k["t0"] + tb + 0.6)});')
            sfx += [dict(t=round(k["t0"] + 0.7, 3), kind="tick"), dict(t=round(k["t0"] + tb + 0.6, 3), kind="tick")]
        elif kind == "check":
            inner = (f'<div class="chk"><div class="chk-top"><span class="chk-no">{("No. " + esc(k["no"])) if k.get("no") else ""}</span><span class="chk-date">{esc(k.get("date", ""))}</span></div>'
                     f'<div class="chk-row"><span class="chk-lab">PAY TO THE<br>ORDER OF</span><span class="chk-pay"><span class="ink" id="{cid}p">{esc(k["payee"])}</span></span>'
                     f'<span class="chk-amt">$ <span class="ink" id="{cid}a">{esc(k["amount"])}</span></span></div>'
                     f'<div class="chk-words"><span class="ink" id="{cid}w">{esc(k.get("words", ""))}</span><span class="chk-dol">DOLLARS</span></div>'
                     f'<div class="chk-bot"><span class="chk-memo">MEMO</span><span class="chk-sig"><span class="ink" id="{cid}s">{esc(k.get("signature", ""))}</span></span></div></div>')
            card_js.append(f'tl.set("#{cid}", {{autoAlpha: 1}}, {q(k["t0"])}); tl.fromTo("#{cid} .chk", {{y: 50, opacity: 0, rotation: -2}}, {{y: 0, opacity: 1, rotation: -1, duration: 0.45, ease: "power3.out"}}, {q(k["t0"])}); '
                           + " ".join(f'tl.fromTo("#{cid}{x}", {{clipPath: "inset(0 100% 0 0)"}}, {{clipPath: "inset(0 0% 0 0)", duration: {d}, ease: "power1.inOut"}}, {q(k["t0"] + o)});'
                                      for x, o, d in (("p", 0.35, 0.45), ("a", 0.85, 0.4), ("w", 1.15, 0.5), ("s", 1.55, 0.35))))
            sfx += [dict(t=round(k["t0"], 3), kind="paper"), dict(t=round(k["t0"] + 0.35, 3), kind="pen")]
        elif kind == "sheet":
            rows = "".join(f'<div class="srow" id="{cid}r{j}"><span class="slab">{esc(a)}</span><span class="sdots"></span><span class="snum">{esc(b)}</span></div>'
                           for j, (a, b) in enumerate(k["rows"]))
            inner = (f'<div class="gfx"><div class="sheet"><div class="shead">{esc(k.get("title", ""))}</div>{rows}</div></div>')
            card_js.append(f'tl.set("#{cid}", {{autoAlpha: 1}}, {q(k["t0"])}); tl.fromTo("#{cid} .gfx", {{opacity: 0}}, {{opacity: 1, duration: 0.25, ease: "power1.out"}}, {q(k["t0"])}); '
                           f'tl.fromTo("#{cid} .sheet", {{y: 80, rotation: -3, opacity: 0}}, {{y: 0, rotation: -1.5, opacity: 1, duration: 0.5, ease: "power3.out"}}, {q(k["t0"] + 0.05)}); '
                           f'tl.fromTo("#{cid} .srow", {{opacity: 0, x: -20}}, {{opacity: 1, x: 0, duration: 0.25, ease: "power2.out", stagger: 0.06}}, {q(k["t0"] + 0.3)});')
            for j, t, col in k.get("hi", []):
                card_js.append(f'tl.to("#{cid}r{j}", {{backgroundColor: "{col}", duration: 0.2, ease: "power1.out"}}, {q(t)}); '
                               f'tl.fromTo("#{cid}r{j}", {{scale: 1}}, {{scale: 1.04, duration: 0.18, ease: "power2.out", yoyo: true, repeat: 1}}, {q(t)});')
                sfx.append(dict(t=round(t, 3), kind="tick"))
        elif kind == "chat":
            msgs = "".join(f'<div class="cmsg" id="{cid}m{j}"><div class="cav">{esc(m[2])}</div><div class="cbody"><div class="cname2">{esc(m[1])}</div>'
                           f'<div class="ctext2">{esc(m[3])}</div></div></div>' for j, m in enumerate(k["msgs"]))
            inner = f'<div class="chat"><div class="chead"><span class="chash">#</span>{esc(k.get("channel", "general"))}<span class="cnote">{esc(k.get("note", ""))}</span></div>{msgs}</div>'
            card_js.append(f'tl.set("#{cid}", {{autoAlpha: 1}}, {q(k["t0"])}); tl.fromTo("#{cid} .chat", {{y: 50, opacity: 0}}, {{y: 0, opacity: 1, duration: 0.45, ease: "power3.out"}}, {q(k["t0"])}); '
                           + " ".join(f'tl.fromTo("#{cid}m{j}", {{y: 24, opacity: 0}}, {{y: 0, opacity: 1, duration: 0.3, ease: "power2.out"}}, {q(m[0])});' for j, m in enumerate(k["msgs"])))
            sfx += [dict(t=round(m[0], 3), kind="pop") for m in k["msgs"]]
        elif kind == "tabs":
            tabs = "".join(f'<div class="xtab" id="{cid}t{j}">{esc(t)}</div>' for j, t in enumerate(k["tabs"]))
            grid = "".join('<div class="xrow">' + "".join('<div class="xcell"></div>' for _ in range(5)) + '</div>' for _ in range(k.get("rows", 7)))
            inner = (f'<div class="xls"><div class="xbar"><span class="xdot"></span><span class="xdot"></span><span class="xdot"></span><span class="xname">{esc(k.get("file", "spreadsheet.xlsx"))}</span></div>'
                     f'<div class="xgrid">{grid}</div><div class="xtabs">{tabs}</div></div>')
            te = k.get("t_tabs", k["t0"] + 0.4); step = k.get("step", 0.09)
            card_js.append(f'tl.set("#{cid}", {{autoAlpha: 1}}, {q(k["t0"])}); tl.fromTo("#{cid} .xls", {{y: 50, opacity: 0}}, {{y: 0, opacity: 1, duration: 0.45, ease: "power3.out"}}, {q(k["t0"])}); '
                           f'tl.fromTo("#{cid} .xtab", {{scale: 0.6, opacity: 0}}, {{scale: 1, opacity: 1, duration: 0.18, ease: "back.out(2)", stagger: {step}}}, {q(te)});')
            sfx += [dict(t=round(te + j * step, 3), kind="tick") for j in range(0, len(k["tabs"]), 2)]
            if k.get("pick") is not None:
                card_js.append(f'tl.to("#{cid}t{k["pick"][0]}", {{backgroundColor: "#E5484D", color: "#FFFFFF", duration: 0.2}}, {q(k["pick"][1])});')
                sfx.append(dict(t=round(k["pick"][1], 3), kind="tick"))
        else:
            sys.exit(f"ig_overlay: unknown card kind {kind}")
        lstyle = f'left:{k.get("x", 90)}px;width:{W - 2 * k.get("x", 90)}px;text-align:left;' if k.get("align") == "left" else ""
        card_html.append(f'<div id="{cid}" class="card{" full" if kind in ("circles", "sheet") else ""}" style="top:{y}px;{lstyle}" data-layout-allow-overflow>{inner}</div>')
        card_js.append(f'tl.to("#{cid}", {{autoAlpha: 0, duration: 0.25, ease: "power1.in"}}, {q(max(k["t0"] + 0.3, k["t1"] - 0.25))});')
        if kind not in ("call", "notify"):
            sfx.append(dict(t=round(k["t0"], 3), kind="pop" if kind in ("chip", "image") else "whoosh"))

    cap_align_css = ".cap .inner { font-style: italic; }\n" if cap.get("italic") else ""
    if cap.get("align") == "left":
        cap_align_css += (f'.cap {{ left: {cap.get("x", 90)}px; width: {cap.get("width", 600)}px; text-align: left; }}\n'
                         f'.cap .inner {{ display: inline; -webkit-box-decoration-break: clone; box-decoration-break: clone; line-height: 1.14; }}\n'
                         f'.cap.plain .inner {{ padding: 0; background: none; }}')
    credit = spec.get("credit")
    credit_html = (f'<div id="credit"><span class="{"pill" if spec.get("credit_pill") else ""}">{esc(credit)}</span></div>') if credit else ""
    credit_y = spec.get("credit_y", cy - 80)
    if credit and spec.get("credit_t0"):
        card_js.append(f'tl.set("#credit", {{autoAlpha: 0}}, 0); tl.to("#credit", {{autoAlpha: 1, duration: 0.3}}, {q(spec["credit_t0"])});')
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width={W}, height={H}" />
<style>
@font-face {{ font-family: "Inter"; src: url("fonts/Inter-Regular.otf"); font-weight: 400; }}
@font-face {{ font-family: "Inter"; src: url("fonts/Inter-Bold.otf"); font-weight: 700; }}
@font-face {{ font-family: "Inter"; src: url("fonts/Inter-Black.otf"); font-weight: 900; }}
@font-face {{ font-family: "PTSerif"; src: url("fonts/PTSerif-Bold.ttf"); font-weight: 700; }}
@font-face {{ font-family: "Playfair"; src: url("fonts/PlayfairDisplay-Italic-VF.ttf"); font-style: italic; }}
html, body {{ margin: 0; background: transparent; }}
#root {{ position: relative; width: {W}px; height: {H}px; overflow: hidden; background: transparent; font-family: "Inter", sans-serif; }}
.cap {{ position: absolute; left: 60px; width: 960px; top: {cy}px; text-align: center; visibility: hidden; }}
.cap .inner {{ display: inline-block; font-size: {csize}px; line-height: 1.18; font-weight: {cweight}; letter-spacing: -0.01em; }}
.cap.box .inner {{ background: #FFFFFF; color: #0B0B0B; padding: 10px 22px 12px; border-radius: 14px; box-shadow: 0 6px 18px rgba(0,0,0,0.25); }}
.cap.darkbox .inner {{ background: rgba(8,8,8,0.9); color: #FFFFFF; padding: 8px 20px 11px; border-radius: 6px; font-weight: 600; }}
.cap.pill .inner {{ background: rgba(20,20,20,0.62); color: #FFFFFF; padding: 10px 24px 12px; border-radius: 40px; font-weight: 600; }}
.cap.accent .inner {{ color: {ccolor}; text-shadow: 0 3px 12px rgba(0,0,0,0.65), 0 1px 2px rgba(0,0,0,0.8); }}
.cap.plain .inner {{ color: {ccolor}; text-shadow: 0 0 14px rgba(0,0,0,0.85), 0 0 4px rgba(0,0,0,0.9), 0 2px 3px rgba(0,0,0,0.95);
  padding: 18px 40px 22px; background: radial-gradient(closest-side, rgba(0,0,0,0.42), rgba(0,0,0,0.26) 55%, rgba(0,0,0,0) 100%); }}
.cap .hl {{ color: {accent}; }}
{cap_align_css}
.cap.box .hl {{ color: #0B0B0B; background: {accent}; border-radius: 6px; padding: 0 6px; }}
.card {{ position: absolute; left: 0; width: {W}px; text-align: center; visibility: hidden; }}
.mask {{ overflow: hidden; padding: 4px 0 8px; }}
.lab {{ background: #FFFFFF; color: #0B0B0B; font-size: 66px; font-weight: 900; letter-spacing: -0.015em; line-height: 1.08;
  padding: 6px 22px 10px; border-radius: 10px; }}
.card.full {{ height: {H}px; }}
.lab.it {{ font-style: italic; }}
.chat {{ display: inline-block; width: 900px; box-sizing: border-box; text-align: left; background: #FFFFFF; color: #1D1C1D; border-radius: 22px;
  padding: 24px 30px 18px; box-shadow: 0 22px 60px rgba(0,0,0,0.5); }}
.chead {{ font-size: 30px; font-weight: 900; padding-bottom: 14px; border-bottom: 2px solid #EAEAEA; margin-bottom: 8px; }}
.chash {{ color: #9A9A9A; margin-right: 4px; }}
.cnote {{ float: right; font-size: 28px; font-weight: 400; color: #555555; padding-top: 6px; }}
.cmsg {{ display: flex; gap: 18px; padding: 12px 0; }}
.cav {{ width: 64px; height: 64px; border-radius: 12px; background: #4A154B; color: #FFFFFF; font-size: 32px; font-weight: 900; display: flex;
  align-items: center; justify-content: center; flex: none; }}
.cname2 {{ font-size: 32px; font-weight: 900; }}
.ctext2 {{ font-size: 38px; font-weight: 400; line-height: 1.25; margin-top: 2px; }}
.xls {{ display: inline-block; width: 900px; box-sizing: border-box; text-align: left; background: #FFFFFF; border-radius: 16px; overflow: hidden;
  box-shadow: 0 22px 60px rgba(0,0,0,0.5); }}
.xbar {{ background: #1F7A47; padding: 14px 20px; display: flex; align-items: center; gap: 10px; }}
.xdot {{ width: 16px; height: 16px; border-radius: 8px; background: rgba(255,255,255,0.55); }}
.xname {{ color: #FFFFFF; font-size: 32px; font-weight: 700; margin-left: 12px; }}
.xgrid {{ padding: 8px 0; }}
.xrow {{ display: flex; }}
.xcell {{ flex: 1; height: 38px; border-right: 1px solid #E3E3E3; border-bottom: 1px solid #E3E3E3; }}
.xtabs {{ display: flex; flex-wrap: wrap; gap: 8px; padding: 14px 16px 18px; background: #F3F3F3; border-top: 2px solid #DADADA; }}
.xtab {{ font-size: 30px; font-weight: 700; padding: 8px 14px; border-radius: 8px; background: #FFFFFF; color: #1F1F1F; border: 1px solid #CFCFCF; }}
.gfx {{ position: absolute; left: 0; top: 0; width: {W}px; height: {H}px; background: #050505; }}
.gtext {{ position: absolute; left: 0; width: {W}px; top: 560px; text-align: center; font-size: 48px; font-weight: 400; color: rgba(255,255,255,0.86);
  letter-spacing: 0.01em; }}
.gsvg {{ position: absolute; left: 0; top: 0; }}
.glab {{ position: absolute; width: 400px; text-align: center; font-size: 54px; font-weight: 700; color: #FFFFFF; }}
.glab span {{ display: block; font-size: 36px; font-weight: 400; color: rgba(255,255,255,0.6); margin-top: 6px; }}
.rise {{ display: inline-block; }}
.title.serif {{ font-family: "PTSerif", serif; font-weight: 700; letter-spacing: -0.01em; line-height: 1.04; }}
.chk {{ display: inline-block; width: 900px; box-sizing: border-box; padding: 26px 34px 30px; border-radius: 14px; text-align: left; color: #1D2A3A;
  background: repeating-linear-gradient(135deg, rgba(120,150,170,0.07) 0 2px, rgba(0,0,0,0) 2px 9px), linear-gradient(180deg, #F3F1EA, #E7EDE9);
  box-shadow: 0 22px 60px rgba(0,0,0,0.5); font-family: "Inter", sans-serif; }}
.chk-top {{ display: flex; justify-content: space-between; font-size: 24px; font-weight: 700; letter-spacing: 0.08em; color: rgba(29,42,58,0.6); margin-bottom: 22px; }}
.chk-row {{ display: flex; align-items: flex-end; gap: 18px; }}
.chk-lab {{ font-size: 20px; font-weight: 700; letter-spacing: 0.06em; line-height: 1.15; color: rgba(29,42,58,0.7); flex: none; }}
.chk-pay {{ flex: 1; border-bottom: 2px solid rgba(29,42,58,0.55); padding-bottom: 2px; }}
.chk-amt {{ flex: none; border: 2px solid rgba(29,42,58,0.55); border-radius: 6px; padding: 4px 14px; font-size: 40px; font-weight: 700; }}
.chk-words {{ display: flex; align-items: flex-end; gap: 14px; margin-top: 26px; border-bottom: 2px solid rgba(29,42,58,0.55); padding-bottom: 2px; }}
.chk-words .ink {{ flex: 1; }}
.chk-dol {{ font-size: 20px; font-weight: 700; letter-spacing: 0.06em; color: rgba(29,42,58,0.7); }}
.chk-bot {{ display: flex; justify-content: space-between; align-items: flex-end; margin-top: 34px; }}
.chk-memo {{ font-size: 20px; font-weight: 700; letter-spacing: 0.06em; color: rgba(29,42,58,0.7); border-bottom: 2px solid rgba(29,42,58,0.4); width: 330px; padding-bottom: 4px; }}
.chk-sig {{ width: 380px; border-bottom: 2px solid rgba(29,42,58,0.55); text-align: center; min-height: 52px; }}
.chk .ink {{ display: inline-block; font-family: "Playfair", serif; font-style: italic; font-size: 46px; color: #1B3D8F; line-height: 1.1; }}
.chk-amt .ink {{ font-family: "Inter", sans-serif; font-style: normal; font-size: 40px; font-weight: 700; color: #1B3D8F; }}
.sheet {{ position: absolute; left: 110px; top: 470px; width: 860px; box-sizing: border-box; padding: 40px 44px 46px; border-radius: 10px;
  background: #F5F3EC; color: #141414; box-shadow: 0 30px 80px rgba(0,0,0,0.6); text-align: left; }}
.shead {{ font-size: 30px; font-weight: 700; letter-spacing: 0.14em; text-transform: uppercase; color: rgba(20,20,20,0.55); margin-bottom: 22px; }}
.srow {{ display: flex; align-items: baseline; gap: 14px; font-size: 44px; font-weight: 700; padding: 12px 16px; margin: 0 -16px; border-radius: 8px;
  background: rgba(255,255,255,0); border-bottom: 2px solid rgba(20,20,20,0.08); }}
.srow .slab {{ flex: none; }}
.srow .sdots {{ flex: 1; border-bottom: 3px dotted rgba(20,20,20,0.3); transform: translateY(-8px); }}
.srow .snum {{ flex: none; font-weight: 400; font-variant-numeric: tabular-nums; letter-spacing: 0.02em; }}
.title {{ font-size: 88px; font-weight: 900; letter-spacing: -0.02em; color: #FFFFFF; text-shadow: 0 6px 24px rgba(0,0,0,0.45); line-height: 1.0; }}
.sub {{ font-size: 40px; font-weight: 700; color: rgba(255,255,255,0.86); text-shadow: 0 4px 16px rgba(0,0,0,0.5); }}
.chip {{ display: inline-flex; align-items: center; gap: 16px; background: #FFFFFF; color: #0B0B0B; font-size: 48px; font-weight: 800;
  padding: 16px 30px; border-radius: 60px; box-shadow: 0 10px 30px rgba(0,0,0,0.3); }}
.chip .ico {{ font-size: 52px; }}
.num {{ font-size: 150px; font-weight: 900; color: #FFFFFF; letter-spacing: -0.03em; text-shadow: 0 8px 30px rgba(0,0,0,0.5); line-height: 1; }}
.numbox .num {{ display: inline-block; padding: 18px 44px 24px; border-radius: 40px; background: rgba(12,12,12,0.98); }}
.numlab {{ font-size: 40px; font-weight: 700; color: rgba(255,255,255,0.9); margin-top: 10px; text-shadow: 0 4px 16px rgba(0,0,0,0.5); }}
.imgcard {{ display: inline-block; overflow: hidden; box-shadow: 0 18px 50px rgba(0,0,0,0.45); background: #fff; }}
.imgcard img {{ display: block; width: 100%; height: auto; }}
.imglab {{ font-size: 36px; font-weight: 700; color: #FFFFFF; margin-top: 14px; text-shadow: 0 4px 16px rgba(0,0,0,0.6); }}
.prompt {{ display: inline-block; text-align: left; background: #FFFFFF; color: #0B0B0B; border-radius: 28px; padding: 30px 38px; box-shadow: 0 18px 50px rgba(0,0,0,0.35); }}
.pq {{ font-size: 50px; font-weight: 900; margin-bottom: 18px; }}
.opt {{ font-size: 42px; font-weight: 700; padding: 12px 18px; margin-top: 10px; border-radius: 16px; background: #F1F1F1; }}
.call {{ display: inline-flex; align-items: center; gap: 26px; width: 860px; box-sizing: border-box; padding: 26px 30px; border-radius: 44px;
  background: rgba(28,28,30,0.97); box-shadow: 0 18px 50px rgba(0,0,0,0.45); text-align: left; }}
.call .av {{ width: 104px; height: 104px; border-radius: 52px; background: linear-gradient(180deg, #A3A8B4, #7D8290); color: #FFFFFF;
  font-size: 50px; font-weight: 700; display: flex; align-items: center; justify-content: center; flex: none; }}
.call .ctext {{ flex: 1; min-width: 0; }}
.call .cname {{ font-size: 46px; font-weight: 700; color: #FFFFFF; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }}
.call .csub {{ font-size: 32px; font-weight: 400; color: rgba(235,235,245,0.6); margin-top: 4px; }}
.call .cbtn {{ width: 96px; height: 96px; border-radius: 48px; display: flex; align-items: center; justify-content: center; flex: none; }}
.call .cbtn svg {{ width: 52px; height: 52px; fill: #FFFFFF; }}
.call .dec {{ background: #FF3B30; }}
.call .acc {{ background: #34C759; }}
.noti {{ display: inline-block; width: 860px; box-sizing: border-box; padding: 26px 32px 30px; border-radius: 40px; text-align: left;
  background: rgba(246,246,248,0.96); box-shadow: 0 18px 50px rgba(0,0,0,0.4); color: #0B0B0B; }}
.noti .nhead {{ display: flex; align-items: center; gap: 16px; margin-bottom: 12px; }}
.noti .nico {{ width: 56px; height: 56px; border-radius: 14px; background: linear-gradient(180deg, #33C76A, #1E9E4E); color: #FFFFFF;
  font-size: 38px; font-weight: 900; display: flex; align-items: center; justify-content: center; }}
.noti .napp {{ font-size: 30px; font-weight: 700; letter-spacing: 0.06em; color: rgba(60,60,67,0.75); flex: 1; }}
.noti .ntime {{ font-size: 28px; color: rgba(60,60,67,0.6); }}
.noti .ntitle {{ font-size: 42px; font-weight: 700; }}
.noti .nbody {{ font-size: 56px; font-weight: 900; color: #1E9E4E; margin-top: 6px; letter-spacing: -0.01em; }}
#credit {{ position: absolute; left: 0; width: {W}px; top: {credit_y}px; text-align: center; font-size: 32px; font-weight: 700;
  color: rgba(255,255,255,0.78); text-shadow: 0 2px 8px rgba(0,0,0,0.6); }}
#credit .pill {{ display: inline-block; padding: 6px 18px 8px; border-radius: 20px; background: rgba(0,0,0,0.42); color: rgba(255,255,255,0.88); }}
</style>
</head>
<body>
<div id="root" data-composition-id="onyx-ig-overlay" data-start="0" data-width="{W}" data-height="{H}" data-duration="{dur:.4f}" data-fps="{fps}">
  {''.join(card_html)}
  {''.join(cap_html)}
  {credit_html}
</div>
<script src="vendor/gsap.min.js"></script>
<script>
(function () {{
  window.__timelines = window.__timelines || {{}};
  const COMP = "onyx-ig-overlay";
  const tl = gsap.timeline({{ paused: true }});
  {chr(10).join(cap_js)}
  {chr(10).join(card_js)}
  tl.set({{}}, {{}}, {dur:.4f});
  window.__timelines[COMP] = tl;
}})();
</script>
</body>
</html>
"""
    open(os.path.join(out, "index.html"), "w", encoding="utf-8").write(html)
    os.makedirs(os.path.join(job, "ig", "work"), exist_ok=True)
    json.dump(sorted(sfx, key=lambda s: s["t"]), open(os.path.join(job, "ig", "work", "sfx-cues.json"), "w", encoding="utf-8"), indent=1)
    print(f"ig_overlay: {len(cap.get('chunks', []))} caption chunks ({style}), {len(spec.get('cards', []))} cards, {len(sfx)} sfx cues -> {out}")


if __name__ == "__main__":
    main()
