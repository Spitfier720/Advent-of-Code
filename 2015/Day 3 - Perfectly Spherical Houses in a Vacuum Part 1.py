#According to eggnog-induced directions, we'll find out how many houses get presents

drunkDirections = input()

#Creating Santa's position and a set to record all the new positions
xCoord = 0
yCoord = 0
houseCoords = set()

#Convert directions to something the program can use
convertDirs = {"^": (0, 1), ">": (1, 0), "v": (0, -1), "<": (-1, 0)}

giftedHouses = 0

for drunkDirection in drunkDirections:
    xChange, yChange = convertDirs[drunkDirection]
    xCoord += xChange; yCoord += yChange

    if((xCoord, yCoord) not in houseCoords):
        giftedHouses += 1
        houseCoords.add((xCoord, yCoord))

print(giftedHouses)