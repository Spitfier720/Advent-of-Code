#Simulating gravity with platforms to break its fall.

#Getting the number of sand that can be safely put.
def totalSand(rocks, lowest):
    numSand = 0
    full = False

    #Keep giving sand until full.
    while(not full):
        source = (500, 0)

        #The sand may have filled up until the source hole.
        if(source in rocks):
            return numSand

        moved = True

        #Keep moving a unit of sand until it can't anymore.
        while(moved):
            moved = False

            #Checking all possible movements in that order due to priority.
            for x in [(0, 1), (-1, 1), (1, 1)]:
                #We have gone outside the grid, it is full.
                if(source[1] + x[1] > lowest):
                    return numSand

                if((source[0] + x[0], source[1] + x[1]) not in rocks):
                    source = (source[0] + x[0], source[1] + x[1])
                    moved = True
                    #We need to start from the possible directions from the start.
                    break
        
        #Add the sand to the blocking platforms, since other units of sand have to go around it.
        rocks.add(source)
        numSand += 1
    
    #If the sand fills the whole grid with none of it falling out.
    return numSand

line = input().split(" -> ")
rocks = set()

#Getting the lowest point of the rocks as a stopper for if the sand falls too far.
lowest = 0

while(line != [""]):
    for i in range(len(line) - 1):
        x1, y1 = list(map(int, line[i].split(",")))
        x2, y2 = list(map(int, line[i + 1].split(",")))

        lowest = max(lowest, max(y1, y2))

        #Finding out the type of line it is and its length.
        if(x2 != x1):
            dist = abs(x2 - x1)
            lineType = "H"
        
        else:
            dist = abs(y2 - y1)
            lineType = "V"

        #Creating the line between two points.
        for x in range(dist + 1):
            if(lineType == "H"):
                rocks.add((min(x1, x2) + x, y1))
            
            else:
                rocks.add((x1, min(y1, y2) + x))
        
    line = input().split(" -> ")

print(totalSand(rocks, lowest))