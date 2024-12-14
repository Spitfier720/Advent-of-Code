import os
import sys

def printGrid(robots, gridHeight, gridWidth):
    grid = [[" " for _ in range(gridWidth)] for _ in range(gridHeight)]

    for r in robots:
        grid[r[0]][r[1]] = "#"

    for row in grid:
        print("".join(row))

robots = []

gridHeight, gridWidth = 103, 101

for line in sys.stdin.readlines():
    line = line.strip().split()

    pos = tuple(map(int, line[0].split("=")[1].split(",")))[::-1]
    vel = tuple(map(int, line[1].split("=")[1].split(",")))[::-1]

    robots.append(pos + vel)

numSeconds = 0

os.system("cls")

printGrid(robots, gridHeight, gridWidth)
isTree = input("Is this a tree? (y/n): ")

while(isTree != "y"):
    os.system("cls")

    unqPos = set()
    isAllUnique = True

    for i in range(len(robots)):
        newX = (robots[i][0] + robots[i][2])

        if(newX < 0):
            newX += gridHeight
        
        if(newX >= gridHeight):
            newX -= gridHeight

        newY = (robots[i][1] + robots[i][3])

        if(newY < 0):
            newY += gridWidth
        
        if(newY >= gridWidth):
            newY -= gridWidth

        robots[i] = (newX, newY, robots[i][2], robots[i][3])

        if((newX, newY) in unqPos):
            isAllUnique = False

        unqPos.add((newX, newY))

    numSeconds += 1

    if(isAllUnique):
        printGrid(robots, gridHeight, gridWidth)
        print("Seconds:", numSeconds)
        isTree = input("Is this a tree? (y/n): ")

print(numSeconds)