from string import digits
removeDigit = str.maketrans('', '', digits)

file = open('input7.txt')
line = file.readline().replace('\n', '')

rules = {}
bags = []


while line:
    arr = line.split('contain')
    outer = arr[0].replace('bags', '').replace(' ', '').strip()
    inner = arr[1].translate(removeDigit).replace('bags', '').replace('bag', '').replace('.', '').replace(' ', '').strip().split(',')
    rules.update({outer: inner})
    for color in inner:
        if color == 'shinygold':
            bags.append(outer)
    line = file.readline().replace('\n', '')
file.close()

count = -1

while count != 0:
    count = 0
    for key in rules:
        valColors = rules.get(key)
        for color in valColors:
            if (color in bags) and (key not in bags):
                bags.append(key)
                count += 1




print('Result: ' + str(len(bags)))

