import os

class Day6:
    def __init__(self):
        self.__equations = []
        self.__total = 0
    
    @property
    def total(self):
        return self.__total
    
    def addRow(self, row):
        if("*" in row or "+" in row): # Using operations
            self.calculate(row.strip().split())
            return

        numbers = list(map(int, row.strip().split()))

        for i in range(len(numbers)):
            if(i + 1 > len(self.__equations)):
                self.__equations.append([numbers[i]])
            
            else:
                self.__equations[i].append(numbers[i])
    
    def calculate(self, operations):
        for i in range(len(operations)):
            if(operations[i] == "+"):
                self.__total += sum(self.__equations[i])
            
            elif(operations[i] == "*"):
                product = 1
                for num in self.__equations[i]:
                    product *= num
                
                self.__total += product

scriptDir = os.path.dirname(__file__)
filePath = os.path.join(scriptDir, f"Day 6 Inputs.txt")
with open(filePath, "r") as f:
    lines = f.readlines()

day6 = Day6()
i = 1

for line in lines:
    if(line.strip() == "---"): # End of input, reset program
        print(f"Iteration {i}'s fresh ingredient ranges: {day6.total}")
        
        day6 = Day6()
        i += 1

    else:
        day6.addRow(line)