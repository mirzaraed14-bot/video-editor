#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["numpy"]
# ///
"""style-report.py <reference_dir> — the second stage over style-probe.py's samples: the numbers a style doc quotes.

Reads <ref>/probe/probe.json (required), <ref>/slowmo.json and <ref>/transcript/words.json (optional) and writes
<ref>/report.md + <ref>/report.json. Nothing is re-decoded.

  ZOOM STEPS   face height median-filtered (3 samples = 0.6 s) so a one-sample detector glitch is gone; a step is the
               3-sample median AFTER a sample over the 3-sample median BEFORE it, >= 1.10 (in) or <= 0.90 (out), and it
               must hold for the whole 3-sample window. Levels: every face sample's height over the run's own floor
               (the 10th percentile), so "1.0 / 1.25 / 1.5" reads as the creator's zoom rungs.
  REFRAMES     a face-centre jump >= 5 % of the frame between consecutive samples inside a face run with no size step
               (a jump cut in the same framing, or a re-take with a different lean) — the visible changes a hard-cut
               detector cannot see on a static-camera talking head.
  OVERLAY RUNS consecutive overlay segments merged; each run keeps its internal cut count and a still|video read.
  SLOW-MO      slowmo.json runs that fall on FACE time with a duplicate share well above the face baseline (the face
               cam is a 30p source doubled onto 60p, so baseline ~0.50; >= 0.62 is a real slow-down; >= 0.90 is a still).
  WORD CUTS    hard cuts and zoom steps that land INSIDE a spoken word (>= 60 ms after its start and before its end):
               the creator's "cut it midway while I'm saying it".
  SPEECH       words/min over speech time, pause census (>= 0.3 s gaps), the longest pauses with their neighbours.
"""
import json, os, sys, statistics
import numpy as np

ref = sys.argv[1]
P = json.load(open(os.path.join(ref, 'probe', 'probe.json'), encoding='utf-8'))
S, cuts, segs = P['samples'], P['cuts'], P['segments']
# (a) only the CREATOR's face counts: a game character's face at 0:18 of Fuel System read as "face" (2026-09-21).
#     The creator's head is >= 18 % of the frame height at the widest framing and sits in the middle band.
def mine(f): return bool(f) and f['h'] >= 0.18 and 0.22 <= f['x'] + f['w'] / 2 <= 0.78 and f['score'] >= 0.7
for s in S:
    if s['face'] and not mine(s['face']): s['face'] = None
# (a2) ...and the SET must be behind it. style-set.py stores a 36-bin hue histogram per sample; the set signature is
#      the median histogram over the big-centred-face samples and a sample is ON the set when its cosine similarity
#      to that template is >= 0.70 (measured 2026-09-21: the creator's shots sit >= 0.84 at the 5th percentile at every
#      zoom, game close-ups 0.11-0.61). On-set samples with no detected face still count as the creator on screen.
SET_NOTE = 'no set.json'
sp = os.path.join(ref, 'set.json')
if os.path.exists(sp):
    T = {round(x['t'], 3): np.array(x['hist']) for x in json.load(open(sp, encoding='utf-8'))['samples']}
    big = [T[round(s['t'], 3)] for s in S if s['face'] and round(s['t'], 3) in T]
    if len(big) >= 20:
        tmpl = np.median(np.array(big), 0); tmpl = tmpl / (np.linalg.norm(tmpl) + 1e-9)
        off = on = 0
        for s in S:
            h = T.get(round(s['t'], 3))
            if h is None: continue
            s['set_sim'] = round(float(np.dot(h, tmpl) / (np.linalg.norm(h) + 1e-9)), 3)
            if s['face'] and s['set_sim'] < 0.70: s['face'] = None; off += 1
            elif not s['face'] and s['set_sim'] >= 0.70: s['face'] = dict(x=0.5, y=0.3, w=0, h=0, score=0, inferred=True); on += 1
        SET_NOTE = f'set signature from {len(big)} samples; {off} detected faces rejected as off-set, {on} on-set samples without a detection counted as the creator'
    else:
        SET_NOTE = 'set.json present but too few face samples to learn a signature'
for sg in segs:
    ss = [s for s in S if sg['start'] <= s['t'] < sg['end']]
    if ss:
        sg['face_share'] = round(sum(1 for s in ss if s['face']) / len(ss), 2)
        sg['kind'] = 'face' if sg['face_share'] >= 0.6 else 'overlay'
