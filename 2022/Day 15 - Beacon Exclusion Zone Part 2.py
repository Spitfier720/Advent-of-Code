#Simulating a several signals' coverage until it hits a beacon.

#Find a square with a Manhattan distance of 2, which will resemble our hole, given a starting point, if it exists.
def getHole(intersections, curPoint, coords):
    #This coordinate modifers are the only possible ways to get the hole we want.
    for d in [(-1, 1), (1, 1), (1, -1), (-1, -1)]:
        newPoint = (curPoint[0] + d[0], curPoint[1] + d[1])

        #We have found a potential square.
        if(len(coords) == 4):
            return coords

        #If our new point exists as an intersection point and is not already part of our square, add it and continue the search.
        if(newPoint in intersections and newPoint not in coords):
            coords.append(newPoint)
            coords = getHole(intersections, newPoint, coords)
            
            #We need to make sure these four coordinates make a closed square and not four random lines.
            if(len(coords) == 4 and abs(coords[3][0] - coords[0][0]) == abs(coords[3][1] - coords[0][1]) == 1):
                return coords
            
            #Pop the newPoint as it clearly does not lead us to a goal.
            coords.pop()

    #Return the coordinates as is, since we have not found a proper square with this path.
    return coords           

line = input().split()
sensors = {}

while(line):
    #Getting the coordinates of the sensor and its closest beacon.
    #The y-coordinates are negative to get the correct line equation.
    sensor = (int(line[2].split("=")[1].strip(",")), -int(line[3].split("=")[1].strip(":")))
    beacon = (int(line[8].split("=")[1].strip(",")), -int(line[9].split("=")[1].strip(":")))

    distance = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])

    #Entering the lines of the square it covers, as well as its domains and ranges.
    sensors[sensor] = [
        (-1, sensor[1] - -1 * (sensor[0] + distance), sensor[0], sensor[0] + distance, sensor[1] + distance, sensor[1]), #Top to right point.
        (1, sensor[1] - (sensor[0] + distance), sensor[0], sensor[0] + distance, sensor[1], sensor[1] - distance),       #Right to bottom point.
        (-1, sensor[1] - -1 * (sensor[0] - distance), sensor[0] - distance, sensor[0], sensor[1], sensor[1] - distance), #Bottom to left point.
        (1, sensor[1] - (sensor[0] - distance), sensor[0] - distance, sensor[0], sensor[1] + distance, sensor[1])        #Left to top point.
        ]
    
    line = input().split()

intersections = set()

#The dimensions we want our grid to be.
row = 4000000

#Finding all the intersection points between sensors.
for s in sensors:
    for line1 in sensors[s]:
        for t in sensors:
            #We want to find the intersections between different sensors.
            if(t == s):
                continue
            
            for line2 in sensors[t]:
                #If the lines have the same slope, there will be no intersections, since overlapping lines are not important.
                if(line1[0] == line2[0]):
                    continue

                intersectionX = (line2[1] - line1[1]) / (line1[0] - line2[0])
                
                #If the intersection x coordinate is not at an integer, it will not be a valid intersection point.
                if(intersectionX % 1 != 0):
                    continue

                intersectionY = line1[0] * intersectionX + line1[1]

                #Checking if the intersection point is within range and is a new point.
                if(max(0, line1[2], line2[2]) <= intersectionX <= min(row, line1[3], line2[3]) and \
                    min(0, line1[4], line2[4]) >= intersectionY >= max(-row, line1[5], line2[5])):
                    intersections.add((int(intersectionX), int(intersectionY)))

holeCandidates = set()

for i in intersections:
    holeBorders = getHole(intersections, i, [i])

    #If we have found the hole, get the middle point, which can be found by averaging the x and y coordinates.
    #Since getHole() will return the inital coordinate if the hole is not found, we need to account for the number of coordinates.
    if(len(holeBorders) == 4):
        #Since there may be multiple "holes", we need to filter this further.
        holeCandidates.add((sum(list(x[0] for x in holeBorders)) // 4, sum(list(x[1] for x in holeBorders)) // 4))

#Finding if the "hole" is full or not.
for h in holeCandidates:
    isFull = False

    #For each square the sensor covers, find the total areas of the triangle with two consecuitive points.
    #If the total area is larger than that of the square itself, then it is not in the square.
    for s in sensors:
        coords = [
            (sensors[s][0][2], sensors[s][0][4]), #Top point.
            (sensors[s][1][3], sensors[s][1][4]), #Right point.
            (sensors[s][2][3], sensors[s][2][5]), #Bottom point.
            (sensors[s][3][2], sensors[s][3][5])  #Left point.
        ]

        dimension = sensors[s][0][3] - sensors[s][0][2]
        totalArea = 0

        #Taking two coords at once to create our triangle.
        for c in range(4):
            #Sorting the triangle coordinates by y value to get the lowest point, which will help us determine our area.
            triangle = sorted([h, coords[c], coords[(c + 1) % 4]], key = lambda x: x[1])

            #Creating trapezoids from two of the triangle points to the x-axis.
            #We need a positive area, so we make the sums of the parallel sides negative.
            trap1 = -(triangle[0][1] + triangle[1][1]) * abs(triangle[0][0] - triangle[1][0]) / 2
            trap2 = -(triangle[0][1] + triangle[2][1]) * abs(triangle[0][0] - triangle[2][0]) / 2
            trap3 = -(triangle[1][1] + triangle[2][1]) * abs(triangle[1][0] - triangle[2][0]) / 2

            #Since one trapezoid covers the area from the bottom of the triangle to the x-axis, subtract it from the other two.
            totalArea += trap1 + trap2 - trap3

        #The side length of our 45 degree square is sqrt(2) * the distance from sensor to beacon.
        #Luckily, the side length squared is a much cleaner number.
        if(totalArea <= 2 * dimension ** 2):
            isFull = True
            break
    
    #We have found the empty hole.
    if(not isFull):
        #Subtracting the y-coordinate since we made it negative.
        print(h[0] * 4000000 - h[1])
    