import math


def readFile():
    file = open('input10.txt')
    line = file.readline().replace('\n', '')

    while line:
        adapters.append(int(line))
        line = file.readline().replace('\n', '')
    file.close()

def reset():
    newArr.clear()
    for val in arrangement:
        newArr.append(val)

def addArrangement(first = False):
    arrstr = ''
    if first:
        for val in arrangement:
            arrstr += str(val) + ', '
    else:
        for val in newArr:
            arrstr += str(val) + ', '

    allArrangements.append(arrstr)

joltage = 0
joltDiff1 = 0
joltDiff2 = 0
joltDiff3 = 0

adapters = []
arrangement = [0]
allArrangements = []

search = 1
found = False

readFile()
builtin = max(adapters)+3

while len(adapters) > 0:
    for adapter in adapters:
        if adapter == joltage+1 and search == 1:
            joltDiff1 += 1
            joltage = adapter
            adapters.remove(adapter)
            found = True
            search = 1
            arrangement.append(joltage)
        elif adapter == joltage+2 and search == 2:
            joltDiff2 += 1
            joltage = adapter
            adapters.remove(adapter)
            found = True
            search = 1
            arrangement.append(joltage)
        elif adapter == joltage+3 and search == 3:
            joltDiff3 += 1
            joltage = adapter
            adapters.remove(adapter)
            found = True
            search = 1
            arrangement.append(joltage)

    if not found:
        search += 1
        if search > 4:
            search = 1
    else:
        found = False
        search = 1

joltage = builtin
joltDiff3 += 1

arrangement.append(joltage)
addArrangement(True)# allArrangements.append(arrangement)

readFile()
newArr = []

reset()

possibleChanges = 0
power2 = 0
power7 = 0
diff = -9999
for i in range(1, len(arrangement)-1):
    if i >= 3:
        diff = arrangement[i-3]
    if arrangement[i+1] - diff == 4:
        power7 += 1
        power2 -= 2
    elif arrangement[i+1] - arrangement[i-1] == 2:
        power2 += 1

res = math.pow(2, power2) * math.pow(7, power7)

print("Result: " + str(res))
