pastnbs = []
found = False
res = ''
file = open('input9.txt')
line = file.readline().replace('\n', '')
while line:
    found = False
    if len(pastnbs) < 25:
        pastnbs.append(int(line))
    else:
        for nb1 in pastnbs:
            for nb2 in pastnbs:
                if nb1 != nb2 and nb1 + nb2 == int(line):
                    found = True

        if not found:
            res = line
            break
        elif found:
            pastnbs = pastnbs[1:]
            pastnbs.append(int(line))
    line = file.readline().replace('\n', '')
file.close()

print('Number: ' + res)

file = open('input9.txt')
line = file.readline().replace('\n', '')
sequence = []
allnbs = []
while line:
    allnbs.append(int(line))
    line = file.readline().replace('\n', '')
file.close()

def findSum(index, res):
    total = 0
    sequence.clear()
    for i in range(index, len(allnbs)-1):
        sequence.append(allnbs[i])
        total += allnbs[i]
        print(str(index) + "   " + str(total))
        if total == int(res):
            return min(sequence) + max(sequence)
        elif total > int(res):
            return 0
    return 0

finalRes = 0
index = 0
while finalRes == 0:
    finalRes = findSum(index, res)
    index += 1

print("Result: " + str(finalRes))
