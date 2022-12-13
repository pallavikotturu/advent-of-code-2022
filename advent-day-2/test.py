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

# inputFile = open('input-day-2.txt', 'r') -- JEFF HOFFMAN
inputFile = open('input-day-2-pallavi.txt', 'r')
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

# Second star:

# x = lose = 0
# y = draw = 3
# z = win = 6

# A = rock = 1
# B = paper = 2
# c = scissors = 3

# A X = 3 + 0 = 3
# A Y = 1 + 3 = 4
# A Z = 2 + 6 = 8
#
# B X = 1 + 0 = 1
# B Y = 2 + 3 = 5
# B Z = 3 + 6 = 9
#
# C X = 2 + 0 = 2
# C Y = 3 + 3 = 6
# C Z = 1 + 6 = 7


inputFile = open('input-day-2-pallavi.txt', 'r')
inputFileLines = inputFile.readlines()

score = 0;

for inputLine in inputFileLines:
    inputLine = inputLine.strip()
    if inputLine == "A X": score += 3
    elif inputLine == "A Y": score += 4
    elif inputLine == "A Z": score += 8
    elif inputLine == "B X": score += 1
    elif inputLine == "B Y": score += 5
    elif inputLine == "B Z": score += 9
    elif inputLine == "C X": score += 2
    elif inputLine == "C Y": score += 6
    elif inputLine == "C Z": score += 7
    else: print ("OUCH!" + inputLine)

print (score)
inputFile.close()