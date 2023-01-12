# Need:

# to read the input file
inputFile = open('example-input.txt', 'r')
inputFileLines = inputFile.readlines()

root = dict()
currentPlace = root

def parentDirectoryOf(start, lookingFor):
    for key, value in start.items():
        print(key, value)
        if value == lookingFor:
            return start
        elif isinstance(value, int):
            pass
        else:
            return parentDirectoryOf(value, lookingFor)

tree = dict();
tree["b.txt"] = 14848514
tree["c.dat"] = 8504156

tree["a"] = dict()
tree["a"]["f"] = 29116
tree["a"]["g"] = 2557
tree["a"]["h.lst"] = 62596
tree["a"]["e"] = dict()
tree["a"]["e"]["i"] = 584

d = dict()
tree["d"] = d
tree["d"]["j"] = 4060174
tree["d"]["d.log"] = 8033020
tree["d"]["d.ext"] = 5626152
tree["d"]["k"] = 7214296
print(tree)

print(parentDirectoryOf(tree, d))
exit(1)

# interpret/map the input line to action
# interpret a line of the file
# to create a datastructure (tree of some sort) to store the heirarchy of that directory structure
for fileLine in inputFileLines:
    if fileLine == '$ cd /\n':
        pass
    elif fileLine == '$ cd ..\n':
        currentPlace = parentDirectoryOf(root, currentPlace)

    elif fileLine[0:4] == '$ cd':
        temp = dict()
        currentPlace[fileLine[5:len(fileLine)-1]] = temp
        currentPlace = temp
    elif fileLine[0:3] == '$ ls':
        pass
    print(root)
# store into datastructure
#need to store the contents into the tree

# depth first algorithm to walk the tree to find and store sizes of directories with files <= 100k size
#function that evaluates whether size of directory <= 100000

# sum them all up


