#!/usr/bin/env bash
# setup-resolve.sh: one-command setup for the OPTIONAL DaVinci Resolve lane.
# Installs the pinned Resolve MCP server (official Resolve scripting API) and
# wires .mcp.json. Safe to re-run; it verifies each piece and skips what's done.
#
#   macOS:            fully supported.
#   Windows (native): supported — run from Git Bash (the shell Claude Code uses
#                     on Windows). The server talks to the Windows-side Resolve
#                     through fusionscript.dll.
#   Linux:            supported (native Resolve install at /opt/resolve).
#   WSL2:             NOT supported — Resolve's scripting library loads
#                     in-process, so a Linux-side server can't reach a
#                     Windows-side Resolve. Run this natively instead (above).
#
# Requirements: DaVinci Resolve (Studio OR the free edition), git, python (3.9+).
#
#   ./setup-resolve.sh            detects the edition and wires the matching path
#   ./setup-resolve.sh --studio   force the direct scripting path (Studio)
#   ./setup-resolve.sh --free     force the in-app bridge path (free edition)
#
# Studio: the MCP talks to Resolve's scripting API directly (External scripting =
# Local is Resolve's default; check that preference only if the connection fails).
# Free edition: Blackmagic gates external scripting to Studio, so this script also
# installs the MCP's in-app bridge into Resolve's Scripts menu and enables it; the
# user then runs Workspace > Scripts > resolve_bridge once per Resolve session.
#
# After it finishes: restart Claude Code once so it picks up .mcp.json, then
# verify by asking Claude to get the Resolve version.
set -euo pipefail

# The vendored installer prints Unicode box-drawing characters; Windows consoles
# default to cp1252 and the print crashes with UnicodeEncodeError AFTER the venv
# built fine, aborting the .mcp.json wiring below (hit 2026-08-13). Force UTF-8
# for every python this script runs; no-op on macOS/Linux. Fixing it here keeps
# the pinned vendor clone unpatched (a re-clone would silently drop a patch).
export PYTHONUTF8=1 PYTHONIOENCODING=utf-8

# Resolve the PROJECT root. In the shipped package this script sits at the root;
# in the source repo it lives under packaging/overlay/. The marker file decides.
HERE="$(cd "$(dirname "$0")" && pwd)"
if [[ -f "$HERE/check-setup.sh" ]]; then
  ROOT="$HERE"
elif [[ -f "$HERE/../../check-setup.sh" ]]; then
  ROOT="$(cd "$HERE/../.." && pwd)"
else
  printf 'ERROR: cannot locate the project root (check-setup.sh not found)\n' >&2
  exit 1
fi
cd "$ROOT"

REPO_URL="https://github.com/samuelgursky/davinci-resolve-mcp.git"
PIN="a9fd831ba301e8268bdf03277ef4de4b289e3bfc"   # v2.72.0, verified 2026-08-03 on Resolve Studio 21.0.3.7
VENDOR="$ROOT/vendor/davinci-resolve-mcp"

say()  { printf '%s\n' "$*"; }
fail() { printf 'ERROR: %s\n' "$*" >&2; exit 1; }

# ---- arguments -------------------------------------------------------------
EDITION_PICK=""
while [[ $# -gt 0 ]]; do
  case "$1" in
    --studio)  EDITION_PICK=studio ;;
    --free)    EDITION_PICK=free ;;
    -h|--help) sed -n '2,28p' "$0"; exit 0 ;;
    *) fail "unknown option: $1 (usage: ./setup-resolve.sh [--studio|--free])" ;;
  esac
  shift
done

# ---- OS detection ----------------------------------------------------------
OS="$(uname -s)"
IS_WINDOWS=0
if [[ "$OS" == "Linux" ]] && grep -qi microsoft /proc/version 2>/dev/null; then
  fail "WSL2 can't drive a Windows-side Resolve (the scripting library is in-process). Run this natively on Windows instead: Git for Windows + Claude Code on Windows, then re-run from Git Bash (see SETUP.md \"Windows\")."
fi

