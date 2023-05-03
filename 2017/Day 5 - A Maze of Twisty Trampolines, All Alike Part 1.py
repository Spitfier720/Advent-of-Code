#Calculating the amount of times it takes to jump out of a list of numbers, using the elements as jumps.

import sys

offsets = [int(x) for x in sys.stdin.readlines()]
index, steps, length = 0, 0, len(offsets)

while(0 <= index < length):
    offsets[index] += 1
    index += offsets[index] - 1
    steps += 1

print(steps)