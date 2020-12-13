from sympy.ntheory.modular import crt

file = open('input13.txt')
line = file.readline().replace('\n', '')

earliest = int(line)
arrivals = []
busses = []

line = file.readline().replace('\n', '').split(',')
for i in range(len(line)):
    if line[i] != 'x':
        busses.append(int(line[i]))
        arrivals.append(int(line[i])-i)
file.close()

res, mult = crt(busses, arrivals)

print('Result: ' + str(res))
