import sys

sum = 0

for line in sys.stdin.readlines():
    game = line.split(":")[1].strip()
    rounds = game.split(";")
    r, g, b = 0, 0, 0
    
    for round in rounds:
        
        for cube in round.strip().split(","):
            cube = cube.strip().split()
            
            if(cube[1] == "red"):
                r = max(r, int(cube[0]))
            elif(cube[1] == "green"):
                g = max(g, int(cube[0]))
            elif(cube[1] == "blue"):
                b = max(b, int(cube[0]))
        
    sum += r * g * b

print(sum)