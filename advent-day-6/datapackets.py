# for every substring [x,y] if any character in that substring is repeated, move to [x++, y++]
inputFile = open('datapackets-input-pallavi.txt', 'r')
input = inputFile.readlines()[0]

# created for use case of string length four
def hasRepeatedCharacters(s) :
    if s[0] == s[1]:
        return True
    if s[0] == s[2]:
        return True
    if s[0] == s[3]:
        return True
    if s[1] == s[2]:
        return True
    if s[1] == s[3]:
        return True
    if s[2] == s[3]:
        return True
    return False


# for each index
for i in range(len(input)-3):
    # substring = substring[startindex, startindex + 4]
    substring = input[i:i+4]
    # if any characters repeat
    if(hasRepeatedCharacters(substring)):
        #   call itself recursively
        pass
    else:
        print(i+4)
        break