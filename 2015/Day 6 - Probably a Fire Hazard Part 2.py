#Configuring a million lights through instructions.
import sys

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

    if(instruction[0] == "turn"):
        xStart, yStart = map(int, instruction[2].split(","))

        if(instruction[1] == "on"):
            brightness = 1

        else:
            brightness = -1
    
    else:
        xStart, yStart = map(int, instruction[1].split(","))
        brightness = 2
    
    for y in range(yStart, yEnd + 1):
        for x in range(xStart, xEnd + 1):

            #Make sure the brightness is not negative
            lightGrid[x][y] = max(lightGrid[x][y] + brightness, 0)

print(sum([light for row in lightGrid for light in row]))