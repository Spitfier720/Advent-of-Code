import sys

def findXMAS(pos, board):
    directions = [
        (-1, 0),
        (-1, 1),
        (0, 1),
        (1, 1),
        (1, 0),
        (1, -1),
        (0, -1),
        (-1, -1)
    ]
    count = 0
    
    for d in directions:
        if(not withinBoard(pos[0] + (d[0] * 3), pos[1] + (d[1] * 3), board)):
            continue
        
        isitXMAS = True
        
        for x in range(1, 4):
            if(board[pos[0] + (d[0] * x)][pos[1] + (d[1] * x)] != "XMAS"[x]):
                isitXMAS = False
                break
        
        count += isitXMAS
    
    return count

def withinBoard(x, y, board):
    return 0 <= x < len(board) and 0 <= y < len(board[0]) 

board = []
rowNum = 0
XPositions = []

for line in sys.stdin.readlines():
    for i in range(len(line)):
        if(line[i] == "X"):
            XPositions.append((rowNum, i))
    
    board.append(line)
    rowNum += 1

numXMAS = 0

for pos in XPositions:
    numXMAS += findXMAS(pos, board)

print(numXMAS)