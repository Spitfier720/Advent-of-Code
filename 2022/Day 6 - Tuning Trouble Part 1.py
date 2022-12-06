#Finding the first occurence of four distinct consecuitive letters in a string.

signal = input()

startPacket = [signal[x] for x in range(3)]
charCount = 3

while(charCount <= len(signal)):
    startPacket.append(signal[charCount])
    
    visited = set()
    distinct = True

    for x in startPacket:
        if(x in visited):
            distinct = False
            break

        visited.add(x)

    if(distinct):
        print(charCount + 1)
        break

    startPacket.pop(0)
    charCount += 1