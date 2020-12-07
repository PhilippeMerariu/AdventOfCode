file = open('input3.txt')
line = file.readline().strip()
visited = ['0,0']
houseSanta = [0,0]
houseRobo = [0,0]
santaTurn = True

for char in line:
    if santaTurn:
        if char == '^':
            houseSanta[1] += 1
        elif char == '>':
            houseSanta[0] += 1
        elif char == '<':
            houseSanta[0] -= 1
        else:
            houseSanta[1] -= 1
        houseStr = str(houseSanta[0]) + ',' + str(houseSanta[1])
    else:
        if char == '^':
            houseRobo[1] += 1
        elif char == '>':
            houseRobo[0] += 1
        elif char == '<':
            houseRobo[0] -= 1
        else:
            houseRobo[1] -= 1
        houseStr = str(houseRobo[0]) + ',' + str(houseRobo[1])

    santaTurn = not(santaTurn)
    if houseStr not in visited:
        visited.append(houseStr)

print("Result: " + str(len(visited)))
file.close()
