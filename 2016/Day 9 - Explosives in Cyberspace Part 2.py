#Decompressing a string by utilizing string slicing and a bit of math.

#Decompressing the marker, and possibly other markers within it as well.
def decompress(substr):
    total, pastIndex, startingIndex = 0, 0, substr.find("(")

    while(startingIndex != -1):
        total += startingIndex - pastIndex #Adding the new characters
        closingIndex = substr.find(")", startingIndex + 1)

        #Adding the repeated characters.
        numChars, numReps = map(int, substr[startingIndex + 1: closingIndex].split("x"))
        total += numReps * decompress(substr[closingIndex + 1: closingIndex + 1 + numChars])
        
        #Properly updating the indexes.
        pastIndex = closingIndex + numChars + 1
        startingIndex = substr.find("(", pastIndex)
    
    total += len(substr) - pastIndex
    return total

print(decompress(open("FileToDecompress.txt", "r").read()))