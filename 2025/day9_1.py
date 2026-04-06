import itertools

file = open('input9.txt')
line = file.readline()

result = 0

grid = []
red_tiles = []

while line:
    line = line.strip('\n')
    red_tiles.append(tuple(int(t) for t in line.split(',')))
    line = file.readline()
file.close()

corner_pairs = itertools.combinations(red_tiles, 2)

for cp in corner_pairs:
    r_size = abs(cp[0][0] - cp[1][0]) + 1
    c_size = abs(cp[0][1] - cp[1][1]) + 1
    volume = r_size * c_size
    if volume > result:
        result = volume

print(f"ANSWER = {result}")
