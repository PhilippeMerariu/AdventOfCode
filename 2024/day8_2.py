import itertools

file = open('input8.txt')
line = file.readline()

map = []
antinode_map = []
frequencies = []

while line:
    line = line.strip('\n')
    map_row = [x for x in line]
    antinode_row = ['.' for x in line]
    map.append(map_row.copy())
    antinode_map.append(antinode_row.copy())
    frequencies = list(set(map_row + frequencies))
    line = file.readline()
file.close()

if '.' in frequencies:
    frequencies.remove('.')

for freq in frequencies:
    # find location of all freq nodes
    freq_locations = []
    for row in range(len(map)):
        for col in range(len(map[row])):
            if map[row][col] == freq:
                freq_locations.append((row, col))

    # find location of antinodes
    for a, b in itertools.combinations(freq_locations, 2):
        dist = (b[0] - a[0], b[1] - a[1])
        loc_anode1 = (a[0] - dist[0], a[1] - dist[1])
        while 0 <= loc_anode1[0] <= (len(map) - 1) and 0 <= loc_anode1[1] <= (len(map[0]) - 1):
            antinode_map[loc_anode1[0]][loc_anode1[1]] = '#'
            loc_anode1 = (loc_anode1[0] - dist[0], loc_anode1[1] - dist[1])

        loc_anode2 = (b[0] + dist[0], b[1] + dist[1])
        while 0 <= loc_anode2[0] <= (len(map) - 1) and 0<= loc_anode2[1] <= (len(map[0]) - 1):
            antinode_map[loc_anode2[0]][loc_anode2[1]] = '#'
            loc_anode2 = (loc_anode2[0] + dist[0], loc_anode2[1] + dist[1])

        loc_anode3 = (a[0] + dist[0], a[1] + dist[1])
        while 0 <= loc_anode3[0] <= (len(map) - 1) and 0 <= loc_anode3[1] <= (len(map[0]) - 1):
            antinode_map[loc_anode3[0]][loc_anode3[1]] = '#'
            loc_anode3 = (loc_anode3[0] + dist[0], loc_anode3[1] + dist[1])

        loc_anode4 = (b[0] - dist[0], b[1] - dist[1])
        while 0 <= loc_anode4[0] <= (len(map) - 1) and 0<= loc_anode4[1] <= (len(map[0]) - 1):
            antinode_map[loc_anode4[0]][loc_anode4[1]] = '#'
            loc_anode4 = (loc_anode4[0] - dist[0], loc_anode4[1] - dist[1])

result = 0
for r in antinode_map:
    result += r.count('#')


print(f"ANSWER = {result}")
