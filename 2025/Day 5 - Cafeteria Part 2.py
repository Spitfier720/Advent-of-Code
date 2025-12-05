import os

class Day5:
    def __init__(self):
        self.__freshRanges = []
    
    def addRange(self, range):
        minID, maxID = map(int, range.strip().split("-"))
        self.__freshRanges.append((minID, maxID))
    
    def numFreshRanges(self):
        self.__freshRanges.sort(key = lambda x: x[0]) # Sort by start of range
        total = 0
        highestEnd = -1

        for i in range(len(self.__freshRanges)):
            minID, maxID = self.__freshRanges[i]

            if(i > 0):
                if(maxID <= highestEnd):
                    continue # Current range is fully contained within previous range, no change
                
                total -= max(highestEnd - minID + 1, 0) # Account for range overlap
            
            total += (maxID - minID + 1) # Inclusive range
            highestEnd = max(highestEnd, maxID)
        
        return total

scriptDir = os.path.dirname(__file__)
filePath = os.path.join(scriptDir, f"Day 5 Inputs.txt")
with open(filePath, "r") as f:
    lines = f.readlines()

day5 = Day5()
i = 1
processingRanges = True

for line in lines:
    if(line.strip() == "---"): # End of input, reset program
        print(f"Iteration {i}'s fresh ingredient ranges: {day5.numFreshRanges()}")
        
        day5 = Day5()
        i += 1
        processingRanges = True

    elif(line == "\n" or not line):
        processingRanges = False

    else:
        if(processingRanges):
            day5.addRange(line)