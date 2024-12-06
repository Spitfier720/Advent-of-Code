import sys

def simulateGuard(obstacles, guardPos, grid):
    directions = [
        (-1, 0),
        (0, 1),
        (1, 0),
        (0, -1)
    ]
    visited = {guardPos + directions[0]}
    i = 0

    while(True):
        filteredStops = sorted(
            list(
                filter(
                    lambda x: x[1 - (i % 2)] == guardPos[1 - (i % 2)] and
                              ((x[i % 2] > guardPos[i % 2]) if directions[i % 4][i % 2] == 1 else (x[i % 2] < guardPos[i % 2])), 
                    obstacles
                )
            ),
            key = lambda x: x[i % 2],
            reverse = directions[i % 4][i % 2] == -1
        )

        if(not filteredStops):
            visited.update(
                set(
                    (x, guardPos[1]) + directions[i % 4] if i % 2 == 0 else (guardPos[0], x) + directions[i % 4]
                    for x in range(guardPos[i % 2] + directions[i % 4][i % 2], 
                                   0 if directions[i % 4][i % 2] == -1 else (len(grid) if i % 2 == 0 else len(grid[0])), 
                                   directions[i % 4][i % 2])
                )
            )

            return visited, False
        
        for x in range(guardPos[i % 2] + directions[i % 4][i % 2], filteredStops[0][i % 2], directions[i % 4][i % 2]):
            if(((x, guardPos[1]) + directions[i % 4] if i % 2 == 0 else (guardPos[0], x) + directions[i % 4]) in visited):
                return visited, True
            
            visited.add((x, guardPos[1]) + directions[i % 4] if i % 2 == 0 else (guardPos[0], x) + directions[i % 4])

        '''visited.update(
            set(
                (x, guardPos[1]) + directions[i % 4] if i % 2 == 0 else (guardPos[0], x) + directions[i % 4]
                for x in range(guardPos[i % 2] + directions[i % 4][i % 2], filteredStops[0][i % 2], directions[i % 4][i % 2])
            )
        )'''
        guardPos = (filteredStops[0][0] - directions[i % 4][0], filteredStops[0][1] - directions[i % 4][1])
        i += 1

grid = []
obstacles = set()
guardPos = (0, 0)
rowNum = 0

for x in sys.stdin.readlines():
    for i in range(len(x)):
        if(x[i] == "#"):
            obstacles.add((rowNum, i))
        
        if(x[i] == "^"):
            guardPos = (rowNum, i)
    
    rowNum += 1
    grid.append(x.strip())

loopingPos = set()
numLoops = 0

for pos in simulateGuard(obstacles, guardPos, grid)[0]:
    if(pos[:2] != guardPos and pos[:2] not in loopingPos):
        print(pos[:2])

        loopingPos.add(pos[:2])
        updatedObstacles = set(obstacles)
        updatedObstacles.add(pos[:2])
        numLoops += simulateGuard(updatedObstacles, guardPos, grid)[1]

print(numLoops)