
file = open('input8.txt')
line = file.readline().replace('\n', '')
instructions = []
while line:
    temp = line.split(' ')
    temp.append(1)
    instructions.append(temp)
    line = file.readline().replace('\n', '')
file.close()

res = 0
index = 0

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
        index += int(val)
        print("Jump to: " + str(index))
    else:
        index += 1
    inst, val, count = instructions[index]

print('Result: ' + str(res))

