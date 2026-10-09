#!/usr/bin/env python3
"""read-timeline.py <project.xml> "<Sequence name>" [--out file.json] [--depth 2]

Dump EVERY track of a Premiere sequence out of a gunzipped .prproj copy (read-only): per clip its timeline
start/end, source in/out, playback speed, colour label, media path (or the nested sequence it plays, recursed),
and its full effect stack — each component's DisplayName / InstanceName (the creator's saved preset name) /
MatchName and every parameter's static value plus decoded keyframes [(t_s, value)]. Audio clips also carry
Volume Level in dB (Premiere stores level as 10^((dB-15)/20), so 0.1778 = 0 dB) and clip Gain in dB.

Built on projects/gta6-pc-release/brief/readlabels.py (the reference chain is documented there). Ticks/s = 254016000000.
"""
import json, math, re, sys
import xml.etree.ElementTree as ET

TICKS = 254016000000
LABELS = ['Violet', 'Iris', 'Caribbean', 'Lavender', 'Cerulean', 'Forest', 'Rose', 'Mango',
          'Purple', 'Blue', 'Teal', 'Magenta', 'Tan', 'Green', 'Brown', 'Yellow']
xml_path, seq_name = sys.argv[1], sys.argv[2]
out = sys.argv[sys.argv.index('--out') + 1] if '--out' in sys.argv else None
max_depth = int(sys.argv[sys.argv.index('--depth') + 1]) if '--depth' in sys.argv else 2

root = ET.parse(xml_path).getroot()
by_id, by_uid = {}, {}
for el in root.iter():
    if el.get('ObjectID'): by_id[el.get('ObjectID')] = el
    if el.get('ObjectUID'): by_uid[el.get('ObjectUID')] = el
seq_by_uid = {e.get('ObjectUID'): e for e in root.iter('Sequence') if e.get('ObjectUID')}


def ref(el):
    if el is None: return None
    if el.get('ObjectRef'): return by_id.get(el.get('ObjectRef'))
    if el.get('ObjectURef'): return by_uid.get(el.get('ObjectURef'))
    return None


def s(t): return round(int(t) / TICKS, 4) if t not in (None, '') else None


def num(v):
    v = v.strip()
    if v in ('true', 'false'): return v == 'true'
    try: return float(v.rstrip('.')) if re.fullmatch(r'-?[\d.]+(e-?\d+)?', v) else v
    except ValueError: return v


def decode_kf(text):
    """'ticks,value,...;ticks,value,...;' -> [(t_s, value)]  (time is clip-relative SOURCE time)"""
    out = []
    for k in (text or '').split(';'):
        f = k.split(',')
        if len(f) >= 2 and f[0].lstrip('-').isdigit():
            out.append((round(int(f[0]) / TICKS, 4), num(f[1])))
    return out


def components(item):
    co = item.find('ClipTrackItem/ComponentOwner/Components')
    chain = ref(co)
    res = []
    if chain is None: return res
    for c in chain.iter('Component'):
        comp = ref(c)
        if comp is None: continue
        inner = comp.find('Component')
        d = dict(kind=comp.tag, display=(inner.findtext('DisplayName') if inner is not None else None),
                 instance=(inner.findtext('InstanceName') if inner is not None else None),
                 match=comp.findtext('MatchName'),
                 bypass=(inner.findtext('Bypass') == 'true') if inner is not None else False, params={})
        for p in comp.iter('Param'):
            pe = ref(p)
            if pe is None: continue
            name = (pe.findtext('Name') or '').strip() or f"#{pe.findtext('ParameterID')}"
            sk = pe.findtext('StartKeyframe')
            static = num(sk.split(',')[1]) if sk and ',' in sk else None
            kfs = decode_kf(pe.findtext('Keyframes'))
            if name in d['params']: name = f"{name}#{pe.findtext('ParameterID')}"
            d['params'][name] = {'v': static, 'kf': kfs} if kfs else static
        res.append(d)
    return res


def media_of(inner_clip):
    src = ref(inner_clip.find('Source')) if inner_clip is not None else None
    if src is None: return None, None
    sq = src.find('.//SequenceSource/Sequence')
    if sq is not None:
        q = seq_by_uid.get(sq.get('ObjectURef'))
        return 'sequence', (q.findtext('Name') or '').strip() if q is not None else '?'
    m = src.find('.//Media')
    me = ref(m)
    if me is not None:
        return 'file', me.findtext('ActualMediaFilePath') or me.findtext('FilePath') or me.findtext('Title')
    return src.tag, None


