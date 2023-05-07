#Building a tree with weights on each node to find an imbalanced node.

class Tree:
    def __init__(self):
        self.__nodes = {}
    
    def add(self, value, weight, outEdges):
        if(self.__nodes.get(value) == None):
            self.__nodes[value] = Node(weight)
        
        else:
            self.__nodes[value].setWeight(weight)

        for x in outEdges:
            if(self.__nodes.get(x) == None):
                self.__nodes[x] = Node()
            
            self.__nodes[x].addInDegree()
            self.__nodes[value].addOutEdges(x)
    
    def findRoot(self):
        for x in self.__nodes:
            if(self.__nodes[x].getInDegree() == 0): return x

    def __getTotalWeight(self, node):
        weight = node.getWeight()

        for x in node.getOutEdges():
            weight += self.__getTotalWeight(self.__nodes[x])
        
        return weight
    
    def properWeight(self, root):
        queue = [root]
        imbalancedNode = ""
        difference = 0

        while(queue):
            curNode = queue.pop(0)
            weights = {}

            for x in self.__nodes[curNode].getOutEdges():
                weights.setdefault(self.__getTotalWeight(self.__nodes[x]), []).append(x)
            
            if(len(weights) == 2):
                weight1, weight2 = list(weights.keys())

                if(len(weights[weight1]) == 1):
                    imbalancedNode = weights[weight1][0]
                    difference = weight1 - weight2

                else:
                    imbalancedNode = weights[weight2][0]
                    difference = weight2 - weight1
                
                queue.append(imbalancedNode)
            
            else:
                if(not imbalancedNode):
                    queue.extend(self.__nodes[curNode].getOutEdges())
        
        return self.__nodes[imbalancedNode].getWeight() - difference

class Node:
    def __init__(self, weight = 0):
        self.__inDegree = 0
        self.__weight = weight
        self.__outEdges = []
    
    def getWeight(self): return self.__weight
    def setWeight(self, weight): self.__weight = weight

    def getInDegree(self): return self.__inDegree
    def addInDegree(self): self.__inDegree += 1

    def getOutEdges(self): return self.__outEdges
    def addOutEdges(self, node): self.__outEdges.append(node)

program = input().split()
tree = Tree()

while(program):
    name, weight = program[0], int(program[1].strip("()"))
    outEdges = []
    
    if(len(program) > 2):
        outEdges = [x.strip(",") for x in program[3:]]
    
    tree.add(name, weight, outEdges)
    program = input().split()

print(tree.properWeight(tree.findRoot()))