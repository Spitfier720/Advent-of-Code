#Building a tree to find the root node.

class Tree:
    def __init__(self):
        self.__nodes = {} #Holds the names of the nodes and their respective inDegrees.
    
    def add(self, value, outEdges):
        self.__nodes[value] = self.__nodes.setdefault(value, 0)

        for x in outEdges:
            self.__nodes[x] = self.__nodes.setdefault(x, 0) + 1
    
    #Finding the root by finding the node with no edges leading to it.
    def findRoot(self):
        for x in self.__nodes:
            if(self.__nodes[x] == 0): return x

program = input().split()
tree = Tree()

while(program):
    name = program[0]
    outEdges = []
    
    #Nodes can be a dead end
    if(len(program) > 2):
        outEdges = [x.strip(",") for x in program[3:]]
    
    tree.add(name, outEdges)
    program = input().split()

print(tree.findRoot())