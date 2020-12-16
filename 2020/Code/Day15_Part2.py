
pos = 1
numbers = {}
nextNb = 0
current = 0

wanted = 30000000-1

file = open('input15.txt')
line = file.readline().replace('\n', '').split(',')
file.close()

for nb in line:
    nb = int(nb)
    numbers.update({nb: pos})
    pos += 1

current = 0

while pos <= wanted:
    if current in numbers:
        nextNb = pos - numbers.get(current)
    else:
        nextNb = 0
    print("Number " + str(current) + " at position " + str(pos))
    numbers.update({current: pos})
    current = nextNb
    pos += 1


print('Result: ' + str(current))

