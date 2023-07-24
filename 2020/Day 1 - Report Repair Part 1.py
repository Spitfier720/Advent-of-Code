#Finding two numbers in a list that add to a certain number.

#Finds two numbers in the report that add to 2020, and returns the product of those two numbers.
def processReport(report):
    for x in report:
        if(2020 - x in report):
            return x * (2020 - x)

import sys; print(processReport(set(map(int, sys.stdin.readlines()))))