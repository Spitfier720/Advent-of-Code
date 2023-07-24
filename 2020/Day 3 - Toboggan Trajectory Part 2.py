#Using a grid and a predetermined slope, finding the number of obstacles in said grid.

import sys, math

#Finding the number of obstacles(trees) in the grid by following our slope.
def numTrees(grid, slopex, slopey):
    length = len(grid[0]) - 1
    curPosx, curPosy = 0, 0
    numTrees = 0

    try:
        while(True):
            curPosx += slopex; curPosy += slopey
            numTrees += grid[curPosx][curPosy % length] == "#"
    
    except IndexError:
        return numTrees

slopes = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
grid = sys.stdin.readlines()

print(math.prod(numTrees(grid, x[0], x[1]) for x in slopes))