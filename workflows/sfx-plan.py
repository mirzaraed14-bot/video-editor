#!/usr/bin/env python3
"""sfx-plan.py: turn a job's PLACED graphics into an SFX plan (pipeline step 6, universal).

  uv run workflows/sfx-plan.py projects/<job>              # write hf-graphics/sfx-plan.{json,md}
  uv run workflows/sfx-plan.py projects/<job> --dry        # print the cut sheet, write nothing
  uv run workflows/sfx-plan.py projects/<job> --candidate  # park it as sfx-plan.candidate.{json,md} to merge by hand

Reads: hf-graphics/placement.json (the placed rows), each row's comp HTML (the registry calls it
makes and, for a text animation, its per-word spans), graphics-plan.json (the preset, the cell kinds) and
the preset's sfx.json (event -> sound -> slice -> class -> target peak). Writes one row per sound:

  {"id", "gid", "event", "at", "file", "src_in", "src_out", "level_db", "track", "cls", "note"}

`at` is the timeline time in seconds, frame-snapped. `track` is the 0-based audio track index
from the preset map (A2 primary, A3/A4 layers). `level_db` is the clip Volume Level that puts the
measured slice peak on the class target. Nothing here touches an editor; placement is per lane
(LANES.md step 6). The WHY and the numbers: presets/youtube/default/sfx.md.

Comp calls are found by a static parse of the comp's script. The `at` argument is evaluated with
the comp's own constants (F, SF, DUR, any `const NAME = <number>`); a call inside a loop over an
array literal is expanded over that array; anything else is listed under ⚠ in the cut sheet for
a hand entry, never guessed.
"""
import html as htmlmod, json, math, os, re, subprocess, sys
for _s in (sys.stdout, sys.stderr):  # Windows pipes default to cp1252, which cannot encode the status glyphs
    try:
        if (getattr(_s, "encoding", "") or "").lower().replace("-", "") != "utf8":
            _s.reconfigure(encoding="utf-8")
    except Exception:
        pass
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CALLS = ('pop', 'slam', 'riseIn', 'riseOut', 'exit', 'slideIn', 'slideOut', 'drawOn', 'countUp', 'reveal', 'flash')
_peak_cache = {}


def slice_peak(path, a, b):
    key = (path, round(a, 3), round(b, 3))
    if key in _peak_cache: return _peak_cache[key]
    r = subprocess.run(['ffmpeg', '-hide_banner', '-nostats', '-i', path, '-ss', str(a), '-t', str(max(b - a, 0.05)),
                        '-af', 'volumedetect', '-f', 'null', '-'], capture_output=True, text=True).stderr   # -ss AFTER -i: exact
    m = re.search(r'max_volume: (-?[0-9.]+)', r)
    v = float(m.group(1)) if m else 0.0
    _peak_cache[key] = v
    return v


_dur_cache = {}


def file_dur(path):
    if path not in _dur_cache:
        _dur_cache[path] = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', path],
                                                capture_output=True, text=True).stdout.strip() or 0)
    return _dur_cache[path]


def probe_fps(path):
    r = subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries', 'stream=r_frame_rate',
                        '-of', 'csv=p=0', path], capture_output=True, text=True).stdout
    n, _, d = r.strip().split('\n')[0].strip(',').partition('/')
    return float(n) / float(d or 1)


class Evaluator:
    """Evaluate a comp's time expressions with its own constants. Refuses anything it cannot bind."""
    SAFE = re.compile(r'^[\w\s+\-*/().]+$')                    # names, numbers, arithmetic, Math.round(...)

    def __init__(self, script, fps):
        self.names = {'F': 1 / fps, 'Math': type('M', (), {'round': staticmethod(lambda x: math.floor(x + 0.5)), 'floor': staticmethod(math.floor), 'ceil': staticmethod(math.ceil), 'min': staticmethod(min), 'max': staticmethod(max)})}
        for m in re.finditer(r'(?:(?:const|let|var)\s+|,\s*)(\w+)\s*=\s*([-\d.]+(?:\s*[/*+\-]\s*[-\d.]+)*)\s*(?=[;,\n])', script):
            try: self.names[m.group(1)] = eval(m.group(2), {'__builtins__': {}}, {})     # `const F = .., DUR = .., AUTO_T = ..;` binds all three
            except Exception: pass
        m = re.search(r'init\(\{([^}]*)\}', script)               # HF.init({fps, stepFps, dur})
        if m:
            for k, v in re.findall(r'(\w+)\s*:\s*([\w.\d/*+\- ]+)', m.group(1)):
                try: self.names[k] = eval(v, {'__builtins__': {}}, dict(self.names))
                except Exception: pass
            if 'dur' in self.names: self.names.setdefault('DUR', self.names['dur'])
            if self.names.get('stepFps'): self.names['SF'] = 1 / self.names['stepFps']
        self.names.setdefault('SF', self.names['F'])

    def ev(self, expr, extra=None):
        if not self.SAFE.match(expr): raise ValueError(expr)
        return float(eval(expr, {'__builtins__': {}}, dict(self.names, **(extra or {}))))


def split_args(s):
    out, depth, cur, q = [], 0, '', None
    for ch in s:
        if q:
            cur += ch
            if ch == q: q = None
            continue
        if ch in '\'"': q = ch; cur += ch; continue
        if ch in '([{': depth += 1
        if ch in ')]}': depth -= 1
        if ch == ',' and depth == 0: out.append(cur.strip()); cur = ''; continue
        cur += ch
    if cur.strip(): out.append(cur.strip())
    return out


