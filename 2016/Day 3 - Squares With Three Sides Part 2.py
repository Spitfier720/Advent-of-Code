#Finding valid triangles through side length.

numValid = 0

line = list(map(int, input().split()))

while(line):
    line2 = list(map(int, input().split()))
    line3 = list(map(int, input().split()))

    #Keeping three triangles at a time since we are looking at the columns instead, and there are three at once.
    sides = []

    #Getting the side lengths through splitting by spaces.
    for x in range(3):
        #We basically "rotate" our input to turn our columns into more managebale rows.
        sides.append(list(map(int, list(i[x] for i in [line, line2, line3]))))

        #We will only have at most 3 elements, so this function takes a negligible time.
        sides[x].sort(reverse = True)

    for x in range(3):
        if(sides[x][0] < sides[x][1] + sides[x][2]):
            numValid += 1
    
    line = list(map(int, input().split()))

print(numValid)