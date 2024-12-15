import sys

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
                walls.add((y, x * 2))
                walls.add((y, (x * 2) + 1))
            elif(char == "O"):
                boxes.add((y, x * 2))
            elif(char == "@"):
                robot = (y, x * 2)
    
    else:
        for char in line:
            movements = []
            queue = [(robot[0] + directions[char][0], robot[1] + directions[char][1])]
            visited = set()

            isValidMove = True

            while(queue):
                curPos = queue.pop(0)

                if(curPos in walls):
                    movements = []
                    isValidMove = False
                    break

                if(curPos in boxes or (curPos[0], curPos[1] - 1) in boxes):
                    oldPos = curPos
                    curPos = curPos if curPos in boxes else (curPos[0], curPos[1] - 1)

                    if(curPos in visited):
                        continue

                    visited.add(curPos)
                    movements.append(curPos)

                    queue.append((curPos[0] + directions[char][0], curPos[1] + directions[char][1] * (1 if oldPos != curPos else 2)))

                    if(char == "^" or char == "v"):
                        queue.append((curPos[0] + directions[char][0], curPos[1] + 1))
            
            if(not isValidMove):
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