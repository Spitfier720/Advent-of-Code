#Finding the maximum integer through formatted input.

line = input()

#We know that we have at least one reindeer, so we add an initial element to the list to prevent index errors.
curCalories, maxCalories = 0, 0

#-1 will be our terminating input.
while(line != "-1"):
    #Updating current counter.
    if(line):
        curCalories += int(line)

    #Setting the maximum calorie count and resetting the counter.
    else:
        maxCalories = max(maxCalories, curCalories)
        curCalories = 0
    
    line = input()

#Taking the last reindeer's calorie count into account as well.
maxCalories = max(maxCalories, curCalories)
print(maxCalories)