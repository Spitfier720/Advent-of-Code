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

    def getResult(self):
        return self.__circList[0] * self.__circList[1]

lengths = list(map(int, input().split(",")))

#hashList = HashList(5)
hashList = HashList(256)

for x in lengths:
    hashList.operate(x)

print(hashList.getResult())