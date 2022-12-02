#Finding the total points from a modified game of Rock Paper Scissors.

line = input().split()

points = 0

while(line):
    #We need to lose.
    if(line[1] == "X"):
        #Find the character that is 1 less than what our opponent picked, which would loop around in case they picked rock.
        '''Formula: 
        (ascii value - 'A' - 1(for getting the losing character) + 2(to prevent negatives))
        % 3(to loop larger values back around) + 1(1-indexing to get our final value)'''
        points += ((ord(line[0]) - 63) % 3) + 1
    
    #We need to draw.
    elif(line[1] == "Y"):
        #Add the character and 3.
        points += ord(line[0]) - 61
    
    #We need to win.
    else:
        #Find the character that is 1 more than our opponent, and add that by 6.
        '''Formula:
        (ascii value - 'A' + 1(to get the winning character)) % 3(to loop larger values back around)
        + 1(1-indexing to get the final value) + 6(the amount of points we get when we win)
        If you noticed, we don't have to add or subtract anything because we never reach any negatives with our formula.'''
        points += (ord(line[0]) - 64) % 3 + 7

    line = input().split()

print(points)