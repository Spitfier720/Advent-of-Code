#Finding whether how much overlap there is between multiple rectangles.

overlapCoords = 0
fabric = [[0 for x in range(1000)] for y in range(1000)]
claim = input().split()

while(claim):
    starty, startx = map(int, claim[2].strip(":").split(","))
    leny, lenx = map(int, claim[3].split("x"))

    for x in range(lenx):
        for y in range(leny):
            overlapCoords += fabric[x + startx][y + starty] == 1
            fabric[x + startx][y + starty] += 1

    claim = input().split()

print(overlapCoords)