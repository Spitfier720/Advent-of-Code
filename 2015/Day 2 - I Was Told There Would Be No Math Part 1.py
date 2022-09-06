# Calculating surface areas to wrap boxes, with a little extra buffer

dimensions = input()
fullOrder = []

#Account for multi-line input
while(dimensions):
    fullOrder.append(dimensions)
    dimensions = input()

totalWrappingPaper = 0

#Calculate surface area(and buffer) and add it to the total
for order in fullOrder:
    length, width, height = map(int, order.split("x"))
    totalWrappingPaper += 2 * length * width + 2 * width * height + 2 * length * height \
         + min(length * width, width * height, length * height)
    
print(totalWrappingPaper)