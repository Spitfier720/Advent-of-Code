import sys

def isOrdered(line, orderings):
    for i in range(1, len(line)):
        if(line[i] in orderings and line[i - 1] in orderings[line[i]]): 
            return False
    
    return True

def reorder(line, orderings):
    prevLine = [0] * len(line)

    while(prevLine != line):
        prevLine = list(line)

        for i in range(1, len(line)):
            if(line[i] in orderings and line[i - 1] in orderings[line[i]]):
                line[i], line[i - 1] = line[i - 1], line[i]
    
    return line

gettingRules = True
orderings = {}

unorderedUpdates = []

for line in sys.stdin.readlines():
    if(line == "\n"):
        gettingRules = False
        continue

    if(gettingRules):
        line = list(map(int, line.split("|")))
        orderings.setdefault(line[0], set()).add(line[1])
    
    else:
        line = list(map(int, line.split(",")))
        
        if(not isOrdered(line, orderings)):
            unorderedUpdates.append(line)

sum = 0

for line in unorderedUpdates:
    sum += reorder(line, orderings)[(len(line) - 1) // 2]

print(sum)