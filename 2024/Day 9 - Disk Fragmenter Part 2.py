import sys

diskMap = ""
blockRepr = []
fileId = 0
maxOpenSize = 0

for block in diskMap.strip():
    if(int(block) == 0):
        fileId += 1
        continue
    
    if(fileId % 2 == 0):
        blockRepr.append((str(fileId // 2), int(block)))
    
    else:
        blockRepr.append((".", int(block)))
        maxOpenSize = max(maxOpenSize, int(block))
    
    fileId += 1

prevFileId = (fileId // 2) + 1
j = len(blockRepr) - 1
checkSum = 0

while(j >= 0):
    if(blockRepr[j][0] == "." or blockRepr[j][1] > maxOpenSize or int(blockRepr[j][0]) >= prevFileId):
        if(blockRepr[j][0] != "." and blockRepr[j][1] > maxOpenSize):
            prevFileId -= 1
        
        j -= 1
        continue

    for i, block in enumerate(blockRepr):
        if(i >= j): break
        
        if(block[0] == "." and block[1] >= blockRepr[j][1]):
            if(block[1] - blockRepr[j][1] == 0):
                blockRepr[i], blockRepr[j] = blockRepr[j], blockRepr[i]
            
            else:
                blockHolder = blockRepr[j]
                blockRepr[i] = (blockRepr[i][0], blockRepr[i][1] - blockRepr[j][1])
                blockRepr[j] = (blockRepr[i][0], blockRepr[j][1])
                blockRepr.insert(i, blockHolder)
                j += 1
            
            break
    
    prevFileId -= 1
    j -= 1

index = 0

for block in blockRepr:
    if(block[0] == "."):
        index += block[1]
        continue
    
    for x in range(block[1]):
        checkSum += int(block[0]) * index
        index += 1

print(checkSum)