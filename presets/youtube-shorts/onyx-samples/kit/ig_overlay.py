"""ig_overlay.py: the OVERLAY layer of an Instagram-look sample (README § 3-6 + LESSONS "Reference study 1") as a transparent
HyperFrames composition -> <job>/ig/hf-overlay/index.html, plus <job>/ig/work/sfx-cues.json (one sound per graphic entrance).

  python presets/youtube-shorts/onyx-samples/kit/ig_overlay.py projects/<job>
  cd projects/<job>/ig/hf-overlay && npx --yes hyperframes@0.8.16 render . --format mov --fps <fps> -o ../work/overlay.mov

Reads `<job>/ig/spec.json`:
  "fps", "frames",
  "captions": {"style": "box" | "pill" | "accent", "y": 1310, "accent": "#CFAA5A",
               "chunks": [{"text": "Is it okay if I tell you", "start": s, "end": s, "hl": ["tell"]}]}   (from ig_captions.py)
      box    white rounded box, black sentence-case text (Chris Do's house style)
      pill   dark translucent pill, white text (Ali Abdaal's)
      accent white text with a soft shadow, the hl words in the accent colour (the pilot's)
      plain  text in "color" (e.g. a host's own caption colour, Rob Dial's yellow) with a soft shadow, no box
               optional for every style: "size" (px, default 52), "weight" (default 700), "color" (plain/accent text)
  "cards": [{"t0": s, "t1": s, "kind": "title" | "chip" | "number" | "image" | "prompt", ...}]   graphics in the top band (y 260-760)
      title   {"text": "THE LOWBALL TEST", "sub": "optional small line"}                         rises in, fades out
      chip    {"text": "Anchor first", "icon": "⚓"}                                              pops in
      number  {"from": 0, "to": 20000, "prefix": "$", "suffix": "", "label": "the final price"}  counts up
      image   {"src": "ig/assets/x.png", "w": 760, "radius": 28, "label": "optional caption"}    pops in, soft shadow
      prompt  {"text": "What would you say?", "options": ["A  Take it", "B  Walk away"]}       participation card
      call    {"name": "Mom", "sub": "calling...", "initials": "M"}                                an incoming-call banner (vibrate sound)
      notify  {"app": "BANK", "title": "Wire transfer received", "body": "+$23,000.00", "time": "now"}   a phone notification (ding)
      every card also takes "y" (top, px) to override its default slot
  "credit": "@thechrisdo"   small credit line above the captions (a prospect's condition: Rob Dial, Rollo); "credit_t0" (s) delays it
      (keep it out of the hook), "credit_y" (px) places it (default: 80 px above the captions)
Motion: type and cards rise 40 px under a mask (power3.out 0.45 s), objects pop 0.85 → 1, exits fade 0.25 s; every step on
the frame grid a quarter frame early.
"""
import json, os, shutil, sys

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8")
    except Exception:
        pass

