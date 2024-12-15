directions = {
    "^": (-1, 0),
    ">": (0, 1),
    "v": (1, 0),
    "<": (0, -1),
}

walls = set()
boxes = set()
robot = ()

gridSetupped = False

puzzleInput = []

with open("2024/Day 15 text file.txt") as f:
    puzzleInput = f.readlines()

for y, line in enumerate(puzzleInput):
    line = line.strip()

    if(not line):
        gridSetupped = True
        continue

    if(not gridSetupped):
        for x, char in enumerate(line):
            if(char == "#"):
                walls.add((y, x))
            elif(char == "O"):
                boxes.add((y, x))
            elif(char == "@"):
                robot = (y, x)
    
    else:
        for char in line:
            movements = []
            curPos = (robot[0] + directions[char][0], robot[1] + directions[char][1])

            while(curPos in boxes):
                movements.append(curPos)
                curPos = (curPos[0] + directions[char][0], curPos[1] + directions[char][1])
            
            if(curPos in walls):
                continue

            while(movements):
                toChange = movements.pop()
                boxes.remove(toChange)
                boxes.add((toChange[0] + directions[char][0], toChange[1] + directions[char][1]))
            
            if((robot[0] + directions[char][0], robot[1] + directions[char][1]) not in walls):
                robot = (robot[0] + directions[char][0], robot[1] + directions[char][1])
sum = 0

for box in boxes:
    sum += ((box[0] * 100) + box[1])

print(sum)