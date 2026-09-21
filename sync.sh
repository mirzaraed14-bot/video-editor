#!/usr/bin/env bash
# sync.sh — the one command to run on EITHER machine (desktop ⇄ MacBook), before and after working.
#
#   ./sync.sh              pull, then push whatever changed here
#   ./sync.sh "message"    same, with your own note on the commit
#
# What travels: the system (skills, presets, workflows, lanes, docs), your MEMORY (memory/, which each
# machine links into ~/.claude/projects/<slug>/memory), and each job's small TEXT state, copied into
# handoff/ by this script — run notes, the EDL, the transcript, the caption lines and the .srt.
# What never travels: footage, renders, caches, .mcp.json (keys go machine to machine by hand once)
# and the heavy static media (assets/sfx/, the preset reference videos) — SSD copy, once per machine.
set -uo pipefail
cd "$(dirname "$0")"

note="${1:-}"
host="$(hostname | tr -d '\r')"
stamp="$(date '+%Y-%m-%d %H:%M')"

# ── 1. job text state → handoff/ (so the other machine can pick a job up cold) ────────────────
copied=0
for job in projects/*/; do
  name="$(basename "$job")"
  case "$name" in _*) continue ;; esac          # _sample, _corpus and friends stay local
  for rel in RUN.md BRIEF.md captions.txt transcript/cuts.json transcript/words.json \
             captions/captions.txt captions/transcript/words.json; do
    [ -f "$job$rel" ] || continue
    mkdir -p "handoff/$name/$(dirname "$rel")"
    cp -p "$job$rel" "handoff/$name/$rel" && copied=$((copied+1))
  done
  for srt in "$job"*.srt "$job"captions/*.srt; do
    [ -f "$srt" ] || continue
    mkdir -p "handoff/$name"
    cp -p "$srt" "handoff/$name/" && copied=$((copied+1))
  done
done
echo "[sync] handoff: $copied job files staged for the other machine"

# ── 2. get what the other machine did ────────────────────────────────────────────────────────
if ! git remote get-url origin >/dev/null 2>&1; then
  echo "[sync] no 'origin' remote yet — set one up first (see MOVE-TO-MAC.md § Two machines), then re-run"
  exit 1
fi
echo "[sync] pulling…"
if ! git pull --rebase --autostash; then
  echo "[sync] ⚠ the pull needs a hand: two machines changed the same file. Fix the conflict, then re-run."
  exit 1
fi

# ── 3. send what this machine did ────────────────────────────────────────────────────────────
git add -A
if git diff --cached --quiet; then
  echo "[sync] nothing new here — both machines are level"
  exit 0
fi
git commit -q -m "sync: $host $stamp${note:+ — $note}"
git push -q && echo "[sync] pushed. The other machine gets it with ./sync.sh"
