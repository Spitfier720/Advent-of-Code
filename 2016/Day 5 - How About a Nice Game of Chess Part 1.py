#Brute forcing hashes eight times. The pinnacle of problem-solving.

import hashlib, time

index = 0
password = ""
charsFound = 0
loadingSymbols = ["/", "-", "\\", "|"]
doorID = input()

print("Input recieved. Processing...")
time.sleep(0.5)

while(len(password) != 8):
    encryption = hashlib.md5((doorID + str(index)).encode()).hexdigest()
    
    if(encryption[:5] == "00000"):
        password += encryption[5]
        charsFound += 1
    
    #Bonus marks for cinematic decryption.
    #I made the mod number big so that the loading animation doesn't go too fast, it can be modified as you wish.
    if(index % 15625 == 0):
        print("Finding password: [" + "█" * charsFound + "" + loadingSymbols[index % 4] +  "." * (7 - charsFound) + "]", end = "")
        print("\r", end = "")

    index += 1

#Adding two spaces at the end to clear everything from the last line, as since this line is shorter so it won't cover everything.
print("Your password is: " + "".join(password) + "  ")