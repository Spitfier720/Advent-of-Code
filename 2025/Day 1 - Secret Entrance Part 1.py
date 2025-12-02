import os

class Day1:
    def __init__(self):
        self.__dial = 50

    @property
    def dial(self):
        return self.__dial

    def rotateLeft(self, steps):
        self.__dial -= steps

        while self.__dial < 0:
            self.__dial += 100

    def rotateRight(self, steps):
        self.__dial += steps

        while self.__dial > 99:
            self.__dial -= 100

scriptDir = os.path.dirname(__file__)
filePath = os.path.join(scriptDir, f"Day 1 Inputs.txt")
with open(filePath, "r") as f:
    lines = f.readlines()

day1 = Day1()
password = 0
i = 1

for line in lines:
    if(line == "\n" or not line): # Empty line, reset program
        print(f"Iteration {i}'s password: {password}")
        
        day1 = Day1()
        password = 0
        i += 1

    else:
        direction = line[0]
        amount = int(line[1:])

        if(direction == "L"):
            day1.rotateLeft(amount)
        
        else:
            day1.rotateRight(amount)
        
        if(day1.dial == 0):
            password += 1
