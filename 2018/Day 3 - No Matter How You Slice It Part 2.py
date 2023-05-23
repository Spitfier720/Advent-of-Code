#Finding a rectangle that doesn't overlap with any other rectangle.

def isOverlap(rect1, rect2):
    if(rect1[2] <= rect2[0] or rect2[2] <= rect1[0]): #If one rectangle is completely to the left of another
        return False
    
    if(rect1[3] <= rect2[1] or rect2[3] <= rect1[1]): #If one rectangle is completely above another
        return False
    
    return True

overlapCoords = 0
rectangles = {}
claim = input().split()
curNonOverlap = set() #Stores the current rectangles that are not overlapping.

while(claim):
    id = int(claim[0].strip("#"))
    starty, startx = map(int, claim[2].strip(":").split(","))
    leny, lenx = map(int, claim[3].split("x"))
    endy, endx = starty + leny, startx + lenx
    curNonOverlap.add(id)

    for x in rectangles:
        if(isOverlap(rectangles[x], [starty, startx, endy, endx])):
            curNonOverlap.discard(x)
            curNonOverlap.discard(id)

    rectangles[id] = [starty, startx, endy, endx]
    claim = input().split()

print(list(curNonOverlap)[0])