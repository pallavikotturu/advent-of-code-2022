# if the digits that fall within the second half are encompassed within the first half, then increment containment counter
inputFile = open('cleaning-input-pallavi.txt', 'r')
# inputFile = open('cleaning-input-jeff.txt', 'r')
inputFileLines = inputFile.readlines()

def contains(lower1, upper1, lower2, upper2):
    # if 3rd number >= first number and 4th number <= second number then increment containsFully
    if lower2 >= lower1 and upper2 <= upper1 : #coincides - part 1
    # if lower2 >= lower1 and lower2 <= upper1 : #overlaps - part 2
        return True


containsFully = 0

# break down each line using the delimiter (,) into two sections
for eachLine in inputFileLines:
    (firstHalf, secondHalf) = eachLine.strip().split(",")
    (lower1, upper1, lower2, upper2) = list(map(int, firstHalf.split('-') + secondHalf.split('-')))

    if contains(lower1, upper1, lower2, upper2) or contains(lower2, upper2, lower1, upper1) :
        # print(eachLine)
        containsFully += 1

print(containsFully)