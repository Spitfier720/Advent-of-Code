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
        else:
            try:
                match x:
                    case "byr": #Birth year must be between 1920 and 2002.
                        if(not (1920 <= int(passport[x]) <= 2002)): return False
                    
                    case "iyr": #Issue year must be between 2010 and 2020.
                        if(not (2010 <= int(passport[x]) <= 2020)): return False
                    
                    case "eyr": #Expiry year must be between 2020 and 2030.
                        if(not (2020 <= int(passport[x]) <= 2030)): return False
                    
                    case "hgt": #Height must be between 150cm and 193cm, or 59in and 76in.
                        if(passport[x][-2:] == "cm"):
                            if(not (150 <= int(passport[x][:-2]) <= 193)): return False
                        
                        elif(passport[x][-2:] == "in"):
                            if(not (59 <= int(passport[x][:-2]) <= 76)): return False
                        
                        else:
                            return False
                    
                    case "hcl": #Hair color must be a valid six character hex number with a # sign at the beginning.
                        if(passport[x][0] != "#"): return False
                        if(len(passport[x]) != 7): return False
                        int(passport[x][1:], 16) #This may raise ValueError, which is fine
                    
                    case "ecl": #Eye color must be one of the following colors in the set below.
                        if(passport[x] not in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}): return False
                    
                    case "pid": #Passport ID must be a 9 digit number, allowing for leading zeros.
                        if(len(passport[x]) != 9 or not passport[x].isdigit()): return False
            
            except ValueError: #If int conversions give an error, the passport is also invalid.
                return False
    
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