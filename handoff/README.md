# handoff/ — the drop box between the desktop and the MacBook

Written by `./sync.sh`: each job's small TEXT state (RUN.md, the EDL, transcript, caption lines, .srt).
Media never lands here. The machine that needs a file copies it out of `handoff/<job>/`;
the job folder in `projects/` stays local to the machine that did the work.
