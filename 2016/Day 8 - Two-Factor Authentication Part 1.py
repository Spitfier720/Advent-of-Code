#Simulating a grid of lights by making rectangles and shifting lines.

LENGTH, WIDTH = 50, 6
screen = [[" " for x in range(LENGTH)] for y in range(WIDTH)]
numOn = 0
operation = input()

while(operation):
    operation = operation.split()
    
    if(operation[0] == "rect"):
        a, b = map(int, (operation[1].split("x")))
        
        for x in range(b):
            for y in range(a):
                if(screen[x][y] == " "):
                    screen[x][y] = "*"
                    numOn += 1

    else:
        index = int(operation[2].split("=")[1])
        shift = int(operation[4])

        if(operation[1] == "row"):
            screen[index] = screen[index][LENGTH - shift:] + screen[index][:LENGTH - shift]
        
        else:
            newColumn = [screen[(x - shift + WIDTH) % WIDTH][index] for x in range(WIDTH)]
            
            for x in range(WIDTH):
                screen[x][index] = newColumn[x]

    operation = input()

print(numOn)