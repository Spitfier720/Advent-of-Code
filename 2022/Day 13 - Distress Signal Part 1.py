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
packets, curPacket = [], []

for line in rawPackets:
    #The line may just be a newline, so we add our pair of packets to the packet pile.
    if(not line):
        packets.append(curPacket)

        #Resetting the current packet because we are going to most likely add a new pair of packets.
        curPacket = []
        continue
    
    #Using a module to do this for us, because doing this manually would be a pain.
    curPacket.append(json.loads(line))

total = 0

for x in range(len(packets)):
    if(isInOrder(packets[x][0], packets[x][1])):
        total += x + 1

print(total)