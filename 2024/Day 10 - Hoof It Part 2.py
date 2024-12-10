import sys

def getScore(pos, grid):
    directions = [
        (-1, 0),
        (0, 1),
        (1, 0),
        (0, -1)
    ]
    
    count = 0
    
    queue = [pos + (0,)]
    visited = set()
    
    while(queue):
        curPos = queue.pop(0)
        curPos, height = curPos[:2], curPos[2]
        visited.add(curPos)
        
        if(grid[curPos[0]][curPos[1]] == "9"):
            count += 1
        
        for d in directions:
            if(isValidStep(curPos[0] + d[0], curPos[1] + d[1], height, grid)):
                queue.append((curPos[0] + d[0], curPos[1] + d[1], height + 1))
    
    return count

def isValidStep(x, y, h, grid):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and int(grid[x][y]) - 1 == h
    

grid = []
zeroPos = set()
row = 0

for line in sys.stdin.readlines():
    for i in range(len(line)):
        if(line[i] == "0"):
            zeroPos.add((row, i))
    
    row += 1
    grid.append(line.strip())

sumScore = 0

for pos in zeroPos:
    sumScore += getScore(pos, grid)

print(sumScore)