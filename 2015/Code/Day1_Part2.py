file = open('input1.txt')
line = file.readline()
pos = 0
floor = 0

for char in line:
    if char == '(':
        floor += 1
    elif char == ')':
        floor -= 1

    pos += 1

    if floor == -1:
        break

print("result: " + str(pos))
file.close
