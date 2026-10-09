#!/usr/bin/env python3
"""numbers-table.py — one row per long-form from each reference folder's style-report (report.json).

Export-probe numbers, measured the same way on every video. Where the probe is known to lie (face share with
illustrations/PiP, slow-downs, zooms inside nests — facecam LESSONS 2026-10-08) the catalogue/timeline figure is
given in the notes column and wins."""
import json, os

ROOT = os.path.dirname(os.path.abspath(__file__))
REF = os.path.join(ROOT, '..', '..', 'presets', 'youtube', 'affan-afterhours-facecam', 'reference')
ROWS = [  # (folder, base dir, date, views, note)
    ('ps5-pro', 'longform', '08-28', '9.7k', 'catalogue face 54 %'),
    ('leaker', 'longform', '08-29', '8.1k', 'catalogue face 63 %'),
    ('fuel-system', REF, '08-31', '172.9k', 'friend-edited'),
    ('crime-system', 'longform', '09-03', '10.7k', 'catalogue face 62 %'),
    ('riskiest', REF, '09-05', '34.8k', 'catalogue face 77 %'),
    ('npc-ai', 'longform', '09-08', '350', 'catalogue face 63 %'),
    ('dirtiest', 'longform', '09-10', '13.6k', 'catalogue face ~61 %; 3 slow-downs by eye'),
    ('cant-do-anymore', 'longform', '09-12', '17.7k', 'catalogue face ~57 %'),
    ('pc-release', 'longform', '09-23', '1.1k', 'timeline: 53 zooms med 130 %, 11 slow-downs'),
    ('collectors-box', 'longform', '09-25', '559', 'timeline: 48 zooms med 136 %; face 64 % + PiP 32 %'),
    ('game-informer', 'longform', '09-30', '287', 'timeline: 23 zooms med 121 %, 0 slow-downs'),
]
print('| up | video | views | changes/min | hard cuts/min | cold open cuts/min* | zoom steps/min · median | push %/s | face (probe) | overlay runs/min · median s | wpm | notes (wins over the probe) |')
print('|---|---|---|---|---|---|---|---|---|---|---|---|')
for name, base, date, views, note in ROWS:
    d = base if os.path.isabs(base) else os.path.join(ROOT, base)
    p = os.path.join(d, name, 'report.json')
    if not os.path.exists(p):
        print(f'| {date} | {name} | {views} | (not measured yet) |||||||| {note} |'); continue
    j = json.load(open(p, encoding='utf-8'))
    pr = json.load(open(os.path.join(d, name, 'probe', 'probe.json'), encoding='utf-8'))
    cold = sum(1 for c in pr['cuts'] if (c['t'] if isinstance(c, dict) else c) < 60)
    push = j.get('zoom_push_pct_per_s', j.get('push_pct_per_s'))
    print(f"| {date} | {name} | {views} | {j['visible_changes_per_min']} | {j['hard_cuts_per_min']} | {cold} | "
          f"{j['zoom_steps_per_min']} · x{j['zoom_step_median']} | {push} | {round(100 * j['face_share'])} % | "
          f"{j['overlay_runs_per_min']} · {j['overlay_run_median']} | {j['wpm']} | {note} |")
print('\n*cold open = hard cuts detected in the first 60 s.')
