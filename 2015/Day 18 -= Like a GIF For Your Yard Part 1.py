#Simulating a light animation using the rules of the Game of Life.

line = input()
row = 0

#Starting off length at -1 to make it 0-indexed.
length = -1

#We put our cells into a set to save time and ignore empty space.
aliveCells = set()

while(line):
    for col in range(len(line)):
        if(line[col] == "#"):
            aliveCells.add((row, col))
    
    row += 1
    length += 1
    line = input()

#Creating all eight directions for neighboring cells.
directions = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]

for x in range(100):
    #Creating a new set for our next generation, since all cells change at the same time.
    nextGen = set()

    for cell in aliveCells:

        #Determines the number of cells adjacent to an alive cell.
        neighborCellsCont = 0

        for dir in directions:
            #A check that our neighboring cell isn't out of range.
            if(not(0 <= cell[0] + dir[0] <= length and 0 <= cell[1] + dir[1] <= length)):
                continue
            
            #Determine the number of cells ajacent to a dead cell that could potentially come back alive.
            neighborCellsBorn = 0

            #This will find out the adjacent cells next to a dead cell, which is why we loop through directions again.
            for nextDir in directions:
                if(not(0 <= cell[0] + dir[0] + nextDir[0] <= length and 0 <= cell[1] + dir[1] + nextDir[1] <= length)):
                    continue

                if((cell[0] + dir[0] + nextDir[0], cell[1] + dir[1] + nextDir[1]) in aliveCells):
                    neighborCellsBorn += 1
            
            if(neighborCellsBorn == 3):
                nextGen.add((cell[0] + dir[0], cell[1] + dir[1]))

            if((cell[0] + dir[0], cell[1] + dir[1]) in aliveCells):
                neighborCellsCont += 1
        
        if(2 <= neighborCellsCont <= 3):
            nextGen.add(cell)
    
    print(nextGen)
    aliveCells = set(nextGen)

print(len(aliveCells))