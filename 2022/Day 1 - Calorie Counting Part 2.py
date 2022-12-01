#Finding the maximum integer through formatted input.

line = input()

#We know that we have at least one reindeer, so we add an initial element to the list to prevent index errors.
curCalories = 0
caloriesCount = []

#-1 will be our terminating input.
while(line != "-1"):
    #Updating current counter.
    if(line):
        curCalories += int(line)

    #Adding the calorie count to a list, since sorting the list to get the top three is easier than holding three variables.
    else:
        caloriesCount.append(curCalories)
        curCalories = 0
    
    line = input()

#Taking the last reindeer's calorie count into account as well.
caloriesCount.append(curCalories)

#We need the sum of the topmost three calories.
print(sum(sorted(caloriesCount, reverse = True)[:3]))