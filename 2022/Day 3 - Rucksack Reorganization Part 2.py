#Finding a matching character between a list of pairs of strings.

first = input()
priorities = 0

#We seee if the first line is empty, then it will ask for the second and third lines.
while(first):
    second, third = input(), input()

    #Checking the letter that is in all three strings.
    #Note that for both parts, the string size is small enough to do an O(n^2) solution.
    for x in first:
        if(x in second and x in third):
            #Getting the right priorities depending on the case of the character.
            if(x.isupper()):
                priorities += ord(x) - 38
            
            else:
                priorities += ord(x) - 96
            
            #We need to break since our character can happen multiple times in both strings.
            break
    
    first = input()

print(priorities)