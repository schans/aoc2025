#!/usr/bin/env pypy3

import fileinput
from collections import defaultdict

# counters
T = 0
T2 = 0

B = set()
D = defaultdict(int)
PD = defaultdict(int)

for line in fileinput.input():
    ll = line.strip()
    if not ll:
        continue

    if "S" in ll:
        B.add(ll.index("S"))
        PD[ll.index("S")] = 1
        continue

    if "^" in ll:
        for c, ch in enumerate(ll):
            if ch == ".":
                D[c] += PD[c]
            elif ch == "^":
                if c in B:
                    B.remove(c)
                    B.add(c - 1)
                    B.add(c + 1)
                    T += 1
                    D[c - 1] += PD[c]
                    D[c + 1] += PD[c]
        PD = D
        D = defaultdict(int)

T2 = sum([v for _, v in PD.items()])
print(f"Tot {T} {T2}")
