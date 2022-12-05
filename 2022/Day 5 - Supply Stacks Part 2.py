#Rearranging a list of stacks.

line = input()
stacks = {}

while(line):
    index = 0

    #Find all the crates in the string until we reach the end.
    #We keep our line of input a string to get the required indexes that will help us create the stacks.
    while(True):
        #Thanks to formatting, the index of the beginning of the crate("[") will always be divisible by 4.
        crateIndex = line.find("[", index)

        #Reached the end of string.
        if(crateIndex == -1):
            break
        
        #1-indexing our crates, and updating or creating our stack.
        stacks.setdefault((crateIndex // 4) + 1, []).insert(0, line[crateIndex + 1])

        #Since we know the index is divislbe by 4, we add that to the index to limit the range.
        index = crateIndex + 4

    line = input()

directions = input().split()

while(directions):
    amount, start, end = int(directions[1]), int(directions[3]), int(directions[5])

    #We can extract the list by slicing, which allows us to get rid of the for loop we had earlier.
    stacks[end].extend(stacks[start][len(stacks[start]) - amount:])
    del stacks[start][len(stacks[start]) - amount:]
    
    directions = input().split()

#We pop the last element from our stacks and print them, for my own ease.
for x in range(1, len(stacks) + 1):
    print(stacks[x].pop(), end = "")

#Because everything is better with a newline.
print()