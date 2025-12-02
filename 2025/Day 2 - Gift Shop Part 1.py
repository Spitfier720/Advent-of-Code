import os

class Day2:
    def __init__(self):
        self.__total = 0

    @property
    def total(self): 
        return self.__total

    def findInvalidIDs(self, minID, maxID):
        minIDlen = len(str(minID))
        maxIDlen = len(str(maxID))

        for x in range(minIDlen, maxIDlen + 1):
            if(x % 2 != 0): continue # Odd number of digits means the ID must be valid, ignore all IDs in this range

            midpoint = x // 2
            startHalf = int(max(minID // (10 ** (midpoint)), 10 ** (midpoint - 1)))
            endHalf = int(min(maxID // (10 ** (midpoint)), 10 ** midpoint - 1))

            for half in range(startHalf, endHalf + 1):
                invalidId = half * (10 ** midpoint) + half

                if(minID <= invalidId <= maxID): #invalid ID
                    self.__total += invalidId
                
                elif(invalidId > maxID): break #Already went out of range, stop checking

        # Brute Force Approach
        # for id in range(minID, maxID + 1): 
        #     strId = str(id)
        #     length = len(strId)
            
        #     if(length % 2 == 0): # ID has even number of digits, could be invalid
        #         midpoint = length // 2
                
        #         if(strId[:midpoint] == strId[midpoint:]): #invalid ID
        #             self.__total += id

scriptDir = os.path.dirname(__file__)
filePath = os.path.join(scriptDir, f"Day 2 Inputs.txt")
with open(filePath, "r") as f:
    lines = f.readlines()

day2 = Day2()
i = 1

for line in lines:
    if(line == "\n" or not line): # Empty line, reset program
        print(f"Iteration {i}'s sum: {day2.total}")
        
        day2 = Day2()
        i += 1

    else:
        for idRange in line.strip().split(","):
            first, last = map(int, idRange.split("-"))
            day2.findInvalidIDs(first, last)