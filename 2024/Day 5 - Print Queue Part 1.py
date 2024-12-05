import sys

def isOrdered(line, orderings):
    for i in range(1, len(line)):
        if(line[i] in orderings and line[i - 1] in orderings[line[i]]): 
            return False
    
    return True

gettingRules = True
orderings = {}
sum = 0

for line in sys.stdin.readlines():
    if(line == "\n"):
        gettingRules = False
        continue

    if(gettingRules):
        line = list(map(int, line.split("|")))
        orderings.setdefault(line[0], set()).add(line[1])
    
    else:
        line = list(map(int, line.split(",")))
        
        if(isOrdered(line, orderings)):
            sum += line[(len(line) - 1) // 2]

print(sum)