LOOP = re.compile(r'\[\s*(\[[^\[\]]*\](?:\s*,\s*\[[^\[\]]*\])*)\s*\]\s*\.forEach\(\s*\(\s*\[([^\]]*)\]\s*\)\s*=>\s*')


def literal(tok):
    tok = tok.strip()
    if tok[:1] in '\'"': return tok[1:-1]
    try: return float(tok)
    except ValueError: return tok


def type_targets(html):
    """Selectors (#id / .class) of every element whose OWN text is words: that is TYPE. Type never pops
    (2026-09-10): it rises with the scissors or slams with the Impact, whatever the comp calls.
    A node/card/row/chip whose words sit in a child element is a surface, not type."""
    from html.parser import HTMLParser as _HP
    class P(_HP):
        def __init__(self):
            super().__init__(convert_charrefs=True); self.stack, self.els = [], []
        def handle_starttag(self, tag, attrs):
            a = dict(attrs); el = dict(id=a.get('id'), cls=(a.get('class') or '').split(), text='')
            self.els.append(el)
            if tag not in ('br', 'img', 'input', 'meta', 'link', 'path', 'circle', 'rect', 'polygon', 'line', 'use'): self.stack.append((tag, el))
        def handle_startendtag(self, tag, attrs): pass
        def handle_endtag(self, tag):
            for i in range(len(self.stack) - 1, -1, -1):
                if self.stack[i][0] == tag: del self.stack[i:]; return
        def handle_data(self, data):
            if self.stack: self.stack[-1][1]['text'] += data
    p = P(); p.feed(re.sub(r'<(script|style)[^>]*>.*?</\1>', '', html, flags=re.S))
    out = set()
    for el in p.els:
        if not any(c.isalpha() for c in el['text']): continue      # one letter is a word too ("i")
        if el['id']: out.add('#' + el['id'])
        for c in el['cls']: out.add('.' + c)
    return out


COMPLETION_CLASSES = {'hi', 'done', 'ok', 'check', 'chk', 'success', 'complete', 'completed', 'finished', 'payoff', 'win', 'green'}
COMPLETION_TEXT = re.compile(r'\b(100 ?%|done|complete|completed|finished|postable|success)\b', re.I)
GREEN = ('#2ff58a', '--green', '#22c55e', '#16a34a', '#28c840', '#0ca30c', '#2ecc71', 'rgba(47,245,138')


def completion_targets(html):
    """Selectors (#id / .class) of every element that SHOWS COMPLETION: a finished node, a check, 100 %, the green
    state. Sound follows meaning before mechanism (2026-09-10: "in special scenarios like this where it's green
    or showing completion or goodness, it's nice to represent that with sound"): such an element rings the bell
    (`payoff`) when it arrives instead of popping. Read off the markup: a completion class, completion words in its own
    text, a green fill/stroke on it or inside it, a green CSS rule whose compound selector it satisfies, or an explicit
    data-sfx="payoff"; data-sfx="pop" opts out."""
    from html.parser import HTMLParser as _HP
    css = ''.join(re.findall(r'<style[^>]*>(.*?)</style>', html, re.S))
    green_compounds = []
    for sel, block in re.findall(r'([^{}]+)\{([^{}]*)\}', css):
        if any(g in block for g in GREEN):
            for branch in sel.split(','):
                toks = re.findall(r'\.([A-Za-z0-9_-]+)', branch.strip().split(' ')[-1])
                if toks: green_compounds.append(set(toks))
    class P(_HP):
        def __init__(self):
            super().__init__(convert_charrefs=True); self.stack, self.els = [], []
        def handle_starttag(self, tag, attrs):
            a = dict(attrs); cls = set((a.get('class') or '').split())
            el = dict(id=a.get('id'), cls=cls, text='', done=False, opt=a.get('data-sfx'))
            sig = bool(cls & COMPLETION_CLASSES) or any(g in (a.get('fill', '') + a.get('stroke', '') + a.get('style', '')) for g in GREEN) \
                  or any(c <= cls for c in green_compounds) or a.get('data-sfx') == 'payoff'
            if sig:
                el['done'] = True
                for _, anc in self.stack: anc['done'] = True          # the green check inside a node marks the node
            self.els.append(el)
            if tag not in ('br', 'img', 'input', 'meta', 'link', 'path', 'circle', 'rect', 'polygon', 'line', 'use'): self.stack.append((tag, el))
        def handle_startendtag(self, tag, attrs): self.handle_starttag(tag, attrs); self.handle_endtag(tag)
        def handle_endtag(self, tag):
            for i in range(len(self.stack) - 1, -1, -1):
                if self.stack[i][0] == tag: del self.stack[i:]; return
        def handle_data(self, data):
            if self.stack: self.stack[-1][1]['text'] += data
    p = P(); p.feed(re.sub(r'<(script|style)[^>]*>.*?</\1>', '', html, flags=re.S))
    out = set()
    for el in p.els:
        if el['opt'] in ('pop', 'none'): continue
        if el['done'] or COMPLETION_TEXT.search(el['text'] or ''):
            if el['id']: out.add('#' + el['id'])
            for c in el['cls']: out.add('.' + c)
    return out


