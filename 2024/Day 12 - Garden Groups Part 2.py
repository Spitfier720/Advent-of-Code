import sys

def findPrice(pos, grid, unChecked):
    directions = [
        (-1, 0),
        (0, 1),
        (1, 0),
        (0, -1)
    ]

    area = 0
    perimeter = set()

    visited = {pos}
    queue = [pos]

    while(queue):
        area += 1
        curPos = queue.pop(0)
        unChecked.discard(curPos)

        for d in directions:
            if((curPos[0] + d[0], curPos[1] + d[1]) in visited):
                continue

            if(not isValidPos((curPos[0] + d[0], curPos[1] + d[1]), grid, pos)):
                perimeter.add((curPos[0] + (d[0] / 10), curPos[1] + (d[1] / 10)))
                continue

            else:
                queue.append((curPos[0] + d[0], curPos[1] + d[1]))
                visited.add((curPos[0] + d[0], curPos[1] + d[1]))
    
    numSides = 0

    while(perimeter):
        numSides += 1
        curPos = perimeter.pop()

        perQueue = [curPos]
        perVisited = {curPos}

        while(perQueue):
            curPos = perQueue.pop(0)
            perimeter.discard(curPos)

            for d in directions:
                if((curPos[0] + d[0], curPos[1] + d[1]) in perVisited or (curPos[0] + d[0], curPos[1] + d[1]) not in perimeter):
                    continue
                    
                perQueue.append((curPos[0] + d[0], curPos[1] + d[1]))
                perVisited.add((curPos[0] + d[0], curPos[1] + d[1]))

    return area * numSides
    

def isValidPos(pos, grid, origPos):
    return 0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[0]) and grid[pos[0]][pos[1]] == grid[origPos[0]][origPos[1]]

grid = []
unChecked = set()
rowNum = 0

for line in sys.stdin.readlines():
    unChecked.update({(rowNum, x) for x in range(len(line.strip()))})
    grid.append(line.strip())
    rowNum += 1

totalPrice = 0

while(unChecked):
    totalPrice += findPrice(unChecked.pop(), grid, unChecked)

print(totalPrice)