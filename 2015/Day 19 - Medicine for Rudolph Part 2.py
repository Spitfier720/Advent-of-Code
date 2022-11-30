#Replacing elements with other elements or compounds to get new results.

#Finding the number of steps to convert one compound into another using BFS.
def numSteps(start, end, replacements):
    queue = [(start, 0)]
    visited = set()
    steps = 0

    while(queue):
        item = queue.pop(0)
        curCompound, steps = item[0], item[1]

        if(curCompound == end):
            return steps
        
        newMolecules = getNewMolecules(curCompound, replacements, steps + 1, visited)

        queue.extend(newMolecules)
        visited.update(set(x[0] for x in newMolecules))
    
    #Really just an error code, based on the problem we shouldn't reach this line.
    return -1

#Finding all the replacements of a compound using the code from part 1.
def getNewMolecules(compound, replacements, step, visited):
    #Since compounds can have more than one letter, we slice the string using our startIndex.
    startIndex = 0

    newMolecules = set()

    #Since the letter at the starting index may not be part of any elements, the compound is iterated n^2 times.
    while(startIndex < len(compound)):
        #Since list slicing stops 1 before the end, the for loop is 1-indexed to match.
        for x in range(startIndex + 1, len(compound) + 1):
            if(compound[startIndex: x] in replacements):

                #Create a changed molecule and check if it exists already.
                for re in replacements[compound[startIndex: x]]:
                    changedMolecule = compound[:startIndex] + re + compound[x:]

                    #Checking if the molecule has been seen before at all, and adding the item to match the formatting.
                    if(changedMolecule not in newMolecules and changedMolecule not in visited):
                        newMolecules.add((changedMolecule, step))
        
        #Moving on to the next character to find all possible elements to replace from there.
        startIndex += 1

    return newMolecules

line = input().strip("\n").split(" => ")
replacements = {}

#The replacement will only have two molecules.
while(len(line) == 2):
    replacements.setdefault(line[0], set()).add(line[1])
    line = input().strip("\n").split(" => ")

compound = input()

print(numSteps("e", compound, replacements))