#Finding the first occurence of four distinct consecuitive letters in a string.

signal = input()

#Getting the first 3 elements in the string, since we need four distinct consecuitive letters.
startPacket = [signal[x] for x in range(3)]

#Our index is set to 3 for the same reason.
charCount = 3

while(charCount <= len(signal)):
    startPacket.append(signal[charCount])
    
    visited = set()
    distinct = True

    #Check if the packet has all unique characters
    for x in startPacket:
        if(x in visited):
            distinct = False
            break

        visited.add(x)

    if(distinct):
        #Since the answer requires 1-indexing.
        print(charCount + 1)
        break

    #Taking out the first element from our potential packet, since we need to maintain only four letters.
    startPacket.pop(0)
    charCount += 1