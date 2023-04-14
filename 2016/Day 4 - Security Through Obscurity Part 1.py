#Counting the occurences of letters in a string.

roomName = input()
sumIDs = 0

while(roomName):
    #Some input processing: isolating the letters, id, and checksum.
    roomName = roomName.split("-")
    id, checksum = roomName[-1].split("[")
    id, checksum = int(id), checksum.strip("]")
    roomName = "".join(roomName[:-1])

    occurences = {}

    for ch in roomName:
        occurences[ch] = occurences.setdefault(ch, 0) + 1
    
    #Since we want to sort the number of occurences from the highest to the lowest and the letters alphabetically,
    #I've made the letters negative, which will favor letters in smaller ASCII values first.
    occurences = sorted(occurences.items(), key = lambda x: (x[1], -ord(x[0])), reverse = True)
    isEqual = True

    for x in range(len(checksum)):
        if(occurences[x][0] != checksum[x]):
            isEqual = False
            break
    
    if(isEqual):
        sumIDs += id

    roomName = input()

print(sumIDs)