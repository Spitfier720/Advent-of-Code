#Following a reallocation process until we get a self-loop.

curConfig = tuple(map(int, input().split()))
length = len(curConfig)
configs = set()
steps = 0

while(curConfig not in configs):
    configs.add(curConfig)

    maxElement = 0
    index = 0

    for x in range(length):
        if(curConfig[x] > maxElement):
            maxElement = curConfig[x]
            index = x
    
    newConfig = []

    for x in range(length):
        offset = x - index

        if(offset <= 0):
            offset += length
        
        #Since we keep adding 1 to the next element until we run out, we can shorten this into a formula.
        blocksToAdd = int((((maxElement - offset) / length) + 1) // 1)
        
        if(x == index):
            newConfig.append(blocksToAdd)

        else:
            newConfig.append(curConfig[x] + blocksToAdd)
    
    steps += 1
    curConfig = tuple(newConfig)

print(steps)