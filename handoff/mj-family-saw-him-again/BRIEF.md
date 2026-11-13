# BRIEF: MJ "Brother Saw Him AGAIN": Affan's direction

## Tella walkthrough 1 (13 Nov 2026 ~18:3x PKT): "Transforming into Michael Jackson"
- Link: https://www.tella.tv/video/transforming-into-michael-jackson-43p4b8l4 (4:42).
- Local copy: `guide/guide.mp4`. Transcript (faster-whisper large-v3, word-timed): `guide/guide.json`. Frames: `guide/fr/`.
- **No narration:** the audio is his cut playing.
- **What it shows:**
  - He edited `MJ Family Saw Him Again - raw bits` directly in ABW11.
  - **His order, played at 0:04-0:38 (~34 s):**
    1. Jackie (ET Berlin): "I got so emotional because he became Michael on that screen. It brought tears to my eyes."
    2. Kevin (ET Berlin): "The emotion it brings out in your uncles... how does that make you feel?"
    3. Jaafar (ET Berlin): "It makes me emotional. I remember when they first saw the screen test, I got a call from
       each one of them individually. Even my Uncle Tito, rest in peace to him. I just remember them getting emotional
       on the phone." **Kevin's "rest in peace" is cut** (one RIP heard).
    4. King (ScreenRant): "When I went over to Katherine's house and showed Katherine Jaafar in his makeup... she was in
       a wheelchair and I bent down and she just said, that's Michael." On screen: Katherine (glasses, pearls), then King.
    5. Jaafar (TODAY): "There were moments she couldn't tell if it was me or Michael."
    6. La Toya (Extra): "You look at him and you forget that it's Jaafar and you think it's your brother."
    7. Jackie (Extra LA): "But I'm watching my nephew."
    8. La Toya (ET LA): "Jaafar did an excellent job."
  - **0:40-4:00, on the timeline:** he drags dialogue pieces up from V1 to V2 at several spots (~10-14 s, ~17 s, ~24 s,
    ~32-33 s): **overlay slots**, the way he marks them (memory: "Overlay slots are marked by dragging the face clips up
    to V2").
  - **The program monitor shows ET's group photo with the boy in the red suit (~1:02-2:00, timecode 00:04:21 on it).**
    In the raw bits that frame was covered on V2; check whether his edit uncovered it.
  - **4:15-4:42, YouTube search "michael movie ending":** Movieclips "Michael (2026) 4K - Bad (11/11)" 6.1M; "Michael
    Closes Out Victory Tour in Front of 90,000 Fans | Michael" (Musical Picks, 1.2M, 9:29); "Jaafar Jackson Performs
    'Bad' (Full Scene) | Michael (2026) (4K)" (MrLOCKiDY, 2.6M); "Your Wish Is My Command | MICHAEL (2026) Movie CLIP
    4K" (Movieclips, 800K). **Read: he wants the film's ending (the Bad-tour / Victory-tour stage footage) as overlay
    picture.**
- **Pending:** the read-back of his edit from ABW11 (`premiere/readback_his_edit.tsv` + `premiere/his_edit_diff.md`), to
  get the exact trims, overlay slots, and whatever he added.

## Read-back of his edit (13 Nov, `premiere/readback_his_edit.tsv` + `premiere/his_edit_diff.md`)
- **His cut: 33.3 s.** Order: A1 Jackie (3 inner cuts incl. the catch) → A2 + A3 Kevin → A4 Jaafar (4 inner cuts; Kevin's
  "rest in peace" removed) → A5 King "When I went over... in his makeup" (1.1 s pause removed) → A6 King from "in a
  wheelchair... that's Michael" (head trimmed) → B4 TODAY "there were moments she couldn't tell if it was me or Michael"
  (cut inside at 340.17-340.71: check by ear) → B1 La Toya → C1 Jackie "But I'm watching my nephew" → C4 La Toya "Jaafar
  did an excellent job".
- Deleted: B2, B3, C2, C3, C5, C6; the covers A2v, A4a, A4b, A5b, B4v. Kept covers: A1v (Jaafar as Michael over "became
  Michael"), A5a (Katherine), A6v (the last 1.5 s).
- **Overlay slots (his V2 convention):** A4's picture moved to V2 at tl 9.34-15.48 (V1 empty under it), and C4's picture on
  V2 at tl 31.70-33.30.
- **His music:** "JVKE - golden hour (instrumental).mp3" on A2 (in 23.46). His rule says music is his job.
- **Minors:**
  - ET's group photo with the boy shows at tl 10.58-13.19, inside slot 1, so it must be covered when the slot is filled.
  - ScreenRant at tl 18.05-20.55: his crop (position 1.58 = the left 608 px of the frame) shows only King and Nia Long,
    and the child actor sits far right (`proof/picks/sr_crop_check.jpg`), so it is clean as long as the crop stays left.
- **His YouTube search, read as the overlay picture he wants:** the film's ending (Movieclips "Bad (11/11)" 4K
  `Ms4xIJh7V2M`, 6.1M; "Closes Out Victory Tour").

## Tella walkthrough 2, NARRATED (13 Nov ~19:xx PKT): "Affan's video", https://www.tella.tv/video/affans-video-b9hhbez3
- Local copy: `guide2/guide.mp4` (5:13). Transcript: `guide2/guide.json`. Note frames with the program timecode:
  `guide2/fr/notes_sheet.jpg`.
- **His last words: "that's the creative direction, you can start your process now" = GO for the build from his cut.**
- **His overlay direction, resolved to his timeline (tl = his cut, read back above):**

| tl | Line under it | His direction (quoted) | Resolved |
|---|---|---|---|
| 1.77-3.54 (A1v) | Jackie "became Michael on that screen" | "this overlay is perfect, but you just have to slow it down and... place it in the middle" | Keep the bj_4k Billie Jean overlay, slow-mo, subject centred |
| ~9.34-11.44 | Jaafar "when they first saw the screen test, I got a call" | "use Jaafar's first screen test on the actual movie, a video overlay preferably... do the letterbox, but not too zoomed out, keep it very zoomed in but still letterboxed" | Screen-test footage (video), letterbox with blurred fill (his look), tight. Source to find |
| ~11.44-13.2 | "from each one of them individually" | "use all the brothers together, including Michael, just in a photo... a still overlay... you can enhance it with Higgsfield" | A photo of the brothers with Michael, adults only (never the child-era Jackson 5), HQ, Higgsfield upscale (preflight cost) |
| ~13.2-16.58 | "even my Uncle Tito, rest in peace to him... emotional on the phone" | "use Tito Jackson's interview... him just talking, don't use the audio, just use it as an overlay... keep it till here"; "with the Tito overlay make sure to gray it out to signify that he has passed away" | Tito talking (video, muted), desaturated, to the end of "phone" |
| 16.58-18.05 (A5a) | King "When I went over to Katherine's house and showed Katherine" | "this overlay's too old, Katherine looks very young here... find Katherine Jackson with this guy [Graham King], preferably a video overlay... if not possible, Katherine these days, red carpet or whatever... use the letterbox format on this also" | Recent Katherine (2025-26), ideally with King; letterboxed |
| 18.05-20.55 | King on camera | "place this guy at the middle" | Re-crop King centred (the child actor stays out of frame, far right) |
| 22.99-24.49 (A6v) | "she just said, that's Michael" | "you can use the Beat It behind the scenes... wherever you just see him clearly... a good face close-up... with a beaded jacket close up, really nice clean shot of Jaafar as Michael" | A Beat It BTS/making-of close-up of Jaafar as Michael (jacket detail), clean |
| 31.70-33.30 (end slot) | La Toya "Jaafar did an excellent job" | "end with the overlay of Jaafar Jackson as Michael, slow motion... let's do this turning head back overlay at the end, because it just suits better at the end" | The film's ending Bad-tour scene, the head-turn shot, slow-mo, as the last image |
