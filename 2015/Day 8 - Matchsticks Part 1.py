#Find the difference between the literal and memory length of strings with escape characters.

import sys

santasList = [x for x in sys.stdin.readlines()]
literalTotal = 0
memoryTotal = 0

#Iterate through each string and add the totals one by one.
for string in santasList:
    literalTotal += len(string) - 1
    
    #Index starts at 1 due to the quotes being counted out of the string.
    index = 1

    #This is a while loop since the index can be changed by more than just 1.
    #The condition specifies that it ends 2 characters before the end of the string, to account for the quote and newline.
    while(index < len(string) - 2):
        if(string[index] != '\\'):
            index += 1
        
        #The character is an escape character, which means the characters consisting of the escape characters will be skipped
        else:
            #Either \\ or \"
            if(string[index + 1] != 'x'):
                index += 2
            
            #\x00, where the 0s are any digit, to represent a character in hex.
            else:
                index += 4

        memoryTotal += 1

print(literalTotal - memoryTotal)