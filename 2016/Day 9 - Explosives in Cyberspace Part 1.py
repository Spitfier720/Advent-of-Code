#Decompressing a string by utilizing string slicing and a bit of math.

sequence = open("FileToDecompress.txt", "r").read()
total, pastIndex, startingIndex = 0, 0, sequence.find("(")

while(startingIndex != -1):
    total += startingIndex - pastIndex #Adding the new characters
    closingIndex = sequence.find(")", startingIndex + 1)

    #Adding the repeated characters.
    numChars, numReps = map(int, sequence[startingIndex + 1: closingIndex].split("x"))
    total += numChars * numReps
    
    #Properly updating the indexes.
    pastIndex = closingIndex + numChars + 1
    startingIndex = sequence.find("(", pastIndex)

total += len(sequence) - pastIndex
print(total)