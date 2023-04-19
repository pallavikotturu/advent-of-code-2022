


clock = 0
register = 1
def noop():
    print("noop")


def addx(param):
    print(param)

def next_clock():
    global clock

    if clock % 40 == 0:
        clock = 0
        print()

    if register == clock or clock == register -1 or clock == register +1:
        print("#", end="")
    else:
        print(".", end="")

    clock += 1

for line in open('input-pallavi.txt', 'r').readlines():
    line = line.strip()
    if "noop" == line:
        next_clock()
    elif line.startswith("addx"):
        (cmd, param) = line.split(" ")
        next_clock()
        next_clock()
        register += int(param)