case "$OS" in
  Darwin)
    # Direct download installs into its own folder; the App Store builds sit flat in
    # /Applications (free = "DaVinci Resolve.app", Studio = "DaVinci Resolve Studio.app").
    APP_PATH="/Applications/DaVinci Resolve/DaVinci Resolve.app"
    for cand in "/Applications/DaVinci Resolve Studio.app" "/Applications/DaVinci Resolve.app"; do
      if [[ ! -e "$APP_PATH" && -d "$cand" ]]; then APP_PATH="$cand"; fi
    done
    SCRIPT_API="/Library/Application Support/Blackmagic Design/DaVinci Resolve/Developer/Scripting"
    SCRIPT_LIB="$APP_PATH/Contents/Libraries/Fusion/fusionscript.so"
    ;;
  Linux)
    APP_PATH="/opt/resolve"
    SCRIPT_API="/opt/resolve/Developer/Scripting"
    SCRIPT_LIB="/opt/resolve/libs/Fusion/fusionscript.so"
    ;;
  MINGW*|MSYS*)
    IS_WINDOWS=1
    # Git Bash spellings here; converted to C:/ form for .mcp.json below (Claude Code
    # spawns the server as a native Windows process, which can't read /c/... paths).
    SYSDRV="$(cygpath -u "${SYSTEMDRIVE:-C:}")"
    APP_PATH="$SYSDRV/Program Files/Blackmagic Design/DaVinci Resolve/Resolve.exe"
    SCRIPT_API="$SYSDRV/ProgramData/Blackmagic Design/DaVinci Resolve/Support/Developer/Scripting"
    SCRIPT_LIB="$SYSDRV/Program Files/Blackmagic Design/DaVinci Resolve/fusionscript.dll"
    ;;
  *)
    fail "unsupported OS: $OS (on Windows, run this from Git Bash — see SETUP.md)"
    ;;
esac
APP_FOUND=1
[[ -e "$APP_PATH" ]] || { APP_FOUND=0; say "WARNING: DaVinci Resolve not found at $APP_PATH. Install it, then re-run this script (continuing so the server is at least staged)."; }

# ---- edition: Studio (direct scripting) or free (in-app bridge) -----------
# Blackmagic gates EXTERNAL scripting to Studio: on the free edition scriptapp("Resolve")
# never answers a foreign process, and on Windows the call HANGS instead of failing, so a
# free-edition lane wired the Studio way sat on its first MCP call for Claude Code's
# 30-minute idle timeout (a client, 2026-09-07). The free edition is fully drivable through
# the MCP's in-app bridge (a script run from Workspace > Scripts, which is not gated), so
# the installer decides the path here instead of handing the user a caveat.
# Signals: the Studio activation files (.license/.davinciresolvestudio_*, every OS), the
# App Store "DaVinci Resolve Studio.app" bundle, and on Windows the uninstall registry
# DisplayName ("DaVinci Resolve" vs "DaVinci Resolve Studio"). Nothing saying Studio means
# the bridge: a Studio user misdetected as free still works (the bridge runs on any edition)
# and can force --studio; a free user misdetected as Studio gets the hang.
detect_edition() {
  local lic_dir names
  case "$OS" in
    Darwin)
      [[ -d "/Applications/DaVinci Resolve Studio.app" ]] && { echo studio; return; }
      lic_dir="/Library/Application Support/Blackmagic Design/DaVinci Resolve/.license" ;;
    Linux)
      lic_dir="/opt/resolve/.license" ;;
    *)
      lic_dir="$SYSDRV/ProgramData/Blackmagic Design/DaVinci Resolve/.license"
      names="$(powershell.exe -NoProfile -NonInteractive -Command "Get-ItemProperty 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\*','HKLM:\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\*','HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\*' -ErrorAction SilentlyContinue | Where-Object { \$_.DisplayName -like 'DaVinci Resolve*' } | ForEach-Object { \$_.DisplayName }" 2>/dev/null | tr -d '\r' | sed 's/[[:space:]]*$//' || true)"
      if printf '%s\n' "$names" | grep -qx 'DaVinci Resolve Studio'; then echo studio; return; fi
      if printf '%s\n' "$names" | grep -qx 'DaVinci Resolve'; then echo free; return; fi ;;
  esac
  if compgen -G "$lic_dir/.davinciresolvestudio*" >/dev/null 2>&1; then echo studio; else echo free; fi
}
if [[ -n "$EDITION_PICK" ]]; then
  EDITION="$EDITION_PICK"; say "[edition] $EDITION (forced by --$EDITION)"
else
  EDITION="$(detect_edition)"; say "[edition] $EDITION detected (wrong? re-run with --studio or --free)"
fi

# ---- prerequisites ---------------------------------------------------------
command -v git >/dev/null 2>&1 || fail "git is required. Install it and re-run."
# python3 on macOS/Linux; `python` on Windows (python3 there is a fake Store stub) —
# probe by RUNNING it, not command -v.
PY=python3; "$PY" -c '' 2>/dev/null || PY=python
"$PY" -c '' 2>/dev/null || fail "python is required. Install it (see SETUP.md) and re-run."

# ---- server: clone at the pin + build the venv -----------------------------
if [[ ! -d "$VENDOR/.git" ]]; then
  say "[server] cloning davinci-resolve-mcp..."
  git clone "$REPO_URL" "$VENDOR"
