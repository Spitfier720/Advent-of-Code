#Finding valid strings with a set of requirements

line = input()
textFile = []

#Account for multi-line input
while(line):
    textFile.append(line)
    line = input()

niceStrings = 0
naughtyPairs = {"ab", "cd", "pq", "xy"}

for string in textFile:

    #Creating flags to find out if a string is valid(nice)
    sameLetters, hasNaughtyPair = False, False
    pastChar = ""
    vowelCount = 0

    for char in string:
        if(char in "aeiou"):
            vowelCount += 1
        
        if(pastChar == char):
            sameLetters = True
        
        if(pastChar + char in naughtyPairs):
            hasNaughtyPair = True
            break
        
        pastChar = char
    
    if(sameLetters and not hasNaughtyPair and vowelCount >= 3):
        niceStrings += 1

print(niceStrings)
