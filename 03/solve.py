#!/usr/bin/env pypy3

import fileinput

# counters
T = 0
T2 = 0

for line in fileinput.input():
    ll = line.strip()
    if not ll:
        continue

    # part 1
    bank = [int(x) for x in ll]
    m = max(bank[:-1])
    mi = bank.index(m)
    e = max(bank[mi + 1 :])
    T += m * 10 + e

    # part 2
    for i in range(12, 0, -1):
        r = len(bank)
        m = max(bank[: r - i + 1])
        mi = bank.index(m)
        bank = bank[mi + 1 :]
        T2 += m * 10 ** (i - 1)

print(f"Tot {T} {T2}")
