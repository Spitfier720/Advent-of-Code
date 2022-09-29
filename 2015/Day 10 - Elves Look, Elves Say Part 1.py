#Find the length of a sequence of numbers after applying a look-and-say sequence 40 times.

digits = input()

for x in range(40):
    #Create a new string for the next iteration, a placeholder for the last digit, and a count to group consecuitive same digits
    newDigits, pastDigit, count = "", "", 0

    #Iterate through the digits and group them.
    for digit in digits:
        if(pastDigit != digit and pastDigit):
            newDigits += str(count) + pastDigit
            count = 1
        
        else:
            count += 1
        
        pastDigit = digit
    
    #Account for the last group which will not be caught by the for loop.
    newDigits += str(count) + pastDigit
    digits = newDigits

print(len(newDigits))