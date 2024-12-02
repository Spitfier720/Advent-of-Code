import numpy
import sys

def checkSafe(line, movement):
    for x in range(1, len(line)):
        if(not(1 <= abs(line[x] - line[x - 1]) <= 3) or numpy.sign(line[x] - line[x - 1]) != movement):
            return False
    
    return True

numSafe = 0

for line in sys.stdin.readlines():
    line = list(map(int, line.split()))
    movement = numpy.sign(line[1] - line[0])
    
    isSafe = True
    
    if(checkSafe(line, movement)):
        print(line)
        numSafe += 1
        continue
    
    for x in range(len(line)):
        dampenedLine = line[:x] + line[x + 1:]
        dampenedMovement = numpy.sign(dampenedLine[1] - dampenedLine[0])
        if(checkSafe(dampenedLine, dampenedMovement)):
            print(dampenedLine)
            numSafe += 1
            break
    
print(numSafe)