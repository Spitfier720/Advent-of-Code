#Finding three numbers in a list that add to a certain number.

#Finds three numbers in the report that add to 2020, and returns the product of those three numbers.
def processReport(report):
    for x in report:
        for y in report:
            if(2020 - x - y in report):
                return x * y * (2020 - x - y)

import sys; print(processReport(set(map(int, sys.stdin.readlines()))))