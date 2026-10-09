"""Build the published catalog page (catalog-page.html) from catalog.json; images are the web/ copies of shots/."""
import html, json, os

ROOT = os.path.dirname(os.path.abspath(__file__))
fx = json.load(open(os.path.join(ROOT, 'catalog.json'), encoding='utf-8'))
E = html.escape
CH = [('jh', 'Johnny Harris', "The REAL reason the US can't beat Iran", '-DDbYSg0Alw'),
      ('mm', 'MagnatesMedia', 'The Nazi Brothers Who Started Rival Shoe Companies', 'QpNJcAEI-Ts'),
      ('lm', 'LEMMiNO', 'The Search For D. B. Cooper', 'CbUjuwhQPKs'),
      ('pc', 'Patrick Cc:', '50 Cent Was Right About Floyd Mayweather', 'TtVrydVPcf8'),
      ('df', 'Dodford', "Jack Black Doesn't Fit In", 'K0HmeeENJcU'),
      ('cz', 'Coffeezilla', 'UFC Fighter Accidentally Exposes a Huge Scam', 'OBJZw3bF0dg'),
      ('sb', 'Jon Bois (Secret Base)', 'Section 1: A short film from Dorktown', 'alcVZZuj_WE'),
      ('jx', 'JxmyHighroller', 'This Comeback Should Have Been Impossible', 'O7IKUtbkJ6k')]
COL = {e['ch']: e['color'] for e in fx}
BEATS = [('0a', 'Cold open', 'Arnold awards, Martin cheers, freeze'), ('0b', 'Cold open', 'NSP: "celebrating that Nick lost"'),
         ('0c', 'Cold open', 'Martin at the press conference'), ('0d', 'Cold open', 'Black card, SEPTEMBER 26, 2026, the Olympia call'),
         ('1b', 'Ch 1 · Same Night', '2022 interview: "we\'ve had our issues"'), ('1d', 'Ch 1 · Same Night', '"Potential to be Mr. Olympia someday"'),
         ('2a', 'Ch 2 · Not In His League', 'Prague: the journalist\'s phone'), ('3a', 'Ch 3 · Runner-Up', 'The handshake he skipped'),
         ('3c', 'Ch 3 · Runner-Up', 'The cheer, unfrozen'), ('3d', 'Ch 3 · Runner-Up', 'The alleged backstage shove'),
         ('4a', 'Ch 4 · The Bill', '"My sleep was so bad"'), ('5a', 'Ch 5 · Opposite Endings', 'Nick: "I will win"'),
         ('5b', 'Ch 5 · Opposite Endings', 'Martin\'s press-conference answer'), ('5c', 'Ch 5 · Opposite Endings', '"The punch in the teeth…"'),
         ('5d', 'Ch 5 · Opposite Endings', 'The crown, then "12. Martin Fitzwater"'), ('5e', 'Ch 5 · Opposite Endings', 'NSP: "karma"'),
         ('5f', 'Ch 5 · Opposite Endings', 'NSP: "punished more than enough"'), ('5g', 'Ch 5 · Opposite Endings', 'Nick\'s vlog the night he won')]


def mmss(t):
    return f'{int(t // 60)}:{int(t % 60):02d}'


def web(p):
    return p.replace('shots/', 'web/') if p else None


cards = []
for e in fx:
    still = web(e['still'])
    strip = web(e['strip'])
    tags = ''.join(f'<span class="beat">{E(b)}</span>' for b in e['beats'])
    cards.append(f'''<article class="card" id="{e['code']}" data-ch="{e['ch']}" data-cat="{E(e['category'])}" data-text="{E((e['code'] + ' ' + e['name'] + ' ' + e['channel'] + ' ' + e['what'] + ' ' + e['fit'] + ' ' + ' '.join(e['beats'])).lower())}">
<button class="frame" type="button" data-src="{E(still)}" aria-label="Enlarge {E(e['name'])}"><img src="{E(still)}" alt="{E(e['name'])}, {E(e['channel'])} at {mmss(e['peak'])}" loading="lazy"></button>
{f'<button class="strip" type="button" data-src="{E(strip)}" aria-label="Enlarge the motion strip"><img src="{E(strip)}" alt="Four frames of the move" loading="lazy"><span>Motion · {mmss(e["move"][0])}–{mmss(e["move"][1])}</span></button>' if strip else ''}
<div class="body">
<div class="slate"><span class="code">{e['code']}</span><h2>{E(e['name'])}</h2></div>
<p class="meta"><span class="dot" style="--c:{e['color']}"></span>{E(e['channel'])} · <a href="{E(e['url'])}" target="_blank" rel="noopener">watch at {mmss(e['peak'])}</a> · <span class="cat">{E(e['category'])}</span></p>
<p class="what">{E(e['what'])}</p>
<h3>Why it works</h3><p>{E(e['job'])}</p>
<h3>For SAME NIGHT {tags}</h3><p>{E(e['fit'])}</p>
<details><summary>How we'd build it</summary><p>{E(e['build'])}</p></details>
</div></article>''')

