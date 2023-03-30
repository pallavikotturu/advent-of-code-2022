head = [0, 0]
tail = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
record_of_tail = [[0, 0]]

# constants to set where the x and y values are in our array of coordinates
X = 0
Y = 1

def moveHead(direction):
    # move the head according to the command
    if direction == 'R':
        head[X] = head[X] + 1
    if direction == 'L':
        head[X] = head[X] - 1
    if direction == 'D':
        head[Y] = head[Y] - 1
    if direction == 'U':
        head[Y] = head[Y] + 1

def moveTail(tail, head):
    # Auto-move tail according to rules
    if head[X] - tail[X] == 2 and head[Y] - tail[Y] == 2:
        tail[X] = tail[X] + 1
        tail[Y] = tail[Y] + 1
        return
    if head[X] + tail[X] == 2 and head[Y] + tail[Y] == 2:
        tail[X] = tail[X] - 1
        tail[Y] = tail[Y] - 1
        return
    if head[X] - tail[X] == 2 and head[Y] + tail[Y] == 2:
        tail[X] = tail[X] + 1
        tail[Y] = tail[Y] - 1
        return
    if head[X] + tail[X] == 2 and head[Y] - tail[Y] == 2:
        tail[X] = tail[X] - 1
        tail[Y] = tail[Y] + 1
        return

    if head[X] - tail[X] == 2:
        tail[X] = tail[X] + 1
        tail[Y] = head[Y]
        return
    if tail[X] - head[X] == 2:
        tail[X] = tail[X] - 1
        tail[Y] = head[Y]
        return
    if tail[Y] - head[Y] == 2:
        tail[Y] = tail[Y] - 1
        tail[X] = head[X]
        return
    if head[Y] - tail[Y] == 2:
        tail[Y] = tail[Y] + 1
        tail[X] = head[X]
        return

# for line in open('directions-pallavi.txt', 'r').readlines():
for line in open('directions-jeff.txt', 'r').readlines():
#for line in ["R 5", "U 8", "L 8", "D 3", "R 17", "D 10", "L 25", "U 20"]:
    (direction, number) = line.split(' ')
    for i in range(int(number)):
        moveHead(direction)
        moveTail(tail[0], head)
        moveTail(tail[1], tail[0])
        moveTail(tail[2], tail[1])
        moveTail(tail[3], tail[2])
        moveTail(tail[4], tail[3])
        moveTail(tail[5], tail[4])
        moveTail(tail[6], tail[5])
        moveTail(tail[7], tail[6])
        moveTail(tail[8], tail[7])



    # check if the record has the current tail
        match = False
        for point in record_of_tail:
            if point[X]==tail[0][X] and point[Y]==tail[0][Y]:
                match = True

        # if it doesn't, then add tail to the list
        if not match:
            record_of_tail.append([tail[0][X], tail[0][Y]])

print(record_of_tail)
print(len(record_of_tail))


