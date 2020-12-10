joltage = 0
joltDiff1 = 0
joltDiff2 = 0
joltDiff3 = 0

adapters = []

search = 1
found = False

file = open('input10.txt')
line = file.readline().replace('\n', '')

while line:
    adapters.append(int(line))
    line = file.readline().replace('\n', '')
file.close()

builtin = max(adapters)+3

while len(adapters) > 0:
    for adapter in adapters:
        if adapter == joltage+1 and search == 1:
            joltDiff1 += 1
            joltage = adapter
            adapters.remove(adapter)
            found = True
            search = 1
        elif adapter == joltage+2 and search == 2:
            joltDiff2 += 1
            joltage = adapter
            adapters.remove(adapter)
            found = True
            search = 1
        elif adapter == joltage+3 and search == 3:
            joltDiff3 += 1
            joltage = adapter
            adapters.remove(adapter)
            found = True
            search = 1
        if found:
            print(joltage)
    if not found:
        search += 1
        if search > 4:
            search = 1
    else:
        found = False
        search = 1

joltage = builtin
joltDiff3 += 1

res = joltDiff1 * joltDiff3

print("Result: " + str(res))
