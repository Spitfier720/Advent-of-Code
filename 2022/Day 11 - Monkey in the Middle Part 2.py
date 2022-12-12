#Simulating monkeys throwing items at each other in a predetermined way.

import sys

monkeys = {}

#Holding the product of all the divisors for each monkey.
productDivisors = 1

#Unforuntately, the monkey numbers don't have a pattern, so we need to keep track of our current monkey's number.
curMonkey = 0

decisions = [x.strip().split() for x in sys.stdin.readlines()]

for line in decisions:
    #Some of the lines are blank, so we need to account for that.
    if(not line):
        continue
    
    #New monkey is being added.
    if(line[0] == "Monkey"):
        curMonkey = int(line[1].strip(":"))
        monkeys[curMonkey] = {}

    #Get its starting item's worry numbers.
    if(line[0] == "Starting"):
        monkeys[curMonkey]["items"] = [int(x.strip(",")) for x in line[2:]]
        monkeys[curMonkey]["inspections"] = 0
    
    #Get the monkey's operation that it will perform on the worry number.
    elif(line[0] == "Operation:"):
        monkeys[curMonkey]["operation"] = line[3:]
    
    #The test for which monkey to pass it to, we only keep track of the number we need to divide it by.
    elif(line[0] == "Test:"):
        monkeys[curMonkey]["test"] = [int(line[3])]
        productDivisors *= monkeys[curMonkey]["test"][0]
    
    #Adding the monkeys to pass it to, so that the 2nd element is if the test is true and vice versa for the 3rd element.
    elif(line[0] == "If"):
        monkeys[curMonkey]["test"].append(int(line[5]))

for r in range(10000):
    for x in monkeys:
        while(monkeys[x]["items"]):
            #Pop the first element of each list of items(like a queue) until it is empty.
            item = monkeys[x]["items"].pop(0)

            _, operand, b = monkeys[x]["operation"]
            
            #"old" refers to our current item.
            if(b == "old"):
                b = item
            
            #The operands are only + and *, which are convienient.
            if(operand == "+"):
                item += int(b)
            
            else:
                item *= int(b)

            #Modding by the product of all the divisors, based on the Chinese Remainder Theorem.
            item %= productDivisors

            #Determining which monkey to pass it to.
            if(item % monkeys[x]["test"][0] == 0):
                monkeys[monkeys[x]["test"][1]]["items"].append(item)
            
            else:
                monkeys[monkeys[x]["test"][2]]["items"].append(item)
            
            #We need to keep track of how many times the monkey interacts with an item.
            monkeys[x]["inspections"] += 1

#Making a list and sorting the number of inspections a bit manually, since layered dictionaries aren't good for sorting.
sortedInspections = []

for x in monkeys:
    sortedInspections.append(monkeys[x]["inspections"])

sortedInspections.sort(reverse = True)
print(sortedInspections[0] * sortedInspections[1])