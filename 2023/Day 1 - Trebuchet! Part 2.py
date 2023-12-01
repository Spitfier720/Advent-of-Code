import sys

sum = 0
digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

for line in sys.stdin.readlines():
    newNum = ""
    firstNum, lastNum = (len(line), "0"), (-1, "0")

    # Find first and last occurences of valid digits to create our new number.
    for x in digits:
        if x in line:
            firstIndex, lastIndex = line.index(x), line.rindex(x)

            if(x == "one"):
                x = "1"
            elif(x == "two"):
                x = "2"
            elif(x == "three"):
                x = "3"
            elif(x == "four"):
                x = "4"
            elif(x == "five"):
                x = "5"
            elif(x == "six"):
                x = "6"
            elif(x == "seven"):
                x = "7"
            elif(x == "eight"):
                x = "8"
            elif(x == "nine"):
                x = "9"

            if(firstNum[0] > firstIndex):
                firstNum = (firstIndex, x)
            
            if(lastNum[0] < lastIndex):
                lastNum = (lastIndex, x)
    
    newNum = firstNum[1] + lastNum[1]
    
    sum += int(newNum)

print(sum)