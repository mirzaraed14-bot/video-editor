import sys, datetime
A = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_'
def sc2date(sc):
    n = 0
    for ch in sc[:11]:
        n = n * 64 + A.index(ch)
    ms = (n >> 23) + 1314220021721
    return datetime.datetime.utcfromtimestamp(ms / 1000).strftime('%Y-%m-%d')
for a in sys.argv[1:]:
    sc = a.strip('/').split('/')[-1]
    print(sc, sc2date(sc))
