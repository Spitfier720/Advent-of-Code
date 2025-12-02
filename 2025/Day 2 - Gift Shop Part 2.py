import os

class Day2:
    def __init__(self):
        self.__total = 0

    @property
    def total(self): 
        return self.__total

    def findInvalidIDs(self, minID, maxID):
        invalidIds = set()
        minIDlen = len(str(minID))
        maxIDlen = len(str(maxID))

        for totalDigits in range(minIDlen, maxIDlen + 1):
            for patternLength in range(1, totalDigits // 2 + 1):
                if(totalDigits % patternLength != 0): continue #Not an invalid ID

                startPattern = int(max(minID // (10 ** (totalDigits - patternLength)), 10 ** (patternLength - 1)))
                endPattern = int(min(maxID // (10 ** (totalDigits - patternLength)), 10 ** patternLength - 1))

                for pattern in range(startPattern, endPattern + 1):
                    invalidId = 0

                    for _ in range(totalDigits // patternLength):
                        invalidId = invalidId * (10 ** patternLength) + pattern
                    
                    if(minID <= invalidId <= maxID and invalidId not in invalidIds): #invalid ID
                        self.__total += invalidId
                        invalidIds.add(invalidId)
                    
                    elif(invalidId > maxID): break #Already went out of range, stop checking
        
        # for id in range(minID, maxID + 1): 
        #     strId = str(id)
        #     length = len(strId)

        #     for x in range(1, length // 2 + 1): 
        #         if(length % x == 0): # Possibly an invalid ID
        #             if((strId[:x] * (length // x)) == strId): #invalid ID
        #                 self.__total += id
        #                 break # Do not add the invalid IDs more than once
                

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