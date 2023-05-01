#Simulating an assembly line with conditional branching.

#Adds the bot the the chip and handles the processes that the bot may do, and recursively handle other processes for affected bots.
def addChip(robots, value, botId):
    if(botId < 0):
        robots[botId] = value
        return

    if(robots[botId][0] == 0):
        robots[botId][0] = value
    
    else:
        robots[botId][1] = value

        addChip(robots, min(robots[botId][0], robots[botId][1]), robots[botId][2])
        addChip(robots, max(robots[botId][0], robots[botId][1]), robots[botId][3])

robots = {}
instruction = input()
chipsToAdd = []

#Setting up the robots.
while(instruction):
    instruction = instruction.split()

    if(instruction[0] == "value"):
        chipsToAdd.append([int(instruction[1]), int(instruction[5])]) #value, bot id
    
    else:
        botId = int(instruction[1])
        lowerDest, higherDest = int(instruction[6]), int(instruction[11])
        
        if(robots.get(botId) == None):
            robots[botId] = [0, 0, 0, 0] #first chip, second chip, lower value destination, higher value destination 
        
        robots[botId][2] = lowerDest if instruction[5] != "output" else -lowerDest - 1
        robots[botId][3] = higherDest if instruction[10] != "output" else -higherDest - 1

        if(robots[botId][2] < 0):
            robots[robots[botId][2]] = 0
        
        if(robots[botId][3] < 0):
            robots[robots[botId][3]] = 0

    instruction = input()

for x in chipsToAdd:
    addChip(robots, x[0], x[1])

print(robots[-1] * robots[-2] * robots[-3])