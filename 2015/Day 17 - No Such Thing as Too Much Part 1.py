#A simple knapsack problem, with eggnog.

import itertools, sys

containers = [int(x.strip()) for x in sys.stdin.readlines()]
comboCount = 0

for i in range(1, len(containers) + 1):
    for x in itertools.combinations(containers, i):
        if(sum(x) == 150):
            comboCount += 1

print(comboCount)