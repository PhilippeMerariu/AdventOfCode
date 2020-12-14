def writeToMemory(index, value):
    value = list(value)
    for i in range(len(mask)):
        if mask[i] == '1' or mask[i] == '0':
            value[i] = mask[i]
    memory.update({index: binaryToDecimal(value)})

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
        memIndex = line[0].replace('[', ' ').replace(']', '').split(' ')[1]
        memDecVal = int(line[1])
        memBinVal = format(memDecVal, '036b')
        writeToMemory(memIndex, memBinVal)
    line = file.readline()
file.close()

res = 0

for mem in memory:
    res += memory.get(mem)


print('Result: ' + str(res))
