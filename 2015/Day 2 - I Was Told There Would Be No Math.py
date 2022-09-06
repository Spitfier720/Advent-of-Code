#How much ribbon do we need to wrap around our present, and make a flashy little bow?

dimensions = input()
fullOrder = []

#Account for multi-line input
while(dimensions):
    fullOrder.append(dimensions)
    dimensions = input()

totalRibbon = 0

#Adding the calculation for each box to the total, one by one
for order in fullOrder:
    length, width, height = map(int, order.split("x"))
    totalRibbon += min(2 * length + 2 * width, 2 * width + 2 * height, 2 * length + 2 * height) \
        + length * width * height

print(totalRibbon)