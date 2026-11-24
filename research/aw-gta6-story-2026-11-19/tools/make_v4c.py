# make_v4c.py: the hub's closing pass (other tellings searched, Instagram retried, the Darren question confirmed).
p = 'SEQUENCE.md'
s = open(p, encoding='utf-8').read()


def rep(a, b):
    global s
    assert a in s, a[:90]
    s = s.replace(a, b)


rep('''  - Checked outside the stream (19 Nov ~20:38-20:42, 3 web searches: Cincinnati, Detroit/Michigan, and the family + the Korean War):
    no record, directory listing or article of a Watkins auto parts store tied to the family. Nothing contradicts it either.
    Unverified. On the call Speed sums it up as "different owners basically", so the name may still trade somewhere.''',
    '''  - **Other tellings, searched (19 Nov ~20:38-21:00): none independent. The single-source line is earned.**
    - DaddySpeed's YouTube: all 455 uploads (2016-2026), titles + descriptions, searched for watkins / korea / auto parts / auto
      shop / grandpa / grandfather / gta / rockstar / 1950. The shop, the Korean War and GTA appear nowhere. Hits: "My Grandpa's 90th
      Birthday" (Mar 2023, 31 min), "Let's support my Grandfather!!!!!" (Dec 2023, 4:41), "Grandpa Speaking in Chicago" (2019, 33 min),
      all with EMPTY descriptions. Not downloaded or heard (`api/daddyspeed_all.json`).
    - The web: 5 searches (Cincinnati; Detroit/Michigan; the family + the Korean War; the dad + an interview; Harold Watkins + an auto
      shop / the Korean War). No record, directory or article. The only extra hit, watkinsautoparts.com, is a parked domain-for-sale
      page retelling the GTA story; it's not a source. Every article (Sportskeeda, ComingSoon, TalkEsport) retells this one call.
    - YouTube Shorts: every "dad + Watkins" Short (17-31K, `api/p_dadcall.*`, `api/p_korean.*`) is a clip of this same call.
    - **A lead, not a fact:** DaddySpeed's grandfather turned 90 in Mar 2023 (born ~1933). That matches Harold Watkins Sr.: a Detroit
      firefighter from 1955, Detroit's first Black fire chief (Detroit Free Press 1993; the Detroit Fire Department via Tribune). A
      Sept 2025 viral clip shows Speed meeting him, called his great-grandfather (`QbVUogd4UY4`, queued for download behind other
      sessions' YouTube jobs, not read). Nothing ties Harold to the shop or the Korean War. Speed has four great-grandfathers, so the
      Short never names one.
    - Unverified, and not contradicted. On the call Speed sums it up as "different owners basically", so the name may still trade
      somewhere.''')
rep('''1. **Instagram per beat:** the keyword search returned "No results" for 3 Speed phrasings ("ishowspeed watkins", "speed gta 6 name",
   "ishowspeed gta 6 dad"), so the dad call and the 2025 recognition were not found on Instagram. Only hashtags and Reels tabs were
   read (9 paced page loads).''',
    '''1. **Instagram per beat:** the keyword search returned "No results" for 3 Speed phrasings ("ishowspeed watkins", "speed gta 6 name",
   "ishowspeed gta 6 dad"). Then (the hub's retry) Speed's own Reels tab, scrolled back to early 2025 (95 reels with counts): no Watkins
   or Trailer 2 reel. DaddySpeed's Instagram is not findable by handle (@daddyspeed = 2 followers, @daddyspeedy = 69: neither is
   him). So the dad call and the 2025 recognition are NOT proven on Instagram (13 paced page loads in all).''')
rep('''3. **Facts and judgment calls open:**
   - G5: the family story has one source, his dad on the 2025 call.''',
    '''3. **Facts and judgment calls open:**
   - G5: the family story has one source, his dad on the 2025 call. Other tellings were searched and none was found (§ 4).''')
open(p, 'w', encoding='utf-8').write(s)

p = 'DELIVERY-NOTE.md'
s = open(p, encoding='utf-8').read()
rep('''1. **Instagram per beat:** the keyword search refused 3 Speed phrasings, so only hashtags and Reels tabs were read.''',
    '''1. **Instagram per beat:** keyword search refused 3 Speed phrasings. His own Reels tab (95 reels, back to early 2025) has no Watkins
   reel, and his dad's Instagram couldn't be found by handle.''')
rep('''3. **One source, one flag:** the family story rests on his dad alone. Three searches (Cincinnati, Detroit, the family + the Korean War)
   found no record of the shop either way. Jamal, a minor, is beside Speed in the 2025 frames.''',
    '''3. **One source, one flag:** the family story rests on his dad alone.
   - Searched with no other telling found: his dad's 455 YouTube uploads, 5 web searches, and every dad+Watkins Short (all clips of
     this same call).
   - A lead, not used: his dad's grandfather turned 90 in 2023, which matches Harold Watkins, Detroit's first Black fire chief, whom
     Speed met on stream in Sept 2025. Nothing ties him to the shop.
   - Jamal, a minor, is beside Speed in the 2025 frames.''')
open(p, 'w', encoding='utf-8').write(s)
print('ok')
