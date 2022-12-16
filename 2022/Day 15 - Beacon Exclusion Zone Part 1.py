#Simulating a several signals' coverage until it hits a beacon.

line = input().split()
sensors = {}

while(line):
    #Getting the coordinates of the sensor and its closest beacon.
    sensors[(int(line[2].split("=")[1].strip(",")), int(line[3].split("=")[1].strip(":")))] = \
        (int(line[8].split("=")[1].strip(",")), int(line[9].split("=")[1].strip(":")))
    line = input().split()

#The row we want to see the signal coverage on.
row = 2000000
rowCoverage = set()

for s in sensors:
    #If the distance between the signal and beacon is less than the distance from the signal to our row.
    if(abs(sensors[s][1] - s[1]) + abs(sensors[s][0] - s[0]) >= abs(s[1] - row)):
        difference = abs(sensors[s][1] - s[1]) + abs(sensors[s][0] - s[0]) - abs(s[1] - row)
        rowCoverage.update(set(x for x in range(s[0] - difference, s[0] + difference + 1)))

notBeaconSpaces = 0
sensors, beacons = {x[1] for x in sensors if x[1] == row}, {sensors[x][1] for x in sensors if sensors[x][1] == row}

#Weeding out any spaces that are taken up by signals or beacons.
for y in rowCoverage:
    if(y not in sensors and y not in beacons):
        notBeaconSpaces += 1

print(notBeaconSpaces)