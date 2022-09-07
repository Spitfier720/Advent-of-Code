#Finding valid strings with a different set of requirements

line = input()
textFile = []

#Account for multi-line input
while(line):
    textFile.append(line)
    line = input()

niceStrings = 0

for string in textFile:

    #Create flags to find if a string is valid
    hasRepeatingPair, hasValidPalindrome = False, False
    pastChar, pastpastChar = "", ""
    letterPairs = []

    for char in string:
        
        #In our case, a valid palindrome is a 3 character substring whose first and last letters are the same
        if(pastpastChar == char):
            hasValidPalindrome = True
        
        #Does our current pair match with any other letter pairs we've seen?
        #The character pairs must not overlap, like "aaa", so this fixes the problem
        if(pastChar and pastChar + char in letterPairs[:-1]):
            hasRepeatingPair = True
        
        #The set will have an element that's one character long,
        #but for the scope of our problem, it won't matter
        else:
            letterPairs.append(pastChar + char)

        pastpastChar = pastChar
        pastChar = char
    
    if(hasRepeatingPair and hasValidPalindrome):
        niceStrings += 1

print(niceStrings)
