head = [0, 0]
tail = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
record_of_tail = [[0, 0]]

# constants to set where the x and y values are in our array of coordinates
X = 0
Y = 1


def move_down_one(tail):
    tail[Y] = tail[Y] - 1


def move_left_one(tail):
    tail[X] = tail[X] - 1


def move_up_one(tail):
    tail[Y] = tail[Y] + 1


def move_right_one(tail):
    tail[X] = tail[X] + 1


def is_below(tail, head, distance):
    return head[Y] - tail[Y] == distance


def is_left_of(tail, head, distance):
    return head[X] - tail[X] == distance

def is_above(tail, head, distance):
    return tail[Y] - head[Y] == distance


def is_right_of(tail, head, distance):
    return tail[X] - head[X] == distance

def moveHead(direction):
    # move the head according to the command
    if direction == 'R':
        move_right_one(head)
    if direction == 'L':
        move_left_one(head)
    if direction == 'D':
        move_down_one(head)
    if direction == 'U':
        move_up_one(head)

def moveTail(tail, head):
    # Auto-move tail according to rules

    if is_left_of(tail, head, 2) and is_below(tail, head, 2):
        move_right_one(tail)
        move_up_one(tail)
        return

    if is_right_of(tail, head, 2) and is_above(tail, head, 2):
        move_left_one(tail)
        move_down_one(tail)
        return

    if is_left_of(tail, head, 2) and is_above(tail, head, 2):
        move_right_one(tail)
        move_down_one(tail)
        return

    if is_right_of(tail, head, 2) and is_below(tail, head, 2):
        move_left_one(tail)
        move_up_one(tail)
        return

    if is_left_of(tail, head, 2):
        move_right_one(tail)
        tail[Y] = head[Y]
        return

    if is_left_of(head, tail, 2):
        move_left_one(tail)
        tail[Y] = head[Y]
        return

    if is_below(head, tail, 2):
        move_down_one(tail)
        tail[X] = head[X]
        return

    if is_below(tail, head, 2):
        move_up_one(tail)
        tail[X] = head[X]
        return



# for line in open('directions-pallavi.txt', 'r').readlines():
for line in open('directions-jeff.txt', 'r').readlines():
#for line in ["R 5", "U 8", "L 8", "D 3", "R 17", "D 10", "L 25", "U 20"]:
    (direction, number) = line.split(' ')
    #print(line)
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
            if point[X]==tail[8][X] and point[Y]==tail[8][Y]:
                match = True

        # if it doesn't, then add tail to the list
        if not match:
            record_of_tail.append([tail[8][X], tail[8][Y]])

    #print(head, tail)

print(record_of_tail)
print(len(record_of_tail))


