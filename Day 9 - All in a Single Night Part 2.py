#Finding the longest path that connects all cities exactly once.

#Find the longest path starting from a given root, using DFS.
def rootPath(graph, root, visited, length, maxLength):
    visited.add(root)

    #Base case: When we have found a path that visits all cities exactly once
    if(len(visited) == len(graph)):
        maxLength = max(maxLength, length)
        return maxLength

    #Try all possible paths from our root
    for node in graph[root]:
        if(node[0] not in visited):
            maxLength = rootPath(graph, node[0], visited, length + node[1], maxLength)
            visited.remove(node[0])
    
    #If no valid path exists, this will return 0, which will not affect the longest path at all.
    return maxLength

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

#Setting shortestPath to 0 so that we can accurately find the longest path.
shortestPath = 0

#Since Santa can start in any city, any city is fair game for it to have the longest valid path.
for city in cities:
    shortestPath = max(shortestPath, rootPath(cities, city, set(), 0, 0))

print(shortestPath)