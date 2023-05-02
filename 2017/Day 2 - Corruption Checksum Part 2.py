#Finding the dividend and divisor of several lists.

row = list(map(int, input().split()))
checksum = 0

while(row):
    breakFlag = False

    for x in range(len(row)):
        for y in range(x + 1, len(row)):
            if(row[x] % row[y] == 0 or row[y] % row[x] == 0):
                checksum += max(row[x] // row[y], row[y] // row[x])
                breakFlag = True
                break
        
        if(breakFlag):
            break
    
    row = list(map(int, input().split()))

print(checksum)