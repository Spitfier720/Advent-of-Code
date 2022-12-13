#Creating an algorithm that determins whether a generic list is larger than another.

import json, sys

def isInOrder(packet1, packet2):
    #Making sure to iterate through the largest list so that we can look for out of bounds.
    for x in range(max(len(packet1), len(packet2))):
        #First packet is out of bounds, packets are in order.
        if(x >= len(packet1)):
            return True

        #Second packet is out of bounds, packets are not in order.
        if(x >= len(packet2)):
            return False
        
        #If any of the elements are a list.
        if(isinstance(packet1[x], list) or isinstance(packet2[x], list)):
            #Converting any of the integers to lists.
            leftPacket, rightPacket = packet1[x], packet2[x]

            if(isinstance(leftPacket, int)):
                leftPacket = [leftPacket]
            
            if(isinstance(rightPacket, int)):
                rightPacket = [rightPacket]
            
            result = isInOrder(leftPacket, rightPacket)
            
            #Since we are working with booleans, we need to specify the return type that will keep the loop going.
            if(result != None):
                return result
        
        #Check if one is bigger than the other.
        else:
            if(packet1[x] > packet2[x]):
                return False
            
            elif(packet1[x] < packet2[x]):
                return True

rawPackets = [x.strip() for x in sys.stdin.readlines()]
packets = []

for line in rawPackets:
    #The line may just be a newline, so we add our packets to the packet pile.
    if(line):
        #Using a module to do this for us, because doing this manually would be a pain.
        packets.append(json.loads(line))
        continue

#As per the problem statment, and these will help give us our answer.
packets.extend([[[2]], [[6]]])

#Doing a very unoptimal bubble sort.
for i in range(len(packets)):
    #Since elements will bubble to the top, we can iterate through a smaller range every time.
    for x in range(len(packets) - 1 - i):
        #Using our old isInOrder function to determine whether or not we need to swap elements.
        if(not isInOrder(packets[x], packets[x + 1])):
            packets[x], packets[x + 1] = packets[x + 1], packets[x]

#1-indexing the indexes because an index of 0 just doesn't work for multiplication.
print((packets.index([[2]]) + 1) * (packets.index([[6]]) + 1))