#!/usr/bin/env pypy3

import fileinput

# counters
T = 0
T2 = 0
S = set()

for line in fileinput.input():
    ll = line.strip()
    if not ll:
        continue

    segs = ll.split(",")
    for s in segs:
        x, y = (int(x) for x in s.split("-"))
        S.add((x, y))

        for i in range(x, y + 1):
            g = str(i)

            # part 1
            h = len(g) // 2
            if g[h:] == g[:h]:
                T += i

            # part 2
            for k in range(1, h + 1):
                if len(g) % k != 0:
                    continue
                chunks = [g[l : k + l] for l in range(0, len(g), k)]
                if all(a == b for a, b in zip(chunks, chunks[1:])):
                    T2 += i
                    break

print(f"Tot {T} {T2}")