def gain_db(clip_el):
    g = clip_el.find('.//Gain') if clip_el is not None else None
    if g is None:
        return None
    try: return round(20 * math.log10(float(g.text)), 2)
    except (TypeError, ValueError): return None


def read_seq(seq, depth):
    res = {'name': (seq.findtext('Name') or '').strip(), 'video': [], 'audio': []}
    for g in seq.find('TrackGroups').findall('TrackGroup'):
        grp = ref(g.find('Second'))
        if grp is None or grp.tag not in ('VideoTrackGroup', 'AudioTrackGroup'): continue
        kind = 'video' if grp.tag == 'VideoTrackGroup' else 'audio'
        fr = grp.find('TrackGroup/FrameRate')
        if kind == 'video' and fr is not None: res['frame_ticks'] = int(fr.text)
        for t in grp.find('TrackGroup/Tracks').findall('Track'):
            tr = ref(t)
            items = []
            for ti in tr.iter('TrackItem'):
                it = ref(ti)
                if it is None or it.tag not in ('VideoClipTrackItem', 'AudioClipTrackItem'): continue
                tri = it.find('ClipTrackItem/TrackItem')
                row = dict(start=s(tri.findtext('Start')), end=s(tri.findtext('End')))
                sc = ref(it.find('ClipTrackItem/SubClip'))
                inner = None
                if sc is not None:
                    row['name'] = (sc.findtext('Name') or '').strip()
                    cl = ref(sc.find('Clip'))
                    inner = cl.find('Clip') if cl is not None else None
                if inner is not None:
                    row['in'], row['out'] = s(inner.findtext('InPoint')), s(inner.findtext('OutPoint'))
                    sp = inner.findtext('PlaybackSpeed')
                    if sp: row['speed'] = round(float(sp), 4)
                    if inner.findtext('IsReversed') == 'true': row['reversed'] = True
                    if inner.findtext('PitchCorrection') or inner.findtext('MaintainAudioPitch'):
                        row['pitch'] = inner.findtext('PitchCorrection') or inner.findtext('MaintainAudioPitch')
                    lab = inner.find('.//asl.clip.label.name')
                    if lab is not None:
                        m = re.match(r'BE\.Prefs\.LabelColors\.(\d+)', (lab.text or '').strip())
                        if m: row['label'] = LABELS[int(m.group(1))] if int(m.group(1)) < 16 else m.group(1)
                    mk, mp = media_of(inner)
                    row['media_kind'], row['media'] = mk, mp
                    if kind == 'audio':
                        gd = gain_db(cl)
                        if gd is not None and abs(gd) > 0.01: row['gain_db'] = gd
                comps = components(it)
                if comps: row['fx'] = comps
                if kind == 'audio':
                    for c in comps:
                        lv = c['params'].get('Level')
                        if lv is not None:
                            v = lv['v'] if isinstance(lv, dict) else lv
                            if isinstance(v, float) and v > 0:
                                row['level_db'] = round(20 * math.log10(v) + 15, 2)
                            if isinstance(lv, dict):
                                row['level_kf_db'] = [(t, round(20 * math.log10(x) + 15, 2) if isinstance(x, float) and x > 0 else x) for t, x in lv['kf']]
                if row.get('media_kind') == 'sequence' and depth < max_depth:
                    q = next((e for e in seq_by_uid.values() if (e.findtext('Name') or '').strip() == row['media']), None)
                    if q is not None: row['nest'] = read_seq(q, depth + 1)
                items.append(row)
            items.sort(key=lambda r: r['start'])
            res[kind].append(items)
    return res


seq = next((e for e in root.iter('Sequence') if (e.findtext('Name') or '').strip() == seq_name), None)
if seq is None: sys.exit(f'{seq_name!r} not found')
data = read_seq(seq, 0)
if out:
    json.dump(data, open(out, 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
for k in ('video', 'audio'):
    for i, tr in enumerate(data[k]):
        if tr:
            print(f"{k[0].upper()}{i + 1}: {len(tr)} clips, {tr[0]['start']:.2f}-{tr[-1]['end']:.2f} s")