def sfx_markers(html):
    """selector -> {event, file} from data-sfx attributes in the comp: the judgement call, named where the element is
    authored. The palette is the DOCUMENTED map only (2026-09-10; owner: presets/youtube/default/sfx.md
    § Sound follows MEANING). data-sfx="<event>" swaps the element's mechanical sound for any event documented in
    sfx.json (emphasis, gunshot, processing, click included); data-sfx="none" silences the element; data-sfx-file is
    parsed only so it can be REFUSED with a warning (sfx.md § Sound follows MEANING, sfx.json `_judgement`: only
    sounds the user has heard and documented are ever placed)."""
    from html.parser import HTMLParser as _HP
    found = {}
    class P(_HP):
        def handle_starttag(self, tag, attrs):
            a = dict(attrs)
            if not any(k.startswith('data-sfx') for k in a): return
            m = {k: v for k, v in (('event', a.get('data-sfx')), ('file', a.get('data-sfx-file'))) if v}
            keys = (['#' + a['id']] if a.get('id') else []) + ['.' + c for c in (a.get('class') or '').split()]
            for k in keys: found[k] = m
        def handle_startendtag(self, tag, attrs): self.handle_starttag(tag, attrs)
    P().feed(re.sub(r'<(script|style)[^>]*>.*?</\1>', '', html, flags=re.S))
    return found


def comp_events(html, fps):
    """[(event, at_seconds, note)] from a comp's registry calls, plus ⚠ notes it could not bind."""
    script = '\n'.join(re.findall(r'<script[^>]*>(.*?)</script>', html, re.S))
    ev = Evaluator(script, fps)
    events, warns = [], []
    consumed = []                                                  # spans handled by the loop expander
    # `[[a, b, 1.1], ...].forEach(([x, y, at]) => BODY)`: bind the params per tuple, evaluate the body's calls
    for lm in LOOP.finditer(script):
        tuples = [[literal(x) for x in split_args(t[1:-1])] for t in split_args(lm.group(1))]
        params = [x.strip() for x in lm.group(2).split(',')]
        i = lm.end(); depth = 0; j = i
        if script[i] == '{':
            while j < len(script):
                depth += {'{': 1, '}': -1}.get(script[j], 0); j += 1
                if depth == 0: break
            body = script[i:j]
        else:
            while j < len(script) and script[j] not in ';\n': j += 1
            body = script[i:j]
        consumed.append((lm.start(), j))
        for tup in tuples:
            bind = {k: v for k, v in zip(params, tup)}
            for cm in re.finditer(r'\b(' + '|'.join(CALLS) + r')\(([^()]*)\)', body):
                args = split_args(cm.group(2))
                if len(args) < 2: continue
                sel = bind.get(args[0].strip(), args[0])
                try: events.append((cm.group(1), ev.ev(args[1], {k: v for k, v in bind.items() if isinstance(v, float)}), str(sel)))
                except Exception: warns.append(f'{cm.group(1)}({args[0]}, {args[1]}) in a loop could not be evaluated')
    FOR = re.compile(r'for\s*\(\s*(?:const|let|var)\s*\[([^\]]*)\]\s*of\s*(\[[^;]*?\]|\w+)\s*\)\s*')
    for fm in FOR.finditer(script):
        src = fm.group(2)
        if not src.startswith('['):                                  # `of ROWS` -> the const array literal
            cm_ = re.search(r'(?:const|let|var)\s+' + re.escape(src) + r'\s*=\s*(\[[^;]*?\])\s*;', script)
            if not cm_: warns.append(f'for-of over {src}: array not found'); continue
            src = cm_.group(1)
        tuples = [[literal(x) for x in split_args(t[1:-1])] for t in split_args(src[1:-1]) if t.startswith('[')]
        params = [x.strip() for x in fm.group(1).split(',')]
        i = fm.end(); j = i
        if script[i] == '{':
            depth = 0
            while j < len(script):
                depth += {'{': 1, '}': -1}.get(script[j], 0); j += 1
                if depth == 0: break
        else:
            while j < len(script) and script[j] not in ';\n': j += 1
        body = script[i:j]; consumed.append((fm.start(), j))
        for tup in tuples:
            bind = {k: v for k, v in zip(params, tup)}
            for cm in re.finditer(r'\b(' + '|'.join(CALLS) + r')\(([^()]*(?:\([^()]*\)[^()]*)*)\)', body):
                args = split_args(cm.group(2))
                if len(args) < 2: continue
                sel = bind.get(args[0].strip(), args[0])
                try: events.append((cm.group(1), ev.ev(args[1], {k: v for k, v in bind.items() if isinstance(v, float)}), str(sel)))
                except Exception: warns.append(f'{cm.group(1)}({args[0]}, {args[1]}) in a for-of could not be evaluated')
    # hand-rolled motion the registry would have named: a tween that carries an element a frame-width
    # in x is a slide, a stroke-dash reveal is a draw-on (pre-registry comps, and scene moves inside
    # a full-screen that no registry primitive covers)
    for fm_ in re.finditer(r'tl\.set\(([^,]+),\s*\{\s*opacity:\s*o\s*\},\s*(?:(.+?)\s*\+\s*)?f\s*\*\s*F\s*\)', script):
        try: events.append(('flash', ev.ev(fm_.group(2).strip()) if fm_.group(2) else 0.0, fm_.group(1).strip() + ' (hand-rolled strobe)'))
        except Exception:
            if not re.fullmatch(r'\w+', (fm_.group(2) or '').strip()): warns.append(f'flash {fm_.group(1).strip()} at {fm_.group(2).strip()}: could not be evaluated')
    for hm in re.finditer(r'tl\.to\(([^,]+),\s*\{([^}]*)\},\s*([^)]+)\)', script):
        props, at_expr = hm.group(2), hm.group(3).strip()
        xm = re.search(r'\bx:\s*(-?\d+(?:\.\d+)?)', props)
        kind = None
        if xm and abs(float(xm.group(1))) >= 900: kind = 'slideOut' if float(xm.group(1)) < 0 else 'slideIn'
        elif re.search(r'strokeDashoffset:\s*0\b', props): kind = 'drawOn'
        if not kind: continue
        try: events.append((kind, ev.ev(at_expr), hm.group(1).strip() + ' (hand-rolled)'))
        except Exception:
            if not re.fullmatch(r'\w+', at_expr):                    # a bare unknown name is a helper's parameter, not a call
                warns.append(f'{kind} {hm.group(1).strip()} at {at_expr}: could not be evaluated')
    for m in re.finditer(r'\b(' + '|'.join(CALLS) + r')\(', script):
        if any(a <= m.start() < b for a, b in consumed): continue
        name = m.group(1)
        i = m.end(); depth = 1; j = i
        while j < len(script) and depth:
            depth += {'(': 1, ')': -1}.get(script[j], 0); j += 1
        args = split_args(script[i:j - 1])
        if name == 'exit' and (not args or len(args) < 2):
            continue                                              # exit() at the comp end: silent anyway
        if len(args) < 2: continue
        at_expr, sel = args[1], args[0]
        extra = {}
        if 'dur' in [a.strip() for a in args[2:3]]: pass
        try:
            if re.search(r'\bi\b', at_expr):
                # a loop over an array literal just above the call: expand over its length
                before = script[max(0, m.start() - 400):m.start()]
                arr = re.findall(r'\[([^\[\]]*)\]\s*\.forEach', before)
                n = len(split_args(arr[-1])) if arr else None
                if n is None:
                    warns.append(f'{name}({sel}, {at_expr}) runs in a loop this parser cannot size')
                    continue
                for k in range(n):
                    events.append((name, ev.ev(at_expr, {'i': k}), f'{sel} [{k}]'))
            else:
                t = ev.ev(at_expr)
                dur = None
                if name == 'countUp' and len(args) > 2:
                    try: dur = ev.ev(args[2])
                    except Exception: dur = None
                if name == 'reveal' and len(args) > 2 and args[2][:1] in '\'"`':
                    # reveal(sel, at, text): the registry reveals 2-6 words per beat on a fixed burst
                    # pattern, doubling on punctuation; replay that on the literal text for the duration
                    text = args[2][1:-1]; words_ = text.split(' '); sizes = [3, 5, 2, 4, 6, 3, 2, 5, 4, 3, 6, 2]
                    beat = ev.names['SF'] if ev.names.get('stepFps') else 2 * ev.names['F']
                    i_ = 0; k_ = 0; dur = 0.0
                    while i_ < len(words_):
                        i_ = min(len(words_), i_ + sizes[k_ % len(sizes)]); k_ += 1
                        dur += 2 * beat if re.search(r'[.,;:!?]$', ' '.join(words_[:i_])) else beat
                elif name == 'reveal':
                    warns.append(f'reveal({sel}) has no literal text: give it a hand entry with dur')
                events.append((name, t, sel if dur is None else f'{sel} dur {dur:.2f}'))
                if dur is not None: events[-1] = (name, t, events[-1][2], dur)
        except Exception:
            warns.append(f'{name}({sel}, {at_expr}) could not be evaluated')
    return events, warns


