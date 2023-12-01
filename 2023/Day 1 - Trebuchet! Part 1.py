import sys

sum = 0

for line in sys.stdin.readlines():
    newNum = ""

    # Find first occurence of digit.
    for x in line:
        if x.isdigit():
            newNum += x
            break
    
    # Find last occurence of digit.
    for x in range(len(line) - 1, -1, -1):
        if line[x].isdigit():
            newNum += line[x]
            break
    
    sum += int(newNum)

print(sum)