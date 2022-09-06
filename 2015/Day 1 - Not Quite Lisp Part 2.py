instructions = input()
floor = 0

for i in range(len(instructions)):
    floor = floor + 1 if instructions[i] == "(" else floor - 1
    
    if(floor == -1):
        print(i + 1)
        break