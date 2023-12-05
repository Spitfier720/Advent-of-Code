import sys

seedLine = list(map(int, sys.stdin.readline().split(":")[1].strip().split()))
seeds = []

for i in range(0, len(seedLine), 2):
    seeds.append([seedLine[i], seedLine[i + 1]])

changed = set()

for line in sys.stdin.readlines():
    line = line.split()

    if(not line):
        changed = set()

    if(line and line[0].isdigit()): #Checks if the line isn't a newline or an irrelevant title
        line = list(map(int, line))
        dest, start, rangeLength = line[0], line[1], line[2]

        for i in range(len(seeds)):
            # Defines the ranges of the seed and the overlap between the mapping and seed intervals
            seedStart, seedEnd = seeds[i][0], seeds[i][1] + seeds[i][0] - 1
            overlapStart = max(seeds[i][0], start)
            overlapEnd = min(seeds[i][0] + seeds[i][1] - 1, start + rangeLength - 1)

            if((overlapStart <= overlapEnd) and i not in changed):
                if(seeds[i][0] < start):
                    seeds.append([seedStart, start - seedStart])
                
                if(seeds[i][0] + seeds[i][1] - 1 > start + rangeLength - 1):
                    seeds.append([start + rangeLength, seedEnd - (start + rangeLength - 1)])
                    
                seeds[i] = [overlapStart - (start - dest), overlapEnd - overlapStart + 1]

                changed.add(i)
    
print(min(seeds, key=lambda x: x[0])[0])