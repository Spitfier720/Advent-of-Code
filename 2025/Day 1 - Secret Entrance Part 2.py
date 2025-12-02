import os

class Day1:
    def __init__(self):
        self.__dial = 50
        self.__password = 0

    @property
    def password(self):
        return self.__password

    def rotateLeft(self, steps):
        #If the dial starts at 0, it does not count as pointing at 0, so subtract 1 to compensate
        if(self.__dial == 0):
            self.__password -= 1
        
        self.__dial -= steps

        while self.__dial < 0:
            self.__dial += 100
            self.__password += 1
        
        # Catch if the dial rotates exactly to 0, special case
        if(self.__dial == 0):
            self.__password += 1

    def rotateRight(self, steps):
        self.__dial += steps

        while self.__dial > 99:
            self.__dial -= 100
            self.__password += 1

scriptDir = os.path.dirname(__file__)
filePath = os.path.join(scriptDir, f"Day 1 Inputs.txt")
with open(filePath, "r") as f:
    lines = f.readlines()

day1 = Day1()
i = 1

for line in lines:
    if(line == "\n" or not line): # Empty line, reset program
        print(f"Iteration {i}'s password: {day1.password}")
        day1 = Day1()
        i += 1

    else:
        direction = line[0]
        amount = int(line[1:])

        if(direction == "L"):
            day1.rotateLeft(amount)
        
        else:
            day1.rotateRight(amount)
