def writeToMemory(index, value):
    index = list(index)
    for i in range(len(mask)):
        if mask[i] == '1' or mask[i] == 'X':
            index[i] = mask[i]

    nbPerm = pow(2, index.count('X'))
    count = 0
    changes = []
    while nbPerm > count:
        number = index.copy()
        changes = list(format(count, '0'+str(index.count("X"))+'b'))
        for k in range(len(index)):
            if index[k] == 'X':
                number[k] = changes[0]
                changes = changes[1:]
        count += 1
        memory.update({binaryToDecimal(number): value})

def binaryToDecimal(bin):
    dec = 0
    for i in range(len(bin)):
        dec += int(bin[i]) * pow(2, len(bin)-(i+1))
    return dec


memory = {}
mask = []

file = open('input14.txt')
line = file.readline()

while line:
    line = line.replace('\n', '').split(' = ')
    if line[0] == 'mask':
        mask.clear()
        for bit in line[1]:
            mask.append(bit)
    else:
        memIndex = int(line[0].replace('[', ' ').replace(']', '').split(' ')[1])
        memDecVal = int(line[1])
        memBinIndex = format(memIndex, '036b')
        writeToMemory(memBinIndex, memDecVal)
    line = file.readline()
file.close()

res = 0

for mem in memory:
    res += memory.get(mem)


print('Result: ' + str(res))
