import sys

def getAntinodes(antennaLoc, length, width):
    antinodeLoc = set()

    for i in range(len(antennaLoc)):
        for j in range(i + 1, len(antennaLoc)):
            difference = (antennaLoc[j][0] - antennaLoc[i][0], antennaLoc[j][1] - antennaLoc[i][1])
            simulatedLoc = antennaLoc[i]

            while(inBounds(simulatedLoc, length, width)):
                antinodeLoc.add(simulatedLoc)
                simulatedLoc = (simulatedLoc[0] - difference[0], simulatedLoc[1] - difference[1])
            
            simulatedLoc = antennaLoc[i]
        
            while(inBounds(simulatedLoc, length, width)):
                antinodeLoc.add(simulatedLoc)
                simulatedLoc = (simulatedLoc[0] + difference[0], simulatedLoc[1] + difference[1])
    
    return antinodeLoc

def inBounds(loc, length, width):
    return 0 <= loc[0] < length and 0 <= loc[1] < width

length, width = 0, 0

antennae = {}

for line in sys.stdin.readlines():
    line = line.strip()

    for i in range(len(line)):
        if(line[i] != "."):
            antennae.setdefault(line[i], []).append((length, i))

    width = len(line)
    length += 1

unqLoc = set()

for key in antennae:
    unqLoc.update(getAntinodes(antennae[key], length, width))

print(len(unqLoc))