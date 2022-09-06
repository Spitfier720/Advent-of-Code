#When will our boy Santa reach the basement? This program will find out!

instructions = input()
floor = 0

#Iterate through each instruction until floor is less than 0
for i in range(len(instructions)):
    floor = floor + 1 if instructions[i] == "(" else floor - 1
    
    if(floor == -1):
        print(i + 1)
        break