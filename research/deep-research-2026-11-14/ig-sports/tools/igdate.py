# igdate.py <shortcode> [...]: decode an Instagram shortcode to its post date (UTC) from the media id's timestamp bits.
import sys, datetime
A = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_"
for sc in sys.argv[1:]:
    n = 0
    for c in sc[:11]:
        n = n * 64 + A.index(c)
    ms = (n >> 23) + 1314220021721
    print(sc, datetime.datetime.fromtimestamp(ms / 1000, datetime.UTC).strftime("%Y-%m-%d"))
