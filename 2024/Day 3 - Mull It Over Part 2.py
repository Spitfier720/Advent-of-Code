import math
import sys

def isValid(instruction):
    if(len(instruction.split(",")) != 2): return False
    
    instruction = instruction.split(",")
    if(not instruction[0].isnumeric() or not instruction[1].isnumeric()): return False
    
    instruction = list(map(int, instruction))
    validRange = range(1, 1000)
    if(instruction[0] not in validRange or instruction[1] not in validRange): return False
    
    return True

rawMemory = "".join(sys.stdin.readlines()).split("don't()")
enabledMemory = rawMemory[0] + "".join(map(lambda x: "".join(x.split("do()")[1:]) if "do()" in x else "", rawMemory[1:]))

memory = enabledMemory.split("mul(")

allInstructions = map(lambda x: x.split(")")[0] if ")" in x else "", memory)
validInstructions = filter(isValid, allInstructions)

sum = 0

for i in validInstructions:
    sum += math.prod(map(int, i.split(",")))

print(sum)