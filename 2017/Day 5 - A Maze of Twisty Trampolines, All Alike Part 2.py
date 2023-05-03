#Calculating the amount of times it takes to jump out of a list of numbers, using the elements as jumps.

import sys

offsets = [int(x) for x in sys.stdin.readlines()]
index, steps, length = 0, 0, len(offsets)

while(0 <= index < length):
    increment = 1 if offsets[index] < 3 else -1
    offsets[index] += increment
    index += offsets[index] - increment
    steps += 1

print(steps)