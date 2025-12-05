import re

file = open('input2.txt')
line = file.readline()

result = 0

ranges = []

while line:
    line = line.strip('\n')
    ranges = line.split(',')
    line = file.readline()
file.close()

def is_repeated(nb_str: str, pattern: str) -> bool:
    matches = re.findall(pattern, nb_str)
    return nb_str == ''.join(matches)

def is_valid(nb: int) -> bool:
    nb_str = str(nb)
    mid = len(nb_str) // 2
    for j in range(1, mid + 1):
        if len(nb_str) % j != 0:
            continue
        pattern = nb_str[:j]
        if is_repeated(nb_str, pattern):
            return False
    return True

for r in ranges:
    first = int(r.split('-')[0])
    last = int(r.split('-')[1])
    for i in range(first, last + 1):
        if not is_valid(i):
            result += i

print(f"ANSWER = {result}")
