#Finding the shortest path that connects all cities exactly once.

#Find the shortest path starting from a given root, using DFS.
def rootPath(graph, root, visited, length, minLength):
    visited.add(root)

    #Base case: When we have found a path that visits all cities exactly once
    if(len(visited) == len(graph)):
        minLength = min(minLength, length)
        return minLength

    #Try all possible paths from our root
    for node in graph[root]:
        if(node[0] not in visited):
            minLength = rootPath(graph, node[0], visited, length + node[1], minLength)
            visited.remove(node[0])
    
    #If no valid path exists, this will return infinity, which will not affect the shortest path at all.
    return minLength

cities = dict()
distance = input()

#Better to modify the input as it comes in rather than storing it and doing it later, it's faster that way.
while(distance):
    distance = distance.split()
    #Create a new set if the key doesn't exist, otherwise return the existing value. The set is added to either way.
    #We are creating our "graph" using an adjacency dictionary, including the weights with the appropriate adjacent edge.
    cities.setdefault(distance[0], set()).add((distance[2], int(distance[4])))
    cities.setdefault(distance[2], set()).add((distance[0], int(distance[4])))

    distance = input()

#This is considered as the largest number value(though it's not really a value), so we can accurately find the smallest value
shortestPath = float('inf')

#Since Santa can start in any city, any city is fair game for it to have the shortest valid path.
for city in cities:
    shortestPath = min(shortestPath, rootPath(cities, city, set(), 0, float('inf')))

print(shortestPath)