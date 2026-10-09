import json
BS = chr(92)
h = json.load(open('projects/gta6-hurricanes/brief/seq16-after-sfx.json', encoding='utf-8'))
n = json.load(open('research/afterhours-channel-audit/prproj/Sequence-16.json', encoding='utf-8'))
base = lambda p: str(p or '').replace(BS, '/').split('/')[-1]


def rows_now(kind):
    out = []
    for ti, tr in enumerate(n[kind]):
        for r in tr:
            out.append((ti, r.get('media') if r.get('media_kind') == 'sequence' else base(r.get('media')),
                        round(r['start'], 2), round(r['end'], 2)))
    return out


def rows_h(k):
    return [(r[0], base(r[1]), round(r[2], 2), round(r[3], 2)) for r in h[k]]


for k, kind in (('v', 'video'), ('a', 'audio')):
    A, B = set(rows_h(k)), set(rows_now(kind))
    print(kind, 'handed', len(A), 'now', len(B), 'removed', len(A - B), 'added', len(B - A))
    for x in sorted(A - B)[:20]: print('  - ', x)
    for x in sorted(B - A)[:20]: print('  + ', x)
