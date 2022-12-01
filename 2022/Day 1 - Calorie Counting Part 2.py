#Finding the maximum integers through formatted input.

import sys

input = [x for x in sys.stdin.readlines()]

#We know that we have at least one reindeer, so we add an initial element to the list to prevent index errors.
calories = [0]

for calorie in input:
    if(calorie == "\n"):
        calories.append(0)
    
    else:
        #Take out the last element, update it, and put it back in.
        calories.append(calories.pop() + int(calorie))

#We need to now find the sum of the top three calories.
print(sum(sorted(calories, reverse = True)[:3]))