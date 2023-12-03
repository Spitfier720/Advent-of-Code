import sys

symbolCoords = []
grid = []
row = 0

for x in sys.stdin.readlines():
    x = x.strip()
    grid.append(x)

    for i in range(len(x)):
        if(x[i] != "." and not x[i].isdigit()):
            symbolCoords.append([row, i])
    
    row += 1

directions = [[0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [-1, -1], [1, -1], [-1, 1]]
visited = set()
sum = 0

#Finds the numbers in the grid that are adjacent to the symbols via the directions list and adds them to the sum
for sym in symbolCoords:
    for dir in directions:
        newX = sym[0] + dir[0]
        newY = sym[1] + dir[1]

        if(0 <= newX <= len(grid) - 1 and 0 <= newY <= len(grid[0]) - 1): #Bound checking
            if(grid[newX][newY].isdigit() and (newX, newY) not in visited): #Check if we found a new part number
                partNumber = grid[newX][newY] #Start the part number with the first digit and add on to it later
                visited.add((newX, newY))

                moreDigitsLeft = True
                moreDigitsRight = True

                for x in range(1, min(newY, len(grid) - 1 - newY) + 1): #Loop until the first edge of the grid found
                    if(grid[newX][newY - x].isdigit() and moreDigitsLeft): #Check if there is a digit to the left
                        partNumber = grid[newX][newY - x] + partNumber
                        visited.add((newX, newY - x))
                    else:
                        moreDigitsLeft = False
                    
                    if(grid[newX][newY + x].isdigit() and moreDigitsRight): #Check if there is a digit to the right
                        partNumber += grid[newX][newY + x]
                        visited.add((newX, newY + x))
                    else:
                        moreDigitsRight = False
            
                sum += int(partNumber)

print(sum)