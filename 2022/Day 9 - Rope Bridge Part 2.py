#Simulating a bit of physics to determine where the end of a rope will go.

#Keeping coordinates of all 10 knots.
coordinates = [[0, 0] for x in range(10)]

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
        coordinates[i][0] += directions[line[0]][0]
        coordinates[i][1] += directions[line[0]][1]

        #Iterating through all the knots, since some of them might need to be moved.
        for i in range(9):
            #This checks if the next knot is a Manhattan distance of 4 away, or 2 x and y units away.
            #This has to be checked in this program, since a knot can take two diagonal moves in the same direction.
            #The previous program could not do that, since the number of knots were too small.
            if(abs(coordinates[i][0] - coordinates[i + 1][0]) + abs(coordinates[i][1] - coordinates[i + 1][1]) == 4):
                #Making a generic way to update the coordinates by getting the average of the x and y coordinates.
                coordinates[i + 1][0] = (coordinates[i][0] + coordinates[i + 1][0]) // 2
                coordinates[i + 1][1] = (coordinates[i][1] + coordinates[i + 1][1]) // 2
            
            #Otherwise, the next knot moves as long as the current knot is at least 2 units away, either from x or y coordinates.
            elif(coordinates[i][0] - coordinates[i + 1][0] == 2): #Head is 2 units right.
                #The y-coordinate of the next knot is updated, just in case the current knot's y-coordinate is different from the next knot's.
                #This means that the next knot made a diagonal move.
                coordinates[i + 1][0], coordinates[i + 1][1] = coordinates[i][0] - 1, coordinates[i][1]
            
            elif(coordinates[i][0] - coordinates[i + 1][0] == -2): #Head is 2 units left.
                coordinates[i + 1][0], coordinates[i + 1][1] = coordinates[i][0] + 1, coordinates[i][1]

            elif(coordinates[i][1] - coordinates[i + 1][1] == 2): #Head is 2 units up.
                coordinates[i + 1][0], coordinates[i + 1][1] = coordinates[i][0], coordinates[i][1] - 1
            
            elif(coordinates[i][1] - coordinates[i + 1][1] == -2): #Head is 2 units down.
                coordinates[i + 1][0], coordinates[i + 1][1] = coordinates[i][0], coordinates[i][1] + 1
        
        #Adding the last knot, which is basically our tail.
        visited.add((coordinates[9][0], coordinates[9][1]))

    line = input().split()

print(len(visited))