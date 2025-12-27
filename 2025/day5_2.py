file = open('input5.txt')
line = file.readline()

result = 0

fresh_ids = []

while line:
    line = line.strip('\n')
    if line == '':
        break
    limits = line.split('-')
    fresh_ids.append((int(limits[0]), int(limits[1])))
    line = file.readline()
file.close()

fresh_ids.sort()

filtered_ranges = []
for low, up in fresh_ids:
    if not filtered_ranges:
        filtered_ranges.append([low, up])
        continue
    flow, fup = filtered_ranges[-1]
    if low <= fup + 1:
        filtered_ranges[-1][1] = max(fup, up)
    else:
        filtered_ranges.append([low, up])

for l, u in filtered_ranges:
    result += u - l + 1

print(f"ANSWER = {result}")
