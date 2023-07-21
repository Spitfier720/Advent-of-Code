#Sorting sleeping and waking events of different guards in chronological order,
#then finding the maximum amount of time slept by a guard and the time it sleeps the most.

from datetime import datetime

event = input()
events = [] #The list of sleeping, waking and starting shift events in chronological order.

while(event):
    #Using strptime for easier input processing.
    events.append((datetime.strptime(event[1:17], "%Y-%m-%d %H:%M"), event[19:]))
    event = input()

events.sort()

guards = {} #Lists the times where each guard is sleeping.
guardId = 0 #The current guard's ID.
asleepTime = 0 #Holding the time the guard falls asleep.

for e in events:
    match e[1][0]: #Primitive event handler.
        case "G": #Guard begins shift.
            #Initialize the guard with an array of 60 elements, for each minute of the hour they could be sleeping.
            guards.setdefault(int(e[1].split()[1].strip("#")), [0 for x in range(60)])
            guardId = int(e[1].split()[1].strip("#"))
            asleepTime = 0

        case "f": #Guard falls asleep.
            asleepTime = e[0].minute

        case "w": #Guard wakes up.
            for x in range(asleepTime, e[0].minute):
                guards[guardId][x] += 1

sleepiestGuard = max(list(guards.items()), key = lambda x: max(x[1]))[0]
sleepiestMinute = guards[sleepiestGuard].index(max(guards[sleepiestGuard][:60]))
print(sleepiestGuard * sleepiestMinute)