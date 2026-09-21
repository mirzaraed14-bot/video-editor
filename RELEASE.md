# Release notes — Claude Video Editor client package

The top section is the current build. `packaging/package-for-client.sh` stamps its version into
the zip as `VERSION` and copies this file in; `packaging/delivery/ship.sh` publishes it to the
download page. Add a new `## <version>` section at the top for every ship; version = the ship
date, `.2`, `.3` suffix for a second ship the same day. Bullets are client-facing and PLAIN: one short line each, what changed for them in everyday
words, no jargon, no internal job names; a creator reads the whole section in ten seconds
(2026-09-07).


## 2026.09.13

A round of fixes from a real edit review. Nothing to re-run; the next edit just picks them up.

- A prompt, command or quote you show on screen now stays full-screen for its whole explanation, complete and word for word, with the part you're saying highlighted as you say it.
- When a beat is about something on your screen (a folder, an app, a page), the plan calls for a real screen recording of it instead of a generic card.
- Dark full-screen scenes are spread across the whole video, so no long stretch goes without one.
- The closing of your video is kept whole: pauses and retakes still go, the sign-off never gets chopped.
- A new dead-air check runs on the final cut, so long pauses hidden under room noise no longer slip through.
- Background music starts where the song actually comes in and sits quieter by default.
- Highlights on long, split graphics no longer blink at the join.
- Sound effects: re-running the plan after a graphic moves tells you which rows changed, and placement refuses to save if any cue is missing, extra or drifted.
- Guardrails that used to live only in the author's private notes are now in the docs you get, so your edits follow the same rules.

## 2026.09.10

A round of polish on how long-form graphics look and sound. Nothing to re-run; the next edit just picks them up.

- Graphics beside your face are measured off your head now instead of placed by eye, so they never crowd you or drift off the edge
- A full-screen graphic is a short scene with a few moments and a camera move, not one static card you stare at
- Full-screen moments are spread through the video, so you never go a long stretch without one
- Text never pops onto screen. It rises in, or slams in with the bold look
- Every video opens on a slow zoom-out, and the zoom-in used for emphasis has smoother timing
- Sound effects follow what a graphic actually means, so a finished or successful moment rings instead of popping
- Fewer sounds stack on the same beat, so a busy graphic no longer sounds cluttered
- Slides and big moves get motion blur, so fast movement looks smooth instead of jumpy

## 2026.09.08

Fixes from a full end-to-end edit. Nothing to re-run; the next edit just picks them up.

- A graphic could end one frame before its cut and flash the last frame of the shot underneath. The placement tool now snaps every graphic to the frame and the checks catch a miss
- The graphics checker catches two more mistakes on its own: a fade that flashes black for a few frames, and a pop that lands on top of the element next to it
- Re-checking one graphic no longer wipes the full check report
- The review step has its own frame grabber, so the review evidence lands in the right folder every time and reviewers get the same brief on every job
- The prompt reviewer and the build notes now spell out that icons inside cards glow like every other accent prop
- Small things: the chin-line tool can save its measurement to a file, and the sound-effects planner tells you the exact file to fill in when it can't read a graphic on its own

## 2026.09.07

First Windows user found some bugs. All fixed. Already set up on Windows? Run `./setup.sh` again. On the free version of Resolve, also run `./setup-resolve.sh` once. If you have an NVIDIA graphics card and transcribing felt slow, delete the folder `~/.cache/video-editor/whisperx-venv` and it rebuilds right on the next edit.

- Windows + NVIDIA card: transcription actually uses your graphics card now. Before, it quietly ran on the CPU and took about 5x longer
- Setup checks it can write to your project folder before it does anything. On Windows, keep the folder out of Documents and Desktop, Windows blocks writes there. Setup tells you if you're in the wrong spot
- The free version of DaVinci Resolve works now. Setup figures out which version you have. One habit on the free version: after you open Resolve and your project, click Workspace → Scripts → resolve_bridge
- Resolve can't freeze Claude for 30 minutes anymore. If something's off, you find out right away
- Premiere export is one command: the final 4K file renders inside Premiere, no Media Encoder
- 4K videos: every graphic renders at real 4K now
- yt-dlp installs with the other tools, for pulling reference clips off YouTube

## 2026.09.05

- Captions are built with the graphics now, not burned on at the end. Re-render a video and the captions stay
- Sound effects run on short videos too, not just long-form
- Resolve audio polish uses the same loudness numbers as Premiere
- Background music is a normal add-on: flat bed, starts when the song actually starts, fades out at the end
- The docs got cut in half. Every rule lives in one place, so Claude opens fewer files per job
- The thumbnail maker left the package. This system stops at the exported video
- Cleanup: dead tools and one-off setup files removed

## 2026.09.03.2

- The one-shot edit: say "edit this video" once and the draft that comes back is finished. Every step run, every objective mistake already caught. You only watch for taste
- Every job runs the same 8 steps in order and keeps a RUN.md, so it picks up where it left off
- Rough cut: cuts land on the real audio edges, then two fresh reviewers check flow and slices before you see it
- Audio: gain measured per shoot, then the limiter. One command in Premiere
- Colour grade: one command puts the house look under the graphics
- Graphics: the default long-form pass includes word-synced text animations, punch cuts, slides, props and push-ins, about 12 beats a minute, all from one animation rulebook
- Two gates before you see anything: the plan is checked before rendering, every frame is checked after
- Sound design: every graphic beat gets a sound, placed on the Premiere timeline in one command. The full library ships in the package
- Setup is one sentence: open the folder in Claude Code and say "run the setup". At most one question and two restarts
- Works on Mac, Windows and Linux. The package is 84 MB smaller
