#Find out the optimal seating such that the maximum happiness is reached.

#Recursively finds the maximum possible happiness from all possible seating permutations.
def getMaxHappiness(happySeatings, visited, maxHappiness, curHappiness, firstPerson, curPerson):
    #Checking beforehand if we have reached the last person standing.
    if(len(visited) + 1 == len(happySeatings)):
        #The happiness units between the first and the last seated person also need to be calculated
        curHappiness += happySeatings[curPerson][firstPerson] + happySeatings[firstPerson][curPerson]
        maxHappiness = max(maxHappiness, curHappiness)
        
        #We have created a seating arrangement, calculations are skipped.
        return maxHappiness
    
    visited.append(curPerson)
    
    for otherPerson in happySeatings[curPerson]:
        #Neither person has been seated
        if(otherPerson not in visited):
            #Both people's happiness values from sitting beside each other have to be calculated.
            curHappiness += happySeatings[curPerson][otherPerson] + happySeatings[otherPerson][curPerson]

            #Keep a reference to the first person seated, since they will be sitting beside the last person seated.
            firstPerson = curPerson if not firstPerson else firstPerson

            #This ensures that maxHappiness will retain its most recent value as it goes through recursive calls.
            maxHappiness = getMaxHappiness(happySeatings, visited, maxHappiness, curHappiness, firstPerson, otherPerson)
            
            #Taking out the happiness values to keep accurate calculations.
            curHappiness -= happySeatings[curPerson][otherPerson] + happySeatings[otherPerson][curPerson]
    
    #We have looked through all curPerson possibilities and remove them from the seating arrangement and current count.
    lastPerson = visited.pop()

    # Since we have removed everyone from the seating arrangement, there is no first person sitting.
    if(not visited):
        firstPerson = ""
        curHappiness = 0
    
    else:
        curHappiness -= happySeatings[visited[-1]][lastPerson] + happySeatings[lastPerson][visited[-1]]

    return maxHappiness

line = input().split()
happySeatings = {}

#The input is given in sentences, so we need to break them down into only relevant data.
while(line):
    happySeatings.setdefault(line[0], {})
    happySeatings[line[0]][line[10].strip(".")] = int(line[3]) * -1 if line[2] == "lose" else int(line[3])

    line = input().split()

#The first person we start with is arbitrary, since the table is circular and the seating arrangements will all be the same.
print(getMaxHappiness(happySeatings, [], -float('inf'), 0, "", list(happySeatings.keys())[0]))