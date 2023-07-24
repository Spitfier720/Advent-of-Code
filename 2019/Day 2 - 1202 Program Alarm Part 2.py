#Processing a list of integers with a predetermined code.

intcode = list(map(int, input().split(",")))

intcode[1], intcode[2] = 12, 2

i = 0

try:
    #Keep iterating and processing until the index goes out of bounds
    while(True):
        match intcode[i]:
            case 1:
                intcode[intcode[i + 3]] = intcode[intcode[i + 1]] + intcode[intcode[i + 2]]
            
            case 2:
                intcode[intcode[i + 3]] = intcode[intcode[i + 1]] * intcode[intcode[i + 2]]
            
            case 99:
                raise IndexError
        
        i += 4

except IndexError:
    print(intcode[0])