def find_comp(hf, gid, render):
    """Resolve within the placed render's build folder first; never score a retired sibling comp.

    Older slug-named jobs can fall back across folders only when the best match is unique.
    An ambiguous source is an error, not a filesystem-order editorial decision.
    """
    base = Path(render).stem
    local = Path(render).parent.parent / 'compositions'
    scopes = [list(local.glob('*.html'))]
    if not (Path(render).parent.name == 'renders' and local.parent.parent.resolve() == hf.resolve()):
        scopes.append(list(hf.glob('*/compositions/*.html')))
    for comps in scopes:
        named = [c for c in comps if base == c.stem or base.startswith(c.stem + '-')]
        candidates = named or [c for c in comps if c.stem == gid]
        if not candidates:
            candidates = [c for c in comps if c.stem.startswith(gid + '-')]
        if candidates:
            if named:
                longest = max(len(c.stem) for c in candidates)
                candidates = [c for c in candidates if len(c.stem) == longest]
            if len(candidates) != 1:
                raise ValueError(f'{gid}: ambiguous composition for {render}: ' + ', '.join(map(str, candidates)))
            return candidates[0]
    return None


def text_events(html):
    """One event per word span; the word comes from data-w when the builder wrote it, else the span text."""
    out = []
    for m in re.finditer(r'<span class="(w[^"]*)" data-t="([\d.]+)"([^>]*)>([^<]*)', html):
        w = re.search(r'data-w="([^"]*)"', m.group(3))
        out.append(('word', float(m.group(2)), htmlmod.unescape((w.group(1) if w else m.group(4)).strip()), m.group(1)))
    return out


