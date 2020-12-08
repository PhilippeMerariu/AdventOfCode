def bruteForce(res=0, index=0, changed=False):
    instructions.clear()
    file = open('input8.txt')
    line = file.readline().replace('\n', '')
    while line:
        temp = line.split(' ')
        temp.append(1)
        instructions.append(temp)
        line = file.readline().replace('\n', '')
    file.close()

    inst = instructions[index][0]
    val = instructions[index][1]
    count = instructions[index][2]
    while count == 1:
        instructions[index][2] += 1
        if inst == 'acc':
            res += int(val)
            index += 1
            print("Current result: " + str(res))
        elif inst == 'jmp':
            if not changed and index not in changedIndex:
                changedIndex.append(index)
                changed = True
                index += 1
            else:
                index += int(val)
            print("Jump to: " + str(index))
        else:
            if not changed and index not in changedIndex:
                changedIndex.append(index)
                changed = True
                index += int(val)
            else:
                index += 1
        if index >= len(instructions):
            return res, index
        inst, val, count = instructions[index]
    return res, index

instructions = []
res = 0
index = 0
changed = False
changedIndex = []
bruteForce(res, index)

while index != len(instructions):
    res, index = bruteForce()

print('Result: ' + str(res))

