import os

def findAccessiblePapers(diagram):
    accessiblePapers = 0

    for row in range(len(diagram)):
        for col in range(len(diagram[row])):
            if(diagram[row][col] == '@' and numNeighbors(diagram, row, col) < 4):
                accessiblePapers += 1
    
    return accessiblePapers

def numNeighbors(diagram, row, col):
    neighbors = 0

    for x in range(-1, 2):
        for y in range(-1, 2):
            if(x == 0 and y == 0): continue
            if(0 > row + x or len(diagram) <= row + x): continue
            if(0 > col + y or len(diagram[row]) <= col + y): continue

            if(diagram[row + x][col + y] == '@'):
                neighbors += 1
    
    return neighbors

scriptDir = os.path.dirname(__file__)
filePath = os.path.join(scriptDir, f"Day 4 Inputs.txt")
with open(filePath, "r") as f:
    lines = f.readlines()

i = 1
diagram = []

for line in lines:
    if(line == "\n" or not line): # Empty line, reset program
        print(f"Iteration {i}'s accessible papers: {findAccessiblePapers(diagram)}")
        
        diagram = []
        i += 1

    else:
        diagram.append(line.strip()) # Remove newline character