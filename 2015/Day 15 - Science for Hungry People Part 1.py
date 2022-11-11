#Finding the best ingredient mixture that leads to the highest total product.

#Finding the highest product through recursion and brute force.
def highestScore(properties, numTsp, numIngr, amounts, maxProduct):
    #If our ingredient is the last ingredient, then we already know how much of it we need to add.
    if(numIngr == 1):
        amounts[len(amounts) - numIngr] = numTsp
        return max(maxProduct, getIngrTotal(properties, amounts, len(amounts)))
    
    #Otherwise, get every combination possible.
    for x in range(0, numTsp + 1):
        #The amounts are 1-indexed, because it's more practical.
        amounts[len(amounts) - numIngr] = x
        maxProduct = highestScore(properties, numTsp - x, numIngr - 1, amounts, maxProduct)

        #There is no need to revert the changes made to amounts, since they will eventually be replaced for new combinations.
    
    return maxProduct

#Finding the product of a mixture of ingredients.
def getIngrTotal(properties, amounts, numIngr):
    totalProduct = 1

    #This for loop is to iterate and keep track of each property.
    for i in range(4):
        
        curTotal = 0
        for x in range(numIngr):
            #Multiply the current property with the current amount of that ingredient.
            curTotal += properties[x][i] * amounts[x]
        
        #If the current total is not positive, then the product will not be positive.
        if(curTotal <= 0):
            return 0
        
        totalProduct *= curTotal
    
    return totalProduct

line = input()

properties = []
amounts = []
numIngredients = 0

while(line):
    line = line.split()

    #Taking the relavant ingredient property values into our list.
    properties.append(tuple(int(line[x].strip(",")) for x in range(2, 9, 2)))
    amounts.append(0)
    numIngredients += 1

    line = input()

print(highestScore(properties, 100, numIngredients, amounts, 0))