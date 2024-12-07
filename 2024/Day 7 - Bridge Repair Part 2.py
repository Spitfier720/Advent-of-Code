import sys

def canFormResult(result, operands):
    if(len(operands) == 1):
        return operands[0] == result

    return canFormResult(result, [operands[0] + operands[1]] + operands[2:]) or \
           canFormResult(result, [operands[0] * operands[1]] + operands[2:]) or \
           canFormResult(result, [int(str(operands[0]) + str(operands[1]))] + operands[2:])

sum = 0

for line in sys.stdin.readlines():
    line = line.split(":")

    result = int(line[0])
    operands = list(map(int, line[1].strip().split(" ")))

    if(canFormResult(result, operands)):
        sum += result

print(sum)