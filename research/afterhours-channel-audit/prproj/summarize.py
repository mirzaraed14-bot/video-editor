#!/usr/bin/env python3
"""summarize.py <Sequence-NN.json> — a readable census of a timeline dumped by read-timeline.py."""
import collections, json, os, sys

d = json.load(open(sys.argv[1], encoding='utf-8'))
tc = lambda t: f"{int(t // 60)}:{t % 60:05.2f}"
base = lambda p: os.path.basename((p or '').replace('\\', '/'))


def motion(row):
    for c in row.get('fx', []):
        if c.get('match') == 'AE.ADBE Motion' or c.get('display') == 'Motion':
            return c
    return None


def scale_desc(row):
    m = motion(row)
    if not m: return ''
    sc = m['params'].get('Scale')
    pos = m['params'].get('Position')
    rot = m['params'].get('Rotation')
    out = []
    if isinstance(sc, dict):
        k = sc['kf']
        span = (k[-1][0] - k[0][0]) if len(k) > 1 else 0
        rate = ((k[-1][1] - k[0][1]) / span) if span else 0
        out.append(f"scale {k[0][1]:g}->{k[-1][1]:g} over {span:.2f}s ({rate:.2f}%/s, {len(k)}kf)")
    elif sc not in (None, 100.0):
        out.append(f"scale {sc:g}")
    if isinstance(pos, dict): out.append(f"pos kf {pos['kf'][:3]}")
    elif pos not in (None, '0.5:0.5'): out.append(f"pos {pos}")
    if isinstance(rot, dict): out.append(f"rot kf {[v for _, v in rot['kf']]}")
    elif rot not in (None, 0.0): out.append(f"rot {rot}")
    if m.get('instance') and m['instance'] not in ('Motion', '1'): out.append(f"PRESET '{m['instance']}'")
    return ', '.join(out)


def other_fx(row):
    res = []
    for c in row.get('fx', []):
        if c.get('match') in ('AE.ADBE Motion', 'AE.ADBE Opacity') or c.get('display') in ('Motion', 'Opacity'):
            if c.get('display') == 'Opacity':
                op = c['params'].get('Opacity')
                if isinstance(op, dict): res.append(f"opacity kf {[v for _, v in op['kf']]}")
                elif op not in (None, 100.0): res.append(f"opacity {op}")
            continue
        if c['kind'] == 'AudioFilterComponent': continue
        nm = c.get('instance') or c.get('display') or c.get('match')
        keyp = {k: (v['kf'] if isinstance(v, dict) else v) for k, v in c['params'].items()
                if k and not k.startswith('#') and v not in (None, '', False)}
        short = {k: v for k, v in list(keyp.items())[:8]}
        res.append(f"{nm} [{c.get('match')}] {short}")
    return res


def show_track(items, label, indent='', detail=True, limit=400):
    print(f"\n{indent}== {label}: {len(items)} clips")
    names = collections.Counter(base(r.get('media')) or r.get('name') for r in items)
    print(f"{indent}   media: {dict(names.most_common(12))}")
    for r in items[:limit]:
        if not detail: break
        dur = r['end'] - r['start']
        bits = [f"{tc(r['start'])}-{tc(r['end'])} ({dur:.2f}s)", (r.get('name') or '')[:40]]
        if r.get('media_kind') == 'sequence': bits.append(f"[NEST {r['media']}]")
        elif r.get('media'): bits.append(f"<{base(r['media'])[:45]}> in {r.get('in')}")
        if r.get('speed') and abs(r['speed'] - 1) > 1e-3: bits.append(f"SPEED {r['speed']}")
        if r.get('label'): bits.append(f"label {r['label']}")
        if 'level_db' in r: bits.append(f"vol {r['level_db']} dB")
        if r.get('level_kf_db'): bits.append(f"vol kf {r['level_kf_db'][:6]}")
        if 'gain_db' in r: bits.append(f"gain {r['gain_db']} dB")
        sd = scale_desc(r)
        if sd: bits.append(sd)
        print(indent + '   ' + ' | '.join(b for b in bits if b))
        for o in other_fx(r): print(indent + '       + ' + o[:260])
        if r.get('nest'):
            for i, tr in enumerate(r['nest']['video']):
                if tr: show_track(tr, f"nest V{i + 1}", indent + '        ', detail=True, limit=40)


print(f"# {d['name']}")
for i, tr in enumerate(d['video']):
    if tr: show_track(tr, f"V{i + 1}")
for i, tr in enumerate(d['audio']):
    if tr: show_track(tr, f"A{i + 1}", detail=(i > 0))
