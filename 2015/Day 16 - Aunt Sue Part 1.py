#Matching person data with sample data.

#Our sample data that we will match each aunt to.
tickerTape = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1
}

aunt = input()

#I make candidates a list, because due to the nature of the question it's possible there may be more than one candidate.
#The assumption is that there is only one match, but it's just a precaution.
candidates = []

while(aunt):
    aunt = aunt.split()
    isCandidate = True

    #Finding if each of the aunt's data matches with the sample data.
    for x in range(2, 7, 2):
        if(tickerTape[aunt[x].strip(":")] != int(aunt[x + 1].strip(","))):
            isCandidate = False
    
    if(isCandidate):
        candidates.append(int(aunt[1].strip(":")))
    
    aunt = input()

print(candidates)