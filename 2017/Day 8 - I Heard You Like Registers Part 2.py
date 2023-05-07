#Following a set of instructions that execute based on comparisons.

class CPU:
    def __init__(self):
        self.__registers = {}
        self.__maxValue = 0
    
    def __willRun(self, condition):
        match condition[1]:
            case "==": return condition[0] == condition[2]
            case "!=": return condition[0] != condition[2]
            case ">=": return condition[0] >= condition[2]
            case "<=": return condition[0] <= condition[2]
            case ">": return condition[0] > condition[2]
            case "<": return condition[0] < condition[2]

    def execute(self, command):
        if(self.__willRun([self.__registers.setdefault(command[4], 0), command[5], int(command[6])])):
            mult = 1 if command[1] == "inc" else -1
            self.__registers[command[0]] = self.__registers.setdefault(command[0], 0) + (int(command[2]) * mult)
            self.__maxValue = max(self.__maxValue, self.__registers[command[0]])
    
    def getLargest(self):
        return self.__maxValue

instruction = input().split()
cpu = CPU()

while(instruction):
    cpu.execute(instruction)
    instruction = input().split()

print(cpu.getLargest())