#Checking for occurences of characters in several strings.

boxId = input()
twoCount, threeCount = 0, 0

while(boxId):
    occurences = {}
    
    for x in boxId:
        occurences[x] = occurences.setdefault(x, 0) + 1
    
    twoCount += 2 in occurences.values()
    threeCount += 3 in occurences.values()

    boxId = input()

print(twoCount * threeCount)