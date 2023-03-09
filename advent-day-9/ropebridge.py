head = [0, 0]
tail = [0, 0]
record_of_tail = [[0, 0]]

# constants to set where the x and y values are in our array of coordinates
X = 0
Y = 1

# for line in open('directions-pallavi.txt', 'r').readlines():
for line in open('directions-jeff.txt', 'r').readlines():
    (direction, number) = line.split(' ')
    for i in range(int(number)):
        if direction == 'R':
            head[X] = head[X] + 1
            if head[X] - tail[X] == 2:
                tail[X] = tail[X] + 1
                tail[Y] = head[Y]

        if direction == 'L':
            head[X] = head[X] - 1
            if tail[X] - head[X] == 2:
                tail[X] = tail[X] - 1
                tail[Y] = head[Y]

        if direction == 'D':
            head[Y] = head[Y] - 1
            if tail[Y] - head[Y] == 2:
                tail[Y] = tail[Y] - 1
                tail[X] = head[X]

        if direction == 'U':
            head[Y] = head[Y] + 1
            if head[Y] - tail[Y] == 2:
                tail[Y] = tail[Y] + 1
                tail[X] = head[X]


    # check if the record has the current tail
        match = False
        for point in record_of_tail:
            if point[X]==tail[X] and point[Y]==tail[Y]:
                match = True

        # if it doesn't, then add tail to the list
        if not match:
            record_of_tail.append([tail[X], tail[Y]])

print(record_of_tail)
print(len(record_of_tail))


