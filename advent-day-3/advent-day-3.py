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
for inputLine in inputFileLines:

    stringLength = len(inputLine)
    middle = int(stringLength / 2)
    firstHalf = inputLine[0:middle]
    secondHalf = inputLine[middle:len(inputLine)]

    for character in set(firstHalf):
        # print(firstHalf + " " + secondHalf + " " + character + " " + str(getPriorityNumber(character)))
        if secondHalf.__contains__(character) : totalPrioritySum += getPriorityNumber(character)
        # if secondHalf.__contains__(character) : print(firstHalf + " " + secondHalf + " " + character + " " + str(getPriorityNumber(character)))

print(totalPrioritySum)