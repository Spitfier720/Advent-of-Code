#Summing up numerous numbers to see which number first appears twice.

import sys

numbers = {0}
frequency = 0
foundDuplicate = False
changes = [int(x) for x in sys.stdin.readlines()]

while(not foundDuplicate):
    for x in changes:
        frequency += x

        if(frequency in numbers):
            print(frequency)
            foundDuplicate = True
            break
        
        numbers.add(frequency)