#!/usr/bin/env pypy3

import fileinput

# counters
T = 0
T2 = 0

B = list()

for line in fileinput.input():
    ll = line.strip()
    if not ll:
        continue
    B.append(tuple(map(int, ll.split(","))))


def square(a, b):
    return (1 + abs(a[0] - b[0])) * (1 + abs(a[1] - b[1]))


S = list()
for i in range(len(B)):
    for j in range(i + 1, len(B)):
        a = square(B[i], B[j])
        T = max(T, a)
        S.append((a, i, j))

S = sorted(S, reverse=True)

for a, i, j in S:
    minx = min(B[i][0], B[j][0])
    maxx = max(B[i][0], B[j][0])
    miny = min(B[i][1], B[j][1])
    maxy = max(B[i][1], B[j][1])

    found = False
    for k in range(len(B)):
        if k == i or k == j:
            continue

        if minx < B[k][0] < maxx and miny < B[k][1] < maxy:
            found = True
            break

        if not (minx < B[k][0] < maxx or miny < B[k][1] < maxy):
            continue

        for l in range(len(B)):
            if l == i or l == j or l == k:
                continue

            # horizontal
            if B[k][1] == B[l][1] and miny < B[k][1] < maxy:
                if B[l][0] <= minx and B[k][0] >= maxx:
                    found = True
                    break
                if B[k][0] <= minx and B[l][0] >= maxx:
                    found = True
                    break

            # vertical
            if B[k][0] == B[l][0] and minx < B[k][0] < maxx:
                if B[l][1] <= miny and B[k][1] >= maxy:
                    found = True
                    break
                if B[k][1] <= miny and B[l][1] >= maxy:
                    found = True
                    break

        if found:
            break
    if not found:
        T2 = a
        break

print(f"Tot {T} {T2}")
