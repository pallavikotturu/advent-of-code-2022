# inputFile = open('input-rucksack-pallavi.txt', 'r')
inputFile = open('input-rucksack-pallavi.txt', 'r')
inputFileLines = inputFile.readlines()

# divide each line into 2 segments
# compare each character from one segment to see
# if it exists in the second

def getPriorityNumber(charToCompare):
    asciiForChar = ord(charToCompare)
    if asciiForChar > 96:
        return asciiForChar - 96
    else:
        return asciiForChar - 38

totalPrioritySum = 0
# for inputLine in inputFileLines:
#
#     stringLength = len(inputLine)
#     middle = int(stringLength / 2)
#     firstHalf = inputLine[0:middle]
#     secondHalf = inputLine[middle:len(inputLine)]
#
#     for character in set(firstHalf):
#         if secondHalf.__contains__(character) : totalPrioritySum += getPriorityNumber(character)

# print(len(inputFileLines))

# for every set of three lines, we have to compare each character in the line to see if any of them are present in all three of them
print(inputFileLines[4])

startIndex = 0
endIndex = 3



for inputLine in inputFileLines:

    stringLength = len(inputLine)
    middle = int(stringLength / 2)
    firstHalf = inputLine[0:middle]
    secondHalf = inputLine[middle:len(inputLine)]

    for character in set(firstHalf):
        if secondHalf.__contains__(character) : totalPrioritySum += getPriorityNumber(character)

print(totalPrioritySum)


# Part 2
print("Part 2")
totalPrioritySum=0
currentGroupIndex = 0
while currentGroupIndex < len(inputFileLines) :
    # if exists in line2 and exists in line 3, print
    firstElf = inputFileLines[currentGroupIndex].strip()
    secondElf = inputFileLines[currentGroupIndex+1].strip()
    thirdElf = inputFileLines[currentGroupIndex+2].strip()

    for character in set(firstElf):
        if secondElf.__contains__(character) and thirdElf.__contains__(character):
            print(character)
            totalPrioritySum += getPriorityNumber(character)

    currentGroupIndex += 3

print(totalPrioritySum)