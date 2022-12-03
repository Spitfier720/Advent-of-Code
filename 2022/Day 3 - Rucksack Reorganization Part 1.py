#Finding a matching character between a list of pairs of strings.

line = input()
priorities = 0

while(line):
    #Split the string into half and assign it to variables.
    left, right = line[:len(line) // 2], line[len(line) // 2:]

    #Finding which character is in both strings, since we know there will only be one.
    for x in left:
        #Character is in the right half.
        if(x in right):
            #We check if the chracter is uppercase, take the ascii value and subtract 64 to 1-index, 
            #then add 26 to get the priority.
            if(x.isupper()):
                priorities += ord(x) - 38
            
            #The character must be lowercase, so we take the ascii value and subtract 96 to 1-index.
            else:
                priorities += ord(x) - 96
            
            #We need to break since our character can happen multiple times in both strings.
            break
    
    line = input()

print(priorities)