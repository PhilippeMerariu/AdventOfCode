file = open('input3.txt')
line = file.readline().strip()
visited = ['0,0']
house = [0,0]

for char in line:
    if char == '^':
        house[1] += 1
    elif char == '>':
        house[0] += 1
    elif char == '<':
        house[0] -= 1
    else:
        house[1] -= 1

    houseStr = str(house[0]) + ',' + str(house[1])
    if houseStr not in visited:
        visited.append(houseStr)

print("Result: " + str(len(visited)))
file.close()