dur = P['summary']['duration']; FPS = round(1 / (S[1]['t'] - S[0]['t'])) if len(S) > 1 else 5
tc = lambda t: f'{int(t // 60)}:{t % 60:05.2f}'

# ---------- face runs (consecutive face segments) and the per-sample face series
runs, cur = [], None
for sg in segs:
    if sg['kind'] == 'face':
        if cur and abs(cur['end'] - sg['start']) < 1e-6: cur['end'] = sg['end']; cur['shots'] += 1
        else:
            if cur: runs.append(cur)
            cur = dict(start=sg['start'], end=sg['end'], shots=1)
    elif cur: runs.append(cur); cur = None
if cur: runs.append(cur)
for r in runs: r['dur'] = round(r['end'] - r['start'], 2)

def med3(v, i):
    w = [x for x in v[max(0, i - 1):i + 2] if x is not None]
    return statistics.median(w) if w else None

steps, reframes, levels_all = [], [], []
for r in runs:
    ss = [s for s in S if r['start'] <= s['t'] < r['end']]
    h = [s['face']['h'] if s['face'] and s['face'].get('score', 0) >= 0.7 and not s['face'].get('inferred') else None for s in ss]
    cx = [s['face']['x'] + s['face']['w'] / 2 if s['face'] and not s['face'].get('inferred') else None for s in ss]
    cy = [s['face']['y'] + s['face']['h'] / 2 if s['face'] and not s['face'].get('inferred') else None for s in ss]
    hm = [med3(h, i) for i in range(len(h))]
    valid = [x for x in hm if x]
    if len(valid) < 4: continue
    floor = float(np.percentile(valid, 10))
    r['face_h_floor'] = round(floor, 4)
    r['levels'] = sorted({round(x / floor, 2) for x in valid})
    levels_all += [x / floor for x in valid]
    # steps: median of the next 3 over the median of the previous 3, persisting
    for i in range(3, len(hm) - 3):
        b = [x for x in hm[i - 3:i] if x]; a = [x for x in hm[i:i + 3] if x]
        if len(b) < 2 or len(a) < 2: continue
        ratio = statistics.median(a) / statistics.median(b)
        if ratio >= 1.10 or ratio <= 0.90:
            t = ss[i]['t']
            if steps and t - steps[-1]['t'] < 0.6: continue          # one step per window
            hard = any(abs(t - c) <= 0.25 for c in cuts)
            # hold: until the next opposite step or the run's end (the next hard cut inside a run is a jump cut, not an exit)
            steps.append(dict(t=round(t, 2), ratio=round(ratio, 3), dir='in' if ratio > 1 else 'out', level=round(statistics.median(a) / floor, 2),
                              at_hard_cut=hard, run_start=r['start'], run_end=r['end']))
    # reframes: centre jump without a size step
    for i in range(1, len(ss)):
        if cx[i] is None or cx[i - 1] is None or h[i] is None or h[i - 1] is None: continue
        dx, dy = abs(cx[i] - cx[i - 1]), abs(cy[i] - cy[i - 1])
        if max(dx, dy) >= 0.05 and 0.9 < h[i] / h[i - 1] < 1.1:
            reframes.append(dict(t=round(ss[i]['t'], 2), dx=round(dx, 3), dy=round(dy, 3), at_hard_cut=any(abs(ss[i]['t'] - c) <= 0.25 for c in cuts)))
for i, st in enumerate(steps):
    nxt = [x['t'] for x in steps[i + 1:] if x['dir'] != st['dir'] and x['run_start'] == st['run_start']]
    st['hold'] = round(min([st['run_end']] + nxt[:1]) - st['t'], 2)
