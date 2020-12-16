
numbers = []
pos = 1
nextNb = 0
previous = 0

file = open('input15.txt')
line = file.readline().replace('\n', '').split(',')
file.close()

for nb in line:
    nb = int(nb)
    previous = nb
    numbers.append(nb)
    pos += 1


while len(numbers) <= 2020:
    if numbers.count(previous) > 1:
        for i in range(len(numbers)-2, -1, -1):
            if numbers[i] == previous:
                nextNb = len(numbers) - (i+1)
                break
    else:
        nextNb = 0

    numbers.append(nextNb)
    previous = nextNb
    pos += 1


print('Result: ' + str(numbers[2019]))

