# Decode an Instagram shortcode to its approximate creation time (UTC). Zero network.
# media_id = base64(shortcode, alphabet A-Za-z0-9-_); epoch_ms = (media_id >> 23) + 1314220021721
import sys, datetime
A = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_"
for sc in sys.argv[1:]:
    n = 0
    for ch in sc[:11]:
        n = n * 64 + A.index(ch)
    ms = (n >> 23) + 1314220021721
    print(sc, datetime.datetime.utcfromtimestamp(ms / 1000).strftime("%Y-%m-%d"))
