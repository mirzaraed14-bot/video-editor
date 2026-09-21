#!/usr/bin/env bash
# SessionStart hook: on a fresh install, inject a reminder telling Claude to run the
# onboarding/setup flow (CLAUDE.md "FIRST RUN" gate) before doing anything else. Emits NOTHING once
# setup is done. Always exits 0 so it can never break a session.
#
# Pure bash + printf on purpose (NO jq / python dependency), because on a brand-new machine those may
# not be installed yet, and this is the very hook that's supposed to get them installed. Runs on macOS,
# Linux, and Windows (Claude Code on Windows runs hooks through Git Bash, which ships with Git for
# Windows). If Git Bash itself is missing the hook can't fire — that front door lives in CLAUDE.md.
#
# cwd is the project root. "Setup done" = the .setup-complete marker exists (written by ./setup.sh
# once every core tool verifies) AND its lane= line is not "pending" (the which-app question, asked
# only when several editing apps are installed, has been answered with ./setup.sh --lane <pick>).
# Personalization (brand-kit.md) is OPTIONAL and never gates this; the editor works out of the box
# with the neutral bundled look.

if [ -f check-setup.sh ]; then
  # NOTE: newlines below are the literal two-character sequence \n (valid JSON string escapes); printf %s
  # passes them through verbatim, and there are no " or \ or apostrophe chars in the messages to break the JSON.
  msg=''
  if [ ! -f .setup-complete ]; then
    msg='⚠️ FRESH INSTALL: setup has not finished yet (no .setup-complete marker).\n\nFollow the FIRST RUN onboarding gate in CLAUDE.md before editing anything:\n  1. Run ./setup.sh yourself (no need to ask). It detects the OS, installs every missing tool, bootstraps the render engine, verifies with ./check-setup.sh, then auto-detects an installed editing app (Premiere / Resolve / CapCut) and wires its lane. It is idempotent; re-run it any time.\n  2. Handle its exit codes per the FIRST RUN gate in CLAUDE.md, step 1 — that block is the spec and it stays current; this reminder is only the nudge to go read it.\n  3. Brand kit is OPTIONAL: offer it once after tools pass; never block editing on it.\n\nIf the user asks to edit a video right now, run setup first (an edit cannot run without ffmpeg).'
  elif grep -qs '^lane=pending' .setup-complete; then
    msg='⚠️ SETUP ALMOST DONE: the tools are installed, but the editing-app pick is still open (.setup-complete says lane=pending). Several editing apps are installed on this machine. Ask the user in ONE line which one they edit in (run ./setup.sh to list the detected apps if unsure), then run ./setup.sh --lane <their pick> (premiere | resolve | capcut | chat-only). premiere/resolve end with a Claude Code restart (answer YES when it asks to enable the .mcp.json servers). See CLAUDE.md FIRST RUN step 2.'
  fi
  if [ -n "$msg" ]; then
    printf '{"hookSpecificOutput":{"hookEventName":"SessionStart","additionalContext":"%s"}}\n' "$msg"
  fi
fi

exit 0
