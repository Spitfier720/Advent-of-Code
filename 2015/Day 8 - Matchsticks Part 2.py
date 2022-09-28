#Find the difference between the literal and memory length of strings with escape characters.

import sys

santasList = [x for x in sys.stdin.readlines()]
difference = 0

#Iterate through each string and add the totals one by one.
for string in santasList:

    #Add 4 for the beginning and end quotes which always need 4 extra characters to make literal(for new beginning and end quotes)
    #Every other \ and " character in the string will only require one extra character
    #The count function has start and end constraints because we cannot include the beginning and end quotes again in our count
    difference += 4 + string.count("\"", 1, len(string) - 2) + string.count("\\", 1, len(string) - 2)

print(difference)