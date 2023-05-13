#Processing a stream of characters using some somewhat complex rules.

#stream = input()
stream = open("CharacterStream.txt", "r").read()
isGarbage = False
index = 0
score = 0

while(index < len(stream)):
    match stream[index]:
        case "<":
            if(isGarbage):
                score += 1

            isGarbage = True
        
        case ">":
            isGarbage = False

        case "!":
            index += 1
        
        case _:
            if(isGarbage):
                score += 1

    index += 1

print(score)