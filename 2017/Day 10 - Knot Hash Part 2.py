#Implementing a small new type of hashing.

class HashList:
    def __init__(self, size):
        self.__size = size
        self.__circList = [x for x in range(size)]
        self.__skipSize = 0
        self.__index = 0
    
    def operate(self, length):
        lengthNums = self.__circList[self.__index: min(self.__size, self.__index + length)] + \
                  self.__circList[0: max(0, length - (self.__size - self.__index))]
        lengthNums.reverse()

        for x in lengthNums:
            self.__circList[self.__index] = x
            self.__index = (self.__index + 1) % self.__size

        self.__index = (self.__index + self.__skipSize) % self.__size
        self.__skipSize += 1

    def __denseHash(self, blockNum):
        xor = self.__circList[16 * blockNum]

        for x in range(1, 16):
            xor ^= self.__circList[x + (16 * blockNum)]
        
        return hex(xor)

    def hash(self):
        knotHashString = ""

        for x in range(16):
            blockHash = self.__denseHash(x)[2:]
            knotHashString += "0" + blockHash if len(blockHash) == 1 else blockHash
        
        return knotHashString

lengths = list(map(ord, input().strip())) + [17, 31, 73, 47, 23]

#hashList = HashList(5)
hashList = HashList(256)

for i in range(64):
    for x in lengths:
        hashList.operate(x)

print(hashList.hash())