def write_plan(hf, rows, md, candidate=False):
    """Write the cut sheet; --candidate parks it beside an approved plan instead of replacing it."""
    stem = 'sfx-plan.candidate' if candidate else 'sfx-plan'
    prev = hf / 'sfx-plan.json'
    changed = []
    if not candidate and prev.exists():
        key = lambda rs: {g: sorted(((r.get('event'), r.get('at'), r.get('level_db'), r.get('track')) for r in rs if r.get('gid') == g), key=repr)
                          for g in {r.get('gid') for r in rs}}
        old, new = key(json.loads(prev.read_text(encoding='utf-8'))), key(rows)
        changed = sorted(g for g in set(old) | set(new) if old.get(g) != new.get(g))
    (hf / f'{stem}.json').write_text(json.dumps(rows, indent=1) + '\n')
    (hf / f'{stem}.md').write_text(md, encoding='utf-8')   # cp1252 is the Windows default and the sheet has arrows in it
    print(f'wrote {hf / (stem + ".json")} (+ {stem}.md)' + ('; existing sfx-plan.json unchanged. '
          'Merge affected graphic IDs, preserving approved cues and levels elsewhere.' if candidate else ''))
    if changed: print('rows changed vs the previous plan: ' + ', '.join(changed))
    return 0


def main():
    a = sys.argv[1:]
    if not a: sys.exit(__doc__)
    job = Path(a[0]).resolve(); dry = '--dry' in a
    hf = job / 'hf-graphics'
    rows_in = json.load(open(hf / 'placement.json'))
    plan = json.load(open(job / 'graphics-plan.json'))
    preset_dir = ROOT / plan.get('preset', 'presets/youtube/default')
    if preset_dir.is_file(): preset_dir = preset_dir.parent          # plans point at the style doc
    if not (preset_dir / 'sfx.json').exists():
        # SFX runs on every format (2026-09-04); only youtube/default ships a sound map so far, so a
        # short-form preset borrows it — one sound vocabulary, house-wide — and the report says so
        print(f"[sfx-plan] {preset_dir.relative_to(ROOT)} has no sfx.json: using presets/youtube/default/sfx.json (the house sound map)")
        preset_dir = ROOT / 'presets/youtube/default'
    cfg = json.load(open(preset_dir / 'sfx.json', encoding='utf-8'))
    # A preset may carry ONLY what differs from the house map, as `"_extends": "presets/youtube/default"`.
    # The sound vocabulary is house-wide (one sound per motion class, everywhere) but the TRACK MAP is
    # per timeline: affan-afterhours puts the creator's own music on A2, so its SFX layers shift up one
    # (2026-09-16). Copying the whole map to change three numbers is how a preset drifts.
    if cfg.get('_extends'):
        base = json.load(open(ROOT / cfg['_extends'] / 'sfx.json', encoding='utf-8'))
        for k, v in cfg.items():
            if k == '_extends': continue
            if isinstance(v, dict) and isinstance(base.get(k), dict): base[k].update(v)
            else: base[k] = v
        print(f"[sfx-plan] {preset_dir.name}/sfx.json extends {cfg['_extends']}: "
              + ', '.join(k for k in cfg if k != '_extends') + " overridden")
        cfg = base
    lib = ROOT / cfg['library']
    fps = probe_fps(next(r['file'] for r in rows_in if os.path.exists(r['file'])))
    F = 1 / fps
    snap = lambda t: round(round(t / F) * F, 4)
    T = cfg['targets_dbfs']; TR = cfg['tracks']; EV = cfg['events']
    rot = {}
    out, warns = [], []
    seen_gids = set()
    # hand entries for comps whose motion is not written with the registry (pre-2026-09-02 jobs):
    # hf-graphics/sfx-hand.json = [{"gid", "event", "at": <comp-relative seconds>, "note"?, "dur"?}]
    HAND = {}
    hp = hf / 'sfx-hand.json'
    if hp.exists():
        for h in json.load(open(hp)): HAND.setdefault(h['gid'], []).append(h)
    # the plan cell behind a placed row (id equal, or the row id is <planid>-<slug>): its KIND decides
    # some pairings (a pop inside a list/card graphic is a row tick, not an object)
    cells = {b['id']: b for b in plan.get('beats', []) if b.get('graphic')}
    def cell_kind(gid):
        c = cells.get(gid) or next((cells[k] for k in sorted(cells, key=len, reverse=True) if gid.startswith(k + '-')), None)
        return (c or {}).get('kind', '')
    first_cut_in = True

    def add(gid, event, at, note='', dur=None, level=None, auto=True, hand=False):
        spec = EV.get(event)
        if spec is None or not isinstance(spec, dict): return
        if auto and spec.get('hand_only'): return
        path = str(lib / spec['file'])
        if not os.path.exists(path): warns.append(f'{event}: {spec["file"]} missing from {lib}'); return
        k = rot.get(event, 0); rot[event] = k + 1
        s_in, s_out = (0.0, file_dur(path)) if spec.get('whole_file') else spec['slices'][k % len(spec['slices'])]
        if spec.get('fit') == 'duration' and dur: s_out = min(s_out, s_in + max(dur, 0.2))
        at = at - spec.get('lead_frames', 0) * F + spec.get('offset_frames', 0) * F
        peak = slice_peak(path, s_in, s_out)
        if peak < -40:
            warns.append(f'{event}: slice {s_in}-{s_out} of {spec["file"]} is silent ({peak} dBFS), skipped'); return
        lvl = int(round(level)) if level is not None else (spec['level_db'] if 'level_db' in spec else min(6, round(T[spec['class']] - peak)))   # hand > fixed > class band
        out.append(dict(gid=gid, event=event, at=snap(at), file=path, src_in=round(s_in, 3), src_out=round(s_out, 3),
                        level_db=lvl, cls=spec['class'], note=note, hand=hand, peak=peak))

    for r in sorted(rows_in, key=lambda r: r['start']):
        gid, kind, start = r['id'], r.get('kind'), float(r['start'])
        if kind == 'captions': continue     # the caption layer has no comp and makes no sound (captions are silent by design)
        try:
            comp = find_comp(hf, gid, r['file'])
        except ValueError as e:
            warns.append(f"{e}; leave exactly one composition matching that id in the placed render's own compositions/ "
                         'folder (retire the obsolete comp and its builder spec out of the scanned folders), or name the '
                         'part comp in the render filename, then re-run')
            continue
        if not comp:
            warns.append(f'{gid}: no comp found under hf-graphics/*/compositions; events for it need a hand entry'); continue
        html = comp.read_text(encoding='utf-8')
        hand = HAND.get(gid, []); seen_gids.add(gid)
        drop = {d for h in hand for d in h.get('drop', [])}
        words = text_events(html)                                  # word spans: a text animation, or a line inside a full-screen
        # a hand entry addressed by WORD (any event) resolves to that span's time; emphasis also
        # takes the word's scissors away
        emph = set()
        for h in hand:
            if not h.get('word') or h.get('at') is not None: continue
            key = h['word'].lower().strip('.,!?')
            hit = next((t for _, t, w_, _ in words if w_.lower().strip('.,!?') == key), None)
            if hit is None: warns.append(f"{gid}: hand entry word {h['word']!r} matches no span in {comp.name}"); continue
            h['at'] = hit
            if h['event'] == 'emphasis': emph.add(key)
        # the text builder's ENTRANCE decides the word sound: rise -> scissors (a RED word -> the
        # Error Buzz, an EMPHASIS hand entry -> the Impact), punch/pop -> the pop, slam -> the
        # Impact stamp, flicker -> ONE Neon Flicker at the block's first word (the strobe start)
        ent = (re.search(r'const ENTRANCE\s*=\s*"(\w+)"', html) or [None, 'rise'])[1]
        if ent == 'punch':                                          # the builder emits pop AND slam as "punch"; the shape tells them apart
            over = re.search(r'POP_OVER\s*=\s*([\d.]+)', html)
            ent = 'pop' if over and float(over.group(1)) > 0 else 'slam'
        if ent == 'flicker' and words:
            add(gid, 'word-flicker', start + min(t for _, t, _, _ in words), 'flicker strobe: ' + ' '.join(w_ for _, _, w_, _ in words))
        else:
            wev = {'pop': 'word-pop', 'slam': 'word-slam'}.get(ent, 'word')
            for ev, t, w_, cls in words:
                key = w_.lower().strip('.,!?')
                if key in emph: continue                            # the emphasis hand entry places its own row
                if wev == 'word' and 'red' in cls.split() and 'word-negative' not in drop: add(gid, 'word-negative', start + t, f'{w_} (red: negation)'); continue
                if wev not in drop: add(gid, wev, start + t, f'{w_} ({ent})' if ent != 'rise' else w_)
        if kind == 'text' and words and not any(h.get('at') is not None for h in hand): continue   # a pure text animation has no other events (a hand entry keeps going)
        evs, w = comp_events(html, fps)
        if any(h.get('event') == 'reveal' for h in hand):            # the hand entry IS the answer to that warning
            w = [x for x in w if 'no literal text' not in x]
        ck = cell_kind(gid)
        evs = [e for e in evs if e[0] not in drop]
        if ck in ('list', 'card'): evs = [('row-tick',) + tuple(e[1:]) if e[0] == 'pop' else e for e in evs]   # rows tick on, objects pop
        # TYPE in a hand comp takes the text sounds (2026-09-10: type never pops; text = the scissors on a
        # rise, the Impact on a slam): an element whose OWN text is words, found from the markup, no marker needed
        tt = type_targets(html)
        done = completion_targets(html)
        marks = sfx_markers(html); used_marks = set()
        def _sel(e): return str(e[2]).strip().strip("'\"").split(' ')[-1] if len(e) > 2 else ''
        remap = []
        for e in evs:
            s = _sel(e)
            m = marks.get(s)
            if m:                                                       # the author named a DOCUMENTED sound: it wins over every rule below
                used_marks.add(id(m))
                if m.get('event') == 'none': continue
                if m.get('file'): warns.append(f"{gid}: data-sfx-file={m['file']!r} on {s} ignored: only the events documented in sfx.json may be used (2026-09-10: nobody here can listen to a file; document it first)")
                elif m.get('event') and m['event'] in EV: remap.append((m['event'], e[1], f"{s} (named: {m['event']})") + tuple(e[3:])); continue
                else: warns.append(f"{gid}: data-sfx={m.get('event')!r} on {s} is not an event in sfx.json")
            if s in done and e[0] in ('pop', 'slam', 'row-tick') and 'payoff' not in drop:
                remap.append(('payoff', e[1], f"{s} (completion: the bell, not the {e[0]})") + tuple(e[3:])); continue   # sound follows meaning
            if s in tt:
                if e[0] == 'riseIn': remap.append(('word',) + tuple(e[1:])); continue
                if e[0] == 'slam': remap.append(('word-slam',) + tuple(e[1:])); continue
                if e[0] == 'pop': warns.append(f'{gid}: pop({s}) on TYPE: type never pops (animations.md), fix the comp (rise + scissors, or slam + Impact)')
            remap.append(e)
        for k, mm in marks.items():
            if id(mm) in used_marks or mm.get('event') == 'none': continue
            used_marks.add(id(mm))                                  # one warning per element, not per selector key
            warns.append(f"{gid}: data-sfx={(mm.get('event') or mm.get('file'))!r} on {k} rode no registry event (the element is not animated by the registry): add a row in hf-graphics/sfx-hand.json, or animate it with the registry (sfx.md § Sound follows MEANING)")
        evs = remap
        for h in hand:
            if h.get('file'): warns.append(f"{gid}: hand row with file={h['file']!r} ignored: only the events documented in sfx.json may be used (document it first)")
        hand_evs = [(h['event'], float(h['at']), h.get('note', 'hand'), h.get('dur'), h.get('level_db')) for h in hand if h.get('at') is not None and not h.get('file')]
        for h in hand_evs: evs.append(h)
        warns += [f'{gid}: {x}' for x in w if not any(x.startswith(k + '(') for k, v in EV.items() if v is None)]
        if not evs and not w and not words:
            warns.append(f'{gid}: no registry calls found in {comp.name} (hand-rolled motion): its events need a hand entry')
        if kind == 'full':
            if not any(e[0] == 'flash' and abs(e[1]) <= 2 * F + 1e-4 for e in evs) and 'cut-in' not in drop:
                add(gid, 'cut-in', start, 'hard cut into the full-screen')   # a flicker on frame 0 IS the cut's sound
            if EV.get('riser') and (first_cut_in or not EV['riser'].get('first_cut_in_only', True)):   # the riser belongs to the FIRST full-screen, whoosh or not
                sp = EV['riser']; d = sp['slices'][0][1] - sp['slices'][0][0]
                t0 = start - cfg['riser_gap_s'] - d
                if t0 >= 0: add(gid, 'riser', t0, 'first cut-in of the job')
                else: warns.append(f'{gid}: no room for the riser before the first full-screen at {start:.2f}s (needs {cfg["riser_gap_s"] + d:.2f}s)')
                first_cut_in = False
        for e in evs:
            name, t, note = e[0], e[1], e[2]
            dur = e[3] if len(e) > 3 else None
            level = e[4] if len(e) > 4 else None
            if t < 0 or t > float(r['end']) - start + 0.05: continue
            add(gid, name, start + t, note, dur, level, auto=(len(e) <= 4), hand=(len(e) > 4))

    for g_ in HAND:
        if g_ not in seen_gids: warns.append(f'sfx-hand.json names {g_!r}, which is not a placed graphic (placement.json ids: check the spelling)')
    # layer stacking: a sound that would OVERLAP a different sound already on a track goes a layer
    # down, so both ring out (the reference put Deep Whoosh 3 under Deep Whoosh 4 on its own track);
    # the same sound repeating on top of itself stays on one track and truncates, which is exactly
    # the reference's machine-gun pops (0.29 / 0.25 / 0.21s, each cut by the next). An identical
    # sound within 2 frames is a doubling, not a layer, and is dropped.
    out.sort(key=lambda x: x['at'])
    # ── DENSITY (2026-09-10, on a 2 s stretch carrying seven sounds: "there's too many, it's too much going on") ──
    # 1. THE STAMP OWNS ITS BEAT: a slam / Impact carries the beat alone. The same graphic's other transients within
    #    ±stamp_owns_beat_s (the scissors of the words around it, the marker stroke under it, a pop) are dropped; the
    #    cut-in stays (the graphic's own entrance, two frames before), beds stay, hand entries stay.
    STAMPS = {'word-slam', 'slam', 'emphasis'}
    beat = float(cfg.get('stamp_owns_beat_s', 0.6))
    drops = []
    stamps = [x for x in out if x['event'] in STAMPS]
    kept = []
    for x in out:
        s_ = next((s for s in stamps if s is not x and s['gid'] == x['gid'] and abs(s['at'] - x['at']) <= beat), None)
        if s_ and x['event'] not in STAMPS and x['event'] not in ('cut-in', 'riser', 'slideIn', 'slideOut') and x['cls'] != 'bed' and not x['hand']:   # scene changes are structure, not accents: they keep their whoosh
            drops.append(f"{x['gid']} {x['event']} @{x['at']:.3f} ({x['note'][:30]}): inside the {s_['event']} @{s_['at']:.3f}'s beat (±{beat:.1f}s)"); continue
        kept.append(x)
    out = kept
    # 2. THREE SOUNDS A SECOND, NO MORE, across all graphics (rolling 1 s), where a RUN of one sound from one graphic
    #    (the scissors of a text animation's words, a wall's machine-gun pops) counts ONCE: the pile-up is different
    #    sounds from different graphics landing together. The lowest-priority source in an over-full second goes (a
    #    newcomer on a tie); beds (typing, loading) are textures and are not counted; a hand entry is never dropped.
    PRIO = {'payoff': 7, 'gunshot': 7, 'title-card': 7, 'word-slam': 6, 'emphasis': 6, 'word-negative': 6, 'cut-in': 5, 'riser': 5,
            'slam': 4, 'pop': 3, 'row-tick': 3, 'riseIn': 2, 'slideIn': 2, 'slideOut': 2, 'flash': 2, 'word-flicker': 2, 'click': 2,
            'word': 1, 'drawOn': 0}
    cap = int(cfg.get('max_per_second', 3))
    src = lambda p: (p['gid'], p['file'])
    kept = []
    for x in out:
        if x['cls'] == 'bed': kept.append(x); continue
        take = True
        while True:
            win_ = [p for p in kept if p['cls'] != 'bed' and x['at'] - p['at'] < 1.0]
            groups = {}
            for p in win_: groups.setdefault(src(p), []).append(p)
            if src(x) in groups or len(groups) < cap: break            # its own run, or room for another source
            # over-full: the lowest-priority SOURCE goes (x on a tie); a source with a hand entry in it stays
            lo = min(list(groups.items()) + [(src(x), [x])],
                     key=lambda g: (min(PRIO.get(p['event'], 2) for p in g[1]), any(p['hand'] for p in g[1]), g[0] == src(x)))
            if any(p['hand'] for p in lo[1]): break
            if lo[0] == src(x):
                drops.append(f"{x['gid']} {x['event']} @{x['at']:.3f} ({x['note'][:30]}): {cap} sources already in the second before it"); take = False; break
            for p in lo[1]:
                drops.append(f"{p['gid']} {p['event']} @{p['at']:.3f} ({p['note'][:30]}): {cap} sources in the second around {x['at']:.3f}, the lowest-priority one"); kept.remove(p)
        if take: kept.append(x)
    out = kept
    win = cfg['layer_window_frames'] * F + 1e-4
    placed = []
    final = []
    for x in out:
        near = [p for p in placed if abs(p['at'] - x['at']) <= win]
        if any(p['file'] == x['file'] for p in near): continue      # one sound per frame; a second copy is a doubling, not a layer
        x_end = x['at'] + (x['src_out'] - x['src_in'])
        used = {p['track'] for p in placed if p['file'] != x['file'] and p['at'] < x_end and x['at'] < p['at'] + (p['src_out'] - p['src_in'])}
        for tr in (TR['primary'], TR['layer2'], TR['layer3']):
            if tr not in used: x['track'] = tr; break
        else:
            warns.append(f"{x['gid']} {x['event']} @{x['at']}: four sounds on one frame, dropped"); continue
        placed.append(x); final.append(x)
    for i, x in enumerate(final): x['id'] = f's{i + 1:03d}'

    # cut sheet
    span = (final[-1]['at'] - final[0]['at']) if len(final) > 1 else 0
    lines = [f"# SFX plan — {job.name}", '',
             f"{len(final)} sounds over {span:.1f}s ({len(final) / span if span else 0:.2f}/s) · preset {preset_dir.relative_to(ROOT)} · fps {fps:.3f}", '',
             '| # | at | track | graphic | event | sound | slice | level | peak→ | note |', '|---|---|---|---|---|---|---|---|---|---|']
    for x in final:
        lines.append(f"| {x['id']} | {x['at']:.3f} | A{x['track'] + 1} | {x['gid']} | {x['event']} | {os.path.basename(x['file'])} | "
                     f"{x['src_in']:.2f}–{x['src_out']:.2f} | {x['level_db']:+d} dB | {x['peak'] + x['level_db']:.1f} | {x['note']} |")
    if drops:
        lines += ['', f'## dropped by the density rules ({len(drops)})', '', 'The stamp owns its beat (±%.1f s, same graphic) · %d sounds a second, no more (rolling 1 s, all graphics). sfx.md § Density.' % (beat, cap), ''] + [f'- {d}' for d in drops]
    if warns:
        hint = ('This parser never guesses a time it cannot bind (a call inside a loop it cannot size, an argument it '
                'cannot evaluate, a `reveal` with no literal text). Enter each line by hand in `hf-graphics/sfx-hand.json`, '
                'a list of `{"gid", "event", "at": <comp-relative seconds>}` rows (`"word": <text>` places it on that span '
                'instead of `at`; `dur`, `level_db`, `note`, `drop` optional), then re-run this script.')
        lines += ['', '## ⚠ needs a hand entry', '', hint, ''] + [f'- {w}' for w in warns]
    md = '\n'.join(lines) + '\n'
    if dry:
        print(md); return
    write_plan(hf, final, md, candidate='--candidate' in a)
    print(f"scored {len(final)} rows; {len(warns)} ⚠; {len(drops)} dropped by the density rules (listed in the cut sheet)")
    for w in warns: print('  ⚠ ' + w)
    if warns: print(f"  -> hand-enter these in {hf / 'sfx-hand.json'}: [{{\"gid\", \"event\", \"at\": <comp-relative seconds>}}], then re-run")
    return 0


if __name__ == '__main__':
    sys.exit(main())
