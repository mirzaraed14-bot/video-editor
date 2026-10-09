#!/usr/bin/env python3
"""aggregate.py <timeline.json> <face-cam file substring>[,<another>] — the creator's grammar, counted off one shipped timeline.

Face clips = clips whose media matches the face-cam substrings (top level or inside a nest). Reports: cut zooms (static
scale > 100 on a face clip), pushes (keyframed scale on a face clip or a nest), slow-downs (speed < 1 on any clip),
overlays (every non-face video clip above or on V1), music (Epidemic-like files on audio tracks) with coverage and gaps,
and SFX. Everything as plain numbers plus per-item rows for the catalogue."""
import collections, json, os, statistics as st, sys

d = json.load(open(sys.argv[1], encoding='utf-8'))
FACE = [s.lower() for s in sys.argv[2].split(',')]
BS = chr(92)
base = lambda p: str(p or '').replace(BS, '/').split('/')[-1]
tc = lambda t: f"{int(t // 60)}:{t % 60:05.2f}"
dur = d['video'][0][-1]['end'] if d['video'][0] else 0
isface = lambda r: r.get('media_kind') == 'file' and any(f in base(r.get('media')).lower() for f in FACE)


def motion(r):
    for c in r.get('fx', []):
        if c.get('display') == 'Motion': return c
    return None


def scale_of(r):
    m = motion(r)
    return m['params'].get('Scale') if m else None


cut_zooms, pushes, slows, overlays = [], [], [], []


def walk(items, track, offset, in_nest):
    for r in items:
        t0, t1 = r['start'] + offset, r['end'] + offset
        sc = scale_of(r)
        m = motion(r)
        preset = m.get('instance') if m and m.get('instance') not in (None, 'Motion', '1') else None
        if r.get('speed') and r['speed'] < 0.999:
            slows.append(dict(t=t0, dur=t1 - t0, speed=r['speed'], face=isface(r), track=track, nest=in_nest))
        if isinstance(sc, dict):
            k = sc['kf']; span = k[-1][0] - k[0][0]
            pushes.append(dict(t=t0, dur=t1 - t0, frm=k[0][1], to=k[-1][1], span=span,
                               rate=(k[-1][1] - k[0][1]) / span if span else 0, preset=preset,
                               on='nest' if r.get('media_kind') == 'sequence' else ('face' if isface(r) else base(r.get('media'))), track=track))
        if isface(r):
            if isinstance(sc, (int, float)) and sc > 100.5:
                pos = m['params'].get('Position') if m else None
                cut_zooms.append(dict(t=t0, dur=t1 - t0, scale=sc, pos=pos if pos != '0.5:0.5' else None, nest=in_nest, track=track))
            elif isinstance(sc, (int, float)) and sc < 99.5:
                overlays.append(dict(t=t0, dur=t1 - t0, track=track, media='FACE-PIP', scale=sc, pos=m['params'].get('Position') if m else None))
        elif r.get('media_kind') == 'sequence':
            if r.get('nest'):
                walk(r['nest']['video'][0], track, t0 - (r.get('in') or 0), True)
                for vi, tr in enumerate(r['nest']['video'][1:], 2):
                    for x in tr: overlays.append(dict(t=x['start'] + t0, dur=x['end'] - x['start'], track=f'{track}>nV{vi}', media=base(x.get('media'))))
            if track != 'V1' or True:
                if not any(isface(x) for x in (r.get('nest') or {}).get('video', [[]])[0]):
                    overlays.append(dict(t=t0, dur=t1 - t0, track=track, media=f"NEST {r.get('media')}", scale=sc))
        else:
            fx = [c.get('instance') or c.get('display') for c in r.get('fx', []) if c.get('display') not in ('Motion', 'Opacity')]
            overlays.append(dict(t=t0, dur=t1 - t0, track=track, media=base(r.get('media')) or r.get('name'), scale=sc,
                                 speed=r.get('speed'), fx=fx, label=r.get('label')))


for i, tr in enumerate(d['video']):
    walk(tr, f'V{i + 1}', 0, False)

print(f"# {d['name']} — {tc(dur)}")
cz = [c['scale'] for c in cut_zooms]
if cz:
    print(f"\n## cut zooms on the face: {len(cz)} = {len(cz) / (dur / 60):.1f}/min · median {st.median(cz):.0f} · p25 {st.quantiles(cz, n=4)[0]:.0f} · p75 {st.quantiles(cz, n=4)[2]:.0f} · min {min(cz):.0f} · max {max(cz):.0f}")
    print(f"   hold: median {st.median(c['dur'] for c in cut_zooms):.2f}s · inside nests {sum(c['nest'] for c in cut_zooms)} · with a reposition {sum(1 for c in cut_zooms if c['pos'])}")
    print('   ' + ' '.join(f"{tc(c['t'])}:{c['scale']:.0f}{'*' if c['pos'] else ''}" for c in cut_zooms))
if pushes:
    print(f"\n## pushes: {len(pushes)} · presets {dict(collections.Counter(p['preset'] for p in pushes))}")
    print(f"   rates %/s: median {st.median(p['rate'] for p in pushes):.2f} · on {dict(collections.Counter(p['on'] for p in pushes if p['on'] in ('nest', 'face')))}")
    for p in pushes[:60]:
        print(f"   {tc(p['t'])} {p['dur']:.2f}s {p['on'][:30]} {p['frm']:g}->{p['to']:g} over {p['span']:.2f}s ({p['rate']:.2f}%/s) {p['preset'] or ''}")
print(f"\n## slow-downs: {len(slows)} · speeds {dict(collections.Counter(round(s['speed'], 3) for s in slows))} · on face {sum(s['face'] for s in slows)}")
for s in slows: print(f"   {tc(s['t'])} {s['dur']:.2f}s x{s['speed']} {'FACE' if s['face'] else ''} {s['track']}{' (in nest)' if s['nest'] else ''}")
print(f"\n## overlays / non-face picture: {len(overlays)}")
for o in sorted(overlays, key=lambda o: o['t']):
    print(f"   {tc(o['t'])} {o['dur']:.2f}s {o['track']} {str(o['media'])[:55]}" + (f" scale {o['scale']}" if o.get('scale') not in (None, 100.0) and not isinstance(o.get('scale'), dict) else (' scale-kf' if isinstance(o.get('scale'), dict) else ''))
          + (f" x{o['speed']}" if o.get('speed') and abs(o['speed'] - 1) > 1e-3 else '') + (f" fx {o['fx']}" if o.get('fx') else '') + (f" pos {o['pos']}" if o.get('pos') else ''))
print('\n## audio')
for i, tr in enumerate(d['audio']):
    if not tr or i == 0: continue
    files = collections.Counter(base(r.get('media')) for r in tr)
    cover = sum(r['end'] - r['start'] for r in tr)
    gains = collections.Counter(r.get('gain_db', 0) for r in tr)
    vols = collections.Counter(r.get('level_db', 0) for r in tr)
    gaps = [(tr[j]['end'], tr[j + 1]['start']) for j in range(len(tr) - 1) if tr[j + 1]['start'] - tr[j]['end'] > 0.05]
    print(f"   A{i + 1}: {len(tr)} clips · {dict(files)} · covers {cover:.1f}s ({100 * cover / dur:.0f}%) · gain dB {dict(gains)} · vol dB {dict(vols)} · gaps {len(gaps)}")
