import os

class Day6:
    def __init__(self):
        self.__total = 0
    
    @property
    def total(self):
        return self.__total

    def calculate(self, operations, worksheet):
        equations = self.parseWorksheet(worksheet)

        for i in range(len(operations)):
            if(operations[i] == "+"):
                self.__total += sum(equations[i])
            
            elif(operations[i] == "*"):
                product = 1
                for num in equations[i]:
                    product *= num
                
                self.__total += product
    
    def parseWorksheet(self, worksheet):
        equations = []
        index = 0

        for i in range(len(worksheet[0]) - 1, -1, -1): # Assuming each row has same number of columns
            hasNumber = False
            number = 0
            for j in range(len(worksheet)):
                if(worksheet[j][i].isnumeric()):
                    number = number * 10 + int(worksheet[j][i])
                    hasNumber = True
            
            if(hasNumber):
                if(index >= len(equations)):
                    equations.append([number])
                else:
                    equations[index].append(number)

            else:
                index += 1
        
        return equations


scriptDir = os.path.dirname(__file__)
filePath = os.path.join(scriptDir, f"Day 6 Inputs.txt")
with open(filePath, "r") as f:
    lines = f.readlines()

day6 = Day6()
worksheet = []
i = 1

for line in lines:
    if(line.strip() == "---"): # End of input, reset program
        print(f"Iteration {i}'s fresh ingredient ranges: {day6.total}")
        
        day6 = Day6()
        worksheet = []
        i += 1

    else:
        if("*" in line or "+" in line): # Using operations
            day6.calculate(list(reversed(line.strip().split())), worksheet)
        else:
            worksheet.append(line[:-1]) # Remove newline character