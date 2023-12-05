import sys

seeds = list(map(int, sys.stdin.readline().split(":")[1].strip().split()))
changed = set()

for line in sys.stdin.readlines():
    line = line.split()

    if(not line):
        changed = set()

    if(line and line[0].isdigit()): #Checks if the line isn't a newline or an irrelevant title
        line = list(map(int, line))
        dest, start, rangeLength = line[0], line[1], line[2]

        for i in range(len(seeds)):
            if(start <= seeds[i] <= start + rangeLength - 1 and i not in changed):
                seeds[i] -= (start - dest)
                changed.add(i)
    
print(min(seeds))