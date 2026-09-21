#!/usr/bin/env python
"""captions.txt (+ the job's words.json) -> captions plan JSON for build.py.

Walks the transcript words in order, consuming them caption by caption, so every caption
lands on the real word timings. Captions are wall-to-wall: each one ends where the next starts.

usage: python make_plan.py <job_dir> [tail_seconds]
"""
import json, os, re, sys
from PIL import ImageFont

FONT = r'C:/Users/affan/AppData/Local/Microsoft/Windows/Fonts/Gretaros-Regular.otf'
FONT_SIZE, TRACKING, WRAP_PX = 52, -0.5, 840
TAG = re.compile(r'<(red|cyan|magenta|yellow|pink|blue)>(.*?)</>', re.S)


def parse_line(line):
    """-> (italic, [(text, colour), ...])"""
    italic = False
    if line.startswith('i:'):
        italic, line = True, line[2:].strip()
    parts, pos = [], 0
    for m in TAG.finditer(line):
        if m.start() > pos:
            parts.append((line[pos:m.start()], 'white'))
        parts.append((m.group(2), m.group(1)))
        pos = m.end()
    if pos < len(line):
        parts.append((line[pos:], 'white'))
    out = []
    for text, colour in parts:
        for w in text.split():
            out.append((w, colour))
    return italic, out


def width(font, words):
    space = font.getlength(' ') + TRACKING
    tot = 0
    for i, (w, _) in enumerate(words):
        tot += font.getlength(w.upper()) + TRACKING * max(0, len(w) - 1)
        if i:
            tot += space
    return tot


def main(job, tail=0.17):
    txt = os.path.join(job, 'captions.txt')
    words = json.load(open(os.path.join(job, 'transcript', 'words.json'), encoding='utf-8'))['clips'][0]
    tw, dur = words['words'], words['duration']
    font = ImageFont.truetype(FONT, FONT_SIZE)

    lines = [l.rstrip() for l in open(txt, encoding='utf-8') if l.strip() and not l.startswith('#')]
    caps, wi = [], 0
    for line in lines:
        italic, parts = parse_line(line)
        n = len(parts)
        if wi + n > len(tw):
            sys.exit('ran past the transcript at: %s' % line)
        chunk = tw[wi:wi + n]
        for (word, _), tword in zip(parts, chunk):
            a = re.sub(r'[^a-z0-9*]', '', word.lower())
            b = re.sub(r'[^a-z0-9]', '', tword['w'].lower())
            if '*' in a:                      # censored word, e.g. s*x
                a = re.match(a.replace('*', '.'), b) and b or a
            if a != b:
                sys.exit('MISMATCH: caption word %r vs transcript %r (line: %s)' % (word, tword['w'], line))
        caps.append({'start': chunk[0]['start'], 'end': None, 'italic': italic,
                     'words': [{'t': w, 'c': c} for (w, c) in parts],
                     'last_word_end': chunk[-1]['end']})
        wi += n
    if wi != len(tw):
        sys.exit('left %d transcript words unused' % (len(tw) - wi))

    for i, c in enumerate(caps):
        c['end'] = caps[i + 1]['start'] if i + 1 < len(caps) else min(dur, c['last_word_end'] + tail)
        del c['last_word_end']
        # merge adjacent words that share a colour so a phrase gets one gradient
        merged = []
        for w in c['words']:
            if merged and merged[-1]['c'] == w['c']:
                merged[-1]['t'] += ' ' + w['t']
            else:
                merged.append(dict(w))
        c['words'] = merged
        # wrap to two lines only when the line would run wide
        flat = [(w['t'], w['c']) for w in c['words']]
        if width(font, flat) > WRAP_PX and len(flat) > 1:
            best, split = None, 1
            for k in range(1, len(flat)):
                diff = abs(width(font, flat[:k]) - width(font, flat[k:]))
                if best is None or diff < best:
                    best, split = diff, k
            c['lines'] = [[{'t': t, 'c': col} for t, col in flat[:split]],
                          [{'t': t, 'c': col} for t, col in flat[split:]]]
        else:
            c['lines'] = [c['words']]
        del c['words']

    plan = {'duration': dur, 'tracking': TRACKING, 'captions': caps}
    out = os.path.join(job, 'captions-plan.json')
    json.dump(plan, open(out, 'w', encoding='utf-8'), indent=1)
    print('%d captions -> %s' % (len(caps), out))
    for c in caps:
        txt = ' / '.join(' '.join(w['t'] for w in ln) for ln in c['lines'])
        cols = ','.join(sorted({w['c'] for ln in c['lines'] for w in ln if w['c'] != 'white'})) or '-'
        print('  %6.2f-%6.2f %-6s %-9s %s' % (c['start'], c['end'],
                                              'italic' if c['italic'] else '', cols, txt))


if __name__ == '__main__':
    main(sys.argv[1], float(sys.argv[2]) if len(sys.argv) > 2 else 0.17)
