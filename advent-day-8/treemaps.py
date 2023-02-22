# to read the input file

forest = []
def lineToArrayOfInt(str):
    arr = []
    for character in str:
      # convert character to integer
      i = int(character)
      # append integer to array
      arr.append(i)
    return arr

# for each line in the file
for line in open('tree-input-jeff.txt', 'r').readlines():
  # Convert line to an array of single digit integers
  arrayOfInt = lineToArrayOfInt(line.strip())
  # Add array of single digit integers to forest
  forest.append(arrayOfInt)

tally = 0

def isvisiblefromtop(treerow, treecolumn):
    isvisiblefromtop_variable = True
    for treetothetoprow in reversed(range(0, treerow)):
        if forest[treetothetoprow][treecolumn] >= forest[treerow][treecolumn] :
            isvisiblefromtop_variable = False
    return isvisiblefromtop_variable

def isvisiblefrombottom(treerow, treecolumn):
    isvisiblefrombottom_variable = True
    for treetothebottomrow in range(treerow + 1, len(forest)):
        if forest[treetothebottomrow][treecolumn] >= forest[treerow][treecolumn] :
            isvisiblefrombottom_variable = False
    return isvisiblefrombottom_variable

def isvisiblefromright(treerow, treecolumn):
    isvisiblefromright_variable = True
    for treetotherightscolumn in range(treecolumn + 1, len(forest[treerow])):
        if forest[treerow][treetotherightscolumn] >= forest[treerow][treecolumn] :
            isvisiblefromright_variable = False
    return isvisiblefromright_variable

def isvisiblefromleft(treerow, treecolumn):
    isvisiblefromleft_variable = True
    for treetotheleftscolumn in reversed(range(0, treecolumn)):
        if forest[treerow][treetotheleftscolumn] >= forest[treerow][treecolumn] :
            isvisiblefromleft_variable = False
    return isvisiblefromleft_variable


for treerow in range(0, len(forest)):
    for treecolumn in range(0, len(forest[treerow])):
        if(isvisiblefromleft(treerow, treecolumn) or isvisiblefromright(treerow, treecolumn) or
        isvisiblefromtop(treerow, treecolumn) or isvisiblefrombottom(treerow, treecolumn)):
            tally = tally + 1

print (tally)

#forest = [[3, 0, 3, 7, 3], [2, 5, 5, 1, 2], [6, 5, 3, 3, 2], [3, 3, 5, 4, 9], [3, 5, 3, 9, 0]]

def checkLeft(treerow, treecolumn, originalTreeHeight):
    tally = 0
    if treecolumn == 0:
        pass
    elif forest[treerow][treecolumn-1] <= originalTreeHeight:
        tally += 1
        if forest[treerow][treecolumn-1] < originalTreeHeight:
            tally += checkLeft(treerow, treecolumn-1, originalTreeHeight)
    elif forest[treerow][treecolumn-1] > originalTreeHeight:
        tally += 1
    return tally

def checkRight(treerow, treecolumn, originalTreeHeight):
    tally = 0
    if treecolumn == len(forest[0])-1:
        pass
    elif forest[treerow][treecolumn+1] <= originalTreeHeight:
        tally += 1
        if forest[treerow][treecolumn+1] < originalTreeHeight:
            tally += checkRight(treerow, treecolumn+1, originalTreeHeight)
    elif forest[treerow][treecolumn+1] > originalTreeHeight:
        tally += 1
    return tally

def checkBottom(treerow, treecolumn, originalTreeHeight):
    tally = 0
    if treerow == len(forest)-1:
        pass
    elif forest[treerow+1][treecolumn] <= originalTreeHeight:
        tally += 1
        if forest[treerow+1][treecolumn] < originalTreeHeight:
            tally += checkBottom(treerow+1, treecolumn, originalTreeHeight)
    elif forest[treerow+1][treecolumn] > originalTreeHeight:
        tally += 1
    return tally

def checkTop(treerow, treecolumn, originalTreeHeight):
    tally = 0
    if treerow == 0:
        pass
    elif forest[treerow-1][treecolumn] <= originalTreeHeight:
        tally += 1
        if forest[treerow-1][treecolumn] < originalTreeHeight:
            tally += checkTop(treerow-1, treecolumn, originalTreeHeight)
    elif forest[treerow-1][treecolumn] > originalTreeHeight:
        tally += 1
    return tally
# for every tree in the forest
highestScore = 0
for treerow in range(0, len(forest)):
    for treecolumn in range(0, len(forest[treerow])):
        currentTreeScore = 1;
        currentTreeScore *= checkLeft(treerow, treecolumn, forest[treerow][treecolumn])
        currentTreeScore *= checkRight(treerow, treecolumn, forest[treerow][treecolumn])
        currentTreeScore *= checkTop(treerow, treecolumn, forest[treerow][treecolumn])
        currentTreeScore *= checkBottom(treerow, treecolumn, forest[treerow][treecolumn])

        if (currentTreeScore > highestScore):
            highestScore = currentTreeScore

print(highestScore)