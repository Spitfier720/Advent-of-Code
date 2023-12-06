import sys

time = int("".join(sys.stdin.readline().split()[1:]))
dist = int("".join(sys.stdin.readline().split()[1:]))
product = 1

for j in range(time + 1):
    if(j * (time - j) > dist):
        product *= (time - j) - j + 1
        break

print(product)