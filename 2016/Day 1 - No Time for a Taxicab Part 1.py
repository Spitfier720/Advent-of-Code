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

for d in directions:
    if(d[0] == "L"):
        rotation -= 90
    
    else:
        rotation += 90
    
    #Changing the coordinates for each direction by finding the appropriate direction and multiplying it by the steps taken.
    for x in range(2):
        coords[x] += cardinals[abs(rotation % 360)][x] * int(d[1:])

#Manhattan distance is just the absolute x value plus the absolute y value.
print(abs(coords[0]) + abs(coords[1]))