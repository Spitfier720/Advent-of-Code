#Simple math with multi-line input, not sure how to do it in one line.

import sys

sum = 0

for x in sys.stdin.readlines():
    fuel = int(x)

    while((fuel // 3) - 2 > 0):
        fuel = (fuel // 3) - 2
        sum += fuel

print(sum)