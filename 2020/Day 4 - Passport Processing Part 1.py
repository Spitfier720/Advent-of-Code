# Taking string input of IDs and checking to see if all the required fields exist.

import sys

#Takes the string input of the passport and returns a dictionary stating all of its fields and given values.
def processPassport(string):
    dct = {}

    for x in string.split():
        field = x.split(":")
        dct[field[0]] = field[1]
    
    return dct

#Finds if the passport is valid depending if all the required information is inside it.
def isValid(passport):
    FIELDS = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

    for x in FIELDS:
        if(x not in passport): return False
    
    return True

passport = ""
numValid = 0

for x in sys.stdin.readlines():
    if(x != "\n"): #Empty line signals end of passport.
        passport += x
    
    else:
        numValid += isValid(processPassport(passport))
        passport = ""

#Make sure to process the last passport.
print(numValid + isValid(processPassport(passport)))