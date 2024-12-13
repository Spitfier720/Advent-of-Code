import sys

def solveLinearEq(a1, b1, r1, a2, b2, r2):
    y = ((r2 * a1) - (a2 * r1)) / ((b2 * a1) - (a2 * b1))

    if(y % 1 != 0 or not (0 <= y <= 100)):
        return (-1, -1)

    x = (r1 - (b1 * y)) / a1

    if(x % 1 != 0 or not (0 <= x <= 100)):
        return (-1, -1)
    
    return (int(x), int(y))

machineIndex = 0

buttonA, buttonB = (0, 0), (0, 0)
prize = (0, 0)

tokensSpent = 0

for line in sys.stdin.readlines():
    if(not line.strip()):
        result = solveLinearEq(buttonA[0], buttonB[0], prize[0], buttonA[1], buttonB[1], prize[1])

        if(result != (-1, -1)):
            tokensSpent += (3 * result[0]) + result[1]

        machineIndex = 0
        continue

    line = line.strip().split(":")[1].strip().split(",")

    xCoord = int(line[0].split("+" if machineIndex != 2 else "=")[1].strip())
    yCoord = int(line[1].split("+" if machineIndex != 2 else "=")[1].strip())

    match(machineIndex):
        case 0:
            buttonA = (xCoord, yCoord)
        
        case 1:
            buttonB = (xCoord, yCoord)
        
        case 2:
            prize = (xCoord, yCoord)
    
    machineIndex += 1

result = solveLinearEq(buttonA[0], buttonB[0], prize[0] + 10000000000000, buttonA[1], buttonB[1], prize[1] + 10000000000000)

if(result != (-1, -1)):
    tokensSpent += (3 * result[0]) + result[1]

print(tokensSpent)