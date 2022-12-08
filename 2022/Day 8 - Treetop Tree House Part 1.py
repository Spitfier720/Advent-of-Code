#Finding the number of "heights" that would be visible when looking from all cardinal directions.

line = input()
heights = []

#Holding the width and height so we don't have to call len multiple times, which would affect performance.
width, height = len(line), 0

#Holding the coordinates of the trees that are visible.
visible = set()

#The maximum height starts off at -1 since trees can be at 0 height.
maxHeight = -1

while(line):
    height += 1

    #Doing this prevents previous loops from affecting our current check.
    maxHeight = -1
    row = []

    #Check the visible trees from left to right(and adding them to our row to be appended in the array while we're at it).
    for x in range(width):
        if(int(line[x]) > maxHeight):
            visible.add((height - 1, x))
            maxHeight = int(line[x])

        row.append(int(line[x]))
    
    maxHeight = -1

    #Checking visible trees from right to left.
    for x in range(width - 1, 0, -1):
        if(int(line[x]) > maxHeight):
            visible.add((height - 1, x))
            maxHeight = int(line[x])
    
    heights.append(row)
    line = input()

#Checking visible trees from up to down, for every column.
for x in range(width):
    maxHeight = -1

    for y in range(height):
        if(heights[y][x] > maxHeight):
            visible.add((y, x))
            maxHeight = heights[y][x]

#Checking visible trees from down to up, and as a side note, I wish there was an easier way than making four loops.
for x in range(width):
    maxHeight = -1

    for y in range(height - 1, 0, -1):
        if(heights[y][x] > maxHeight):
            visible.add((y, x))
            maxHeight = heights[y][x]

print(len(visible))