# counters
monkey0 = 0
monkey1 = 0
monkey2 = 0
monkey4 = 0

monkeyItemsMap = {'Monkey 0:':{79, 98},
                  'Monkey 1:': {54, 65, 75, 74},
                  'Monkey 2:': {79, 60, 97},
                  'Monkey 3:':{74}}

# implement output to generate what items each monkeys have
def printPostRoundOutput():
    print("Monkey 0:", monkeyItemsMap.get("Monkey 0:"))
    print("Monkey 1:", monkeyItemsMap.get("Monkey 1:"))
    print("Monkey 2:", monkeyItemsMap.get("Monkey 2:"))
    print("Monkey 3:", monkeyItemsMap.get("Monkey 3:"))

def moveItemToNewMonkey(startingItem, initialMonkey, finalMonkey):
    monkeyItemsMap.get(initialMonkey).remove(startingItem)
    monkeyItemsMap.get(finalMonkey).add(startingItem)
    pass

def ifFalse():
    pass

def evaluateModulus(startingItem, base, dividedBy, initialMonkey, finalMonkey):
    if ((base % dividedBy) == 0):
        moveItemToNewMonkey(startingItem, initialMonkey, finalMonkey)
    else:
        ifFalse()

printPostRoundOutput()
# counter to see how many times each monkey inspected an item

# calculate monkey business