file = open('input11.txt')
line = file.readline()

result = 0
stones = []
blinks = 25

while line:
    line = line.strip('\n')
    stones = line.split(' ')
    line = file.readline()
file.close()

for i in range(blinks):
    new_stones = []
    for stone in stones:
        if stone == '0':
            new_stones.append('1')
        elif len(stone) % 2 == 0:
            mid = int(len(stone) / 2)
            new_stones.append(str(int(stone[:mid])))
            new_stones.append(str(int(stone[mid:])))
        else:
            new_stones.append(str(int(stone) * 2024))
    stones = new_stones.copy()
    new_stones.clear()

result = len(stones)

print(f"ANSWER = {result}")
