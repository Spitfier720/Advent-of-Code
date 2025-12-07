import os

class Day7:
    def __init__(self):
        self.__beamPos = set()
        self.__numSplits = 0

    @property
    def numSplits(self):
        return self.__numSplits
    
    def parseRow(self, row):
        for i in range(len(row)):
            if(row[i] == 'S'):
                self.__beamPos = {i}
            
            elif(row[i] == '^'):
                if(i in self.__beamPos):
                    self.__beamPos.remove(i)
                    self.__beamPos.add(i - 1)
                    self.__beamPos.add(i + 1)
                    self.__numSplits += 1


scriptDir = os.path.dirname(__file__)
filePath = os.path.join(scriptDir, f"Day 7 Inputs.txt")
with open(filePath, "r") as f:
    lines = f.readlines()

day7 = Day7()
i = 1

for line in lines:
    if(line.strip() == "---"): # End of input, reset program
        print(f"Iteration {i}'s fresh ingredient ranges: {day7.numSplits}")
        
        day7 = Day7()
        i += 1

    else:
        day7.parseRow(line)