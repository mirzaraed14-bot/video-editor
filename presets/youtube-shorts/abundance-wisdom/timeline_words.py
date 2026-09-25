#!/usr/bin/env python
"""The job's per-source transcript + the LIVE audio clips of a sequence -> one words.json on the
sequence clock, ready for make_plan.py. No re-transcription: every word comes from the sources'
transcript and is moved to timeline time through the clip that plays it.

A word is kept when its midpoint falls inside a clip's source window (so a word the creator's
trim cut in half goes with whichever side kept most of it). Words are sorted by timeline time.

usage: python timeline_words.py <job_dir> <tracks.txt> <end_seconds> <out_job_dir> [--tracks A1]
  tracks.txt: lines "A1|start|end|inPoint|outPoint|path" (the a23.jsx / a03.jsx reader output)
  sources.json in <job_dir>: key -> {source, offset, window}; the transcript clip is raw/<key>.mp4
"""
import json, os, sys


def norm(p):
    return p.replace('\\', '/').lower()


def main(job, tracks_path, end, out_job, tracks=('A1',)):
    src = json.load(open(os.path.join(job, 'sources.json'), encoding='utf-8'))
    tr = {c['clip']: c['words'] for c in json.load(open(os.path.join(job, 'transcript', 'words.json'),
                                                         encoding='utf-8'))['clips']}
    out, report = [], []
    for line in open(tracks_path, encoding='utf-8'):
        f = line.rstrip('\n').split('|')
        if len(f) < 6 or f[0] not in tracks:
            continue
        start, stop, sin = float(f[1]), float(f[2]), float(f[3])
        if start >= end:
            continue
        sout = sin + (stop - start)
        # the transcript whose window covers this clip's source range
        keys = [k for k, v in src.items() if norm(v['source']) == norm(f[5])
                and sin >= v['offset'] - 0.01 and (v['window'] is None or sout <= v['offset'] + v['window'] + 0.01)]
        if not keys:
            sys.exit('no transcript covers %s %.3f-%.3f of %s' % (f[0], sin, sout, f[5]))
        k = keys[0]
        off = src[k]['offset']
        got = []
        for w in tr[k + '.mp4']:
            if 'start' not in w:
                continue
            mid = (w['start'] + w['end']) / 2 + off
            if sin <= mid < sout:
                t0 = max(start, start + (w['start'] + off - sin))
                t1 = min(stop, start + (w['end'] + off - sin))
                got.append({'w': w['w'], 'start': round(t0, 3), 'end': round(t1, 3), 'prob': w.get('prob', 1)})
        # a sliver the creator's trim left at a clip EDGE (aligner gave up on it) is not a caption word;
        # short prob-0 words mid-clip ("in a bed") are real and stay
        for g in [x for x in (got[:1] + got[-1:]) if x['prob'] == 0 and x['end'] - x['start'] < 0.06]:
            if g in got:
                got.remove(g)
                report.append('   dropped edge fragment %r at %.3f (%d ms, prob 0)' % (
                    g['w'], g['start'], (g['end'] - g['start']) * 1000))
        out += got
        report.append('%s %6.2f-%6.2f  %-10s %8.2f-%8.2f  %s' % (f[0], start, stop, k, sin, sout,
                                                                 ' '.join(g['w'] for g in got)))
    out.sort(key=lambda w: w['start'])
    os.makedirs(os.path.join(out_job, 'transcript'), exist_ok=True)
    json.dump({'language': 'en', 'clips': [{'clip': 'timeline', 'duration': end, 'words': out}]},
              open(os.path.join(out_job, 'transcript', 'words.json'), 'w', encoding='utf-8'), ensure_ascii=False)
    print('\n'.join(report))
    print('%d words on the timeline -> %s' % (len(out), os.path.join(out_job, 'transcript', 'words.json')))


if __name__ == '__main__':
    a = sys.argv[1:]
    tk = ('A1',)
    if '--tracks' in a:
        i = a.index('--tracks'); tk = tuple(a[i + 1].split(',')); del a[i:i + 2]
    main(a[0], a[1], float(a[2]), a[3], tk)
