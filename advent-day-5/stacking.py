# DAY 5
# Python program to
# follow list of instructions and move crates across 9 different stacks
# for elves to work on

inputFile = open('instructions-jeff.txt', 'r')
inputFileLines = inputFile.readlines()

jeffStacks = [
    ['D', 'L', 'V', 'T', 'M', 'H', 'F'],
    ['H', 'Q', 'G', 'J', 'C', 'T', 'N', 'P'],
    ['R', 'S', 'D', 'M', 'P', 'H'],
    ['L', 'B', 'V', 'F'],
    ['N', 'H', 'G', 'L', 'Q'],
    ['W', 'B', 'D', 'G', 'R', 'M', 'P'],
    ['G', 'M', 'N', 'R', 'C', 'H', 'L', 'Q'],
    ['C', 'L', 'W'],
    ['R', 'D', 'L', 'Q', 'J', 'Z', 'M', 'T']
]

stacks = jeffStacks

# split each line using delimiter ' '
# ignore all words.
# capture the 3 numbers.
# convert them into integers
# create function moveCrates (first number is quantity, second number is stack start location, third number is stack end location)
# within the function, we pop and then append based on location values -1 from stacks

def moveCrates(quantity, startStack, finalStack):
    subStack = stacks[startStack-1][-quantity:]
    stacks[startStack-1] = stacks[startStack-1][:-quantity]
    for c in subStack:
        stacks[finalStack-1].append(c)


for eachLine in inputFileLines:
    listOfLineSegments = eachLine.split(' ')
    quantity = int(listOfLineSegments[1])
    startStack = int(listOfLineSegments[3])
    finalStack = int(listOfLineSegments[5])

    moveCrates(quantity, startStack, finalStack)


finalTopCrates = ''
for stack in stacks:
    finalTopCrates += stack[len(stack) - 1]

print(finalTopCrates)

