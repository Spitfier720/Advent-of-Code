import sys

def simulateBlink(stones):
    newStones = {}
    
    for s in stones:
        if(s == 0):
            newStones[1] = newStones.setdefault(1, 0) + stones[s]
        
        elif(len(str(s)) % 2 == 0):
            newStones[int(str(s)[:len(str(s)) // 2])] = newStones.setdefault(int(str(s)[:len(str(s)) // 2]), 0) + stones[s]
            newStones[int(str(s)[len(str(s)) // 2:])] = newStones.setdefault(int(str(s)[len(str(s)) // 2:]), 0) + stones[s]
        
        else:
            newStones[s * 2024] = newStones.setdefault(s * 2024, 0) + stones[s]
    
    return newStones

stones = {}
puzzleInput = list(map(int, sys.stdin.readline().split()))

for num in puzzleInput:
    stones[num] = stones.setdefault(num, 0) + 1

for x in range(75):
    stones = simulateBlink(stones)

print(sum(stones.values()))