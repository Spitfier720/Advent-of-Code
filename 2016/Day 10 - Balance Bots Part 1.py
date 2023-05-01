#Simulating an assembly line with conditional branching.

#Adds the bot the the chip and handles the processes that the bot may do, and recursively handle other processes for affected bots.
#Tries to return the bot that deals with value-61 and value-17 chips.
def addChip(robots, value, botId):
    if(botId == -1):
        return

    if(robots[botId][0] == 0):
        robots[botId][0] = value
    
    else:
        robots[botId][1] = value

        if(61 in robots[botId][0:2] and 17 in robots[botId][0:2]): #We found the bot
            return botId

        #Checking if the bot was found recursively.
        botInQuestion = addChip(robots, min(robots[botId][0], robots[botId][1]), robots[botId][2])

        if(botInQuestion != None):
            return botInQuestion

        botInQuestion = addChip(robots, max(robots[botId][0], robots[botId][1]), robots[botId][3])

        if(botInQuestion != None):
            return botInQuestion

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
        lowerDest, higherDest = -1, -1

        #Currently, we're assuming that putting chips in the output bins means that it no longer matters.
        if(instruction[5] != "output"):
            lowerDest = int(instruction[6])
        
        if(instruction[10] != "output"):
            higherDest = int(instruction[11])
        
        if(robots.get(botId) == None):
            robots[botId] = [0, 0, 0, 0] #first chip, second chip, lower value destination, higher value destination 
        
        robots[botId][2] = lowerDest
        robots[botId][3] = higherDest

    instruction = input()

for x in chipsToAdd:
    botInQuestion = addChip(robots, x[0], x[1])

    #The bot may not be found just by adding the first chip, so I'm trying not to print a bunch of Nones.
    if(botInQuestion != None):
        print(botInQuestion)
        break