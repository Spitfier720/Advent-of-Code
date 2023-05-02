#Finding the minimum and maximum of several lists.

row = list(map(int, input().split()))
checksum = 0

while(row):
    checksum += max(row) - min(row)
    row = list(map(int, input().split()))

print(checksum)