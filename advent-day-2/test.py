print ("Hello, world!")

# for each game/line
#  total += game/line score
# print total

# game score
#   big switch/if statements for scores

# A X = 1 + 3 = 4
# A Y = 2 + 6 = 8
# A Z = 3 + 0 = 3
#
# B X = 1 + 0 = 1
# B Y = 2 + 3 = 5
# B Z = 3 + 6 = 9
#
# C X = 1 + 6 = 7
# C Y = 2 + 0 = 2
# C Z = 3 + 3 = 6

inputFile = open('input-day-2.txt', 'r')
inputFileLines = inputFile.readlines()

score = 0;

for inputLine in inputFileLines:
    inputLine = inputLine.strip()
    if inputLine == "A X": score += 4
    elif inputLine == "A Y": score += 8
    elif inputLine == "A Z": score += 3
    elif inputLine == "B X": score += 1
    elif inputLine == "B Y": score += 5
    elif inputLine == "B Z": score += 9
    elif inputLine == "C X": score += 7
    elif inputLine == "C Y": score += 2
    elif inputLine == "C Z": score += 6
    else: print ("OUCH!" + inputLine)

print (score)
inputFile.close()