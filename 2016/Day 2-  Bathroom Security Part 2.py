#Moving around a keypad to find the password.

line = input()

#This keypad is different due to the irregular grid, so it's padded with zeros, which act as out of
keypad = [
    ["0", "0", "1", "0", "0"],
    ["0", "2", "3", "4", "0"],
    ["5", "6", "7", "8", "9"],
    ["0", "A", "B", "C", "0"],
    ["0", "0", "D", "0", "0"]
]

#Translating the directions in our input to coordinate changes.
directions = {
    "U": (-1, 0),
    "R": (0, 1),
    "D": (1, 0),
    "L": (0, -1)
}

x, y = 2, 0
code = ""

while(line):
    #For each direction per line, make sure that the direction doesn't go out of bounds.
    for d in line:
        if(0 <= x + directions[d][0] <= 4 and 0 <= y + directions[d][1] <= 4 and \
            keypad[x + directions[d][0]][y + directions[d][1]] != "0"):
            x += directions[d][0]
            y += directions[d][1]
    
    #Adding to the passcode.
    code += str(keypad[x][y])

    line = input()

print(code)