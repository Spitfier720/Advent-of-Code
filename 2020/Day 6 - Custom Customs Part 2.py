#Finding the number of characters that appear in every line for a group of lines, really just a data structure problem.

import sys

ans = set()
sum = 0
isEmpty = False # Determines if a group has no characters in common with each other.

for x in sys.stdin.readlines():
    if(x != "\n"):
        #Since we don't have any list of characters, we need to add them all first to find the characters remaining.
        if(not ans and not isEmpty):
            ans.update(x.strip()) #Get rid of the newline character.
        
        #Remove any character in the set that does not appear in the line of input.
        else:
            ans = ans.intersection(x.strip())

            if(not ans):
                isEmpty = True # Prevents any other characters in the group from already being added.
    
    else:
        sum += len(ans)
        ans.clear()
        isEmpty = False

print(sum + len(ans)) #Get the last group's results to get the right answer.