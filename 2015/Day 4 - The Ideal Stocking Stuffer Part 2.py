#Finding MD5 hashes startin with 5 zeros.

import hashlib

key = input()
answer = 0

#Brute force until solution is found
while(hashlib.md5((key + str(answer)).encode()).hexdigest()[:6] != "000000"):
    answer += 1

print(answer)