#Decrypting a signal using repetition coding.

import sys

message = ""
signals = list(x for x in sys.stdin.readlines())

#Assuming that each signal is the same length.
#We also subtract 1 so we don't add a newline character that comes with every string.
for x in range(len(signals[0]) - 1):
    letterCount = {}

    for y in signals:
        letterCount[y[x]] = letterCount.setdefault(y[x], 0) + 1
    
    #A nice one-liner that gets the "min" key through the minimum value.
    message += min(letterCount, key = letterCount.get)

print(message)