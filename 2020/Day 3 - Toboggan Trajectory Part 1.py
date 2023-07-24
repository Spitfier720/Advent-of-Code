#Using a grid and a predetermined slope, finding the number of obstacles in said grid.

import sys

#Finding the number of obstacles(trees) in the grid by following our slope.
def numTrees(grid):
    length = len(grid[0]) - 1
    slopex, slopey = 1, 3
    curPosx, curPosy = 0, 0
    numTrees = 0

    try:
        while(True):
            curPosx += slopex; curPosy += slopey
            numTrees += grid[curPosx][curPosy % length] == "#"
    
    except IndexError:
        return numTrees

print(numTrees(sys.stdin.readlines()))