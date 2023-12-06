import sys

times = list(map(int, sys.stdin.readline().split()[1:]))
dists = list(map(int, sys.stdin.readline().split()[1:]))
product = 1

for i in range(len(times)):
    for j in range(times[i] + 1):
        if(j * (times[i] - j) > dists[i]):
            product *= (times[i] - j) - j + 1
            break

print(product)