file = open('input2.txt')
line = file.readline()

result = 0

ranges = []

while line:
    line = line.strip('\n')
    ranges = line.split(',')
    line = file.readline()
file.close()

def is_valid(nb: int) -> bool:
    nb_str = str(nb)
    if len(nb_str) % 2 != 0:
        return True
    mid = len(nb_str) // 2
    part1 = nb_str[:mid]
    part2 = nb_str[mid:]
    if part1 == part2:
        return False
    return True

for r in ranges:
    first = int(r.split('-')[0])
    last = int(r.split('-')[1])
    for i in range(first, last + 1):
        if not is_valid(i):
            result += i

print(f"ANSWER = {result}")
