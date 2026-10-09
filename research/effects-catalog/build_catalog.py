"""Merge work/<code>/effects.json into one numbered catalog: catalog.json, CATALOG.md and index.html (opens locally,
images from shots/). Codes are stable by channel block: FX-01..10 Johnny Harris, 11..20 MagnatesMedia, 21..30 LEMMiNO,
31..40 Patrick Cc:, 41..50 Dodford, 51..60 Coffeezilla, 61..70 Jon Bois, 71..80 JxmyHighroller."""
import html, json, os, re

ROOT = os.path.dirname(os.path.abspath(__file__))
CH = [
    ('jh', 'Johnny Harris', "The REAL reason the US can't beat Iran", '-DDbYSg0Alw', '#e0a84f'),
    ('mm', 'MagnatesMedia', 'The Nazi Brothers Who Started Rival Shoe Companies', 'QpNJcAEI-Ts', '#e05a4f'),
    ('lm', 'LEMMiNO', 'The Search For D. B. Cooper', 'CbUjuwhQPKs', '#ef4444'),
    ('pc', 'Patrick Cc:', '50 Cent Was Right About Floyd Mayweather', 'TtVrydVPcf8', '#f5c542'),
    ('df', 'Dodford', "Jack Black Doesn't Fit In", 'K0HmeeENJcU', '#e889b5'),
    ('cz', 'Coffeezilla', 'UFC Fighter Accidentally Exposes a Huge Scam', 'OBJZw3bF0dg', '#3ad1e0'),
    ('sb', 'Jon Bois (Secret Base)', 'Section 1: A short film from Dorktown', 'alcVZZuj_WE', '#f08a24'),
    ('jx', 'JxmyHighroller', 'This Comeback Should Have Been Impossible', 'O7IKUtbkJ6k', '#7c9cff'),
]
BEATS = {'COLD OPEN': ['0a', '0b', '0c', '0d'], 'CH1 Same Night': ['1a', '1b', '1c', '1d'],
         'CH2 Not In His League': ['2a'], 'CH3 Runner-Up': ['3a', '3b', '3c', '3d', '3e'],
         'CH4 The Bill': ['4a'], 'CH5 Opposite Endings': ['5a', '5b', '5c', '5d', '5e', '5f', '5g', '5h']}


def slug(s):
    return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')


def mmss(t):
    return f'{int(t // 60)}:{int(t % 60):02d}'


fx = []
for i, (code, chname, title, vid, col) in enumerate(CH):
    for j, e in enumerate(json.load(open(os.path.join(ROOT, 'work', code, 'effects.json'), encoding='utf-8'))):
        s = slug(e['name'])
        still, strip = f'shots/{code}-{s}.jpg', f'shots/{code}-{s}-strip.jpg'
        fx.append({**e, 'code': f'FX-{i * 10 + j + 1:02d}', 'ch': code, 'channel': chname, 'video': title, 'color': col,
                   'url': f"https://www.youtube.com/watch?v={vid}&t={int((e.get('move') or [e['peak']])[0])}s",
                   'still': still if os.path.exists(os.path.join(ROOT, still)) else None,
                   'strip': strip if os.path.exists(os.path.join(ROOT, strip)) else None,
                   'beats': sorted(set(re.findall(r'\b([0-5][a-h])\b', e.get('fit', ''))))})
json.dump(fx, open(os.path.join(ROOT, 'catalog.json'), 'w', encoding='utf-8'), indent=1, ensure_ascii=False)

# CATALOG.md: the text index to direct from
md = ['# Effects catalog: 80 signature moves from 8 premium documentary channels (2026-10-08)', '',
      'Say "FX-34 on 3c" to direct. Pictures + full notes: `index.html` (open in a browser). Frames are reference only,',
      'from the first 10 minutes of one video per channel; never used in an edit.', '']
for code, chname, title, vid, _ in CH:
    md += [f'## {chname}: *{title}* (https://youtu.be/{vid})', '', '| Code | Name | Category | At | What |', '|---|---|---|---|---|']
    for e in [x for x in fx if x['ch'] == code]:
        first = re.split(r'(?<=[.!?])\s', e['what'])[0].replace('|', '/')
        md.append(f"| {e['code']} | **{e['name']}** | {e['category']} | {mmss(e['peak'])} | {first} |")
    md.append('')
md += ['## By SAME NIGHT beat (where the agents suggested each move)', '']
for ch, beats in BEATS.items():
    for b in beats:
        hits = [f"{e['code']} {e['name']}" for e in fx if b in e['beats']]
        if hits:
            md.append(f"- **{b}** ({ch}): " + ' · '.join(hits))
