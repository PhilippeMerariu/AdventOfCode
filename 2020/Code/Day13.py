import math

file = open('input13.txt')
line = file.readline().replace('\n', '')

earliest = int(line)
arrivals = []

line = file.readline().replace('\n', '')
busses = line.replace('x,', '').split(',')
file.close()

for bus in busses:
    bus = int(bus)
    factor = math.floor(earliest / bus)
    if factor*bus < earliest:
        factor += 1
    arrivals.append(factor*bus)

for i in range(len(arrivals)):
    if arrivals[i] == min(arrivals):
        wait = arrivals[i] - earliest
        res = wait* int(busses[i])

print('Result: ' + str(res) )
