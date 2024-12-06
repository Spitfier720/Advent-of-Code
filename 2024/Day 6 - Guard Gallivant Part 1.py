import sys

def numPosCovered(obstacles, guardPos, grid):
    directions = [
        (-1, 0),
        (0, 1),
        (1, 0),
        (0, -1)
    ]
    visited = {guardPos}
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
                    (x, guardPos[1]) if i % 2 == 0 else (guardPos[0], x)
                    for x in range(guardPos[i % 2] + directions[i % 4][i % 2], 
                                   0 if directions[i % 4][i % 2] == -1 else (len(grid) if i % 2 == 0 else len(grid[0])), 
                                   directions[i % 4][i % 2])
                )
            )

            return len(visited)
        
        visited.update(
            set(
                (x, guardPos[1]) if i % 2 == 0 else (guardPos[0], x)
                for x in range(guardPos[i % 2] + directions[i % 4][i % 2], filteredStops[0][i % 2], directions[i % 4][i % 2])
            )
        )
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

print(numPosCovered(obstacles, guardPos, grid))