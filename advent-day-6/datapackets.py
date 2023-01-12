# for every substring [x,y] if any character in that substring is repeated, move to [x++, y++]
inputFile = open('datapackets-input-jeff.txt', 'r')
inputFile = open('datapackets-input-pallavi.txt', 'r')
input = inputFile.readlines()[0]

# created for use case of string length four
def hasRepeatedCharacters(s) :
    # common algorithm for comparing through all elements in list
    for x in range(0, len(s)-1):
        for y in range(x+1, len(s)):
            if s[x] == s[y]:
                return True
    return False


startTokenSize = 14
# for each index
for i in range(len(input)-3):
    # substring = substring[startindex, startindex + 4]
    substring = input[i:i+startTokenSize]
    # if any characters repeat
    if(hasRepeatedCharacters(substring)):
        #   call itself recursively
        pass
    else:
        print(i+startTokenSize)
        print(substring)
        break