#Using binary search to single out a seat in a grid.

import sys

#Holds the ranges in which the seat could be in, and with enough partitioning, will narrow the range to a single number.
class RowsBinary:
    def __init__(self, length):
        self.__left = 0
        self.__right = length
        self.__middle = (self.__right // 2)
    
    #The right half of the range will be dropped, leaving only the left half to be considered.
    def partitionLeft(self):
        self.__right = self.__middle
        self.__middle = (self.__left + self.__right) // 2
    
    #The left half of the range will be dropped, leaving only the right half to be considered.
    def partitionRight(self):
        self.__left = self.__middle + 1
        self.__middle = (self.__left + self.__right) // 2
    
    def getResult(self):
        return self.__left if self.__left == self.__right else None

#Finds the right seat using the RowsBinary class and returns its String ID.
def findSeat(stringInput):
    row = RowsBinary(127)
    
    #Getting the row.
    for x in stringInput[:7]:
        match x:
            case "F":
                row.partitionLeft()
            
            case "B":
                row.partitionRight()
    
    col = RowsBinary(7)

    #Getting the column.
    for x in stringInput[7:]:
        match x:
            case "L":
                col.partitionLeft()

            case "R":
                col.partitionRight()
    
    return (row.getResult() * 8) + col.getResult()

print(max(findSeat(x) for x in sys.stdin.readlines()))