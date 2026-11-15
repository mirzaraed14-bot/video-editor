"""Compile every Harry Potter YouTube row that earlier HP sessions already pulled (no new YouTube requests).
import sys; sys.stdout.reconfigure(encoding="utf-8")
Rows come in two shapes: id|date|views|dur|channel|subs|title  or  id|views|dur|channel|title  (plus a likes variant)."""
import glob, re, sys
rows = {}
files = glob.glob('projects/harry-potter-*/meta/*.txt')
for f in files:
    for ln in open(f, encoding='utf-8', errors='replace'):
        ln = ln.strip()
        if '|' not in ln or ln.startswith(('DESC', '==', 'CH ')):
            continue
        p = ln.split('|')
        vid = p[0]
        if not re.fullmatch(r'[A-Za-z0-9_-]{11}', vid):
            continue
        rec = {'id': vid, 'src': f.split('/')[-1]}
        try:
            if re.fullmatch(r'\d{8}', p[1]):          # id|date|views|...|
                rec['date'] = p[1]; rec['views'] = int(p[2])
                rest = p[3:]
                if len(rest) >= 2 and rest[0].isdigit() and rest[1].isdigit() and int(rest[0]) > 3000:  # id|date|views|likes|dur|...
                    rec['likes'] = int(rest[0]); rest = rest[1:]
                rec['dur'] = int(rest[0]) if rest and rest[0].isdigit() else None
                rest = rest[1:]
                rec['channel'] = rest[0] if rest else ''
                if len(rest) > 1 and rest[1].isdigit():
                    rec['subs'] = int(rest[1]); rest = rest[1:]
                rec['title'] = '|'.join(rest[1:]) if len(rest) > 1 else ''
            elif p[1].isdigit():                        # id|views|dur|channel|title  (or id|views|title)
                rec['views'] = int(p[1])
                if len(p) > 2 and p[2].isdigit():
                    rec['dur'] = int(p[2]); rec['channel'] = p[3] if len(p) > 3 else ''; rec['title'] = '|'.join(p[4:])
                else:
                    rec['title'] = '|'.join(p[2:])
            else:
                continue
        except Exception:
            continue
        old = rows.get(vid)
        if not old or len(str(rec)) > len(str(old)):
            rows[vid] = rec
cast = re.compile(r'radcliffe|rickman|felton|watson|grint|gambon|coltrane|hagrid actor|maggie|bonham|fiennes|oldman|lewis|lynch|evanna|holmes|cast|interview|reunion|hogwarts|stunt', re.I)
out = sorted([r for r in rows.values() if cast.search(r.get('title', '') + r.get('channel', ''))], key=lambda r: -r['views'])
print('rows total', len(rows), 'cast-ish', len(out))
for r in out[:80]:
    print('%-11s %10s %4s %-9s %-26.26s %s' % (r['id'], f"{r['views']:,}", r.get('dur') or '', r.get('date', ''), r.get('channel', ''), r.get('title', '')[:95]))
