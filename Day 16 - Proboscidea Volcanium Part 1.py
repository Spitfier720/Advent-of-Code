#Finding the path that allows the highest pressure to be released.

#Getting the best path to release the most pressure.
def optimalPath(graph, start, distances):
    minutes = 0
    totalPressure = 0
    pressurePerMin = 0
    opened = set()

    while(minutes < 30):
        #We have opened all pumps, add the rest of the pressure released and return the total.
        if(len(opened) == len(distances["AA"])):
            totalPressure += pressurePerMin * (30 - minutes)
            return totalPressure

        potentials = {}
        maxDist = sorted(list(distances[start].items()), key = lambda x: x[1], reverse = True)[0][1] + 1

        #Returning the potential pressure lost if we headed directly to each of the other pumps.
        for x in distances[start]:
            if(x not in opened):
                potentials[x] = (maxDist - distances[start][x]) * graph[x][0]
        
        #Getting our optimal move from the most pressure released in the given time.
        optimalMove = sorted(list(potentials.items()), key = lambda x: x[1], reverse = True)[0]
        
        #Just in case we can't get to all the pumps in time.
        timeChange = min(distances[start][optimalMove[0]] + 1, 30 - minutes)

        #Update the function values based on our optimal move.
        minutes += timeChange
        totalPressure += pressurePerMin * timeChange + graph[optimalMove[0]][0]
        pressurePerMin += graph[optimalMove[0]][0]
        opened.add(optimalMove[0])

        #"Move" ourself to the pump.
        start = optimalMove[0]
    
    return totalPressure

#Getting the distances from a starting point to several endpoints.
def bfs(graph, start, ends):
    queue = [(0, start)]
    visited = {start}

    while(queue):
        steps, pump = queue.pop(0)

        #Found an endpoint.
        if(pump in ends):
            ends[pump] = steps

        for x in graph[pump][1]:
            #The new point cannot have been visited before.
            if(x not in visited):
                queue.append((steps + 1, x))
                visited.add(x)
    
    return ends

line = input().split()
graph = {}

#A list of all the pumps that don't have a flow rate of 0.
workingPumps = []

while(line):
    #Basically just getting the important stuff out.
    graph[line[1]] = [int(line[4].split("=")[1].strip(";")), set(x.strip(",") for x in line[9:])]
    
    if(graph[line[1]][0] != 0):
        workingPumps.append(line[1])
    
    line = input().split()

#Starting off with the distances from the starting point to the working pumps.
distances = {
    "AA": bfs(graph, "AA", {x: 0 for x in workingPumps})
}

#Getting the distances from each working pump to all the others.
for x in workingPumps:
    tempList = list(workingPumps)
    tempList.remove(x)
    distances[x] = bfs(graph, x, {i: 0 for i in tempList})

print(optimalPath(graph, "AA", distances))