ins = [s for s in steps if s['dir'] == 'in']
# (b) the background zoom track (style-zoom.py) is the truth for steps and pushes: a face box jitters with a head
#     turn, the neon sign behind it does not. When zoom.json exists its steps replace the box-height ones.
zoom_src = 'face box (fallback)'
zp = os.path.join(ref, 'zoom.json')
if os.path.exists(zp):
    Z = json.load(open(zp, encoding='utf-8')); zoom_src = 'background features'
    steps = []
    for r in Z['runs']:
        for st in r['steps']:
            nxt = [x['t'] for x in r['steps'] if x['t'] > st['t'] and (x['ratio'] < 1) != (st['ratio'] < 1)]
            steps.append(dict(t=round(st['t'], 2), ratio=st['ratio'], dir='in' if st['ratio'] > 1 else 'out', level=None,
                              at_hard_cut=any(abs(st['t'] - c) <= 0.25 for c in cuts), run_start=r['start'], run_end=r['end'],
                              hold=round(min([r['end']] + nxt[:1]) - st['t'], 2), on_face=any(rr['start'] - 0.2 <= st['t'] <= rr['end'] for rr in runs)))
    steps = [st for st in steps if st['on_face']]
    ins = [s for s in steps if s['dir'] == 'in']
    zoom_push = Z['summary'].get('push_pct_per_s'); zoom_level = Z['summary'].get('level_max_median')
else:
    zoom_push = P['summary']['push_median_pct_per_s']; zoom_level = None

# ---------- overlay runs
oruns, cur = [], None
for sg in segs:
    if sg['kind'] == 'overlay':
        if cur and abs(cur['end'] - sg['start']) < 1e-6: cur['end'] = sg['end']; cur['cuts'] += 1; cur['motion'].append(sg['motion'])
        else:
            if cur: oruns.append(cur)
            cur = dict(start=sg['start'], end=sg['end'], cuts=0, motion=[sg['motion']])
    elif cur: oruns.append(cur); cur = None
if cur: oruns.append(cur)
for o in oruns:
    o['dur'] = round(o['end'] - o['start'], 2); o['kind'] = 'still' if statistics.median(o['motion']) < 1.0 else 'video'; o['motion'] = round(statistics.median(o['motion']), 2)

# ---------- slow-mo on face time
slow = []
sm = os.path.join(ref, 'slowmo.json')
if os.path.exists(sm):
    for x in json.load(open(sm, encoding='utf-8'))['runs']:
        on_face = sum(max(0, min(x['end'], r['end']) - max(x['start'], r['start'])) for r in runs)
        if on_face >= 0.6 * x['dur'] and 0.62 <= x['dup_share'] < 0.90:
            slow.append(dict(start=x['start'], end=x['end'], dur=x['dur'], dup=x['dup_share'], speed=round(1 - x['dup_share'] + 0.5 * (1 - x['dup_share']) * 0, 2)))
    # a 30p face doubled onto 60p is 0.50 baseline: the played speed ≈ 0.5 / dup_share
    for x in slow: x['speed'] = round(0.5 / x['dup'], 2)

# (c) the voice devices come from the audio (style-audio.py): a pitch drop is a slow-down, a level break inside a word
#     at a hard cut is a chopped word. Duplicate-frame counting cannot tell a slow-down from a held pose.
audio = None
ap = os.path.join(ref, 'audio.json')
if os.path.exists(ap):
    audio = json.load(open(ap, encoding='utf-8')); slow = [dict(start=x['start'], end=x['end'], dur=x['dur'], dup=None, speed=x['pitch_ratio'], words=x['words']) for x in audio['slowdowns']]
