#Finding when a number in a spiral pattern is bigger than our given number.
#For reference, our spiral pattern looks as follows:
'''
147  142  133  122   59
304    5    4    2   57
330   10    1    1   54
351   11   23   25   26
362  747  806--->   ...
'''

class Spiral:
    def __init__(self):
        self.spiral = [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ]

        self.length = 3
        self.x, self.y = 1, 1
        self.direction = [0, 1] #Right

    def updateCoords(self):
        if(self.y == self.length - 1): #Reached right end
            if(self.x == 0): #Go left
                self.direction = [0, -1]
            
            elif (self.x == self.length - 1): #Resize, and direction will stay the same
                self.x += 1
                self.y += 1
                self.resize()
            
            else: #Go up
                self.direction = [-1, 0]
        
        elif(self.y == 0): #Reached left end
            if(self.x == self.length - 1): #Go right
                self.direction = [0, 1]
            
            else: #Go down
                self.direction = [1, 0]

        self.x += self.direction[0]
        self.y += self.direction[1]

    #Adding the next element by adding all its adjacent values.
    def addNext(self):
        self.updateCoords()
        newVal = 0

        for i in range(-1, 2):
            for j in range(-1, 2):
                if((i == 0 and j == 0) or \
                   not (0 <= self.x + i < self.length) or \
                    not (0 <= self.y + j < self.length)): continue

                newVal += self.spiral[self.x + i][self.y + j]
        
        self.spiral[self.x][self.y] = newVal
        return newVal

    #Instead of adding to our 2d list one by one, assuming that it must be a square list makes it more easier to handle.
    def resize(self):
        self.length += 2

        newSpiral = [[0 for x in range(self.length)] for y in range(self.length)]

        for x in range(1, self.length - 1):
            for y in range(1, self.length - 1):
                newSpiral[x][y] = self.spiral[x - 1][y - 1]
        
        self.spiral = list(newSpiral)

number = int(input())
spiral = Spiral()
curElement = spiral.addNext()

while(curElement < number):
    curElement = spiral.addNext()

print(curElement)