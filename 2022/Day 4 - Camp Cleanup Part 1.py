#Finding which ranges completely encompass another given range.

line = input().split(",")

count = 0

while(line[0]):
    first, second = list(map(int, line[0].split("-"))), list(map(int, line[1].split("-")))
    
    #Checking if the ranges are encompassing by seeing if either range has 
    #the first endpoint higher and the second endpoint lower than the other range.
    if((first[0] <= second[0] and first[1] >= second[1]) or (first[0] >= second[0] and first[1] <= second[1])):
        count += 1
    
    line = input().split(",")

print(count)