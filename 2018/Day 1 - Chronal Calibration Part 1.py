#Summing up numerous numbers in a single line of code.

import sys; print(sum(list(map(int, [x for x in sys.stdin.readlines()]))))