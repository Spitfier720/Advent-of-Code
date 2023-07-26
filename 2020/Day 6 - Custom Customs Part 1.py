#Finding the number of unique characters from multiple lines, really just a data structure problem.

import sys

ans = set()
sum = 0

for x in sys.stdin.readlines():
    if(x != "\n"):
        ans.update(x.strip()) #Get rid of the newline character.
    
    else:
        sum += len(ans)
        ans.clear()

print(sum + len(ans)) #Get the last group's results to get the right answer.