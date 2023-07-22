#Simulating chemical reactions using ASCII values.

#A doubly linked list with a head and a tail that will help us with performing the reactions.
class LinkedList:
    def __init__(self) -> None:
        self.__head = None
        self.__tail = None
        self.__curPointer = None
        self.__length = 0
    
    #Adds the element to the tail, making our new element the tail. In our situation, that is all we need for adding.
    def add(self, data):
        newUnit = Unit(data)
        
        if(not self.__head):
            self.__head = newUnit
            self.__tail = newUnit
            self.__curPointer = newUnit
        
        else:
            newUnit.prev = self.__tail
            self.__tail.next = newUnit
            self.__tail = newUnit
        
        self.__length += 1
    
    #Removes the element at the current pointer.
    def remove(self):
        if(not self.__curPointer.next and not self.__curPointer.prev): #Last element
            self.__curPointer = None
            self.__head = None
            self.__tail = None

        else:
            if(self.__curPointer.next and self.__curPointer.prev): #Element is in the middle
                self.__curPointer.next.prev = self.__curPointer.prev
                self.__curPointer.prev.next = self.__curPointer.next
                self.__curPointer = self.__curPointer.next

            elif(self.__curPointer.prev): #Element is the tail
                self.__curPointer.prev.next = None
                self.__tail = self.__curPointer.prev
                self.__curPointer = self.__tail
            
            else: #Element is the head
                self.__curPointer.next.prev = None
                self.__head = self.__curPointer.next
                self.__curPointer = self.__head

        self.__length -= 1
    
    #Making the chemical react to boil it down into its base form, and returns the number of units remaining.
    def execute(self):
        self.__curPointer = self.__head

        while(self.__curPointer and self.__curPointer.next):
            if(abs(ord(self.__curPointer.data) - ord(self.__curPointer.next.data)) == 32): #Reaction detected, remove both units.
                self.remove()
                self.remove()
                
                if(self.__curPointer and self.__curPointer.prev):
                    self.__curPointer = self.__curPointer.prev
                
            else:
                self.__curPointer = self.__curPointer.next

        return self.__length


#The elements in the linked list, with its respective data and two pointers to its previous and next elements, if applicable.
class Unit:
    def __init__(self, data):
        self.__data = data
        self.__prev = None
        self.__next = None
    
    #Getter and setter methods for the properties of this class.

    @property
    def data(self):
        return self.__data
    
    @property
    def prev(self):
        return self.__prev
    
    @prev.setter
    def prev(self, unit):
        self.__prev = unit

    @property
    def next(self):
        return self.__next
    
    @next.setter
    def next(self, unit):
        self.__next = unit

#polymer = input()
polymer = open("polymer.txt", "r").read()
letters = set() #Contains all the existing letters, ignoring case, in the input.
shortestLen = len(polymer)

for i in polymer:
    letters.add(i.lower())

for i in letters:
    linkedList = LinkedList()

    for j in polymer:
        if(j.lower() != i):
            linkedList.add(j)

    shortestLen = min(shortestLen, linkedList.execute())
    print("Letter " + i + " processed, the shortest possible length is now " + str(shortestLen)) #Progress bar.

print(shortestLen)