#Creating a file system and finding the directories below a certain size.

#Getting the size of a directory, using recursion to account for the sizes of its subdirectories.
def getSum(dir, directory):
    #Our initial size will always be the first element due to our formatting.
    total = directory[dir][0]

    #Get the sum of each of the subdirectories.
    for x in range(1, len(directory[dir])):
        total += getSum(directory[dir][x], directory)
    
    return total

line = input().split()
directory = {}
curDir = "0"
dirCount = 1
dirPath = []

#We already have our initial path in here, because unlike the other directories, this one has never been seen before.
dirToInt = {("/",): "1"}

while(line):
    #Command prompt.
    if(line[0] == "$"):
        #cd is the only one that matters, ls is just an indication we can do without.
        if(line[1] == "cd"):
            #Simply because we don't want a directory of "..".
            #Also, our current directory will always be the most recently picked one, since ls is only called on new directories.
            if(line[2] != ".."):
                dirPath.append(line[2])
                curDir = dirToInt[tuple(dirPath)]
                directory[curDir] = [0]

            #We are going up a level, so we remove the last directory from our path.
            else:
                dirPath.pop()

    #The files in the current directory are being shown.
    else:
        #The file is an actual file with an integer size we can add to our directory's initial size.
        if(line[0].isdigit()):
            directory[curDir][0] += int(line[0])
        
        #The file is a directory which we append to the list for later.
        else:
            #Add to the number of directories that we have seen.
            dirCount += 1

            #Add the new directory to our directory path to ensure uniqueness, and save that path.
            dirPath.append(line[1])
            dirToInt[tuple(dirPath)] = str(dirCount)

            #Instead of saving the directory as its name, which can be not unique apparently, it's saved as a unique number.
            directory[curDir].append(dirToInt[tuple(dirPath)])

            #Remove the new directory as we are not actually in it.
            dirPath.pop()

    line = input().split()

#We want to get the smallest directory size that still will free up all the excess space.
minSize = float('inf')
excessSpace = getSum("1", directory) - 40000000

#Getting the sizes of all the directories, regardless of whether it has been checked already or not, for simplicity.
for dir in directory:
    dirSum = getSum(dir, directory)

    #Checking that the sum fits the size requirement, which we do after the function call for simplicity.
    if(dirSum >= excessSpace):
        minSize = min(minSize, dirSum)

print(minSize)