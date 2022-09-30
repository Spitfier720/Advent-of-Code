#Find the next valid password starting from Santa's old password

#Find if our new password is valid.
def isValid(string):
    if(any(x in string for x in "iol")):
        return False
    
    #Creating two character placeholders which will be used to test the consecuitive substring condition.
    pastPastChar, pastChar = '', ''
    #Creating two booleans to account for the other two conditions we'll be testing.
    hasStraight, pairCount = False, 0

    for char in string:
        #We need to make sure the pairs don't overlap.
        #This will get the maximum possible amount of pairs, even though it's a greety-like algorithm(e.g. "gggggggh").
        if(pastChar == char and pastChar != pastPastChar):
            pairCount += 1
        
        #If there is a three character straight, the ASCII values should only differ by 1.
        #We, of course, also need to make sure that they aren't empty(e.g. the early iterations).
        if(pastPastChar and pastChar and ord(char) - ord(pastChar) == ord(pastChar) - ord(pastPastChar) == 1):
            hasStraight = True

        pastPastChar = pastChar
        pastChar = char
    
    return True if hasStraight and pairCount >= 2 else False

#Increment the string by 1, like a base 26 number.
def increment(string):
    for x in range(7, 0, -1):
        #Incrementing the letter by 1.
        string[x] = chr(ord(string[x]) + 1)

        #Dealing with regrouping.
        if(string[x] == '{'):
            string[x] = 'a'
        
        else:
            break
    
    return string

password = list(input())

#Due to another expiry, we must do this twice.
for x in range(2):
    #This is under the assumption that we will find a valid password before we reach the end combination of letters("zzzzzzzz")
    while(not isValid(password)):
        password = increment(password)
    
    #Preventing the first valid password from becoming the answer.
    if(x == 0):
        password = increment(password)

#Since we modified our input to be a list, we need to turn it back into a string before outputting.

print("".join(password))