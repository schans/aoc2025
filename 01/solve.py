#!/usr/bin/env pypy3

import fileinput

# counters
T = 0
T2 = 0

cur = 50
for line in fileinput.input():
    ll = line.strip()
    if not ll:
        continue

    d = int(ll[1:])
    if ll.startswith("L"):
        cur -= d
    elif ll.startswith("R"):
        cur += d

    T2 += abs(cur // 100)
    if cur < 100:
        T2 += cur % 100 == 0
    if cur < 0 and cur + d == 0:
        T2 -= 1

    cur %= 100
    T += cur == 0

print(f"Tot {T} {T2}")
