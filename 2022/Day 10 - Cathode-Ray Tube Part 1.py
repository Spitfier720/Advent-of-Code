#Simulating commands that take different times to complete.

#Holding the x value, the cycle number and the total strengths.
x = 1
cycle = 1
strengths = 0

line = input().split()

while(line):
    if(line[0] == "addx"):
        #Add to the cycle here since addx takes two cycles.
        cycle += 1

        #If the cycle number is 40x + 20, where x >= 0.
        if((cycle + 20) % 40 == 0):
            strengths += cycle * x
        
        x += int(line[1])

    #This will update the cycle to the correct number regardless of the command.
    cycle += 1

    #Since the cycle number is updated, we need to check here as well. Very unfortunate.
    if((cycle + 20) % 40 == 0):
        strengths += cycle * x

    line = input().split()

print(strengths)