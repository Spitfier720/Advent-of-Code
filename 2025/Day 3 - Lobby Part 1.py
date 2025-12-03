import os

class Day3:
    def __init__(self):
        self.__joltage = 0
    
    @property
    def joltage(self):
        return self.__joltage
    
    def findLargestJoltage(self, ratings):
        tensDigit = 0
        tensDigitIndex = 0

        for i in range(len(ratings) - 1): # Remove the last character as it cannot be a tensDigit
            if(int(ratings[i]) > tensDigit):
                tensDigit = int(ratings[i])
                tensDigitIndex = i

        onesDigit = int(max(ratings[tensDigitIndex + 1:])) # Find max of characters after the tensDigitIndex for the max two digit joltage

        self.__joltage += tensDigit * 10 + onesDigit

scriptDir = os.path.dirname(__file__)
filePath = os.path.join(scriptDir, f"Day 3 Inputs.txt")
with open(filePath, "r") as f:
    lines = f.readlines()

day3 = Day3()
i = 1

for line in lines:
    if(line == "\n" or not line): # Empty line, reset program
        print(f"Iteration {i}'s total output joltage: {day3.joltage}")
        
        day3 = Day3()
        i += 1

    else:
        day3.findLargestJoltage(line.strip()) # Remove newline character