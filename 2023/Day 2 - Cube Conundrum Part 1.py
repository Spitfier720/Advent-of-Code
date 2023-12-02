import sys

red, green, blue = 12, 13, 14
sumID = 0
id = 1

for line in sys.stdin.readlines():
    game = line.split(":")[1].strip()
    rounds = game.split(";")
    isPossible = True

    for round in rounds:
        r, g, b = 0, 0, 0
        
        for cube in round.strip().split(","):
            cube = cube.strip().split()
            
            if(cube[1] == "red"):
                r += int(cube[0])
            elif(cube[1] == "green"):
                g += int(cube[0])
            elif(cube[1] == "blue"):
                b += int(cube[0])
        
        if(r > red or g > green or b > blue):
            isPossible = False
            break
    
    if(isPossible):
        sumID += id
    
    id += 1

print(sumID)