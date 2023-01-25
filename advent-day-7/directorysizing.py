# Need:

# to read the input file
inputFile = open('example-input.txt', 'r')


inputFileLines = inputFile.readlines()

root = dict()
currentPlace = root

def parentDirectoryOf(start, lookingFor):
    for key, value in start.items():
        # print(key, value)
        if value == lookingFor:
            return start
        elif isinstance(value, int):
            pass
        else:
            result = parentDirectoryOf(value, lookingFor)
            if result!=None :
                return result
            else:
                pass
    return None


# store into datastructure - done
# need to store the contents into the tree - done

# function that evaluates whether size of directory <= 100000
def getSizeOfDirectory(dir):

    totalSize = 0
    for key in dir:
        isItADirectory = isinstance(dir[key], dict)
        if(isItADirectory):
            sizeOfChild = getSizeOfDirectory(dir[key])
            totalSize = totalSize + sizeOfChild
        else:
            #this is for non-dictionary items
            totalSize = totalSize + dir[key]
    return totalSize



# interpret/map the input line to action
# interpret a line of the file
# to create a datastructure (tree of some sort) to store the heirarchy of that directory structure
state = "command" # or listing
for fileLine in inputFileLines:
    if fileLine == '$ cd /\n':
        state = "command"
        pass
    elif fileLine == '$ cd ..\n':
        state = "command"
        currentPlace = parentDirectoryOf(root, currentPlace)
    elif fileLine[0:4] == '$ cd':
        state = "command"
        temp = dict()
        currentPlace[fileLine[5:len(fileLine)-1]] = temp
        currentPlace = temp
    elif fileLine[0:4] == '$ ls':
        state = "listing"
        pass
    elif state == "listing":
        (size, name) = fileLine.strip().split(" ")
        if (size!="dir"):
            currentPlace[name] = int(size)

print(root)


listOfMatchingDirectories = []
def findSmallDirectories(dir):
# walk child node of the dir
    for child in dir:
        print(child)
        # if the node is a directory
        if isinstance(dir[child], dict):
            print("isDict")
            # check its size
            childSize = getSizeOfDirectory(dir[child])
             # if it's size is > 100k
            if (childSize <= 100000):
                # add to a list of matching directories
                listOfMatchingDirectories.append(childSize)
            findSmallDirectories(dir[child])

findSmallDirectories(root)
print(listOfMatchingDirectories)

totalSize = 0
for size in listOfMatchingDirectories:
    totalSize += size

print(totalSize)


# PART TWO - DAY 7

# plain text logic:
# run the new input file commands through above code to generate directory size
totalFileSystemSize = getSizeOfDirectory(root) #pallavi: 41072511
print(totalFileSystemSize)

# set local int to 70 MILLION - size of root directory
delta_pallavi = 30000000 - (70000000 - totalFileSystemSize)
print(delta_pallavi) # need a directory that frees up at least 1072511

listOfAcceptableDirectories = []
def findSizableDirectories(dir):
    # walk child node of the dir
    for child in dir:
        print(child)
        # if the node is a directory
        if isinstance(dir[child], dict):
            print("isDict")
            # check its size
            childSize = getSizeOfDirectory(dir[child])
            # if it's size is > 100k
            if (childSize >= delta_pallavi):
                # add to a list of matching directories
                listOfAcceptableDirectories.append(childSize)
            findSizableDirectories(dir[child])

findSizableDirectories(root)
print(min(listOfAcceptableDirectories))

# traverse through tree to collect list of directories whose size is >= delta (above local variable)


# get smallest sized directory

