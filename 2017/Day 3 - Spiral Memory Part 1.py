#Finding where a number is in a spiral pattern and it's Manhattan Distance to the center.
#For reference, our spiral pattern looks as follows:
'''
17  16  15  14  13
18   5   4   3  12
19   6   1   2  11
20   7   8   9  10
21  22  23---> ...
'''

import math

number = int(input())

#Starting from 1, the bottom-right diagonal's numbers are all squares of odd numbers and have a distance that differs by 2.
#We can use this to find our Manhattan Distance quickly.

#Find largest odd number whos square is less than our input.
largestSquare = int(math.sqrt(number)) - 1 if int(math.sqrt(number)) % 2 == 0 else int(math.sqrt(number))

if(largestSquare * largestSquare == number): #If our number is a perfect odd square
    print(largestSquare - 1)

else:
    curDist = largestSquare #Moving to the next number after largestSquare^2 will increase the Manhattan Distance by 1.
    
    #Unless the number is less than 9, moving upwards will decrease the distance by 1.
    increment = -1 if largestSquare != 1 else 1

    for x in range(largestSquare * largestSquare + 1, number):
        curDist += increment

        #Checking if we have travelled halfway or fully across the length of one side.
        #If it is halfway across, the distance increases, since it takes the most distance to get to the corner of a square.
        #If it is fully across, the distance decreases, since it takes the least distance to get to the midpoint of its side.
        if((x + 1 - (largestSquare * largestSquare)) % ((largestSquare + 1) // 2) == 0):
            increment = -increment

    print(curDist)
