#Simulating a circuit to find out what value is passed to a specific wire(wire a)

import sys

#This is the function that will return the signal given to any given wire
#The function works through recursion, by finding the wire's input wire values over and over until we get a number.
def signal(circuit, letter, cache):
    #It's possible that a number is included in the bitwise operation, so this catches that
    #There are no numerical keys in the dictionary after all
    #This is our base case as well, seeing if the value is an integer
    if(letter.isdigit()):
        return int(letter)
    
    #Our cache parameter saves time, because wires can send their signal to several other ones which causes unnecessary lookups
    if(letter in cache):
        return cache[letter]

    print(letter, "=", circuit[letter])

    match len(circuit[letter]):
        #By far the hardest case to code, this signal will have either AND, OR, or the SHIFTs in it
        case 3:
            #Unfortunately, ternaries can only hold an if-else statement, and we have four if-conditions
            #They could also be an if-elif-else statement, but I just felt like making this more descipriptive and painful
            if(circuit[letter][1] == "AND"):
                cache[letter] = signal(circuit, circuit[letter][0], cache) & signal(circuit, circuit[letter][2], cache)
            
            if(circuit[letter][1] == "OR"):
                cache[letter] = signal(circuit, circuit[letter][0], cache) | signal(circuit, circuit[letter][2], cache)
            
            if(circuit[letter][1] == "LSHIFT"):
                cache[letter] = signal(circuit, circuit[letter][0], cache) << signal(circuit, circuit[letter][2], cache)
            
            if(circuit[letter][1] == "RSHIFT"):
                cache[letter] = signal(circuit, circuit[letter][0], cache) >> signal(circuit, circuit[letter][2], cache)

        #The signal is in the form NOT [wire], thanks to formatting
        case 2:
            #The 0xFFFF is there due to getting rid of two's complementing, and to keep it within 16 bits(0 - 65535)
            cache[letter] = ~(signal(circuit, circuit[letter][1], cache)) & 0xFFFF
        
        #The signal is a single value, which can unfortunately also be a wire
        case 1:
            cache[letter] = signal(circuit, circuit[letter][0], cache)
    
    return cache[letter]

#Good news! I learned a better way to account for multi-line input
#This requires an EOF to stop, which in layman's terms is a Ctrl + Z
connections = [x.strip() for x in sys.stdin.readlines()]
circuit = {}

#Build the circuit, I would have solved it in this same loop if I knew how
for connection in connections:
    connection = connection.split(" -> ")
    signalNum = connection[0].split()
    wire = connection[1]
    circuit[wire] = signalNum

circuit['b'] = [str(signal(circuit, 'a', dict()))]
print(signal(circuit, 'a', dict()))