fi
HEAD="$(git -C "$VENDOR" rev-parse HEAD)"
if [[ "$HEAD" != "$PIN" ]]; then
  say "[server] checking out pinned build ${PIN:0:7}..."
  git -C "$VENDOR" fetch --quiet origin
  git -C "$VENDOR" -c advice.detachedHead=false checkout --quiet "$PIN"
fi
# venv layout differs by OS: bin/python (macOS/Linux) vs Scripts/python.exe (Windows)
venv_py() {
  if [[ -e "$VENDOR/venv/Scripts/python.exe" ]]; then echo "$VENDOR/venv/Scripts/python.exe"
  else echo "$VENDOR/venv/bin/python"; fi
}
if [[ ! -x "$(venv_py)" ]]; then
  say "[server] building the Python environment (one time, a minute or two)..."
  # The vendored installer prints ~60 lines of Cursor/JetBrains/OpenCode config blocks and its
  # own "Next steps", which contradict the real next step printed below. Keep its output in a
  # log and show it only if the build fails.
  if ! (cd "$VENDOR" && "$PY" install.py --clients manual >install.log 2>&1); then
    cat "$VENDOR/install.log"
    fail "the Python environment build failed (full output above, also in vendor/davinci-resolve-mcp/install.log)"
  fi
  say "[server] environment built (installer output in vendor/davinci-resolve-mcp/install.log)"
fi
VENV_PY="$(venv_py)"
[[ -x "$VENV_PY" ]] || fail "venv build did not produce a venv python (re-run '$PY install.py --clients manual' inside vendor/davinci-resolve-mcp and read its output)"
say "[server] ready at vendor/davinci-resolve-mcp (pinned ${PIN:0:7})"

# ---- free edition: the in-app bridge --------------------------------------
# The opt-in is BAKED INTO THE VENV, not left to .mcp.json's env: a client's Claude Code
# kept respawning the server from a config snapshot taken at session start, so a flag added
# to .mcp.json afterwards never reached the process, while one baked into the interpreter
# did (2026-09-07). A .pth import line runs at every interpreter start, whatever command
# line the host uses (a sitecustomize.py would be shadowed by Debian's own). .mcp.json
# carries the same flag so the intent is readable. The server reads it at call time.
SITE="$("$VENV_PY" -c 'import sysconfig; print(sysconfig.get_paths()["purelib"])')"
PTH="$SITE/zz_davinci_resolve_bridge.pth"
BRIDGE_OK=0
if [[ "$EDITION" == free ]]; then
  printf 'import os; os.environ.setdefault("DAVINCI_RESOLVE_BRIDGE", "1")\n' > "$PTH"
  say "[bridge] DAVINCI_RESOLVE_BRIDGE=1 baked into the venv ($PTH)"
  # The bridge refuses paths outside its allow-lists, and the vendored installer's default
  # output root is ~/Movies: a macOS path that does not exist on Windows, and not where
  # step 8 renders (projects/<job>/outputs/). Seed the project root into both lists BEFORE
  # the installer copies the config next to the bridge; existing roots are kept.
  BRIDGE_ROOT="$ROOT"; [[ "$IS_WINDOWS" -eq 1 ]] && BRIDGE_ROOT="$(cygpath -w "$ROOT")"
  "$VENV_PY" - "$BRIDGE_ROOT" <<'PY'
