


clock = 0
register = 1
sum = 0

def noop():
    print("noop")


def addx(param):
    print(param)


for line in open('input-jeff.txt', 'r').readlines():
    line = line.strip()
    if "noop" == line:
        clock += 1
        if clock in (20, 60, 100, 140, 180, 220):
                sum += clock * register
    elif line.startswith("addx"):
        (cmd, param) = line.split(" ")
        clock += 1
        if clock in (20, 60, 100, 140, 180, 220):
            sum += clock * register
        clock += 1
        if clock in (20, 60, 100, 140, 180, 220):
            sum += clock * register
        register += int(param)

print(sum)