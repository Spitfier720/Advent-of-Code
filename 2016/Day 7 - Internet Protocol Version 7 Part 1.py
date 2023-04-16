#Checking for strings with an "abba" pattern inside of them, or the first two characters reversed is the last two characters.

ntls = 0
ipv7 = input()

while(ipv7):
    isHypernet = False
    isSnoopable = False
    i = 3

    while(i < len(ipv7)):
        #We need to check the whole string, since any "abba" pattern in the hypernet characters would make the whole ip non-snoopable.
        if(ipv7[i - 3] == ipv7[i] and ipv7[i - 2] == ipv7[i - 1] and ipv7[i - 1] != ipv7[i]):
            if(isHypernet):
                isSnoopable = False
                break

            isSnoopable = True

        #Adding 4 to our index when we enter or leave hypernet characters, since brackets should not count towards our "abba" pattern.
        if(ipv7[i] == "["):
            isHypernet = True
            i += 3
        
        elif(ipv7[i] == "]"):
            isHypernet = False
            i += 3
        
        i += 1

    ntls += isSnoopable #Boolean addition(since True = 1)
    ipv7 = input()

print(ntls)