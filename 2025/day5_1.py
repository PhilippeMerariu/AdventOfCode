file = open('input5.txt')
line = file.readline()

result = 0

fresh_ids = []
ingredients = []

get_ids = True
while line:
    line = line.strip('\n')
    if line == '':
        get_ids = False
    elif get_ids:
        limits = line.split('-')
        fresh_ids.append((int(limits[0]), int(limits[1])))
    else:
        ingredients.append(int(line))
    line = file.readline()
file.close()

for ing in ingredients:
    for low, up in fresh_ids:
        if low <= ing <= up:
            result += 1
            break

print(f"ANSWER = {result}")
