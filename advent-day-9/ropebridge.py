# SMALL FUNCTIONS:

# read command
# move head based on command
# calculate delta between head and tail (condition maybe?)
# generate acceptable coordinates for tail to be in
# if tail isn't in acceptable coordinate, move tail left, right, down, up
# record every position that tail has visited

# QUESTIONS TO ANSWER:
# what datastructure to use for representing head and tail?
head = [0, 0]
tail = [0, 0]
record_of_tail = [[0, 0]]

# how to capture positions that tail has visited?
sample_instructions = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""

X = 0
Y = 1

# reads command
# record tail position
# reads commands & moves head
for line in sample_instructions.split("\n"):
    (direction, number) = line.split(' ')
    for i in range(int(number)):
        if direction == 'R':
            head[X] = head[X] + 1
        if direction == 'L':
            head[X] = head[X] - 1
        if direction == 'D':
            head[Y] = head[Y] + 1
        if direction == 'U':
            head[Y] = head[Y] - 1
        record_of_tail.append([head[X], head[Y]])


print(record_of_tail)

# moves tail u
# moves tail d
# moves tail r
# moves tail l
# reads commands & moves head & move tail & record tail position
