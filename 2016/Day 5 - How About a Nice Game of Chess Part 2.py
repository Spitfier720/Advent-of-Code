#Brute forcing hashes eight times. The pinnacle of problem-solving.

import hashlib, time

index = 0
password = [" " for x in range(8)]
charsFound = 0
loadingSymbols = ["/", "-", "\\", "|"]
doorID = input()

print("Input recieved. Processing...")
time.sleep(0.5)

while(charsFound != 8):
    encryption = hashlib.md5((doorID + str(index)).encode()).hexdigest()
    
    #Another thing is that the hashes can lead to indices in which there already is a character inside, which should then be ignored.
    if(encryption[:5] == "00000" and encryption[5].isnumeric() and 0 <= int(encryption[5]) <= 7 and password[int(encryption[5])] == " "):
        password[int(encryption[5])] = encryption[6]
        charsFound += 1

    #Bonus marks for cinematic decryption.
    #I made the mod number big so that the loading animation doesn't go too fast, it can be modified as you wish.
    if(index % 15625 == 0):
        print("Finding password: [" + "█" * charsFound + "" + loadingSymbols[index % 4] +  "." * (7 - charsFound) + "]", end = "")
        print("\r", end = "")

    index += 1

#Adding two spaces at the end to clear everything from the last line, as since this line is shorter so it won't cover everything.
print("Your password is: " + "".join(password) + "  ")