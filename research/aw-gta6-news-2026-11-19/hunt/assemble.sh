#!/bin/bash
cd "$(dirname "$0")"
python -I tools/logtable.py > logtable.md
{
  cat hunt-head.md
  echo "## (a) Channel log"
  echo
  echo "Lists are yt-dlp flat playlists of Twitch clips, top 150 by views per range. \"fresh\" = pulled 20 Nov from this run (\`hunt/lists/\`); \"older 24hr\" = the 19 Nov pull in \`../twitch/\` (day 1 only; the Kai 7d there is the 98-clip list). \"all\" (all-time top 20) was not pulled for anyone. Title grep = bigfoot, big foot, skunk, sasquatch, mangrove, effigy, monster, creature, scream, scared, scary, jumpscare, spooked, wtf, what is that, knocked, passed out, swamp, ape, kirk, drone (plus the misspelling \"biggfoot\", which I caught by eye). Top-15 most-viewed clips per channel with vague titles were opened as thumbnail contact sheets for every channel that had a list; the sheets I read are in \`hunt/sheets/\`."
  echo
  cat logtable.md
  echo
  echo "Not pulled this run (lane busy, no fresh list): ludwig, asmongold, timthetatman, sodapoppin, ohnepixel, clix, valkyrae, pokimane, shroud, nadeshot, n3on, plaqueboymax, agent00, emiru, mizkif, hasanabi, esfandtv, quin69, ninja, dream, ranboo, tommyinnit, swagg. Where the table shows an older 24hr count, day 1 was grepped; otherwise the channel is uncovered. Empty or short lists (adinross, ishowspeed 7d, fanum 24hr, summit1g 24hr, kaicenat 7d) are unreliable pulls and must not be read as \"no clips\"; summit1g 7d and lacy 7d were never obtained."
  cat hunt-body.md
} > HUNT-TWITCH.md
echo wrote HUNT-TWITCH.md; wc -l HUNT-TWITCH.md
