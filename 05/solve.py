#!/usr/bin/env pypy3

import fileinput

# counters
T = 0
T2 = 0

R = set()
I = set()

for line in fileinput.input():
    ll = line.strip()
    if not ll:
        continue

    if "-" in ll:
        R.add(tuple([int(x) for x in ll.split("-")]))
    else:
        I.add(int(ll))

for i in I:
    T += any(s <= i <= e for s, e in R)

cur = 0
for s, e in sorted(R):
    if s > cur:
        T2 += e - s + 1
        cur = e
    elif e > cur:
        T2 += e - cur
        cur = e

print(f"Tot {T} {T2}")