# ---------- words
words, wpm, pauses, word_cuts, word_steps = [], None, [], [], []
wp = os.path.join(ref, 'transcript', 'words.json')
if os.path.exists(wp):
    W = json.load(open(wp, encoding='utf-8'))
    for c in W['clips']: words += c['words']
    words.sort(key=lambda w: w['start'])
    speech = sum(w['end'] - w['start'] for w in words)
    wpm = round(60 * len(words) / dur, 1)
    for a, b in zip(words, words[1:]):
        g = b['start'] - a['end']
        if g >= 0.3: pauses.append(dict(t=round(a['end'], 2), gap=round(g, 2), before=a['w'], after=b['w']))
    def inside(t):
        for w in words:
            if w['start'] + 0.06 <= t <= w['end'] - 0.02: return w
        return None
    for c in cuts:
        w = inside(c)
        if w: word_cuts.append(dict(t=round(c, 2), word=w['w'], into=round(c - w['start'], 2), of=round(w['end'] - w['start'], 2)))
    for st in ins:
        w = inside(st['t'])
        if w: word_steps.append(dict(t=st['t'], word=w['w'], ratio=st['ratio']))
    for x in slow:
        if not x.get('words'): x['words'] = ' '.join(w['w'] for w in words if x['start'] - 0.1 <= w['start'] <= x['end'])
    # (d) a slow-down with the pitch KEPT (Premiere's default) leaves no pitch trace, so the second detector is the
    #     agreement of two independent signals: 3+ consecutive words spoken at <= 0.75x the speaker's median
    #     characters-per-second AND a duplicate-frame run (slowmo.json) over the same face time. Either alone lies
    #     (short emphasised words; a held pose), together they do not (measured 2026-09-21).
    rate = [len(w['w'].strip(".,!?'\"")) / max(w['end'] - w['start'], 0.05) for w in words]
    medr = statistics.median(rate) if rate else 1
    dupruns = []
    if os.path.exists(sm): dupruns = [x for x in json.load(open(sm, encoding='utf-8'))['runs'] if 0.62 <= x['dup_share'] < 0.9]
    two, i = [], 0
    while i < len(words):
        if rate[i] <= 0.7 * medr and len(words[i]['w']) >= 3:
            j = i
            while j < len(words) and (rate[j] <= 0.75 * medr or len(words[j]['w']) < 3): j += 1
            a0, b0 = words[i]['start'], words[j - 1]['end']
            if j - i >= 3 and b0 - a0 >= 0.8 and any(x['start'] <= b0 and x['end'] >= a0 for x in dupruns)                and any(r['start'] <= a0 and b0 <= r['end'] + 0.3 for r in runs):
                two.append(dict(start=round(a0, 2), end=round(b0, 2), dur=round(b0 - a0, 2), dup=None, speed=round(statistics.median(rate[i:j]) / medr, 2),
                                words=' '.join(w['w'] for w in words[i:j])))
            i = j
        else: i += 1
    if not slow: slow = two
    for st in ins: st['word'] = next((w['w'] for w in words if w['start'] - 0.15 <= st['t'] <= w['end'] + 0.15), '')

# ---------- write
lv = np.array(levels_all) if levels_all else np.array([1.0])
hist = {f'{lo:.1f}-{lo + 0.2:.1f}': int(((lv >= lo) & (lv < lo + 0.2)).sum()) for lo in np.arange(1.0, 2.2, 0.2)}
R = dict(duration=dur, hard_cuts=len(cuts), hard_cuts_per_min=round(60 * len(cuts) / dur, 1),
         zoom_steps_in=len(ins), zoom_steps_out=len(steps) - len(ins), zoom_steps_per_min=round(60 * len(ins) / dur, 1),
         zoom_step_median=round(statistics.median([s['ratio'] for s in ins]), 3) if ins else None,
         zoom_step_hold_median=round(statistics.median([s['hold'] for s in ins]), 2) if ins else None,
         zoom_steps_at_hard_cut=sum(1 for s in ins if s['at_hard_cut']),
         zoom_level_share=hist, zoom_level_max_median=round(statistics.median([max(r['levels']) for r in runs if r.get('levels')]), 2) if runs else None,
         reframes=len(reframes), reframes_per_min=round(60 * len(reframes) / dur, 1),
         visible_changes_per_min=round(60 * (len(cuts) + len(ins) + len([x for x in reframes if not x['at_hard_cut']])) / dur, 1),
         face_share=P['summary']['face_share'], face_runs=len(runs), face_run_median=round(statistics.median([r['dur'] for r in runs]), 2) if runs else None,
         face_run_max=max(r['dur'] for r in runs) if runs else None,
         overlay_runs=len(oruns), overlay_runs_per_min=round(60 * len(oruns) / dur, 1), overlay_run_median=round(statistics.median([o['dur'] for o in oruns]), 2) if oruns else None,
         overlay_video=len([o for o in oruns if o['kind'] == 'video']), overlay_still=len([o for o in oruns if o['kind'] == 'still']),
         overlay_internal_cuts=sum(o['cuts'] for o in oruns), longest_face_gap=max((o['dur'] for o in oruns), default=0),
         slowmo=slow, slowmo_source=('pitch' if audio and audio['slowdowns'] else 'word rate + duplicate frames'), chopped=(audio or {}).get('chopped', []), zoom_source=zoom_src, zoom_push_pct_per_s=zoom_push, zoom_bg_level=zoom_level, wpm=wpm, pauses_over_0_3=len(pauses), pauses_over_1=len([p for p in pauses if p['gap'] >= 1.0]),
         word_cuts=word_cuts, word_steps=word_steps, push_pct_per_s=P['summary']['push_median_pct_per_s'],
         zoom_steps=steps, reframe_list=reframes, overlay_runs_list=oruns, face_runs_list=runs, pauses=sorted(pauses, key=lambda p: -p['gap'])[:12])
