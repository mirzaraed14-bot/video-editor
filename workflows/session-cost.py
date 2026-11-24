#!/usr/bin/env python3
"""What a Claude Code session (main + its subagents + advisor calls) cost, in $ and in % of the weekly cap.

Used by every lane that logs a job's cost ("Every finished job logs its actual cost in % in its lane's JOBS/STATUS file",
WEEK-PLAN.md). Method = memory `reference-usage-costs`: tokens from the session transcripts x API list prices, 1 % of the week
= $22 (calibrated on the meter 2026-10-22; re-check against the meter now and then with --usd-per-pct).

    python workflows/session-cost.py --job <job-name>          # every session whose FIRST user message names the job
    python workflows/session-cost.py --session <id> [--session <id> ...]
    options: --since 2026-11-23T00:00 --until ... (UTC, ISO prefix)  --usd-per-pct 22  --quiet

Reads ~/.claude/projects/*/<id>.jsonl and <id>/subagents/*.jsonl. Advisor calls (usage.iterations[] with
type "advisor_message") are priced at their own model, uncached. Read-only; prints one JOBS.md-ready line at the end.
"""
import argparse, glob, json, os, sys

# $ per MTok: input, output, cache read. Cache write = 1.25x input (5 min TTL) or 2x input (1 h TTL).
# Input/output: claude-api skill model table (cached 2026-11-03). Cache reads from that skill for Fable 5.2, Opus 5.5 and
# Sonnet 5.5; the others are ASSUMED at 0.1x input. Longest matching prefix wins.
PRICES = {
    'claude-fable-5-2': (8, 40, 0.20), 'claude-mythos-5-2': (8, 40, 0.20),
    'claude-fable-5-1': (10, 50, 1.0), 'claude-mythos-5-1': (10, 50, 1.0), 'claude-fable-5': (10, 50, 1.0),
    'claude-opus-5-5': (4, 20, 0.20), 'claude-opus-5': (5, 25, 0.50), 'claude-opus-4': (5, 25, 0.50),
    'claude-sonnet-5-5': (2, 10, 0.10), 'claude-sonnet-5': (2, 10, 0.20), 'claude-sonnet-4': (3, 15, 0.30),
    'claude-haiku-5-5': (0.10, 0.50, 0.01), 'claude-haiku-4': (1, 5, 0.10),
}


def price(model):
    best = None
    for k in PRICES:
        if (model or '').startswith(k) and (best is None or len(k) > len(best)):
            best = k
    return PRICES.get(best)


def part_cost(u, model):
    p = price(model)
    if not p:
        return 0.0, 'unpriced:' + str(model)
    pin, pout, pread = p
    cc = u.get('cache_creation') or {}
    w5, w1 = cc.get('ephemeral_5m_input_tokens'), cc.get('ephemeral_1h_input_tokens')
    wtot = u.get('cache_creation_input_tokens', 0) or 0
    if w5 is None and w1 is None:
        w5, w1 = 0, wtot                      # unknown TTL: assume 1 h (Claude Code default)
    elif (w5 or 0) + (w1 or 0) < wtot:
        w1 = (w1 or 0) + wtot - (w5 or 0) - (w1 or 0)
    c = (u.get('input_tokens', 0) * pin + u.get('output_tokens', 0) * pout + (u.get('cache_read_input_tokens', 0) or 0) * pread
         + (w5 or 0) * pin * 1.25 + (w1 or 0) * pin * 2.0) / 1e6
    return c, model


def file_cost(path, lo, hi):
    by_model, seen, turns, first_user = {}, set(), 0, None
    with open(path, encoding='utf-8', errors='ignore') as fh:
        for line in fh:
            try:
                d = json.loads(line)
            except ValueError:
                continue
            if first_user is None and d.get('type') == 'user':
                c = (d.get('message') or {}).get('content')
                if isinstance(c, list):
                    c = ' '.join(b.get('text', '') for b in c if isinstance(b, dict))
                first_user = c if isinstance(c, str) else ''
            if d.get('type') != 'assistant':
                continue
            ts = d.get('timestamp', '')
            if (lo and ts < lo) or (hi and ts > hi):
                continue
            m = d.get('message') or {}
            mid = m.get('id')
            if mid in seen:
                continue
            seen.add(mid)
            u = m.get('usage') or {}
            its = u.get('iterations') or []
            parts = [(it, it.get('model') if it.get('type') == 'advisor_message' else m.get('model')) for it in its] or [(u, m.get('model'))]
            for pu, pm in parts:
                c, key = part_cost(pu, pm)
                if pu is not u and pu.get('type') == 'advisor_message':
                    key = 'advisor:' + str(pm)
                by_model[key] = by_model.get(key, 0.0) + c
            turns += 1
    return by_model, turns, first_user or ''


def sessions_for(sid):
    out = []
    for main in glob.glob(os.path.expanduser('~/.claude/projects/*/%s.jsonl' % sid)):
        out.append(main)
        out += sorted(glob.glob(os.path.join(main[:-6], 'subagents', '*.jsonl')))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--session', action='append', default=[])
    ap.add_argument('--job')
    ap.add_argument('--since')
    ap.add_argument('--until')
    ap.add_argument('--usd-per-pct', type=float, default=22.0)
    ap.add_argument('--quiet', action='store_true')
    a = ap.parse_args()
    sids = list(a.session)
    if a.job:
        for f in glob.glob(os.path.expanduser('~/.claude/projects/*/*.jsonl')):
            seen_users = 0
            with open(f, encoding='utf-8', errors='ignore') as fh:
                for line in fh:          # the job must be named in one of the first 3 user messages (a hook may come first)
                    try:
                        d = json.loads(line)
                    except ValueError:
                        continue
                    if d.get('type') != 'user':
                        continue
                    c = (d.get('message') or {}).get('content')
                    if isinstance(c, list):
                        c = ' '.join(b.get('text', '') for b in c if isinstance(b, dict))
                    if isinstance(c, str) and a.job in c:
                        sids.append(os.path.basename(f)[:-6])
                        break
                    seen_users += 1
                    if seen_users >= 3:
                        break
    if not sids:
        sys.exit('no session found (use --session <id> or --job <name named in the first prompt>)')
    total, tot_model = 0.0, {}
    for sid in dict.fromkeys(sids):
        for f in sessions_for(sid):
            bm, turns, fu = file_cost(f, a.since, a.until)
            c = sum(bm.values())
            if not turns:
                continue
            total += c
            for k, v in bm.items():
                tot_model[k] = tot_model.get(k, 0.0) + v
            if not a.quiet:
                kind = 'sub ' if '/subagents/' in f.replace('\\', '/') else 'main'
                print('%8.2f  %s %-28s %4d turns  %s' % (c, kind, os.path.basename(f)[:28], turns, fu[:70].replace('\n', ' ')))
    if not a.quiet:
        for k, v in sorted(tot_model.items(), key=lambda kv: -kv[1]):
            print('          %-28s %8.2f' % (k, v))
    pct = total / a.usd_per_pct
    print('cost: $%.2f = %.2f %% of the week (session-cost.py, $%g per %%, sessions %s)'
          % (total, pct, a.usd_per_pct, ','.join(s[:8] for s in dict.fromkeys(sids))))


if __name__ == '__main__':
    main()
