#Finding the number of "heights" that would be visible when looking from all cardinal directions.

line = input()
heights = []

#Holding the width and height so we don't have to call len multiple times, which would affect performance.
width, height = len(line), 0

#Simple parsing of input, the core of solving the problem is done later.
while(line):
    height += 1
    row = []
    
    for char in line:
        row.append(int(char))

    heights.append(row)
    line = input()

maxScore = 0

#Skip the edges; since at least one side will have no visible trees, the total score will be 0.
for x in range(1, height - 1):
    for y in range(1, width - 1):
        curScore = 1
        directions = {
            (x - 1, y): 0,
            (x, y + 1): 0, 
            (x + 1, y): 0, 
            (x, y - 1): 0
            }

        #We keep going through this loop, removing no longer valid directions, and breaking out when the loop is empty.
        while(directions):
            #Making a copy of the directions to save for later.
            newDirs = dict(directions)
            toRemove = set()

            for d in directions:
                #Coordinates are out of range, the direction is now invalid.
                if(not (0 <= d[0] <= height - 1) or not(0 <= d[1] <= width - 1)):
                    toRemove.add(d)

                else:
                    #Whether or not the tree is bigger than the one we are currently on, it is still visible.
                    newDirs[d] += 1

                    #The direction is invalid if the tree is at least the same size as our current tree.
                    if(heights[d[0]][d[1]] >= heights[x][y]):
                        toRemove.add(d)
            
            #Delete the invalid directions.
            for d in toRemove:
                curScore *= newDirs[d]
                newDirs.pop(d)
            
            #Resetting the original directions to make the updated ones.
            directions = dict()

            #Updating the remaining directions using the most primitive way imaginable, because I can't see another way and it's 2am.
            for d in newDirs:
                #The direction is up or down.
                if(x != d[0]):
                    if(x > d[0]): #Up
                        directions[(x - (newDirs[d] + 1), y)] = newDirs[d]
                    
                    else: #Down
                        directions[(x + (newDirs[d] + 1), y)] = newDirs[d]
                
                #The direction is left or right.
                else:
                    if(y > d[1]): #Left
                        directions[(x, y - (newDirs[d] + 1))] = newDirs[d]
                    
                    else: #Right
                        directions[(x, y + (newDirs[d] + 1))] = newDirs[d]
        
        maxScore = max(maxScore, curScore)

print(maxScore)