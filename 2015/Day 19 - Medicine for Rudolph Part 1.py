#Replacing elements with other elements or compounds to get new results.

line = input().strip("\n").split(" => ")
replacements = {}

#The replacement will only have two molecules.
while(len(line) == 2):
    replacements.setdefault(line[0], set()).add(line[1])
    line = input().strip("\n").split(" => ")

compound = input()

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

                if(changedMolecule not in newMolecules):
                    newMolecules.add(changedMolecule)
    
    #Moving on to the next character to find all possible elements to replace from there.
    startIndex += 1

print(len(newMolecules))