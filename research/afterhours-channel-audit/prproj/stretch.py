import json
BS = chr(92)
def walk(items, off, path, out):
    for r in items:
        for c in r.get('fx', []):
            if c.get('display') == 'Motion':
                sw = c['params'].get('Scale Width'); sc = c['params'].get('Scale'); uni = c['params'].get('#4')
                if (isinstance(sw, (int, float)) and abs(sw - 100) > 0.5) or isinstance(sw, dict):
                    out.append((round(r['start'] + off, 2), round(r['end'] - r['start'], 2), path,
                                str(r.get('media')).replace(BS, '/').split('/')[-1][:30], sc, sw, uni))
        if r.get('nest'): walk(r['nest']['video'][0], r['start'] - (r.get('in') or 0), path + '>nest', out)
for f in ('PC-release-Seq24.json', 'Sequence-05.json', 'Sequence-16.json'):
    d = json.load(open(f, encoding='utf-8')); out = []
    for i, tr in enumerate(d['video']): walk(tr, 0, f'V{i + 1}', out)
    print('##', f)
    for o in out: print('  ', o)
