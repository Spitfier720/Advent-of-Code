#Following directions by turning and moving.

directions = input().split(", ")
coords = [0, 0]
rotation = 0

#Translating rotation angle to the coordinate change.
cardinals = {
    0: (1, 0),
    90: (0, 1),
    180: (-1, 0),
    270: (0, -1)
}
visited = set()
isFound = False

for d in directions:
    if(d[0] == "L"):
        rotation -= 90
    
    else:
        rotation += 90

    #Updating the coordinates for each step so that we can store each coordinate visited.
    for y in range(int(d[1:])):
        coords[0] += cardinals[abs(rotation % 360)][0]
        coords[1] += cardinals[abs(rotation % 360)][1]
        
        if(tuple(coords) in visited):
            #Manhattan distance is just the absolute x value plus the absolute y value.
            print(abs(coords[0]) + abs(coords[1]))
            isFound = True
            break
        
        visited.add(tuple(coords))
    
    #Break out of the loop if a location has been visited twice so that we don't print more than one number.
    if(isFound):
        break