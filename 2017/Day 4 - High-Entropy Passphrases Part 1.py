#Checking if a word already exists within a given phrase.

passphrase = input().split()
numValid = 0

while(passphrase):
    uniqueWords = set()
    isValid = True

    for x in passphrase:
        if(x in uniqueWords):
            isValid = False
            break
            
        uniqueWords.add(x)

    numValid += isValid
    passphrase = input().split()

print(numValid)