chips = ''.join(f'<button class="chip" type="button" data-f="ch" data-v="{c}" aria-pressed="false"><span class="dot" style="--c:{COL[c]}"></span>{E(n)}</button>' for c, n, _, _ in CH)
cats = sorted({e['category'] for e in fx})
catchips = ''.join(f'<button class="chip" type="button" data-f="cat" data-v="{E(c)}" aria-pressed="false">{E(c)}</button>' for c in cats)
legend = ''.join(f'<li><span class="dot" style="--c:{COL[c]}"></span><b>{E(n)}</b> <span class="range">FX-{i*10+1:02d}–{i*10+10:02d}</span><br><a href="https://www.youtube.com/watch?v={v}" target="_blank" rel="noopener">{E(t)}</a></li>' for i, (c, n, t, v) in enumerate(CH))
rows = ''
for b, ch, label in BEATS:
    hits = [e for e in fx if b in e['beats']]
    if hits:
        rows += f'<tr><th scope="row"><span class="beat">{b}</span><small>{E(ch)}</small><span class="bl">{E(label)}</span></th><td>' + ''.join(
            f'<a class="pill" href="#{e["code"]}"><span class="dot" style="--c:{e["color"]}"></span>{e["code"]} {E(e["name"])}</a>' for e in hits) + '</td></tr>'

