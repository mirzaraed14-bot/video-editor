# Decode Instagram shortcodes to their UTC post date (media id >> 23 = ms since IG epoch 1314220021721).
import sys, datetime
A = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_'
for sc in sys.argv[1:]:
    n = 0
    for c in sc[:11]:
        n = n * 64 + A.index(c)
    ms = (n >> 23) + 1314220021721
    print(sc, datetime.datetime.fromtimestamp(ms / 1000, datetime.timezone.utc).strftime('%Y-%m-%d'))
