def recursiveCount(key):
    if key == '0':
        return 0
    valColors = rules.get(key[1:])
    temp.update({key: valColors})
    for color in valColors:
        # nb = int(color[0])
        # print(color)
        # total += nb*fact
        recursiveCount(color)


def product(list):
    if len(list) == 1:
        return list[0]
    else:
        return list[0] * product(list[1:])

from string import digits
removeDigit = str.maketrans('', '', digits)

file = open('input7.txt')
line = file.readline().replace('\n', '')

rules = {}
bags = []
total = 0
temp = {}

while line:
    arr = line.split('contain')
    outer = arr[0].replace('bags', '').replace(' ', '').strip()
    inner = arr[1].replace('no other', '0').replace('bags', '').replace('bag', '').replace('.', '').replace(' ', '').strip().split(',')
    rules.update({outer: inner})
    for color in inner:
        if color == 'shinygold':
            bags.append(outer)
    line = file.readline().replace('\n', '')
file.close()


listBags = ['shinygold']
listNb = []
for item in listBags:
    valColors = rules.get(item)
    for color in valColors:
        if color != '0':
            listBags.append(color[1:])
            listNb.append(int(color[0]))
        # total += int(color[0]) + int(color[0])*findBags(color)

size = {}
recursiveCount('1shinygold')
# number of bags inside parent bag
for key in temp:
    value = temp.get(key)
    n = 0
    for v in value:
        n += int(v[0])
    size.update({key: n})
    total += int(key[0])*n


res = 0
dfs = [(1, 'shinygold')]

while len(dfs) > 0:
    amount, color = dfs.pop()
    res += amount
    if color in rules:
        children = rules.get(color)
        for child in children:
            dfs.append((int(child[0])*amount, child[1:]))




# listTemp = []
# for t in temp:
#     if t == '0':
#         total += product(listTemp)
#         listTemp.clear()
#     else:
#         listTemp.append(int(t[0]))

print('Result: ' + str(res-1))

