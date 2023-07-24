#Finding the number of occurences of a letter in a string.

import sys

def isValidPassword(line):
    constraints, letter, password = line.split()
    mn, mx = map(int, constraints.split("-"))
    return mn <= password.count(letter[0]) <= mx

lst = sys.stdin.readlines()
sum = 0

for x in lst:
    sum += isValidPassword(x)

print(sum)