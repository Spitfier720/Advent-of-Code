import sys

sum = 0
list1, dict2 = [], {}

for line in sys.stdin.readlines():
    line = line.split()
    list1.append(int(line[0]))
    dict2[int(line[1])] = dict2.setdefault(int(line[1]), 0) + 1

for i in range(len(list1)):
    if(list1[i] in dict2):
        sum += list1[i] * dict2[list1[i]] 

print(sum)