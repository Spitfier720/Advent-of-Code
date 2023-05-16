#Checking several strings to find two almost identical ones.

boxId = input()
candidates = []
correctBoxes = ""

while(boxId):
    for x in candidates:
        differentChars = 0
        commonChars = ""
        
        for i in range(len(boxId)):
            differentChars += boxId[i] != x[i]
            commonChars += boxId[i] if boxId[i] == x[i] else ""

            if(differentChars > 1):
                break
        
        if(differentChars == 1):
            correctBoxes = commonChars
            break
    
    candidates.append(boxId)
    boxId = input()

print(correctBoxes)