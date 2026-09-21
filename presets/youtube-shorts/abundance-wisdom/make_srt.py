#!/usr/bin/env python
"""captions-plan.json -> .srt + a colour cheat-sheet.

The .srt goes into Premiere as a caption track; "Upgrade Captions To Graphics" turns it into
editable text graphics the creator can style and drop their "Revised Light pop" preset on.
The cheat-sheet lists which word in each caption takes which of their saved Text Styles.

usage: python make_srt.py <job_dir>
"""
import json, os, sys

STYLE_NAME = {'red': 'Red Shade Greators', 'pink': 'Pink Shade', 'magenta': 'Pink Shade',
              'blue': 'Light Blue Shade', 'cyan': 'Light Blue Shade',
              'yellow': 'Orange Yellow Shade'}


def ts(t):
    h, rem = divmod(t, 3600)
    m, s = divmod(rem, 60)
    return '%02d:%02d:%06.3f' % (h, m, s).replace('.', ',') if False else \
        '%02d:%02d:%02d,%03d' % (h, m, int(s), round((s - int(s)) * 1000))


def main(job):
    plan = json.load(open(os.path.join(job, 'captions-plan.json'), encoding='utf-8'))
    srt, rows = [], []
    for i, c in enumerate(plan['captions'], 1):
        lines = [' '.join(w['t'].upper() for w in ln) for ln in c['lines']]
        text = '\n'.join(lines)
        if c.get('italic'):
            text = '<i>' + text + '</i>'
        srt.append('%d\n%s --> %s\n%s\n' % (i, ts(c['start']), ts(c['end']), text))
        coloured = [(w['t'].upper(), w['c']) for ln in c['lines'] for w in ln if w['c'] != 'white']
        rows.append((i, c['start'], c['end'], ' / '.join(lines), c.get('italic', False), coloured))

    out_srt = os.path.join(job, 'outputs', 'seq22-captions.srt')
    os.makedirs(os.path.dirname(out_srt), exist_ok=True)
    open(out_srt, 'w', encoding='utf-8-sig').write('\n'.join(srt))

    md = ['# Caption styling cheat-sheet — Sequence 22', '',
          'After **Upgrade Captions To Graphics**: apply **Gretaros** to every caption,',
          '**Gretaris Italic** to captions 1–11 (the interviewer), then colour the words below.',
          'Everything not listed stays white.', '',
          '| # | in | out | caption | style |', '|---|---|---|---|---|']
    for i, st, en, text, ital, coloured in rows:
        note = ', '.join('**%s** → %s' % (w, STYLE_NAME[c]) for w, c in coloured) or '—'
        md.append('| %d | %.2f | %.2f | %s%s | %s |' % (i, st, en, '*(italic)* ' if ital else '', text, note))
    out_md = os.path.join(job, 'caption-colours.md')
    open(out_md, 'w', encoding='utf-8').write('\n'.join(md) + '\n')

    print('wrote %s (%d captions)' % (out_srt, len(rows)))
    print('wrote %s' % out_md)


if __name__ == '__main__':
    main(sys.argv[1])
