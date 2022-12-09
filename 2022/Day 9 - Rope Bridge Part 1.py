#Simulating a bit of physics to determine where the end of a rope will go.

#Keeping coordinates of the head and tail.
hx, hy, tx, ty = 0, 0, 0, 0

#Keeping track of directions so that we don't have to make four if statements.
directions = {
    "U": (0, 1),
    "R": (1, 0),
    "D": (0, -1),
    "L": (-1, 0)
}

#This is where we will store all our coordinates, and which will ultimately get us the answer.
visited = {(0, 0)}

line = input().split()

while(line):
    #Iterating through the number of moves our head will take since the tail might move for some of them, which we need to track.
    for x in range(int(line[1])):
        hx += directions[line[0]][0]
        hy += directions[line[0]][1]

        #The tail moves as long as the head is at least 2 units away, either from x or y coordinates.
        if(hx - tx == 2): #Head is 2 units right.
            #The y-coordinate of the tail is updated, just in case the head's y-coordinate is different from the tail's.
            #This means that the tail made a diagonal move.
            tx, ty = hx - 1, hy
        
        elif(hx - tx == -2): #Head is 2 units left.
            tx, ty = hx + 1, hy
        
        elif(hy - ty == 2): #Head is 2 units up.
            tx, ty = hx, hy - 1
        
        elif(hy - ty == -2): #Head is 2 units down.
            tx, ty = hx, hy + 1
        
        visited.add((tx, ty))

    line = input().split()

print(len(visited))