json.dump(R, open(os.path.join(ref, 'report.json'), 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
L = [f"# style report — {os.path.basename(os.path.abspath(ref))} ({tc(dur)})", '',
     f"- **visible changes: {R['visible_changes_per_min']}/min** = hard cuts {R['hard_cuts_per_min']}/min + zoom steps {R['zoom_steps_per_min']}/min + reframes {R['reframes_per_min']}/min",
     f"- **zoom steps (in):** {R['zoom_steps_in']} · median x{R['zoom_step_median']} · median hold {R['zoom_step_hold_median']} s · {R['zoom_steps_at_hard_cut']} coincide with a hard cut · out-steps {R['zoom_steps_out']}",
     f"- **zoom levels** (face size over each run's floor, share of face samples): {hist} · typical tightest level x{R['zoom_level_max_median']}",
     f"- **gradual push:** {R['zoom_push_pct_per_s']} %/s · typical tightest level over a matched run x{R['zoom_bg_level'] or R['zoom_level_max_median']} (source: {R['zoom_source']})",
     f"- **chopped words at hard cuts (audio breaks inside the word):** {len(R['chopped'])}",
     f"- **face:** {100 * R['face_share']:.0f} % in {R['face_runs']} runs, median {R['face_run_median']} s, longest {R['face_run_max']} s",
     f"- **overlay runs:** {R['overlay_runs']} = {R['overlay_runs_per_min']}/min · median {R['overlay_run_median']} s · {R['overlay_video']} video / {R['overlay_still']} still · {R['overlay_internal_cuts']} cuts inside them · longest without the face {R['longest_face_gap']} s",
     f"- **speech:** {R['wpm']} words/min over the whole runtime · pauses >= 0.3 s: {R['pauses_over_0_3']} · >= 1 s: {R['pauses_over_1']}",
     f"- **slowed stretches ({R['slowmo_source']}):** {len(slow)}", '']
if R['chopped']:
    L += ['## chopped words (the audio itself breaks mid-word at a hard cut)', '', '| t | word | into | drop | context |', '|---|---|---|---|---|']
    L += [f"| {tc(c['t'])} | {c['word']} | {c['into']} s | {c['drop_db']} dB | {c['context']} |" for c in R['chopped']]; L.append('')
if slow:
    L += ['## slowed stretches (the comedy slow-down)', '', '| t | dur | pitch/speed | words |', '|---|---|---|---|']
    L += [f"| {tc(x['start'])} | {x['dur']} s | x{x['speed']} | {x.get('words', '')} |" for x in slow]; L.append('')
if word_cuts:
    L += ['## hard cuts landing INSIDE a word', '', '| t | word | into | word length |', '|---|---|---|---|']
    L += [f"| {tc(w['t'])} | {w['word']} | {w['into']} s | {w['of']} s |" for w in word_cuts]; L.append('')
L += ['## zoom steps in (median-filtered, persistent)', '', '| t | step | to level | hold | on word | hard cut? |', '|---|---|---|---|---|---|']
L += [f"| {tc(s['t'])} | x{s['ratio']} | {('x' + str(s['level'])) if s.get('level') else '-'} | {s['hold']} s | {s.get('word', '')} | {'yes' if s['at_hard_cut'] else ''} |" for s in ins]
L += ['', '## overlay runs', '', '| start | dur | kind | cuts inside |', '|---|---|---|---|']
L += [f"| {tc(o['start'])} | {o['dur']} s | {o['kind']} | {o['cuts']} |" for o in oruns]
L += ['', '## longest pauses', '', '| t | gap | between |', '|---|---|---|']
L += [f"| {tc(p['t'])} | {p['gap']} s | {p['before']} … {p['after']} |" for p in R['pauses']]
open(os.path.join(ref, 'report.md'), 'w', encoding='utf-8').write('\n'.join(L) + '\n')
print('\n'.join(L[:11])); print('   [' + SET_NOTE + ']')
