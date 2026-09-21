# Two machines, one brain: the desktop and the MacBook

Same Claude account, same system, same memory, on both computers. Edit on whichever you're at; the
MacBook can run the autonomous edits while the desktop stays free. Set up 2026-09-21.

**How it holds together**
- **The system + your memory live in a private git repo.** Both machines pull and push it with `./sync.sh`.
- **Memory is shared, not copied.** `memory/` lives in the repo, and each machine links its own
  `~/.claude/projects/<slug>/memory` path to it, so both see the same facts.
- **Jobs stay local, their notes travel.** `./sync.sh` copies each job's small text state into `handoff/`.
  Footage and renders never move.
- **The chat follows you.** Sessions connect to Remote Control, so a session running on one machine can be
  continued from claude.ai/code on the other. Nothing to re-explain, no second conversation to keep in sync.

---

## 1. One-time: create the hub

1. On github.com → **New repository** → name it `video-editor` → **Private** → do **not** add a README.
2. Copy the URL it shows (`https://github.com/<you>/video-editor.git`).
3. On the desktop, in the project folder:
   ```bash
   git remote add origin https://github.com/<you>/video-editor.git
   git push -u origin main
   ```
   Git opens a browser once to sign you in.

The repo carries ~200 MB: every skill, preset, workflow, doc, and your memory. It deliberately leaves out
footage, renders, `.mcp.json` (your keys) and the heavy static media.

## 2. One-time: the MacBook

```bash
git clone https://github.com/<you>/video-editor.git ~/video-editor
cd ~/video-editor
```
Then, in order:

1. **Homebrew**, if it isn't there (it needs your password, so Claude can't run it):
   `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
2. **Open the folder in Claude Code** and paste **Prompt A** below — it runs `./setup.sh` (ffmpeg, node, uv,
   the render engine) and verifies with `./check-setup.sh`.
3. **Link the memory** so the Mac reads the repo's copy:
   ```bash
   SLUG="-Users-$(whoami)-video-editor"
   mkdir -p ~/.claude/projects/$SLUG
   ln -s ~/video-editor/memory ~/.claude/projects/$SLUG/memory
   ```
   (The slug is the project path with `/`, `\`, `:` and spaces turned into `-`. On the desktop the same job is
   done by a junction at `C:\Users\affan\.claude\projects\E--Claude-Projects-video-editor-client-video-editor\memory`.)
4. **Copy the two things git doesn't carry**, by SSD or AirDrop, from the desktop folder:
   - `.mcp.json` (your MCP keys — never put this in the repo)
   - `assets/sfx/` (145 MB) and `presets/youtube/fern-inspired/reference/videos/` (429 MB), only if you edit
     the long-form channel there. Reels don't need either.
5. If Premiere isn't on the Mac: `./setup.sh --lane chat-only`.

## 3. Every day: `./sync.sh`

Run it **before** you start and **after** you finish, on whichever machine you used:

```bash
./sync.sh                 # pull what the other machine did, push what this one did
./sync.sh "seq 22 cut"    # same, with a note
```

It stages each job's text state into `handoff/`, pulls, commits and pushes. If both machines changed the same
file it stops and says so — rare, because you work on one at a time.

**The rhythm that keeps it clean**
- Start a work session with `./sync.sh`. Finish it with `./sync.sh`.
- Let one machine own a job from start to finish. The other picks it up only after a sync.
- The MacBook is the edit bot: raw take in, cut + captions out. The desktop is where you hand-finish in Premiere.
- The deliverable for the desktop (an `.srt`, an EDL) arrives in `handoff/<job>/` after a sync.

## 4. Same chat, two machines

Sessions already connect to Remote Control (Settings → Claude Code). That means:

- A session **running on the desktop** can be opened from the MacBook at **claude.ai/code**, and vice versa —
  the same conversation, same context. The work still executes on the machine that started it.
- So: **start the session on the machine that should do the work.** Heavy transcode or transcription while you
  edit? Start it on the MacBook and watch it from the desktop.
- You never need to re-explain anything to a fresh session: memory plus each job's `RUN.md` resume block do that.
  Prompt F below is the whole handover.

## 5. The prompts

**A — first run on a machine**
```
This is my video-editor system, cloned from my private repo. Same account, new machine.
Run ./setup.sh and verify with ./check-setup.sh. Don't change any presets or skills.
If Premiere isn't installed here, set the lane to chat-only.
```

**B — check the brain came across**
```
Read your memory for this project and tell me, in five lines: who I am, what the @affanwizu channel is,
what the reel recipe is, and what we agreed about captions. Then read
presets/instagram/affanwizu/README.md and confirm the preset files are all there.
```

**C — a new reel, full edit**
```
New @affanwizu reel. Raw take: ~/reels/incoming/<FILE>.MP4
Do the whole edit per presets/instagram/affanwizu/PLAYBOOK.md § 0 and reel-recipe.md:
Urdu transcript on CPU, cut to final takes only with tight edges, the frame stack, punch-ins on the
insult / one-word payoff / closing punchline, yellow captions, and propose a title.
Music: <path to the instrumental, or "ask me when the cut is locked">.
Show me the cut sheet and a preview when it's ready. Then run ./sync.sh so my desktop gets the files.
```

**D — captions only**
```
Captions only for this cut: <path>. @affanwizu yellow style, editable .srt, follow PLAYBOOK.md.
```

**E — after you ship a reel (always)**
```
I've shipped this reel: <path to the final export>. Do a learning pass: compare it against what you
delivered, update presets/instagram/affanwizu/LESSONS.md and reel-recipe.md, then ./sync.sh.
```

**F — picking up on the other machine**
```
./sync.sh first, then read handoff/<job>/RUN.md and tell me where we are.
```

## 6. What's different on Apple Silicon

- **No CUDA**: WhisperX runs CPU int8 (locked on Apple Silicon). About the same ~4 min per 2.5 min take as the
  Windows CPU runs — and it stops fighting Premiere for the GPU, which was the real time sink here.
- **No memory fights.** On 2026-09-20 the desktop had After Effects, Premiere, Photoshop and Media Encoder open,
  87 of 91 GB committed, and large-v3 could not load at all. That is the reason for the second machine.
- **Renders get faster**: ffmpeg uses Apple's `h264_videotoolbox`.
- Drop the `PYTHONUTF8=1` prefixes — macOS is already UTF-8, and there's no Git Bash in the way.
- **Scripted Premiere import** is broken on the Windows machine (since 2026-09-18), not in the code. If Premiere
  goes on the Mac, test it early — it may simply work there.

## 7. Prove it works

1. `./check-setup.sh` — every core item ✓
2. Prompt B answers correctly (memory + presets found)
3. `./sync.sh` on the Mac, then on the desktop: the same commit shows on both
4. A 30-second take runs end to end: transcript → cut → `.srt`
5. A preview frame shows gold captions, upright, under the chin
