import numpy
import sys

numSafe = 0

for line in sys.stdin.readlines():
    line = list(map(int, line.split()))
    movement = numpy.sign(line[1] - line[0])
    
    isSafe = True
    
    for x in range(1, len(line)):
        if(not(1 <= abs(line[x] - line[x - 1]) <= 3) or numpy.sign(line[x] - line[x - 1]) != movement):
            isSafe = False
            break
        
    numSafe += isSafe
    
print(numSafe)