#!/usr/bin/env pypy3

import fileinput

# counters
T = 0
T2 = 0

OP = []
N = []
L = []
S = []
ml = 0
for line in fileinput.input():
    ll = line
    if not ll.strip():
        continue

    ml = max(ml, len(ll))
    if ll[0] in "*+":
        OP = ll.split()
        for i in range(len(ll)):
            if ll[i] == " ":
                continue
            else:
                S.append(i)
    else:
        N.append([int(x) for x in ll.strip().split()])
        L.append(ll)

S[-1] += 1  # "add space at end"
R = len(N)
C = len(N[0])
assert C == len(OP)

for i, op in enumerate(OP):
    # col nums
    s, e = S[i], S[i + 1] - 2
    ns = []
    for c in range(e, s - 1, -1):
        n = ""
        for r in range(R):
            if c < len(L[r]) and L[r][c] != " ":
                n += L[r][c]
        ns.append(int(n))

    if op == "*":
        t = t2 = 1
        for j in range(R):
            t *= N[j][i]
        for n in ns:
            t2 *= n
    elif op == "+":
        t = t2 = 0
        for j in range(R):
            t += N[j][i]
        for n in ns:
            t2 += n
    else:
        assert False
    T += t
    T2 += t2

print(f"Tot {T} {T2}")
