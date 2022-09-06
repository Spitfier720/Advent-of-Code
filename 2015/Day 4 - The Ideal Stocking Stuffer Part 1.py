#Finding MD5 hashes starting with 5 zeros.

import hashlib

key = input()
answer = 0

#Brute force until solution is found
while(hashlib.md5((key + str(answer)).encode()).hexdigest()[:5] != "00000"):
    answer += 1

print(answer)