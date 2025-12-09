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


def dist(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2


D = set()
for i in range(len(B)):
    for j in range(i + 1, len(B)):
        d = dist(B[i], B[j])
        D.add((d, i, j))
D = sorted(D)

G = list()
seen = set()
for n, (d, i, j) in enumerate(D):
    if i not in seen and j not in seen:
        # new
        seen.add(i)
        seen.add(j)
        G.append({i, j})
    elif (i in seen and j not in seen) or (i not in seen and j in seen):
        # attach
        seen.add(i)
        seen.add(j)
        for gi, g in enumerate(G):
            if i in g:
                g.add(j)
            if j in g:
                g.add(i)
    elif i in seen and j in seen:
        # merge or ignore
        same = False
        ni = nj = -1
        ii = ij = -1
        for gi, g in enumerate(G):
            if i in g and j in g:
                same = True
            if i in g:
                ii = gi
            if j in g:
                ij = gi

        if not same:
            # merge
            ns = {i, j}
            gii = G[ii]
            gij = G[ij]
            ns |= gii
            ns |= gij
            G.remove(gii)
            G.remove(gij)
            G.append(ns)

    # part 1
    if n == 1000:
        sizes = sorted([len(g) for g in G])
        T = sizes.pop() * sizes.pop() * sizes.pop()

    # part 2
    if len(seen) == len(B) and len(G) == 1:
        T2 = B[i][0] * B[j][0]
        break

print(f"Tot {T} {T2}")
