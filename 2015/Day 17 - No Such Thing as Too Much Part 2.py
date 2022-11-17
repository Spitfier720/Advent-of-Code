#A simple knapsack problem, with eggnog.

import itertools, sys

containers = [int(x.strip()) for x in sys.stdin.readlines()]
comboCount = 0
foundCombo = False

#1-indexed since the combination must hold at least one element.
for i in range(1, len(containers) + 1):
    #Using itertools.combinations due to the fact that it's faster than recursively finding the algorithm.
    for x in itertools.combinations(containers, i):
        if(sum(x) == 150):
            comboCount += 1
            foundCombo = True
    
    #Breaking the loop if the combo is found, since we only want the minimum number of containers.
    if(foundCombo):
        break

print(comboCount)