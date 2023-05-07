#Building a tree to find the root node.

class Tree:
    def __init__(self):
        self.__nodes = {}
    
    def add(self, value, outEdges):
        self.__nodes[value] = self.__nodes.setdefault(value, 0)

        for x in outEdges:
            self.__nodes[x] = self.__nodes.setdefault(x, 0) + 1
    
    def findRoot(self):
        for x in self.__nodes:
            if(self.__nodes[x] == 0): return x

program = input().split()
tree = Tree()

while(program):
    name = program[0]
    outEdges = []
    
    if(len(program) > 2):
        outEdges = [x.strip(",") for x in program[3:]]
    
    tree.add(name, outEdges)
    program = input().split()

print(tree.findRoot())