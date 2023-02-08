# to read the input file
inputFile = open('tree-input-pallavi.txt', 'r')
inputFileLines = inputFile.readlines()

forest = [[3, 0, 3, 7, 3], [2, 5, 5, 1, 2], [6, 5, 3, 3, 2], [3, 3, 5, 4, 9], [3, 5, 3, 9, 0]]
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