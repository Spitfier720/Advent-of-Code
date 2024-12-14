import sys

robots = []

numSeconds = 100
gridHeight, gridWidth = 103, 101

for line in sys.stdin.readlines():
    line = line.strip().split()

    pos = tuple(map(int, line[0].split("=")[1].split(",")))[::-1]
    vel = tuple(map(int, line[1].split("=")[1].split(",")))[::-1]

    newX = (pos[0] + (vel[0] * numSeconds)) % (gridHeight * (1 if vel[0] >= 0 else -1))
    newY = (pos[1] + (vel[1] * numSeconds)) % (gridWidth * (1 if vel[1] >= 0 else -1))

    robots.append(
        (
            newX + (gridHeight if (vel[0] < 0 and newX < 0) else 0), 
            newY + (gridWidth if (vel[1] < 0 and newY < 0) else 0)
        )
    )

quadrants = [0, 0, 0, 0]

for r in robots:
    if(r[0] == gridHeight // 2 or r[1] == gridWidth // 2):
        continue

    quadrants[(0 if r[0] < gridHeight // 2 else 2) + (0 if r[1] < gridWidth // 2 else 1)] += 1

prod = 1

for q in quadrants:
    prod *= q

print(prod)