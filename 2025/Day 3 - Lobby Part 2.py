import os

class Day3:
    def __init__(self):
        self.__joltage = 0
    
    @property
    def joltage(self):
        return self.__joltage
    
    def findLargestJoltage(self, ratings, numDigits):
        ratingLength = len(ratings)
        maxJoltage = 0
        cutoffIndexLeft = 0 # When a number is chosen for the maxJoltage, we cannot include any characters before and including it since we cannot rearrange batteries
        cutoffIndexRight = ratingLength - numDigits + 1 # This is to ensure we have enough digits remaining to make the rest of our maximum joltage

        for x in range(numDigits):
            maxRating, maxIndex = self.getMaxRating(ratings[cutoffIndexLeft: cutoffIndexRight + x])
            maxJoltage = maxJoltage * 10 + maxRating
            cutoffIndexLeft += maxIndex + 1
        
        self.__joltage += maxJoltage
    
    def getMaxRating(self, ratings):
        maxRating = 0
        maxIndex = 0

        for i in range(len(ratings)):
            if(int(ratings[i]) > maxRating):
                maxRating = int(ratings[i])
                maxIndex = i
        
        return maxRating, maxIndex
            

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
        day3.findLargestJoltage(line.strip(), 12) # Remove newline character