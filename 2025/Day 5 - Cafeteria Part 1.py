import os

class Day5:
    def __init__(self):
        self.__numFresh = 0
        self.__freshRanges = set()
    
    @property
    def numFresh(self):
        return self.__numFresh
    
    def addRange(self, range):
        minID, maxID = map(int, range.strip().split("-"))
        self.__freshRanges.add((minID, maxID))
    
    def isFresh(self, id):
        for minID, maxID in self.__freshRanges:
            if(minID <= id <= maxID):
                self.__numFresh += 1
                return

scriptDir = os.path.dirname(__file__)
filePath = os.path.join(scriptDir, f"Day 5 Inputs.txt")
with open(filePath, "r") as f:
    lines = f.readlines()

day5 = Day5()
i = 1
processingRanges = True

for line in lines:
    if(line.strip() == "---"): # End of input, reset program
        print(f"Iteration {i}'s fresh ingredients: {day5.numFresh}")
        
        day5 = Day5()
        i += 1
        processingRanges = True

    elif(line == "\n" or not line):
        processingRanges = False

    else:
        if(processingRanges):
            day5.addRange(line)
        else:
            day5.isFresh(int(line.strip()))