import json, sys
from pathlib import Path
root = sys.argv[1]
cfg_path = Path.home() / ".config/davinci-resolve-mcp/bridge.json"
cfg = {}
if cfg_path.exists():
    try:
        cfg = json.loads(cfg_path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        cfg = {}
defaults = {"allowed_media_roots": [str(Path.home())],
            "allowed_output_roots": [str(Path.home() / "Movies")]}
for key, default in defaults.items():
    roots = [r for r in (cfg.get(key) or default) if isinstance(r, str)]
    if root not in roots:
        roots.append(root)
    cfg[key] = roots
cfg_path.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
cfg_path.write_text(json.dumps(cfg, indent=2, sort_keys=True), encoding="utf-8")
print("[bridge] allowed media/output roots include " + root)
PY
  say "[bridge] installing the in-app bridge into Resolve's Scripts menu (log: vendor/davinci-resolve-mcp/bridge-install.log)..."
  if (cd "$VENDOR" && "$VENV_PY" scripts/install_resolve_bridge.py >bridge-install.log 2>&1); then
    BRIDGE_OK=1
    grep '^WARNING' "$VENDOR/bridge-install.log" || true   # framework-Python / stale-container advice
    say "[bridge] installed"
  else
    cat "$VENDOR/bridge-install.log"
    say "[bridge] ⚠ the bridge installer failed (output above). The usual cause: Resolve has never been"
    say "         launched on this machine, so its Scripts folder does not exist yet. Launch Resolve once,"
    say "         quit it, then re-run ./setup-resolve.sh (the server and .mcp.json below are done)."
  fi
else
  rm -f "$PTH"
fi

# ---- .mcp.json: merge the davinci-resolve entry in place -------------------
# On Windows every path must be written in C:/ form — Claude Code launches the
# server natively (not through Git Bash), so /c/... spellings would not resolve.
if [[ "$IS_WINDOWS" -eq 1 ]]; then
  J_PY="$(cygpath -m "$VENV_PY")"
  J_SERVER="$(cygpath -m "$VENDOR/src/server.py")"
  J_API="$(cygpath -m "$SCRIPT_API")"
  J_LIB="$(cygpath -m "$SCRIPT_LIB")"
else
  J_PY="$VENV_PY"; J_SERVER="$VENDOR/src/server.py"; J_API="$SCRIPT_API"; J_LIB="$SCRIPT_LIB"
fi
MCP_JSON="$ROOT/.mcp.json"
"$PY" - "$MCP_JSON" "$J_PY" "$J_SERVER" "$J_API" "$J_LIB" "$EDITION" <<'PY'
import json, os, sys
path, py, server, api, lib, edition = sys.argv[1:7]
cfg = {"mcpServers": {}}
if os.path.exists(path):
    with open(path) as fh:
        cfg = json.load(fh)
env = {
    "RESOLVE_SCRIPT_API": api,
    "RESOLVE_SCRIPT_LIB": lib,
    "PYTHONPATH": api + "/Modules",
}
if edition == "free":
    # Readable intent only; the venv .pth is what actually carries the flag (see above).
    env["DAVINCI_RESOLVE_BRIDGE"] = "1"
cfg.setdefault("mcpServers", {})["davinci-resolve"] = {
    "command": py,
    "args": [server],
    "env": env,
    # Per-call wall-clock cap in ms (Claude Code >= 2.1.203; older builds ignore it). The
    # default is ~28 h with a 30-minute idle abort, and a hung first call ate all of that
    # once (free edition wired the Studio way, 2026-09-07). Ten minutes covers the longest
    # legitimate call (Resolve's own AI analysis on a long clip; renders are non-blocking)
    # and ends a hang inside the same session.
    "timeout": 600000,
}
with open(path, "w") as fh:
    json.dump(cfg, fh, indent=2)
    fh.write("\n")
print("[config] davinci-resolve entry written to .mcp.json (other servers untouched)")
PY

# Record the lane for setup.sh / the SessionStart hook (only once the tools marker exists;
# this script can also run standalone before ./setup.sh, and then setup.sh records it).
[[ -f "$ROOT/.setup-complete" ]] && printf 'lane=resolve\n' > "$ROOT/.setup-complete"

# ---- done ------------------------------------------------------------------
say ""
if [[ "$APP_FOUND" -eq 0 ]]; then
  say "NOTE: DaVinci Resolve was NOT found at $APP_PATH. The server is staged and .mcp.json"
  say "is written, but the lane cannot connect until Resolve is installed there."
fi
say "Setup complete ($EDITION edition). One step left:"
say "  Restart Claude Code (quit it fully, reopen this project) so it loads the new"
say "  davinci-resolve MCP; answer YES when it asks to enable this project's .mcp.json"
say "  servers (a no is remembered: 'claude mcp reset-project-choices' clears it), then"
say "  say \"continue setup\"."
if [[ "$EDITION" == free ]]; then
  say "Free edition, ONE RECURRING STEP (every time Resolve starts): open a project, then"
  say "  Workspace > Scripts > resolve_bridge, and leave it running. That script hands the"
  say "  MCP the live Resolve; without it every call answers BRIDGE_UNAVAILABLE at once."
  [[ "$BRIDGE_OK" -eq 1 ]] && say "  (Restart Resolve once first so it re-scans its Scripts menu.)"
  say "Verify after the restart: start the bridge as above, then ask Claude to \"get the"
  say "Resolve version\"."
  say "Troubleshooting: resolve_bridge missing from the Scripts menu → re-run ./setup-resolve.sh"
  say "with Resolve closed (macOS needs a python.org framework Python for Resolve to list .py"
  say "scripts; the installer says so above if that applies). Wrong edition detected →"
  say "./setup-resolve.sh --studio."
else
  say "Verify after the restart: ask Claude to \"get the Resolve version\"; Resolve must"
  say "be running (Claude can launch it)."
  say "Troubleshooting (only if that fails): check Resolve Preferences > System > General >"
  say "External scripting = Local. That IS the shipped default, so don't change it up front."
  say "If this is actually the FREE edition (external scripting is Studio-only, and on"
  say "Windows the free edition hangs instead of refusing): ./setup-resolve.sh --free."
fi
