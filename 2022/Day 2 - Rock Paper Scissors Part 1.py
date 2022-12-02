#Finding the total points from a modified game of Rock Paper Scissors.

line = input().split()

points = 0

while(line):
    #Using ASCII values to get more understandable numbers, 1 for rock, 2 for paper, and 3 for scissors.
    #They are also 1-indexed to match the required values.
    opponent, you = ord(line[0]) - 64, ord(line[1]) - 87

    #A draw situation.
    if(opponent == you):
        points += 3 + you
    
    #A win situation(2 - 1, 3 - 2, 1 - 3)(see the mapped numbers).
    elif(you - opponent == 1 or you - opponent == -2):
        points += 6 + you
    
    #Whatever situation is left has to be a loss.
    else:
        points += you
    
    line = input().split()

print(points)