open(os.path.join(ROOT, 'CATALOG.md'), 'w', encoding='utf-8').write('\n'.join(md) + '\n')

# index.html
E = html.escape
cats = sorted({e['category'] for e in fx})
cards = []
for e in fx:
    img = f'<img class="still" src="{E(e["still"])}" alt="{E(e["name"])}" loading="lazy">' if e['still'] else '<div class="noimg">no frame</div>'
    strip = (f'<figure class="stripwrap"><img class="strip" src="{E(e["strip"])}" alt="{E(e["name"])} in motion" loading="lazy">'
             f'<figcaption>The move, 4 frames across {mmss(e["move"][0])}–{mmss(e["move"][1])}</figcaption></figure>') if e['strip'] else ''
    beats = ''.join(f'<span class="beat">{E(b)}</span>' for b in e['beats'])
    cards.append(f'''<article class="card" data-ch="{e['ch']}" data-cat="{E(e['category'])}" data-text="{E((e['code'] + ' ' + e['name'] + ' ' + e['what'] + ' ' + e['fit']).lower())}" id="{e['code']}">
  <div class="media">{img}</div>
  {strip}
  <div class="body">
    <div class="head"><span class="code" style="--c:{e['color']}">{e['code']}</span><h2>{E(e['name'])}</h2></div>
    <div class="meta"><span class="dot" style="background:{e['color']}"></span>{E(e['channel'])} · <a href="{E(e['url'])}" target="_blank" rel="noopener">{mmss(e['peak'])} ↗</a> · <span class="cat">{E(e['category'])}</span></div>
    <p class="what">{E(e['what'])}</p>
    <h3>Why it works</h3><p>{E(e['job'])}</p>
    <h3>Where in SAME NIGHT {beats}</h3><p>{E(e['fit'])}</p>
    <details><summary>How we'd build it</summary><p>{E(e['build'])}</p></details>
  </div>
</article>''')
chips = ''.join(f'<button class="chip" data-f="ch" data-v="{c}" style="--c:{col}"><span class="dot" style="background:{col}"></span>{E(n)}</button>' for c, n, _, _, col in CH)
catchips = ''.join(f'<button class="chip" data-f="cat" data-v="{E(c)}">{E(c)}</button>' for c in cats)
beatrows = ''
for ch, beats in BEATS.items():
    for b in beats:
        hits = [e for e in fx if b in e['beats']]
        if hits:
            beatrows += f'<tr><td><b>{b}</b><br><small>{E(ch)}</small></td><td>' + ' '.join(
                f'<a class="pill" href="#{e["code"]}" style="--c:{e["color"]}">{e["code"]} {E(e["name"])}</a>' for e in hits) + '</td></tr>'
page = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Effects Catalog</title>
<style>
:root{{--bg:#0e0f11;--panel:#17181b;--line:#2a2c31;--ink:#ecebe7;--mute:#9a9ca3;--acc:#f5c542}}
*{{box-sizing:border-box}} body{{margin:0;background:var(--bg);color:var(--ink);font:15px/1.55 system-ui,-apple-system,Segoe UI,sans-serif}}
header{{padding:28px 16px 8px;max-width:1240px;margin:auto}} h1{{margin:0 0 6px;font-size:28px;letter-spacing:-.01em}}
.sub{{color:var(--mute);max-width:820px}} .sub b{{color:var(--ink)}}
.bar{{position:sticky;top:0;z-index:5;background:rgba(14,15,17,.94);backdrop-filter:blur(6px);border-bottom:1px solid var(--line)}}
.bar .in{{max-width:1240px;margin:auto;padding:10px 16px;display:flex;flex-wrap:wrap;gap:6px;align-items:center}}
input{{flex:1 1 220px;min-width:0;background:var(--panel);border:1px solid var(--line);color:var(--ink);border-radius:8px;padding:8px 10px;font:inherit}}
.chip{{background:var(--panel);border:1px solid var(--line);color:var(--ink);border-radius:99px;padding:5px 11px;font:13px system-ui;cursor:pointer;display:inline-flex;gap:6px;align-items:center}}
.chip.on{{border-color:var(--acc);background:#2a2412}} .dot{{width:8px;height:8px;border-radius:50%;display:inline-block}}
.row{{width:100%;display:flex;flex-wrap:wrap;gap:6px}}
main{{max-width:1240px;margin:auto;padding:16px;display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%,560px),1fr));gap:18px}}
.card{{background:var(--panel);border:1px solid var(--line);border-radius:14px;overflow:hidden;display:flex;flex-direction:column}}
.media{{background:#000;aspect-ratio:16/9}} .still{{width:100%;height:100%;object-fit:contain;display:block;cursor:zoom-in}}
.stripwrap{{margin:0;border-top:1px solid var(--line)}} .strip{{width:100%;display:block;cursor:zoom-in}}
figcaption{{font-size:12px;color:var(--mute);padding:4px 12px}}
.body{{padding:12px 16px 16px}} .head{{display:flex;gap:10px;align-items:center}} h2{{margin:0;font-size:20px}}
.code{{font:700 13px ui-monospace,Consolas,monospace;background:var(--c);color:#111;border-radius:6px;padding:3px 7px;white-space:nowrap}}
.meta{{color:var(--mute);font-size:13px;margin:4px 0 8px;display:flex;flex-wrap:wrap;gap:6px;align-items:center}} .meta a{{color:var(--ink)}}
.cat{{border:1px solid var(--line);border-radius:6px;padding:0 6px}}
h3{{font-size:12px;text-transform:uppercase;letter-spacing:.08em;color:var(--acc);margin:12px 0 2px;display:flex;flex-wrap:wrap;gap:5px;align-items:center}}
p{{margin:0}} .what{{color:#d6d5d0}} details{{margin-top:10px}} summary{{cursor:pointer;color:var(--acc);font-size:13px}}
details p{{color:#cfcfca;font-size:14px;margin-top:4px}}
.beat{{font:600 11px ui-monospace,Consolas,monospace;color:#111;background:var(--acc);border-radius:4px;padding:0 5px;letter-spacing:0}}
section.beats{{max-width:1240px;margin:auto;padding:8px 16px 40px}} table{{width:100%;border-collapse:collapse}}
td{{border-top:1px solid var(--line);padding:8px 6px;vertical-align:top}} td:first-child{{width:150px}}
.pill{{display:inline-block;margin:2px;padding:2px 8px;border-radius:99px;border:1px solid var(--c);color:var(--ink);text-decoration:none;font-size:13px}}
.lb{{position:fixed;inset:0;background:rgba(0,0,0,.92);display:none;align-items:center;justify-content:center;z-index:9;cursor:zoom-out}}
.lb img{{max-width:96vw;max-height:94vh}} .lb.on{{display:flex}} .hide{{display:none!important}} .count{{color:var(--mute);font-size:13px;margin-left:auto}}
</style></head><body>
<header><h1>Effects Catalog</h1>
<p class="sub"><b>80 signature moves</b> from 8 premium documentary channels, each from the first 10 minutes of one video, named so you can
direct with a code: <b>“FX-34 on 3c”</b>. The still is the effect at its clearest; where it's a move, the strip under it shows 4 frames of the motion.
Yellow tags = the SAME NIGHT beats each move was suggested for. Reference only: these frames never go into an edit.</p></header>
<div class="bar"><div class="in"><input id="q" placeholder="Search names, looks, beats…"><span class="count" id="n"></span>
<div class="row">{chips}</div><div class="row">{catchips}</div></div></div>
<main id="grid">{''.join(cards)}</main>
<section class="beats"><h2>By SAME NIGHT beat</h2><p class="sub">Which moves the analysis suggested for each beat. Click to jump.</p><table>{beatrows}</table></section>
<div class="lb" id="lb"><img alt=""></div>
<script>
const on={{ch:new Set(),cat:new Set()}};const q=document.getElementById('q');
function apply(){{let n=0;const t=q.value.trim().toLowerCase();document.querySelectorAll('.card').forEach(c=>{{const ok=(!on.ch.size||on.ch.has(c.dataset.ch))&&(!on.cat.size||on.cat.has(c.dataset.cat))&&(!t||c.dataset.text.includes(t));c.classList.toggle('hide',!ok);if(ok)n++}});document.getElementById('n').textContent=n+' of 80'}}
document.querySelectorAll('.chip').forEach(b=>b.onclick=()=>{{const s=on[b.dataset.f];s.has(b.dataset.v)?s.delete(b.dataset.v):s.add(b.dataset.v);b.classList.toggle('on');apply()}});
q.oninput=apply;apply();
const lb=document.getElementById('lb');document.querySelectorAll('.still,.strip').forEach(i=>i.onclick=()=>{{lb.querySelector('img').src=i.src;lb.classList.add('on')}});lb.onclick=()=>lb.classList.remove('on');
</script></body></html>'''
open(os.path.join(ROOT, 'index.html'), 'w', encoding='utf-8').write(page)
print(len(fx), 'effects;', sum(1 for e in fx if e['still']), 'stills;', sum(1 for e in fx if e['strip']), 'strips')
