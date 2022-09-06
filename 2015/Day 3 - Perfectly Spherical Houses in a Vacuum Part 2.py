#Santa gets a robot to help! How many houses will they get now?

drunkDirections = input()

#Creating Santa and the robot's position and a set to record all the new positions
xCoordSanta, yCoordSanta, xCoordRobot, yCoordRobot = 0, 0, 0, 0
houseCoords = {(0, 0)}

#Convert directions into something the program can use
convertDirs = {"^": (0, 1), ">": (1, 0), "v": (0, -1), "<": (-1, 0)}

giftedHouses = 1
santasMove = True

#Go through each direction, and adjust the coordinates of either Santa or the robot accordingly
for drunkDirection in drunkDirections:
    xChange, yChange = convertDirs[drunkDirection]

    if(santasMove):
        xCoordSanta += xChange; yCoordSanta += yChange
    
    else:
        xCoordRobot += xChange; yCoordRobot += yChange
    
    if((xCoordSanta, yCoordSanta) not in houseCoords or (xCoordRobot, yCoordRobot) not in houseCoords):
        houseCoords.update([(xCoordSanta, yCoordSanta), (xCoordRobot, yCoordRobot)])
        giftedHouses += 1
    
    santasMove = not santasMove

print(giftedHouses)