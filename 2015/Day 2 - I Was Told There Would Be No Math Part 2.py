dimensions = input()
fullOrder = []

while(dimensions):
    fullOrder.append(dimensions)
    dimensions = input()

totalRibbon = 0

for order in fullOrder:
    length, width, height = map(int, order.split("x"))
    totalRibbon += min(2 * length + 2 * width, 2 * width + 2 * height, 2 * length + 2 * height) \
        + length * width * height

print(totalRibbon)