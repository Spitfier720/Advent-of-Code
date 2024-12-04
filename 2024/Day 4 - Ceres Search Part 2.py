import sys

def findXMAS(pos, board):
    directions = [
        (-1, 1),
        (1, 1),
        (1, -1),
        (-1, -1)
    ]
    
    MASPos = {}
    
    for d in directions:
        if(not withinBoard(pos[0] + d[0], pos[1] + d[1], board)): 
            return 0
        
        if(board[pos[0] + d[0]][pos[1] + d[1]] not in "MS"): 
            return 0
        
        MASPos.setdefault(board[pos[0] + d[0]][pos[1] + d[1]], []).append((pos[0] + d[0], pos[1] + d[1]))
    
    if("M" not in MASPos or "S" not in MASPos): 
        return 0
    
    if(len(MASPos["M"]) != 2 or len(MASPos["S"]) != 2): 
        return 0
    
    if(MASPos["M"][0][0] != MASPos["M"][1][0] and MASPos["M"][0][1] != MASPos["M"][1][1]): 
        return 0
    
    return 1

def withinBoard(x, y, board):
    return 0 <= x < len(board) and 0 <= y < len(board[0]) 

board = []
rowNum = 0
XPositions = []

for line in sys.stdin.readlines():
    for i in range(len(line)):
        if(line[i] == "A"):
            XPositions.append((rowNum, i))
    
    board.append(line)
    rowNum += 1

numXMAS = 0

for pos in XPositions:
    numXMAS += findXMAS(pos, board)

print(numXMAS)