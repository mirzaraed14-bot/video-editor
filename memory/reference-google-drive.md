---
name: reference-google-drive
description: Affan's Google Drive is mounted on this PC as G:\ by Google Drive for desktop; "upload to my drive" = copy into G:\My Drive (it syncs up in the background)
metadata:
  type: reference
---

`G:\My Drive\` is Affan's Google Drive (Google Drive for desktop, process GoogleDriveFS). Copying a file there uploads it; the tray
icon shows the sync. He keeps finished samples and reaction exports at the top level of My Drive (e.g. `harbinger.final.mp4`,
`Jeremy Miner reaction.mov`); batch folders work too (`My Drive/Onyx Samples - Batch 2/`, 2026-10-14). The Drive was ~97 % full
(≈ 19 GB free) on 2026-10-14: say so before uploading anything large. Related: [[project-onyx-sample-shorts]].

**Scott Clary client clips (2026-11-06):** the folder is `G:\My Drive\Scott Clary Clips - Affan` (folder id `1dEVI5uK5n2trVutpzIvdpl5lBi55ZzW4`); finished Shorts go there named by their title (house style: Title Case + one CAPS word + ` !`, e.g. `Robert Herjavec Almost DIED !.mov`). **Getting a share link without a browser:** Drive for desktop keeps a local index, `%LOCALAPPDATA%\Google\DriveFS\<account>\metadata_sqlite_db` (copy it with its `-wal` / `-shm` first, then sqlite3: table `items`, columns `id`, `local_title`, `file_size`). `id` is the cloud file id once the upload is done (`https://drive.google.com/file/d/<id>/view`); while uploading it reads `local-<n>` with file_size 0, so poll. Sharing stays private unless he asks. The Drive was 96 % full (20 GB free) on 2026-11-06.