page = f'''<title>Doc Effects Catalog</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700&family=IBM+Plex+Mono:wght@500;600&family=IBM+Plex+Sans:wght@400;500;600&display=swap">
<style>
/* Layout: an edit-bay bin. A sticky filter strip over a grid of clip cards, each with a slate (FX code) you can call out by name. */
:root {{
  color-scheme: dark;
  --bg: #111317; --panel: #1a1d23; --raise: #22262e; --line: #2d323b;
  --ink: #ecebe6; --mute: #9aa0aa; --tc: #ffc93c; --tc-ink: #141414;
  --display: "Barlow Condensed", "Arial Narrow", "Roboto Condensed", sans-serif;
  --body: "IBM Plex Sans", "Segoe UI", system-ui, sans-serif;
  --mono: "IBM Plex Mono", ui-monospace, Consolas, monospace;
}}
* {{ box-sizing: border-box }}
body {{ background: var(--bg); color: var(--ink); font: 15px/1.55 var(--body); padding-inline: 16px; padding-block: 0 48px }}
.wrap {{ max-width: 1280px; margin-inline: auto }}
header {{ padding-block: 28px 18px; display: grid; gap: 18px; grid-template-columns: minmax(0, 1.2fr) minmax(0, 1fr) }}
h1 {{ font: 700 clamp(34px, 6vw, 56px)/1 var(--display); letter-spacing: .01em; text-transform: uppercase; margin: 0 0 10px; text-wrap: balance }}
.lede {{ color: var(--mute); max-width: 62ch; margin: 0 }} .lede b {{ color: var(--ink) }}
.say {{ font: 600 14px var(--mono); color: var(--tc) }}
.legend {{ list-style: none; margin: 0; padding: 0; display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 8px 16px; font-size: 13px }}
.legend a {{ color: var(--mute) }} .range {{ font: 500 12px var(--mono); color: var(--tc) }}
.dot {{ width: 9px; height: 9px; border-radius: 50%; display: inline-block; background: var(--c); flex: none }}
.bar {{ position: sticky; top: env(safe-area-inset-top, 0px); z-index: 4; background: color-mix(in srgb, var(--bg) 92%, transparent); backdrop-filter: blur(8px);
  border-block: 1px solid var(--line); margin-inline: -16px; padding: 10px 16px }}
.bar .wrap {{ display: flex; flex-wrap: wrap; gap: 6px; align-items: center }}
#q {{ flex: 1 1 240px; min-width: 0; background: var(--panel); border: 1px solid var(--line); color: var(--ink); border-radius: 8px; padding: 8px 11px; font: inherit }}
.count {{ font: 500 13px var(--mono); color: var(--mute) }}
.chips {{ width: 100%; display: flex; flex-wrap: wrap; gap: 6px }}
.chip {{ background: var(--panel); border: 1px solid var(--line); color: var(--ink); border-radius: 99px; padding: 4px 11px; font: 13px var(--body); cursor: pointer; display: inline-flex; gap: 7px; align-items: center }}
.chip[aria-pressed="true"] {{ border-color: var(--tc); background: color-mix(in srgb, var(--tc) 16%, var(--panel)) }}
button:focus-visible, a:focus-visible, input:focus-visible, summary:focus-visible {{ outline: 2px solid var(--tc); outline-offset: 2px }}
main {{ padding-block: 18px; display: grid; grid-template-columns: repeat(auto-fill, minmax(min(100%, 520px), 1fr)); gap: 18px }}
.card {{ background: var(--panel); border: 1px solid var(--line); border-radius: 12px; overflow: hidden; display: flex; flex-direction: column; min-width: 0 }}
.card:target {{ border-color: var(--tc) }}
.frame, .strip {{ all: unset; display: block; cursor: zoom-in; background: #000 }}
.frame img {{ width: 100%; aspect-ratio: 16 / 9; object-fit: contain; display: block }}
.strip {{ border-top: 1px solid var(--line); position: relative }} .strip img {{ width: 100%; display: block }}
.strip span {{ display: block; font: 500 11px var(--mono); color: var(--mute); padding: 4px 12px; background: var(--raise) }}
.body {{ padding: 14px 16px 16px; display: grid; gap: 4px; min-width: 0 }}
.slate {{ display: flex; gap: 10px; align-items: baseline; flex-wrap: wrap }}
.code {{ font: 600 14px var(--mono); background: var(--tc); color: var(--tc-ink); border-radius: 4px; padding: 2px 7px }}
h2 {{ margin: 0; font: 700 26px/1.05 var(--display); letter-spacing: .01em; text-transform: uppercase }}
.meta {{ margin: 0 0 6px; color: var(--mute); font-size: 13px; display: flex; flex-wrap: wrap; gap: 6px; align-items: center }}
.meta a {{ color: var(--ink) }} .cat {{ border: 1px solid var(--line); border-radius: 4px; padding: 0 6px }}
.body p {{ margin: 0 }} .what {{ color: var(--ink) }}
h3 {{ margin: 10px 0 0; font: 600 11px var(--mono); letter-spacing: .12em; text-transform: uppercase; color: var(--tc); display: flex; flex-wrap: wrap; gap: 5px; align-items: center }}
.body p:not(.what):not(.meta) {{ color: #c9cbd0 }}
.beat {{ font: 600 11px var(--mono); color: var(--tc-ink); background: var(--tc); border-radius: 3px; padding: 0 5px; letter-spacing: 0 }}
details {{ margin-top: 10px; border-top: 1px dashed var(--line); padding-top: 8px }}
summary {{ cursor: pointer; color: var(--tc); font: 600 12px var(--mono); letter-spacing: .06em; text-transform: uppercase }}
details p {{ margin-top: 6px !important; font-size: 14px }}
.beats {{ padding-block: 12px 0 }} .beats h2 {{ font-size: 32px; margin-bottom: 4px }}
.tablewrap {{ overflow-x: auto }} table {{ width: 100%; border-collapse: collapse; min-width: 560px }}
th, td {{ border-top: 1px solid var(--line); padding: 10px 8px; vertical-align: top; text-align: left }}
th {{ width: 230px; font-weight: 500 }} th small {{ display: block; color: var(--mute); font-size: 12px; margin-top: 4px }} .bl {{ display: block; font-size: 13px }}
.pill {{ display: inline-flex; gap: 6px; align-items: center; margin: 2px; padding: 3px 9px; border-radius: 99px; border: 1px solid var(--line); color: var(--ink); text-decoration: none; font-size: 13px; background: var(--raise) }}
.pill:hover {{ border-color: var(--tc) }}
.note {{ color: var(--mute); font-size: 13px; max-width: 80ch }}
.lb {{ position: fixed; inset: 0; background: rgba(0, 0, 0, .93); z-index: 9; display: flex; align-items: center; justify-content: center; cursor: zoom-out; padding: 16px }}
.lb img {{ max-width: 100%; max-height: 100%; }}
@media (max-width: 760px) {{ header {{ grid-template-columns: 1fr }} .legend {{ grid-template-columns: 1fr }} }}
@media (prefers-reduced-motion: no-preference) {{ .card {{ transition: border-color .2s }} }}
</style>
<div class="wrap">
<header>
  <div>
    <h1>Doc Effects Catalog</h1>
    <p class="lede"><b>80 signature moves</b> pulled from the first 10 minutes of one video on each of 8 premium documentary channels. Each move has a code you can call out, for example <span class="say">“FX-34 on 3c”</span>. The big frame shows the effect at its clearest; where it moves, the strip underneath shows four frames of the motion. Yellow tags mark the SAME NIGHT beats it was suggested for.</p>
  </div>
  <ul class="legend">{legend}</ul>
</header>
</div>
<div class="bar"><div class="wrap">
  <input id="q" type="search" placeholder="Search a move, a look, a beat (e.g. highlighter, map, 5d)" aria-label="Search the catalog">
  <span class="count" id="n" aria-live="polite"></span>
  <div class="chips" role="group" aria-label="Channel">{chips}</div>
  <div class="chips" role="group" aria-label="Category">{catchips}</div>
</div></div>
<div class="wrap">
<main id="grid">{''.join(cards)}</main>
<section class="beats" id="by-beat">
  <h2>By SAME NIGHT beat</h2>
  <p class="note">Which moves were suggested for each beat. Tap one to jump to it.</p>
  <div class="tablewrap"><table>{rows}</table></div>
  <p class="note">Frames are reference only and never go into an edit. Coffeezilla and JxmyHighroller were captured at 480p (YouTube only allowed a lower quality to be read), so their stills are softer.</p>
</section>
</div>
<div class="lb" id="lb" hidden><img alt="Enlarged frame"></div>
<script>
const on = {{ ch: new Set(), cat: new Set() }};
const q = document.getElementById('q'), n = document.getElementById('n'), cards = [...document.querySelectorAll('.card')];
function apply() {{
  const t = q.value.trim().toLowerCase(); let k = 0;
  for (const c of cards) {{
    const ok = (!on.ch.size || on.ch.has(c.dataset.ch)) && (!on.cat.size || on.cat.has(c.dataset.cat)) && (!t || c.dataset.text.includes(t));
    c.hidden = !ok; if (ok) k++;
  }}
  n.textContent = k + ' of ' + cards.length;
}}
document.querySelectorAll('.chip').forEach(b => b.addEventListener('click', () => {{
  const s = on[b.dataset.f], v = b.dataset.v; s.has(v) ? s.delete(v) : s.add(v);
  b.setAttribute('aria-pressed', s.has(v)); apply();
}}));
q.addEventListener('input', apply); apply();
const lb = document.getElementById('lb');
document.querySelectorAll('.frame, .strip').forEach(b => b.addEventListener('click', () => {{ lb.querySelector('img').src = b.dataset.src; lb.hidden = false; }}));
lb.addEventListener('click', () => {{ lb.hidden = true; }});
document.addEventListener('keydown', e => {{ if (e.key === 'Escape') lb.hidden = true; }});
</script>
'''
open(os.path.join(ROOT, 'catalog-page.html'), 'w', encoding='utf-8').write(page)
used = sorted({p for e in fx for p in (web(e['still']), web(e['strip'])) if p})
json.dump({p: p for p in used}, open(os.path.join(ROOT, 'catalog-files.json'), 'w'), indent=0)
print('page bytes', len(page.encode()), 'images', len(used))
