#Find out the optimal seating such that the maximum happiness is reached.

#Recursively finds the maximum possible happiness from all possible seating permutations.
def getMaxHappiness(happySeatings, arrangement, bestArrangement, maxHappiness, curHappiness, firstPerson, curPerson):
    #Checking beforehand if we have reached the last person standing.
    if(len(arrangement) + 1 == len(happySeatings)):
        #The happiness units between the first and the last seated person also need to be calculated
        curHappiness += happySeatings[curPerson][firstPerson] + happySeatings[firstPerson][curPerson]
        
        if(curHappiness > maxHappiness):
            maxHappiness = curHappiness
            bestArrangement = arrangement + [curPerson]
        
        #We have created a seating arrangement, calculations are skipped.
        return (maxHappiness, bestArrangement)
    
    arrangement.append(curPerson)
    
    for otherPerson in happySeatings[curPerson]:
        #Neither person has been seated
        if(otherPerson not in arrangement):
            #Both people's happiness values from sitting beside each other have to be calculated.
            curHappiness += happySeatings[curPerson][otherPerson] + happySeatings[otherPerson][curPerson]

            #Keep a reference to the first person seated, since they will be sitting beside the last person seated.
            firstPerson = curPerson if not firstPerson else firstPerson

            #This ensures that maxHappiness will retain its most recent value as it goes through recursive calls.
            maxHappiness, bestArrangement = getMaxHappiness(happySeatings, arrangement, bestArrangement, maxHappiness, \
                curHappiness, firstPerson, otherPerson)
            
            #Taking out the happiness values to keep accurate calculations.
            curHappiness -= happySeatings[curPerson][otherPerson] + happySeatings[otherPerson][curPerson]
    
    #We have looked through all curPerson possibilities and remove them from the seating arrangement and current count.
    lastPerson = arrangement.pop()

    # Since we have removed everyone from the seating arrangement, there is no first person sitting.
    if(not arrangement):
        firstPerson = ""
        curHappiness = 0
    
    else:
        curHappiness -= happySeatings[arrangement[-1]][lastPerson] + happySeatings[lastPerson][arrangement[-1]]

    #Not the cleanest way of returning the best seating arrangment, but it's pretty decent.
    return (maxHappiness, bestArrangement)

line = input().split()
happySeatings = {}

#The input is given in sentences, so we need to break them down into only relevant data.
while(line):
    happySeatings.setdefault(line[0], {})
    happySeatings[line[0]][line[10].strip(".")] = int(line[3]) * -1 if line[2] == "lose" else int(line[3])

    line = input().split()

#The first person we start with is arbitrary, since the table is circular and the seating arrangements will all be the same.
bestHappiness, bestArrangement = getMaxHappiness(happySeatings, [], [], -float('inf'), 0, "", list(happySeatings.keys())[0])

minHappyPair = float('inf')

#Finding the happiness units from each pair and finding the smallest one.
for x in range(len(bestArrangement)):
    minHappyPair = min(minHappyPair, happySeatings[bestArrangement[x]][bestArrangement[(x + 1) % len(bestArrangement)]] + \
        happySeatings[bestArrangement[(x + 1) % len(bestArrangement)]][bestArrangement[x]])

print(bestHappiness - minHappyPair)