KIT = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(KIT, "..", "..", "..", ".."))
W, H = 1080, 1920
SLOTS = {"title": 300, "chip": 420, "number": 330, "image": 300, "prompt": 300, "call": 280, "notify": 280}


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
    for fn in ("Inter-Regular.otf", "Inter-Bold.otf", "Inter-Black.otf"):
        shutil.copy(os.path.join(REPO, "assets", "fonts", fn), os.path.join(out, "fonts", fn))
    shutil.copy(os.path.join(REPO, "presets", "youtube-shorts", "onyx-samples-youtube", "kit", "vendor", "gsap.min.js"), os.path.join(out, "vendor", "gsap.min.js"))

    # ---- captions
    cap_html, cap_js = [], []
    for i, c in enumerate(cap.get("chunks", [])):
        words = []
        for w in c["text"].split(" "):
            hl = any(w.strip(".,!?;:").lower() == h.lower() for h in c.get("hl", []))
            words.append(f'<span class="w{" hl" if hl else ""}">{esc(w)}</span>')
        cap_html.append(f'<div id="c{i}" class="cap {style}"><span class="inner">{" ".join(words)}</span></div>')
        cap_js.append(f'tl.set("#c{i}", {{autoAlpha: 1}}, {q(c["start"])}); tl.fromTo("#c{i} .inner", {{y: 14}}, {{y: 0, duration: 0.16, ease: "power2.out"}}, {q(c["start"])}); '
                      f'tl.set("#c{i}", {{autoAlpha: 0}}, {q(c["end"])});')

    # ---- cards
    card_html, card_js, sfx = [], [], []
    for i, k in enumerate(spec.get("cards", [])):
        kind, y, cid = k["kind"], k.get("y", SLOTS.get(k["kind"], 320)), f"k{i}"
        if kind == "title":
            inner = f'<div class="mask"><div class="rise title">{esc(k["text"])}</div></div>' + (f'<div class="mask"><div class="rise sub">{esc(k["sub"])}</div></div>' if k.get("sub") else "")
            card_js.append(f'tl.set("#{cid}", {{autoAlpha: 1}}, {q(k["t0"])}); tl.fromTo("#{cid} .rise", {{yPercent: 110}}, {{yPercent: 0, duration: 0.45, ease: "power3.out", stagger: 0.06}}, {q(k["t0"])});')
        elif kind == "chip":
            inner = f'<div class="chip"><span class="ico">{esc(k.get("icon", ""))}</span>{esc(k["text"])}</div>'
            card_js.append(f'tl.set("#{cid}", {{autoAlpha: 1}}, {q(k["t0"])}); tl.fromTo("#{cid} .chip", {{scale: 0.85, opacity: 0}}, {{scale: 1, opacity: 1, duration: 0.3, ease: "back.out(2)"}}, {q(k["t0"])});')
        elif kind == "number":
            inner = (f'<div class="num"><span class="pre">{esc(k.get("prefix", ""))}</span><span class="val" id="{cid}v">{k.get("from", 0):,}</span>'
                     f'<span class="suf">{esc(k.get("suffix", ""))}</span></div>' + (f'<div class="numlab">{esc(k["label"])}</div>' if k.get("label") else ""))
            d = min(0.9, max(0.4, (k["t1"] - k["t0"]) * 0.4))
            card_js.append(f'tl.set("#{cid}", {{autoAlpha: 1}}, {q(k["t0"])}); tl.fromTo("#{cid}", {{y: 40}}, {{y: 0, duration: 0.45, ease: "power3.out"}}, {q(k["t0"])}); '
                           f'(function(){{ const o = {{v: {k.get("from", 0)}}}; tl.to(o, {{v: {k["to"]}, duration: {d:.2f}, ease: "power2.out", onUpdate: () => {{ document.getElementById("{cid}v").textContent = Math.round(o.v).toLocaleString("en-US"); }}}}, {q(k["t0"] + 0.1)}); }})();')
            sfx.append(dict(t=round(k["t0"] + 0.1 + d, 3), kind="tick"))
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
        else:
            sys.exit(f"ig_overlay: unknown card kind {kind}")
        card_html.append(f'<div id="{cid}" class="card" style="top:{y}px" data-layout-allow-overflow>{inner}</div>')
        card_js.append(f'tl.to("#{cid}", {{autoAlpha: 0, duration: 0.25, ease: "power1.in"}}, {q(max(k["t0"] + 0.3, k["t1"] - 0.25))});')
        if kind not in ("call", "notify"):
            sfx.append(dict(t=round(k["t0"], 3), kind="pop" if kind in ("chip", "image") else "whoosh"))

    credit = spec.get("credit")
    credit_html = f'<div id="credit">{esc(credit)}</div>' if credit else ""
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
html, body {{ margin: 0; background: transparent; }}
#root {{ position: relative; width: {W}px; height: {H}px; overflow: hidden; background: transparent; font-family: "Inter", sans-serif; }}
.cap {{ position: absolute; left: 60px; width: 960px; top: {cy}px; text-align: center; visibility: hidden; }}
.cap .inner {{ display: inline-block; font-size: {csize}px; line-height: 1.18; font-weight: {cweight}; letter-spacing: -0.01em; }}
.cap.box .inner {{ background: #FFFFFF; color: #0B0B0B; padding: 10px 22px 12px; border-radius: 14px; box-shadow: 0 6px 18px rgba(0,0,0,0.25); }}
.cap.pill .inner {{ background: rgba(20,20,20,0.62); color: #FFFFFF; padding: 10px 24px 12px; border-radius: 40px; font-weight: 600; }}
.cap.accent .inner {{ color: {ccolor}; text-shadow: 0 3px 12px rgba(0,0,0,0.65), 0 1px 2px rgba(0,0,0,0.8); }}
.cap.plain .inner {{ color: {ccolor}; text-shadow: 0 2px 10px rgba(0,0,0,0.75), 0 1px 2px rgba(0,0,0,0.9); }}
.cap .hl {{ color: {accent}; }}
.cap.box .hl {{ color: #0B0B0B; background: {accent}; border-radius: 6px; padding: 0 6px; }}
.card {{ position: absolute; left: 0; width: {W}px; text-align: center; visibility: hidden; }}
.mask {{ overflow: hidden; padding: 4px 0 8px; }}
.rise {{ display: inline-block; }}
.title {{ font-size: 88px; font-weight: 900; letter-spacing: -0.02em; color: #FFFFFF; text-shadow: 0 6px 24px rgba(0,0,0,0.45); line-height: 1.0; }}
.sub {{ font-size: 40px; font-weight: 700; color: rgba(255,255,255,0.86); text-shadow: 0 4px 16px rgba(0,0,0,0.5); }}
.chip {{ display: inline-flex; align-items: center; gap: 16px; background: #FFFFFF; color: #0B0B0B; font-size: 48px; font-weight: 800;
  padding: 16px 30px; border-radius: 60px; box-shadow: 0 10px 30px rgba(0,0,0,0.3); }}
.chip .ico {{ font-size: 52px; }}
.num {{ font-size: 150px; font-weight: 900; color: #FFFFFF; letter-spacing: -0.03em; text-shadow: 0 8px 30px rgba(0,0,0,0.5); line-height: 1; }}
.numlab {{ font-size: 40px; font-weight: 700; color: rgba(255,255,255,0.9); margin-top: 10px; text-shadow: 0 4px 16px rgba(0,0,0,0.5); }}
.imgcard {{ display: inline-block; overflow: hidden; box-shadow: 0 18px 50px rgba(0,0,0,0.45); background: #fff; }}
.imgcard img {{ display: block; width: 100%; height: auto; }}
.imglab {{ font-size: 36px; font-weight: 700; color: #FFFFFF; margin-top: 14px; text-shadow: 0 4px 16px rgba(0,0,0,0.6); }}
.prompt {{ display: inline-block; text-align: left; background: #FFFFFF; color: #0B0B0B; border-radius: 28px; padding: 30px 38px; box-shadow: 0 18px 50px rgba(0,0,0,0.35); }}
.pq {{ font-size: 50px; font-weight: 900; margin-bottom: 18px; }}
.opt {{ font-size: 42px; font-weight: 700; padding: 12px 18px; margin-top: 10px; border-radius: 16px; background: #F1F1F1; }}
.call {{ display: inline-flex; align-items: center; gap: 26px; width: 860px; box-sizing: border-box; padding: 26px 30px; border-radius: 44px;
  background: rgba(28,28,30,0.92); box-shadow: 0 18px 50px rgba(0,0,0,0.45); text-align: left; }}
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
