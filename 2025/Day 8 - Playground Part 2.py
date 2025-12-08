import math
import os

class Day8:
    def __init__(self):
        self.__coords = []
        self.__distances = {}
        self.__circuits = []

    def addCoords(self, x, y, z):
        for c in self.__coords:
            self.__distances[((c), (x, y, z))] = math.sqrt((c[0] - x)**2 + (c[1] - y)**2 + (c[2] - z)**2) # Straight-line distance between all points
    
        self.__coords.append((x, y, z))
    
    def connectBoxes(self):
        sortedDistances = list(sorted(self.__distances.items(), key=lambda x: x[1]))
        index = 0

        while(True):
            box1, box2 = sortedDistances[index][0]
            box1CircuitIndex, box2CircuitIndex = -1, -1

            if(not self.__circuits):
                self.__circuits.append({box1, box2})
                index += 1
                continue

            for i in range(len(self.__circuits)): # Find circuit indices of both boxes
                if(box1 in self.__circuits[i]):
                    box1CircuitIndex = i
                
                if(box2 in self.__circuits[i]):
                    box2CircuitIndex = i
            
            if(box1CircuitIndex == -1 and box2CircuitIndex == -1):
                self.__circuits.append({box1, box2})
            
            elif(box1CircuitIndex != -1 and box2CircuitIndex == -1):
                self.__circuits[box1CircuitIndex].add(box2)
            
            elif(box1CircuitIndex == -1 and box2CircuitIndex != -1):
                self.__circuits[box2CircuitIndex].add(box1)
            
            else:
                if(box1CircuitIndex != box2CircuitIndex): # Only deal with merging if they are in different circuits
                    self.__circuits[box1CircuitIndex] = self.__circuits[box1CircuitIndex].union(self.__circuits[box2CircuitIndex])
                    del self.__circuits[box2CircuitIndex]
        
            if(len(self.__circuits) == 1 and len(self.__circuits[0]) == len(self.__coords)): # All boxes are now connected
                return box1[0] * box2[0]
            
            index += 1


scriptDir = os.path.dirname(__file__)
filePath = os.path.join(scriptDir, f"Day 8 Inputs.txt")
with open(filePath, "r") as f:
    lines = f.readlines()

day8 = Day8()
i = 1

for line in lines:
    if(line.strip() == "---"): # End of input, reset program
        print(f"Iteration {i}'s product of the x-coordinates of the last junction boxes to connect to make a full circuit: {day8.connectBoxes()}")
        
        day8 = Day8()
        i += 1

    else:
        x, y, z = map(int, line.strip().split(","))
        day8.addCoords(x, y, z)