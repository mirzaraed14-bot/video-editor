#!/usr/bin/env python
"""Write the Abundance Wisdom transition pass JSX for one comp (README § 7).

The creator labels the BLOCK; the label names the transition at the cut AFTER it:
10 Purple = brightness dip to -90 · 16 Dark Green = brightness +30 · 4 Pink = white solid flash
6 Peach = uni.Exposure Blur Mix 50 -> 0 · 14 Cyan = Gaussian Blur 50 -> 0 · anything else = none.
Re-runnable (removes its own previous transition layers), one undo group, reads every value back.

usage: python transition_pass.py "<comp name>" <out.jsx>   then run it with AfterFX -r
       (the result log lands next to the jsx as <name>.txt)
"""
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
comp, out = sys.argv[1], os.path.abspath(sys.argv[2])
log = os.path.splitext(out)[0] + '.txt'
s = open(os.path.join(HERE, 'transition_pass.jsx.tmpl'), encoding='utf-8').read()
s = s.replace('%COMP%', comp).replace('%OUT%', log.replace(os.sep, '/'))
open(out, 'w', encoding='utf-8').write(s)
print('wrote', out, '-> log', log)
