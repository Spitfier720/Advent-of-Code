#Finding valid triangles through side length.

numValid = 0

line = input()

while(line):
    #Getting the side lengths through splitting by spaces.
    sides = sorted(list(map(int, line.split())), reverse = True)

    #Only when the longest side is smaller than the sum of the other two is it a valid triangle.
    if(sides[0] < sides[1] + sides[2]):
        numValid += 1
    
    line = input()

print(numValid)