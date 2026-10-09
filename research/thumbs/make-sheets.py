"""make-sheets.py: each reference channel's POPULAR tab as YouTube presents it (dark mode, 4 x 3 grid, duration badge,
title, views and age), from the live Popular lists (popular.txt, read off youtube.com 2026-10-09) and the full-res
thumbnails (popular/<id>.jpg). One PNG per channel in sheets/, screenshotted with headless Chrome.

  python research/thumbs/make-sheets.py
"""
import html, os, subprocess

D = os.path.dirname(os.path.abspath(__file__))
CHROME = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
os.makedirs(os.path.join(D, 'sheets'), exist_ok=True)
blocks = open(os.path.join(D, 'popular.txt'), encoding='utf-8').read().strip().split('\n===\n')

CSS = """
*{margin:0;padding:0;box-sizing:border-box}
body{background:#0f0f0f;color:#f1f1f1;font-family:Roboto,Arial,sans-serif;width:1600px;padding:28px 40px 30px}
.head{display:flex;align-items:center;gap:18px;margin-bottom:22px}
.av{width:56px;height:56px;border-radius:50%;background:#272727;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:24px}
.ch{font-size:30px;font-weight:700} .sub{font-size:14px;color:#aaa;margin-top:4px}
.tabs{display:flex;gap:28px;font-size:16px;font-weight:500;color:#aaa;border-bottom:1px solid #3f3f3f;margin-bottom:16px}
.tabs span{padding:10px 0} .tabs .on{color:#f1f1f1;border-bottom:2px solid #f1f1f1}
.chips{display:flex;gap:12px;margin-bottom:22px} .chip{background:#272727;border-radius:8px;padding:7px 12px;font-size:14px;font-weight:500}
.chip.on{background:#f1f1f1;color:#0f0f0f}
.grid{display:grid;grid-template-columns:repeat(4,1fr);gap:40px 16px}
.th{position:relative;width:100%;aspect-ratio:16/9;border-radius:12px;overflow:hidden;background:#222}
.th img{width:100%;height:100%;object-fit:cover;display:block}
.dur{position:absolute;right:8px;bottom:8px;background:rgba(0,0,0,.75);color:#fff;font-size:12px;font-weight:500;padding:3px 5px;border-radius:4px}
.t{margin-top:12px;font-size:16px;font-weight:500;line-height:22px;max-height:44px;overflow:hidden;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical}
.m{margin-top:4px;font-size:14px;color:#aaa}
"""

for b in blocks:
    lines = b.strip().split('\n')
    handle, name, rows = lines[0], lines[1], [l.split('\t') for l in lines[2:]]
    cards = ''
    for vid, ln, views, title in rows:
        v, ago = [x.strip() for x in views.split('·')]
        ago = ago.replace('y ago', ' years ago').replace('mo ago', ' months ago').replace('d ago', ' days ago').replace('1 years', '1 year').replace('1 months', '1 month')
        cards += (f'<div><div class="th"><img src="../popular/{vid}.jpg"><span class="dur">{ln}</span></div>'
                  f'<div class="t">{html.escape(title)}</div><div class="m">{v} views • {ago}</div></div>')
    page = (f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>'
            f'<div class="head"><div class="av">{html.escape(name[0])}</div><div><div class="ch">{html.escape(name)}</div>'
            f'<div class="sub">@{handle} · most popular videos, as listed on YouTube 9 Oct 2026</div></div></div>'
            f'<div class="tabs"><span>Home</span><span class="on">Videos</span><span>Shorts</span><span>Playlists</span></div>'
            f'<div class="chips"><span class="chip">Latest</span><span class="chip on">Popular</span><span class="chip">Oldest</span></div>'
            f'<div class="grid">{cards}</div></body></html>')
    hp = os.path.join(D, 'sheets', f'{handle}.html')
    open(hp, 'w', encoding='utf-8').write(page)
    out = os.path.join(D, 'sheets', f'{handle}.png')
    subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--hide-scrollbars', '--force-device-scale-factor=1',
                    '--window-size=1600,1255', f'--screenshot={out}', '--virtual-time-budget=4000', 'file:///' + hp.replace('\\', '/')],
                   check=True, capture_output=True)
    print(out)
