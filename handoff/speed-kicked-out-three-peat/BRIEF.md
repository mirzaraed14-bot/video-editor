# BRIEF: His Mom Kicked Him Out (AW Short, IShowSpeed)

## HIS TELLA 1 (14 Nov 2026, 8:36, https://www.tella.tv/video/affans-video-cencgyh0)
Downloaded without a browser (`guide/guide.mp4`). Transcript (large-v3, GPU) in `guide/transcript.json`, frames in `guide/sheet_a.jpg`.
His ABW11 sequence was read back afterwards: `premiere/readback_his_1.tsv` (27.694 s). His edits are decisions.

### What he did to the cut (read back 14 Nov ~15:40; span = in-point + duration, NOT Premiere's outPoint column, which over-states the tail)
| # | His clip (HD-file time) | Words (large-v3 on his cut's own audio, `proof/seq_his1/asr.txt`) | vs my STOP-1 cut |
|---|---|---|---|
| 1 | support 27.56-29.13 | "At first, I didn't really have support." | same |
| 2 | covid 13.61-15.12 + 15.28-16.65 | "I didn't talk to my friends, right? I / was only talking to my online friends." | he cut 0.17 s inside the take (15.12-15.28); "right?" kept |
| 3 | fam 0.23-3.57 (+ V2 plate) | "(I) had that one viewer, and that viewer made me keep going." | head trimmed 0.13 s |
| 4 | fam 49.22-50.85 | "There was a clip that kind of blown up." | tail trimmed 0.13 s |
| 5 | fam 61.33-62.43 | "My mom seen the video." | same |
| 6 | fam 105.84-108.91 + 109.98-111.14 | "So boom, she kicked me out. I moved to my dad in Detroit. / Then I kept going." | 1 s pause cut |
| - | **Keystone (therapist) beat REMOVED** | | "he already looks so successful here ... remove this if you're being honest, and that yellow shirt clip" |
| - | **2024 card + "All right, IShowSpeed" REMOVED** | | |
| 8 | win24 40.27-42.91 | "Man, oh man. Streamer of the Year." | head trimmed 0.13 s |
| 9 | win25 13.25-15.35 (+ V2 walk-up) | "...IShowSpeed." | same |
| 10 | soty26 292.25-293.55 | "IShowSpeed!" | **"So the Streamer of the Year award goes to" REMOVED** ("we have already announced previously") |
| 10 | soty26 322.28-323.64 + 324.51-327.01 (+ V2 wide) | the Indonesian line, with a 0.9 s cut inside it | |
| 11 | support 31.60-34.63 | "(my) mom always supported me, you know, she just didn't understand it." | **"But my mom," and "I still love my mom" REMOVED**: the Short ends on "she just didn't understand it" |
Notes for the build: his last clip ends at 34.63, before the single->wide cut at 34.70 (no stray frames). Its in-point (31.598) sits ~40 ms after the voice onset at 31.56 (energy), so the first word may lose its "m"; flag it, don't change it.

### What he asked for (his words, lightly cleaned)
- "I distinctly remember there's a clip of Speed back in his old days where he was streaming in his mom's house, where he would constantly be told to shut the stream off, 'what is he doing, what the hell is he doing', and his mom would come in all angry, and then after she left Speed would be on the verge of crying or very sad. **We need to include those moments.**"
- "After 'my mom seen the video' we can include all the parts where his mother called him and said to shut the stream down and everything."
- "There are moments of Speed calling up his mother ... he just wouldn't get a nice reply ... I believe it was his birthday, when he was at Aiden house, Adin Ross' house ... called up his mom, he didn't even get a reply properly. **Find all of these moments where we just genuinely feel bad for Speed, but he still kept going.**"
- Mused, not decided: after "Then I kept going", "I kept going, my dad didn't really care, my dad let me ... shout out to my mom too, I still love my mom", and "and now here we are" (if Speed says it in this podcast), then straight into the awards ("or what if we don't include that bit 'now here we are' and we directly go into IShowSpeed").
- **His order:** "After this bit [My mom seen the video] we have to put all the mom bits we can find which fit my criteria, and I'm gonna go in there and mix and match them myself. Your job is to just put them in between these bits [before 'So boom, she kicked me out']. Find all the bits, put them here so that I can approve, and **then** you can start the final build." / "Don't start the build until I approve it."

### Open conflict to show him first
- **The 2020-22 mom-house streams have Speed at 15-17** (born 21 Jan 2005). His standing rule ("no minors on frame, ever; real-life children stay out"; this job's constraint "every frame adult-era, nothing before 21 Jan 2023") excludes them. He asked for them by name, so they are found and laid out for his approval, each labelled with its date and Speed's age; the final build uses them only on his explicit yes. The birthday call is checked for its date (his 18th birthday was 21 Jan 2023).
