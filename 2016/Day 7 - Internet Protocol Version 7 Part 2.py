#Checking for strings with an "aba" pattern inside of them, a variation of the "abba" pattern.

nssl = 0
ipv7 = input()

while(ipv7):
    isHypernet = False
    patterns = {}
    i = 2

    while(i < len(ipv7)):
        if(ipv7[i - 2] == ipv7[i] and ipv7[i - 1] != ipv7[i]):
            if(ipv7[i - 1] + ipv7[i] + ipv7[i - 1] in patterns and (not isHypernet) in patterns[ipv7[i - 1] + ipv7[i] + ipv7[i - 1]]):
                nssl += 1
                break
            
            else:
                patterns.setdefault(ipv7[i - 2: i + 1], set()).add(isHypernet)

        #Adding 4 to our index when we enter or leave hypernet characters, since brackets should not count towards our "abba" pattern.
        if(ipv7[i] == "["):
            isHypernet = True
            i += 2
        
        elif(ipv7[i] == "]"):
            isHypernet = False
            i += 2
        
        i += 1
    
    ipv7 = input()

print(nssl)