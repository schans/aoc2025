#!/usr/bin/env pypy3

import fileinput

# counters
T = T2 = 0
DIRS = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]

G = []
for line in fileinput.input():
    ll = line.strip()
    if not ll:
        continue

    G.append(list(ll))

R = len(G)
C = len(G[0])


for r in range(R):
    for c in range(C):
        if G[r][c] == "@":
            t = 0
            for dr, dc in DIRS:
                rr, cc = r + dr, c + dc
                if 0 <= rr < R and 0 <= cc < C:
                    if G[rr][cc] == "@":
                        t += 1
            if t < 4:
                T += 1

pT = 1e12
while True:
    for r in range(R):
        for c in range(C):
            if G[r][c] == "@":
                t = 0
                for dr, dc in DIRS:
                    rr, cc = r + dr, c + dc
                    if 0 <= rr < R and 0 <= cc < C:
                        if G[rr][cc] == "@":
                            t += 1
                if t < 4:
                    T2 += 1
                    G[r][c] = "."
    if pT == T2:
        break
    pT = T2

print(f"Tot {T} {T2}")
