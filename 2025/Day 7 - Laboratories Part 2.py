import os

class Day7:
    def __init__(self):
        self.__beamPos = {}
    
    def numTimelines(self):
        return sum(self.__beamPos.values())
    
    def parseRow(self, row):
        for i in range(len(row)):
            if(row[i] == 'S'):
                self.__beamPos = {i: 1}
            
            elif(row[i] == '^'):
                if(i in self.__beamPos):
                    self.__beamPos[i - 1] = self.__beamPos.get(i - 1, 0) + self.__beamPos[i]
                    self.__beamPos[i + 1] = self.__beamPos.get(i + 1, 0) + self.__beamPos[i]
                    del self.__beamPos[i]


scriptDir = os.path.dirname(__file__)
filePath = os.path.join(scriptDir, f"Day 7 Inputs.txt")
with open(filePath, "r") as f:
    lines = f.readlines()

day7 = Day7()
i = 1

for line in lines:
    if(line.strip() == "---"): # End of input, reset program
        print(f"Iteration {i}'s fresh ingredient ranges: {day7.numTimelines()}")
        
        day7 = Day7()
        i += 1

    else:
        day7.parseRow(line)