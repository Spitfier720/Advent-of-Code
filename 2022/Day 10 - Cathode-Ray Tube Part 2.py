#Simulating commands that take different times to complete.

#Holding the x value and cycle number.
x = 1
cycle = 1

#Our CRT which will be our output.
crt = [["." for x in range(40)] for y in range(6)]

line = input().split()

while(line):
    if(line[0] == "addx"):
        #We add two here since the other way didn't properly simulate the device, because it wasn't necessary.
        for i in range(2):
            #If the current position is within the sprite's position, which is from x - 1 to x + 1.
            if(x - 1 <= (cycle - 1) % 40 <= x + 1):
                #The cycles need to be subtracted by 1 to 0-index.
                crt[(cycle - 1) // 40][(cycle - 1) % 40] = "#"
            
            cycle += 1
        
        #We only add to the x value after the two cycles are done.
        x += int(line[1])
    
    #The crt will still be drawn in this cycle.
    else:    
        if(x - 1 <= (cycle - 1) % 40 <= x + 1):
            crt[(cycle - 1) // 40][(cycle - 1) % 40] = "#"

        cycle += 1
    
    line = input().split()

print("\n".join("".join(x) for x in crt))