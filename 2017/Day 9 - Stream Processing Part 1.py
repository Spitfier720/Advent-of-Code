#Processing a stream of characters using some somewhat complex rules.

#stream = input()
stream = open("CharacterStream.txt", "r").read()
groupNum = 0
isGarbage = False
index = 0
score = 0

while(index < len(stream)):
    match stream[index]:
        case "{":
            if(not isGarbage):
                score += groupNum + 1
                groupNum += 1
        
        case "}":
            groupNum -= not isGarbage
        
        case "<":
            isGarbage = True
        
        case ">":
            isGarbage = False

        case "!":
            index += 1

    index += 1

print(score)