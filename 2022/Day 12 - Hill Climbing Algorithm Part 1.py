#As the title suggests, a pathfinding algorithm to get from start to end as fast as possible.

#A function to find the path from start to end in the least amount of steps, using BFS.
def hca(grid, start, end, width, height):
    #Starting off with our queue and visited which will hold the spot we are starting from.
    queue, visited = [(0, start)], {start}

    while(queue):
        steps, coord = queue.pop(0)

        #Found the end.
        if(coord == end):
            return steps
        
        #Iterating through the cardinal directions to get possible candidates.
        for x in [(1, 0), (-1, 0), (0, 1), (0, -1)]:

            #If the coordinate is within range, not visited before, and is at most 1 "elevation" higher.
            #I've decided to map the elevations to the ASCII values.
            if(0 <= coord[0] + x[0] <= height - 1 and 0 <= coord[1] + x[1] <= width - 1 and \
                (coord[0] + x[0], coord[1] + x[1]) not in visited and \
                ord(grid[coord[0] + x[0]][coord[1] + x[1]]) - ord(grid[coord[0]][coord[1]]) <= 1):
                #Update queue and visited.
                visited.add((coord[0] + x[0], coord[1] + x[1]))
                queue.append((steps + 1, (coord[0] + x[0], coord[1] + x[1])))
    
    #Meant as an error code, this line should not be reached.
    return -1

line = input()
start, end = (), ()
grid = []

#Get width and height for performance purposes.
width, height = len(line), 0

while(line):
    row = []

    for x in range(width):
        #Replacing the start with a character that's one under "a", even though it could have just been "a".
        if(line[x] == "S"):
            start = (height, x)
            row.append(chr(ord("a") - 1))

        #Replacing the end with a character that's one over "z", as we assume that's the highest spot.
        if(line[x] == "E"):
            end = (height, x)
            row.append(chr(ord("z") + 1))
        
        #Adding the other characters to the grid as is.
        if(line[x] not in "SE"):
            row.append(line[x])
    
    grid.append(row)
    
    height += 1
    line = input()

print(hca(grid, start, end, width, height))