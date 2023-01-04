#Moving around a keypad to find the password.

line = input()
keypad = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]    
]

#Translating the directions in our input to coordinate changes.
directions = {
    "U": (-1, 0),
    "R": (0, 1),
    "D": (1, 0),
    "L": (0, -1)
}

x, y = 1, 1
code = ""

while(line):
    #For each direction per line, make sure that the direction doesn't go out of bounds.
    for d in line:
        if(0 <= x + directions[d][0] <= 2 and 0 <= y + directions[d][1] <= 2):
            x += directions[d][0]
            y += directions[d][1]
    
    #Adding to the passcode.
    code += str(keypad[x][y])

    line = input()

print(code)