#Configuring a million lights through instructions.

lineOfInput = input()
instructions = []

#Account for multi-line input, will try to find a shorter way
while(lineOfInput):
    instructions.append(lineOfInput)
    lineOfInput = input()

#Simulation, because as slow as it is, there is no other solution I could think of
lightGrid = [[0 for x in range(1000)] for y in range(1000)]

for instruction in instructions:

    #Break up the instructions and get the useful information out
    instruction = instruction.split()
    xEnd, yEnd = map(int, instruction[-1].split(","))

    #This variable determines the state that the light wil be changed into
    change = -1

    if(instruction[0] == "turn"):
        xStart, yStart = map(int, instruction[2].split(","))

        if(instruction[1] == "on"):
            change = 1

        else:
            change = 0
    
    else:
        xStart, yStart = map(int, instruction[1].split(","))
    
    for y in range(yStart, yEnd + 1):
        for x in range(xStart, xEnd + 1):
            if(change >= 0):
                lightGrid[x][y] = change
            
            #Toggle light to its opposite state
            else:
                lightGrid[x][y] *= -1
                lightGrid[x][y] += 1

print(sum([light for row in lightGrid for light in row]))