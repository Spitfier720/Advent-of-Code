import sys

def simulateBlink(stones):
    newStones = []
    
    for s in stones:
        if(s == 0):
            newStones.append(1)
        
        elif(len(str(s)) % 2 == 0):
            newStones.append(int(str(s)[:len(str(s)) // 2]))
            newStones.append(int(str(s)[len(str(s)) // 2:]))
        
        else:
            newStones.append(s * 2024)
        
    return newStones

stones = list(map(int, sys.stdin.readline().split()))

for x in range(25):
    stones = simulateBlink(stones)

print(len(stones))