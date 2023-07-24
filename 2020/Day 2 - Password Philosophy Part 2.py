#Finding the of occurences of a letter at a certain index of a string.

import sys

def isValidPassword(line):
    constraints, letter, password = line.split()
    mn, mx = map(int, constraints.split("-"))
    return (password[mn - 1] == letter[0]) + (password[mx - 1] == letter[0]) == 1

lst = sys.stdin.readlines()
sum = 0

for x in lst:
    sum += isValidPassword(x)

print(sum)