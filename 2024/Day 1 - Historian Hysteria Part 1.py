import sys

sum = 0
list1, list2 = [], []

for line in sys.stdin.readlines():
    line = line.split()
    list1.append(line[0])
    list2.append(line[1])

list1.sort()
list2.sort()

for i in range(len(list1)):
    sum += abs(int(list1[i]) - int(list2[i]))

print(sum)