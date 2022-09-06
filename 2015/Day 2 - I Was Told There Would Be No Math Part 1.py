dimensions = input()
fullOrder = []

while(dimensions):
    fullOrder.append(dimensions)
    dimensions = input()

totalWrappingPaper = 0

for order in fullOrder:
    length, width, height = map(int, order.split("x"))
    totalWrappingPaper += 2 * length * width + 2 * width * height + 2 * length * height \
         + min(length * width, width * height, length * height)
    
print(totalWrappingPaper)