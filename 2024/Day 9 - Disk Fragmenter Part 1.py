import sys

diskMap = ""
blockRepr = []
fileId = 0

for block in diskMap.strip():
    if(fileId % 2 == 0):
        blockRepr += [str(fileId // 2)] * int(block)
    
    else:
        blockRepr += ["."] * int(block)
    
    fileId += 1
    
i, j = 0, len(blockRepr) - 1
checkSum = 0

while(i <= j):
    if(blockRepr[i] == "."):
        if(i == j): break
        
        while(blockRepr[j] == "."):
            j -= 1
        
        blockRepr[i], blockRepr[j] = blockRepr[j], blockRepr[i]
        j -= 1
    
    checkSum += i * int(blockRepr[i])
    i += 1

print(checkSum)