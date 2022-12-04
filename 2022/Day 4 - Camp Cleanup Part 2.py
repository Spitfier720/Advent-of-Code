#Finding which ranges overlap another given range.

line = input().split(",")

count = 0

while(line[0]):
    first, second = list(map(int, line[0].split("-"))), list(map(int, line[1].split("-")))
    
    #Checking if the ranges overlap by finding if either range encompasses the other range's endpoint.
    #We only have to make two expressions since the four endpoints can be shortened down into two.
    if((first[0] <= second[0] and first[1] >= second[0]) or (first[0] >= second[0] and first[0] <= second[1])):
        count += 1
    
    line = input().split(",")

print(count)