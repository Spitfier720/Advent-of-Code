#Finding the total distances travelled with different cycles of running and resting, at once.

speeds, distances = [], []
numReindeers = 0

line = input()

while(line):
    line = line.split()

    #Storing the speed, the running times, and the full cycle time.
    speeds.append(((int(line[6]), int(line[13]) + int(line[6])), int(line[3])))
    distances.append(0)

    numReindeers += 1
    line = input()

#The range is adjusted so that the seconds are 1-indexed, and therefore are easier to read.
for x in range(1, 2504):
    for y in range(numReindeers):
        if(0 < x % speeds[y][0][1] <= speeds[y][0][0]):
            distances[y] += speeds[y][1]

print(max(distances))