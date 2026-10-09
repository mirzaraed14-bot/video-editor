#!/usr/bin/env python3
"""grammar-stats.py — timeline-level numbers off the creator's shipped GTA long-forms (read-timeline.py JSONs)."""
import json, statistics as st

BS = chr(92)
base = lambda p: str(p or '').replace(BS, '/').split('/')[-1]
JOBS = [('PC Release (09-23)', 'PC-release-Seq24.json', 'pc-release-synced'),
        ("Collector's Box (09-25)", 'Sequence-05.json', 'C1302'),
        ('Game Informer (09-30)', 'Sequence-16.json', 'hurricanes-synced')]


def motion_scale(r):
    for c in r.get('fx', []):
        if c.get('display') == 'Motion':
            return c['params'].get('Scale')
    return None


for title, f, face in JOBS:
    d = json.load(open(f, encoding='utf-8'))
    V = d['video']
    dur = max(r['end'] for tr in V for r in tr)
    isface = lambda r: face.lower() in base(r.get('media')).lower()
    # what is VISIBLE at time t: the top-most clip covering t (opacity ignored; a scale<100 face clip is a PiP)
    step = 0.05
    vis = []
    t = 0.0
    while t < dur:
        top = None
        for ti in range(len(V) - 1, -1, -1):
            for r in V[ti]:
                if r['start'] <= t < r['end']:
                    top = (ti, r); break
            if top: break
        vis.append(top)
        t += step
    def kind(x):
        if x is None: return 'gap'
        ti, r = x
        if base(r.get('media')) in ('1112293707',) : return 'black'
        if r.get('media_kind') == 'sequence':
            inner = (r.get('nest') or {}).get('video', [[]])[0]
            return 'face' if any(isface(c) for c in inner) else 'overlay'
        if isface(r):
            sc = motion_scale(r)
            return 'pip' if isinstance(sc, (int, float)) and sc < 99 else 'face'
        return 'overlay'
    ks = [kind(x) for x in vis]
    # the V5 black-video fade sits over everything for 68 s at opacity 0 — treat black as transparent after its fade
    ks = ['face' if k == 'black' else k for k in ks]
    share = {k: round(100 * ks.count(k) / len(ks), 1) for k in set(ks)}
    # runs of face
    runs, cur = [], None
    for i, k in enumerate(ks):
        if k == 'face':
            cur = cur or [i, i]; cur[1] = i
        elif cur:
            runs.append((cur[1] - cur[0] + 1) * step); cur = None
    if cur: runs.append((cur[1] - cur[0] + 1) * step)
    # edits: every clip boundary on V1 (top level) + nest-internal boundaries
    bounds = set()
    for tr in V:
        for r in tr:
            bounds.add(round(r['start'], 2))
            if r.get('nest'):
                for c in r['nest']['video'][0]:
                    s = r['start'] + c['start'] - (r.get('in') or 0)
                    if r['start'] < s < r['end']: bounds.add(round(s, 2))
    b = sorted(x for x in bounds if 0 < x < dur)
    cold = sum(1 for x in b if x < 60)
    nests = [r for r in V[0] if r.get('media_kind') == 'sequence']
    nest_d = [r['end'] - r['start'] for r in nests]
    nest_n = [len(r['nest']['video'][0]) for r in nests if r.get('nest')]
    # music out under cut zooms
    czs = []
    def walk(items, off):
        for r in items:
            sc = motion_scale(r)
            if isface(r) and isinstance(sc, (int, float)) and sc > 100.5:
                czs.append((r['start'] + off, r['end'] + off))
            if r.get('nest'):
                walk(r['nest']['video'][0], r['start'] - (r.get('in') or 0))
    walk(V[0], 0)
    music = [r for tr in d['audio'][1:] for r in tr if base(r.get('media')).startswith('ES_')]
    def music_at(t): return any(m['start'] <= t < m['end'] for m in music)
    out = sum(1 for a, z in czs if not music_at((a + z) / 2))
    first = kind(vis[0]); last = kind(vis[-1])
    print(f"\n### {title} — {int(dur // 60)}:{dur % 60:04.1f}")
    print(f"  picture share %: {share}")
    print(f"  face runs: {len(runs)} · median {st.median(runs):.1f}s · longest {max(runs):.1f}s")
    print(f"  edit points (all tracks, incl. inside nests): {len(b)} = {len(b) / (dur / 60):.1f}/min · first 60 s: {cold}/min")
    print(f"  nests on V1: {len(nests)} · median {st.median(nest_d) if nest_d else 0:.1f}s · clips per nest median {st.median(nest_n) if nest_n else 0}")
    print(f"  cut zooms with the music OUT: {out}/{len(czs)}  (music clips: {len(music)})")
    print(f"  first picture: {first} · last picture: {last}")
