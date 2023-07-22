#Simple math with multi-line input in one line.

import sys; print(sum((int(x) // 3) - 2 for x in sys.stdin.readlines()))