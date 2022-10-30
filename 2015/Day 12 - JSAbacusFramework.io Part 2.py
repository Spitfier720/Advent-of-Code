#Get the sum of all numbers in a JSON file that does not have "red" as a value.

import json

#Recursively find the total of all valid numbers.
def getValidTotal(jsonDoc):
    total = [0]

    #Getting all the dict totals in case one is invalid.
    dictStack = []

    isDict = isinstance(jsonDoc, dict)

    #Create new element for every dictionary.
    if(isinstance(jsonDoc, dict)):
        dictStack.append(0)
    
    for x in jsonDoc:
        #Dictionaries have a different method of processing as both their keys and values have to be evaluated.
        if(isDict):
            #Red is in our current value of our dictionary.
            if(jsonDoc[x] == "red"):
                dictStack[-1] = 0
                break

            elif(isinstance(jsonDoc[x], int)):
                dictStack.append(dictStack.pop() + jsonDoc[x])
            
            elif(not isinstance(jsonDoc[x], str)):
                dictStack.append(dictStack.pop() + getValidTotal(jsonDoc[x]))

        #The code below looks pretty similar to the code above, unfortunately, there's no easy way to merge them together.
        else:
            if(isinstance(x, int)):
                #Although the if statements are a little repetitive, it's the only way I could forsee.
                if(dictStack):
                    dictStack.append(dictStack.pop() + x)
                
                else:
                    total[0] += x
            
            #Strings are skipped because they don't help with our total.
            elif(not isinstance(x, str)):
                if(dictStack):
                    dictStack.append(dictStack.pop() + getValidTotal(x))
                
                else:
                    total[0] += getValidTotal(x)
    
    #We add onto the second last element until we are no longer in a dictionary.
    if(len(dictStack) >= 2):
        dictStack.append(dictStack.pop() + dictStack.pop())
    
    #If this is the last dictionary, add the total to the actual total
    elif(dictStack):
        total[0] += dictStack.pop()

    return total[0]

jsonDoc = json.load(open("JSONDocument.json", "r"))
print(getValidTotal(jsonDoc))