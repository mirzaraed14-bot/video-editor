#!/usr/bin/env python
"""Find a quoted line inside a transcribed source, fuzzily, and print word-exact times.

A cut sheet's timestamps come from whichever upload the researcher watched; the bin copy is
often a different upload (remaster, part split, re-encode), so quotes are located by their
words, never by the sheet's clock.

usage: python find_quote.py <job_dir> <clip> "<start phrase>" ["<end phrase>"] [--context N]
       clip = the raw/ file stem (e.g. sixtymin). Times are printed in SOURCE time
       (the window offset from sources.json is added back).
"""
import json, os, re, sys
from difflib import SequenceMatcher


def norm(w):
    return re.sub(r'[^a-z0-9]', '', w.lower())


def load(job, clip):
    data = json.load(open(os.path.join(job, 'transcript', 'words.json'), encoding='utf-8'))
    c = next(c for c in data['clips'] if os.path.splitext(c['clip'])[0] == clip)
    meta = json.load(open(os.path.join(job, 'sources.json'), encoding='utf-8'))
    off = meta.get(clip, {}).get('offset', 0) or 0
    return c['words'], off


def best(words, phrase, after=0):
    target = [norm(w) for w in phrase.split() if norm(w)]
    n = len(target)
    toks = [norm(w['w']) for w in words]
    best_i, best_s = None, 0.0
    for i in range(after, len(words) - n + 1):
        s = SequenceMatcher(None, target, toks[i:i + n]).ratio()
        if s > best_s:
            best_i, best_s = i, s
    return best_i, best_s, n


def show(words, off, i, j, ctx):
    a, b = max(0, i - ctx), min(len(words), j + 1 + ctx)
    out = []
    for k in range(a, b):
        w = words[k]
        mark = '[' if k == i else ''
        mark2 = ']' if k == j else ''
        out.append('%s%s%s' % (mark, w['w'], mark2))
    return ' '.join(out)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    ctx = 8
    if '--context' in sys.argv:
        ctx = int(sys.argv[sys.argv.index('--context') + 1])
        args = [a for a in args if a != str(ctx)]
    job, clip, start = args[0], args[1], args[2]
    end = args[3] if len(args) > 3 else None
    words, off = load(job, clip)
    i, s1, n1 = best(words, start)
    if end:
        j0, s2, n2 = best(words, end, after=i)
        j = j0 + n2 - 1
    else:
        j, s2 = i + n1 - 1, s1
    print('match %.2f / %.2f' % (s1, s2))
    print('IN  %.3f  (source %s)' % (words[i]['start'] + off, '%d:%06.3f' % divmod(words[i]['start'] + off, 60)))
    print('OUT %.3f  (source %s)' % (words[j]['end'] + off, '%d:%06.3f' % divmod(words[j]['end'] + off, 60)))
    print('LEN %.2fs' % (words[j]['end'] - words[i]['start']))
    print(show(words, off, i, j, ctx))


if __name__ == '__main__':
    main()
