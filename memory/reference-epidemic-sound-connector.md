---
name: reference-epidemic-sound-connector
description: "Epidemic Sound is the user's licensed music/SFX library; its MCP OAuth sign-in fails here, so use an API key in .mcp.json instead"
metadata: 
  node_type: memory
  type: reference
  originSessionId: e1b9cd8c-a044-4294-9e79-318eb202a8a0
  modified: 2026-09-16T07:34:46.237Z
---

**Epidemic Sound is the creator's licensed library** for both music (`audio/music/`) and sound effects
(`assets/sfx/`), confirmed 2026-09-16. It ships an official MCP server, launched Aug 2026.

- **Server URL:** `https://www.epidemicsound.com/a/mcp-service/mcp`
- **No partnership agreement or developer-portal account is needed** — an ordinary subscriber account
  works. Docs: `developers.epidemicsound.com/docs/mcp`.

**The OAuth route FAILED for this user (2026-09-16):** *"Couldn't register with Epidemic Sound's
sign-in service… or add an OAuth Client ID in the connector settings"* (ref `ofid_7f5aa0e57648e07f`).
**Cause:** Epidemic uses Dynamic Client Registration but only against *"an allowlist of vetted MCP
client redirect URIs"*, so a client whose redirect URI is not on that allowlist cannot register.
Adding a Client ID does not help — Epidemic does not issue client IDs to individual subscribers.

**The working route is an API KEY**, which Epidemic's own docs assign to Claude Code specifically
(OAuth is for Cursor / Claude Desktop). Key from
`https://www.epidemicsound.com/account/api-keys`, valid one year. It goes in the project's
`.mcp.json` as a Bearer header:

```json
"epidemic-sound": {
  "type": "http",
  "url": "https://www.epidemicsound.com/a/mcp-service/mcp",
  "headers": { "Authorization": "Bearer <key>" }
}
```

`.mcp.json` is gitignored here and the project is not a git repo, so the key stays machine-local.
**Claude cannot write `.mcp.json` itself** (blocked as self-modification) and **must never be given
the key in chat** — the user pastes it and restarts Claude Code.

**This does NOT contradict [[reference-higgsfield-connector]].** That note says the `.mcp.json` route
failed for Higgsfield — but that was an OAuth *sign-in* failure. An API key involves no sign-in flow,
so `.mcp.json` is the right home for Epidemic and the wrong one for Higgsfield.

**CONNECTED AND VERIFIED 2026-09-16.** The one mistake to avoid: replacing the whole placeholder
string drops the word `Bearer`, and the server answers 401. The value must read `Bearer <key>`.

**It DOWNLOADS — this is a full pipeline integration, not just search.** Tools:
`SearchRecordings`, `SearchSoundEffects`, `SearchSimilarToRecording`, `SearchSimilarToSoundEffect`,
`SearchExternalReferences` (find by Spotify track), `DownloadRecording`, `DownloadSoundEffect`,
`DownloadRecordingEdit`, `EditRecording` + `PollEditRecordingJob`, and a voiceover set
(`GenerateVoiceover`, `ListVoices`, `DownloadVoiceover`).

- Download tools take `fileType: MP3 | WAV` and return an `assetUrl` to curl down. **Use WAV** into
  `assets/sfx/` and `audio/music/`; the pipeline works on files, not the catalogue.
- **Music tracks carry separated STEMS** (drums, bass, melody, instruments, vocals). For a bed under
  narration, the no-drums stems are often better than the full mix.
- Search filters that matter: `vocals:false`, `duration`, `bpm`, `moodSlugs`, `taxonomySlugs`.
  Useful mood/genre slugs seen: suspense, dark, sneaking, mysterious, dark ambient, crime scene.
- `EditRecording` re-cuts a track to a target length — useful for fitting a bed to a runtime.

**How to apply:** the licence attaches to the creator's own account, so everything is pulled under
their key. Downloaded files go in `assets/sfx/` (step 6) and `audio/music/` (the music pass).
Related: [[project-gta-documentary-channel]].
